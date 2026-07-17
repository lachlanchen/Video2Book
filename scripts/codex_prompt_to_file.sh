#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 5 ]]; then
  echo "Usage: $0 <repo_path> <prompt_file> <output_file> <model> <reasoning> [<image> ...]" >&2
  exit 1
fi

repo_path="$1"
prompt_file="$2"
output_file="$3"
model="$4"
reasoning="$5"
shift 5
session_file="${CODEX_SHARED_SESSION_FILE:-}"
session_doc_file="${CODEX_SHARED_SESSION_DOC_FILE:-}"
tmux_session_name="${NOTE_TMUX_SESSION_NAME:-susskind-notes}"
session_scope="${NOTE_CODEX_SESSION_SCOPE:-global}"
prompt_access="${CODEX_PROMPT_ACCESS:-danger-full-access}"
disable_shell_snapshot="${CODEX_DISABLE_SHELL_SNAPSHOT:-false}"
prompt_timeout_seconds="${CODEX_PROMPT_TIMEOUT_SECONDS:-1800}"
codex_config=(
  -c "model_reasoning_effort=\"$reasoning\""
)
if [[ "$disable_shell_snapshot" == "true" ]]; then
  codex_config+=(-c "features.shell_snapshot=false")
fi

extract_session_id() {
  python3 - "$1" <<'PY'
import json
import sys

path = sys.argv[1]
with open(path, encoding="utf-8", errors="replace") as handle:
    for line in handle:
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        if data.get("type") == "session_meta":
            payload = data.get("payload", {})
            session_id = payload.get("id")
            if session_id:
                print(session_id)
                break
        if data.get("type") == "thread.started":
            thread_id = data.get("thread_id")
            if thread_id:
                print(thread_id)
                break
PY
}

write_session_doc() {
  local session_id="$1"
  local target="$2"
  [[ -n "$target" ]] || return 0
  mkdir -p "$(dirname "$target")"
  cat > "$target" <<EOF
# Shared Codex Session

- tmux session: $tmux_session_name
- codex session id: $session_id
- codex session file: $session_file
- codex session scope: $session_scope
- prompt access: $prompt_access
- repo root: $repo_path
- model: $model
- updated at: $(date --iso-8601=seconds)
EOF
}

if [[ "$prompt_access" != "danger-full-access" && "$prompt_access" != "read-only" ]]; then
  echo "CODEX_PROMPT_ACCESS must be danger-full-access or read-only" >&2
  exit 2
fi
if [[ ! "$prompt_timeout_seconds" =~ ^[1-9][0-9]*$ ]]; then
  echo "CODEX_PROMPT_TIMEOUT_SECONDS must be a positive integer" >&2
  exit 2
fi

if [[ -n "$session_file" ]]; then
  mkdir -p "$(dirname "$session_file")"
  if [[ -z "$session_doc_file" ]]; then
    session_doc_file="${session_file%.session_id}.session.md"
  fi
fi

session_access_file="${session_file:+${session_file}.access}"
if [[ -n "$session_file" && -s "$session_file" ]]; then
  recorded_access=""
  if [[ -n "$session_access_file" && -s "$session_access_file" ]]; then
    recorded_access="$(tr -d '[:space:]' < "$session_access_file")"
  fi
  if [[ "$recorded_access" != "$prompt_access" ]]; then
    echo "Refusing to resume Codex session with access '$recorded_access'; requested '$prompt_access'. Reset the session file to create a correctly sandboxed session." >&2
    exit 3
  fi
fi

jsonl_file="$(mktemp)"
trap 'rm -f "$jsonl_file"' EXIT

if [[ -n "$session_file" && -s "$session_file" ]]; then
  session_id="$(tr -d '[:space:]' < "$session_file")"
  cmd=(
    codex
    exec
    resume
    --json
    -m "$model"
    "${codex_config[@]}"
    -o "$output_file"
  )
else
  cmd=(
    codex
    exec
    --json
    -m "$model"
    "${codex_config[@]}"
    -C "$repo_path"
    -o "$output_file"
  )
  if [[ "$prompt_access" == "read-only" ]]; then
    cmd+=(--sandbox read-only)
  else
    cmd+=(--dangerously-bypass-approvals-and-sandbox)
  fi
fi

for image in "$@"; do
  cmd+=(--image "$image")
done

if [[ -n "${session_id:-}" ]]; then
  cmd+=("$session_id" -)
else
  cmd+=(-)
fi

set +e
timeout --signal=TERM --kill-after=30s "$prompt_timeout_seconds" \
  "${cmd[@]}" < "$prompt_file" > "$jsonl_file"
status=$?
set -e

if [[ "$status" -eq 124 || "$status" -eq 137 ]]; then
  echo "Codex prompt timed out after ${prompt_timeout_seconds}s" >&2
fi

if [[ -n "$session_file" && ! -s "$session_file" ]]; then
  new_session_id="$(extract_session_id "$jsonl_file")"
  if [[ -n "$new_session_id" ]]; then
    printf '%s\n' "$new_session_id" > "$session_file"
    printf '%s\n' "$prompt_access" > "$session_access_file"
    write_session_doc "$new_session_id" "$session_doc_file"
  fi
elif [[ -n "${session_id:-}" ]]; then
  write_session_doc "$session_id" "$session_doc_file"
fi

cat "$jsonl_file"
exit "$status"
