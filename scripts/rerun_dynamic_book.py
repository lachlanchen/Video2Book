#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

MODULE_ROOT = Path(__file__).resolve().parents[1]
if str(MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(MODULE_ROOT))

import subtitles2notes.generate_course_notes as notes_module
from subtitles2notes.generate_course_notes import (
    lecture_from_transcript_rel,
    load_course_config,
    update_dynamic_book,
)


def read_text_or_placeholder(path: Path, placeholder: str) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return placeholder


def asset_list_text(lecture_dir: Path, asset_paths: list[Path]) -> str:
    metadata_path = lecture_dir / "metadata.json"
    if metadata_path.exists():
        data = json.loads(metadata_path.read_text(encoding="utf-8"))
        assets = data.get("assets") or []
        lines = []
        for item in assets:
            name = str(item.get("name") or "unknown")
            stamp = str(item.get("timestamp_hhmmss") or "unknown")
            use = str(item.get("recommended_use") or "supporting figure")
            caption = str(item.get("caption_hint") or "none")
            excerpt = str(item.get("subtitle_excerpt") or "none")
            rationale = str(item.get("rationale") or "none")
            lines.append(
                " | ".join(
                    [
                        f"- {name}",
                        f"frame {stamp}",
                        use,
                        f"caption hint: {caption}",
                        f"subtitle excerpt: {excerpt}",
                        f"rationale: {rationale}",
                    ]
                )
            )
        if lines:
            return "\n".join(lines)

    if asset_paths:
        return "\n".join(f"- {path.name} | reused existing validated figure asset" for path in asset_paths)
    return "- none"


def metadata_files_with_cutoff(course_root: Path, cutoff: int) -> list[Path]:
    matched: list[tuple[int, Path]] = []
    for metadata_file in sorted((course_root / "chapters").glob("lecture_*/metadata.json")):
        data = json.loads(metadata_file.read_text(encoding="utf-8"))
        lecture_number = int(data.get("lecture_number") or 0)
        if lecture_number <= cutoff:
            matched.append((lecture_number, metadata_file))
    matched.sort(key=lambda item: (item[0], item[1].parent.name))
    return [item[1] for item in matched]


def filtered_processed_lecture_summary(course_root: Path, cutoff: int) -> str:
    entries: list[tuple[int, str, str]] = []
    for metadata_file in metadata_files_with_cutoff(course_root, cutoff):
        meta = json.loads(metadata_file.read_text(encoding="utf-8"))
        entries.append(
            (
                int(meta.get("lecture_number") or 0),
                str(meta.get("lecture_slug") or metadata_file.parent.name),
                str(meta.get("lecture_title") or metadata_file.parent.name),
            )
        )
    if not entries:
        return "- No processed lectures yet."
    return "\n".join(
        f"- {slug} | lecture {number:02d} | {title}" if number > 0 else f"- {slug} | {title}"
        for number, slug, title in entries
    )


def filtered_course_corpus_snapshot(course_root: Path, cutoff: int) -> str:
    entries: list[str] = []
    for metadata_file in metadata_files_with_cutoff(course_root, cutoff):
        chapter_dir = metadata_file.parent
        meta = json.loads(metadata_file.read_text(encoding="utf-8"))
        lecture_number = int(meta.get("lecture_number") or 0)
        lecture_slug = str(meta.get("lecture_slug") or chapter_dir.name)
        lecture_title = str(meta.get("lecture_title") or chapter_dir.name)
        assets = [Path(asset).name for asset in meta.get("assets", []) if str(asset).strip()]
        analysis_excerpt = notes_module.markdown_body_excerpt(chapter_dir / "analysis.md", limit=240)
        narrative_excerpt = notes_module.markdown_body_excerpt(chapter_dir / "narrative_map.md", limit=220)
        math_excerpt = notes_module.markdown_body_excerpt(chapter_dir / "math_bank.md", limit=180)
        parts = [
            f"- {lecture_slug} | lecture {lecture_number:02d} | {lecture_title}" if lecture_number > 0 else f"- {lecture_slug} | {lecture_title}",
            f"analysis: {analysis_excerpt}",
            f"narrative: {narrative_excerpt}",
            f"math/business detail: {math_excerpt}",
        ]
        if assets:
            parts.append(f"assets: {', '.join(assets)}")
        entries.append("\n".join(parts))
    return "\n\n".join(entries) or "- No processed lecture corpus yet."


