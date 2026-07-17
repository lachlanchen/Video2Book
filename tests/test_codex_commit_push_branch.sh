#!/usr/bin/env bash
set -euo pipefail

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

git init --bare "$tmp_dir/remote.git" >/dev/null
git init "$tmp_dir/work" >/dev/null
git -C "$tmp_dir/work" config user.name "Video2Book Test"
git -C "$tmp_dir/work" config user.email "video2book@example.invalid"
git -C "$tmp_dir/work" checkout -b editorial-test >/dev/null
git -C "$tmp_dir/work" remote add origin "$tmp_dir/remote.git"

mkdir -p "$tmp_dir/bin"
cat > "$tmp_dir/bin/codex" <<'SH'
#!/usr/bin/env bash
exit 1
SH
chmod +x "$tmp_dir/bin/codex"

printf 'branch-neutral push\n' > "$tmp_dir/work/result.txt"
PATH="$tmp_dir/bin:$PATH" bash "$module_root/scripts/codex_commit_push.sh" \
  "$tmp_dir/work" \
  "Test branch-neutral push" \
  result.txt >/dev/null

test "$(git --git-dir="$tmp_dir/remote.git" show main:result.txt)" = "branch-neutral push"
test "$(git -C "$tmp_dir/work" branch --show-current)" = "editorial-test"
