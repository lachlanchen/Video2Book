#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from string import Template


MODULE_ROOT = Path(__file__).resolve().parents[1]
NOTES_MODULE_PATH = MODULE_ROOT / "subtitles2notes" / "generate_course_notes.py"


def load_notes_module():
    spec = importlib.util.spec_from_file_location("video2book_generate_course_notes", NOTES_MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


notes_module = load_notes_module()


FIGURE_ENV_RE = re.compile(r"\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}", re.S)
INCLUDEGRAPHICS_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
TARGET_IMAGE_RE = re.compile(r"(lecture_\d{2})_(?:frame|figure)_(\d{2})(?:[_-].*)?\.(?:png|jpg|jpeg)$", re.I)


@dataclass
class FigureRecord:
    index: int
    image_ref: str
    image_span: tuple[int, int]
    caption: str
    caption_span: tuple[int, int]
    env_span: tuple[int, int]


@dataclass
class CandidateBundle:
    window: object
    candidates: list[object]


def extract_balanced_braces(text: str, open_brace_index: int) -> tuple[str, int]:
    depth = 0
    chars: list[str] = []
    for index in range(open_brace_index, len(text)):
        char = text[index]
        if char == "{":
            depth += 1
            if depth == 1:
                continue
        elif char == "}":
            depth -= 1
            if depth == 0:
                return "".join(chars), index
        if depth >= 1:
            chars.append(char)
    raise ValueError("Unbalanced braces in LaTeX figure block")


def parse_figure_records(content_text: str) -> list[FigureRecord]:
    records: list[FigureRecord] = []
    for env_index, match in enumerate(FIGURE_ENV_RE.finditer(content_text), start=1):
        env_text = match.group(0)
        env_start = match.start()

        image_match = INCLUDEGRAPHICS_RE.search(env_text)
        if not image_match:
            continue
        image_ref = image_match.group(1).strip()
        image_span = (env_start + image_match.start(1), env_start + image_match.end(1))

        caption_cmd = re.search(r"\\caption(?:\[[^\]]*\])?\{", env_text)
        if not caption_cmd:
            continue
        brace_index = caption_cmd.end() - 1
        caption_text, close_index = extract_balanced_braces(env_text, brace_index)
        caption_span = (env_start + brace_index + 1, env_start + close_index)

        records.append(
            FigureRecord(
                index=env_index,
                image_ref=image_ref,
                image_span=image_span,
                caption=caption_text.strip(),
                caption_span=caption_span,
                env_span=(match.start(), match.end()),
            )
        )
    return records


def rewrite_content_text(content_text: str, record: FigureRecord, new_image_ref: str | None, new_caption: str | None) -> str:
    replacements: list[tuple[int, int, str]] = []
    if new_image_ref is not None and new_image_ref != record.image_ref:
        replacements.append((record.image_span[0], record.image_span[1], new_image_ref))
    if new_caption is not None and new_caption != record.caption:
        replacements.append((record.caption_span[0], record.caption_span[1], new_caption))
    if not replacements:
        return content_text

    rebuilt = content_text
    for start, end, value in sorted(replacements, key=lambda item: item[0], reverse=True):
        rebuilt = rebuilt[:start] + value + rebuilt[end:]
    return rebuilt


def target_figure_image(record: FigureRecord) -> bool:
    return bool(TARGET_IMAGE_RE.search(Path(record.image_ref).name))


def resolve_image_path(course_root: Path, lecture_dir: Path, image_ref: str) -> Path | None:
    ref_path = Path(image_ref)
    candidates = [
        lecture_dir / ref_path,
        course_root / ref_path,
        course_root / "assets" / ref_path.name,
        course_root / "figures" / ref_path.name,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def lecture_dirs_for_course(course_root: Path) -> list[Path]:
    chapters_dir = course_root / "chapters"
    if not chapters_dir.exists():
        return []
    return sorted([path for path in chapters_dir.iterdir() if path.is_dir() and path.name.startswith("lecture_")])


def content_context(content_text: str, record: FigureRecord, window_chars: int = 700) -> str:
    start = max(0, record.env_span[0] - window_chars)
    end = min(len(content_text), record.env_span[1] + 260)
    return content_text[start:end].strip()


def tokenize_query(text: str, max_terms: int = 14) -> list[str]:
    tokens = [token for token in re.findall(r"[A-Za-z]{4,}", text.lower()) if token not in notes_module.STOPWORDS]
    ordered: list[str] = []
    for token in tokens:
        if token not in ordered:
            ordered.append(token)
    return ordered[:max_terms]


def score_window(window: object, query_terms: list[str]) -> int:
    lowered = window.text.lower()
    score = 0
    for term in query_terms:
        count = lowered.count(term)
        if count:
            score += 4 * count
    score += notes_module.keyword_score(window.text)
    return score


def choose_candidate_windows(windows: list[object], query_terms: list[str], max_windows: int = 2) -> list[object]:
    if not windows:
        return []

    ranked = sorted(
        enumerate(windows),
        key=lambda item: (score_window(item[1], query_terms), len(item[1].text)),
        reverse=True,
    )
    selected: list[int] = []
    min_gap = 35.0
    for index, window in ranked:
        midpoint = notes_module.window_midpoint(window)
        if all(abs(midpoint - notes_module.window_midpoint(windows[existing])) >= min_gap for existing in selected):
            selected.append(index)
        if len(selected) >= max_windows:
            break

    if not selected:
        return notes_module.choose_figure_windows(windows, max_frames=max_windows)
    return [windows[index] for index in sorted(selected, key=lambda item: windows[item].start_seconds)]


def build_candidate_windows_text(bundles: list[CandidateBundle]) -> str:
    lines: list[str] = []
    for bundle_index, bundle in enumerate(bundles, start=1):
        lines.append(
            f"- window {bundle_index}: "
            f"{notes_module.format_seconds(bundle.window.start_seconds)}-"
            f"{notes_module.format_seconds(bundle.window.end_seconds)} | "
            f"{notes_module.trim_excerpt(bundle.window.text, limit=220)}"
        )
    return "\n".join(lines) or "- none"


def build_candidate_list_text(bundles: list[CandidateBundle]) -> str:
    lines: list[str] = []
    for bundle_index, bundle in enumerate(bundles, start=1):
        for candidate in bundle.candidates:
            lines.append(
                f"- {candidate.path.name} | window {bundle_index} | "
                f"{notes_module.format_seconds(candidate.timestamp_seconds)} | "
                f"subtitle: {notes_module.trim_excerpt(candidate.subtitle_excerpt, limit=180)}"
            )
    return "\n".join(lines) or "- none"


def transcript_excerpt_for_windows(all_windows: list[object], focus_windows: list[object], radius: int = 4) -> str:
    if not all_windows:
        return ""
    if not focus_windows:
        focus_windows = all_windows[: min(len(all_windows), 10)]

    selected_indices: set[int] = set()
    for focus in focus_windows:
        for index, window in enumerate(all_windows):
            if window == focus:
                start = max(0, index - radius)
                end = min(len(all_windows), index + radius + 1)
                selected_indices.update(range(start, end))
                break

    if not selected_indices:
        selected_indices.update(range(min(len(all_windows), 10)))

    lines: list[str] = []
    for index in sorted(selected_indices):
        window = all_windows[index]
        lines.append(
            f"- [{notes_module.format_seconds(window.start_seconds)} - "
            f"{notes_module.format_seconds(window.end_seconds)}] {window.text}"
        )
    return "\n".join(lines)


def safe_caption_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def compile_latex_tex(working_dir: Path, tex_name: str) -> None:
    for _ in range(2):
        notes_module.run_command(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                tex_name,
            ],
            cwd=working_dir,
        )


def process_figure(
    repo_root: Path,
    source_root: Path,
    markdown_root: Path,
    subtitle_root: Path,
    course_root: Path,
    lecture_dir: Path,
    lecture: object,
    course_config: object,
    record: FigureRecord,
    content_text: str,
    runtime_root: Path,
    model: str,
    reasoning: str,
    max_windows: int,
    force: bool,
    apply_changes: bool,
) -> dict:
    current_image_path = resolve_image_path(course_root, lecture_dir, record.image_ref)
    if current_image_path is None:
        return {
            "figure_index": record.index,
            "status": "skipped",
            "reason": f"image not found: {record.image_ref}",
        }

    transcript_md = lecture.transcript_path.read_text(encoding="utf-8")
    windows = notes_module.subtitle_windows_for_lecture(lecture, transcript_md)
    query_text = "\n".join([record.caption, content_context(content_text, record, window_chars=420)])
    query_terms = tokenize_query(query_text)
    selected_windows = choose_candidate_windows(windows, query_terms, max_windows=max_windows)

    figure_runtime = runtime_root / lecture.course_rel / lecture.lecture_slug / f"figure_{record.index:02d}"
    figure_runtime.mkdir(parents=True, exist_ok=True)

    bundles: list[CandidateBundle] = []
    for window_index, window in enumerate(selected_windows, start=1):
        candidates = notes_module.extract_window_candidate_frames(
            lecture=lecture,
            runtime_dir=figure_runtime,
            window_index=window_index,
            window=window,
            force=force,
        )
        bundles.append(CandidateBundle(window=window, candidates=candidates))

    prompt = Template(
        (MODULE_ROOT / "subtitles2notes" / "prompts" / "lecture_notes" / "figure_recheck_prompt.txt").read_text(encoding="utf-8")
    ).substitute(
        task_context=notes_module.build_task_context(lecture, course_config),
        course_title=lecture.course_title,
        course_descriptor=lecture.course_descriptor,
        lecture_title=lecture.lecture_title,
        transcript_rel=lecture.transcript_rel,
        video_rel=lecture.video_rel,
        figure_file=str(lecture_dir.relative_to(course_root) / "content.tex"),
        current_image=current_image_path.name,
        current_caption=record.caption,
        query_terms=", ".join(query_terms) or "none",
        figure_context=content_context(content_text, record),
        candidate_windows=build_candidate_windows_text(bundles),
        candidate_list=build_candidate_list_text(bundles),
        transcript_text=transcript_excerpt_for_windows(windows, selected_windows),
    )

    decision_path = figure_runtime / "decision.json"
    images = [current_image_path]
    for bundle in bundles:
        for candidate in bundle.candidates:
            images.append(candidate.path)

    notes_module.run_codex_prompt(
        repo_root=repo_root,
        prompt_text=prompt,
        output_path=decision_path,
        runtime_dir=figure_runtime,
        log_prefix="figure_recheck",
        model=model,
        reasoning=reasoning,
        images=images,
    )

    payload = notes_module.parse_json_payload(decision_path.read_text(encoding="utf-8"))
    verdict = str(payload.get("verdict", "keep")).strip().lower()
    chosen_asset = str(payload.get("chosen_asset", current_image_path.name)).strip() or current_image_path.name
    revised_caption = safe_caption_text(str(payload.get("caption", record.caption)).strip() or record.caption)
    reason = str(payload.get("reason", "")).strip()

    candidate_lookup = {current_image_path.name: current_image_path}
    timestamp_lookup = {current_image_path.name: None}
    for bundle in bundles:
        for candidate in bundle.candidates:
            candidate_lookup[candidate.path.name] = candidate.path
            timestamp_lookup[candidate.path.name] = candidate.timestamp_seconds

    changed = False
    if apply_changes and verdict in {"replace", "keep"}:
        new_image_ref: str | None = None
        if chosen_asset != current_image_path.name and chosen_asset in candidate_lookup and verdict == "replace":
            target_name = f"{lecture.lecture_slug}_figure_recheck_{record.index:02d}.png"
            target_path = course_root / "assets" / target_name
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(candidate_lookup[chosen_asset], target_path)
            new_image_ref = target_name
            changed = True
        updated_text = rewrite_content_text(
            content_text,
            record,
            new_image_ref=new_image_ref,
            new_caption=revised_caption,
        )
        if updated_text != content_text:
            (lecture_dir / "content.tex").write_text(updated_text, encoding="utf-8")
            content_text = updated_text
            changed = True

    result = {
        "figure_index": record.index,
        "status": verdict,
        "chosen_asset": chosen_asset,
        "fit_assessment": str(payload.get("fit_assessment", "")).strip(),
        "caption": revised_caption,
        "reason": reason,
        "changed": changed,
        "timestamp_seconds": timestamp_lookup.get(chosen_asset),
    }
    return result


def find_course_roots(output_root: Path, source_root: Path, course_filter: str | None) -> list[Path]:
    if course_filter:
        course_root = output_root / course_filter
        return [course_root] if (course_root / "course.tex").exists() else []

    ordered = []
    grouped = notes_module.video_files_by_course(source_root)
    seen: set[Path] = set()
    for course_rel in notes_module.ordered_courses(grouped):
        course_root = output_root / course_rel
        if (course_root / "course.tex").exists():
            ordered.append(course_root)
            seen.add(course_root)

    for extra in sorted(path.parent for path in output_root.rglob("course.tex")):
        if extra not in seen:
            ordered.append(extra)
    return ordered


def course_summary_markdown(course_root: Path, summaries: list[dict]) -> str:
    lines = [f"# Figure Recheck Summary", "", f"- course: {course_root}", ""]
    for item in summaries:
        lines.append(
            f"- lecture {item['lecture_slug']} figure {item['figure_index']:02d}: "
            f"{item['status']} | chosen={item['chosen_asset']} | changed={item['changed']} | {item['reason'] or 'no reason provided'}"
        )
    return "\n".join(lines) + "\n"


def parser() -> argparse.ArgumentParser:
    default_repo_root = Path.cwd().resolve()
    default_source_root = Path("/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG")
    parsed = argparse.ArgumentParser(description="Recheck inserted lecture figures against source videos and transcript context.")
    parsed.add_argument("--repo-root", type=Path, default=default_repo_root)
    parsed.add_argument("--source-root", type=Path, default=default_source_root)
    parsed.add_argument("--markdown-root", type=Path)
    parsed.add_argument("--subtitle-root", type=Path)
    parsed.add_argument("--output-root", type=Path)
    parsed.add_argument("--runtime-root", type=Path)
    parsed.add_argument("--course-config", type=Path)
    parsed.add_argument("--course", help="Restrict to one course rel path under generated_course_notes/")
    parsed.add_argument("--lecture-slug", help="Restrict to one lecture slug, e.g. lecture_02")
    parsed.add_argument("--figure-index", type=int, help="Restrict to one figure index within the lecture content.tex order")
    parsed.add_argument("--model", default="gpt-5.4")
    parsed.add_argument("--reasoning", default="high", choices=["low", "medium", "high", "xhigh"])
    parsed.add_argument("--max-windows", type=int, default=2)
    parsed.add_argument("--force", action="store_true")
    parsed.add_argument("--report-only", action="store_true")
    parsed.add_argument("--rebuild", action="store_true")
    return parsed


def main() -> int:
    args = parser().parse_args()
    repo_root = args.repo_root.resolve()
    markdown_root = (args.markdown_root or repo_root / "markdown").resolve()
    subtitle_root = (args.subtitle_root or repo_root / "subtitles").resolve()
    output_root = (args.output_root or repo_root / "generated_course_notes").resolve()
    runtime_root = (args.runtime_root or repo_root / ".lecture-notes-work" / "figure_recheck").resolve()
    course_config = notes_module.load_course_config(args.course_config)

    course_roots = find_course_roots(output_root, args.source_root, args.course)
    if not course_roots:
        print("No matching course roots found.")
        return 0

    changed_courses: list[Path] = []
    for course_root in course_roots:
        course_rel = str(course_root.relative_to(output_root))
        lecture_summaries: list[dict] = []
        lecture_dirs = lecture_dirs_for_course(course_root)
        for lecture_dir in lecture_dirs:
            if args.lecture_slug and lecture_dir.name != args.lecture_slug:
                continue
            metadata_path = lecture_dir / "metadata.json"
            content_path = lecture_dir / "content.tex"
            if not metadata_path.exists() or not content_path.exists():
                continue
            meta = json.loads(metadata_path.read_text(encoding="utf-8"))
            lecture = notes_module.lecture_from_transcript_rel(
                repo_root=repo_root,
                source_root=args.source_root,
                markdown_root=markdown_root,
                subtitle_root=subtitle_root,
                transcript_rel=meta["transcript_rel"],
                course_config=course_config,
                source_rel_override=meta.get("video_rel"),
            )
            content_text = content_path.read_text(encoding="utf-8")
            records = [record for record in parse_figure_records(content_text) if target_figure_image(record)]
            lecture_changed = False
            for record in records:
                if args.figure_index and record.index != args.figure_index:
                    continue
                result = process_figure(
                    repo_root=repo_root,
                    source_root=args.source_root,
                    markdown_root=markdown_root,
                    subtitle_root=subtitle_root,
                    course_root=course_root,
                    lecture_dir=lecture_dir,
                    lecture=lecture,
                    course_config=course_config,
                    record=record,
                    content_text=content_text,
                    runtime_root=runtime_root,
                    model=args.model,
                    reasoning=args.reasoning,
                    max_windows=args.max_windows,
                    force=args.force,
                    apply_changes=not args.report_only,
                )
                result["lecture_slug"] = lecture_dir.name
                lecture_summaries.append(result)
                if result["changed"]:
                    content_text = content_path.read_text(encoding="utf-8")
                    lecture_changed = True

            if lecture_changed and args.rebuild and not args.report_only:
                compile_latex_tex(lecture_dir, "lecture.tex")

        if lecture_summaries:
            course_runtime = runtime_root / course_rel
            course_runtime.mkdir(parents=True, exist_ok=True)
            (course_runtime / "summary.json").write_text(json.dumps(lecture_summaries, indent=2), encoding="utf-8")
            (course_runtime / "summary.md").write_text(course_summary_markdown(course_root, lecture_summaries), encoding="utf-8")

        if any(item["changed"] for item in lecture_summaries):
            changed_courses.append(course_root)
            if args.rebuild and not args.report_only:
                compile_latex_tex(course_root, "course.tex")

    print(f"rechecked_courses={len(course_roots)} changed_courses={len(changed_courses)}")
    for course_root in changed_courses:
        print(f"changed: {course_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
