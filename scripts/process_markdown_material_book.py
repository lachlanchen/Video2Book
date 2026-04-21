#!/usr/bin/env python3
"""Turn an ordered Markdown material folder into a pocket-size TeX book."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class SourceItem:
    index: int
    title: str
    rel_path: str
    source_path: Path
    chapter_dir: Path
    chapter_slug: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Write a pocket-size TeX book from a numbered Markdown material corpus."
    )
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--material-root", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--source-credit", default="")
    parser.add_argument("--curator", default="LazyingArt LLC")
    parser.add_argument("--language", default="English")
    parser.add_argument("--model", default="gpt-5.4")
    parser.add_argument("--reasoning", default="high")
    parser.add_argument("--max-items", type=int, default=0)
    parser.add_argument("--no-compile", action="store_true")
    parser.add_argument("--commit-each", action="store_true")
    parser.add_argument("--compile-engine", default="xelatex", choices=["xelatex", "lualatex", "pdflatex"])
    return parser.parse_args()


def run(cmd: list[str], *, cwd: Path | None = None) -> None:
    print("+ " + " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=cwd, check=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text or "chapter"


def tex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def parse_summary(material_root: Path, output_dir: Path) -> list[SourceItem]:
    summary_path = material_root / "SUMMARY.md"
    summary = read_text(summary_path) if summary_path.exists() else ""
    items: list[tuple[str, str]] = []
    for title, rel_path in re.findall(r"\[([^\]]+)\]\(([^)]+\.md)\)", summary):
        if rel_path == "README.md":
            continue
        source_path = material_root / rel_path
        if source_path.exists():
            items.append((title.strip(), rel_path))

    if not items:
        for source_path in sorted(material_root.glob("*.md"), key=lambda p: int(p.stem) if p.stem.isdigit() else 10_000):
            if source_path.name in {"README.md", "SUMMARY.md"}:
                continue
            items.append((source_path.stem, source_path.name))

    sources: list[SourceItem] = []
    for index, (title, rel_path) in enumerate(items, start=1):
        chapter_slug = f"{index:03d}-{slugify(Path(rel_path).stem + '-' + title)}"
        sources.append(
            SourceItem(
                index=index,
                title=title,
                rel_path=rel_path,
                source_path=material_root / rel_path,
                chapter_dir=output_dir / "chapters" / chapter_slug,
                chapter_slug=chapter_slug,
            )
        )
    return sources


def referenced_images(item: SourceItem, material_root: Path) -> list[Path]:
    text = read_text(item.source_path)
    candidates: list[Path] = []
    for raw in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
        rel = raw.split()[0].strip("<>")
        path = (item.source_path.parent / rel).resolve()
        if path.exists():
            candidates.append(path)

    numbered = material_root / "img" / f"{item.index:05d}.jpg"
    if numbered.exists():
        candidates.append(numbered.resolve())

    seen: set[Path] = set()
    result: list[Path] = []
    for path in candidates:
        if path not in seen:
            seen.add(path)
            result.append(path)
    return result[:8]


def prepare_project(args: argparse.Namespace, sources: list[SourceItem]) -> None:
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "chapters").mkdir(exist_ok=True)
    (args.output_dir / "assets").mkdir(exist_ok=True)
    (args.output_dir / ".material-book-work" / "prompts").mkdir(parents=True, exist_ok=True)

    source_img = args.material_root / "img"
    target_img = args.output_dir / "assets" / "source-img"
    if source_img.exists():
        shutil.copytree(source_img, target_img, dirs_exist_ok=True)

    manifest_lines = ["index\ttitle\trel_path\tchapter_slug"]
    for item in sources:
        manifest_lines.append(f"{item.index}\t{item.title}\t{item.rel_path}\t{item.chapter_slug}")
    write_text(args.output_dir / "source_manifest.tsv", "\n".join(manifest_lines) + "\n")

    summary_ref = args.material_root / "SUMMARY.md"
    readme_ref = args.material_root / "README.md"
    plan = [
        f"# {args.title} - Material Book Plan",
        "",
        "This book is written one source note at a time, but each chapter must keep the full corpus arc in view.",
        "",
        "## Whole-Corpus Context",
        "",
        f"- Material root: `{args.material_root}`",
        f"- Summary path: `{summary_ref}`",
        f"- README path: `{readme_ref}`",
        "- Before writing a chapter, inspect the full ordered source list and the already generated chapters.",
        "- Preserve the source sequence as evidence, but write the book as a coherent wealth-freedom argument.",
        "- Repetition across source notes can become reinforcing evidence; do not delete prior substance just to avoid repetition.",
        "- Structural moves are allowed only when they clearly improve the reader's route through the whole book.",
        "",
        "## Ordered Source Notes",
        "",
    ]
    for item in sources:
        plan.append(f"{item.index}. `{item.rel_path}` - {item.title}")
    write_text(args.output_dir / "book_plan.md", "\n".join(plan) + "\n")

    write_text(args.output_dir / "common_preamble.tex", common_preamble())
    write_course_tex(args, sources)


def common_preamble() -> str:
    return r"""\usepackage{fontspec}
