#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


TEX_OPEN_RE = re.compile(r"\((?P<path>(?:\./|\.\./|/)?[^()\s]+\.(?:tex|sty|cls|cfg|def|clo|fd))")
OVERFULL_DETECTED_RE = re.compile(
    r"^Overfull \\hbox \((?P<amount>[^)]+)\) detected at line (?P<line>\d+)$"
)
OVERFULL_PARAGRAPH_RE = re.compile(
    r"^Overfull \\hbox \((?P<amount>[^)]+)\) in paragraph at lines (?P<start>\d+)(?:--(?P<end>\d+))?$"
)
UNDERFULL_PARAGRAPH_RE = re.compile(
    r"^Underfull \\hbox \(badness (?P<amount>\d+)\) in paragraph at lines (?P<start>\d+)(?:--(?P<end>\d+))?$"
)
PAGE_BUILDER_RE = re.compile(
    r"^Overfull \\\\[hv]box \((?P<amount>[^)]+)\) has occurred while \\\\output is active$"
)


@dataclass
class WarningItem:
    amount: str
    file_path: Path | None
    display_path: str
    line_start: int | None
    line_end: int | None
    kind: str
    suggestion: str
    excerpt: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Map LaTeX overfull warnings back to source files.")
    parser.add_argument("--log", required=True, help="Path to the pdflatex log file.")
    parser.add_argument("--compile-root", help="Temporary compile root used to resolve relative paths.")
    parser.add_argument("--display-root", help="Canonical source root to display in the report.")
    parser.add_argument("--actionable-root", help="Root path used to decide whether a warning is actionable.")
    parser.add_argument("--output", required=True, help="Destination Markdown report path.")
    parser.add_argument("--variant-label", default="", help="Human-readable build label for the report header.")
    return parser.parse_args()


def normalize_log_path(raw: str) -> str:
    return raw.rstrip(".,")


def resolve_source_path(raw: str, compile_root: Path | None, display_root: Path | None) -> tuple[Path | None, str]:
    raw = normalize_log_path(raw)
    resolved: Path | None
    if raw.startswith("/"):
      resolved = Path(raw)
    elif compile_root is not None:
      resolved = (compile_root / raw).resolve()
    else:
      resolved = Path(raw)

    display_path = raw
    if raw.startswith("./"):
      display_path = raw[2:]
    elif raw.startswith("../"):
      display_path = raw

    if resolved is not None and display_root is not None:
      if raw.startswith("./"):
        mapped = display_root / raw[2:]
        return mapped, str(mapped)
      if raw.startswith("../"):
        mapped = (display_root / raw).resolve()
        return mapped, str(mapped)
      if not raw.startswith("/"):
        mapped = (display_root / raw).resolve()
        return mapped, str(mapped)
      if raw.startswith("/"):
        try:
          if compile_root is not None:
            rel = resolved.relative_to(compile_root)
            mapped = display_root / rel
            return mapped, str(mapped)
        except ValueError:
          pass

    return resolved, display_path


def classify_excerpt(excerpt: str) -> tuple[str, str]:
    if not excerpt:
        return ("unknown", "Inspect the surrounding source manually; the log did not map cleanly to a readable line.")

    figure_tokens = ("\\begin{figure", "\\includegraphics", "\\begin{tikzpicture}", "\\begin{subfigure}", "\\caption{")
    math_tokens = ("\\begin{equation", "\\begin{align", "\\begin{gather", "\\begin{multline", "\\[", "\\]", "$")
    if any(token in excerpt for token in figure_tokens):
        return (
            "figure",
            "Scale the figure or TikZ block to `\\linewidth`, shorten labels, or move wide captions out of the narrow layout.",
        )
    if any(token in excerpt for token in math_tokens):
        return (
            "math",
            "Rewrite the expression as `align` or `split`, add explicit line breaks, or move wide inline math into a display block.",
        )
    if re.search(r"https?://|www\.|[A-Za-z0-9]/[A-Za-z0-9]|_[A-Za-z0-9]", excerpt):
        return (
            "unbreakable-text",
            "Insert discretionary breaks, shorten the unbreakable token, or move it out of the narrow paragraph.",
        )
    return (
        "paragraph",
        "Rewrite the sentence around the long span or apply a local `\\sloppypar` only where the warning occurs.",
    )


def extract_excerpt(file_path: Path | None, line_start: int | None) -> str:
    if file_path is None or line_start is None or not file_path.exists():
        return ""
    try:
        lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return ""
    if line_start < 1 or line_start > len(lines):
        return ""
    start = max(0, line_start - 2)
    end = min(len(lines), line_start + 1)
    return "\n".join(lines[start:end]).strip()


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|")


def is_under_root(path: Path | None, root: Path | None) -> bool:
    if path is None or root is None:
        return True
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def build_warning(
    raw_path: str | None,
    amount: str,
    line_start: int | None,
    line_end: int | None,
    compile_root: Path | None,
    display_root: Path | None,
) -> WarningItem:
    file_path = None
    display_path = "(unknown)"
    if raw_path:
        file_path, display_path = resolve_source_path(raw_path, compile_root, display_root)
    excerpt = extract_excerpt(file_path, line_start)
    kind, suggestion = classify_excerpt(excerpt)
    return WarningItem(
        amount=amount,
        file_path=file_path,
        display_path=display_path,
        line_start=line_start,
        line_end=line_end,
        kind=kind,
        suggestion=suggestion,
        excerpt=excerpt,
    )


