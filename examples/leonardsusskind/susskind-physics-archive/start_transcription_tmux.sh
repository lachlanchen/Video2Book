#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$script_dir/../common.sh"
load_leonardsusskind_archive_env "$script_dir"

export TRANSCRIPTION_REPO_ROOT="$HOST_REPO_ROOT"
export SOURCE_ROOT="$TRANSCRIPTION_SOURCE_ROOT"

session_name="${1:-$TRANSCRIPTION_SESSION}"
transcribe_model="${2:-${TRANSCRIBE_MODEL:-large-v3}}"
min_free_gpu_mib="${3:-${MIN_FREE_GPU_MIB:-}}"

cd "$HOST_REPO_ROOT"
if [[ -n "$min_free_gpu_mib" ]]; then
  exec bash "$VIDEO2BOOK_ROOT/scripts/start_transcription_tmux.sh" "$session_name" "$transcribe_model" "$min_free_gpu_mib"
fi
exec bash "$VIDEO2BOOK_ROOT/scripts/start_transcription_tmux.sh" "$session_name" "$transcribe_model"