\usepackage{microtype}
\usepackage[paperwidth=6in,paperheight=9in,margin=0.55in]{geometry}
\usepackage{scrextend}
\changefontsizes[16pt]{13.2pt}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage{caption}
\usepackage{float}
\usepackage{adjustbox}
\usepackage{tikz}

\setmainfont{Latin Modern Roman}
\newfontfamily\cjkfont{Noto Serif CJK SC}
\setsansfont{Latin Modern Sans}
\setmonofont{Latin Modern Mono}

\hypersetup{colorlinks=true,linkcolor=blue!45!black,urlcolor=blue!45!black}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em}
\setlength{\emergencystretch}{1.8em}
\setlength{\hfuzz}{1.5pt}
\setlength{\tabcolsep}{3pt}
\pretolerance=1000
\tolerance=3200
\hbadness=3200
\sloppy
\setlist[itemize]{topsep=0.25em,itemsep=0.2em,leftmargin=*}
\setlist[enumerate]{topsep=0.25em,itemsep=0.2em,leftmargin=*}
\setlength{\headheight}{42pt}

\newenvironment{sourceinsight}{\begin{quote}\small\itshape}{\end{quote}}
\newcommand{\sourcenote}[1]{\par\smallskip{\footnotesize\color{black!60}Source note: #1}\par}
\newcommand{\chapterdivider}{\par\medskip\hrule\medskip}

\makeatletter
\newcommand{\material@headerfont}{\normalfont\footnotesize\itshape}
\newcommand{\material@pagefont}{\normalfont\footnotesize}
\newcommand{\material@headerraise}{14pt}
\newlength{\material@headerboxheight}
\setlength{\material@headerboxheight}{\dimexpr\headheight-\material@headerraise-12pt\relax}
\newcommand{\material@leftheadbox}[1]{%
  \raisebox{\material@headerraise}{%
    \parbox[t][\material@headerboxheight][t]{0.76\textwidth}{%
      \raggedright\material@headerfont\strut\MakeUppercase{#1}\strut%
    }%
  }%
}
\renewcommand{\chaptermark}[1]{\markboth{\MakeUppercase{\chaptername\ \thechapter.\ #1}}{}}
\fancyhf{}
\fancyhead[L]{\material@leftheadbox{\leftmark}}
\fancyhead[R]{\material@pagefont\thepage}
\renewcommand{\headrulewidth}{0.45pt}
\pagestyle{fancy}
\fancypagestyle{plain}{%
  \fancyhf{}
  \fancyhead[L]{\material@leftheadbox{\leftmark}}
  \fancyhead[R]{\material@pagefont\thepage}
  \renewcommand{\headrulewidth}{0.45pt}
}
\makeatother
"""


def write_course_tex(args: argparse.Namespace, sources: list[SourceItem]) -> None:
    inputs = []
    for item in sources:
        content = item.chapter_dir / "content.tex"
        if content.exists() and content.stat().st_size > 0:
            inputs.append(rf"\input{{chapters/{item.chapter_slug}/content.tex}}")

    cover_path = args.output_dir / "assets" / "source-img" / "cover1.jpeg"
    if cover_path.exists():
        cover_art = r"\includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio]{assets/source-img/cover1.jpeg}"
    else:
        cover_art = r"\fcolorbox{black!15}{black!3}{\rule{0pt}{0.72\paperheight}\rule{0.82\paperwidth}{0pt}}"

    title = tex_escape(args.title)
    subtitle = tex_escape(args.subtitle)
    source_credit = tex_escape(args.source_credit)
    curator = tex_escape(args.curator)

    tex = rf"""\documentclass[oneside]{{book}}
\input{{common_preamble.tex}}
\graphicspath{{{{assets/source-img/}}{{assets/}}}}
\begin{{document}}
\frontmatter
\hypersetup{{pageanchor=false}}
\begin{{titlepage}}
\thispagestyle{{empty}}
\begin{{tikzpicture}}[remember picture,overlay]
  \node[anchor=center,inner sep=0] at (current page.center) {{{cover_art}}};
  \node[
    anchor=north west,
    align=left,
    text width=0.78\paperwidth,
    fill=white,
    fill opacity=0.9,
    text opacity=1,
    rounded corners=8pt,
    inner xsep=10pt,
    inner ysep=8pt
  ] at ([xshift=0.08\paperwidth,yshift=-0.07\paperheight]current page.north west) {{%
    {{\fontsize{{24}}{{28}}\selectfont\bfseries {title}\\[0.5em]}}
    {{\large\color{{black!70}} {subtitle}}}
  }};
  \node[
    anchor=south west,
    align=left,
    text width=0.72\paperwidth,
    fill=white,
    fill opacity=0.84,
    text opacity=1,
    rounded corners=6pt,
    inner sep=10pt
  ] at ([xshift=0.08\paperwidth,yshift=0.08\paperheight]current page.south west) {{%
    {{\small\color{{black!72}} {source_credit}\\[0.35em]}}
    {{\footnotesize\color{{black!68}} Book edition organized by {curator} with Video2Book.}}
  }};
\end{{tikzpicture}}
\mbox{{}}
\end{{titlepage}}
\hypersetup{{pageanchor=true}}
\clearpage
\tableofcontents
\mainmatter
{chr(10).join(inputs)}
\end{{document}}
"""
    write_text(args.output_dir / "course.tex", tex)


def make_prompt(args: argparse.Namespace, item: SourceItem, sources: list[SourceItem], images: list[Path]) -> Path:
    prompt_path = args.output_dir / ".material-book-work" / "prompts" / f"{item.index:03d}.md"
    image_lines = "\n".join(f"- `{path}`" for path in images) or "- No directly referenced local image found for this source."
    existing = sorted(args.output_dir.glob("chapters/*/content.tex"))
    existing_lines = "\n".join(f"- `{path}`" for path in existing[-12:]) or "- No prior generated chapters yet."
    prompt = f"""You are writing one chapter of a pocket-size TeX book.

Book title: {args.title}
Book subtitle: {args.subtitle}
Output language: {args.language}
Current source note: {item.index}/{len(sources)}
Current source title: {item.title}
Current source path: {item.source_path}

Whole-corpus context paths:
- Summary: {args.material_root / "SUMMARY.md"}
- Source README: {args.material_root / "README.md"}
- Generated book plan: {args.output_dir / "book_plan.md"}
- Source manifest: {args.output_dir / "source_manifest.tsv"}
- Existing chapter directory: {args.output_dir / "chapters"}

Important: although this worker writes one source note at a time, keep the overview and big picture in mind. Read the full source order in SUMMARY.md / source_manifest.tsv and inspect existing generated chapters when useful. The chapter should fit the larger arc of a book about wealth freedom, attention, time, capital, personal business models, investing discipline, and execution.

Current related images you may inspect:
{image_lines}

Recently generated chapters for continuity:
{existing_lines}

Required output:
- Write only valid LaTeX body content for this chapter.
- Start with exactly one `\\chapter{{...}}`.
- Do not include `\\documentclass`, `\\begin{{document}}`, `\\end{{document}}`, Markdown fences, or explanatory chat text.
- Write in original prose based on the source, not a raw translation dump.
- Preserve concrete ideas, definitions, examples, and decision methods from the current source.
- Connect the current source to the whole-book arc when useful.
- If ideas repeat from earlier notes, treat repetition as reinforcing evidence instead of deleting substance.
- Use conservative restructuring only when it makes the new source easier to place in the full book.
- If an image is genuinely useful, include it with a pocket-safe command such as `\\includegraphics[width=\\linewidth]{{assets/source-img/FILENAME}}`; do not invent captions for images you did not inspect.
- Keep tables, diagrams, and equations narrow enough for a 6x9 pocket book.
- End with `\\sourcenote{{Material source: {item.rel_path}.}}`
"""
    write_text(prompt_path, prompt)
    return prompt_path


def sanitize_tex(path: Path, fallback_title: str) -> None:
    text = read_text(path).strip()
    text = re.sub(r"^```(?:tex|latex)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    text = re.sub(r"\\documentclass(?:.|\n)*?\\begin\{document\}", "", text)
    text = text.replace(r"\end{document}", "")
    text = text.strip()
    if r"\chapter" not in text[:500]:
        text = rf"\chapter{{{tex_escape(fallback_title)}}}" + "\n\n" + text
    write_text(path, text + "\n")


def compile_book(args: argparse.Namespace) -> None:
    build = args.output_dir / "build"
    build.mkdir(exist_ok=True)
    for _ in range(2):
        run(
            [
                args.compile_engine,
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                "-output-directory=build",
                "course.tex",
            ],
            cwd=args.output_dir,
        )
    src = build / "course.pdf"
    if src.exists():
        shutil.copy2(src, args.output_dir / "course_pocket_1_2x.pdf")


def commit_step(args: argparse.Namespace, item: SourceItem) -> None:
    pathspecs = [
        str(args.output_dir.relative_to(args.repo_root)),
    ]
    run(
        [
            str(MODULE_ROOT / "scripts" / "codex_commit_push.sh"),
            str(args.repo_root),
            f"Update material book chapter {item.index:03d}",
            *pathspecs,
        ]
    )


def main() -> int:
    args = parse_args()
    args.repo_root = args.repo_root.resolve()
    args.material_root = args.material_root.resolve()
    args.output_dir = args.output_dir.resolve()
    if not args.material_root.exists():
        raise SystemExit(f"Material root not found: {args.material_root}")

    sources = parse_summary(args.material_root, args.output_dir)
    if not sources:
        raise SystemExit("No source markdown files found.")
    prepare_project(args, sources)

    processed = 0
    for item in sources:
        content_path = item.chapter_dir / "content.tex"
        if content_path.exists() and content_path.stat().st_size > 0:
            continue
        if args.max_items and processed >= args.max_items:
            break

        item.chapter_dir.mkdir(parents=True, exist_ok=True)
        images = referenced_images(item, args.material_root)
        prompt_path = make_prompt(args, item, sources, images)
        output_tmp = item.chapter_dir / "content.raw.tex"
        cmd = [
            str(MODULE_ROOT / "scripts" / "codex_prompt_to_file.sh"),
            str(args.repo_root),
            str(prompt_path),
            str(output_tmp),
            args.model,
            args.reasoning,
            *[str(path) for path in images],
        ]
        run(cmd, cwd=args.repo_root)
        sanitize_tex(output_tmp, item.title)
        output_tmp.replace(content_path)
        write_course_tex(args, sources)
        if not args.no_compile:
            compile_book(args)
        if args.commit_each:
            commit_step(args, item)
        processed += 1

    write_course_tex(args, sources)
    if not args.no_compile:
        compile_book(args)
    print(json.dumps({"processed": processed, "output_dir": str(args.output_dir)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
