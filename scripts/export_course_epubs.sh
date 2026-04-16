#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/export_course_epubs.sh [options]

Generate EPUB3 files directly from course TeX sources.

Defaults:
- host-root aware paths (tries ../generated_course_notes)
- output to <host-root>/all_notes/epub if available, else <host-root>/epub
- optional rsync to Nutstore

Options:
  --host-root <path>          Host repo root (default: parent folder of Video2Book)
  --source-dir <path>         Source directory containing course TeX files (default: <host-root>/generated_course_notes)
  --output-dir <path>         Destination directory for EPUB files (default: <host-root>/all_notes/epub if exists, else <host-root>/epub)
  --nutstore-dir <dir>        Destination directory for Nutstore sync (default: /home/lachlan/Nutstore Files/Projects/LazyingArtBooks/epub)
  --course <relative_path>     Process only one course dir relative to source (e.g. core/statistical_mechanics/2013_spring_theoretical_minimum)
  --no-rsync                  Skip Nutstore sync
  -h, --help                  Show this help text
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
host_root="${HOST_ROOT:-$(cd "$module_root/.." && pwd)}"
source_dir=""
output_dir=""
nutstore_dir="/home/lachlan/Nutstore Files/Projects/LazyingArtBooks/epub"
target_course=""
do_rsync=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --host-root)
      host_root="$2"
      shift 2
      ;;
    --source-dir)
      source_dir="$2"
      shift 2
      ;;
    --output-dir)
      output_dir="$2"
      shift 2
      ;;
    --nutstore-dir)
      nutstore_dir="$2"
      shift 2
      ;;
    --course)
      target_course="$2"
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
  if [[ -d "$host_root/generated_course_notes" ]]; then
    source_dir="$host_root/generated_course_notes"
  elif [[ -d "$module_root/generated_course_notes" ]]; then
    source_dir="$module_root/generated_course_notes"
  else
    echo "Cannot find generated_course_notes under $host_root or $module_root" >&2
    exit 1
  fi
fi

if [[ -z "$output_dir" ]]; then
  if [[ -d "$host_root/all_notes" ]]; then
    output_dir="$host_root/all_notes/epub"
  else
    output_dir="$host_root/epub"
  fi
fi

for command in pandoc rsync; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "Required command not found: $command" >&2
    exit 1
  fi
done

mkdir -p "$output_dir"

declare -A CANONICAL_OUTPUTS=(
  [core/classical_mechanics/2011_fall_modern_physics_stanford_partial]=classical_mechanics_stanford_partial.epub
  [core/classical_mechanics/2011_fall_theoretical_minimum]=classical_mechanics_theoretical_minimum.epub
  [core/cosmology/2009_winter_legacy_cosmology]=cosmology_legacy.epub
  [core/cosmology/2013_winter_theoretical_minimum]=cosmology_theoretical_minimum.epub
  [core/general_relativity/2012_fall_theoretical_minimum]=general_relativity_theoretical_minimum.epub
  [core/quantum_mechanics/2012_winter_theoretical_minimum_alt_title]=quantum_mechanics_theoretical_minimum.epub
  [core/special_relativity/2012_spring_theoretical_minimum]=special_relativity_theoretical_minimum.epub
  [core/statistical_mechanics/2013_spring_theoretical_minimum]=statistical_mechanics_theoretical_minimum.epub
  [supplementary/advanced_quantum_mechanics/2013_fall]=advanced_quantum_mechanics.epub
  [supplementary/cosmology_and_black_holes/2011_winter_topics_in_string_theory]=topics_in_string_theory.epub
  [supplementary/higgs_boson/2012_summer]=demystifying_the_higgs_boson.epub
  [supplementary/particle_physics_1_basic_concepts/2009_fall]=particle_physics_1_basic_concepts.epub
  [supplementary/particle_physics_2_standard_model/2010_winter]=particle_physics_2_standard_model.epub
  [supplementary/particle_physics_3_supersymmetry_and_grand_unification/2010_spring]=particle_physics_3_supersymmetry_and_grand_unification.epub
  [supplementary/quantum_entanglement/2006_fall_part_1]=quantum_entanglement_part_1.epub
  [supplementary/quantum_entanglement/2006_fall_part_3]=quantum_entanglement_part_3.epub
  [supplementary/string_theory/2010_fall_string_theory_and_m_theory]=string_theory_and_m_theory.epub
)

