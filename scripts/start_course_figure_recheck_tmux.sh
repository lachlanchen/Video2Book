#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/start_course_figure_recheck_tmux.sh [options]

Starts a tmux session for course-by-course figure rechecking.

Options:
  --session <name>       tmux session name (default: susskind-figure-recheck)
  --repo-root <path>     Host notes repo root (default: current directory)
  --course <rel>         Restrict to one course
  --lecture-slug <slug>  Restrict to one lecture slug
  --figure-index <n>     Restrict to one figure index
  --model <name>         Codex model
  --reasoning <level>    low|medium|high|xhigh
  --report-only          Audit only; do not patch figures
  --force                Re-extract candidate frames even if cached
  --kill                 Kill existing session first
  --no-attach            Do not attach after startup
  -h, --help             Show help
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${NOTES_REPO_ROOT:-$(pwd)}"
session="susskind-figure-recheck"
course=""
lecture_slug=""
figure_index=""
model="${NOTE_MODEL:-gpt-5.4}"
reasoning="${NOTE_REASONING:-high}"
report_only=0
force=0
kill_existing=0
attach=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --session)
      session="${2:-}"
      shift 2
      ;;
    --repo-root)
      repo_root="${2:-}"
      shift 2
      ;;
    --course)
      course="${2:-}"
      shift 2
      ;;
    --lecture-slug)
      lecture_slug="${2:-}"
      shift 2
      ;;
    --figure-index)
      figure_index="${2:-}"
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
    --report-only)
      report_only=1
      shift
      ;;
    --force)
      force=1
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

cmd=(bash "$module_root/scripts/process_course_figure_rechecks_one_by_one.sh" --repo-root "$repo_root" --model "$model" --reasoning "$reasoning")
if [[ -n "$course" ]]; then
  cmd+=(--course "$course")
fi
if [[ -n "$lecture_slug" ]]; then
  cmd+=(--lecture-slug "$lecture_slug")
fi
if [[ -n "$figure_index" ]]; then
  cmd+=(--figure-index "$figure_index")
fi
if [[ "$report_only" -eq 1 ]]; then
  cmd+=(--report-only)
fi
if [[ "$force" -eq 1 ]]; then
  cmd+=(--force)
fi

env_exports="export NOTES_REPO_ROOT=\"$repo_root\"; "
if [[ -n "${NOTE_SOURCE_ROOT:-}" ]]; then
  env_exports+="export NOTE_SOURCE_ROOT=\"${NOTE_SOURCE_ROOT}\"; "
fi

tmux new-session -d -s "$session" -c "$repo_root" "bash -lc 'cd \"$repo_root\" && set -o pipefail && ${env_exports}${cmd[*]} 2>&1 | tee \"$log_path\"; status=\${PIPESTATUS[0]}; echo; echo \"figure recheck worker exit status: \$status\"; echo \"tmux session kept open for inspection; exit the shell to close it.\"; exec bash'"
tmux rename-window -t "$session:0" "figure-recheck"
tmux set-option -t "$session" -g mouse on

echo "tmux session: $session"
echo "log: $log_path"
echo "attach: tmux attach -t $session"

if [[ "$attach" -eq 1 ]]; then
  exec tmux attach -t "$session"
fi
