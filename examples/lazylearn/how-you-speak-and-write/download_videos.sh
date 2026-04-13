#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$script_dir/../common.sh"
load_lazylearn_course_env "$script_dir"

cd "$HOST_REPO_ROOT"
mkdir -p "$DOWNLOAD_LOG_ROOT"

exec python3 "$VIDEO2BOOK_ROOT/playlist2videos/download_video_list.py" \
  --urls-file "$VIDEO2BOOK_EXAMPLE_DIR/$URLS_FILE" \
  --workspace "$YT_DLP_WORKSPACE" \
  --download-root "$DOWNLOAD_ROOT" \
  --download-subdir "$DOWNLOAD_SUBDIR" \
  --log-root "$DOWNLOAD_LOG_ROOT" \
  "$@"
