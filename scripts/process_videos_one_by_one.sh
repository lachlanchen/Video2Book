#!/usr/bin/env bash
set -euo pipefail

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${TRANSCRIPTION_REPO_ROOT:-$(pwd)}"
source_root="${SOURCE_ROOT:-/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG}"
source_subdir="${SOURCE_SUBDIR:-}"
transcribe_model="${TRANSCRIBE_MODEL:-large-v3}"
transcription_git_paths="${TRANSCRIPTION_GIT_PATHS:-subtitles markdown}"
git_lock="${TRANSCRIPTION_GIT_LOCK_FILE:-$repo_root/.git/video2book-main.lock}"
selected_gpu_id=""

if [[ -n "${TRANSCRIBE_CUDA_VISIBLE_DEVICES:-}" ]]; then
  selected_gpu_id="${TRANSCRIBE_CUDA_VISIBLE_DEVICES%%,*}"
elif [[ -n "${CUDA_VISIBLE_DEVICES:-}" ]]; then
  selected_gpu_id="${CUDA_VISIBLE_DEVICES%%,*}"
fi

if [[ -n "${MIN_FREE_GPU_MIB:-}" ]]; then
  min_free_gpu_mib="${MIN_FREE_GPU_MIB}"
else
  case "$transcribe_model" in
    large|large-v1|large-v2|large-v3)
      min_free_gpu_mib=14000
      ;;
    medium|medium.en)
      min_free_gpu_mib=9000
      ;;
    *)
      min_free_gpu_mib=4000
      ;;
  esac
fi

cd "$repo_root"
read -r -a git_add_paths <<<"$transcription_git_paths"

wait_for_gpu_memory() {
  while true; do
    if [[ -n "$selected_gpu_id" ]]; then
      free_mib="$(nvidia-smi --id="$selected_gpu_id" --query-gpu=memory.free --format=csv,noheader,nounits | head -n 1 | tr -d ' ')"
      gpu_label="GPU $selected_gpu_id"
    else
      free_mib="$(nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits | head -n 1 | tr -d ' ')"
      gpu_label="first visible GPU"
    fi
    if [[ -n "$free_mib" ]] && (( free_mib >= min_free_gpu_mib )); then
      return
    fi
    echo "Waiting for GPU memory on ${gpu_label}: ${free_mib:-unknown} MiB free, need ${min_free_gpu_mib} MiB"
    sleep 60
  done
}

while true; do
  next_cmd=(python3 "$module_root/videos2subtitles/transcribe_video.py" --repo-root "$repo_root" --source-root "$source_root" --print-next)
  if [[ -n "$source_subdir" ]]; then
    next_cmd+=(--source-subdir "$source_subdir")
  fi
  next_video="$("${next_cmd[@]}")"
  if [[ -z "$next_video" ]]; then
    echo "No pending videos remain."
    exit 0
  fi

  wait_for_gpu_memory
  if [[ -n "$selected_gpu_id" ]]; then
    echo "Processing $next_video with model $transcribe_model on GPU $selected_gpu_id"
  else
    echo "Processing $next_video with model $transcribe_model"
  fi
  transcribe_cmd=(
    python3
    "$module_root/videos2subtitles/transcribe_video.py"
    --repo-root "$repo_root"
    --source-root "$source_root"
    --model "$transcribe_model"
    --video "$next_video"
  )
  if [[ -n "$source_subdir" ]]; then
    transcribe_cmd+=(--source-subdir "$source_subdir")
  fi
  PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True "${transcribe_cmd[@]}"

  existing_git_add_paths=()
  for path in "${git_add_paths[@]}"; do
    if [[ -e "$path" ]]; then
      existing_git_add_paths+=("$path")
    fi
  done
  (
    flock 200

    if (( ${#existing_git_add_paths[@]} > 0 )); then
      git add -- "${existing_git_add_paths[@]}"
    else
      echo "No transcript paths exist yet after processing $next_video"
    fi

    if git diff --cached --quiet; then
      echo "No new tracked changes after processing $next_video"
      exit 0
    fi

    rel_path="${next_video#${source_root}/}"
    rel_path="${rel_path%.*}"
    git commit -m "Add transcript for ${rel_path}"
    git push origin main
  ) 200>"$git_lock"
done
