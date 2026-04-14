#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$script_dir/../common.sh"
load_leonardsusskind_archive_env "$script_dir"

export TRANSCRIPTION_REPO_ROOT="$HOST_REPO_ROOT"
export SOURCE_ROOT="$TRANSCRIPTION_SOURCE_ROOT"

monitor_session="${1:-$TRANSCRIPTION_MONITOR_SESSION}"
worker_session="${2:-$TRANSCRIPTION_SESSION}"

cd "$HOST_REPO_ROOT"
exec bash "$VIDEO2BOOK_ROOT/scripts/start_transcription_monitor_tmux.sh" "$monitor_session" "$worker_session"
