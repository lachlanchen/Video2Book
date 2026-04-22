#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: start_unique_notes_pocket_tmux.sh [options]

Runs the strict unique-lecture Entrepreneurship note writer, then exports the
finished course PDF as a 6x9 pocket PDF with the onepointtwo font preset.

Options:
  --kill       Kill and recreate the tmux session if it already exists.
  --no-attach  Start in the background without attaching.
  -h, --help   Show this help text.
USAGE
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$script_dir/../common.sh"
load_lazyearn_course_env "$script_dir"

kill_existing=0
attach=1
while [[ $# -gt 0 ]]; do
  case "$1" in
    --kill)
      kill_existing=1
      shift
      ;;
    --no-attach)
      attach=0
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

note_model="${NOTE_MODEL:-$NOTE_MODEL_DEFAULT}"
note_reasoning="${NOTE_REASONING:-$NOTE_REASONING_DEFAULT}"
note_session_scope="${NOTE_CODEX_SESSION_SCOPE:-$NOTE_SESSION_SCOPE_DEFAULT}"
log_dir="$HOST_REPO_ROOT/.lecture-notes-work/logs"
runner_dir="$HOST_REPO_ROOT/.lecture-notes-work/runners"
mkdir -p "$log_dir" "$runner_dir"
timestamp="$(date +%Y%m%d_%H%M%S)"
log_path="$log_dir/${NOTES_SESSION}_${timestamp}.log"
runner_path="$runner_dir/${NOTES_SESSION}.sh"
output_dir="$HOST_REPO_ROOT/all_notes/pocket_books_1_2x"
nutstore_dir="/home/lachlan/Nutstore Files/Projects/LazyingArtBooks/lazyearn/pocket_books_1_2x"

if tmux has-session -t "$NOTES_SESSION" 2>/dev/null; then
  if [[ "$kill_existing" -eq 1 ]]; then
    tmux kill-session -t "$NOTES_SESSION"
  else
    if [[ "$attach" -eq 1 ]]; then
      exec tmux attach -t "$NOTES_SESSION"
    fi
    echo "tmux session already running: $NOTES_SESSION"
    exit 0
  fi
fi

cat > "$runner_path" <<RUNNER
#!/usr/bin/env bash
set -euo pipefail
cd "$HOST_REPO_ROOT"
export NOTES_REPO_ROOT="$HOST_REPO_ROOT"
export NOTE_SOURCE_ROOT="$TRANSCRIPTION_SOURCE_ROOT"
export NOTE_TMUX_SESSION_NAME="$NOTES_SESSION"
export NOTE_CODEX_SESSION_FILE="$HOST_REPO_ROOT/.lecture-notes-work/codex_sessions/$NOTES_SESSION.session_id"
export NOTE_CODEX_SESSION_DOC_FILE="$HOST_REPO_ROOT/.lecture-notes-work/codex_sessions/$NOTES_SESSION.session.md"
export VIDEO2BOOK_COURSE_CONFIG="$COURSE_CONFIG_PATH"
export VIDEO2BOOK_REFERENCE_PDF_DIR="$HOST_REPO_ROOT/references/course-books/$COURSE_SLUG"

set +e
bash "$VIDEO2BOOK_ROOT/scripts/process_course_notes_one_by_one.sh" \\
  --course "$COURSE_REL" \\
  --model "$note_model" \\
  --reasoning "$note_reasoning" \\
  --session-scope "$note_session_scope" \\
  --allow-partial-course \\
  2>&1 | tee "$log_path"
status=\${PIPESTATUS[0]}
set -e

if [[ "\$status" -eq 0 ]]; then
  bash "$VIDEO2BOOK_ROOT/scripts/export_course_pocket_pdfs.sh" \\
    --host-root "$HOST_REPO_ROOT" \\
    --course "$COURSE_REL" \\
    --output-dir "$output_dir" \\
    --font-mode onepointtwo \\
    --suffix pocket_1_2x \\
    --nutstore-dir "$nutstore_dir"
fi

echo
echo "notes worker exit status: \$status"
echo "tmux session kept open for inspection; exit the shell to close it."
exec bash
RUNNER
chmod +x "$runner_path"

tmux new-session -d -s "$NOTES_SESSION" -c "$HOST_REPO_ROOT" "bash '$runner_path'"
tmux rename-window -t "$NOTES_SESSION:0" "notes"
tmux set-option -t "$NOTES_SESSION" -g mouse on

echo "tmux session: $NOTES_SESSION"
echo "log: $log_path"
echo "runner: $runner_path"
echo "attach: tmux attach -t $NOTES_SESSION"

if [[ "$attach" -eq 1 ]]; then
  exec tmux attach -t "$NOTES_SESSION"
fi
