#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/process_book_translation_one_by_one.sh [options]

Translates one TeX-book unit at a time with Codex and checkpoints progress after
each completed unit.

Options:
  --book-root <rel>       book root relative to the repo root
  --language <code>       zh or jp
  --model <name>          Codex model (default: BOOK_TRANSLATION_MODEL or gpt-5.4)
  --reasoning <level>     low|medium|high|xhigh (default: BOOK_TRANSLATION_REASONING or high)
  --max-units <n>         stop after n completed translation units
  --branch <name>         push branch (default: current branch or main)
  --no-commit             skip git commit/push checkpoints
  -h, --help              show help
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root="${NOTES_REPO_ROOT:-$(pwd)}"
book_root=""
language=""
model="${BOOK_TRANSLATION_MODEL:-gpt-5.4}"
reasoning="${BOOK_TRANSLATION_REASONING:-high}"
max_units=0
branch="${BOOK_TRANSLATION_BRANCH:-$(git -C "$repo_root" branch --show-current 2>/dev/null || true)}"
do_commit=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --book-root)
      book_root="${2:-}"
      shift 2
      ;;
    --language)
      language="${2:-}"
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
    --max-units)
      max_units="${2:-0}"
      shift 2
      ;;
    --branch)
      branch="${2:-}"
      shift 2
      ;;
    --no-commit)
      do_commit=0
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

if [[ -z "$book_root" || -z "$language" ]]; then
  usage >&2
  exit 1
fi

case "$language" in
  zh|jp) ;;
  *)
    echo "Invalid language: $language" >&2
    exit 1
    ;;
esac

case "$reasoning" in
  low|medium|high|xhigh) ;;
  *)
    echo "Invalid reasoning level: $reasoning" >&2
    exit 1
    ;;
esac

if [[ -z "$branch" ]]; then
  branch="main"
fi

cd "$repo_root"

book_slug="$(basename "$book_root")"
work_root="$repo_root/$book_root/.translation-work"
prompt_dir="$work_root/prompts/$language"
session_dir="$work_root/codex_sessions"
git_lock="$repo_root/.git/video2book-translation.lock"
mkdir -p "$prompt_dir" "$session_dir"

export CODEX_SHARED_SESSION_FILE="$session_dir/${book_slug}-${language}.session_id"
export CODEX_SHARED_SESSION_DOC_FILE="$session_dir/${book_slug}-${language}.session.md"

python3 "$module_root/scripts/translate_tex_book.py" \
  --repo-root "$repo_root" \
  --book-root "$book_root" \
  --language "$language" \
  init >/dev/null

commit_progress() {
  local message="$1"
  (
    flock 200
    git -C "$repo_root" add -- "$book_root/.gitignore" "$book_root/$language"
    if git -C "$repo_root" diff --cached --quiet -- "$book_root/.gitignore" "$book_root/$language"; then
      echo "No translation changes to commit for $language"
      exit 0
    fi
    git -C "$repo_root" commit -m "$message"
    for attempt in 1 2 3 4 5; do
      if git -C "$repo_root" push origin "$branch"; then
        exit 0
      fi
      sleep $((attempt * 2))
    done
    echo "Failed to push translation checkpoint for $language after retries." >&2
    exit 1
  ) 200>"$git_lock"
}

processed=0
while true; do
  next_line="$(
    python3 "$module_root/scripts/translate_tex_book.py" \
      --repo-root "$repo_root" \
      --book-root "$book_root" \
      --language "$language" \
      print-next --format tsv
  )"

  if [[ -z "$next_line" ]]; then
    echo "No pending translation units remain for $book_root ($language)."
    exit 0
  fi

  IFS=$'\t' read -r unit_key unit_kind target_rel unit_title <<<"$next_line"
  prompt_path="$prompt_dir/${processed}_$unit_key.prompt.txt"

  echo "Translating $language unit: $unit_key ($unit_kind)"
  python3 "$module_root/scripts/translate_tex_book.py" \
    --repo-root "$repo_root" \
    --book-root "$book_root" \
    --language "$language" \
    write-prompt \
    --unit "$unit_key" \
    --output "$prompt_path" >/dev/null

  "$module_root/scripts/codex_prompt_to_file.sh" \
    "$repo_root" \
    "$prompt_path" \
    "$repo_root/$target_rel" \
    "$model" \
    "$reasoning"

  python3 "$module_root/scripts/translate_tex_book.py" \
    --repo-root "$repo_root" \
    --book-root "$book_root" \
    --language "$language" \
    mark-done \
    --unit "$unit_key" >/dev/null

  python3 "$module_root/scripts/translate_tex_book.py" \
    --repo-root "$repo_root" \
    --book-root "$book_root" \
    --language "$language" \
    compile >/dev/null

  if [[ "$do_commit" -eq 1 ]]; then
    commit_progress "Translate $book_slug $language: $unit_key"
  fi

  processed=$((processed + 1))
  if [[ "$max_units" -gt 0 && "$processed" -ge "$max_units" ]]; then
    echo "Reached translation unit limit: $max_units"
    exit 0
  fi
done