def main() -> int:
    args = parse_args()
    log_path = Path(args.log)
    compile_root = Path(args.compile_root).resolve() if args.compile_root else None
    display_root = Path(args.display_root).resolve() if args.display_root else None
    actionable_root = Path(args.actionable_root).resolve() if args.actionable_root else display_root
    output_path = Path(args.output)

    if not log_path.exists():
        print(f"missing log: {log_path}", file=sys.stderr)
        return 1

    try:
        lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        print(f"failed to read log {log_path}: {exc}", file=sys.stderr)
        return 1

    current_tex: str | None = None
    actionable_overfulls: list[WarningItem] = []
    page_builder_overfulls: list[str] = []
    underfulls: list[WarningItem] = []
    seen_actionable: set[tuple[str, str | None, int | None, int | None]] = set()
    seen_underfull: set[tuple[str, str | None, int | None, int | None]] = set()

    for line in lines:
        for match in TEX_OPEN_RE.finditer(line):
            raw_path = normalize_log_path(match.group("path"))
            if raw_path.endswith(".tex"):
                current_tex = raw_path

        page_builder_match = PAGE_BUILDER_RE.match(line)
        if page_builder_match:
            page_builder_overfulls.append(page_builder_match.group("amount"))
            continue

        overfull_match = OVERFULL_DETECTED_RE.match(line)
        if overfull_match:
            line_no = int(overfull_match.group("line"))
            key = (overfull_match.group("amount"), current_tex, line_no, line_no)
            if key not in seen_actionable:
                item = build_warning(
                    current_tex,
                    overfull_match.group("amount"),
                    line_no,
                    line_no,
                    compile_root,
                    display_root,
                )
                if is_under_root(item.file_path, actionable_root):
                    seen_actionable.add(key)
                    actionable_overfulls.append(item)
            continue

        overfull_paragraph_match = OVERFULL_PARAGRAPH_RE.match(line)
        if overfull_paragraph_match:
            line_start = int(overfull_paragraph_match.group("start"))
            line_end = int(overfull_paragraph_match.group("end") or line_start)
            key = (overfull_paragraph_match.group("amount"), current_tex, line_start, line_end)
            if key not in seen_actionable:
                item = build_warning(
                    current_tex,
                    overfull_paragraph_match.group("amount"),
                    line_start,
                    line_end,
                    compile_root,
                    display_root,
                )
                if is_under_root(item.file_path, actionable_root):
                    seen_actionable.add(key)
                    actionable_overfulls.append(item)
            continue

        underfull_match = UNDERFULL_PARAGRAPH_RE.match(line)
        if underfull_match:
            line_start = int(underfull_match.group("start"))
            line_end = int(underfull_match.group("end") or line_start)
            key = (underfull_match.group("amount"), current_tex, line_start, line_end)
            if key not in seen_underfull:
                item = build_warning(
                    current_tex,
                    underfull_match.group("amount"),
                    line_start,
                    line_end,
                    compile_root,
                    display_root,
                )
                if is_under_root(item.file_path, actionable_root):
                    seen_underfull.add(key)
                    underfulls.append(item)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    summary_lines = [
        "# LaTeX Overflow Report",
        "",
        f"- Generated: {datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')}",
        f"- Variant: {args.variant_label or 'unspecified'}",
        f"- Log: `{log_path}`",
        f"- Actionable overfull warnings: `{len(actionable_overfulls)}`",
        f"- Page-builder overfull warnings: `{len(page_builder_overfulls)}`",
        f"- Underfull paragraph warnings: `{len(underfulls)}`",
        "",
    ]

    if actionable_overfulls:
        summary_lines.extend(
            [
                "## Actionable Overfull Warnings",
                "",
                "| Width | File | Line | Kind | Suggestion |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for item in actionable_overfulls:
            line_display = "?"
            if item.line_start is not None:
                line_display = str(item.line_start) if item.line_end in (None, item.line_start) else f"{item.line_start}-{item.line_end}"
            summary_lines.append(
                "| "
                + " | ".join(
                    [
                        markdown_escape(item.amount),
                        markdown_escape(item.display_path),
                        line_display,
                        item.kind,
                        markdown_escape(item.suggestion),
                    ]
                )
                + " |"
            )
        summary_lines.append("")

        summary_lines.append("## Source Excerpts")
        summary_lines.append("")
        for item in actionable_overfulls:
            line_display = "?"
            if item.line_start is not None:
                line_display = str(item.line_start) if item.line_end in (None, item.line_start) else f"{item.line_start}-{item.line_end}"
            summary_lines.append(f"### `{item.display_path}:{line_display}`")
            summary_lines.append("")
            summary_lines.append(f"- Width: `{item.amount}`")
            summary_lines.append(f"- Kind: `{item.kind}`")
            summary_lines.append(f"- Suggestion: {item.suggestion}")
            if item.excerpt:
                summary_lines.append("")
                summary_lines.append("```tex")
                summary_lines.append(item.excerpt)
                summary_lines.append("```")
            summary_lines.append("")
    else:
        summary_lines.extend(
            [
                "## Actionable Overfull Warnings",
                "",
                "No source-mapped overfull `\\hbox` warnings were found in this build.",
                "",
            ]
        )

    if page_builder_overfulls:
        top_amounts = ", ".join(page_builder_overfulls[:10])
        if len(page_builder_overfulls) > 10:
            top_amounts += ", ..."
        summary_lines.extend(
            [
                "## Page-Builder Warnings",
                "",
                "These are usually pagination/layout side effects and are not reliably attributable to one source line.",
                "",
                f"- Sample widths: `{top_amounts}`",
                "",
            ]
        )

    output_path.write_text("\n".join(summary_lines).rstrip() + "\n", encoding="utf-8")
    print(
        "actionable_overfulls="
        + str(len(actionable_overfulls))
        + " page_builder_overfulls="
        + str(len(page_builder_overfulls))
        + " underfulls="
        + str(len(underfulls))
        + " report="
        + str(output_path)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
