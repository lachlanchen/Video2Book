#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shlex
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Sequence
from urllib.parse import parse_qs, urlparse


DEFAULT_PLAYLIST_URL = (
    "https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG"
)
DEFAULT_WORKSPACE = Path("/home/lachlan/ProjectsLFS/YoutubeDownloader")
DEFAULT_OUTPUT_TEMPLATE = "%(playlist_index)03d - %(title)s [%(id)s].%(ext)s"
DEFAULT_FORMAT = "bv*+ba/b"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Download or refresh a YouTube playlist with yt-dlp using a stable "
            "archive layout and log files."
        )
    )
    parser.add_argument(
        "--playlist-url",
        default=DEFAULT_PLAYLIST_URL,
        help="Playlist URL to download. Defaults to the Susskind physics playlist.",
    )
    parser.add_argument(
        "--workspace",
        type=Path,
        default=DEFAULT_WORKSPACE,
        help="External downloader workspace. Defaults to /home/lachlan/ProjectsLFS/YoutubeDownloader.",
    )
    parser.add_argument(
        "--download-root",
        type=Path,
        help="Override the downloads root. Defaults to <workspace>/downloads.",
    )
    parser.add_argument(
        "--download-subdir",
        help="Optional relative subdirectory under the downloads root. Defaults to the playlist id.",
    )
    parser.add_argument(
        "--log-root",
        type=Path,
        help="Override the logs root. Defaults to <workspace>/logs.",
    )
    parser.add_argument(
        "--format",
        default=DEFAULT_FORMAT,
        help="yt-dlp format selector. Defaults to %(default)s.",
    )
    parser.add_argument(
        "--playlist-start",
        type=int,
        default=1,
        help="First playlist entry to process.",
    )
    parser.add_argument(
        "--playlist-end",
        type=int,
        help="Last playlist entry to process.",
    )
    parser.add_argument(
        "--concurrent-fragments",
        type=int,
        default=8,
        help="Fragment concurrency for yt-dlp.",
    )
    parser.add_argument(
        "--retries",
        default="infinite",
        help="Retry policy passed to yt-dlp. Defaults to %(default)s.",
    )
    parser.add_argument(
        "--yt-dlp",
        type=Path,
        help="Explicit path to the yt-dlp executable.",
    )
    parser.add_argument(
        "--archive-file",
        type=Path,
        help="Override the download archive file. Defaults to <log-root>/playlist_<id>.archive.",
    )
    parser.add_argument(
        "--output-template",
        default=DEFAULT_OUTPUT_TEMPLATE,
        help="Filename template inside the playlist download directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the resolved command and paths without downloading.",
    )
    parser.add_argument(
        "yt_dlp_args",
        nargs=argparse.REMAINDER,
        help="Extra arguments forwarded directly to yt-dlp. Prefix with --.",
    )
    args = parser.parse_args()
    if args.yt_dlp_args and args.yt_dlp_args[0] == "--":
        args.yt_dlp_args = args.yt_dlp_args[1:]
    return args


def extract_playlist_id(url: str) -> str:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    playlist_ids = query.get("list")
    if playlist_ids and playlist_ids[0]:
        return playlist_ids[0]
    raise SystemExit(f"Could not extract a playlist id from URL: {url}")


def resolve_ytdlp(explicit_path: Path | None, workspace: Path) -> Path:
    candidates: list[Path] = []
    if explicit_path is not None:
        candidates.append(explicit_path)
    candidates.append(workspace / ".ytdlp-venv" / "bin" / "yt-dlp")
    which = shutil.which("yt-dlp")
    if which:
        candidates.append(Path(which))
    for candidate in candidates:
        if candidate and candidate.exists():
            return candidate
    raise SystemExit(
        "Could not find yt-dlp. Install it or pass --yt-dlp /path/to/yt-dlp."
    )


def resolve_paths(args: argparse.Namespace, playlist_id: str) -> tuple[Path, Path, Path]:
    download_root = (args.download_root or (args.workspace / "downloads")).expanduser()
    log_root = (args.log_root or (args.workspace / "logs")).expanduser()
    download_subdir = Path(args.download_subdir) if args.download_subdir else Path(playlist_id)
    download_dir = download_root / download_subdir
    archive_file = args.archive_file or (log_root / f"playlist_{playlist_id}.archive")
    return download_dir, log_root, archive_file.expanduser()


def build_command(
    yt_dlp_path: Path,
    args: argparse.Namespace,
    download_dir: Path,
    archive_file: Path,
) -> list[str]:
    command = [
        str(yt_dlp_path),
        args.playlist_url,
        "--newline",
        "--continue",
        "--ignore-errors",
        "--download-archive",
        str(archive_file),
        "--retries",
        str(args.retries),
        "--concurrent-fragments",
        str(args.concurrent_fragments),
        "--format",
        args.format,
        "--output",
        str(download_dir / args.output_template),
    ]
    if args.playlist_start != 1:
        command.extend(["--playlist-start", str(args.playlist_start)])
    if args.playlist_end is not None:
        command.extend(["--playlist-end", str(args.playlist_end)])
    node_path = shutil.which("node")
    if node_path:
        command.extend(["--js-runtimes", f"node:{node_path}"])
    command.extend(args.yt_dlp_args)
    return command


def write_log_header(
    log_file: Path,
    playlist_id: str,
    playlist_url: str,
    download_dir: Path,
    archive_file: Path,
    command: Sequence[str],
) -> None:
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    header = [
        f"# Timestamp: {timestamp}",
        f"# Playlist URL: {playlist_url}",
        f"# Playlist ID: {playlist_id}",
        f"# Download directory: {download_dir}",
        f"# Archive file: {archive_file}",
        f"# Command: {shlex.join(command)}",
        "",
    ]
    log_file.write_text("\n".join(header), encoding="utf-8")


def stream_command(command: Sequence[str], log_file: Path) -> int:
    with log_file.open("a", encoding="utf-8") as handle:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert process.stdout is not None
        for line in process.stdout:
            sys.stdout.write(line)
            handle.write(line)
        return process.wait()


if __name__ == "__main__":
    args = parse_args()
    playlist_id = extract_playlist_id(args.playlist_url)
    workspace = args.workspace.expanduser()
    download_dir, log_root, archive_file = resolve_paths(args, playlist_id)
    yt_dlp_path = resolve_ytdlp(args.yt_dlp, workspace)
    log_root.mkdir(parents=True, exist_ok=True)
    download_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_root / f"ytplaylist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    command = build_command(yt_dlp_path, args, download_dir, archive_file)
    write_log_header(
        log_file,
        playlist_id,
        args.playlist_url,
        download_dir,
        archive_file,
        command,
    )

    summary = [
        f"yt-dlp: {yt_dlp_path}",
        f"playlist: {args.playlist_url}",
        f"download_dir: {download_dir}",
        f"archive_file: {archive_file}",
        f"log_file: {log_file}",
        f"command: {shlex.join(command)}",
    ]
    print("\n".join(summary))
    if args.dry_run:
        sys.exit(0)

    return_code = stream_command(command, log_file)
    sys.exit(return_code)
