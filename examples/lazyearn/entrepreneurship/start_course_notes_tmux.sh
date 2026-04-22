#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$script_dir/../common.sh"
load_lazyearn_course_env "$script_dir"

export NOTES_REPO_ROOT="$HOST_REPO_ROOT"
export NOTE_SOURCE_ROOT="$TRANSCRIPTION_SOURCE_ROOT"
export NOTE_TMUX_SESSION_NAME="$NOTES_SESSION"
export NOTE_CODEX_SESSION_FILE="${NOTE_CODEX_SESSION_FILE:-$HOST_REPO_ROOT/.lecture-notes-work/codex_sessions/$NOTES_SESSION.session_id}"
export NOTE_CODEX_SESSION_DOC_FILE="${NOTE_CODEX_SESSION_DOC_FILE:-$HOST_REPO_ROOT/.lecture-notes-work/codex_sessions/$NOTES_SESSION.session.md}"
export VIDEO2BOOK_COURSE_CONFIG="$COURSE_CONFIG_PATH"
export VIDEO2BOOK_REFERENCE_PDF_DIR="${VIDEO2BOOK_REFERENCE_PDF_DIR:-$HOST_REPO_ROOT/references/course-books/$COURSE_SLUG}"

note_model="${NOTE_MODEL:-$NOTE_MODEL_DEFAULT}"
note_reasoning="${NOTE_REASONING:-$NOTE_REASONING_DEFAULT}"
note_session_scope="${NOTE_CODEX_SESSION_SCOPE:-$NOTE_SESSION_SCOPE_DEFAULT}"

cd "$HOST_REPO_ROOT"
exec bash "$VIDEO2BOOK_ROOT/scripts/start_course_notes_tmux.sh" \
  --session "$NOTES_SESSION" \
  --course "$COURSE_REL" \
  --model "$note_model" \
  --reasoning "$note_reasoning" \
  --session-scope "$note_session_scope" \
  --allow-partial-course \
  "$@"
