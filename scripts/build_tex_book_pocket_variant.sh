#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/build_tex_book_pocket_variant.sh --source-root <path> --main-tex <file> --compile-root <path> --build-dir <path> --log-path <path> [options]

Build a standalone TeX book into a pocket-size variant inside a disposable
compile tree, while keeping source files in the original project untouched.

Options:
  --source-root <path>       Canonical source project root (required)
  --main-tex <file>          Main TeX file relative to source root (required)
  --compile-root <path>      Disposable compile root (required)
  --build-dir <path>         Build/output directory inside compile root (required)
  --log-path <path>          Path to combined compiler log (required)
  --font-mode <mode>         normal (default) or onepointtwo
  --paper-width <size>       Custom width, e.g. 6in
  --paper-height <size>      Custom height, e.g. 9in
  --margin <size>            Geometry margin, e.g. 0.55in
  --compile-engine <name>    xelatex (default), lualatex, or pdflatex
  -h, --help                 Show this help
USAGE
}

source_root=""
main_tex=""
compile_root=""
build_dir=""
log_path=""
font_mode="normal"
paper_width="6in"
paper_height="9in"
geometry_margin="0.55in"
compile_engine="xelatex"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --source-root)
      source_root="${2:-}"
      shift 2
      ;;
    --main-tex)
      main_tex="${2:-}"
      shift 2
      ;;
    --compile-root)
      compile_root="${2:-}"
      shift 2
      ;;
    --build-dir)
      build_dir="${2:-}"
      shift 2
      ;;
    --log-path)
      log_path="${2:-}"
      shift 2
      ;;
    --font-mode)
      font_mode="${2:-}"
      shift 2
      ;;
    --paper-width)
      paper_width="${2:-}"
      shift 2
      ;;
    --paper-height)
      paper_height="${2:-}"
      shift 2
      ;;
    --margin)
      geometry_margin="${2:-}"
      shift 2
      ;;
    --compile-engine)
      compile_engine="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ -z "$source_root" || -z "$main_tex" || -z "$compile_root" || -z "$build_dir" || -z "$log_path" ]]; then
  echo "--source-root, --main-tex, --compile-root, --build-dir, and --log-path are required." >&2
  exit 1
fi

source_root="$(cd "$source_root" && pwd)"
compile_root="$(mkdir -p "$compile_root" && cd "$compile_root" && pwd)"
build_dir="$(mkdir -p "$build_dir" && cd "$build_dir" && pwd)"
mkdir -p "$(dirname "$log_path")"

case "$font_mode" in
  normal|onepointtwo)
    ;;
  *)
    echo "Unknown font mode: $font_mode" >&2
    exit 1
    ;;
esac

case "$compile_engine" in
  xelatex|lualatex|pdflatex)
    ;;
  *)
    echo "Unknown compile engine: $compile_engine" >&2
    exit 1
    ;;
esac

if [[ ! -f "$source_root/$main_tex" ]]; then
  echo "Main TeX file not found: $source_root/$main_tex" >&2
  exit 1
fi

main_dir_rel="$(dirname "$main_tex")"
if [[ "$main_dir_rel" == "." ]]; then
  main_dir_rel=""
fi

rsync -a --delete "$source_root"/ "$compile_root"/

tmp_tex="$compile_root/$main_tex"
tmp_compile_root="$compile_root"
if [[ -n "$main_dir_rel" ]]; then
  tmp_compile_root="$compile_root/$main_dir_rel"
fi
tmp_main_argument="$(basename "$main_tex")"

python3 - "$tmp_tex" "$font_mode" "$paper_width" "$paper_height" "$geometry_margin" <<'PY'
from pathlib import Path
import re
import sys

path = Path(sys.argv[1])
font_mode = sys.argv[2]
paper_width = sys.argv[3]
paper_height = sys.argv[4]
margin = sys.argv[5]

