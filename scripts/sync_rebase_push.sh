#!/usr/bin/env bash
set -euo pipefail

repo_root="${1:-$(pwd)}"
branch="${2:-main}"
remote="${3:-origin}"

repo_root="$(cd "$repo_root" && pwd)"
stash_name="video2book-auto-sync-$(date +%Y%m%d_%H%M%S)"
stashed=0

cleanup_on_error() {
  local status=$?
  if git -C "$repo_root" rebase --show-current-patch >/dev/null 2>&1; then
    git -C "$repo_root" rebase --abort || true
  fi
  if [[ "$stashed" -eq 1 ]]; then
    git -C "$repo_root" stash pop || true
  fi
  exit "$status"
}

trap cleanup_on_error ERR

if [[ -n "$(git -C "$repo_root" status --porcelain)" ]]; then
  git -C "$repo_root" stash push -u -m "$stash_name" >/dev/null
  stashed=1
fi

git -C "$repo_root" fetch "$remote" "$branch"
git -C "$repo_root" rebase "$remote/$branch"
git -C "$repo_root" push "$remote" "$branch"

if [[ "$stashed" -eq 1 ]]; then
  git -C "$repo_root" stash pop
fi

echo "Synced $repo_root to $remote/$branch and pushed successfully."
