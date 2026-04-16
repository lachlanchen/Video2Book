#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/export_course_epubs.sh [options]

Options:
  --source-dir <dir>       Source directory containing full-course PDFs (required)
  --epub-dir <dir>         Destination directory for EPUB outputs (default: <source-dir>/epub)
  --nutstore-dir <dir>     Destination directory for Nutstore sync (default: /home/lachlan/Nutstore Files/Projects/LazyingArtBooks/epub)
  --no-rsync               Skip Nutstore sync
  --help                   Show this help text
USAGE
}

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir=""
epub_dir=""
nutstore_dir="/home/lachlan/Nutstore Files/Projects/LazyingArtBooks/epub"
do_rsync=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --source-dir)
      source_dir="$2"
      shift 2
      ;;
    --epub-dir)
      epub_dir="$2"
      shift 2
      ;;
    --nutstore-dir)
      nutstore_dir="$2"
      shift 2
      ;;
    --no-rsync)
      do_rsync=0
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

if [[ -z "$source_dir" ]]; then
  echo "Required option missing: --source-dir" >&2
  usage >&2
  exit 1
fi

source_dir="$(cd "$source_dir" && pwd)"
epub_dir="${epub_dir:-$source_dir/epub}"

for command in pdftotext pandoc rsync; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "Required command not found: $command" >&2
    exit 1
  fi
done

mkdir -p "$epub_dir"
mkdir -p "$source_dir"

export_count=0
failed_count=0
failures=()
log_file="$epub_dir/export_course_epubs.log"

echo "[epub-export] source=$source_dir" | tee "$log_file"
echo "[epub-export] output=$epub_dir" | tee -a "$log_file"
echo "[epub-export] start $(date -Iseconds)" | tee -a "$log_file"

for pdf_path in "$source_dir"/*.pdf; do
  if [[ ! -f "$pdf_path" ]]; then
    echo "[epub-export] no PDFs found in $source_dir" | tee -a "$log_file"
    break
  fi

  pdf_stem="$(basename "$pdf_path" .pdf)"
  epub_path="$epub_dir/$pdf_stem.epub"

  title_raw=""
  if pdf_info_output="$(pdfinfo "$pdf_path" 2>/dev/null)"; then
    title_raw="$(printf '%s\n' "$pdf_info_output" | awk -F': ' '/^Title:/{sub(/^Title: /, "", $0); print $2; exit}')"
  fi
  if [[ -z "$title_raw" || "$title_raw" == "-" ]]; then
    title="$pdf_stem"
    title="${title//_/ }"
  else
    title="$title_raw"
  fi

  text_tmp="$(mktemp)"
  if ! pdftotext -layout "$pdf_path" "$text_tmp"; then
    echo "[epub-export] ERROR: pdftotext failed for $pdf_stem" | tee -a "$log_file"
    failures+=("$pdf_stem: pdftotext")
    rm -f "$text_tmp"
    ((failed_count += 1))
    continue
  fi

  if [[ ! -s "$text_tmp" ]]; then
    echo "[epub-export] ERROR: no extracted text for $pdf_stem" | tee -a "$log_file"
    failures+=("$pdf_stem: no text")
    rm -f "$text_tmp"
    ((failed_count += 1))
    continue
  fi

  meta_tmp="$(mktemp)"
  {
    printf "title: |\n"
    printf "  %s\n" "$title"
    printf "creator: Video2Book (LazyingArt LLC)\n"
  } > "$meta_tmp"

  if pandoc -f markdown -t epub3 --standalone --metadata-file "$meta_tmp" -o "$epub_path" < "$text_tmp"; then
    echo "[epub-export] OK: $(basename "$pdf_path") -> $(basename "$epub_path")" | tee -a "$log_file"
    ((export_count += 1))
  else
    echo "[epub-export] ERROR: pandoc failed for $pdf_stem" | tee -a "$log_file"
    failures+=("$pdf_stem: pandoc")
    ((failed_count += 1))
  fi

  rm -f "$text_tmp" "$meta_tmp"
done

if [[ "$do_rsync" -eq 1 ]]; then
  mkdir -p "$nutstore_dir"
  rsync -a "$epub_dir/" "$nutstore_dir/" | tee -a "$log_file"
  echo "[epub-export] synced EPUB folder to $nutstore_dir" | tee -a "$log_file"
fi

echo "[epub-export] completed exports=$export_count failures=$failed_count" | tee -a "$log_file"
echo "[epub-export] done $(date -Iseconds)" | tee -a "$log_file"

if [[ "$failed_count" -gt 0 ]]; then
  echo "[epub-export] failures recorded: ${failures[*]}" | tee -a "$log_file"
  exit 1
fi

echo "[epub-export] all succeeded" | tee -a "$log_file"
