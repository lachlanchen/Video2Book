#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/fix_course_pocket_overfulls.sh --course <relpath> [options]

Iteratively fix LaTeX source overfulls for one generated course by:
1. exporting a target PDF variant,
2. generating a mapped overflow report,
3. asking Codex to patch only the flagged source files,
4. recompiling until warnings drop or stop improving.

Options:
  --course <relpath>            Course path under generated_course_notes (required)
  --host-root <path>            Host repo root (default: parent of Video2Book)
  --source-dir <path>           generated_course_notes root (default: <host-root>/generated_course_notes)
  --work-dir <path>             Working root for logs, reports, and temporary exports
  --size <preset>               penguin (default) | a5 | custom
  --font-mode <mode>            normal | onepointtwo | onehalf | double (default: onepointtwo)
  --paper-width <size>          For --size custom
  --paper-height <size>         For --size custom
  --margin <size>               For --size custom
  --model <name>                Codex model (default: gpt-5.4)
  --reasoning <level>           low|medium|high|xhigh (default: medium)
  --max-iterations <n>          Maximum Codex edit passes (default: 4)
  --session-file <path>         Shared Codex session id file
  --session-doc <path>          Shared Codex session metadata doc
  --skip-commit                 Do not commit/push after a successful edit pass
  -h, --help                    Show this help
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
host_root="${HOST_ROOT:-$(cd "$module_root/.." && pwd)}"
source_dir=""
course=""
work_dir=""
size_preset="penguin"
font_mode="onepointtwo"
paper_width=""
paper_height=""
geometry_margin=""
model="${NOTE_MODEL:-gpt-5.4}"
reasoning="${NOTE_REASONING:-medium}"
max_iterations=4
do_commit=1
session_file=""
session_doc=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --course)
      course="${2:-}"
      shift 2
      ;;
    --host-root)
      host_root="${2:-}"
      shift 2
      ;;
    --source-dir)
      source_dir="${2:-}"
      shift 2
      ;;
    --work-dir)
      work_dir="${2:-}"
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
    --paper-width)
      paper_width="${2:-}"
      shift 2
      ;;
    --paper-height)
      paper_height="${2:-}"
      shift 2
      ;;
    --margin)
      geometry_margin="${2:-}"
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
    --session-file)
      session_file="${2:-}"
      shift 2
      ;;
    --session-doc)
      session_doc="${2:-}"
      shift 2
      ;;
    --skip-commit)
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

if [[ -z "$course" ]]; then
  echo "--course is required." >&2
  usage >&2
  exit 1
fi

case "$reasoning" in
  low|medium|high|xhigh) ;;
  *)
    echo "Invalid reasoning level: $reasoning" >&2
    exit 1
    ;;
esac

case "$font_mode" in
  normal|onepointtwo|onehalf|double) ;;
  *)
    echo "Invalid font mode: $font_mode" >&2
    exit 1
    ;;
esac

if [[ -z "$source_dir" ]]; then
  source_dir="$host_root/generated_course_notes"
fi

if [[ ! -d "$source_dir" ]]; then
  echo "Missing source_dir: $source_dir" >&2
  exit 1
fi

course_dir="$source_dir/$course"
if [[ ! -f "$course_dir/course.tex" ]]; then
  echo "Missing course.tex for course: $course_dir" >&2
  exit 1
fi

if [[ -z "$work_dir" ]]; then
  work_dir="$host_root/.lecture-notes-work/pocket_overflow_fix"
fi

slug="$(printf '%s__%s__%s\n' "$course" "$size_preset" "$font_mode" | tr '/ ' '__' | tr -cs 'A-Za-z0-9._-' '_')"
run_dir="$work_dir/$slug"
pdf_dir="$run_dir/pdfs"
report_dir="$run_dir/reports"
logs_dir="$run_dir/logs"
mkdir -p "$pdf_dir" "$report_dir" "$logs_dir"

if [[ -z "$session_file" ]]; then
  session_file="$host_root/.lecture-notes-work/codex_sessions/pocket-overflow-fixer.session_id"
