#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/process_course_pocket_overflow_fixes_one_by_one.sh [options]

Runs the pocket-overflow fixer course by course, reusing one Codex session.

Options:
  --host-root <path>        Host repo root (default: current working directory)
  --source-dir <path>       generated_course_notes root
  --course <relpath>        Restrict to one course
  --start-course <relpath>  Start from this course in sorted order
  --size <preset>           penguin|a5|custom (default: penguin)
  --font-mode <mode>        normal|onepointtwo|onehalf|double (default: onepointtwo)
  --model <name>            Codex model (default: gpt-5.4)
  --reasoning <level>       low|medium|high|xhigh (default: medium)
  --max-iterations <n>      Max Codex edit passes per course (default: 4)
  -h, --help                Show this help
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
host_root="${HOST_ROOT:-$(pwd)}"
source_dir=""
course=""
start_course=""
size_preset="penguin"
font_mode="onepointtwo"
model="${NOTE_MODEL:-gpt-5.4}"
reasoning="${NOTE_REASONING:-medium}"
max_iterations=4
post_fix_hook="${VIDEO2BOOK_POST_OVERFLOW_FIX_HOOK:-}"
state_file="${VIDEO2BOOK_POCKET_OVERFLOW_STATE_FILE:-$host_root/.lecture-notes-work/pocket_overflow_fix/queue_state.env}"
failures_file="${VIDEO2BOOK_POCKET_OVERFLOW_FAILURES_FILE:-$host_root/.lecture-notes-work/pocket_overflow_fix/course_failures.tsv}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --host-root)
      host_root="${2:-}"
      shift 2
      ;;
    --source-dir)
      source_dir="${2:-}"
      shift 2
      ;;
    --course)
      course="${2:-}"
      shift 2
      ;;
    --start-course)
      start_course="${2:-}"
      shift 2
      ;;
    --size)
      size_preset="${2:-}"
      shift 2
      ;;
    --font-mode)
      font_mode="${2:-}"
      shift 2
      ;;
    --model)
      model="${2:-}"
      shift 2
      ;;
    --reasoning)
      reasoning="${2:-}"
      shift 2
      ;;
    --max-iterations)
      max_iterations="${2:-4}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ -z "$source_dir" ]]; then
  source_dir="$host_root/generated_course_notes"
fi

latest_course_from_log() {
  local worker_log="${VIDEO2BOOK_WORKER_LOG_PATH:-}"
  if [[ -z "$worker_log" || ! -f "$worker_log" ]]; then
    return 0
  fi
  python3 - "$worker_log" <<'PY'
from pathlib import Path
import re
import sys

course = ""
for line in Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace").splitlines():
    match = re.match(r"^==> fixing (.+?) \[", line)
    if match:
        course = match.group(1)
print(course)
PY
}

if [[ -z "$course" && -z "$start_course" && -f "$state_file" ]]; then
  # shellcheck disable=SC1090
  source "$state_file"
  if [[ "${STATE_STATUS:-}" != "finished" ]]; then
    log_resume_course="$(latest_course_from_log)"
    if [[ -n "$log_resume_course" ]]; then
      start_course="$log_resume_course"
    elif [[ -n "${CURRENT_COURSE:-}" ]]; then
      start_course="$CURRENT_COURSE"
    elif [[ -n "${NEXT_COURSE:-}" ]]; then
      start_course="$NEXT_COURSE"
    fi
  fi
fi

if [[ ! -d "$source_dir" ]]; then
  echo "Missing source_dir: $source_dir" >&2
  exit 1
fi

if [[ -n "$course" ]]; then
  courses=("$course")
else
  mapfile -t courses < <(
    find "$source_dir" -type f -name course.tex -print | sort |
      while read -r tex_path; do
        course_dir="$(dirname "$tex_path")"
        if [[ -f "$course_dir/course.pdf" ]]; then
          printf '%s\n' "${course_dir#${source_dir}/}"
        fi
      done
  )
fi

if [[ -n "$start_course" && -z "$course" ]]; then
  filtered=()
  reached=0
  for rel in "${courses[@]}"; do
    if [[ "$reached" -eq 0 && "$rel" == "$start_course" ]]; then
      reached=1
    fi
    if [[ "$reached" -eq 1 ]]; then
      filtered+=("$rel")
    fi
  done
  courses=("${filtered[@]}")
fi

if [[ "${#courses[@]}" -eq 0 ]]; then
  echo "No eligible courses found."
  exit 0
fi

mkdir -p "$(dirname "$state_file")"
last_completed_course=""
last_failed_course=""
current_course=""
next_course=""
mkdir -p "$(dirname "$failures_file")"
touch "$failures_file"

write_state() {
  local status="$1"
  {
    printf 'STATE_UPDATED_AT=%q\n' "$(date --iso-8601=seconds)"
    printf 'STATE_STATUS=%q\n' "$status"
    printf 'CURRENT_COURSE=%q\n' "$current_course"
    printf 'LAST_COMPLETED_COURSE=%q\n' "$last_completed_course"
    printf 'LAST_FAILED_COURSE=%q\n' "$last_failed_course"
    printf 'NEXT_COURSE=%q\n' "$next_course"
    printf 'FAILURES_FILE=%q\n' "$failures_file"
    printf 'START_COURSE=%q\n' "$start_course"
    printf 'FONT_MODE=%q\n' "$font_mode"
    printf 'SIZE_PRESET=%q\n' "$size_preset"
    printf 'MODEL=%q\n' "$model"
    printf 'REASONING=%q\n' "$reasoning"
    printf 'MAX_ITERATIONS=%q\n' "$max_iterations"
  } > "$state_file"
}

write_state "starting"

for idx in "${!courses[@]}"; do
  rel="${courses[$idx]}"
  current_course="$rel"
  if (( idx + 1 < ${#courses[@]} )); then
    next_course="${courses[$((idx + 1))]}"
  else
    next_course=""
  fi
  write_state "running"
  echo "==> fixing $rel [$font_mode/$size_preset]"
  status=0
  if bash "$module_root/scripts/fix_course_pocket_overfulls.sh" \
    --host-root "$host_root" \
    --source-dir "$source_dir" \
    --course "$rel" \
    --size "$size_preset" \
    --font-mode "$font_mode" \
    --model "$model" \
    --reasoning "$reasoning" \
    --max-iterations "$max_iterations"; then
    status=0
  else
    status=$?
  fi
  if [[ "$status" -ne 0 ]]; then
    printf '%s\tfix\t%s\tstatus=%s\n' "$(date --iso-8601=seconds)" "$rel" "$status" >> "$failures_file"
    echo "skip course after fixer failure: $rel (status=$status)"
    last_failed_course="$rel"
    current_course=""
    write_state "course_failed"
    continue
  fi
  if [[ -n "$post_fix_hook" ]]; then
    if ! "$post_fix_hook" --repo-root "$host_root" --course "$rel"; then
      printf '%s\thook\t%s\tstatus=1\n' "$(date --iso-8601=seconds)" "$rel" >> "$failures_file"
      echo "skip publish hook failure and continue: $rel"
      last_failed_course="$rel"
      current_course=""
      write_state "hook_failed"
      continue
    fi
  fi
  last_completed_course="$rel"
  current_course=""
  write_state "completed"
done

write_state "finished"
