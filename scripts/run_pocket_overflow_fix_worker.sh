#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/run_pocket_overflow_fix_worker.sh [process options]

Wrap the course-by-course pocket overflow fixer in a self-healing loop. If the
queue process exits unexpectedly, restart it from the saved state file after a
short delay, without requiring a separate monitor tmux session.

Worker-only options:
  --restart-delay <seconds>  Delay before automatic restart (default: 15)
  --max-restarts <n>         Maximum automatic restarts before giving up (default: 8)
  -h, --help                 Show this help

All other arguments are forwarded to:
  scripts/process_course_pocket_overflow_fixes_one_by_one.sh
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${NOTES_REPO_ROOT:-$(pwd)}"
state_file="${VIDEO2BOOK_POCKET_OVERFLOW_STATE_FILE:-$repo_root/.lecture-notes-work/pocket_overflow_fix/queue_state.env}"
restart_delay=15
max_restarts=8
process_args=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --restart-delay)
      restart_delay="${2:-15}"
      shift 2
      ;;
    --max-restarts)
      max_restarts="${2:-8}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      process_args+=("$1")
      shift
      ;;
  esac
done

load_state() {
  unset STATE_STATUS CURRENT_COURSE NEXT_COURSE || true
  if [[ -f "$state_file" ]]; then
    # shellcheck disable=SC1090
    source "$state_file"
  fi
}

is_finished() {
  load_state
  [[ "${STATE_STATUS:-}" == "finished" && -z "${CURRENT_COURSE:-}" && -z "${NEXT_COURSE:-}" ]]
}

restart_count=0

while true; do
  if bash "$module_root/scripts/process_course_pocket_overflow_fixes_one_by_one.sh" "${process_args[@]}"; then
    exit 0
  fi

  if is_finished; then
    exit 0
  fi

  restart_count=$((restart_count + 1))
  if [[ "$restart_count" -gt "$max_restarts" ]]; then
    echo "worker restart limit reached ($max_restarts)" >&2
    exit 1
  fi

  echo "worker crashed; restarting in ${restart_delay}s (attempt ${restart_count}/${max_restarts})" >&2
  sleep "$restart_delay"
done