def filtered_course_figure_inventory(course_root: Path, cutoff: int) -> str:
    entries: list[str] = []
    for metadata_file in metadata_files_with_cutoff(course_root, cutoff):
        chapter_dir = metadata_file.parent
        meta = json.loads(metadata_file.read_text(encoding="utf-8"))
        assets = [Path(asset).name for asset in meta.get("assets", []) if str(asset).strip()]
        if not assets:
            continue
        lecture_number = int(meta.get("lecture_number") or 0)
        lecture_slug = str(meta.get("lecture_slug") or chapter_dir.name)
        lecture_title = str(meta.get("lecture_title") or chapter_dir.name)
        figure_excerpt = notes_module.markdown_body_excerpt(chapter_dir / "figures_markdown.md", limit=240)
        entries.append(
            "\n".join(
                [
                    f"- {lecture_slug} | lecture {lecture_number:02d} | {lecture_title}" if lecture_number > 0 else f"- {lecture_slug} | {lecture_title}",
                    f"assets: {', '.join(assets)}",
                    f"figure notes: {figure_excerpt}",
                ]
            )
        )
    return "\n\n".join(entries) or "- No validated figure assets exist yet across the processed lectures."


@contextlib.contextmanager
def patch_dynamic_book_views(cutoff: int):
    original_summary = notes_module.processed_lecture_summary
    original_corpus = notes_module.course_corpus_snapshot
    original_figures = notes_module.course_figure_inventory
    notes_module.processed_lecture_summary = lambda course_root: filtered_processed_lecture_summary(course_root, cutoff)
    notes_module.course_corpus_snapshot = lambda course_root: filtered_course_corpus_snapshot(course_root, cutoff)
    notes_module.course_figure_inventory = lambda course_root: filtered_course_figure_inventory(course_root, cutoff)
    try:
        yield
    finally:
        notes_module.processed_lecture_summary = original_summary
        notes_module.course_corpus_snapshot = original_corpus
        notes_module.course_figure_inventory = original_figures


def reset_dynamic_book(course_root: Path, runtime_root: Path) -> Path | None:
    dynamic_root = course_root / "dynamic_book"
    if not dynamic_root.exists():
        dynamic_root.mkdir(parents=True, exist_ok=True)
        return None

    backup_root = runtime_root / "backups" / course_root.name / datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_root.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(dynamic_root, backup_root)
    shutil.rmtree(dynamic_root)
    dynamic_root.mkdir(parents=True, exist_ok=True)
    return backup_root


def parser() -> argparse.ArgumentParser:
    default_repo_root = Path.cwd().resolve()
    parsed = argparse.ArgumentParser(description="Replay only the dynamic-book update over an existing course.")
    parsed.add_argument("--repo-root", type=Path, default=default_repo_root)
    parsed.add_argument("--source-root", type=Path, default=default_repo_root / "downloads")
    parsed.add_argument("--markdown-root", type=Path, default=default_repo_root / "markdown")
    parsed.add_argument("--subtitle-root", type=Path, default=default_repo_root / "subtitles")
    parsed.add_argument("--output-root", type=Path, default=default_repo_root / "generated_course_notes")
    parsed.add_argument("--runtime-root", type=Path, default=default_repo_root / ".lecture-notes-work" / "dynamic-rerun")
    parsed.add_argument("--course-config", type=Path, required=True)
    parsed.add_argument("--course", required=True)
    parsed.add_argument("--start-number", type=int, default=1)
    parsed.add_argument("--end-number", type=int, required=True)
    parsed.add_argument("--model", default="gpt-5.4")
    parsed.add_argument("--reasoning", default="xhigh", choices=["low", "medium", "high", "xhigh"])
    parsed.add_argument("--clean-start", action="store_true", help="Backup and rebuild the dynamic book from scratch before replaying.")
    return parsed


