#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$script_dir/../common.sh"
load_leonardsusskind_archive_env "$script_dir"

export NOTES_REPO_ROOT="$HOST_REPO_ROOT"
export NOTE_SOURCE_ROOT="$TRANSCRIPTION_SOURCE_ROOT"
export NOTE_TMUX_SESSION_NAME="$NOTES_SESSION"
export NOTE_CODEX_SESSION_FILE="${NOTE_CODEX_SESSION_FILE:-$HOST_REPO_ROOT/.lecture-notes-work/codex_sessions/$NOTES_SESSION.session_id}"
export NOTE_CODEX_SESSION_DOC_FILE="${NOTE_CODEX_SESSION_DOC_FILE:-$HOST_REPO_ROOT/.lecture-notes-work/codex_sessions/$NOTES_SESSION.session.md}"

note_monitor_model="${NOTE_MONITOR_MODEL:-$NOTE_MONITOR_MODEL_DEFAULT}"
note_monitor_reasoning="${NOTE_MONITOR_REASONING:-$NOTE_MONITOR_REASONING_DEFAULT}"
note_session_scope="${NOTE_CODEX_SESSION_SCOPE:-$NOTE_SESSION_SCOPE_DEFAULT}"

cd "$HOST_REPO_ROOT"
exec bash "$VIDEO2BOOK_ROOT/scripts/start_course_notes_monitor_tmux.sh" \
  --session "$NOTES_MONITOR_SESSION" \
  --target-session "$NOTES_SESSION" \
  --model "$note_monitor_model" \
  --reasoning "$note_monitor_reasoning" \
  --notes-session-scope "$note_session_scope" \
  "$@"
