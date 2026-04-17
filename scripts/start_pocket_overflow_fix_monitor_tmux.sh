#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/start_pocket_overflow_fix_monitor_tmux.sh [options]

Starts a tmux monitor session for the pocket-overflow worker.

Options:
  --session <name>          Monitor tmux session name (default: susskind-pocket-fix-monitor)
  --worker-session <name>   Worker tmux session name (default: susskind-pocket-fix)
  --interval <seconds>      Monitor poll interval (default: 300)
  --host-root <path>        Host repo root (default: current directory)
  --start-course <relpath>  Initial fallback start course
  --model <name>            Codex model for worker restarts
  --reasoning <level>       Codex reasoning for worker restarts
  --size <preset>           penguin|a5|custom (default: penguin)
  --font-mode <mode>        normal|onepointtwo|onehalf|double (default: onepointtwo)
  --max-iterations <n>      Max iterations per course (default: 4)
  --kill                    Kill existing monitor session before starting
  --no-attach               Do not attach after startup
  -h, --help                Show this help
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${NOTES_REPO_ROOT:-$(pwd)}"
session="susskind-pocket-fix-monitor"
worker_session="susskind-pocket-fix"
interval=300
start_course=""
model="${NOTE_MODEL:-gpt-5.4}"
reasoning="${NOTE_REASONING:-medium}"
size_preset="penguin"
font_mode="onepointtwo"
max_iterations=4
kill_existing=0
attach=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --session)
      session="${2:-}"
      shift 2
      ;;
    --worker-session)
      worker_session="${2:-}"
      shift 2
      ;;
    --interval)
      interval="${2:-300}"
      shift 2
      ;;
    --host-root)
      repo_root="${2:-}"
      shift 2
      ;;
    --start-course)
      start_course="${2:-}"
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
    --size)
      size_preset="${2:-}"
      shift 2
      ;;
    --font-mode)
      font_mode="${2:-}"
      shift 2
      ;;
    --max-iterations)
      max_iterations="${2:-4}"
      shift 2
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

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux not found." >&2
  exit 1
fi

log_dir="$repo_root/.lecture-notes-work/logs"
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
  bash "$module_root/scripts/monitor_pocket_overflow_fix.sh"
  --session "$worker_session"
  --interval "$interval"
  --host-root "$repo_root"
  --model "$model"
  --reasoning "$reasoning"
  --size "$size_preset"
  --font-mode "$font_mode"
  --max-iterations "$max_iterations"
)
if [[ -n "$start_course" ]]; then
  cmd+=(--start-course "$start_course")
fi

env_exports="export NOTES_REPO_ROOT=\"$repo_root\"; "
if [[ -n "${VIDEO2BOOK_POST_OVERFLOW_FIX_HOOK:-}" ]]; then
  env_exports+="export VIDEO2BOOK_POST_OVERFLOW_FIX_HOOK=\"${VIDEO2BOOK_POST_OVERFLOW_FIX_HOOK}\"; "
fi
if [[ -n "${VIDEO2BOOK_POCKET_OVERFLOW_STATE_FILE:-}" ]]; then
  env_exports+="export VIDEO2BOOK_POCKET_OVERFLOW_STATE_FILE=\"${VIDEO2BOOK_POCKET_OVERFLOW_STATE_FILE}\"; "
fi

tmux new-session -d -s "$session" -c "$repo_root" "bash -lc 'cd \"$repo_root\" && ${env_exports}${cmd[*]} 2>&1 | tee \"$log_path\"'"
tmux rename-window -t "$session:0" "monitor"
tmux set-option -t "$session" -g mouse on

echo "tmux monitor session: $session"
echo "log: $log_path"
echo "attach: tmux attach -t $session"

if [[ "$attach" -eq 1 ]]; then
  exec tmux attach -t "$session"
fi
