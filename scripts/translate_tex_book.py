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


def parse_source_main(source_main: Path) -> list[dict[str, str]]:
    lines = read_text(source_main).splitlines()
    current_part = ""
    in_mainmatter = False
    chapters: list[dict[str, str]] = []
    for line in lines:
        stripped = line.strip()
        if stripped == r"\mainmatter":
            in_mainmatter = True
            continue
        part_match = re.match(r"\\part\{(.+)\}", stripped)
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
        chapter_match = re.search(r"\\chapter\{(.+?)\}", chapter_text)
        title = chapter_match.group(1) if chapter_match else source_chapter.parent.name
        chapters.append(
            {
                "key": source_chapter.parent.name,
                "title": title,
                "part": current_part,
                "source_abs": str(source_chapter),
                "source_input_rel": input_rel,
            }
        )
    if not chapters:
        raise SystemExit(f"No chapter inputs found in {source_main}")
    return chapters


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


def render_initial_main(source_main: Path, language_dir: Path, chapters: list[dict[str, str]]) -> str:
    source_text = read_text(source_main)
    chapter_lookup = {chapter["source_input_rel"]: chapter["key"] for chapter in chapters}
    out_lines: list[str] = []
    for line in source_text.splitlines(keepends=True):
        stripped = line.strip()
        if re.fullmatch(r"\\input\{.+common_preamble\.tex\}", stripped):
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
    source_main = (repo_root / book_root_rel / f"{Path(book_root_rel).name}.tex").resolve()
    if not source_main.exists():
        raise SystemExit(f"Source main TeX file not found: {source_main}")
    language_dir = (repo_root / book_root_rel / language).resolve()
    chapters = parse_source_main(source_main)
    target_main = language_dir / source_main.name
    manifest = {
        "book_root_rel": book_root_rel,
        "language": language,
        "language_name": LANGUAGES[language]["name"],
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
            "source_rel": manifest["source_main_rel"],
            "target_rel": manifest["target_main_rel"],
            "status": "pending",
            "sha256": "",
            "updated_at": "",
        }
    )
    for chapter in chapters:
        source_abs = Path(chapter["source_abs"])
        target_abs = language_dir / "chapters" / chapter["key"] / "content.tex"
        manifest["units"].append(
            {
                "key": chapter["key"],
                "kind": "chapter",
                "title": chapter["title"],
                "part": chapter["part"],
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
    preamble_path = language_dir / "translated_common_preamble.tex"
    write_text(preamble_path, render_translated_preamble(language))

    source_main = repo_root / manifest["source_main_rel"]
    chapters = parse_source_main(source_main)
    initial_main = render_initial_main(source_main, language_dir, chapters)
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
        chapters = parse_source_main(repo_root / manifest["source_main_rel"])
        source_text = render_initial_main(
            repo_root / manifest["source_main_rel"],
            repo_root / manifest["language_dir_rel"],
            chapters,
        )
        scope_line = "This file contains the cover page text, title metadata, part titles, and chapter includes for the translated edition."
    else:
        source_text = read_text(repo_root / unit["source_rel"])
        scope_line = f'This file is one chapter from part "{unit["part"]}" with the chapter title "{unit["title"]}".'
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
