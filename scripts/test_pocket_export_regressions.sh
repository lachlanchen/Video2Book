#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

source_root="$tmp_dir/source"
compile_root="$tmp_dir/compile"
mkdir -p "$source_root"

cat >"$source_root/common.tex" <<'TEX'
\usepackage{fancyhdr}
\pagestyle{fancy}
TEX

# The main file deliberately inherits fancyhdr through an input file. Pocket
# header detection must still define every macro used when rewriting the heads.
cat >"$source_root/main.tex" <<'TEX'
\documentclass{book}
\input{common.tex}
\fancyhead[LO]{\leftmark}
\fancyhead[RE]{\rightmark}
\begin{document}
\chapter{A Long Chapter Title That Must Wrap Cleanly}
Pocket export regression fixture.
\end{document}
TEX

"$repo_root/scripts/build_tex_book_pocket_variant.sh" \
  --source-root "$source_root" \
  --main-tex main.tex \
  --compile-root "$compile_root" \
  --build-dir "$compile_root/build" \
  --log-path "$compile_root/compile.log" \
  --font-mode onepointtwo \
  --paper-width 6in \
  --paper-height 9in \
  --margin 0.55in \
  --compile-engine pdflatex

test -s "$compile_root/build/main.pdf"
test -s "$compile_root/compile.log"

"$repo_root/scripts/export_tex_book_pocket_pdf.sh" \
  --repo-root "$tmp_dir" \
  --project-root "$source_root" \
  --main-tex main.tex \
  --output-pdf "$tmp_dir/exported.pdf" \
  --size penguin \
  --font-mode onepointtwo \
  --compile-engine pdflatex

test -s "$tmp_dir/exported.pdf"
if command -v qpdf >/dev/null 2>&1; then
  qpdf --check "$compile_root/build/main.pdf" >/dev/null
  qpdf --check "$tmp_dir/exported.pdf" >/dev/null
fi

printf 'pocket export regressions: PASS\n'