if font_mode == "onepointtwo":
    stretch = "1.8em"
    hfuzz = "1.5pt"
    tolerance = "3200"
    hbadness = "3200"
    headheight = "42pt"
    header_raise = "14pt"
    header_clearance = "12pt"
    header_width = "0.76"
    chapter_number_font = "large"
    chapter_title_font = "Large"
    section_font = "small"
    subsection_font = "footnotesize"
    section_afterskip = "0.75ex"
    subsection_afterskip = "0.55ex"
    chapter_top_shift = "-14pt"
    cover_font_size = "18"
    cover_font_baseline = "21"
    title_width = "0.86"
    note_width = "0.78"
    manuscript_title_size = "28"
    manuscript_title_baseline = "32"
else:
    stretch = "1.2em"
    hfuzz = "1pt"
    tolerance = "2200"
    hbadness = "2200"
    headheight = "38pt"
    header_raise = "12pt"
    header_clearance = "10pt"
    header_width = "0.74"
    chapter_number_font = "Large"
    chapter_title_font = "LARGE"
    section_font = "normalsize"
    subsection_font = "small"
    section_afterskip = "0.9ex"
    subsection_afterskip = "0.7ex"
    chapter_top_shift = "-16pt"
    cover_font_size = "20"
    cover_font_baseline = "23"
    title_width = "0.84"
    note_width = "0.74"
    manuscript_title_size = "30"
    manuscript_title_baseline = "34"

text = path.read_text(encoding="utf-8")

geometry_replaced = False
updated = re.sub(
    r"\\geometry\{[^}]*\}",
    rf"\\geometry{{paperwidth={paper_width},paperheight={paper_height},margin={margin}}}",
    text,
    count=1,
)
if updated != text:
    text = updated
    geometry_replaced = True
else:
    updated = re.sub(
        r"\\usepackage(\[[^\]]*\])?\{geometry\}",
        rf"\\usepackage[paperwidth={paper_width},paperheight={paper_height},margin={margin}]{{geometry}}",
        text,
        count=1,
    )
    if updated != text:
        text = updated
        geometry_replaced = True

if not geometry_replaced:
    preamble_match = re.search(r"(?m)^\\input\{[^}]*preamble[^}]*\.tex\}\s*$", text)
    if preamble_match:
        text = text[:preamble_match.start()] + rf"\PassOptionsToPackage{{paperwidth={paper_width},paperheight={paper_height},margin={margin}}}{{geometry}}" + "\n" + text[preamble_match.start():]
        geometry_replaced = True

if not geometry_replaced:
    text = text.replace(
        "\\begin{document}",
        rf"\PassOptionsToPackage{{paperwidth={paper_width},paperheight={paper_height},margin={margin}}}{{geometry}}" + "\n\\begin{document}",
        1,
    )

if font_mode == "onepointtwo" and "\\changefontsizes" not in text:
    geom_pattern = re.compile(r"(\\(?:usepackage(?:\[[^\]]*\])?\{geometry\}|geometry\{[^}]*\})[^\n]*\n)", re.MULTILINE)
    text, count = geom_pattern.subn(rf"\1\\usepackage{{scrextend}}\n\\changefontsizes[16pt]{{13.2pt}}\n", text, count=1)
    if count == 0:
        text = text.replace("\\begin{document}", "\\usepackage{scrextend}\n\\changefontsizes[16pt]{13.2pt}\n\\begin{document}", 1)

package_inject = ""
if "\\usepackage{adjustbox}" not in text:
    package_inject += "\\usepackage{adjustbox}\n"
if package_inject:
    text = text.replace("\\begin{document}", package_inject + "\\begin{document}", 1)

