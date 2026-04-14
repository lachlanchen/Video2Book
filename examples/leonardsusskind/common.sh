#!/usr/bin/env bash
set -euo pipefail

load_leonardsusskind_archive_env() {
  local script_dir="$1"
  export VIDEO2BOOK_EXAMPLE_DIR="$(cd "$script_dir" && pwd)"
  export VIDEO2BOOK_ROOT="$(cd "$VIDEO2BOOK_EXAMPLE_DIR/../../.." && pwd)"
  export HOST_REPO_ROOT="${HOST_REPO_ROOT:-$(pwd)}"

  export PLAYLIST_URL="${PLAYLIST_URL:-https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG}"
  export PLAYLIST_ID="${PLAYLIST_ID:-PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG}"
  export DOWNLOAD_WORKSPACE="${DOWNLOAD_WORKSPACE:-/home/lachlan/ProjectsLFS/YoutubeDownloader}"
  export DOWNLOAD_ROOT="${DOWNLOAD_ROOT:-$DOWNLOAD_WORKSPACE/downloads}"
  export DOWNLOAD_SUBDIR="${DOWNLOAD_SUBDIR:-$PLAYLIST_ID}"
  export DOWNLOAD_LOG_ROOT="${DOWNLOAD_LOG_ROOT:-$DOWNLOAD_WORKSPACE/logs}"
  export TRANSCRIPTION_SOURCE_ROOT="${TRANSCRIPTION_SOURCE_ROOT:-$DOWNLOAD_ROOT/$DOWNLOAD_SUBDIR}"

  export TRANSCRIPTION_SESSION="${TRANSCRIPTION_SESSION:-susskind-transcribe}"
  export TRANSCRIPTION_MONITOR_SESSION="${TRANSCRIPTION_MONITOR_SESSION:-susskind-transcribe-monitor}"
  export NOTES_SESSION="${NOTES_SESSION:-susskind-notes}"
  export NOTES_MONITOR_SESSION="${NOTES_MONITOR_SESSION:-susskind-notes-monitor}"

  export NOTE_MODEL_DEFAULT="${NOTE_MODEL_DEFAULT:-gpt-5.4}"
  export NOTE_REASONING_DEFAULT="${NOTE_REASONING_DEFAULT:-xhigh}"
  export NOTE_SESSION_SCOPE_DEFAULT="${NOTE_SESSION_SCOPE_DEFAULT:-global}"
  export NOTE_MONITOR_MODEL_DEFAULT="${NOTE_MONITOR_MODEL_DEFAULT:-gpt-5.4-mini}"
  export NOTE_MONITOR_REASONING_DEFAULT="${NOTE_MONITOR_REASONING_DEFAULT:-low}"
}
