#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


LANGUAGES = {
    "zh": {
        "name": "Traditional Chinese",
        "locale": "zh",
        "cjk_main_font": "Noto Serif CJK TC",
        "cjk_sans_font": "Noto Sans CJK TC",
    },
    "jp": {
        "name": "Japanese",
        "locale": "ja",
        "cjk_main_font": "Noto Serif CJK JP",
        "cjk_sans_font": "Noto Sans CJK JP",
    },
}


CHAPTER_RE = re.compile(r"\\chapter(?:\[[^\]]*\])?\{(.+?)\}")
PART_RE = re.compile(r"\\part(?:\[[^\]]*\])?\{(.+?)\}")


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def rel_to_repo(path: Path, repo_root: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def chapter_unit_key(index: int, title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if not slug:
        slug = f"chapter-{index:02d}"
    return f"chapter-{index:02d}-{slug}"


def translation_source_dir(repo_root: Path, book_root_rel: str) -> Path:
    return repo_root / book_root_rel / ".translation-work" / "source_units"


def ensure_book_gitignore(repo_root: Path, book_root_rel: str) -> Path:
    gitignore_path = repo_root / book_root_rel / ".gitignore"
    existing = read_text(gitignore_path).splitlines() if gitignore_path.exists() else []
    required = [
        ".translation-work/",
        "zh/build/",
        "jp/build/",
    ]
    changed = False
    for item in required:
        if item not in existing:
            existing.append(item)
            changed = True
    if changed or not gitignore_path.exists():
        text = "\n".join(line for line in existing if line.strip()) + "\n"
        write_text(gitignore_path, text)
    return gitignore_path


def detect_source_main(book_root: Path) -> Path:
    expected = book_root / f"{book_root.name}.tex"
    if expected.exists():
        return expected.resolve()

    fallback = book_root / "main.tex"
    if fallback.exists():
        return fallback.resolve()

    candidates = []
    for path in sorted(book_root.glob("*.tex")):
        if path.name in {"common_preamble.tex", "translated_common_preamble.tex"}:
            continue
        text = read_text(path)
        if r"\documentclass" in text:
            candidates.append(path.resolve())

    if len(candidates) == 1:
        return candidates[0]
    raise SystemExit(f"Source main TeX file not found under {book_root}")


def parse_source_main_inputs(source_main: Path) -> list[dict[str, str]]:
    lines = read_text(source_main).splitlines()
    current_part = ""
    in_mainmatter = False
    chapters: list[dict[str, str]] = []
    for line in lines:
        stripped = line.strip()
        if stripped == r"\mainmatter":
            in_mainmatter = True
            continue
        part_match = PART_RE.match(stripped)
        if part_match:
            current_part = part_match.group(1)
            continue
        if not in_mainmatter:
            continue
        input_match = re.match(r"\\input\{(.+/content\.tex)\}", stripped)
        if not input_match:
            continue
        input_rel = input_match.group(1)
        source_chapter = (source_main.parent / input_rel).resolve()
        chapter_text = read_text(source_chapter)
        chapter_match = CHAPTER_RE.search(chapter_text)
        title = chapter_match.group(1) if chapter_match else source_chapter.parent.name
        chapters.append(
            {
                "key": source_chapter.parent.name,
                "title": title,
                "part": current_part,
                "appendix": False,
                "source_abs": str(source_chapter),
                "source_input_rel": input_rel,
            }
        )
    if not chapters:
        raise SystemExit(f"No chapter inputs found in {source_main}")
    return chapters


def parse_source_main_inline(source_main: Path) -> list[dict[str, object]]:
    lines = read_text(source_main).splitlines(keepends=True)
    current_part = ""
    in_mainmatter = False
    in_appendix = False
    chapters: list[dict[str, object]] = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped == r"\mainmatter":
            in_mainmatter = True
            i += 1
            continue
        if stripped == r"\appendix":
            in_appendix = True
            i += 1
            continue
        part_match = PART_RE.match(stripped)
        if part_match:
            current_part = part_match.group(1)
            i += 1
            continue
        if not in_mainmatter:
            i += 1
            continue
        chapter_match = CHAPTER_RE.match(stripped)
        if not chapter_match:
            i += 1
            continue

        start = i
        title = chapter_match.group(1)
        j = i + 1
        while j < len(lines):
            probe = lines[j].strip()
            if CHAPTER_RE.match(probe) or PART_RE.match(probe) or probe in {r"\appendix", r"\backmatter", r"\end{document}"}:
                break
            j += 1

        key = chapter_unit_key(len(chapters) + 1, title)
        chapters.append(
            {
                "key": key,
                "title": title,
                "part": current_part,
                "appendix": in_appendix,
                "start_line": start,
                "end_line": j,
                "source_text": "".join(lines[start:j]),
            }
        )
        i = j

    if not chapters:
        raise SystemExit(f"No inline chapters found in {source_main}")
    return chapters


def parse_source_main(source_main: Path) -> dict[str, object]:
    source_text = read_text(source_main)
    has_input_chapters = bool(re.search(r"\\input\{(.+/content\.tex)\}", source_text))
    if has_input_chapters:
        return {"layout": "inputs", "chapters": parse_source_main_inputs(source_main)}
    return {"layout": "inline", "chapters": parse_source_main_inline(source_main)}


def rewrite_graphicspath_line(line: str, source_dir: Path, target_dir: Path) -> str:
    items = re.findall(r"\{([^{}]+)\}", line)
    if not items:
        return line
    rewritten = []
    source_assets = (source_dir / "assets").resolve()
    for item in items:
        absolute = (source_dir / item).resolve()
        if absolute == source_assets:
            rewritten.append("assets/")
            continue
        rel = os.path.relpath(absolute, target_dir).replace(os.sep, "/")
        if item.endswith("/") and not rel.endswith("/"):
            rel += "/"
        rewritten.append(rel)
    return "\\graphicspath{" + "".join(f"{{{item}}}" for item in rewritten) + "}\n"


def render_initial_main_inputs(source_main: Path, language_dir: Path, chapters: list[dict[str, object]]) -> str:
    source_text = read_text(source_main)
    chapter_lookup = {chapter["source_input_rel"]: chapter["key"] for chapter in chapters}
    out_lines: list[str] = []
    for line in source_text.splitlines(keepends=True):
        stripped = line.strip()
        if re.fullmatch(r"\\input\{.*common_preamble\.tex\}", stripped):
            out_lines.append(r"\input{translated_common_preamble.tex}" + "\n")
            continue
        if stripped.startswith(r"\graphicspath{"):
            out_lines.append(rewrite_graphicspath_line(line, source_main.parent, language_dir))
            continue
        input_match = re.match(r"\\input\{(.+/content\.tex)\}", stripped)
        if input_match:
            source_rel = input_match.group(1)
            key = chapter_lookup[source_rel]
            out_lines.append(f"\\input{{chapters/{key}/content.tex}}\n")
            continue
        out_lines.append(line)
    return "".join(out_lines)


def render_initial_main_inline(source_main: Path, language_dir: Path, chapters: list[dict[str, object]]) -> str:
    lines = read_text(source_main).splitlines(keepends=True)
    chapter_by_start = {int(chapter["start_line"]): chapter for chapter in chapters}
    out_lines: list[str] = []
    i = 0
    while i < len(lines):
        chapter = chapter_by_start.get(i)
        if chapter is not None:
            out_lines.append(f"\\input{{chapters/{chapter['key']}/content.tex}}\n")
            i = int(chapter["end_line"])
            continue
        line = lines[i]
        stripped = line.strip()
        if re.fullmatch(r"\\input\{.*common_preamble\.tex\}", stripped):
            out_lines.append(r"\input{translated_common_preamble.tex}" + "\n")
        elif stripped.startswith(r"\graphicspath{"):
            out_lines.append(rewrite_graphicspath_line(line, source_main.parent, language_dir))
        else:
            out_lines.append(line)
        i += 1
    return "".join(out_lines)


def render_initial_main(source_main: Path, language_dir: Path, parsed: dict[str, object]) -> str:
    chapters = parsed["chapters"]
    if parsed["layout"] == "inputs":
        return render_initial_main_inputs(source_main, language_dir, chapters)
    return render_initial_main_inline(source_main, language_dir, chapters)


def render_translated_preamble(language: str) -> str:
    config = LANGUAGES[language]
    locale = config["locale"]
    cjk_main = config["cjk_main_font"]
    cjk_sans = config["cjk_sans_font"]
    return f"""\\usepackage{{fontspec}}
\\defaultfontfeatures{{Ligatures=TeX,Scale=MatchLowercase}}
\\setmainfont{{{cjk_main}}}
\\setsansfont{{{cjk_sans}}}
\\setmonofont{{Latin Modern Mono}}
\\XeTeXlinebreaklocale "{locale}"
\\XeTeXlinebreakskip = 0pt plus 1pt minus 0.1pt

\\usepackage[margin=1in]{{geometry}}
\\usepackage{{microtype}}
\\usepackage{{amsmath,amssymb,amsthm,mathtools,bm}}
\\usepackage{{graphicx}}
\\usepackage{{xcolor}}
\\usepackage{{booktabs}}
\\usepackage{{array}}
\\usepackage{{longtable}}
\\usepackage{{enumitem}}
\\usepackage{{float}}
\\usepackage{{caption}}
\\usepackage{{hyperref}}
\\usepackage{{tikz}}
\\usetikzlibrary{{arrows.meta,positioning,calc,decorations.pathmorphing}}

\\hypersetup{{
  colorlinks=true,
  linkcolor=blue!50!black,
  urlcolor=blue!50!black,
  citecolor=blue!50!black
}}

\\setlength{{\\parskip}}{{0.5em}}
\\setlength{{\\parindent}}{{0pt}}
\\setlength{{\\emergencystretch}}{{2em}}
\\setlist[itemize]{{topsep=0.25em,itemsep=0.2em}}
\\setlist[enumerate]{{topsep=0.25em,itemsep=0.2em}}
\\numberwithin{{equation}}{{chapter}}

\\newtheorem{{theorem}}{{Theorem}}[chapter]
\\newtheorem{{proposition}}[theorem]{{Proposition}}
\\newtheorem{{lemma}}[theorem]{{Lemma}}
\\newtheorem{{corollary}}[theorem]{{Corollary}}
\\theoremstyle{{definition}}
\\newtheorem{{definition}}[theorem]{{Definition}}
\\newtheorem{{example}}[theorem]{{Example}}
\\theoremstyle{{remark}}
\\newtheorem{{remark}}[theorem]{{Remark}}

\\providecommand{{\\ket}}[1]{{\\left\\lvert#1\\right\\rangle}}
\\providecommand{{\\bra}}[1]{{\\left\\langle#1\\right\\rvert}}
\\providecommand{{\\braket}}[2]{{\\left\\langle#1\\,\\middle|\\,#2\\right\\rangle}}
\\providecommand{{\\expect}}[1]{{\\left\\langle#1\\right\\rangle}}
\\newcommand{{\\lectureoverview}}[1]{{\\paragraph{{Overview.}} #1}}
"""


def build_manifest(repo_root: Path, book_root_rel: str, language: str) -> dict:
    source_main = detect_source_main((repo_root / book_root_rel).resolve())
    language_dir = (repo_root / book_root_rel / language).resolve()
    parsed = parse_source_main(source_main)
    chapters = parsed["chapters"]
    source_dir = translation_source_dir(repo_root, book_root_rel)
    source_book = source_dir / "book_main_source.tex"
    target_main = language_dir / source_main.name
    manifest = {
        "book_root_rel": book_root_rel,
        "language": language,
        "language_name": LANGUAGES[language]["name"],
        "source_layout": parsed["layout"],
        "source_main_rel": rel_to_repo(source_main, repo_root),
        "language_dir_rel": rel_to_repo(language_dir, repo_root),
        "target_main_rel": rel_to_repo(target_main, repo_root),
        "target_pdf_rel": rel_to_repo(language_dir / source_main.with_suffix(".pdf").name, repo_root),
        "units": [],
    }
    manifest["units"].append(
        {
            "key": "book",
            "kind": "book",
            "title": Path(book_root_rel).name,
            "part": "",
            "appendix": False,
            "source_rel": rel_to_repo(source_book, repo_root),
            "target_rel": manifest["target_main_rel"],
            "status": "pending",
            "sha256": "",
            "updated_at": "",
        }
    )
    for chapter in chapters:
        if parsed["layout"] == "inputs":
            source_abs = Path(chapter["source_abs"])
        else:
            source_abs = source_dir / f"{chapter['key']}.tex"
        target_abs = language_dir / "chapters" / chapter["key"] / "content.tex"
        manifest["units"].append(
            {
                "key": chapter["key"],
                "kind": "chapter",
                "title": chapter["title"],
                "part": chapter["part"],
                "appendix": bool(chapter.get("appendix", False)),
                "source_rel": rel_to_repo(source_abs, repo_root),
                "target_rel": rel_to_repo(target_abs, repo_root),
                "status": "pending",
                "sha256": "",
                "updated_at": "",
            }
        )
    return manifest


def manifest_path(repo_root: Path, book_root_rel: str, language: str) -> Path:
    return repo_root / book_root_rel / language / "translation_manifest.json"


def load_manifest(repo_root: Path, book_root_rel: str, language: str) -> dict:
    path = manifest_path(repo_root, book_root_rel, language)
    if not path.exists():
        raise SystemExit(f"Manifest not found: {path}. Run init first.")
    return json.loads(read_text(path))


def save_manifest(repo_root: Path, manifest: dict) -> Path:
    path = manifest_path(repo_root, manifest["book_root_rel"], manifest["language"])
    write_text(path, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return path


def init_language(repo_root: Path, book_root_rel: str, language: str) -> Path:
    manifest = build_manifest(repo_root, book_root_rel, language)
    existing = manifest_path(repo_root, book_root_rel, language)
    existing_units = {}
    if existing.exists():
        prior = json.loads(read_text(existing))
        existing_units = {unit["key"]: unit for unit in prior.get("units", [])}
    manifest["initialized_at"] = now_iso()
    manifest["updated_at"] = now_iso()
    language_dir = repo_root / manifest["language_dir_rel"]
    language_dir.mkdir(parents=True, exist_ok=True)
    ensure_book_gitignore(repo_root, book_root_rel)
    preamble_path = language_dir / "translated_common_preamble.tex"
    write_text(preamble_path, render_translated_preamble(language))

    source_main = repo_root / manifest["source_main_rel"]
    parsed = parse_source_main(source_main)
    chapters = parsed["chapters"]
    initial_main = render_initial_main(source_main, language_dir, parsed)
    source_dir = translation_source_dir(repo_root, book_root_rel)
    write_text(source_dir / "book_main_source.tex", initial_main)
    target_main = repo_root / manifest["target_main_rel"]
    prior_book = existing_units.get("book", {})
    if prior_book.get("status") != "done":
        write_text(target_main, initial_main)

    source_assets_dir = source_main.parent / "assets"
    target_assets_dir = language_dir / "assets"
    if source_assets_dir.exists():
        target_assets_dir.mkdir(parents=True, exist_ok=True)
        for asset in source_assets_dir.iterdir():
            if asset.is_file():
                shutil.copy2(asset, target_assets_dir / asset.name)

    for unit in manifest["units"]:
        prior = existing_units.get(unit["key"])
        if prior:
            unit["status"] = prior.get("status", unit["status"])
            unit["sha256"] = prior.get("sha256", "")
            unit["updated_at"] = prior.get("updated_at", "")
        target_path = repo_root / unit["target_rel"]
        if unit["kind"] == "book":
            if prior_book.get("status") != "done":
                write_text(target_path, initial_main)
        else:
            if manifest["source_layout"] == "inline":
                source_text = next(chapter["source_text"] for chapter in chapters if chapter["key"] == unit["key"])
                write_text(repo_root / unit["source_rel"], source_text)
            if not target_path.exists():
                source_text = read_text(repo_root / unit["source_rel"])
                write_text(target_path, source_text)

    return save_manifest(repo_root, manifest)


def get_unit(manifest: dict, unit_key: str) -> dict:
    for unit in manifest["units"]:
        if unit["key"] == unit_key:
            return unit
    raise SystemExit(f"Unknown unit key: {unit_key}")


def next_pending_unit(manifest: dict) -> dict | None:
    for unit in manifest["units"]:
        if unit.get("status") != "done":
            return unit
    return None


def render_translation_prompt(repo_root: Path, manifest: dict, unit: dict) -> str:
    language_name = LANGUAGES[manifest["language"]]["name"]
    if unit["kind"] == "book":
        source_text = read_text(repo_root / unit["source_rel"])
        if manifest.get("source_layout") == "inline":
            scope_line = "This file contains the translated-edition skeleton for a single-file TeX book: cover page text, front matter, part titles, appendix markers, and chapter include lines."
        else:
            scope_line = "This file contains the cover page text, title metadata, part titles, and chapter includes for the translated edition."
    else:
        source_text = read_text(repo_root / unit["source_rel"])
        scope_line = f'This file is one chapter from part "{unit["part"]}" with the chapter title "{unit["title"]}".'
        if unit.get("appendix"):
            scope_line += " It belongs to the appendix section of the book."
    return f"""Translate the following LaTeX file into {language_name}.

Goal:
- Preserve meaning faithfully.
- Make the prose smooth, natural, and elegant rather than literal.
- Keep the tone as polished lecture notes or literary nonfiction where appropriate.

Important translation constraints:
- Output only the full translated LaTeX file. No Markdown fences. No commentary.
- Preserve every LaTeX command, environment, macro name, label, path, filename, URL, citation key, and equation structure exactly.
- Preserve image filenames and all \\input targets exactly.
- Translate human-readable prose inside chapter titles, section titles, captions, paragraph headings, remarks, list items, and body text.
- Keep proper names in Latin script unless a standard target-language rendering is overwhelmingly obvious.
- Do not invent content, omit content, summarize content, or simplify technical arguments.
- Keep math unchanged unless a short prose word appears inside a command such as \\text{{...}} and clearly belongs to the surrounding sentence.
- Keep the final file compilable with XeLaTeX.
- For Chinese, use Traditional Chinese only, never Simplified Chinese.
- Keep "LazyingArt LLC" and "Video2Book" in English.

{scope_line}

Return the translated file only:

```tex
{source_text}
```
"""


def compile_translation(repo_root: Path, manifest: dict) -> None:
    language_dir = repo_root / manifest["language_dir_rel"]
    main_name = Path(manifest["target_main_rel"]).name
    build_dir = language_dir / "build"
    build_dir.mkdir(parents=True, exist_ok=True)
    command = [
        "xelatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-output-directory",
        str(build_dir),
        main_name,
    ]
    for _ in range(2):
        proc = subprocess.run(
            command,
            cwd=language_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        if proc.returncode != 0:
            sys.stderr.write(proc.stdout)
            raise SystemExit(proc.returncode)
    build_pdf = build_dir / Path(main_name).with_suffix(".pdf").name
    target_pdf = repo_root / manifest["target_pdf_rel"]
    shutil.copy2(build_pdf, target_pdf)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Translate a compiled TeX book chapter by chapter.")
    parser.add_argument("--repo-root", default=os.getcwd())
    parser.add_argument("--book-root", required=True, help="Book root relative to the repo root, for example: how-to-speak-and-write")
    parser.add_argument("--language", required=True, choices=sorted(LANGUAGES))
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init")
    subparsers.add_parser("status")

    next_parser = subparsers.add_parser("print-next")
    next_parser.add_argument("--format", choices=["key", "tsv"], default="tsv")

    prompt_parser = subparsers.add_parser("write-prompt")
    prompt_parser.add_argument("--unit", help="Unit key; defaults to the next pending unit")
    prompt_parser.add_argument("--output", required=True)

    done_parser = subparsers.add_parser("mark-done")
    done_parser.add_argument("--unit", required=True)

    compile_parser = subparsers.add_parser("compile")
    compile_parser.add_argument("--quiet", action="store_true")

    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    book_root_rel = args.book_root.strip("/").rstrip("/")
    language = args.language

    if args.command == "init":
        path = init_language(repo_root, book_root_rel, language)
        print(path.relative_to(repo_root).as_posix())
        return

    manifest = load_manifest(repo_root, book_root_rel, language)

    if args.command == "status":
        done = sum(1 for unit in manifest["units"] if unit.get("status") == "done")
        total = len(manifest["units"])
        next_unit = next_pending_unit(manifest)
        next_key = next_unit["key"] if next_unit else ""
        print(f'{manifest["language"]}\t{done}\t{total}\t{next_key}')
        return

    if args.command == "print-next":
        unit = next_pending_unit(manifest)
        if not unit:
            return
        if args.format == "key":
            print(unit["key"])
        else:
            print(f'{unit["key"]}\t{unit["kind"]}\t{unit["target_rel"]}\t{unit["title"]}')
        return

    if args.command == "write-prompt":
        unit = get_unit(manifest, args.unit) if args.unit else next_pending_unit(manifest)
        if not unit:
            raise SystemExit("No pending unit remains.")
        prompt = render_translation_prompt(repo_root, manifest, unit)
        write_text(Path(args.output).resolve(), prompt)
        print(unit["target_rel"])
        return

    if args.command == "mark-done":
        unit = get_unit(manifest, args.unit)
        target_path = repo_root / unit["target_rel"]
        if not target_path.exists():
            raise SystemExit(f"Translated target file missing: {target_path}")
        content = read_text(target_path)
        unit["status"] = "done"
        unit["sha256"] = sha256_text(content)
        unit["updated_at"] = now_iso()
        manifest["updated_at"] = now_iso()
        save_manifest(repo_root, manifest)
        print(unit["target_rel"])
        return

    if args.command == "compile":
        compile_translation(repo_root, manifest)
        if not args.quiet:
            print(manifest["target_pdf_rel"])
        return

    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
