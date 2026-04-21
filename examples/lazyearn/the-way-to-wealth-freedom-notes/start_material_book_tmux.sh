#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$script_dir/../common.sh"
load_lazyearn_course_env "$script_dir"

material_root="${MATERIAL_BOOK_SOURCE_DIR:-$HOST_REPO_ROOT/$MATERIAL_BOOK_SOURCE_DIR_DEFAULT}"
output_dir="${MATERIAL_BOOK_OUTPUT_DIR:-$HOST_REPO_ROOT/$MATERIAL_BOOK_OUTPUT_DIR_DEFAULT}"

cd "$HOST_REPO_ROOT"
exec bash "$VIDEO2BOOK_ROOT/scripts/start_markdown_material_book_tmux.sh" \
  --session "${MATERIAL_BOOK_SESSION}" \
  --repo-root "$HOST_REPO_ROOT" \
  --material-root "$material_root" \
  --output-dir "$output_dir" \
  --title "${MATERIAL_BOOK_TITLE:-$MATERIAL_BOOK_TITLE_DEFAULT}" \
  --subtitle "${MATERIAL_BOOK_SUBTITLE:-$MATERIAL_BOOK_SUBTITLE_DEFAULT}" \
  --source-credit "${MATERIAL_BOOK_SOURCE_CREDIT:-$MATERIAL_BOOK_SOURCE_CREDIT_DEFAULT}" \
  --curator "${MATERIAL_BOOK_CURATOR:-LazyingArt LLC}" \
  --language "${MATERIAL_BOOK_LANGUAGE:-$MATERIAL_BOOK_LANGUAGE_DEFAULT}" \
  --model "${MATERIAL_BOOK_MODEL:-$MATERIAL_BOOK_MODEL_DEFAULT}" \
  --reasoning "${MATERIAL_BOOK_REASONING:-$MATERIAL_BOOK_REASONING_DEFAULT}" \
  --compile-engine "${MATERIAL_BOOK_COMPILE_ENGINE:-$MATERIAL_BOOK_COMPILE_ENGINE_DEFAULT}" \
  --commit-each \
  "$@"