tuning_block = f"""
\\setlength{{\\emergencystretch}}{{{stretch}}}
\\setlength{{\\hfuzz}}{{{hfuzz}}}
\\setlength{{\\tabcolsep}}{{4pt}}
\\pretolerance=1000
\\tolerance={tolerance}
\\hbadness={hbadness}
\\hyphenpenalty=150
\\exhyphenpenalty=100
\\providecommand{{\\allowdisplaybreaks}}[1][]{{}}
\\allowdisplaybreaks[2]
\\sloppy
\\makeatletter
\\def\\bookpocket@chapternumberfont{{\\normalfont\\{chapter_number_font}\\scshape}}
\\def\\bookpocket@chaptertitlefont{{\\normalfont\\{chapter_title_font}\\itshape}}
\\def\\bookpocket@sectionfont{{\\{section_font}\\bfseries}}
\\def\\bookpocket@subsectionfont{{\\{subsection_font}\\bfseries}}
\\def\\bookpocket@headerfont{{\\normalfont\\small\\itshape}}
\\def\\bookpocket@pagefont{{\\normalfont\\small}}
\\renewcommand{{\\chaptermark}}[1]{{\\markboth{{\\MakeUppercase{{\\chaptername\\ \\thechapter.\\ #1}}}}{{}}}}
\\renewcommand{{\\sectionmark}}[1]{{\\markright{{\\MakeUppercase{{\\thesection\\hspace{{0.4em}}#1}}}}}}
\\@ifundefined{{chapter}}{{}}{{%
  \\renewcommand{{\\@makechapterhead}}[1]{{%
    {{\\parindent\\z@\\normalfont
      \\vspace*{{{chapter_top_shift}}}
      \\ifnum \\c@secnumdepth >\\m@ne
        \\if@mainmatter
          \\noindent\\parbox[t]{{\\textwidth}}{{\\raggedright
            {{\\bookpocket@chapternumberfont \\MakeUppercase{{\\@chapapp\\space \\thechapter}}}}\\\\[0.4em]
            {{\\bookpocket@chaptertitlefont \\MakeUppercase{{#1}}\\par}}
          }}\\par\\nobreak
          \\vskip 14\\p@
        \\fi
      \\fi
      \\interlinepenalty\\@M
    }}%
  }}
  \\renewcommand{{\\@makeschapterhead}}[1]{{%
    {{\\parindent\\z@\\normalfont
      \\vspace*{{{chapter_top_shift}}}
      \\interlinepenalty\\@M
      \\noindent\\parbox[t]{{\\textwidth}}{{\\raggedright{{\\bookpocket@chaptertitlefont \\MakeUppercase{{#1}}\\par}}}}\\par\\nobreak
      \\vskip 14\\p@
    }}%
  }}
}}
\\renewcommand\\section{{\\@startsection{{section}}{{1}}{{\\z@}}{{-2.2ex \\@plus -0.8ex \\@minus -.2ex}}{{{section_afterskip} \\@plus .15ex}}{{\\normalfont\\raggedright\\bookpocket@sectionfont}}}}
\\renewcommand\\subsection{{\\@startsection{{subsection}}{{2}}{{\\z@}}{{-1.8ex \\@plus -0.6ex \\@minus -.2ex}}{{{subsection_afterskip} \\@plus .1ex}}{{\\normalfont\\raggedright\\bookpocket@subsectionfont}}}}
\\renewcommand\\subsubsection{{\\@startsection{{subsubsection}}{{3}}{{\\z@}}{{-1.5ex \\@plus -0.4ex \\@minus -.2ex}}{{0.4ex \\@plus .08ex}}{{\\normalfont\\raggedright\\footnotesize\\bfseries}}}}
\\@ifpackageloaded{{caption}}{{\\captionsetup{{font=small,justification=raggedright,singlelinecheck=false}}}}{{}}
\\makeatother
"""

