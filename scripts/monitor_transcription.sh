#!/usr/bin/env bash
set -euo pipefail

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${TRANSCRIPTION_REPO_ROOT:-$(pwd)}"
session_name="${1:-susskind-transcribe}"
check_interval="${TRANSCRIPTION_MONITOR_INTERVAL_SECONDS:-1800}"
stale_seconds="${TRANSCRIPTION_MONITOR_STALE_SECONDS:-2700}"
source_root="${SOURCE_ROOT:-/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG}"
source_subdir="${SOURCE_SUBDIR:-}"
transcribe_model="${TRANSCRIBE_MODEL:-large-v3}"
min_free_gpu_mib="${MIN_FREE_GPU_MIB:-}"
transcribe_cuda_visible_devices="${TRANSCRIBE_CUDA_VISIBLE_DEVICES:-${CUDA_VISIBLE_DEVICES:-}}"
transcription_engine="${TRANSCRIPTION_ENGINE:-}"
primary_timeout_seconds="${TRANSCRIPTION_PRIMARY_TIMEOUT_SECONDS:-}"
log_dir="$repo_root/transcription_logs"

mkdir -p "$log_dir"
monitor_log="$log_dir/${session_name}-monitor_$(date +%Y%m%d_%H%M%S).log"

log_line() {
  printf '[%s] %s\n' "$(date --iso-8601=seconds)" "$*" | tee -a "$monitor_log"
}

latest_worker_log() {
  ls -1t "$log_dir"/"${session_name}"_*.log 2>/dev/null | head -n 1 || true
}

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

restart_worker() {
  TRANSCRIPTION_REPO_ROOT="$repo_root" SOURCE_ROOT="$source_root" SOURCE_SUBDIR="$source_subdir" TRANSCRIPTION_GIT_PATHS="${TRANSCRIPTION_GIT_PATHS:-}" TRANSCRIBE_MODEL="$transcribe_model" MIN_FREE_GPU_MIB="$min_free_gpu_mib" TRANSCRIBE_CUDA_VISIBLE_DEVICES="$transcribe_cuda_visible_devices" CUDA_VISIBLE_DEVICES="$transcribe_cuda_visible_devices" TRANSCRIPTION_ENGINE="$transcription_engine" TRANSCRIPTION_PRIMARY_TIMEOUT_SECONDS="$primary_timeout_seconds" \
    bash "$module_root/scripts/start_transcription_tmux.sh" "$session_name"
}

while true; do
  next_video="$(pending_video || true)"
  if [[ -z "$next_video" ]]; then
    log_line "No pending videos remain. Monitor exiting."
    exit 0
  fi

  status="healthy"
  action="none"
  reason="worker active"

  if ! tmux has-session -t "$session_name" 2>/dev/null; then
    status="crashed"
    action="restart"
    reason="tmux session missing"
  else
    worker_log="$(latest_worker_log)"
    if [[ -n "$worker_log" ]]; then
      now_epoch="$(date +%s)"
      log_epoch="$(stat -c %Y "$worker_log")"
      age_seconds=$(( now_epoch - log_epoch ))
      if (( age_seconds > stale_seconds )); then
        status="stalled"
        action="restart"
        reason="worker log stale for ${age_seconds}s"
      fi
    fi
  fi

  log_line "Monitor decision: status=$status action=$action next=$(basename "$next_video") reason=$reason"

  if [[ "$action" == "restart" ]]; then
    restart_worker
  fi

  sleep "$check_interval"
done