fi
if [[ -z "$session_doc" ]]; then
  session_doc="${session_file%.session_id}.session.md"
fi

export CODEX_SHARED_SESSION_FILE="$session_file"
export CODEX_SHARED_SESSION_DOC_FILE="$session_doc"
export NOTE_TMUX_SESSION_NAME="${NOTE_TMUX_SESSION_NAME:-susskind-pocket-fix}"

extract_actionable_count() {
  python3 - "$1" <<'PY'
from pathlib import Path
import re
import sys

text = Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace")
match = re.search(r"Actionable overfull warnings: `(\d+)`", text)
print(match.group(1) if match else "")
PY
}

extract_first_actionable_file() {
  python3 - "$1" <<'PY'
from pathlib import Path
import re
import sys

text = Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace").splitlines()
for line in text:
    if not line.startswith("| "):
        continue
    parts = [part.strip() for part in line.strip().strip("|").split("|")]
    if len(parts) < 5 or parts[0] in {"Width", "---"} or parts[1] in {"File", "---"}:
        continue
    print(parts[1])
    break
PY
}

latest_report_path() {
  find "$report_dir" -maxdepth 1 -type f -name '*_overflow.md' -print | sort | tail -n 1
}

run_export() {
  local iteration="$1"
  local log_path="$logs_dir/export_iteration_${iteration}.log"
  local cmd=(
    bash "$module_root/scripts/export_course_pocket_pdfs.sh"
    --host-root "$host_root"
    --source-dir "$source_dir"
    --output-dir "$pdf_dir"
    --overflow-report-dir "$report_dir"
    --course "$course"
    --size "$size_preset"
    --font-mode "$font_mode"
    --suffix "${font_mode}_${size_preset}"
    --no-rsync
  )

  if [[ "$size_preset" == "custom" ]]; then
    cmd+=(--paper-width "$paper_width" --paper-height "$paper_height" --margin "$geometry_margin")
  fi

  "${cmd[@]}" 2>&1 | tee "$log_path"
}