if "\\usepackage{fancyhdr}" in text or "\\pagestyle{fancy}" in text:
    header_block = f"""
\\setlength{{\\headheight}}{{{headheight}}}
\\newlength{{\\bookpocketheaderboxheight}}
\\setlength{{\\bookpocketheaderboxheight}}{{\\dimexpr\\headheight-{header_raise}-{header_clearance}\\relax}}
\\newcommand{{\\bookpocketoddheadbox}}[1]{{\\raisebox{{{header_raise}}}{{\\parbox[t][\\bookpocketheaderboxheight][t]{{{header_width}\\textwidth}}{{\\raggedright\\strut #1\\strut}}}}}}
\\newcommand{{\\bookpocketevenheadbox}}[1]{{\\raisebox{{{header_raise}}}{{\\parbox[t][\\bookpocketheaderboxheight][t]{{{header_width}\\textwidth}}{{\\raggedleft\\strut #1\\strut}}}}}}
"""
    if "\\bookpocketoddheadbox" not in text:
        tuning_block += header_block
    text = re.sub(r"\\setlength\{\\headheight\}\{[^}]*\}", rf"\\setlength{{\\headheight}}{{{headheight}}}", text, count=1)

text = text.replace("\\begin{document}", tuning_block + "\n\\begin{document}", 1)

lines = text.splitlines()
patched_lines = []
for line in lines:
    stripped = line.strip()
    if stripped.startswith("\\fancyhead[") and "\\thepage" not in stripped and stripped.endswith("}"):
        close_bracket = stripped.find("]")
        opts = stripped[len("\\fancyhead["):close_bracket]
        content = stripped[close_bracket + 2:-1]
        macro = None
        if opts in {"LO", "L"}:
            macro = "bookpocketoddheadbox"
        elif opts in {"RE", "R"}:
            macro = "bookpocketevenheadbox"
        if macro:
            indent = line[: len(line) - len(line.lstrip())]
            line = f"{indent}\\fancyhead[{opts}]{{\\nouppercase{{\\{macro}{{{content}}}}}}}"
    patched_lines.append(line)
text = "\n".join(patched_lines) + "\n"

cover_replacements = {
    "text width=0.72\\paperwidth": f"text width={title_width}\\paperwidth",
    "text width=0.7\\paperwidth": f"text width={title_width}\\paperwidth",
    "text width=0.70\\paperwidth": f"text width={title_width}\\paperwidth",
    "text width=0.68\\paperwidth": f"text width={note_width}\\paperwidth",
    "text width=0.62\\paperwidth": f"text width={note_width}\\paperwidth",
    "text width=0.6\\paperwidth": f"text width={note_width}\\paperwidth",
    "text width=0.58\\paperwidth": f"text width={note_width}\\paperwidth",
}
for old, new in cover_replacements.items():
    text = text.replace(old, new)

text = text.replace(
    "{\\fontsize{30}{33}\\selectfont",
    f"{{\\fontsize{{{cover_font_size}}}{{{cover_font_baseline}}}\\selectfont",
    1,
)
text = text.replace(
    "{\\fontsize{28}{31}\\selectfont",
    f"{{\\fontsize{{{cover_font_size}}}{{{cover_font_baseline}}}\\selectfont",
    1,
)
text = text.replace(
    "{\\fontsize{34}{38}\\selectfont",
    f"{{\\fontsize{{{manuscript_title_size}}}{{{manuscript_title_baseline}}}\\selectfont",
    1,
)
text = text.replace("{\\Large\\color{black!72}", "{\\normalsize\\color{black!72}")
text = text.replace("{\\large\\color{black!72}", "{\\small\\color{black!72}")
text = text.replace("{\\normalsize\\color{black!78}", "{\\small\\color{black!78}")
text = text.replace("\\vspace*{2.2cm}", "\\vspace*{1.6cm}", 1)
text = text.replace("\\vspace{1.6cm}", "\\vspace{1.15cm}", 1)
text = text.replace("\\vspace{1.4cm}", "\\vspace{1.0cm}", 1)
text = text.replace("\\mainmatter", "\\tikzset{every picture/.append style={scale=0.78,transform shape}}\n\\mainmatter", 1)

path.write_text(text, encoding="utf-8")
PY

: > "$log_path"
(
  cd "$tmp_compile_root"
  "$compile_engine" -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$tmp_main_argument" >>"$log_path" 2>&1
  "$compile_engine" -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$tmp_main_argument" >>"$log_path" 2>&1
)
