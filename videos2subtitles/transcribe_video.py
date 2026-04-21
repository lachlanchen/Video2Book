#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_SOURCE_ROOT = Path(
    os.environ.get(
        "SOURCE_ROOT",
        "/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG",
    )
)


def resolve_primary_whisper_script() -> Path:
    explicit = os.environ.get("WHISPER_WITH_LANG_DETECT_SCRIPT")
    if explicit:
        candidate = Path(explicit).expanduser()
        if candidate.exists():
            return candidate
    for path in [
        Path("/home/lachlan/ProjectsLFS/whisper_with_lang_detect/vad_lang_subtitle.py"),
        Path("/home/lachlan/DiskMech/Projects/lazyedit/whisper_with_lang_detect/vad_lang_subtitle.py"),
    ]:
        if path.exists():
            return path
    return Path("/home/lachlan/ProjectsLFS/whisper_with_lang_detect/vad_lang_subtitle.py")


DEFAULT_WHISPER_SCRIPT = resolve_primary_whisper_script()
DEFAULT_FALLBACK_SCRIPT = Path(__file__).with_name("fallback_whisper_transcribe.py")
DEFAULT_CONDA_ENV = "whisper"
DEFAULT_MODEL = "large-v3"
DEFAULT_TRANSCRIPTION_ENGINE = os.environ.get("TRANSCRIPTION_ENGINE", "auto")
DEFAULT_PRIMARY_TIMEOUT_SECONDS = int(os.environ.get("TRANSCRIPTION_PRIMARY_TIMEOUT_SECONDS", "0") or "0")
VIDEO_EXTENSIONS = {".mp4", ".mkv", ".webm", ".m4a", ".mp3"}
YT_DLP_FRAGMENT_STEM_RE = re.compile(r"\.f\d+$")


def default_repo_root() -> Path:
    env_repo_root = os.environ.get("TRANSCRIPTION_REPO_ROOT")
    if env_repo_root:
        return Path(env_repo_root).expanduser()
    return Path.cwd()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Transcribe a single lecture video into repo-local subtitles and "
            "Markdown while preserving the source folder structure."
        )
    )
    parser.add_argument("--video", help="Absolute path to a single source video.")
    parser.add_argument(
        "--print-next",
        action="store_true",
        help="Print the next unprocessed source video and exit.",
    )
    parser.add_argument(
        "--repo-root",
        default=default_repo_root(),
        type=Path,
        help="Repository root that will receive markdown/ and subtitles/ outputs.",
    )
    parser.add_argument(
        "--source-root",
        default=DEFAULT_SOURCE_ROOT,
        type=Path,
        help="Root of the organized external lecture video tree.",
    )
    parser.add_argument(
        "--source-subdir",
        type=Path,
        default=Path(os.environ["SOURCE_SUBDIR"]).expanduser() if os.environ.get("SOURCE_SUBDIR") else None,
        help="Optional relative subdirectory under --source-root to scan for pending videos.",
    )
    parser.add_argument(
        "--whisper-script",
        default=DEFAULT_WHISPER_SCRIPT,
        type=Path,
        help="Path to the whisper_with_lang_detect subtitle entrypoint.",
    )
    parser.add_argument(
        "--conda-env",
        default=DEFAULT_CONDA_ENV,
        help="Conda environment that can run the Whisper subtitle script.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Whisper model name passed through to whisper_with_lang_detect.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rebuild outputs even if subtitle and Markdown files already exist.",
    )
    parser.add_argument(
        "--engine",
        default=DEFAULT_TRANSCRIPTION_ENGINE,
        choices=["auto", "primary", "fallback"],
        help=(
            "Transcription engine. auto tries the VAD/language-aware primary "
            "engine and falls back on failure/timeout; fallback skips directly "
            "to plain Whisper."
        ),
    )
    parser.add_argument(
        "--primary-timeout-seconds",
        type=int,
        default=DEFAULT_PRIMARY_TIMEOUT_SECONDS,
        help="Timeout for the primary VAD/language-aware engine. 0 disables the timeout.",
    )
    return parser


def iter_videos(source_root: Path, source_subdir: Path | None = None) -> list[Path]:
    scan_root = source_root / source_subdir if source_subdir else source_root
    videos: list[Path] = []
    for path in scan_root.rglob("*"):
        if not path.is_file():
            continue
        if path.name.endswith(".part"):
            continue
        if YT_DLP_FRAGMENT_STEM_RE.search(path.stem):
            continue
        if path.suffix.lower() not in VIDEO_EXTENSIONS:
            continue
        videos.append(path)
    return sorted(videos)