run_codex_fix() {
  local iteration="$1"
  local report_path="$2"
  local focus_file="$3"
  local prompt_file="$logs_dir/fix_iteration_${iteration}.prompt.md"
  local output_file="$logs_dir/fix_iteration_${iteration}.codex.md"
  cat > "$prompt_file" <<EOF
You are fixing narrow-layout LaTeX overflow issues for one course in this repository.

Work only inside:
- \`$course_dir\`

On this iteration, focus only on the first flagged source file:
- \`$focus_file\`

Target build:
- course: \`$course\`
- size preset: \`$size_preset\`
- font mode: \`$font_mode\`

Read this report first:
- \`$report_path\`

Required editing policy:
1. Edit only \`$focus_file\` on this pass.
2. Prefer small, local fixes instead of broad global changes.
3. Preserve the scientific meaning, notation, and narrative flow.
4. Do not edit generated PDFs, build folders, README files, or unrelated courses.
5. Do not run git commands.

Preferred fix patterns:
- Split wide display equations into \`align\`, \`split\`, or short consecutive displays.
- Move wide inline math into display form when that reduces line pressure.
- Scale TikZ or figures to \`\\linewidth\` when the warning is figure-driven.
- Shorten or restructure captions and paragraphs that contain unbreakable spans.
- Avoid introducing visually ugly manual hacks unless they are local and necessary.

Success goal:
- Reduce actionable overfull warnings for this variant.
- If a warning is clearly the report's page-builder noise, ignore it.

Stop after editing. The outer script will recompile and measure the result.
EOF

  bash "$module_root/scripts/codex_prompt_to_file.sh" \
    "$host_root" \
    "$prompt_file" \
    "$output_file" \
    "$model" \
    "$reasoning" >/dev/null
}

maybe_commit() {
  local iteration="$1"
  if [[ "$do_commit" -ne 1 ]]; then
    return 0
  fi
  bash "$module_root/scripts/codex_commit_push.sh" \
    "$host_root" \
    "Fix pocket overfulls for $course [$font_mode/$size_preset] iter $iteration" \
    "generated_course_notes/$course" >/dev/null
}

snapshot_course_dir() {
  local backup_dir="$1"
  rm -rf "$backup_dir"
  mkdir -p "$backup_dir"
  rsync -a --delete "$course_dir/" "$backup_dir/"
}

restore_course_dir() {
  local backup_dir="$1"
  rsync -a --delete "$backup_dir/" "$course_dir/"
}

echo "course=$course"
echo "host_root=$host_root"
echo "work_dir=$run_dir"
echo "model=$model"
echo "reasoning=$reasoning"
echo "session_file=$CODEX_SHARED_SESSION_FILE"
echo "session_doc=$CODEX_SHARED_SESSION_DOC_FILE"
if [[ -s "$CODEX_SHARED_SESSION_FILE" ]]; then
  echo "reusing_session=$(tr -d '[:space:]' < "$CODEX_SHARED_SESSION_FILE")"
fi

run_export 0
report_path="$(latest_report_path)"
if [[ -z "$report_path" || ! -f "$report_path" ]]; then
  echo "No overflow report produced." >&2
  exit 1
fi
best_count="$(extract_actionable_count "$report_path")"
if [[ -z "$best_count" ]]; then
  echo "Could not parse actionable count from $report_path" >&2
  exit 1
fi
echo "initial_actionable_overfulls=$best_count report=$report_path"

if [[ "$best_count" -eq 0 ]]; then
  echo "No actionable overfulls remain for $course [$font_mode/$size_preset]."
  exit 0
fi

iteration=1
while [[ "$iteration" -le "$max_iterations" ]]; do
  focus_file="$(extract_first_actionable_file "$report_path")"
  if [[ -z "$focus_file" || ! -f "$focus_file" ]]; then
    echo "No actionable file could be extracted from $report_path"
    exit 1
  fi
  backup_dir="$logs_dir/backup_iteration_${iteration}"
  snapshot_course_dir "$backup_dir"
  echo "iteration=$iteration start"
  echo "iteration=$iteration focus_file=$focus_file"
  if ! run_codex_fix "$iteration" "$report_path" "$focus_file"; then
    echo "Codex edit failed on iteration $iteration; restoring previous course state."
    restore_course_dir "$backup_dir"
    run_export "restore_${iteration}" >/dev/null
    exit 1
  fi

  if ! run_export "$iteration"; then
    echo "Compile/export failed on iteration $iteration; restoring previous course state."
    restore_course_dir "$backup_dir"
    run_export "restore_${iteration}" >/dev/null
    exit 1
  fi

  new_report_path="$(latest_report_path)"
  if [[ -z "$new_report_path" || ! -f "$new_report_path" ]]; then
    restore_course_dir "$backup_dir"
    run_export "restore_${iteration}" >/dev/null
    echo "Iteration $iteration did not produce a report." >&2
    exit 1
  fi
  new_count="$(extract_actionable_count "$new_report_path")"
  if [[ -z "$new_count" ]]; then
    restore_course_dir "$backup_dir"
    run_export "restore_${iteration}" >/dev/null
    echo "Could not parse actionable count from $new_report_path" >&2
    exit 1
  fi

  echo "iteration=$iteration actionable_overfulls=$new_count previous_best=$best_count report=$new_report_path"

  if [[ "$new_count" -eq 0 ]]; then
    echo "Resolved all actionable overfulls for $course [$font_mode/$size_preset]."
    exit 0
  fi

  if [[ "$new_count" -ge "$best_count" ]]; then
    echo "No improvement after iteration $iteration; restoring previous course state."
    restore_course_dir "$backup_dir"
    run_export "restore_${iteration}" >/dev/null
    echo "No improvement after iteration $iteration; stopping to avoid churn."
    exit 0
  fi

  maybe_commit "$iteration"
  best_count="$new_count"
  report_path="$new_report_path"
  iteration=$((iteration + 1))
done

echo "Reached max iterations with actionable_overfulls=$best_count"
