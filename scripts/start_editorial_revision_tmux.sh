#!/usr/bin/env bash
set -euo pipefail

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${NOTES_REPO_ROOT:-$(pwd)}"
session="${EDITORIAL_TMUX_SESSION:-video2book-editorial}"
log_file=""
forwarded=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root)
      repo_root="$2"
      forwarded+=("$1" "$2")
      shift 2
      ;;
    --session)
      session="$2"
      shift 2
      ;;
    --log)
      log_file="$2"
      shift 2
      ;;
    *)
      forwarded+=("$1")
      shift
      ;;
  esac
done

repo_root="$(cd "$repo_root" && pwd)"
if [[ -z "$log_file" ]]; then
  log_file="$repo_root/.editorial-revision-work/editorial.log"
fi
mkdir -p "$(dirname "$log_file")"

if tmux has-session -t "$session" 2>/dev/null; then
  echo "tmux session already exists: $session" >&2
  exit 1
fi

command=(bash "$module_root/scripts/process_editorial_revision_one_by_one.sh" "${forwarded[@]}")
printf -v quoted_command '%q ' "${command[@]}"
printf -v quoted_log '%q' "$log_file"
tmux new-session -d -s "$session" "set -o pipefail; $quoted_command 2>&1 | tee -a $quoted_log"
tmux set-option -t "$session" remain-on-exit on

echo "Started tmux session: $session"
echo "Attach: tmux attach -t $session"
echo "Log: $log_file"