def output_paths(repo_root: Path, source_root: Path, video_path: Path) -> tuple[Path, Path, Path]:
    rel = video_path.relative_to(source_root)
    subtitle_path = repo_root / "subtitles" / rel.with_suffix(".srt")
    markdown_path = repo_root / "markdown" / rel.with_suffix(".md")
    work_video = repo_root / ".transcription_tmp" / rel
    return subtitle_path, markdown_path, work_video


def next_unprocessed_video(repo_root: Path, source_root: Path, source_subdir: Path | None = None) -> Path | None:
    for video in iter_videos(source_root, source_subdir=source_subdir):
        subtitle_path, markdown_path, _ = output_paths(repo_root, source_root, video)
        if not subtitle_path.exists() or not markdown_path.exists():
            return video
    return None


def clean_text(text: str) -> str:
    return " ".join(text.split())


def render_markdown(entries: list[dict], source_rel: Path) -> str:
    lines = [
        "# Transcript",
        "",
        f"Source: {source_rel.as_posix()}",
        "",
    ]
    for entry in entries:
        text = clean_text(str(entry.get("text", "")))
        if not text:
            continue
        start = str(entry.get("start", "")).strip()
        end = str(entry.get("end", "")).strip()
        lines.append(f"- [{start} - {end}] {text}")
    lines.append("")
    return "\n".join(lines)


def has_meaningful_entries(entries: list[dict]) -> bool:
    return any(clean_text(str(entry.get("text", ""))) for entry in entries)


def parse_srt_entries(srt_path: Path) -> list[dict]:
    entries: list[dict] = []
    content = srt_path.read_text(encoding="utf-8").strip()
    if not content:
        return entries
    for block in content.split("\n\n"):
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) < 3:
            continue
        if "-->" not in lines[1]:
            continue
        start, end = [part.strip() for part in lines[1].split("-->", 1)]
        text = " ".join(lines[2:])
        entries.append({"start": start, "end": end, "text": text})
    return entries


def cleanup_paths(paths: list[Path]) -> None:
    for path in paths:
        try:
            if path.is_symlink() or path.is_file():
                path.unlink()
        except FileNotFoundError:
            continue


def link_or_copy(source_path: Path, target_path: Path) -> None:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        if target_path.exists() or target_path.is_symlink():
            target_path.unlink()
    except FileNotFoundError:
        pass

    try:
        os.link(source_path, target_path)
    except OSError:
        shutil.copy2(source_path, target_path)


def load_entries(json_path: Path) -> list[dict]:
    return json.loads(json_path.read_text(encoding="utf-8"))


def validate_outputs(srt_path: Path, json_path: Path, source_rel: Path) -> list[dict]:
    if not srt_path.exists():
        raise FileNotFoundError(f"Subtitle output not produced: {srt_path}")
    if not json_path.exists():
        raise FileNotFoundError(f"JSON output not produced: {json_path}")

    entries = load_entries(json_path)
    if not has_meaningful_entries(entries):
        raise RuntimeError(
            f"Transcription produced no usable subtitle content for {source_rel.as_posix()}"
        )
    return entries


def run_fallback_transcription(
    *,
    source_rel: Path,
    conda_env: str,
    model: str,
    work_video: Path,
    work_wav: Path,
    work_json: Path,
    work_srt: Path,
    reason: str,
) -> None:
    fallback_input = work_wav if work_wav.exists() else work_video
    print(
        "Falling back to direct Whisper for "
        f"{source_rel.as_posix()} because {reason}.",
        flush=True,
    )
    cleanup_paths([work_srt, work_json])
    fallback_command = [
        "conda",
        "run",
        "-n",
        conda_env,
        "python",
        str(DEFAULT_FALLBACK_SCRIPT),
        "--input",
        str(fallback_input),
        "--json-output",
        str(work_json),
        "--srt-output",
        str(work_srt),
        "--model",
        model,
        "--language",
        "en",
    ]
    subprocess.run(fallback_command, check=True)


