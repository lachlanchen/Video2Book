#!/usr/bin/env python3
"""Audit and revise transcript-derived lecture notes against their sources."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from string import Template
from typing import Iterable


MODULE_ROOT = Path(__file__).resolve().parents[1]
PROMPT_ROOT = Path(__file__).resolve().parent / "prompts" / "editorial_revision"
PROMPT_ACCESS_LEVELS = {"read-only", "workspace-write", "danger-full-access"}
TRANSCRIPT_SOURCE_RE = re.compile(r"^Source:\s*(.+)$", re.MULTILINE)
LECTURE_NUMBER_RE = re.compile(
    r"\bLectures?\s+(\d+)(?:\s*(?:&|and|[-\u2013\u2014,/])\s*(\d+))?\b",
    re.IGNORECASE,
)
CHAPTER_NUMBER_RE = re.compile(r"lecture_(\d+)(?:_(\d+))?$", re.IGNORECASE)
CHAPTER_TITLE_RE = re.compile(r"\\chapter\{([^{}]+)\}")
INCLUDEGRAPHICS_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^{}]+)\}")
REFERENCE_LECTURE_RE = re.compile(
    r"(?:^|[_ -])(?:lesson|lecture)[_ -]?(\d+(?:[_ -]\d+)*)$",
    re.IGNORECASE,
)

REFERENCE_STOPWORDS = {
    "about", "after", "again", "against", "almost", "also", "always", "among",
    "another", "because", "before", "being", "between", "could", "every", "first",
    "from", "have", "here", "into", "itself", "little", "maybe", "might", "other",
    "over", "really", "since", "still", "their", "there", "these", "thing", "think",
    "those", "through", "under", "until", "very", "what", "when", "where", "which",
    "while", "with", "would", "your", "just", "then", "than", "them", "they", "this",
    "that", "some", "more", "such", "like", "only", "each", "much", "many", "been",
    "were", "will", "does", "make", "made", "take",
}


SCAN_RULES = (
    (
        "internal_tooling",
        "error",
        re.compile(
            r"\b(?:Codex|ChatGPT|AI agent|language model|system prompt|user prompt|prompt instructions?)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "body_credit",
        "error",
        re.compile(r"\b(?:LazyingArt|Video2Book)\b", re.IGNORECASE),
    ),
    (
        "editorial_directive",
        "error",
        re.compile(
            r"\b(?:the notes|this chapter)\s+(?:should|must|need(?:s)?\s+to|will)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "production_language",
        "error",
        re.compile(
            r"\b(?:source of truth|board evidence|documentary evidence|transcript[- ]backed|"
            r"canonical reconstruction|cleaned form|production process|attached images?)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "conversation_leak",
        "error",
        re.compile(r"\b(?:the user asked|we were asked|your request|our conversation)\b", re.IGNORECASE),
    ),
    (
        "formulaic_choreography",
        "warning",
        re.compile(
            r"\bthe lecture\s+(?:begins|turns|pivots|pauses|unfolds|ends|returns|moves|"
            r"insists|announces|lingers)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "formulaic_payoff",
        "warning",
        re.compile(
            r"\b(?:the payoff|the order matters|the sequence matters|the story now|"
            r"the real lesson)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "legacy_qa_heading",
        "warning",
        re.compile(r"\\subsection\{Question\s+\\&\s+Answer\}"),
    ),
    (
        "forced_summary",
        "warning",
        re.compile(r"\\(?:section|section\*)\{(?:Summary|Chapter Summary|Closing Summary)\}", re.IGNORECASE),
    ),
)

BLOCKING_SCAN_RULES = {
    "formulaic_choreography",
    "formulaic_payoff",
    "legacy_qa_heading",
}


@dataclass
class ChapterRecord:
    course_rel: str
    course_root: Path
    chapter_dir: Path
    chapter_slug: str
    lecture_number: int
    lecture_numbers: tuple[int, ...]
    content_path: Path
    metadata_path: Path
    metadata: dict
    transcript_path: Path
    transcript_rel: str
    video_rel: str
    assets: list[Path]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_lecture_numbers(value: str) -> tuple[int, ...]:
    match = LECTURE_NUMBER_RE.search(value)
    if match:
        return tuple(int(number) for number in match.groups() if number)
    prefix = re.match(r"^(\d+)\s*-", value)
    return (int(prefix.group(1)),) if prefix else ()


def parse_lecture_number(value: str) -> int:
    numbers = parse_lecture_numbers(value)
    return numbers[0] if numbers else 0


def parse_json_text(text: str) -> dict:
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()[1:]
        while lines and lines[-1].strip().startswith("```"):
            lines.pop()
        stripped = "\n".join(lines).strip()
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start < 0 or end < start:
        raise ValueError("prompt output did not contain a JSON object")
    value = json.loads(stripped[start : end + 1])
    if not isinstance(value, dict):
        raise ValueError("prompt output JSON must be an object")
    return value


def canonical_json(value: object) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def read_template(name: str) -> Template:
    return Template(read_text(PROMPT_ROOT / name))


def editorial_charter() -> str:
    return read_text(PROMPT_ROOT / "editorial_charter.txt").strip()


def editable_prompt_access() -> bool:
    return os.environ.get("CODEX_PROMPT_ACCESS") in {
        "workspace-write",
        "danger-full-access",
    }


def candidate_delivery_instructions(candidate: Path) -> str:
    if not editable_prompt_access():
        return (
            "Do not edit repository files or run formatters or compilers. Return the complete "
            "candidate through your final response only; the outer driver owns all writes and "
            "validation."
        )
    return (
        "You have a sandboxed editable workspace. Save the complete raw LaTeX candidate to "
        f"`{candidate}` and do not modify any other file. Do not run formatters, compilers, git, "
        "or publishing commands. After saving, return a short confirmation; the outer driver "
        "will validate the saved candidate before promoting it to the chapter source."
    )


def run_codex_prompt(
    repo_root: Path,
    prompt: str,
    output_path: Path,
    runtime_dir: Path,
    log_prefix: str,
    model: str,
    reasoning: str,
    images: Iterable[Path] = (),
    direct_write: bool = False,
) -> None:
    runtime_dir.mkdir(parents=True, exist_ok=True)
    prompt_path = runtime_dir / f"{log_prefix}.prompt.txt"
    stdout_path = runtime_dir / f"{log_prefix}.stdout.log"
    stderr_path = runtime_dir / f"{log_prefix}.stderr.log"
    temp_output = runtime_dir / f"{log_prefix}.output.tmp"
    prompt_path.write_text(prompt, encoding="utf-8")
    command = [
        "bash",
        str(MODULE_ROOT / "scripts" / "codex_prompt_to_file.sh"),
        str(repo_root),
        str(prompt_path),
        str(temp_output),
        model,
        reasoning,
        *[str(path) for path in images if path.exists()],
    ]
    if direct_write:
        workspace = Path(os.environ.get("CODEX_PROMPT_WORKSPACE", runtime_dir)).resolve()
        try:
            output_path.resolve().relative_to(workspace)
        except ValueError as error:
            raise RuntimeError(
                f"editable Codex output must stay inside runtime workspace: {output_path}"
            ) from error
        output_path.unlink(missing_ok=True)

    last_error = ""
    for attempt in range(1, 4):
        temp_output.unlink(missing_ok=True)
        with stdout_path.open("w", encoding="utf-8") as stdout_handle, stderr_path.open(
            "w", encoding="utf-8"
        ) as stderr_handle:
            completed = subprocess.run(
                command,
                cwd=repo_root,
                text=True,
                stdin=subprocess.DEVNULL,
                stdout=stdout_handle,
                stderr=stderr_handle,
                check=False,
            )
        if completed.returncode == 0 and temp_output.exists():
            text = read_text(temp_output).strip()
            if text.startswith("```"):
                lines = text.splitlines()[1:]
                while lines and lines[-1].strip().startswith("```"):
                    lines.pop()
                text = "\n".join(lines).strip()
            if not direct_write or not output_path.exists() or not read_text(output_path).strip():
                output_path.write_text(text.rstrip() + "\n", encoding="utf-8")
            temp_output.unlink(missing_ok=True)
            return

        last_error = "\n".join(
            (read_text(stdout_path) + "\n" + read_text(stderr_path)).splitlines()[-50:]
        )
        transient = any(
            marker in last_error.lower()
            for marker in (
                "context window",
                "transport channel closed",
                "temporarily unavailable",
                "timed out",
                "connection reset",
                "bad gateway",
                "service unavailable",
            )
        )
        if attempt < 3 and transient:
            time.sleep(5 * attempt)
            continue
        break
    raise RuntimeError(f"Codex prompt failed for {log_prefix}:\n{last_error}")


def source_from_transcript(text: str) -> str:
    match = TRANSCRIPT_SOURCE_RE.search(text)
    return match.group(1).strip() if match else ""


def normalized_assets(metadata: dict, course_root: Path, content_text: str) -> tuple[list[dict], list[Path]]:
    records: list[dict] = []
    seen: set[str] = set()
    raw_assets = metadata.get("assets") or []
    if isinstance(raw_assets, list):
        for raw in raw_assets:
            if isinstance(raw, str):
                record = {"name": raw}
            elif isinstance(raw, dict):
                record = dict(raw)
            else:
                continue
            name = str(record.get("name") or record.get("asset") or "").strip()
            if not name or name in seen:
                continue
            record["name"] = name
            records.append(record)
            seen.add(name)

    for name in INCLUDEGRAPHICS_RE.findall(content_text):
        basename = Path(name).name
        if basename in seen or basename == "cover-art.png":
            continue
        records.append({"name": basename})
        seen.add(basename)

    paths: list[Path] = []
    for record in records:
        name = str(record["name"])
        candidates = (
            course_root / "figures" / name,
            course_root / "assets" / name,
            course_root / name,
        )
        match = next((path for path in candidates if path.exists()), None)
        if match:
            paths.append(match)
    return records, paths


def load_chapter(
    repo_root: Path,
    markdown_root: Path,
    output_root: Path,
    course_rel: str,
    chapter_dir: Path,
) -> ChapterRecord:
    content_path = chapter_dir / "content.tex"
    if not content_path.exists():
        raise RuntimeError(f"missing chapter source: {content_path}")
    content_text = read_text(content_path)
    metadata_path = chapter_dir / "metadata.json"
    metadata = json.loads(read_text(metadata_path)) if metadata_path.exists() else {}
    slug_match = CHAPTER_NUMBER_RE.search(chapter_dir.name)
    metadata_numbers = metadata.get("lecture_numbers") or []
    lecture_numbers = tuple(int(number) for number in metadata_numbers if int(number) > 0)
    if not lecture_numbers and slug_match:
        lecture_numbers = tuple(int(number) for number in slug_match.groups() if number)
    lecture_number = int(metadata.get("lecture_number") or (lecture_numbers[0] if lecture_numbers else 0))
    if not lecture_numbers and lecture_number > 0:
        lecture_numbers = (lecture_number,)
    if lecture_number <= 0:
        raise RuntimeError(f"cannot determine lecture number for {chapter_dir}")

    markdown_dir = markdown_root / course_rel
    transcript_rel_value = str(metadata.get("transcript_rel") or "")
    transcript_path = markdown_root / transcript_rel_value if transcript_rel_value else None
    if transcript_path is None or not transcript_path.exists():
        candidates = [
            path
            for path in sorted(markdown_dir.glob("*.md"))
            if lecture_number in parse_lecture_numbers(path.stem)
        ]
        if len(candidates) != 1:
            raise RuntimeError(
                f"expected one transcript for {course_rel}/{chapter_dir.name}, found {len(candidates)}"
            )
        transcript_path = candidates[0]
    transcript_rel = str(transcript_path.relative_to(markdown_root))
    transcript_text = read_text(transcript_path)
    video_rel = str(metadata.get("video_rel") or source_from_transcript(transcript_text))

    title_match = CHAPTER_TITLE_RE.search(content_text)
    metadata.update(
        {
            "schema_version": 2,
            "course_rel": course_rel,
            "transcript_rel": transcript_rel,
            "video_rel": video_rel,
            "lecture_number": lecture_number,
            "lecture_numbers": list(lecture_numbers),
            "lecture_slug": chapter_dir.name,
            "lecture_title": str(
                metadata.get("lecture_title")
                or (title_match.group(1) if title_match else f"Lecture {lecture_number}")
            ),
        }
    )
    asset_records, asset_paths = normalized_assets(metadata, output_root / course_rel, content_text)
    metadata["assets"] = asset_records
    return ChapterRecord(
        course_rel=course_rel,
        course_root=output_root / course_rel,
        chapter_dir=chapter_dir,
        chapter_slug=chapter_dir.name,
        lecture_number=lecture_number,
        lecture_numbers=lecture_numbers,
        content_path=content_path,
        metadata_path=metadata_path,
        metadata=metadata,
        transcript_path=transcript_path,
        transcript_rel=transcript_rel,
        video_rel=video_rel,
        assets=asset_paths,
    )


def scan_text(path: Path, text: str) -> list[dict]:
    findings: list[dict] = []
    for rule, severity, pattern in SCAN_RULES:
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            findings.append(
                {
                    "rule": rule,
                    "severity": severity,
                    "path": str(path),
                    "line": line,
                    "excerpt": match.group(0),
                }
            )

    qa_depth = 0
    for line_number, line in enumerate(text.splitlines(), 1):
        qa_depth += line.count(r"\begin{classroomqa}")
        if r"\lecturetimestamp{" in line and qa_depth == 0:
            findings.append(
                {
                    "rule": "misplaced_lecture_timestamp",
                    "severity": "error",
                    "path": str(path),
                    "line": line_number,
                    "excerpt": line.strip(),
                }
            )
        qa_depth = max(0, qa_depth - line.count(r"\end{classroomqa}"))
    return findings


def corpus_scan(output_root: Path, courses: list[str] | None = None) -> dict:
    content_paths: list[Path] = []
    if courses:
        for course_rel in courses:
            content_paths.extend(sorted((output_root / course_rel / "chapters").glob("*/content.tex")))
    else:
        content_paths = sorted(output_root.glob("*/*/*/chapters/*/content.tex"))

    findings: list[dict] = []
    chapter_titles: dict[str, list[str]] = {}
    course_roots: set[Path] = set()
    represented_transcripts: set[str] = set()
    metadata_missing = 0
    legacy_asset_records = 0
    incomplete_asset_records = 0
    for path in content_paths:
        text = read_text(path)
        findings.extend(scan_text(path.relative_to(output_root.parent), text))
        course_root = path.parents[2]
        course_roots.add(course_root)
        match = CHAPTER_TITLE_RE.search(text)
        if match:
            chapter_titles.setdefault(match.group(1).strip(), []).append(str(path.relative_to(output_root.parent)))
        metadata_path = path.parent / "metadata.json"
        if not metadata_path.exists():
            metadata_missing += 1
            findings.append(
                {
                    "rule": "missing_metadata",
                    "severity": "error",
                    "path": str(path.parent.relative_to(output_root.parent)),
                    "line": 1,
                    "excerpt": "metadata.json",
                }
            )
            continue
        try:
            metadata = json.loads(read_text(metadata_path))
        except json.JSONDecodeError:
            findings.append(
                {
                    "rule": "invalid_metadata",
                    "severity": "error",
                    "path": str(metadata_path.relative_to(output_root.parent)),
                    "line": 1,
                    "excerpt": "invalid JSON",
                }
            )
            continue
        transcript_rel = str(metadata.get("transcript_rel") or "")
        if transcript_rel:
            represented_transcripts.add(transcript_rel)
        for asset in metadata.get("assets") or []:
            if isinstance(asset, str):
                legacy_asset_records += 1
                findings.append(
                    {
                        "rule": "legacy_asset_metadata",
                        "severity": "warning",
                        "path": str(metadata_path.relative_to(output_root.parent)),
                        "line": 1,
                        "excerpt": asset,
                    }
                )
                continue
            if not isinstance(asset, dict):
                continue
            if not all(str(asset.get(key) or "").strip() for key in ("rationale", "caption_hint", "subtitle_excerpt")):
                incomplete_asset_records += 1
                findings.append(
                    {
                        "rule": "incomplete_asset_metadata",
                        "severity": "warning",
                        "path": str(metadata_path.relative_to(output_root.parent)),
                        "line": 1,
                        "excerpt": str(asset.get("name") or "unnamed asset"),
                    }
                )

    for course_root in sorted(course_roots):
        course_tex = course_root / "course.tex"
        if not course_tex.exists():
            continue
        course_text = read_text(course_tex)
        relative = str(course_tex.relative_to(output_root.parent))
        if r"\begin{titlepage}" in course_text and r"\maketitle" in course_text:
            findings.append(
                {
                    "rule": "duplicate_title_page",
                    "severity": "error",
                    "path": relative,
                    "line": course_text.count("\n", 0, course_text.find(r"\maketitle")) + 1,
                    "excerpt": r"titlepage + \maketitle",
                }
            )
        if r"\author{Leonard Susskind}" in course_text:
            findings.append(
                {
                    "rule": "ambiguous_authorship",
                    "severity": "error",
                    "path": relative,
                    "line": course_text.count("\n", 0, course_text.find(r"\author{Leonard Susskind}")) + 1,
                    "excerpt": r"\author{Leonard Susskind}",
                }
            )
        if "About These Notes" not in course_text:
            findings.append(
                {
                    "rule": "missing_editorial_statement",
                    "severity": "warning",
                    "path": relative,
                    "line": 1,
                    "excerpt": "About These Notes",
                }
            )

    duplicates = {
        title: paths for title, paths in chapter_titles.items() if len(paths) > 1
    }
    by_rule: dict[str, int] = {}
    by_severity: dict[str, int] = {}
    for finding in findings:
        by_rule[finding["rule"]] = by_rule.get(finding["rule"], 0) + 1
        by_severity[finding["severity"]] = by_severity.get(finding["severity"], 0) + 1
    markdown_root = output_root.parent / "markdown"
    transcript_paths = sorted(markdown_root.rglob("*.md")) if markdown_root.exists() else []
    transcript_rels = {str(path.relative_to(markdown_root)) for path in transcript_paths}
    uncovered_transcripts = sorted(transcript_rels - represented_transcripts)
    return {
        "schema_version": 1,
        "courses_scanned": len(course_roots),
        "chapters_scanned": len(content_paths),
        "findings_total": len(findings),
        "counts_by_severity": by_severity,
        "counts_by_rule": by_rule,
        "duplicate_chapter_titles": duplicates,
        "coverage": {
            "transcripts_total": len(transcript_rels),
            "transcripts_represented_by_metadata": len(transcript_rels & represented_transcripts),
            "transcripts_not_represented": uncovered_transcripts,
            "chapters_missing_metadata": metadata_missing,
            "legacy_asset_records": legacy_asset_records,
            "incomplete_asset_records": incomplete_asset_records,
        },
        "findings": findings,
    }


def scan_report_markdown(report: dict) -> str:
    lines = [
        "# Editorial Corpus Scan",
        "",
        f"- Chapters scanned: {report['chapters_scanned']}",
        f"- Courses scanned: {report.get('courses_scanned', 0)}",
        f"- Findings: {report['findings_total']}",
        f"- Errors: {report['counts_by_severity'].get('error', 0)}",
        f"- Warnings: {report['counts_by_severity'].get('warning', 0)}",
        "",
        "## Findings By Rule",
        "",
        "| Rule | Count |",
        "| --- | ---: |",
    ]
    for rule, count in sorted(report["counts_by_rule"].items()):
        lines.append(f"| `{rule}` | {count} |")
    lines.extend(["", "## Duplicate Chapter Titles", ""])
    if report["duplicate_chapter_titles"]:
        for title, paths in sorted(report["duplicate_chapter_titles"].items()):
            lines.append(f"- **{title}**: {len(paths)} chapters")
    else:
        lines.append("No duplicate chapter titles detected.")
    coverage = report.get("coverage") or {}
    lines.extend(
        [
            "",
            "## Coverage And Metadata",
            "",
            f"- Transcripts: {coverage.get('transcripts_total', 0)}",
            f"- Unrepresented transcripts: {len(coverage.get('transcripts_not_represented') or [])}",
            f"- Chapters missing metadata: {coverage.get('chapters_missing_metadata', 0)}",
            f"- Legacy asset records: {coverage.get('legacy_asset_records', 0)}",
            f"- Incomplete asset records: {coverage.get('incomplete_asset_records', 0)}",
        ]
    )
    return "\n".join(lines) + "\n"


def reference_lecture_numbers(path: Path) -> tuple[int, ...]:
    match = REFERENCE_LECTURE_RE.search(path.stem)
    if not match:
        return ()
    return tuple(int(number) for number in re.findall(r"\d+", match.group(1)))


def reference_pdf_candidates(
    reference_paths: list[Path], lecture_number: int
) -> list[Path]:
    explicit_files: list[Path] = []
    direct_lessons: list[Path] = []
    direct_lectures: list[Path] = []
    nested_lessons: list[Path] = []
    nested_lectures: list[Path] = []
    fallback: list[Path] = []
    for path in reference_paths:
        resolved = path.expanduser().resolve()
        if resolved.is_file() and resolved.suffix.lower() == ".pdf":
            explicit_files.append(resolved)
        elif resolved.is_dir():
            for candidate in sorted(resolved.rglob("*.pdf")):
                direct = candidate.parent == resolved
                numbers = reference_lecture_numbers(candidate)
                kind_match = re.search(r"(?:^|[_ -])(lesson|lecture)", candidate.stem, re.IGNORECASE)
                kind = kind_match.group(1).lower() if kind_match else ""
                if lecture_number in numbers and kind == "lesson":
                    (direct_lessons if direct else nested_lessons).append(candidate)
                elif lecture_number in numbers and kind == "lecture":
                    (direct_lectures if direct else nested_lectures).append(candidate)
                elif direct and not numbers:
                    fallback.append(candidate)

    for group in (
        explicit_files,
        direct_lessons,
        direct_lectures,
        nested_lessons,
        nested_lectures,
        fallback,
    ):
        if group:
            return list(dict.fromkeys(group))[:2]
    return []


def extract_pdf_text(path: Path) -> str:
    if shutil.which("pdftotext") is None:
        return ""
    completed = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return completed.stdout if completed.returncode == 0 else ""


def reference_query_terms(record: ChapterRecord) -> list[str]:
    title = str(record.metadata.get("lecture_title") or "")
    source = f"{title}\n{read_text(record.transcript_path)}".lower()
    title_terms = re.findall(r"[a-z]{4,}", title.lower())
    counts = Counter(
        token
        for token in re.findall(r"[a-z]{4,}", source)
        if token not in REFERENCE_STOPWORDS
    )
    terms: list[str] = []
    for term in title_terms + [token for token, _count in counts.most_common(24)]:
        if term not in terms:
            terms.append(term)
    return terms[:28]


def reference_paragraphs(text: str) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        current.append(line)
    if current:
        paragraphs.append(" ".join(current))
    return [
        re.sub(r"\s+", " ", paragraph).strip()
        for paragraph in paragraphs
        if len(paragraph) > 120
    ]


def topical_reference_excerpt(path: Path, text: str, record: ChapterRecord, limit: int) -> str:
    terms = reference_query_terms(record)
    ranked: list[tuple[int, int, str]] = []
    for index, paragraph in enumerate(reference_paragraphs(text)):
        lowered = paragraph.lower()
        score = sum(lowered.count(term) for term in terms)
        if score > 0:
            ranked.append((score, -index, paragraph))
    ranked.sort(reverse=True)
    selected: list[str] = []
    used = 0
    for _score, _index, paragraph in ranked:
        item = f"REFERENCE: {path}\n{paragraph}"
        if used + len(item) > limit:
            continue
        selected.append(item)
        used += len(item)
        if len(selected) >= 8:
            break
    return "\n\n".join(selected)


def collect_reference_text(
    reference_paths: list[Path], record: ChapterRecord, char_limit: int
) -> str:
    if not reference_paths:
        return "No external reference was supplied."
    chunks: list[str] = []
    remaining = char_limit
    for path in reference_pdf_candidates(reference_paths, record.lecture_number):
        if remaining <= 0:
            break
        pdf_text = extract_pdf_text(path).strip()
        if not pdf_text:
            continue
        if record.lecture_number in reference_lecture_numbers(path):
            excerpt = f"REFERENCE: {path}\n{pdf_text[:remaining]}"
        else:
            excerpt = topical_reference_excerpt(path, pdf_text, record, min(remaining, 12_000))
        if excerpt:
            chunks.append(excerpt)
            remaining -= len(excerpt)
    return "\n\n".join(chunks) or "Supplied references could not be converted to text."


def markdown_audit(audit: dict) -> str:
    lines = [
        "# Editorial Audit",
        "",
        f"- Status: **{audit.get('overall_status', 'unknown')}**",
        f"- Findings: {len(audit.get('findings') or [])}",
        "",
        "## Findings",
        "",
    ]
    findings = audit.get("findings") or []
    if not findings:
        lines.append("No editorial findings were reported.")
    for finding in findings:
        lines.append(
            f"- **{finding.get('severity', 'unknown')} / {finding.get('category', 'other')}** "
            f"at `{finding.get('locator', 'unspecified')}`: {finding.get('evidence', '')} "
            f"Repair: {finding.get('action', '')}"
        )
    lines.extend(["", "## Source Uncertainties", ""])
    uncertainties = audit.get("uncertain_sources") or []
    if not uncertainties:
        lines.append("No unresolved source uncertainty was reported.")
    for item in uncertainties:
        lines.append(
            f"- `{item.get('locator', 'unspecified')}`: {item.get('problem', '')} "
            f"Check: {item.get('required_check', '')}"
        )
    return "\n".join(lines) + "\n"


def ensure_editorial_preamble(path: Path) -> bool:
    text = read_text(path)
    marker = "% Video2Book editorial provenance macros"
    if marker in text:
        if r"\newcommand{\lectureframe}" in text:
            return False
        path.write_text(
            text.rstrip()
            + "\n"
            + r"\newcommand{\lectureframe}[1]{\par\smallskip{\centering\footnotesize\itshape Lecture frame: #1.\par}}"
            + "\n",
            encoding="utf-8",
        )
        return True
    block = r"""

