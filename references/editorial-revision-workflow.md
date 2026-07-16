# Source-Aware Editorial Revision

Video2Book separates initial note generation from editorial revision. The revision pass is intended for books that compile successfully but still contain formulaic prose, prompt-shaped structure, weak provenance, or questionable figures.

The motivating corpus audit is recorded in [susskind-corpus-audit-2026-07.md](susskind-corpus-audit-2026-07.md).

## Editorial Contract

The versioned charter in `subtitles2notes/prompts/editorial_revision/editorial_charter.txt` is injected into every writer, critic, and repair call. It requires direct explanatory prose, preserves useful lecture repetition, keeps only verified classroom exchanges, and prohibits internal process language in chapter bodies.

Each revised chapter receives:

- `editorial_audit.json` and `editorial_audit.md`
- `editorial_fidelity.json`
- `source_map.json`
- revised `content.tex` and compiled `lecture.pdf`

The source map classifies prose, equations, Q&A, and figures as transcript, blackboard, named-reference, or editorial material. Nontrivial reconstruction is also identified in the PDF with a concise footnote.

Use `\lecturetimestamp{HH:MM:SS}` only inside `classroomqa`; it creates the Q&A timestamp footnote. Put a retained video's frame time in `\lectureframe{HH:MM:SS}` immediately after the figure caption. Do not place `\lecturetimestamp` on its own or nest it inside `\editorialnote`, because either form produces orphan or nested footnote markers. The deterministic scan blocks those placements.

## Run One Course

```bash
./Video2Book/scripts/start_editorial_revision_tmux.sh \
  --repo-root "$PWD" \
  --session susskind-editorial \
  --course core/cosmology/2009_winter_legacy_cosmology \
  --reference core_cosmology \
  --model gpt-5.4 \
  --reasoning xhigh
```

The queue reuses one global writer session and sends an explicit boundary packet before each course. Commit/push calls use their separate helper session, preventing Git or monitoring language from entering the writer context. State under `.editorial-revision-work/` makes the run resumable.

Editorial writer sessions are created with Codex's read-only sandbox. The access mode is recorded next to the session ID, and the wrapper refuses to resume a session created with a different access level. Only the outer Python driver may replace chapter sources or compile PDFs after the audit and fidelity gates pass.

## Deterministic Audit

Run a local corpus scan without invoking Codex:

```bash
python3 Video2Book/subtitles2notes/editorial_revision.py \
  --repo-root "$PWD" \
  --scan-only \
  --scan-report references/editorial-corpus-scan.md
```

The scan reports body credits, internal tooling, transformed directives, production language, formulaic choreography, legacy Q&A headings, forced summaries, and duplicate chapter titles. A rewrite is accepted only when deterministic error rules and the source-fidelity critic both pass.

## Safety

Use a clean branch or worktree when the host repository has unrelated edits. Candidate prose is written under the runtime directory first. `content.tex` is replaced only after audit, rewrite, and fidelity gates pass; a failed LaTeX build restores the previous chapter source. Intermediate LaTeX files remain under the runtime `build/` directories.
