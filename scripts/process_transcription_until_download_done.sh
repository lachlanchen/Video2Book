#!/usr/bin/env bash
set -euo pipefail

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${TRANSCRIPTION_REPO_ROOT:-$(pwd)}"
source_root="${SOURCE_ROOT:-/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG}"
source_subdir="${SOURCE_SUBDIR:-}"
download_done_file="${DOWNLOAD_DONE_FILE:-}"
follow_done_file="${TRANSCRIPTION_FOLLOW_DONE_FILE:-}"
poll_seconds="${TRANSCRIPTION_FOLLOW_POLL_SECONDS:-60}"

cd "$repo_root"

if [[ -z "$download_done_file" ]]; then
  echo "DOWNLOAD_DONE_FILE is required for follow-mode transcription."
  exit 1
fi

if [[ -n "$follow_done_file" ]]; then
  mkdir -p "$(dirname "$follow_done_file")"
  rm -f "$follow_done_file"
fi

pending_video() {
  cmd=(
    python3
    "$module_root/videos2subtitles/transcribe_video.py"
    --repo-root "$repo_root"
    --source-root "$source_root"
    --print-next
  )
  if [[ -n "$source_subdir" ]]; then
    cmd+=(--source-subdir "$source_subdir")
  fi
  "${cmd[@]}"
}

while true; do
  next_video="$(pending_video || true)"
  if [[ -n "$next_video" ]]; then
    echo "Follow-mode transcription found pending video: $(basename "$next_video")"
    bash "$module_root/scripts/process_videos_one_by_one.sh"
    continue
  fi

  if [[ -f "$download_done_file" ]]; then
    echo "Download marker present and no pending videos remain."
    if [[ -n "$follow_done_file" ]]; then
      touch "$follow_done_file"
    fi
    exit 0
  fi

  echo "No completed videos ready yet; waiting ${poll_seconds}s for more downloads."
  sleep "$poll_seconds"
done
