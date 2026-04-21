#!/usr/bin/env bash
set -euo pipefail

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${TRANSCRIPTION_REPO_ROOT:-$(pwd)}"
session_name="${1:-susskind-transcribe-follow}"
transcribe_model="${TRANSCRIBE_MODEL:-large-v3}"
min_free_gpu_mib="${MIN_FREE_GPU_MIB:-}"
transcribe_cuda_visible_devices="${TRANSCRIBE_CUDA_VISIBLE_DEVICES:-${CUDA_VISIBLE_DEVICES:-}}"

cd "$repo_root"
mkdir -p transcription_logs

if tmux has-session -t "$session_name" 2>/dev/null; then
  echo "Session already exists: $session_name"
  tmux list-panes -t "$session_name" -F '#S:#I.#P #{pane_current_command}'
  exit 0
fi

if [[ -z "${DOWNLOAD_DONE_FILE:-}" ]]; then
  echo "DOWNLOAD_DONE_FILE is required."
  exit 1
fi

log_file="transcription_logs/${session_name}_$(date +%Y%m%d_%H%M%S).log"
tmux_command="export TRANSCRIPTION_REPO_ROOT='$repo_root'; "
tmux_command+="export SOURCE_ROOT='${SOURCE_ROOT:-/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG}'; "
if [[ -n "${SOURCE_SUBDIR:-}" ]]; then
  tmux_command+="export SOURCE_SUBDIR='${SOURCE_SUBDIR}'; "
fi
if [[ -n "${TRANSCRIPTION_GIT_PATHS:-}" ]]; then
  tmux_command+="export TRANSCRIPTION_GIT_PATHS='${TRANSCRIPTION_GIT_PATHS}'; "
fi
tmux_command+="export DOWNLOAD_DONE_FILE='${DOWNLOAD_DONE_FILE}'; "
if [[ -n "${TRANSCRIPTION_FOLLOW_DONE_FILE:-}" ]]; then
  tmux_command+="export TRANSCRIPTION_FOLLOW_DONE_FILE='${TRANSCRIPTION_FOLLOW_DONE_FILE}'; "
fi
if [[ -n "${TRANSCRIPTION_FOLLOW_POLL_SECONDS:-}" ]]; then
  tmux_command+="export TRANSCRIPTION_FOLLOW_POLL_SECONDS='${TRANSCRIPTION_FOLLOW_POLL_SECONDS}'; "
fi
tmux_command+="export TRANSCRIBE_MODEL='$transcribe_model'; "
if [[ -n "$min_free_gpu_mib" ]]; then
  tmux_command+="export MIN_FREE_GPU_MIB='$min_free_gpu_mib'; "
fi
if [[ -n "$transcribe_cuda_visible_devices" ]]; then
  tmux_command+="export TRANSCRIBE_CUDA_VISIBLE_DEVICES='$transcribe_cuda_visible_devices'; "
  tmux_command+="export CUDA_VISIBLE_DEVICES='$transcribe_cuda_visible_devices'; "
fi
tmux_command+="cd '$repo_root' && bash '$module_root/scripts/process_transcription_until_download_done.sh' 2>&1 | tee '$log_file'"

tmux new-session -d -s "$session_name" "$tmux_command"

echo "Started follow-mode tmux session: $session_name"
echo "Log file: $log_file"
echo "Attach with: tmux attach -t $session_name"
