#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/export_tex_book_pocket_pdf.sh --repo-root <path> --project-root <path> --main-tex <file> [options]

Export a standalone LaTeX book/article into a compact pocket-size PDF.

Options:
  --repo-root <path>         Host repo root (required)
  --project-root <path>      Project root containing the TeX sources and relative assets (required)
  --main-tex <file>          Main TeX file relative to project root; may live in a subdirectory such as zh/book_zh.tex (required)
  --output-pdf <path>        Destination PDF in the host repo (default: <project-root>/<base>_<suffix>.pdf)
  --docs-output-pdf <path>   Optional docs mirror PDF path
  --overflow-report <path>   Optional Markdown overflow report path
  --size <preset>            penguin (6x9, default), a5, or custom
  --font-mode <mode>         normal (default) or onepointtwo
  --paper-width <size>       Custom width for --size custom, e.g. 6in
  --paper-height <size>      Custom height for --size custom, e.g. 9in
  --margin <size>            Custom geometry margin for --size custom, e.g. 0.55in
  --suffix <suffix>          Output suffix (default: pocket)
  --compile-engine <name>    xelatex (default), lualatex, or pdflatex
  --nutstore-pdf <path>      Optional extra sync target PDF path
  -h, --help                 Show this help text
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root=""
project_root=""
main_tex=""
output_pdf=""
docs_output_pdf=""
overflow_report=""
nutstore_pdf=""
size_preset="penguin"
font_mode="normal"
paper_width="6in"
paper_height="9in"
geometry_margin="0.55in"
suffix="pocket"
compile_engine="xelatex"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root)
      repo_root="${2:-}"
      shift 2
      ;;
    --project-root)
      project_root="${2:-}"
      shift 2
      ;;
    --main-tex)
      main_tex="${2:-}"
      shift 2
      ;;
    --output-pdf)
      output_pdf="${2:-}"
      shift 2
      ;;
    --docs-output-pdf)
      docs_output_pdf="${2:-}"
      shift 2
      ;;
    --overflow-report)
      overflow_report="${2:-}"
      shift 2
      ;;
    --size)
      size_preset="${2:-}"
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
    --suffix)
      suffix="${2:-}"
      shift 2
      ;;
    --compile-engine)
      compile_engine="${2:-}"
      shift 2
      ;;
    --nutstore-pdf)
      nutstore_pdf="${2:-}"
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

if [[ -z "$repo_root" || -z "$project_root" || -z "$main_tex" ]]; then
  echo "--repo-root, --project-root, and --main-tex are required." >&2
  exit 1
fi

repo_root="$(cd "$repo_root" && pwd)"
project_root="$(cd "$project_root" && pwd)"

case "$size_preset" in
  penguin)
    paper_width="6in"
    paper_height="9in"
    geometry_margin="0.55in"
    ;;
  a5)
    paper_width="5.83in"
    paper_height="8.27in"
    geometry_margin="0.52in"
    ;;
  custom)
    if [[ -z "$paper_width" || -z "$paper_height" || -z "$geometry_margin" ]]; then
      echo "Custom size requires --paper-width, --paper-height, and --margin." >&2
      exit 1
    fi
    ;;
  *)
    echo "Unknown size preset: $size_preset" >&2
    exit 1
    ;;
esac

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

for command in "$compile_engine" python3; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "Required command not found: $command" >&2
    exit 1
  fi
done

if [[ ! -f "$project_root/$main_tex" ]]; then
  echo "Main TeX file not found: $project_root/$main_tex" >&2
  exit 1
fi

base_name="$(basename "${main_tex%.tex}")"
main_dir_rel="$(dirname "$main_tex")"
if [[ "$main_dir_rel" == "." ]]; then
  main_dir_rel=""
fi
project_compile_root="$project_root"
if [[ -n "$main_dir_rel" ]]; then
  project_compile_root="$project_root/$main_dir_rel"
fi

if [[ -z "$output_pdf" ]]; then
  output_pdf="$project_root/${base_name}_${suffix}.pdf"
fi

if [[ -z "$docs_output_pdf" ]]; then
  repo_investment_root="$repo_root/investment_pdfs"
  if [[ "$project_root" == "$repo_investment_root"* ]]; then
    rel_dir="${project_root#"$repo_investment_root"/}"
    docs_output_pdf="$repo_root/docs/investment_pdfs/$rel_dir/${base_name}_${suffix}.pdf"
  fi
fi

if [[ -z "$overflow_report" ]]; then
  overflow_report="$project_root/${base_name}_${suffix}_overflow.md"
fi

mkdir -p "$(dirname "$output_pdf")"
if [[ -n "$docs_output_pdf" ]]; then
  mkdir -p "$(dirname "$docs_output_pdf")"
fi
if [[ -n "$nutstore_pdf" ]]; then
  mkdir -p "$(dirname "$nutstore_pdf")"
fi
mkdir -p "$(dirname "$overflow_report")"

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

cp -a "$project_root"/. "$tmp_dir"/
tmp_tex="$tmp_dir/$main_tex"
tmp_compile_root="$tmp_dir"
if [[ -n "$main_dir_rel" ]]; then
  tmp_compile_root="$tmp_dir/$main_dir_rel"
fi
tmp_main_basename="$(basename "$main_tex")"
build_dir="$tmp_compile_root/build"
mkdir -p "$build_dir"

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

tuning_block = f"""
\\setlength{{\\emergencystretch}}{{{stretch}}}
\\setlength{{\\hfuzz}}{{{hfuzz}}}
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

if "\\bookpocketoddheadbox" not in text:
    text = text.replace("\\begin{document}", tuning_block + "\n\\begin{document}", 1)
else:
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

path.write_text(text, encoding="utf-8")
PY

compile_log="$build_dir/${base_name}.log"
if ! (
  cd "$tmp_compile_root"
  "$compile_engine" -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$tmp_main_basename" >/tmp/export_tex_book_pocket_pdf.out 2>&1
); then
  cat /tmp/export_tex_book_pocket_pdf.out >&2
  exit 1
fi
if ! (
  cd "$tmp_compile_root"
  "$compile_engine" -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$tmp_main_basename" >/tmp/export_tex_book_pocket_pdf.out 2>&1
); then
  cat /tmp/export_tex_book_pocket_pdf.out >&2
  exit 1
fi

compiled_pdf="$build_dir/${base_name}.pdf"
if [[ ! -f "$compiled_pdf" ]]; then
  echo "Expected compiled PDF not found: $compiled_pdf" >&2
  exit 1
fi

cp "$compiled_pdf" "$output_pdf"
if [[ -n "$docs_output_pdf" ]]; then
  cp "$compiled_pdf" "$docs_output_pdf"
fi
if [[ -n "$nutstore_pdf" ]]; then
  cp "$compiled_pdf" "$nutstore_pdf"
fi

if [[ -f "$compile_log" ]]; then
  python3 "$module_root/scripts/report_latex_overfulls.py" \
    --log "$compile_log" \
    --compile-root "$tmp_compile_root" \
    --display-root "$project_compile_root" \
    --output "$overflow_report" \
    --variant-label "$(basename "$output_pdf")" >/dev/null
fi

printf 'exported %s\n' "$output_pdf"
if [[ -n "$docs_output_pdf" ]]; then
  printf 'synced docs %s\n' "$docs_output_pdf"
fi
if [[ -n "$nutstore_pdf" ]]; then
  printf 'synced nutstore %s\n' "$nutstore_pdf"
fi
