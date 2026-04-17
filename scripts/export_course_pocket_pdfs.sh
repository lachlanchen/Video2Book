#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/export_course_pocket_pdfs.sh [options]

Generate hand-held/compact companion PDFs from finished transcript-derived notes.

Defaults:
- host-root aware paths (tries ../generated_course_notes and ../all_notes/pocket_books)
- 6x9 inch size ("penguin")
- optional rsync to Nutstore

Options:
  --host-root <path>          Host repo root (default: parent folder of Video2Book)
  --source-dir <path>         Source directory containing generated courses (default: <host-root>/generated_course_notes)
  --output-dir <path>         Destination directory for pocket PDFs (default: <host-root>/all_notes/pocket_books if exists, else <host-root>/pocket_books)
  --course <relpath>          Limit export to one course path under generated_course_notes
  --size <preset>             Output preset: penguin (6x9, default), a5 (5.83x8.27), custom
  --font-mode <mode>          Font preset: normal (default), onepointtwo (13.2pt via scrextend), onehalf (extbook 17pt), or double (extbook 20pt)
  --paper-width <size>        Custom width for --size custom, e.g. 6in
  --paper-height <size>       Custom height for --size custom, e.g. 9in
  --margin <size>             Custom geometry margin for --size custom, e.g. 0.55in
  --suffix <suffix>           Output filename suffix (default: pocket)
  --overflow-report-dir <dir> Destination for Markdown overflow reports (default: <output-dir>/overflow_reports)
  --no-overflow-report        Skip LaTeX overflow report generation
  --nutstore-dir <dir>        Destination directory for Nutstore sync (default: /home/lachlan/Nutstore Files/Projects/LazyingArtBooks/pocket_books)
  --no-rsync                  Skip Nutstore sync
  -h, --help                  Show this help text
USAGE
}

module_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
host_root="${HOST_ROOT:-$(cd "$module_root/.." && pwd)}"
source_dir=""
output_dir=""
course_filter=""
overflow_report_dir=""
nutstore_dir="/home/lachlan/Nutstore Files/Projects/LazyingArtBooks/pocket_books"
size_preset="penguin"
font_mode="normal"
paper_width="6in"
paper_height="9in"
geometry_margin="0.55in"
name_suffix="pocket"
do_rsync=1
do_overflow_report=1
overflow_reporter="$module_root/scripts/report_latex_overfulls.py"

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
    --course)
      course_filter="$2"
      shift 2
      ;;
    --size)
      size_preset="$2"
      shift 2
      ;;
    --font-mode)
      font_mode="$2"
      shift 2
      ;;
    --paper-width)
      paper_width="$2"
      shift 2
      ;;
    --paper-height)
      paper_height="$2"
      shift 2
      ;;
    --margin)
      geometry_margin="$2"
      shift 2
      ;;
    --suffix)
      name_suffix="$2"
      shift 2
      ;;
    --overflow-report-dir)
      overflow_report_dir="$2"
      shift 2
      ;;
    --no-overflow-report)
      do_overflow_report=0
      shift
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
    output_dir="$host_root/all_notes/pocket_books"
  else
    output_dir="$host_root/pocket_books"
  fi
fi

if [[ -z "$overflow_report_dir" ]]; then
  overflow_report_dir="$output_dir/overflow_reports"
fi

case "$size_preset" in
  penguin)
    paper_width="6in"
    paper_height="9in"
    geometry_margin="0.55in"
    ;;
  a5)
    paper_width="5.83in"
    paper_height="8.27in"
    geometry_margin="0.52in"
    ;;
  custom)
    if [[ -z "$paper_width" || -z "$paper_height" || -z "$geometry_margin" ]]; then
      echo "Custom size requires --paper-width, --paper-height, and --margin" >&2
      exit 1
    fi
    ;;
  *)
    echo "Unknown size preset: $size_preset" >&2
    exit 1
    ;;
esac

case "$font_mode" in
  normal|onepointtwo|onehalf|double)
    ;;
  *)
    echo "Unknown font mode: $font_mode" >&2
    exit 1
    ;;
esac

for command in pdflatex rsync awk python3; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "Required command not found: $command" >&2
    exit 1
  fi
done

if [[ "$do_overflow_report" -eq 1 && ! -f "$overflow_reporter" ]]; then
  echo "Overflow reporter not found: $overflow_reporter" >&2
  exit 1
fi

