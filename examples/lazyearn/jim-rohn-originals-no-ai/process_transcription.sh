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
export TRANSCRIBE_MODEL="${TRANSCRIBE_MODEL:-$TRANSCRIBE_MODEL_DEFAULT}"

cd "$HOST_REPO_ROOT"
exec bash "$VIDEO2BOOK_ROOT/scripts/process_videos_one_by_one.sh"
