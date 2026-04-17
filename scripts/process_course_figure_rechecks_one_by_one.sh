#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/process_course_figure_rechecks_one_by_one.sh [options]

Rechecks generated lecture figures course by course.

Options:
  --repo-root <path>       Host notes repo root (default: current directory)
  --source-root <path>     Source video root
  --course <rel>           Restrict to one course rel path
  --lecture-slug <slug>    Restrict to one lecture slug
  --figure-index <n>       Restrict to one figure index inside the lecture
  --model <name>           Codex model (default: NOTE_MODEL or gpt-5.4)
  --reasoning <level>      low|medium|high|xhigh (default: NOTE_REASONING or high)
  --report-only            Audit only; do not patch figures
  --force                  Re-extract candidate frames even if cached
  -h, --help               Show help
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${NOTES_REPO_ROOT:-$(pwd)}"
source_root="${NOTE_SOURCE_ROOT:-${SOURCE_ROOT:-/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG}}"
course=""
lecture_slug=""
figure_index=""
model="${NOTE_MODEL:-gpt-5.4}"
reasoning="${NOTE_REASONING:-high}"
report_only=0
force=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root)
      repo_root="${2:-}"
      shift 2
      ;;
    --source-root)
      source_root="${2:-}"
      shift 2
      ;;
    --course)
      course="${2:-}"
      shift 2
      ;;
    --lecture-slug)
      lecture_slug="${2:-}"
      shift 2
      ;;
    --figure-index)
      figure_index="${2:-}"
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
    --report-only)
      report_only=1
      shift
      ;;
    --force)
      force=1
      shift
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

cmd=(
  python3 "$module_root/scripts/recheck_course_figures.py"
  --repo-root "$repo_root"
  --source-root "$source_root"
  --model "$model"
  --reasoning "$reasoning"
  --rebuild
)

if [[ -n "$course" ]]; then
  cmd+=(--course "$course")
fi
if [[ -n "$lecture_slug" ]]; then
  cmd+=(--lecture-slug "$lecture_slug")
fi
if [[ -n "$figure_index" ]]; then
  cmd+=(--figure-index "$figure_index")
fi
if [[ "$report_only" -eq 1 ]]; then
  cmd+=(--report-only)
fi
if [[ "$force" -eq 1 ]]; then
  cmd+=(--force)
fi

cd "$repo_root"
"${cmd[@]}"