get_output_name() {
  local course_rel="$1"
  if [[ -n "${CANONICAL_OUTPUTS[$course_rel]:-}" ]]; then
    printf '%s\n' "${CANONICAL_OUTPUTS[$course_rel]}"
    return
  fi

  local subject="${course_rel#*/}"
  subject="${subject%%/*}"
  local run="${course_rel#*/$subject/}"
  printf '%s_%s.epub\n' "$subject" "$run"
}

run_pandoc_convert() {
  local source_dir_local="$1"
  local dest_file="$2"
  local command_log="$3"
  local title=""

  title="$(sed -n 's/^[[:space:]]*\\title{\(.*\)}[[:space:]]*$/\\1/p' "$source_dir_local/course.tex" | head -n 1)"

  if [[ -n "$title" ]]; then
    pandoc "$source_dir_local/course.tex" \
      --from=latex+raw_tex \
      --to=epub3 \
      --standalone \
      --resource-path="$source_dir_local:$source_dir_local/build:$source_dir_local/figures:$source_dir_local/assets" \
      --toc \
      --metadata="title:$title" \
      --output="$dest_file" >>"$command_log" 2>&1
  else
    pandoc "$source_dir_local/course.tex" \
      --from=latex+raw_tex \
      --to=epub3 \
      --standalone \
      --resource-path="$source_dir_local:$source_dir_local/build:$source_dir_local/figures:$source_dir_local/assets" \
      --toc \
      --output="$dest_file" >>"$command_log" 2>&1
  fi
}

log_file="$output_dir/epub_export.log"

printf '[epub-export] source=%s\n' "$source_dir" | tee "$log_file"
printf '[epub-export] output=%s\n' "$output_dir" | tee -a "$log_file"
printf '[epub-export] start %s\n' "$(date -Iseconds)" | tee -a "$log_file"

export_count=0
failed_count=0
failures=()

if [[ -n "$target_course" ]]; then
  course_glob="$source_dir/$target_course/course.tex"
else
  course_glob="$source_dir/*/*/course.tex"
fi

if [[ -n "$target_course" ]]; then
  if [[ ! -f "$course_glob" ]]; then
    echo "[epub-export] missing target course.tex: $course_glob" | tee -a "$log_file"
    exit 1
  fi
fi

if [[ -n "$target_course" ]]; then
  courses=("$course_glob")
else
  mapfile -d '' courses < <(find "$source_dir" -type f -name course.tex -print0 | sort -z)
fi

for tex_path in "${courses[@]}"; do
  course_dir="$(dirname "$tex_path")"
  course_rel="${course_dir#${source_dir}/}"
  output_file="$output_dir/$(get_output_name "$course_rel")"

  if ! run_pandoc_convert "$course_dir" "$output_file" "$log_file"; then
    failures+=("$course_rel: pandoc")
    ((failed_count += 1))
    printf '[epub-export] ERROR: %s\n' "$course_rel" | tee -a "$log_file"
    continue
  fi

  if [[ ! -f "$output_file" ]]; then
    failures+=("$course_rel: missing output")
    ((failed_count += 1))
    printf '[epub-export] ERROR: output missing for %s\n' "$course_rel" | tee -a "$log_file"
    continue
  fi

  ((export_count += 1))
  printf '[epub-export] OK: %s -> %s\n' "$(basename "$tex_path")" "$(basename "$output_file")" | tee -a "$log_file"
done

if [[ "$do_rsync" -eq 1 ]]; then
  mkdir -p "$nutstore_dir"
  rsync -a "$output_dir/" "$nutstore_dir/" | tee -a "$log_file"
  printf '[epub-export] synced to %s\n' "$nutstore_dir" | tee -a "$log_file"
fi

printf '[epub-export] completed exports=%s failures=%s\n' "$export_count" "$failed_count" | tee -a "$log_file"
printf '[epub-export] done %s\n' "$(date -Iseconds)" | tee -a "$log_file"

if [[ "$failed_count" -gt 0 ]]; then
  printf '[epub-export] failures: %s\n' "${failures[*]}" | tee -a "$log_file"
  exit 1
fi

printf '[epub-export] all succeeded\n' | tee -a "$log_file"
