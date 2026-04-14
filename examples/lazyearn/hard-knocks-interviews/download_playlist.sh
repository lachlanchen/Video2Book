#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$script_dir/../common.sh"
load_lazyearn_course_env "$script_dir"

cd "$HOST_REPO_ROOT"
mkdir -p "$DOWNLOAD_LOG_ROOT"

exec python3 "$VIDEO2BOOK_ROOT/playlist2videos/download_playlist.py" \
  --playlist-url "$PLAYLIST_URL" \
  --workspace "$YT_DLP_WORKSPACE" \
  --download-root "$DOWNLOAD_ROOT" \
  --download-subdir "$DOWNLOAD_SUBDIR" \
  --log-root "$DOWNLOAD_LOG_ROOT" \
  "$@"