mkdir -p "$output_dir"
if [[ "$do_overflow_report" -eq 1 ]]; then
  mkdir -p "$overflow_report_dir"
fi

declare -A CANONICAL_OUTPUTS=(
  [core/classical_mechanics/2011_fall_modern_physics_stanford_partial]=classical_mechanics_stanford_partial.pdf
  [core/classical_mechanics/2011_fall_theoretical_minimum]=classical_mechanics_theoretical_minimum.pdf
  [core/cosmology/2009_winter_legacy_cosmology]=cosmology_legacy.pdf
  [core/cosmology/2013_winter_theoretical_minimum]=cosmology_theoretical_minimum.pdf
  [core/general_relativity/2012_fall_theoretical_minimum]=general_relativity_theoretical_minimum.pdf
  [core/quantum_mechanics/2012_winter_theoretical_minimum_alt_title]=quantum_mechanics_theoretical_minimum.pdf
  [core/special_relativity/2012_spring_theoretical_minimum]=special_relativity_theoretical_minimum.pdf
  [core/statistical_mechanics/2013_spring_theoretical_minimum]=statistical_mechanics_theoretical_minimum.pdf
  [supplementary/advanced_quantum_mechanics/2013_fall]=advanced_quantum_mechanics.pdf
  [supplementary/cosmology_and_black_holes/2011_winter_topics_in_string_theory]=topics_in_string_theory.pdf
  [supplementary/higgs_boson/2012_summer]=demystifying_the_higgs_boson.pdf
  [supplementary/particle_physics_1_basic_concepts/2009_fall]=particle_physics_1_basic_concepts.pdf
  [supplementary/particle_physics_2_standard_model/2010_winter]=particle_physics_2_standard_model.pdf
  [supplementary/particle_physics_3_supersymmetry_and_grand_unification/2010_spring]=particle_physics_3_supersymmetry_and_grand_unification.pdf
  [supplementary/quantum_entanglement/2006_fall_part_1]=quantum_entanglement_part_1.pdf
  [supplementary/quantum_entanglement/2006_fall_part_3]=quantum_entanglement_part_3.pdf
  [supplementary/string_theory/2010_fall_string_theory_and_m_theory]=string_theory_and_m_theory.pdf
)

