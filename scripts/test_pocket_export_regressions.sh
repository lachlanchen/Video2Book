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

# A copied historical PDF must never survive a failed current compile and be
# mistaken for a successful export.
broken_source="$tmp_dir/broken-source"
broken_compile="$tmp_dir/broken-compile"
mkdir -p "$broken_source/build"
cp "$compile_root/build/main.pdf" "$broken_source/build/main.pdf"
cp "$source_root/main.tex" "$broken_source/main.tex"
cat >"$broken_source/common.tex" <<'TEX'
\input{missing-pocket-regression-file.tex}
TEX

if "$repo_root/scripts/build_tex_book_pocket_variant.sh" \
  --source-root "$broken_source" \
  --main-tex main.tex \
  --compile-root "$broken_compile" \
  --build-dir "$broken_compile/build" \
  --log-path "$broken_compile/compile.log" \
  --font-mode onepointtwo \
  --paper-width 6in \
  --paper-height 9in \
  --margin 0.55in \
  --compile-engine pdflatex; then
  echo "broken pocket source unexpectedly succeeded" >&2
  exit 1
fi

test ! -e "$broken_compile/build/main.pdf"

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
