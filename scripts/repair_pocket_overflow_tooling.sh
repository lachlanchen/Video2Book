#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/repair_pocket_overflow_tooling.sh [options]

Use Codex to repair the Video2Book pocket-overflow tooling itself after an
unexpected worker crash. Edits are restricted to Video2Book scripts and are
committed/pushed automatically if changes are produced.

Options:
  --host-root <path>         Host notes repo root (default: NOTES_REPO_ROOT or cwd)
  --state-file <path>        Queue state file
  --worker-log <path>        Worker log path
  --model <name>             Codex model (default: gpt-5.4)
  --reasoning <level>        low|medium|high|xhigh (default: medium)
  -h, --help                 Show this help
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
host_root="${NOTES_REPO_ROOT:-$(pwd)}"
state_file="${VIDEO2BOOK_POCKET_OVERFLOW_STATE_FILE:-$host_root/.lecture-notes-work/pocket_overflow_fix/queue_state.env}"
worker_log="${VIDEO2BOOK_WORKER_LOG_PATH:-}"
model="${NOTE_MODEL:-gpt-5.4}"
reasoning="${NOTE_REASONING:-medium}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --host-root)
      host_root="${2:-}"
      shift 2
      ;;
    --state-file)
      state_file="${2:-}"
      shift 2
      ;;
    --worker-log)
      worker_log="${2:-}"
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

if [[ -z "$worker_log" ]]; then
  worker_log="$(ls -1t "$host_root/.lecture-notes-work/logs"/susskind-pocket-fix_*.log 2>/dev/null | head -n 1 || true)"
fi

repair_dir="$host_root/.lecture-notes-work/pocket_overflow_fix/tool_repair"
mkdir -p "$repair_dir"
timestamp="$(date +%Y%m%d_%H%M%S)"
prompt_file="$repair_dir/tool_repair_${timestamp}.prompt.md"
output_file="$repair_dir/tool_repair_${timestamp}.codex.md"

cat > "$prompt_file" <<EOF
You are repairing the Video2Book pocket-overflow tooling after an unexpected worker failure.

Edit only inside this repository:
- \`$module_root\`

Edit only under:
- \`scripts/\`

Read these files first:
- queue state: \`$state_file\`
- worker log: \`$worker_log\`

Goals:
1. Keep the pocket-overflow tmux worker alive across tooling errors.
2. Preserve resume-from-state behavior and per-course publish hooks.
3. Avoid external monitor requirements.
4. Fix the actual tooling failure visible in the current log if one is present.
5. Do not modify the host notes repository.

Constraints:
- Do not edit README files, examples, references, or non-script files.
- Do not run git commands.
- Prefer small, surgical script fixes over broad rewrites.

After editing, stop.
EOF

repair_session_file="$repair_dir/pocket-overflow-tool-repair.session_id"
repair_session_doc="$repair_dir/pocket-overflow-tool-repair.session.md"

CODEX_SHARED_SESSION_FILE="$repair_session_file" \
CODEX_SHARED_SESSION_DOC_FILE="$repair_session_doc" \
NOTE_TMUX_SESSION_NAME="${NOTE_TMUX_SESSION_NAME:-susskind-pocket-fix}" \
bash "$module_root/scripts/codex_prompt_to_file.sh" \
  "$module_root" \
  "$prompt_file" \
  "$output_file" \
  "$model" \
  "$reasoning" >/dev/null

mapfile -t changed_paths < <(git -C "$module_root" status --porcelain -- scripts | awk '{print $2}')
if [[ "${#changed_paths[@]}" -eq 0 ]]; then
  echo "No tooling changes produced."
  exit 0
fi

bash "$module_root/scripts/codex_commit_push.sh" \
  "$module_root" \
  "Repair pocket overflow tooling after worker crash" \
  "${changed_paths[@]}"
