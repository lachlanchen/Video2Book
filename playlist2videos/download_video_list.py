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


DEFAULT_WORKSPACE = Path("/home/lachlan/ProjectsLFS/YoutubeDownloader")
DEFAULT_FORMAT = "bv*+ba/b"
DEFAULT_OUTPUT_TEMPLATE = "{index:0{digits}d} - %(title)s [%(id)s].%(ext)s"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Download an ordered list of YouTube videos with yt-dlp using a stable "
            "archive layout and log files."
        )
    )
    parser.add_argument(
        "--urls-file",
        required=True,
        type=Path,
        help="Text file containing one video URL per line.",
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
        help="Optional relative subdirectory under the downloads root. Defaults to the URL file stem.",
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
        help="Override the download archive file. Defaults to <log-root>/<urls-file-stem>.archive.",
    )
    parser.add_argument(
        "--start-index",
        type=int,
        default=1,
        help="Index used for the first URL in the list. Defaults to %(default)s.",
    )
    parser.add_argument(
        "--digits",
        type=int,
        help="Zero-padding width for the numeric filename prefix. Defaults to the list length.",
    )
    parser.add_argument(
        "--output-template",
        default=DEFAULT_OUTPUT_TEMPLATE,
        help=(
            "Filename template inside the download directory. Available fields are "
            "{index} and {digits}; yt-dlp placeholders may also be used."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the resolved commands and paths without downloading.",
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


def load_urls(urls_file: Path) -> list[str]:
    urls: list[str] = []
    for raw_line in urls_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        urls.append(line)
    if not urls:
        raise SystemExit(f"No URLs found in {urls_file}")
    return urls


def resolve_paths(args: argparse.Namespace) -> tuple[Path, Path, Path]:
    download_root = (args.download_root or (args.workspace / "downloads")).expanduser()
    log_root = (args.log_root or (args.workspace / "logs")).expanduser()
    download_subdir = Path(args.download_subdir) if args.download_subdir else Path(args.urls_file.stem)
    download_dir = download_root / download_subdir
    archive_file = args.archive_file or (log_root / f"{args.urls_file.stem}.archive")
    return download_dir, log_root, archive_file.expanduser()


def output_template_for(index: int, digits: int, template: str) -> str:
    return template.format(index=index, digits=digits)


def build_command(
    yt_dlp_path: Path,
    args: argparse.Namespace,
    url: str,
    download_dir: Path,
    archive_file: Path,
    output_template: str,
) -> list[str]:
    command = [
        str(yt_dlp_path),
        url,
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
        str(download_dir / output_template),
    ]
    node_path = shutil.which("node")
    if node_path:
        command.extend(["--js-runtimes", f"node:{node_path}"])
    command.extend(args.yt_dlp_args)
    return command


def write_log_header(
    log_file: Path,
    urls_file: Path,
    urls: Sequence[str],
    download_dir: Path,
    archive_file: Path,
    digits: int,
) -> None:
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    header = [
        f"# Timestamp: {timestamp}",
        f"# URL file: {urls_file}",
        f"# Download directory: {download_dir}",
        f"# Archive file: {archive_file}",
        f"# Digits: {digits}",
        "# URLs:",
        *[f"#   {index + 1:0{digits}d}: {url}" for index, url in enumerate(urls)],
        "",
    ]
    log_file.write_text("\n".join(header), encoding="utf-8")


def append_log_command(log_file: Path, command: Sequence[str], index: int, url: str) -> None:
    with log_file.open("a", encoding="utf-8") as handle:
        handle.write(f"# ---- video {index} ----\n")
        handle.write(f"# URL: {url}\n")
        handle.write(f"# Command: {shlex.join(command)}\n\n")


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


def main() -> int:
    args = parse_args()
    workspace = args.workspace.expanduser()
    urls_file = args.urls_file.expanduser().resolve()
    urls = load_urls(urls_file)
    digits = args.digits or max(2, len(str(args.start_index + len(urls) - 1)))
    download_dir, log_root, archive_file = resolve_paths(args)
    yt_dlp_path = resolve_ytdlp(args.yt_dlp, workspace)

    log_root.mkdir(parents=True, exist_ok=True)
    download_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_root / f"ytvideos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    write_log_header(log_file, urls_file, urls, download_dir, archive_file, digits)

    print(f"yt-dlp: {yt_dlp_path}")
    print(f"urls_file: {urls_file}")
    print(f"download_dir: {download_dir}")
    print(f"archive_file: {archive_file}")
    print(f"log_file: {log_file}")
    print(f"videos: {len(urls)}")

    return_code = 0
    for offset, url in enumerate(urls):
        index = args.start_index + offset
        output_template = output_template_for(index, digits, args.output_template)
        command = build_command(
            yt_dlp_path=yt_dlp_path,
            args=args,
            url=url,
            download_dir=download_dir,
            archive_file=archive_file,
            output_template=output_template,
        )
        print(f"\n[{index:0{digits}d}/{args.start_index + len(urls) - 1:0{digits}d}] {url}")
        print(f"command: {shlex.join(command)}")
        append_log_command(log_file, command, index, url)
        if args.dry_run:
            continue
        current_return_code = stream_command(command, log_file)
        if current_return_code != 0:
            return_code = current_return_code

    return return_code


if __name__ == "__main__":
    sys.exit(main())
