#!/usr/bin/env bash
set -euo pipefail

load_lazylearn_course_env() {
  local script_dir="$1"
  export VIDEO2BOOK_EXAMPLE_DIR="$(cd "$script_dir" && pwd)"
  export VIDEO2BOOK_ROOT="$(cd "$VIDEO2BOOK_EXAMPLE_DIR/../../.." && pwd)"
  export HOST_REPO_ROOT="${HOST_REPO_ROOT:-$(pwd)}"

  # shellcheck source=/dev/null
  source "$VIDEO2BOOK_EXAMPLE_DIR/course.env"

  export COURSE_REL="${COURSE_NAMESPACE}/${COURSE_SLUG}"
  export DOWNLOAD_ROOT="${DOWNLOAD_ROOT:-$HOST_REPO_ROOT/downloads}"
  export DOWNLOAD_SUBDIR="${DOWNLOAD_SUBDIR:-$COURSE_REL}"
  export DOWNLOAD_LOG_ROOT="${DOWNLOAD_LOG_ROOT:-$HOST_REPO_ROOT/downloads/logs/$COURSE_NAMESPACE/$COURSE_SLUG}"
  export COURSE_CONFIG_PATH="${COURSE_CONFIG_PATH:-$VIDEO2BOOK_EXAMPLE_DIR/course.json}"
  export TRANSCRIPTION_SOURCE_ROOT="${TRANSCRIPTION_SOURCE_ROOT:-$DOWNLOAD_ROOT}"
  export TRANSCRIPTION_SOURCE_SUBDIR="${TRANSCRIPTION_SOURCE_SUBDIR:-$COURSE_REL}"
}