% Video2Book editorial provenance macros
\newenvironment{classroomqa}{%
  \par\medskip\noindent\begin{minipage}{\linewidth}\small\hrule\medskip
}{%
  \medskip\hrule\end{minipage}\par\medskip
}
\newcommand{\audiencequestion}[1]{\noindent\textbf{Question from the audience.} #1\par\smallskip}
\newcommand{\lecturerresponse}[1]{\noindent\textbf{Response.} #1\par}
\newcommand{\lecturetimestamp}[1]{\footnote{Lecture timestamp: #1.}}
\newcommand{\lectureframe}[1]{\par\smallskip{\centering\footnotesize\itshape Lecture frame: #1.\par}}
\newcommand{\editorialnote}[1]{\footnote{Editorial clarification: #1}}
"""
    path.write_text(text.rstrip() + block.rstrip() + "\n", encoding="utf-8")
    return True


def normalize_course_front_matter(path: Path) -> bool:
    text = read_text(path)
    original = text
    text = text.replace("Leonard Susskind lecture notes", "Lectures by Leonard Susskind")
    cover_lines: list[str] = []
    for line in text.splitlines():
        if (
            r"\small\color{black!72}" in line
            and "LazyingArt" in line
            and "Video2Book" in line
        ):
            indent = line[: len(line) - len(line.lstrip())]
            line = (
                indent
                + r"{\small\color{black!72} Companion edition by "
                + r"\href{https://lazying.art}{LazyingArt LLC} with "
                + r"\href{https://github.com/lachlanchen/Video2Book}{Video2Book}}"
            )
        cover_lines.append(line)
    text = "\n".join(cover_lines) + ("\n" if text.endswith("\n") else "")
    anchor = text.find(r"\hypersetup{pageanchor=true}")
    toc = text.find(r"\tableofcontents", anchor if anchor >= 0 else 0)
    if anchor >= 0 and toc > anchor:
        anchor_end = anchor + len(r"\hypersetup{pageanchor=true}")
        about = r"""

\clearpage
\chapter*{About These Notes}
These independently edited companion notes follow lectures by Leonard Susskind. They were reconstructed from machine transcripts, subtitles, and selected blackboard frames, then checked against the available source material. They are not an original manuscript by Professor Susskind and have not been reviewed or endorsed by him.

The edition was prepared by \href{https://lazying.art}{LazyingArt LLC} using the open-source \href{https://github.com/lachlanchen/Video2Book}{Video2Book} workflow. Machine transcripts remain available separately and may contain recognition errors. Editorial clarifications and nontrivial reconstructions are identified in footnotes.
\clearpage
"""
        text = text[:anchor_end] + about + text[toc:]
    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def normalize_lecture_wrapper(path: Path) -> bool:
    if not path.exists():
        return False
    text = read_text(path)
    original = text
    lines: list[str] = []
    inside_credit = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == r"\begin{center}":
            inside_credit = True
            continue
        if inside_credit:
            if stripped == r"\end{center}":
                inside_credit = False
            continue
        if stripped.startswith(r"\author{"):
            line = r"\author{Lecture by Leonard Susskind\\Edited companion notes by LazyingArt LLC}"
        elif stripped.startswith(r"\date{"):
            line = r"\date{AI-assisted companion edition prepared with Video2Book}"
        lines.append(line)
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    if text == original:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def validate_tex(text: str) -> list[str]:
    errors: list[str] = []
    if not text.lstrip().startswith(r"\chapter{"):
        errors.append("chapter must begin with \\chapter{...}")
    for marker in (r"\documentclass", r"\begin{document}", r"\end{document}"):
        if marker in text:
            errors.append(f"chapter contains forbidden document wrapper: {marker}")
    if text.count(r"\begin{classroomqa}") != text.count(r"\end{classroomqa}"):
        errors.append("classroomqa environments are unbalanced")
    return errors


def compile_tex(tex_path: Path, build_dir: Path, passes: int = 2) -> tuple[bool, str, Path | None]:
    if shutil.which("pdflatex") is None:
        return False, "pdflatex is not installed", None
    build_dir.mkdir(parents=True, exist_ok=True)
    log_path = build_dir / f"{tex_path.stem}.driver.log"
    with log_path.open("w", encoding="utf-8") as log:
        for _ in range(passes):
            completed = subprocess.run(
                [
                    "pdflatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-file-line-error",
                    f"-output-directory={build_dir}",
                    tex_path.name,
                ],
                cwd=tex_path.parent,
                stdout=log,
                stderr=subprocess.STDOUT,
                check=False,
            )
            if completed.returncode != 0:
                return False, "\n".join(read_text(log_path).splitlines()[-100:]), None
    pdf = build_dir / f"{tex_path.stem}.pdf"
    return pdf.exists(), read_text(log_path), pdf if pdf.exists() else None


def prompt_json(
    repo_root: Path,
    prompt: str,
    runtime_dir: Path,
    prefix: str,
    model: str,
    reasoning: str,
    images: list[Path],
) -> dict:
    output = runtime_dir / f"{prefix}.raw.json"
    run_codex_prompt(repo_root, prompt, output, runtime_dir, prefix, model, reasoning, images)
    try:
        parsed = parse_json_text(read_text(output))
    except (ValueError, json.JSONDecodeError):
        repair_prompt = read_template("editorial_json_repair_prompt.txt").substitute(
            schema_description="Return the same object requested by the immediately preceding editorial task.",
            failed_output=read_text(output),
        )
        repaired_output = runtime_dir / f"{prefix}.repaired.json"
        run_codex_prompt(
            repo_root,
            repair_prompt,
            repaired_output,
            runtime_dir,
            f"{prefix}_json_repair",
            model,
            reasoning,
        )
        parsed = parse_json_text(read_text(repaired_output))
    output.write_text(canonical_json(parsed), encoding="utf-8")
    return parsed


def session_boundary(
    repo_root: Path,
    course_rel: str,
    runtime_dir: Path,
    model: str,
    reasoning: str,
) -> None:
    prompt = read_template("editorial_course_boundary_prompt.txt").substitute(
        editorial_charter=editorial_charter(),
        course_rel=course_rel,
        boundary_access=(
            "The session has a sandboxed editable workspace for later chapter candidates. "
            "Do not write files or run commands during this course-boundary acknowledgement."
            if editable_prompt_access()
            else "Do not edit repository files or run commands. This is a read-only writer session."
        ),
    )
    output = runtime_dir / "course_boundary.txt"
    run_codex_prompt(repo_root, prompt, output, runtime_dir, "course_boundary", model, reasoning)
    expected = f"EDITORIAL COURSE READY: {course_rel}"
    if expected not in read_text(output):
        raise RuntimeError("writer session did not acknowledge the editorial course boundary")


def audit_chapter(
    record: ChapterRecord,
    repo_root: Path,
    runtime_dir: Path,
    reference_text: str,
    model: str,
    reasoning: str,
) -> dict:
    figures_notes = record.chapter_dir / "figures_markdown.md"
    prompt = read_template("editorial_audit_prompt.txt").substitute(
        editorial_charter=editorial_charter(),
        course_rel=record.course_rel,
        chapter_slug=record.chapter_slug,
        transcript_rel=record.transcript_rel,
        video_rel=record.video_rel,
        metadata_json=canonical_json(record.metadata),
        figures_markdown_text=read_text(figures_notes) if figures_notes.exists() else "No figure notes.",
        reference_text=reference_text,
        content_tex=read_text(record.content_path),
        transcript_text=read_text(record.transcript_path),
    )
    audit = prompt_json(repo_root, prompt, runtime_dir, "editorial_audit", model, reasoning, record.assets)
    if not isinstance(audit.get("findings", []), list):
        raise RuntimeError("editorial audit returned an invalid findings list")
    return audit


def rewrite_chapter(
    record: ChapterRecord,
    repo_root: Path,
    runtime_dir: Path,
    audit: dict,
    reference_text: str,
    model: str,
    reasoning: str,
) -> Path:
    candidate = runtime_dir / "content.revised.tex"
    prompt = read_template("editorial_rewrite_prompt.txt").substitute(
        editorial_charter=editorial_charter(),
        course_rel=record.course_rel,
        chapter_slug=record.chapter_slug,
        transcript_rel=record.transcript_rel,
        video_rel=record.video_rel,
        asset_names=", ".join(path.name for path in record.assets) or "none",
        audit_json=canonical_json(audit),
        metadata_json=canonical_json(record.metadata),
        reference_text=reference_text,
        content_tex=read_text(record.content_path),
        transcript_text=read_text(record.transcript_path),
        delivery_instructions=candidate_delivery_instructions(candidate),
    )
    run_codex_prompt(
        repo_root,
        prompt,
        candidate,
        runtime_dir,
        "editorial_rewrite",
        model,
        reasoning,
        record.assets,
        direct_write=editable_prompt_access(),
    )
    errors = validate_tex(read_text(candidate))
    if errors:
        raise RuntimeError("invalid revised chapter: " + "; ".join(errors))
    return candidate


def fidelity_review(
    record: ChapterRecord,
    repo_root: Path,
    runtime_dir: Path,
    candidate: Path,
    reference_text: str,
    model: str,
    reasoning: str,
    prefix: str,
) -> dict:
    prompt = read_template("editorial_fidelity_prompt.txt").substitute(
        editorial_charter=editorial_charter(),
        course_rel=record.course_rel,
        chapter_slug=record.chapter_slug,
        transcript_rel=record.transcript_rel,
        video_rel=record.video_rel,
        metadata_json=canonical_json(record.metadata),
        reference_text=reference_text,
        revised_tex=read_text(candidate),
        transcript_text=read_text(record.transcript_path),
    )
    report = prompt_json(repo_root, prompt, runtime_dir, prefix, model, reasoning, record.assets)
    if report.get("status") not in {"pass", "revise"}:
        raise RuntimeError("fidelity review returned an invalid status")
    if not isinstance(report.get("source_map", []), list):
        raise RuntimeError("fidelity review returned an invalid source map")
    return report


def repair_chapter(
    record: ChapterRecord,
    repo_root: Path,
    runtime_dir: Path,
    candidate: Path,
    fidelity: dict,
    reference_text: str,
    model: str,
    reasoning: str,
    pass_number: int,
) -> Path:
    repaired = runtime_dir / f"content.repaired.{pass_number}.tex"
    prompt = read_template("editorial_repair_prompt.txt").substitute(
        editorial_charter=editorial_charter(),
        course_rel=record.course_rel,
        chapter_slug=record.chapter_slug,
        transcript_rel=record.transcript_rel,
        video_rel=record.video_rel,
        asset_names=", ".join(path.name for path in record.assets) or "none",
        fidelity_json=canonical_json(fidelity),
        metadata_json=canonical_json(record.metadata),
        reference_text=reference_text,
        revised_tex=read_text(candidate),
        transcript_text=read_text(record.transcript_path),
        delivery_instructions=candidate_delivery_instructions(repaired),
    )
    run_codex_prompt(
        repo_root,
        prompt,
        repaired,
        runtime_dir,
        f"editorial_repair_{pass_number}",
        model,
        reasoning,
        record.assets,
        direct_write=editable_prompt_access(),
    )
    errors = validate_tex(read_text(repaired))
    if errors:
        raise RuntimeError("invalid repaired chapter: " + "; ".join(errors))
    return repaired


def hard_scan_passes(candidate: Path) -> tuple[bool, list[dict]]:
    findings = scan_text(candidate, read_text(candidate))
    blocked = any(
        item["severity"] == "error" or item["rule"] in BLOCKING_SCAN_RULES
        for item in findings
    )
    return not blocked, findings


def fidelity_passes(candidate: Path, report: dict) -> tuple[bool, list[str]]:
    problems: list[str] = []
    if report.get("status") != "pass":
        problems.append("critic status is not pass")
    for field in ("unsupported_claims", "missing_beats", "style_violations", "provenance_gaps"):
        if report.get(field):
            problems.append(f"{field} is not empty")
    source_map = report.get("source_map") or []
    if not source_map:
        problems.append("source_map is empty")

    text = read_text(candidate)
    included_assets = [Path(name).name for name in INCLUDEGRAPHICS_RE.findall(text)]
    source_map_text = canonical_json(source_map)
    for asset in included_assets:
        if asset not in source_map_text:
            problems.append(f"included figure is absent from source_map: {asset}")

    qa_count = text.count(r"\begin{classroomqa}")
    qa_checks = report.get("q_and_a_checks") or []
    verified_qa = [item for item in qa_checks if isinstance(item, dict) and item.get("verified") is True]
    if len(verified_qa) < qa_count:
        problems.append(
            f"only {len(verified_qa)} of {qa_count} classroom Q&A blocks are verified"
        )
    if any(
        isinstance(item, dict)
        and Path(str(item.get("asset") or "")).name in included_assets
        and item.get("verdict") not in {None, "keep"}
        for item in (report.get("figure_checks") or [])
    ):
        problems.append("figure review still requests replacement or removal")
    return not problems, problems


def complete_verified_qa_source_map(record: ChapterRecord, report: dict) -> None:
    source_map = report.setdefault("source_map", [])
    mapped_timestamps = {
        str(timestamp)
        for entry in source_map
        if isinstance(entry, dict) and entry.get("kind") == "q_and_a"
        for timestamp in (entry.get("timestamps") or [])
    }
    for check in report.get("q_and_a_checks") or []:
        if not isinstance(check, dict) or check.get("verified") is not True:
            continue
        timestamp = str(check.get("timestamp") or "").strip()
        if not timestamp or timestamp in mapped_timestamps:
            continue
        source_map.append(
            {
                "locator": str(check.get("locator") or "Verified classroom exchange"),
                "kind": "q_and_a",
                "source_type": "transcript",
                "timestamps": [timestamp],
                "reference": record.transcript_rel,
                "confidence": "high",
                "note": str(check.get("reason") or "Verified against the timestamped transcript."),
            }
        )
        mapped_timestamps.add(timestamp)


def process_chapter(
    record: ChapterRecord,
    repo_root: Path,
    runtime_root: Path,
    reference_paths: list[Path],
    reference_char_limit: int,
    model: str,
    reasoning: str,
    audit_only: bool,
    rewrite: bool,
    max_repair_passes: int,
    compile_enabled: bool,
    resume: bool,
    force: bool,
) -> str:
    runtime_dir = runtime_root / record.course_rel / record.chapter_slug
    runtime_dir.mkdir(parents=True, exist_ok=True)
    state_path = runtime_dir / "state.json"
    current_hash = sha256_text(read_text(record.content_path))
    if resume and not force and state_path.exists():
        state = json.loads(read_text(state_path))
        if state.get("status") == "complete" and state.get("content_sha256") == current_hash:
            return "skipped"

    reference_text = collect_reference_text(
        reference_paths, record, reference_char_limit
    )
    audit_artifact = runtime_dir / "editorial_audit.raw.json"
    if resume and not force and audit_artifact.exists():
        audit = parse_json_text(read_text(audit_artifact))
    else:
        audit = audit_chapter(record, repo_root, runtime_dir, reference_text, model, reasoning)
    if audit_only and not rewrite:
        record.chapter_dir.joinpath("editorial_audit.json").write_text(canonical_json(audit), encoding="utf-8")
        record.chapter_dir.joinpath("editorial_audit.md").write_text(markdown_audit(audit), encoding="utf-8")
        return "audited"

    candidate_artifact = runtime_dir / "content.revised.tex"
    if resume and not force and candidate_artifact.exists() and not validate_tex(read_text(candidate_artifact)):
        candidate = candidate_artifact
    else:
        candidate = rewrite_chapter(
            record, repo_root, runtime_dir, audit, reference_text, model, reasoning
        )
    final_fidelity: dict | None = None
    final_scan: list[dict] = []
    for pass_number in range(max_repair_passes + 1):
        scan_ok, final_scan = hard_scan_passes(candidate)
        fidelity = fidelity_review(
            record,
            repo_root,
            runtime_dir,
            candidate,
            reference_text,
            model,
            reasoning,
            f"editorial_fidelity_{pass_number}",
        )
        complete_verified_qa_source_map(record, fidelity)
        fidelity_ok, fidelity_problems = fidelity_passes(candidate, fidelity)
        if scan_ok and fidelity_ok:
            final_fidelity = fidelity
            break
        if pass_number >= max_repair_passes:
            break
        if not scan_ok:
            fidelity.setdefault("style_violations", []).extend(
                {
                    "locator": f"line {item['line']}",
                    "problem": f"deterministic {item['rule']} violation: {item['excerpt']}",
                    "repair": "remove the internal or production-oriented language",
                }
                for item in final_scan
                if item["severity"] == "error" or item["rule"] in BLOCKING_SCAN_RULES
            )
            fidelity["status"] = "revise"
        if not fidelity_ok:
            fidelity.setdefault("style_violations", []).extend(
                {
                    "locator": "editorial gate",
                    "problem": problem,
                    "repair": "repair the chapter or provenance report so this gate is satisfied",
                }
                for problem in fidelity_problems
            )
            fidelity["status"] = "revise"
        candidate = repair_chapter(
            record,
            repo_root,
            runtime_dir,
            candidate,
            fidelity,
            reference_text,
            model,
            reasoning,
            pass_number + 1,
        )

    if final_fidelity is None:
        backup = runtime_dir / "content.before.tex"
        if backup.exists():
            record.content_path.write_text(read_text(backup), encoding="utf-8")
        pdf_backup = runtime_dir / "lecture.before.pdf"
        if pdf_backup.exists():
            shutil.copy2(pdf_backup, record.chapter_dir / "lecture.pdf")
        state_path.write_text(
            canonical_json(
                {
                    "status": "blocked",
                    "reason": "fidelity or deterministic scan did not pass",
                    "scan_findings": final_scan,
                }
            ),
            encoding="utf-8",
        )
        raise RuntimeError(f"editorial gates did not pass for {record.course_rel}/{record.chapter_slug}")

    backup = runtime_dir / "content.before.tex"
    if not backup.exists():
        backup.write_text(read_text(record.content_path), encoding="utf-8")
    original = read_text(backup)
    pdf_backup = runtime_dir / "lecture.before.pdf"
    if not pdf_backup.exists() and (record.chapter_dir / "lecture.pdf").exists():
        shutil.copy2(record.chapter_dir / "lecture.pdf", pdf_backup)
    record.content_path.write_text(read_text(candidate), encoding="utf-8")
    record.metadata_path.write_text(canonical_json(record.metadata), encoding="utf-8")
    normalize_lecture_wrapper(record.chapter_dir / "lecture.tex")

    try:
        if compile_enabled:
            ok, log, pdf = compile_tex(
                record.chapter_dir / "lecture.tex",
                runtime_dir / "build",
            )
            if not ok or pdf is None:
                raise RuntimeError(f"chapter compile failed:\n{log}")
            shutil.copy2(pdf, record.chapter_dir / "lecture.pdf")
    except Exception:
        record.content_path.write_text(original, encoding="utf-8")
        if pdf_backup.exists():
            shutil.copy2(pdf_backup, record.chapter_dir / "lecture.pdf")
        raise

    record.chapter_dir.joinpath("editorial_audit.json").write_text(canonical_json(audit), encoding="utf-8")
    record.chapter_dir.joinpath("editorial_audit.md").write_text(markdown_audit(audit), encoding="utf-8")
    record.chapter_dir.joinpath("editorial_fidelity.json").write_text(
        canonical_json(final_fidelity), encoding="utf-8"
    )
    record.chapter_dir.joinpath("source_map.json").write_text(
        canonical_json(
            {
                "schema_version": 1,
                "course_rel": record.course_rel,
                "chapter": record.chapter_slug,
                "transcript_rel": record.transcript_rel,
                "video_rel": record.video_rel,
                "entries": final_fidelity.get("source_map", []),
            }
        ),
        encoding="utf-8",
    )
    state_path.write_text(
        canonical_json(
            {
                "status": "complete",
                "content_sha256": sha256_text(read_text(record.content_path)),
                "transcript_sha256": sha256_text(read_text(record.transcript_path)),
                "model": model,
                "reasoning": reasoning,
            }
        ),
        encoding="utf-8",
    )
    return "revised"


def selected_courses(output_root: Path, requested: list[str], all_courses: bool) -> list[str]:
    if requested:
        return requested
    if not all_courses:
        return []
    return [
        str(path.relative_to(output_root))
        for path in sorted(output_root.glob("*/*/*"))
        if (path / "chapters").is_dir()
    ]


def chapter_dirs(course_root: Path, requested: list[str]) -> list[Path]:
    if requested:
        result = [course_root / "chapters" / item for item in requested]
    else:
        result = sorted((course_root / "chapters").glob("lecture_*"))
    return [path for path in result if (path / "content.tex").exists()]


def prepare_environment(args: argparse.Namespace) -> tuple[Path, Path, Path, Path]:
    repo_root = args.repo_root.resolve()
    markdown_root = (args.markdown_root or repo_root / "markdown").resolve()
    output_root = (args.output_root or repo_root / "generated_course_notes").resolve()
    runtime_root = (args.runtime_root or repo_root / ".editorial-revision-work").resolve()
    runtime_root.mkdir(parents=True, exist_ok=True)
    prompt_access = getattr(args, "prompt_access", "read-only")
    if prompt_access not in PROMPT_ACCESS_LEVELS:
        raise ValueError(f"unsupported Codex prompt access: {prompt_access}")
    session_stem = {
        "read-only": "writer",
        "workspace-write": "writer.editable",
        "danger-full-access": "writer.editable-full",
    }[prompt_access]
    session_file = (args.session_file or runtime_root / f"{session_stem}.session_id").resolve()
    session_doc = (args.session_doc or runtime_root / f"{session_stem}.session.md").resolve()
    os.environ["CODEX_SHARED_SESSION_FILE"] = str(session_file)
    os.environ["CODEX_SHARED_SESSION_DOC_FILE"] = str(session_doc)
    os.environ["NOTE_CODEX_SESSION_SCOPE"] = "global"
    os.environ["CODEX_PROMPT_ACCESS"] = prompt_access
    os.environ["CODEX_PROMPT_WORKSPACE"] = (
        str(repo_root) if prompt_access == "read-only" else str(runtime_root)
    )
    os.environ.setdefault("NOTE_TMUX_SESSION_NAME", "susskind-editorial")
    return repo_root, markdown_root, output_root, runtime_root


def parser() -> argparse.ArgumentParser:
    parsed = argparse.ArgumentParser(
        description="Audit and revise transcript-derived TeX course notes with source provenance."
    )
    parsed.add_argument("--repo-root", type=Path, default=Path.cwd())
    parsed.add_argument("--markdown-root", type=Path)
    parsed.add_argument("--output-root", type=Path)
    parsed.add_argument("--runtime-root", type=Path)
    parsed.add_argument("--session-file", type=Path)
    parsed.add_argument("--session-doc", type=Path)
    parsed.add_argument(
        "--prompt-access",
        default="read-only",
        choices=sorted(PROMPT_ACCESS_LEVELS),
        help="Codex sandbox for the persistent writer session.",
    )
    parsed.add_argument("--course", action="append", default=[])
    parsed.add_argument("--all-courses", action="store_true")
    parsed.add_argument("--chapter", action="append", default=[])
    parsed.add_argument("--reference", action="append", type=Path, default=[])
    parsed.add_argument("--reference-char-limit", type=int, default=50_000)
    parsed.add_argument("--scan-only", action="store_true")
    parsed.add_argument("--scan-report", type=Path)
    parsed.add_argument("--audit-only", action="store_true")
    parsed.add_argument("--rewrite", action="store_true")
    parsed.add_argument("--model", default="gpt-5.4")
    parsed.add_argument(
        "--reasoning",
        default="xhigh",
        choices=["low", "medium", "high", "xhigh", "ultra"],
    )
    parsed.add_argument("--max-repair-passes", type=int, default=2)
    parsed.add_argument("--resume", action="store_true")
    parsed.add_argument("--force", action="store_true")
    parsed.add_argument("--no-compile", action="store_true")
    return parsed


def main() -> int:
    args = parser().parse_args()
    repo_root, markdown_root, output_root, runtime_root = prepare_environment(args)
    courses = selected_courses(output_root, args.course, args.all_courses)

    if args.scan_only:
        report = corpus_scan(output_root, courses or None)
        if args.scan_report:
            report_path = args.scan_report.resolve()
            report_path.parent.mkdir(parents=True, exist_ok=True)
            if report_path.suffix.lower() == ".md":
                report_path.write_text(scan_report_markdown(report), encoding="utf-8")
            else:
                report_path.write_text(canonical_json(report), encoding="utf-8")
        print(canonical_json(report), end="")
        return 0

    if not args.audit_only and not args.rewrite:
        raise SystemExit("choose --scan-only, --audit-only, or --rewrite")
    if not courses:
        raise SystemExit("provide --course or --all-courses")

    for course_rel in courses:
        course_root = output_root / course_rel
        if not course_root.exists():
            raise RuntimeError(f"course does not exist: {course_rel}")
        course_runtime = runtime_root / course_rel
        course_runtime.mkdir(parents=True, exist_ok=True)
        session_boundary(repo_root, course_rel, course_runtime, args.model, args.reasoning)
        if args.rewrite:
            ensure_editorial_preamble(course_root / "common_preamble.tex")
            normalize_course_front_matter(course_root / "course.tex")

        for chapter_dir in chapter_dirs(course_root, args.chapter):
            record = load_chapter(repo_root, markdown_root, output_root, course_rel, chapter_dir)
            result = process_chapter(
                record=record,
                repo_root=repo_root,
                runtime_root=runtime_root,
                reference_paths=args.reference,
                reference_char_limit=args.reference_char_limit,
                model=args.model,
                reasoning=args.reasoning,
                audit_only=args.audit_only,
                rewrite=args.rewrite,
                max_repair_passes=args.max_repair_passes,
                compile_enabled=not args.no_compile,
                resume=args.resume,
                force=args.force,
            )
            print(f"{course_rel}/{chapter_dir.name}: {result}", flush=True)

        if args.rewrite and not args.no_compile:
            ok, log, pdf = compile_tex(course_root / "course.tex", course_runtime / "build")
            if not ok or pdf is None:
                raise RuntimeError(f"course compile failed for {course_rel}:\n{log}")
            shutil.copy2(pdf, course_root / "course.pdf")
    return 0


if __name__ == "__main__":
    sys.exit(main())
