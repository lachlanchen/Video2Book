#!/usr/bin/env bash
set -uo pipefail

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="$(pwd)"
manifest=""
worker_session="video2book-editorial"
worker_log=""
interval=1800
model=""
reasoning=""
prompt_access=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root) repo_root="$2"; shift 2 ;;
    --manifest) manifest="$2"; shift 2 ;;
    --worker-session) worker_session="$2"; shift 2 ;;
    --worker-log) worker_log="$2"; shift 2 ;;
    --interval) interval="$2"; shift 2 ;;
    --model) model="$2"; shift 2 ;;
    --reasoning) reasoning="$2"; shift 2 ;;
    --prompt-access) prompt_access="$2"; shift 2 ;;
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
if [[ -z "$worker_log" ]]; then
  worker_log="$repo_root/.editorial-revision-work/queue/worker.log"
fi

state_file="$repo_root/.editorial-revision-work/queue/state.json"
watchdog_log="$repo_root/.editorial-revision-work/queue/watchdog.log"
mkdir -p "$(dirname "$worker_log")"

queue_status() {
  python3 - "$state_file" <<'PY'
from pathlib import Path
import json
import sys

path = Path(sys.argv[1])
if not path.exists():
    print("missing")
else:
    try:
        print(json.loads(path.read_text(encoding="utf-8")).get("status", "unknown"))
    except Exception:
        print("invalid")
PY
}

worker_is_live() {
  tmux has-session -t "$worker_session" 2>/dev/null || return 1
  [[ "$(tmux display-message -p -t "$worker_session:0.0" '#{pane_dead}' 2>/dev/null)" == "0" ]]
}

start_worker() {
  if tmux has-session -t "$worker_session" 2>/dev/null; then
    tmux kill-session -t "$worker_session" 2>/dev/null || true
  fi
  command=(
    python3 "$module_root/subtitles2notes/editorial_queue.py"
    --repo-root "$repo_root"
    --manifest "$manifest"
  )
  [[ -z "$model" ]] || command+=(--model "$model")
  [[ -z "$reasoning" ]] || command+=(--reasoning "$reasoning")
  [[ -z "$prompt_access" ]] || command+=(--prompt-access "$prompt_access")
  printf -v quoted_command '%q ' "${command[@]}"
  printf -v quoted_log '%q' "$worker_log"
  tmux new-session -d -s "$worker_session" "set -o pipefail; $quoted_command 2>&1 | tee -a $quoted_log"
  tmux set-option -t "$worker_session" remain-on-exit on
  printf '[%s] restarted worker session=%s\n' "$(date --iso-8601=seconds)" "$worker_session" | tee -a "$watchdog_log"
}

printf '[%s] watchdog started worker=%s interval=%ss\n' \
  "$(date --iso-8601=seconds)" "$worker_session" "$interval" | tee -a "$watchdog_log"

while true; do
  status="$(queue_status)"
  case "$status" in
    complete|complete_with_blocks)
      printf '[%s] terminal queue status=%s; watchdog exiting\n' \
        "$(date --iso-8601=seconds)" "$status" | tee -a "$watchdog_log"
      exit 0
      ;;
  esac
  if worker_is_live; then
    printf '[%s] worker live queue_status=%s\n' \
      "$(date --iso-8601=seconds)" "$status" >> "$watchdog_log"
  else
    printf '[%s] worker missing/dead queue_status=%s\n' \
      "$(date --iso-8601=seconds)" "$status" | tee -a "$watchdog_log"
    start_worker
  fi
  sleep "$interval"
done
