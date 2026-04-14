#!/usr/bin/env bash
set -euo pipefail

load_lazyearn_course_env() {
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
  export TRANSCRIPTION_GIT_PATHS="${TRANSCRIPTION_GIT_PATHS:-subtitles/$COURSE_REL markdown/$COURSE_REL}"
}

run_lazyearn_playlist_download() {
  local playlist_id archive_file
  playlist_id="${PLAYLIST_URL#*list=}"
  playlist_id="${playlist_id%%&*}"
  archive_file="${DOWNLOAD_ARCHIVE_FILE:-$DOWNLOAD_LOG_ROOT/playlist_${playlist_id}.archive}"
  local forward_dry_run=""
  local arg
  for arg in "$@"; do
    if [[ "$arg" == "--dry-run" ]]; then
      forward_dry_run="--dry-run"
      break
    fi
  done

  mkdir -p "$DOWNLOAD_LOG_ROOT"

  if declare -p DEDUP_SOURCE_SUBDIRS >/dev/null 2>&1 && (( ${#DEDUP_SOURCE_SUBDIRS[@]} > 0 )); then
    local dedup_args=()
    local source_subdir
    for source_subdir in "${DEDUP_SOURCE_SUBDIRS[@]}"; do
      dedup_args+=(--source-subdir "$source_subdir")
    done
    python3 "$VIDEO2BOOK_ROOT/playlist2videos/link_playlist_duplicates.py" \
      --playlist-url "$PLAYLIST_URL" \
      --workspace "$YT_DLP_WORKSPACE" \
      --download-root "$DOWNLOAD_ROOT" \
      --download-subdir "$DOWNLOAD_SUBDIR" \
      --archive-file "$archive_file" \
      ${forward_dry_run:+$forward_dry_run} \
      "${dedup_args[@]}"
  fi

  exec python3 "$VIDEO2BOOK_ROOT/playlist2videos/download_playlist.py" \
    --playlist-url "$PLAYLIST_URL" \
    --workspace "$YT_DLP_WORKSPACE" \
    --download-root "$DOWNLOAD_ROOT" \
    --download-subdir "$DOWNLOAD_SUBDIR" \
    --log-root "$DOWNLOAD_LOG_ROOT" \
    --archive-file "$archive_file" \
    "$@"
}