get_output_name() {
  local course_rel="$1"
  if [[ -n "${CANONICAL_OUTPUTS[$course_rel]:-}" ]]; then
    printf '%s\n' "${CANONICAL_OUTPUTS[$course_rel]}"
    return
  fi

  if [[ "$course_rel" != */* ]]; then
    printf '%s.pdf\n' "$course_rel"
    return
  fi

  local remainder="${course_rel#*/}"
  local subject="${remainder%%/*}"
  if [[ "$remainder" == "$subject" ]]; then
    printf '%s.pdf\n' "$subject"
    return
  fi

  local run="${remainder#*/}"

  if [[ "$run" == *theoretical_minimum* ]]; then
    printf '%s\n' "${subject}_theoretical_minimum.pdf"
    return
  fi
  if [[ "$run" == *modern_physics_stanford_partial* ]]; then
    printf '%s\n' "${subject}_stanford_partial.pdf"
    return
  fi
  if [[ -n "$run" ]]; then
    printf '%s\n' "${subject}_${run}.pdf"
    return
  fi

  printf '%s.pdf\n' "$subject"
}

run_tex_compile() {
  local source_dir_local="$1"
  local build_dir="$2"
  local command_log="$build_dir/pdflatex.log"
  : > "$command_log"

  local attempt
  for attempt in 1 2; do
    if ! (cd "$source_dir_local" && pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory="$build_dir" course.tex >>"$command_log" 2>&1); then
      echo "pdflatex failed on attempt $attempt" >>"$command_log"
      return 1
    fi
  done
  return 0
}

compute_stretch_dimension() {
  local ratio="$1"
  python3 - "$paper_width" "$geometry_margin" "$ratio" <<'PY'
import re
import sys

paper_width, margin, ratio = sys.argv[1], sys.argv[2], float(sys.argv[3])
UNITS = {
    "pt": 1.0,
    "bp": 72.27 / 72.0,
    "in": 72.27,
    "cm": 72.27 / 2.54,
    "mm": 72.27 / 25.4,
}

def parse_dim(raw: str) -> float:
    match = re.fullmatch(r"\s*([0-9]+(?:\.[0-9]+)?)\s*(pt|bp|in|cm|mm)\s*", raw)
    if not match:
        raise SystemExit(f"unsupported dimension: {raw}")
    value = float(match.group(1))
    unit = match.group(2)
    return value * UNITS[unit]

paper_pt = parse_dim(paper_width)
margin_pt = parse_dim(margin)
text_width_pt = max(72.0, paper_pt - 2.0 * margin_pt)
stretch_pt = max(10.0, text_width_pt * ratio)
print(f"{stretch_pt:.2f}pt")
PY
}

copy_failure_log() {
  local tmp_dir="$1"
  local course_rel="$2"
  local failure_path="$output_dir/${course_rel//\//__}_${name_suffix}_compile_failure.log"
  if [[ -f "$tmp_dir/build/pdflatex.log" ]]; then
    cp "$tmp_dir/build/pdflatex.log" "$failure_path"
    printf '%s\n' "$failure_path"
    return 0
  fi
  return 1
}

apply_pocket_layout_tuning() {
  local tex_path="$1"
  local tuned_path="${tex_path}.tuned"
  local stretch_ratio="0.022"
  local tolerance="2000"
  local hbadness="2000"
  local hfuzz="1pt"

  case "$font_mode" in
    normal)
      ;;
    onepointtwo)
      stretch_ratio="0.026"
      tolerance="3200"
      hbadness="3200"
      hfuzz="1.5pt"
      ;;
    onehalf)
      stretch_ratio="0.030"
      tolerance="4300"
      hbadness="4300"
      hfuzz="2pt"
      ;;
    double)
      stretch_ratio="0.036"
      tolerance="6500"
      hbadness="6500"
      hfuzz="3pt"
      ;;
  esac

  local stretch
  stretch="$(compute_stretch_dimension "$stretch_ratio")"

  awk -v geom="$geometry_option" -v stretch="$stretch" -v tolerance="$tolerance" -v hbadness="$hbadness" -v hfuzz="$hfuzz" -v fontmode="$font_mode" '
    /^\\input\{common_preamble\.tex\}$/ && !done {
      print "\\PassOptionsToPackage{" geom "}{geometry}";
      print $0;
      if (fontmode == "onepointtwo") {
        print "\\usepackage{scrextend}";
        print "\\changefontsizes[16pt]{13.2pt}";
      }
      print "\\AtBeginDocument{";
      print "  \\microtypesetup{protrusion=true,expansion=true}";
      print "  \\UseMicrotypeSet[protrusion]{basicmath}";
      print "  \\setlength{\\emergencystretch}{" stretch "}";
      print "  \\setlength{\\hfuzz}{" hfuzz "}";
      print "  \\pretolerance=1000";
      print "  \\tolerance=" tolerance;
      print "  \\hbadness=" hbadness;
      print "  \\allowdisplaybreaks[2]";
      print "  \\sloppy";
      print "}";
      done = 1;
      next;
    }
    { print }
  ' "$tex_path" > "$tuned_path"
  mv "$tuned_path" "$tex_path"
}

geometry_option="paperwidth=$paper_width,paperheight=$paper_height,margin=$geometry_margin"
log_file="$output_dir/${name_suffix}_export.log"

printf '[pocket] host_root=%s\n' "$host_root" | tee "$log_file"
printf '[pocket] source=%s\n' "$source_dir" | tee -a "$log_file"
printf '[pocket] output=%s\n' "$output_dir" | tee -a "$log_file"
printf '[pocket] size=%s (%s x %s, margin=%s)\n' "$size_preset" "$paper_width" "$paper_height" "$geometry_margin" | tee -a "$log_file"
printf '[pocket] font_mode=%s\n' "$font_mode" | tee -a "$log_file"
if [[ -n "$course_filter" ]]; then
  printf '[pocket] course=%s\n' "$course_filter" | tee -a "$log_file"
fi
if [[ "$do_overflow_report" -eq 1 ]]; then
  printf '[pocket] overflow_report_dir=%s\n' "$overflow_report_dir" | tee -a "$log_file"
fi
printf '[pocket] start %s\n' "$(date -Iseconds)" | tee -a "$log_file"

export_count=0
failed_count=0
failures=()

