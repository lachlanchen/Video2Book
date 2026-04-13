#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$script_dir/../common.sh"
load_lazyearn_course_env "$script_dir"

export NOTES_REPO_ROOT="$HOST_REPO_ROOT"
export VIDEO2BOOK_COURSE_CONFIG="$COURSE_CONFIG_PATH"
export VIDEO2BOOK_REFERENCE_PDF_DIR="${VIDEO2BOOK_REFERENCE_PDF_DIR:-$HOST_REPO_ROOT/references/course-books/$COURSE_SLUG}"

note_monitor_model="${NOTE_MONITOR_MODEL:-$NOTE_MONITOR_MODEL_DEFAULT}"
note_monitor_reasoning="${NOTE_MONITOR_REASONING:-$NOTE_MONITOR_REASONING_DEFAULT}"
note_session_scope="${NOTE_CODEX_SESSION_SCOPE:-$NOTE_SESSION_SCOPE_DEFAULT}"

cd "$HOST_REPO_ROOT"
exec bash "$VIDEO2BOOK_ROOT/scripts/start_course_notes_monitor_tmux.sh" \
  --session "$NOTES_MONITOR_SESSION" \
  --target-session "$NOTES_SESSION" \
  --model "$note_monitor_model" \
  --reasoning "$note_monitor_reasoning" \
  --course "$COURSE_REL" \
  --notes-session-scope "$note_session_scope" \
  "$@"
