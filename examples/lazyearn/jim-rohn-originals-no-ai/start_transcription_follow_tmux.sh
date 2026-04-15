#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$script_dir/../common.sh"
load_lazyearn_course_env "$script_dir"

state_root="${HOST_REPO_ROOT}/.video2book-state/${COURSE_REL}"
export DOWNLOAD_DONE_FILE="${DOWNLOAD_DONE_FILE:-$state_root/download.done}"
export TRANSCRIPTION_FOLLOW_DONE_FILE="${TRANSCRIPTION_FOLLOW_DONE_FILE:-$state_root/transcription.done}"
export TRANSCRIPTION_FOLLOW_SESSION="${TRANSCRIPTION_FOLLOW_SESSION:-${TRANSCRIPTION_SESSION}-follow}"

mkdir -p "$(dirname "$DOWNLOAD_DONE_FILE")"
rm -f "$DOWNLOAD_DONE_FILE" "$TRANSCRIPTION_FOLLOW_DONE_FILE"

export TRANSCRIPTION_REPO_ROOT="$HOST_REPO_ROOT"
export SOURCE_ROOT="$TRANSCRIPTION_SOURCE_ROOT"
export SOURCE_SUBDIR="$TRANSCRIPTION_SOURCE_SUBDIR"
export TRANSCRIPTION_GIT_PATHS="$TRANSCRIPTION_GIT_PATHS"

cd "$HOST_REPO_ROOT"
exec bash "$VIDEO2BOOK_ROOT/scripts/start_transcription_follow_tmux.sh" "$TRANSCRIPTION_FOLLOW_SESSION"
