#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


TOKEN_PATTERNS = [
    (
        "leaked_font_token",
        re.compile(r"(ootnotesize|ormalsize|criptsize|footnotesize|scriptsize|normalsize)"),
        "Possible leaked TeX font-size token rendered into PDF text.",
    ),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit a rendered pocket PDF for obvious typography/render leaks.")
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--pages-output", type=Path)
    parser.add_argument("--max-issues", type=int, default=20)
    return parser.parse_args()


def pdftotext_layout(pdf_path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout


def normalize_excerpt(page_text: str, match_start: int, match_end: int) -> str:
    lines = page_text.splitlines()
    offset = 0
    for idx, line in enumerate(lines):
        line_end = offset + len(line) + 1
        if match_start < line_end:
            excerpt_lines = lines[max(0, idx - 1): min(len(lines), idx + 2)]
            return "\n".join(excerpt_lines).strip()
        offset = line_end
    return page_text[max(0, match_start - 80): match_end + 80].strip()


def main() -> int:
    args = parse_args()
    text = pdftotext_layout(args.pdf)
    pages = text.split("\f")
    issues: list[dict[str, object]] = []
    issue_pages: list[int] = []
    seen: set[tuple[int, str, str]] = set()

    for page_no, page_text in enumerate(pages, start=1):
        if not page_text.strip():
            continue
        for kind, pattern, description in TOKEN_PATTERNS:
            for match in pattern.finditer(page_text):
                excerpt = normalize_excerpt(page_text, match.start(), match.end())
                key = (page_no, kind, excerpt)
                if key in seen:
                    continue
                seen.add(key)
                issues.append(
                    {
                        "page": page_no,
                        "kind": kind,
                        "token": match.group(0),
                        "description": description,
                        "excerpt": excerpt,
                    }
                )
                issue_pages.append(page_no)
                if len(issues) >= args.max_issues:
                    break
            if len(issues) >= args.max_issues:
                break
        if len(issues) >= args.max_issues:
            break

    unique_pages = sorted(set(issue_pages))

    lines = [
        "# Pocket PDF Audit",
        "",
        f"- PDF: `{args.pdf}`",
        f"- Pages: `{len([p for p in pages if p.strip()])}`",
        f"- Audit issues: `{len(issues)}`",
        "",
    ]

    if issues:
        lines.extend(
            [
                "## Issues",
                "",
                "| Page | Kind | Token | Excerpt |",
                "| --- | --- | --- | --- |",
            ]
        )
        for issue in issues:
            excerpt = str(issue["excerpt"]).replace("\n", " / ").replace("|", "\\|")
            token = str(issue["token"]).replace("|", "\\|")
            lines.append(f"| {issue['page']} | {issue['kind']} | `{token}` | {excerpt} |")
    else:
        lines.extend(
            [
                "## Issues",
                "",
                "No obvious rendered-PDF token leaks were detected.",
            ]
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")

    payload = {
        "pdf": str(args.pdf),
        "page_count": len([p for p in pages if p.strip()]),
        "issue_count": len(issues),
        "issue_pages": unique_pages,
        "issues": issues,
    }
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    if args.pages_output:
        args.pages_output.parent.mkdir(parents=True, exist_ok=True)
        args.pages_output.write_text("\n".join(str(page) for page in unique_pages) + ("\n" if unique_pages else ""), encoding="utf-8")

    print(f"audit_issues={len(issues)} issue_pages={','.join(str(p) for p in unique_pages)} report={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
