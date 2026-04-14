#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/start_book_translation_tmux.sh [options]

Starts a tmux session for chapter-by-chapter translated book generation.

Options:
  --book-root <rel>       book root relative to the repo root
  --language <code>       zh or jp
  --session <name>        tmux session name (default: <book>-translate-<lang>)
  --model <name>          Codex model
  --reasoning <level>     low|medium|high|xhigh
  --max-units <n>         stop after n translation units
  --branch <name>         push branch (default: current branch or main)
  --no-commit             skip git commit/push checkpoints
  --kill                  kill an existing session and recreate it
  --no-attach             do not attach after startup
  -h, --help              show help
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${NOTES_REPO_ROOT:-$(pwd)}"
book_root=""
language=""
session=""
model="${BOOK_TRANSLATION_MODEL:-gpt-5.4}"
reasoning="${BOOK_TRANSLATION_REASONING:-high}"
max_units=0
branch="${BOOK_TRANSLATION_BRANCH:-$(git -C "$repo_root" branch --show-current 2>/dev/null || true)}"
do_commit=1
kill_existing=0
attach=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --book-root)
      book_root="${2:-}"
      shift 2
      ;;
    --language)
      language="${2:-}"
      shift 2
      ;;
    --session)
      session="${2:-}"
      shift 2
      ;;
    --model)
      model="${2:-}"
      shift 2
      ;;
    --reasoning)
      reasoning="${2:-}"
      shift 2
      ;;
    --max-units)
      max_units="${2:-0}"
      shift 2
      ;;
    --branch)
      branch="${2:-}"
      shift 2
      ;;
    --no-commit)
      do_commit=0
      shift
      ;;
    --kill)
      kill_existing=1
      shift
      ;;
    --no-attach)
      attach=0
      shift
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

if [[ -z "$book_root" || -z "$language" ]]; then
  usage >&2
  exit 1
fi

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux not found." >&2
  exit 1
fi

book_slug="$(basename "$book_root")"
if [[ -z "$session" ]]; then
  session="${book_slug}-translate-${language}"
fi
if [[ -z "$branch" ]]; then
  branch="main"
fi

log_dir="$repo_root/$book_root/.translation-work/logs"
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

cmd=(bash "$module_root/scripts/process_book_translation_one_by_one.sh" --book-root "$book_root" --language "$language" --model "$model" --reasoning "$reasoning" --branch "$branch")
if [[ "$max_units" -gt 0 ]]; then
  cmd+=(--max-units "$max_units")
fi
if [[ "$do_commit" -eq 0 ]]; then
  cmd+=(--no-commit)
fi

env_exports="export NOTES_REPO_ROOT=\"$repo_root\"; "
tmux new-session -d -s "$session" -c "$repo_root" "bash -lc 'cd \"$repo_root\" && ${env_exports}${cmd[*]} 2>&1 | tee \"$log_path\"'"
tmux rename-window -t "$session:0" "translate"
tmux set-option -t "$session" -g mouse on

echo "tmux session: $session"
echo "log: $log_path"
echo "attach: tmux attach -t $session"

if [[ "$attach" -eq 1 ]]; then
  exec tmux attach -t "$session"
fi
