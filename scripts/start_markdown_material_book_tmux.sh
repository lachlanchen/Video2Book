#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/start_markdown_material_book_tmux.sh [options]

Starts a tmux session that turns an ordered Markdown material folder into a
pocket-size TeX/PDF book.

Options:
  --session <name>         tmux session name
  --repo-root <path>       host repo root
  --material-root <path>   source material folder
  --output-dir <path>      generated book output folder
  --title <text>           book title
  --subtitle <text>        book subtitle
  --source-credit <text>   source credit line
  --curator <text>         curator/publisher line
  --language <text>        output language
  --model <name>           Codex model
  --reasoning <level>      low|medium|high|xhigh
  --max-items <n>          stop after n new source notes
  --no-compile             skip PDF compilation
  --commit-each            commit/push after each generated chapter
  --compile-engine <name>  xelatex, lualatex, or pdflatex
  --kill                   kill existing session and recreate
  --no-attach              do not attach after startup
  -h, --help               show help
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${MATERIAL_BOOK_REPO_ROOT:-$(pwd)}"
material_root="${MATERIAL_BOOK_SOURCE_DIR:-}"
output_dir="${MATERIAL_BOOK_OUTPUT_DIR:-}"
session="${MATERIAL_BOOK_SESSION:-material-book-writer}"
title="${MATERIAL_BOOK_TITLE:-}"
subtitle="${MATERIAL_BOOK_SUBTITLE:-}"
source_credit="${MATERIAL_BOOK_SOURCE_CREDIT:-}"
curator="${MATERIAL_BOOK_CURATOR:-LazyingArt LLC}"
language="${MATERIAL_BOOK_LANGUAGE:-English}"
model="${MATERIAL_BOOK_MODEL:-gpt-5.4}"
reasoning="${MATERIAL_BOOK_REASONING:-high}"
max_items="${MATERIAL_BOOK_MAX_ITEMS:-0}"
compile_engine="${MATERIAL_BOOK_COMPILE_ENGINE:-xelatex}"
no_compile=0
commit_each=0
kill_existing=0
attach=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --session) session="${2:-}"; shift 2 ;;
    --repo-root) repo_root="${2:-}"; shift 2 ;;
    --material-root) material_root="${2:-}"; shift 2 ;;
    --output-dir) output_dir="${2:-}"; shift 2 ;;
    --title) title="${2:-}"; shift 2 ;;
    --subtitle) subtitle="${2:-}"; shift 2 ;;
    --source-credit) source_credit="${2:-}"; shift 2 ;;
    --curator) curator="${2:-}"; shift 2 ;;
    --language) language="${2:-}"; shift 2 ;;
    --model) model="${2:-}"; shift 2 ;;
    --reasoning) reasoning="${2:-}"; shift 2 ;;
    --max-items) max_items="${2:-0}"; shift 2 ;;
    --no-compile) no_compile=1; shift ;;
    --commit-each) commit_each=1; shift ;;
    --compile-engine) compile_engine="${2:-xelatex}"; shift 2 ;;
    --kill) kill_existing=1; shift ;;
    --no-attach) attach=0; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 1 ;;
  esac
done

if [[ -z "$material_root" || -z "$output_dir" || -z "$title" ]]; then
  echo "--material-root, --output-dir, and --title are required." >&2
  exit 1
fi

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux not found." >&2
  exit 1
fi

repo_root="$(cd "$repo_root" && pwd)"
log_dir="$repo_root/.material-book-work/logs"
mkdir -p "$log_dir"
timestamp="$(date +%Y%m%d_%H%M%S)"
log_path="$log_dir/${session}_${timestamp}.log"

if tmux has-session -t "$session" 2>/dev/null; then
  if [[ "$kill_existing" -eq 1 ]]; then
    tmux kill-session -t "$session"
  else
    if [[ "$attach" -eq 1 ]]; then
      exec tmux attach -t "$session"
    fi
    echo "tmux session already running: $session"
    exit 0
  fi
fi

cmd=(
  python3 "$module_root/scripts/process_markdown_material_book.py"
  --repo-root "$repo_root"
  --material-root "$material_root"
  --output-dir "$output_dir"
  --title "$title"
  --curator "$curator"
  --language "$language"
  --model "$model"
  --reasoning "$reasoning"
  --max-items "$max_items"
  --compile-engine "$compile_engine"
)
if [[ -n "$subtitle" ]]; then
  cmd+=(--subtitle "$subtitle")
fi
if [[ -n "$source_credit" ]]; then
  cmd+=(--source-credit "$source_credit")
fi
if [[ "$no_compile" -eq 1 ]]; then
  cmd+=(--no-compile)
fi
if [[ "$commit_each" -eq 1 ]]; then
  cmd+=(--commit-each)
fi

printf -v cmd_string '%q ' "${cmd[@]}"
tmux new-session -d -s "$session" -c "$repo_root" "bash -lc 'cd \"$repo_root\" && set -o pipefail && $cmd_string 2>&1 | tee \"$log_path\"; status=\${PIPESTATUS[0]}; echo; echo \"material book worker exit status: \$status\"; echo \"tmux session kept open for inspection; exit the shell to close it.\"; exec bash'"
tmux rename-window -t "$session:0" "material-book"
tmux set-option -t "$session" -g mouse on

echo "tmux session: $session"
echo "log: $log_path"
echo "attach: tmux attach -t $session"

if [[ "$attach" -eq 1 ]]; then
  exec tmux attach -t "$session"
fi
