#!/usr/bin/env bash
set -euo pipefail

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
temp_dir="$(mktemp -d)"
trap 'rm -rf "$temp_dir"' EXIT
mkdir -p "$temp_dir/bin" "$temp_dir/repo"
printf 'Return OK.\n' > "$temp_dir/prompt.txt"

cat > "$temp_dir/bin/codex" <<'MOCK'
#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' "$@" > "$MOCK_CODEX_ARGS"
output=""
while [[ $# -gt 0 ]]; do
  if [[ "$1" == "-o" || "$1" == "--output-last-message" ]]; then
    output="$2"
    shift 2
    continue
  fi
  shift
done
printf 'OK\n' > "$output"
printf '%s\n' '{"type":"thread.started","thread_id":"00000000-0000-0000-0000-000000000001"}'
MOCK
chmod +x "$temp_dir/bin/codex"

export PATH="$temp_dir/bin:$PATH"
export MOCK_CODEX_ARGS="$temp_dir/codex.args"
export CODEX_SHARED_SESSION_FILE="$temp_dir/writer.session_id"
export CODEX_SHARED_SESSION_DOC_FILE="$temp_dir/writer.session.md"
export CODEX_PROMPT_ACCESS=read-only

bash "$module_root/scripts/codex_prompt_to_file.sh" \
  "$temp_dir/repo" \
  "$temp_dir/prompt.txt" \
  "$temp_dir/output.txt" \
  gpt-test \
  high >/dev/null

grep -Fx -- "--sandbox" "$temp_dir/codex.args" >/dev/null
grep -Fx -- "read-only" "$temp_dir/codex.args" >/dev/null
grep -Fx -- "read-only" "$CODEX_SHARED_SESSION_FILE.access" >/dev/null
grep -F -- "prompt access: read-only" "$CODEX_SHARED_SESSION_DOC_FILE" >/dev/null

rm -f "$CODEX_SHARED_SESSION_FILE.access"
set +e
bash "$module_root/scripts/codex_prompt_to_file.sh" \
  "$temp_dir/repo" \
  "$temp_dir/prompt.txt" \
  "$temp_dir/output-2.txt" \
  gpt-test \
  high >/dev/null 2>&1
status=$?
set -e
[[ "$status" -eq 3 ]]

rm -f "$CODEX_SHARED_SESSION_FILE" "$CODEX_SHARED_SESSION_FILE.access"
mkdir -p "$temp_dir/editable-workspace"
export CODEX_PROMPT_ACCESS=workspace-write
export CODEX_PROMPT_WORKSPACE="$temp_dir/editable-workspace"

bash "$module_root/scripts/codex_prompt_to_file.sh" \
  "$temp_dir/repo" \
  "$temp_dir/prompt.txt" \
  "$temp_dir/output-editable.txt" \
  gpt-test \
  high >/dev/null

grep -Fx -- "--sandbox" "$temp_dir/codex.args" >/dev/null
grep -Fx -- "workspace-write" "$temp_dir/codex.args" >/dev/null
grep -Fx -- "$temp_dir/editable-workspace" "$temp_dir/codex.args" >/dev/null
grep -Fx -- "workspace-write" "$CODEX_SHARED_SESSION_FILE.access" >/dev/null
grep -F -- "writable workspace: $temp_dir/editable-workspace" "$CODEX_SHARED_SESSION_DOC_FILE" >/dev/null
