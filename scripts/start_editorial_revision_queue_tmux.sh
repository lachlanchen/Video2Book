#!/usr/bin/env bash
set -euo pipefail

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="$(pwd)"
manifest=""
session="video2book-editorial"
watchdog_session=""
log_file=""
watchdog_log=""
interval=1800
model=""
reasoning=""
no_watchdog=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root) repo_root="$2"; shift 2 ;;
    --manifest) manifest="$2"; shift 2 ;;
    --session) session="$2"; shift 2 ;;
    --watchdog-session) watchdog_session="$2"; shift 2 ;;
    --log) log_file="$2"; shift 2 ;;
    --watchdog-log) watchdog_log="$2"; shift 2 ;;
    --interval) interval="$2"; shift 2 ;;
    --model) model="$2"; shift 2 ;;
    --reasoning) reasoning="$2"; shift 2 ;;
    --no-watchdog) no_watchdog=1; shift ;;
    *) echo "Unknown option: $1" >&2; exit 2 ;;
  esac
done

repo_root="$(cd "$repo_root" && pwd)"
if [[ -z "$manifest" ]]; then
  echo "--manifest is required" >&2
  exit 2
fi
if [[ "$manifest" != /* ]]; then
  manifest="$repo_root/$manifest"
fi
watchdog_session="${watchdog_session:-${session}-watchdog}"
log_file="${log_file:-$repo_root/.editorial-revision-work/queue/worker.log}"
watchdog_log="${watchdog_log:-$repo_root/.editorial-revision-work/queue/watchdog.stdout.log}"
mkdir -p "$(dirname "$log_file")"

start_session() {
  local target="$1"
  shift
  local target_log="$1"
  shift
  if tmux has-session -t "$target" 2>/dev/null; then
    if [[ "$(tmux display-message -p -t "$target:0.0" '#{pane_dead}' 2>/dev/null)" == "0" ]]; then
      echo "tmux session already running: $target" >&2
      return 1
    fi
    tmux kill-session -t "$target"
  fi
  printf -v quoted_command '%q ' "$@"
  printf -v quoted_log '%q' "$target_log"
  tmux new-session -d -s "$target" "set -o pipefail; $quoted_command 2>&1 | tee -a $quoted_log"
  tmux set-option -t "$target" remain-on-exit on
}

worker=(
  python3 "$module_root/subtitles2notes/editorial_queue.py"
  --repo-root "$repo_root"
  --manifest "$manifest"
)
[[ -z "$model" ]] || worker+=(--model "$model")
[[ -z "$reasoning" ]] || worker+=(--reasoning "$reasoning")
start_session "$session" "$log_file" "${worker[@]}"

if [[ "$no_watchdog" -eq 0 ]]; then
  watchdog=(
    bash "$module_root/scripts/watch_editorial_revision_queue.sh"
    --repo-root "$repo_root"
    --manifest "$manifest"
    --worker-session "$session"
    --worker-log "$log_file"
    --interval "$interval"
  )
  [[ -z "$model" ]] || watchdog+=(--model "$model")
  [[ -z "$reasoning" ]] || watchdog+=(--reasoning "$reasoning")
  start_session "$watchdog_session" "$watchdog_log" "${watchdog[@]}"
fi

echo "Started worker: $session"
echo "Started watchdog: $watchdog_session"
echo "Worker log: $log_file"
echo "State: $repo_root/.editorial-revision-work/queue/state.json"
