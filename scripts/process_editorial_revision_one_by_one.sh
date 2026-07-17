#!/usr/bin/env bash
set -euo pipefail

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${NOTES_REPO_ROOT:-$(pwd)}"
output_root=""
model="${EDITORIAL_CODEX_MODEL:-gpt-5.6-sol}"
reasoning="${EDITORIAL_CODEX_REASONING:-ultra}"
all_courses=0
no_compile=0
no_commit=0
force=0
courses=()
chapters=()
references=()

usage() {
  cat <<'EOF'
Usage: process_editorial_revision_one_by_one.sh [options]

Options:
  --repo-root <path>       Host repository root
  --output-root <path>     Generated notes root; defaults to generated_course_notes
  --course <relpath>       Course to revise; repeatable
  --all-courses            Revise every generated course
  --chapter <slug>         Restrict to a chapter; repeatable
  --reference <path>       Reference PDF or directory; repeatable
  --model <name>           Codex model (default: gpt-5.6-sol)
  --reasoning <level>      low, medium, high, xhigh, or ultra
  --no-compile             Skip chapter and course PDF builds
  --no-commit              Do not commit and push after each course
  --force                  Ignore completed resume state
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root) repo_root="$2"; shift 2 ;;
    --output-root) output_root="$2"; shift 2 ;;
    --course) courses+=("$2"); shift 2 ;;
    --all-courses) all_courses=1; shift ;;
    --chapter) chapters+=("$2"); shift 2 ;;
    --reference) references+=("$2"); shift 2 ;;
    --model) model="$2"; shift 2 ;;
    --reasoning) reasoning="$2"; shift 2 ;;
    --no-compile) no_compile=1; shift ;;
    --no-commit) no_commit=1; shift ;;
    --force) force=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done

repo_root="$(cd "$repo_root" && pwd)"
if [[ -z "$output_root" ]]; then
  output_root="$repo_root/generated_course_notes"
fi

if [[ "$all_courses" -eq 1 ]]; then
  mapfile -t courses < <(
    find "$output_root" -mindepth 3 -maxdepth 3 -type d -print0 |
      while IFS= read -r -d '' path; do
        [[ -d "$path/chapters" ]] || continue
        printf '%s\n' "${path#"$output_root"/}"
      done | sort
  )
fi

if [[ "${#courses[@]}" -eq 0 ]]; then
  echo "Provide --course or --all-courses." >&2
  exit 2
fi

export CODEX_SHARED_SESSION_FILE="${CODEX_SHARED_SESSION_FILE:-$repo_root/.editorial-revision-work/writer.session_id}"
export CODEX_SHARED_SESSION_DOC_FILE="${CODEX_SHARED_SESSION_DOC_FILE:-$repo_root/.editorial-revision-work/writer.session.md}"
export NOTE_CODEX_SESSION_SCOPE=global

for course in "${courses[@]}"; do
  command=(
    python3 "$module_root/subtitles2notes/editorial_revision.py"
    --repo-root "$repo_root"
    --output-root "$output_root"
    --course "$course"
    --rewrite
    --resume
    --model "$model"
    --reasoning "$reasoning"
  )
  for chapter in "${chapters[@]}"; do
    command+=(--chapter "$chapter")
  done
  for reference in "${references[@]}"; do
    command+=(--reference "$reference")
  done
  [[ "$no_compile" -eq 0 ]] || command+=(--no-compile)
  [[ "$force" -eq 0 ]] || command+=(--force)

  printf '[editorial] starting %s\n' "$course"
  "${command[@]}"
  printf '[editorial] completed %s\n' "$course"

  if [[ "$no_commit" -eq 0 ]]; then
    bash "$module_root/scripts/codex_commit_push.sh" \
      "$repo_root" \
      "Editorially revise $course" \
      "${output_root#"$repo_root"/}/$course"
  fi
done
