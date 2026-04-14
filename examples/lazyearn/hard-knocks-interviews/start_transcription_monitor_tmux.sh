#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$script_dir/../common.sh"
load_lazyearn_course_env "$script_dir"

export TRANSCRIPTION_REPO_ROOT="$HOST_REPO_ROOT"
export SOURCE_ROOT="$TRANSCRIPTION_SOURCE_ROOT"
export SOURCE_SUBDIR="$TRANSCRIPTION_SOURCE_SUBDIR"
export TRANSCRIPTION_GIT_PATHS="$TRANSCRIPTION_GIT_PATHS"

cd "$HOST_REPO_ROOT"
exec bash "$VIDEO2BOOK_ROOT/scripts/start_transcription_monitor_tmux.sh" "$TRANSCRIPTION_MONITOR_SESSION" "$TRANSCRIPTION_SESSION"
