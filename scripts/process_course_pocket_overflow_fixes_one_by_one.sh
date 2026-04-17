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
size_preset="penguin"
font_mode="onepointtwo"
model="${NOTE_MODEL:-gpt-5.4}"
reasoning="${NOTE_REASONING:-medium}"
max_iterations=4

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

if [[ "${#courses[@]}" -eq 0 ]]; then
  echo "No eligible courses found."
  exit 0
fi

for rel in "${courses[@]}"; do
  echo "==> fixing $rel [$font_mode/$size_preset]"
  bash "$module_root/scripts/fix_course_pocket_overfulls.sh" \
    --host-root "$host_root" \
    --source-dir "$source_dir" \
    --course "$rel" \
    --size "$size_preset" \
    --font-mode "$font_mode" \
    --model "$model" \
    --reasoning "$reasoning" \
    --max-iterations "$max_iterations"
done