def main() -> None:
    args = parser().parse_args()
    repo_root = args.repo_root.resolve()
    source_root = args.source_root.resolve()
    markdown_root = args.markdown_root.resolve()
    subtitle_root = args.subtitle_root.resolve()
    output_root = args.output_root.resolve()
    runtime_root = args.runtime_root.resolve()
    prompt_root = MODULE_ROOT / "subtitles2notes" / "prompts" / "lecture_notes"
    course_config = load_course_config(args.course_config.resolve())

    course_dir = markdown_root / args.course
    if not course_dir.exists():
        raise SystemExit(f"Course markdown directory not found: {course_dir}")

    transcript_rels: list[str] = []
    for transcript_path in sorted(course_dir.glob("*.md")):
        transcript_rel = str(transcript_path.relative_to(markdown_root))
        lecture = lecture_from_transcript_rel(
            repo_root,
            source_root,
            markdown_root,
            subtitle_root,
            transcript_rel,
            course_config,
        )
        if args.start_number <= lecture.lecture_number <= args.end_number:
            transcript_rels.append(transcript_rel)

    if not transcript_rels:
        raise SystemExit("No lectures matched the requested replay range.")

    primary_lecture = lecture_from_transcript_rel(
        repo_root,
        source_root,
        markdown_root,
        subtitle_root,
        transcript_rels[0],
        course_config,
    )
    course_root = output_root / primary_lecture.course_rel
    backup_root: Path | None = None
    if args.clean_start:
        backup_root = reset_dynamic_book(course_root, runtime_root)

    print(f"Dynamic-book replay lectures: {len(transcript_rels)}")
    print(f"Course: {args.course}")
    print(f"Range: {args.start_number} to {args.end_number}")
    if backup_root is not None:
        print(f"Backed up prior dynamic book to: {backup_root}")

    with patch_dynamic_book_views(args.end_number):
        for transcript_rel in transcript_rels:
            lecture = lecture_from_transcript_rel(
                repo_root,
                source_root,
                markdown_root,
                subtitle_root,
                transcript_rel,
                course_config,
            )
            course_root = output_root / lecture.course_rel
            lecture_dir = course_root / "chapters" / lecture.lecture_slug
            figures_dir = course_root / "figures"
            assets = sorted(figures_dir.glob(f"{lecture.lecture_slug}_figure_*.png"))
            course_runtime = runtime_root / lecture.course_rel / lecture.lecture_slug
            course_runtime.mkdir(parents=True, exist_ok=True)

            figures_markdown_text = read_text_or_placeholder(
                lecture_dir / "figures_markdown.md",
                "# Figure Notes\n\nNo validated mathematical screenshots were kept for this lecture.\n",
            )
            visual_notes_text = read_text_or_placeholder(
                lecture_dir / "visual_notes.md",
                "# Visual Notes\n\nNo visual extraction notes are available for this lecture.\n",
            )
            narrative_map_text = read_text_or_placeholder(
                lecture_dir / "narrative_map.md",
                "# Narrative Map\n\nNo narrative map is available for this lecture.\n",
            )
            math_bank_text = read_text_or_placeholder(
                lecture_dir / "math_bank.md",
                "# Math Bank\n\nNo math bank is available for this lecture.\n",
            )
            analysis_text = read_text_or_placeholder(
                lecture_dir / "analysis.md",
                "# Chapter Plan\n\nNo chapter analysis is available for this lecture.\n",
            )
            current_chapter_tex = read_text_or_placeholder(
                lecture_dir / "content.tex",
                "% No chapter content exists yet.\n",
            )

            print(f"Replaying dynamic book from lecture {lecture.lecture_number:02d}: {lecture.lecture_title}")
            update_dynamic_book(
                repo_root=repo_root,
                course_root=course_root,
                markdown_root=markdown_root,
                lecture=lecture,
                course_config=course_config,
                runtime_dir=course_runtime,
                prompt_root=prompt_root,
                model=args.model,
                reasoning=args.reasoning,
                asset_list_text=asset_list_text(lecture_dir, assets),
                figures_markdown_text=figures_markdown_text,
                visual_notes_text=visual_notes_text,
                narrative_map_text=narrative_map_text,
                math_bank_text=math_bank_text,
                analysis_text=analysis_text,
                current_chapter_tex=current_chapter_tex,
                assets=assets,
            )


if __name__ == "__main__":
    main()