def transcribe_video(
    *,
    repo_root: Path,
    source_root: Path,
    video_path: Path,
    whisper_script: Path,
    conda_env: str,
    model: str,
    force: bool,
    engine: str,
    primary_timeout_seconds: int,
) -> tuple[Path, Path]:
    video_path = video_path.expanduser()
    if not video_path.is_absolute():
        video_path = (Path.cwd() / video_path).resolve()
    source_root = source_root.resolve()
    repo_root = repo_root.resolve()

    if not video_path.is_file():
        raise FileNotFoundError(f"Video not found: {video_path}")
    try:
        source_rel = video_path.relative_to(source_root)
    except ValueError as exc:
        raise ValueError(f"{video_path} is not under source root {source_root}") from exc

    subtitle_path, markdown_path, work_video = output_paths(repo_root, source_root, video_path)
    subtitle_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)

    if video_path.is_symlink() and not force:
        target_path = video_path.resolve()
        try:
            target_subtitle_path, target_markdown_path, _ = output_paths(
                repo_root, source_root, target_path
            )
        except ValueError:
            target_subtitle_path = None
            target_markdown_path = None
        if (
            target_subtitle_path
            and target_markdown_path
            and target_subtitle_path != subtitle_path
            and target_markdown_path != markdown_path
            and target_subtitle_path.exists()
            and target_markdown_path.exists()
        ):
            link_or_copy(target_subtitle_path, subtitle_path)
            link_or_copy(target_markdown_path, markdown_path)
            print(f"VIDEO {video_path}")
            print(f"SUBTITLE {subtitle_path}")
            print(f"MARKDOWN {markdown_path}")
            print(f"REUSED {target_subtitle_path}")
            return subtitle_path, markdown_path

    if subtitle_path.exists() and markdown_path.exists() and not force:
        print(f"SKIP {source_rel.as_posix()}")
        return subtitle_path, markdown_path

    if subtitle_path.exists() and not markdown_path.exists() and not force:
        entries = parse_srt_entries(subtitle_path)
        markdown_path.write_text(render_markdown(entries, source_rel), encoding="utf-8")
        print(f"MARKDOWN {markdown_path}")
        return subtitle_path, markdown_path

    work_video.parent.mkdir(parents=True, exist_ok=True)
    work_srt = work_video.with_suffix(".srt")
    work_json = work_video.with_suffix(".json")
    work_wav = work_video.with_suffix(".wav")

    cleanup_paths([work_video, work_srt, work_json, work_wav])
    work_video.symlink_to(video_path)

    command = [
        "conda",
        "run",
        "-n",
        conda_env,
        "python",
        str(whisper_script),
        "-t",
        str(work_video),
        "--whisper-model",
        model,
    ]

    try:
        entries: list[dict] | None = None
        if engine == "fallback":
            run_fallback_transcription(
                source_rel=source_rel,
                conda_env=conda_env,
                model=model,
                work_video=work_video,
                work_wav=work_wav,
                work_json=work_json,
                work_srt=work_srt,
                reason="the fallback engine was requested",
            )
        else:
            try:
                subprocess.run(
                    command,
                    check=True,
                    timeout=primary_timeout_seconds if primary_timeout_seconds > 0 else None,
                )
            except subprocess.TimeoutExpired:
                if engine == "primary":
                    raise
                run_fallback_transcription(
                    source_rel=source_rel,
                    conda_env=conda_env,
                    model=model,
                    work_video=work_video,
                    work_wav=work_wav,
                    work_json=work_json,
                    work_srt=work_srt,
                    reason=f"the primary subtitle engine exceeded {primary_timeout_seconds}s",
                )
            except subprocess.CalledProcessError as exc:
                if engine == "primary":
                    raise
                run_fallback_transcription(
                    source_rel=source_rel,
                    conda_env=conda_env,
                    model=model,
                    work_video=work_video,
                    work_wav=work_wav,
                    work_json=work_json,
                    work_srt=work_srt,
                    reason=f"the primary subtitle engine exited with code {exc.returncode}",
                )
            else:
                try:
                    entries = validate_outputs(work_srt, work_json, source_rel)
                except (FileNotFoundError, json.JSONDecodeError, RuntimeError) as exc:
                    if engine == "primary":
                        raise
                    run_fallback_transcription(
                        source_rel=source_rel,
                        conda_env=conda_env,
                        model=model,
                        work_video=work_video,
                        work_wav=work_wav,
                        work_json=work_json,
                        work_srt=work_srt,
                        reason=str(exc),
                    )

        if entries is None:
            entries = validate_outputs(work_srt, work_json, source_rel)
        shutil.move(str(work_srt), str(subtitle_path))
        markdown_path.write_text(render_markdown(entries, source_rel), encoding="utf-8")
    finally:
        cleanup_paths([work_video, work_srt, work_json, work_wav])

    print(f"VIDEO {video_path}")
    print(f"SUBTITLE {subtitle_path}")
    print(f"MARKDOWN {markdown_path}")
    return subtitle_path, markdown_path


def main() -> int:
    args = build_parser().parse_args()

    if args.print_next:
        next_video = next_unprocessed_video(args.repo_root, args.source_root, source_subdir=args.source_subdir)
        if next_video is not None:
            print(next_video)
        return 0

    if not args.video:
        raise SystemExit("--video is required unless --print-next is used")

    transcribe_video(
        repo_root=args.repo_root,
        source_root=args.source_root,
        video_path=Path(args.video),
        whisper_script=args.whisper_script,
        conda_env=args.conda_env,
        model=args.model,
        force=args.force,
        engine=args.engine,
        primary_timeout_seconds=args.primary_timeout_seconds,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
