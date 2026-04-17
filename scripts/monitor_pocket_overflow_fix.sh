#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/monitor_pocket_overflow_fix.sh [options]

Watch the pocket-overflow tmux worker. If it exits, restart it from the last
recorded course state.

Options:
  --session <name>          Worker tmux session name (default: susskind-pocket-fix)
  --interval <seconds>      Poll interval (default: 300)
  --host-root <path>        Host repo root (default: current directory)
  --start-course <relpath>  Initial fallback start course if no state exists
  --model <name>            Codex model for worker restarts
  --reasoning <level>       Codex reasoning for worker restarts
  --size <preset>           penguin|a5|custom (default: penguin)
  --font-mode <mode>        normal|onepointtwo|onehalf|double (default: onepointtwo)
  --max-iterations <n>      Max iterations per course (default: 4)
  -h, --help                Show this help
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${NOTES_REPO_ROOT:-$(pwd)}"
worker_session="susskind-pocket-fix"
interval=300
start_course=""
model="${NOTE_MODEL:-gpt-5.4}"
reasoning="${NOTE_REASONING:-medium}"
size_preset="penguin"
font_mode="onepointtwo"
max_iterations=4
state_file="${VIDEO2BOOK_POCKET_OVERFLOW_STATE_FILE:-$repo_root/.lecture-notes-work/pocket_overflow_fix/queue_state.env}"
post_fix_hook="${VIDEO2BOOK_POST_OVERFLOW_FIX_HOOK:-}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --session)
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

log_dir="$repo_root/.lecture-notes-work/logs"
mkdir -p "$log_dir"
monitor_log="$log_dir/${worker_session}-monitor_$(date +%Y%m%d_%H%M%S).log"

log() {
  printf '[%s] %s\n' "$(date --iso-8601=seconds)" "$*" | tee -a "$monitor_log"
}

load_state() {
  unset STATE_STATUS CURRENT_COURSE LAST_COMPLETED_COURSE NEXT_COURSE START_COURSE || true
  if [[ -f "$state_file" ]]; then
    # shellcheck disable=SC1090
    source "$state_file"
  fi
}

determine_resume_course() {
  load_state
  if [[ -n "${CURRENT_COURSE:-}" ]]; then
    printf '%s\n' "$CURRENT_COURSE"
    return
  fi
  if [[ -n "${NEXT_COURSE:-}" ]]; then
    printf '%s\n' "$NEXT_COURSE"
    return
  fi
  if [[ -n "$start_course" ]]; then
    printf '%s\n' "$start_course"
    return
  fi
}

should_restart() {
  load_state
  if [[ "${STATE_STATUS:-}" == "finished" && -z "${NEXT_COURSE:-}" && -z "${CURRENT_COURSE:-}" ]]; then
    return 1
  fi
  return 0
}

restart_worker() {
  local resume_course="$1"
  local cmd=(
    bash "$module_root/scripts/start_pocket_overflow_fix_tmux.sh"
    --session "$worker_session"
    --model "$model"
    --reasoning "$reasoning"
    --size "$size_preset"
    --font-mode "$font_mode"
    --max-iterations "$max_iterations"
    --no-attach
  )
  if [[ -n "$resume_course" ]]; then
    cmd+=(--start-course "$resume_course")
  fi
  log "restarting worker session=$worker_session resume_course=${resume_course:-<start>}"
  VIDEO2BOOK_POST_OVERFLOW_FIX_HOOK="$post_fix_hook" \
  VIDEO2BOOK_POCKET_OVERFLOW_STATE_FILE="$state_file" \
  "${cmd[@]}" >>"$monitor_log" 2>&1
}

log "monitoring worker=$worker_session interval=${interval}s state_file=$state_file"

while true; do
  if tmux has-session -t "$worker_session" 2>/dev/null; then
    log "worker alive"
  else
    if should_restart; then
      resume_course="$(determine_resume_course)"
      restart_worker "$resume_course" || log "worker restart failed"
    else
      log "worker absent and queue state is finished; not restarting"
    fi
  fi
  sleep "$interval"
done