while IFS= read -r -d '' tex_path; do
  course_dir="$(dirname "$tex_path")"
  if [[ ! -f "$course_dir/course.pdf" ]]; then
    printf '[pocket] SKIP missing merged source PDF: %s\n' "$course_dir" | tee -a "$log_file"
    continue
  fi

  course_rel="${course_dir#${source_dir}/}"
  if [[ -n "$course_filter" && "$course_rel" != "$course_filter" ]]; then
    continue
  fi
  output_basename="$(get_output_name "$course_rel")"
  output_path="$output_dir/${output_basename%.pdf}_${name_suffix}.pdf"

  tmp_dir="$(mktemp -d)"
  rsync -a --delete --exclude 'build' "$course_dir/" "$tmp_dir/"

  if ! grep -q "^\\\\input{common_preamble.tex}$" "$tmp_dir/course.tex"; then
    failures+=("$course_rel: missing \\\\input{common_preamble.tex}")
    ((failed_count += 1))
    printf '[pocket] ERROR missing preamble include in %s\n' "$course_rel" | tee -a "$log_file"
    rm -rf "$tmp_dir"
    continue
  fi

  apply_pocket_layout_tuning "$tmp_dir/course.tex"

  case "$font_mode" in
    normal)
      ;;
    onepointtwo)
      ;;
    onehalf)
      perl -0pi -e 's/\\documentclass\[(.*?)\]\{book\}/\\documentclass[17pt,$1]{extbook}/s' "$tmp_dir/course.tex"
      ;;
    double)
      perl -0pi -e 's/\\documentclass\[(.*?)\]\{book\}/\\documentclass[20pt,$1]{extbook}/s' "$tmp_dir/course.tex"
      ;;
  esac

  mkdir -p "$tmp_dir/build"
  if ! run_tex_compile "$tmp_dir" "$tmp_dir/build"; then
    failures+=("$course_rel: pdflatex")
    ((failed_count += 1))
    failure_log_path="$(copy_failure_log "$tmp_dir" "$course_rel" || true)"
    if [[ -n "${failure_log_path:-}" ]]; then
      printf '[pocket] ERROR compile failed: %s (log: %s)\n' "$course_rel" "$failure_log_path" | tee -a "$log_file"
    else
      printf '[pocket] ERROR compile failed: %s\n' "$course_rel" | tee -a "$log_file"
    fi
    rm -rf "$tmp_dir"
    continue
  fi

  src_pdf="$tmp_dir/build/course.pdf"
  if [[ ! -f "$src_pdf" ]]; then
    failures+=("$course_rel: missing output PDF")
    ((failed_count += 1))
    printf '[pocket] ERROR no output PDF for %s\n' "$course_rel" | tee -a "$log_file"
    rm -rf "$tmp_dir"
    continue
  fi

  if ! mv "$src_pdf" "$output_path"; then
    failures+=("$course_rel: write")
    ((failed_count += 1))
    printf '[pocket] ERROR write failed for %s\n' "$course_rel" | tee -a "$log_file"
  else
    ((export_count += 1))
    printf '[pocket] OK %s -> %s\n' "$course_rel" "$(basename "$output_path")" | tee -a "$log_file"
    if [[ "$do_overflow_report" -eq 1 ]]; then
      report_path="$overflow_report_dir/${output_basename%.pdf}_${name_suffix}_overflow.md"
      report_summary="$(python3 "$overflow_reporter" \
        --log "$tmp_dir/build/pdflatex.log" \
        --compile-root "$tmp_dir" \
        --display-root "$course_dir" \
        --output "$report_path" \
        --variant-label "$name_suffix (${font_mode}, ${paper_width} x ${paper_height}, margin ${geometry_margin})")"
      printf '[pocket] overflow-report %s\n' "$report_summary" | tee -a "$log_file"
    fi
  fi

  rm -rf "$tmp_dir"
done < <(find "$source_dir" -type f -name course.tex -print0 | sort -z)

if [[ "$do_rsync" -eq 1 ]]; then
  mkdir -p "$nutstore_dir"
  rsync -a "$output_dir/" "$nutstore_dir/" | tee -a "$log_file"
  printf '[pocket] synced to %s\n' "$nutstore_dir" | tee -a "$log_file"
fi

printf '[pocket] completed exports=%s failures=%s\n' "$export_count" "$failed_count" | tee -a "$log_file"
printf '[pocket] done %s\n' "$(date -Iseconds)" | tee -a "$log_file"

if [[ "$failed_count" -gt 0 ]]; then
  printf '[pocket] failures: %s\n' "${failures[*]}" | tee -a "$log_file"
  exit 1
fi

printf '[pocket] all succeeded\n' | tee -a "$log_file"
