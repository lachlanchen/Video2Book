#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/fix_latex_project_overfulls.sh --repo-root <path> --project-root <path> --main-tex <file> [options]

Generic LaTeX overflow fixer for any repository. It compiles one project,
maps overfull warnings back to source lines, and asks Codex to patch the first
flagged file on each iteration.

Options:
  --repo-root <path>         Git repo root that Codex should edit (required)
  --project-root <path>      LaTeX project root (required)
  --main-tex <file>          Main TeX file relative to project root (required)
  --compile-command <cmd>    Custom shell build command run inside project root
  --work-dir <path>          Working directory for logs and reports
  --model <name>             Codex model (default: gpt-5.4)
  --reasoning <level>        low|medium|high|xhigh (default: medium)
  --max-iterations <n>       Max Codex edit passes (default: 4)
  --skip-commit              Do not commit/push after each successful pass
  -h, --help                 Show this help
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_root=""
project_root=""
main_tex=""
compile_command=""
work_dir=""
model="${NOTE_MODEL:-gpt-5.4}"
reasoning="${NOTE_REASONING:-medium}"
max_iterations=4
do_commit=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root)
      repo_root="${2:-}"
      shift 2
      ;;
    --project-root)
      project_root="${2:-}"
      shift 2
      ;;
    --main-tex)
      main_tex="${2:-}"
      shift 2
      ;;
    --compile-command)
      compile_command="${2:-}"
      shift 2
      ;;
    --work-dir)
      work_dir="${2:-}"
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

if [[ -z "$repo_root" || -z "$project_root" || -z "$main_tex" ]]; then
  echo "--repo-root, --project-root, and --main-tex are required." >&2
  exit 1
fi

if [[ -z "$work_dir" ]]; then
  work_dir="$repo_root/.latex-overflow-fix"
fi

mkdir -p "$work_dir"
build_dir="$work_dir/build"
report_path="$work_dir/overflow_report.md"
logs_dir="$work_dir/logs"
mkdir -p "$build_dir" "$logs_dir"

session_file="$repo_root/.lecture-notes-work/codex_sessions/latex-overflow-fixer.session_id"
session_doc="${session_file%.session_id}.session.md"
export CODEX_SHARED_SESSION_FILE="$session_file"
export CODEX_SHARED_SESSION_DOC_FILE="$session_doc"
export NOTE_TMUX_SESSION_NAME="${NOTE_TMUX_SESSION_NAME:-latex-overflow-fix}"

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
import sys
for line in Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace").splitlines():
    if not line.startswith("| "):
        continue
    parts = [part.strip() for part in line.strip().strip("|").split("|")]
    if len(parts) < 5 or parts[0] == "Width":
        continue
    print(parts[1])
    break
PY
}

run_compile() {
  local iteration="$1"
  local compile_log="$logs_dir/compile_iteration_${iteration}.log"
  mkdir -p "$build_dir"
  : > "$compile_log"
  if [[ -n "$compile_command" ]]; then
    (
      cd "$project_root"
      export VIDEO2BOOK_BUILD_DIR="$build_dir"
      export VIDEO2BOOK_LOG_PATH="$compile_log"
      export VIDEO2BOOK_MAIN_TEX="$main_tex"
      export VIDEO2BOOK_PROJECT_ROOT="$project_root"
      bash -lc "$compile_command"
    )
  else
    (
      cd "$project_root"
      pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$main_tex" >>"$compile_log" 2>&1
      pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" "$main_tex" >>"$compile_log" 2>&1
    )
  fi
}

run_report() {
  python3 "$module_root/scripts/report_latex_overfulls.py" \
    --log "$logs_dir/compile_iteration_$1.log" \
    --compile-root "$project_root" \
    --display-root "$project_root" \
    --output "$report_path" \
    --variant-label "$(basename "$project_root")"
}

run_codex_fix() {
  local iteration="$1"
  local focus_file="$2"
  local prompt_file="$logs_dir/fix_iteration_${iteration}.prompt.md"
  local output_file="$logs_dir/fix_iteration_${iteration}.codex.md"
  cat > "$prompt_file" <<EOF
You are fixing LaTeX overflow warnings in this project.

Work only inside:
- \`$project_root\`

Read this report first:
- \`$report_path\`

On this iteration, edit only:
- \`$focus_file\`

Rules:
1. Preserve meaning and notation.
2. Prefer local fixes: split wide equations, wrap or scale wide figures, move long inline math to display, and shorten unbreakable lines.
3. Do not edit generated PDFs or unrelated files.
4. Do not run git commands.

Stop after editing. The outer script will recompile and measure the result.
EOF
  bash "$module_root/scripts/codex_prompt_to_file.sh" \
    "$repo_root" \
    "$prompt_file" \
    "$output_file" \
    "$model" \
    "$reasoning" >/dev/null
}

maybe_commit() {
  if [[ "$do_commit" -ne 1 ]]; then
    return 0
  fi
  rel_path="$(python3 - "$repo_root" "$project_root" <<'PY'
from pathlib import Path
import sys
repo = Path(sys.argv[1]).resolve()
project = Path(sys.argv[2]).resolve()
print(project.relative_to(repo))
PY
)"
  bash "$module_root/scripts/codex_commit_push.sh" \
    "$repo_root" \
    "Fix LaTeX overfulls in $(basename "$project_root")" \
    "$rel_path" >/dev/null
}

run_compile 0
run_report 0 >/dev/null
best_count="$(extract_actionable_count "$report_path")"
if [[ -z "$best_count" || "$best_count" -eq 0 ]]; then
  echo "No actionable overfulls remain."
  exit 0
fi

iteration=1
while [[ "$iteration" -le "$max_iterations" ]]; do
  focus_file="$(extract_first_actionable_file "$report_path")"
  if [[ -z "$focus_file" ]]; then
    echo "No actionable file found in $report_path" >&2
    exit 1
  fi
  echo "iteration=$iteration focus_file=$focus_file actionable_overfulls=$best_count"
  run_codex_fix "$iteration" "$focus_file"
  maybe_commit
  run_compile "$iteration"
  run_report "$iteration" >/dev/null
  new_count="$(extract_actionable_count "$report_path")"
  if [[ -z "$new_count" ]]; then
    echo "Could not parse updated actionable count." >&2
    exit 1
  fi
  if [[ "$new_count" -eq 0 ]]; then
    echo "Resolved all actionable overfulls."
    exit 0
  fi
  if [[ "$new_count" -ge "$best_count" ]]; then
    echo "No improvement after iteration $iteration; stopping."
    exit 0
  fi
  best_count="$new_count"
  iteration=$((iteration + 1))
done

echo "Reached max iterations with actionable_overfulls=$best_count"
