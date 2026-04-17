# Figure Recheck Handoff

Date: 2026-04-17

This note documents the post-generation figure recheck pass for transcript-derived
lecture notes.

## Why This Exists

The original notes pipeline already:

- chooses subtitle-aligned windows
- probes candidate video frames with `ffmpeg`
- uses image-aware Codex prompts to select useful screenshots

That works well during first-pass note generation, but figures can still drift:

- the chosen frame may be technically sharp but contextually wrong
- a title card or talking-head shot may slip through when the lecture is still opening
- a later caption revision can become more specific than the current image really supports

The figure recheck pass fixes that after the chapter exists.

## Added Tools

- `scripts/recheck_course_figures.py`
- `scripts/process_course_figure_rechecks_one_by_one.sh`
- `scripts/start_course_figure_recheck_tmux.sh`
- `subtitles2notes/prompts/lecture_notes/figure_recheck_prompt.txt`

## What The Recheck Pass Does

For each generated lecture chapter:

1. parse `content.tex` and find inserted figure environments
2. restrict to screenshot-like assets such as `lecture_02_frame_01.png` or `lecture_06_figure_03.png`
3. read the local caption and nearby TeX context
4. search subtitle windows in the matching lecture transcript using caption/context keywords
5. extract fresh candidate frames from the source video around the best windows
6. attach the current image plus candidate frames to Codex
7. ask Codex to choose:
   - keep the current figure
   - replace it with a better-matched candidate
   - or mark it for manual review
8. if a replacement is chosen, copy it into the course `assets/` folder, patch `content.tex`, and optionally rebuild `lecture.pdf` and `course.pdf`

## Why This Is Better Than Hardcoded Figure Rules

The tool does not assume one universal timestamp recipe for every figure.

Instead it uses:

- the actual current caption
- the local chapter context
- the actual transcript window text
- the actual candidate replacement frames

That makes the decision dynamic and image-grounded instead of relying on fixed
"always take the second frame" rules.

## Recommended Usage

Audit one course:

```bash
python3 scripts/recheck_course_figures.py \
  --repo-root /path/to/host-repo \
  --source-root /path/to/video/downloads \
  --course supplementary/advanced_quantum_mechanics/2013_fall \
  --lecture-slug lecture_02 \
  --figure-index 1 \
  --model gpt-5.4 \
  --reasoning high \
  --rebuild
```

Run the whole queue in tmux:

```bash
bash scripts/start_course_figure_recheck_tmux.sh \
  --repo-root /path/to/host-repo \
  --model gpt-5.4 \
  --reasoning high
```

Audit without modifying files:

```bash
python3 scripts/recheck_course_figures.py \
  --repo-root /path/to/host-repo \
  --course supplementary/advanced_quantum_mechanics/2013_fall \
  --report-only
```

## Runtime Outputs

The tool writes runtime artifacts under:

- `<host-repo>/.lecture-notes-work/figure_recheck/<course>/<lecture>/figure_XX/`

This includes:

- candidate frame probes
- prompt files
- Codex stdout/stderr logs
- `decision.json`
- per-course `summary.json`
- per-course `summary.md`

## Validation Strategy

The first strong sanity check is whether obviously wrong frames are replaced:

- title cards
- campus shots
- lecturer-only frames
- blank boards
- off-topic diagrams

The second check is whether the updated caption remains honest to the image and
the nearby transcript context.

## Integration Rule

Use this pass after a chapter already exists. It is a repair/refinement stage,
not a substitute for the first-pass frame selection logic in
`subtitles2notes/generate_course_notes.py`.
