#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qs, urlparse


DEFAULT_WORKSPACE = Path("/home/lachlan/ProjectsLFS/YoutubeDownloader")
VIDEO_EXTENSIONS = {".mp4", ".mkv", ".webm", ".m4a", ".mp3"}
YT_DLP_FRAGMENT_STEM_RE = re.compile(r"\.f\d+$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Pre-seed a playlist download directory with symlinks to duplicate videos "
            "that already exist in earlier course folders, and mark those IDs in a "
            "download archive so yt-dlp skips re-downloading them."
        )
    )
    parser.add_argument("--playlist-url", required=True)
    parser.add_argument(
        "--workspace",
        type=Path,
        default=DEFAULT_WORKSPACE,
        help="External downloader workspace used to resolve yt-dlp.",
    )
    parser.add_argument(
        "--download-root",
        type=Path,
        required=True,
        help="Root download directory in the host repo.",
    )
    parser.add_argument(
        "--download-subdir",
        required=True,
        help="Relative playlist directory under the download root.",
    )
    parser.add_argument(
        "--source-subdir",
        action="append",
        default=[],
        help="Relative prior playlist directory under the same download root. Repeatable.",
    )
    parser.add_argument(
        "--archive-file",
        type=Path,
        required=True,
        help="Download archive file to append duplicate IDs into.",
    )
    parser.add_argument(
        "--yt-dlp",
        type=Path,
        help="Explicit path to the yt-dlp executable.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the symlink plan without modifying the filesystem.",
    )
    return parser.parse_args()


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
    which = subprocess.run(
        ["bash", "-lc", "command -v yt-dlp || true"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if which:
        candidates.append(Path(which))
    for candidate in candidates:
        if candidate and candidate.exists():
            return candidate
    raise SystemExit("Could not find yt-dlp. Install it or pass --yt-dlp /path/to/yt-dlp.")


def load_playlist_entries(yt_dlp_path: Path, playlist_url: str) -> list[dict]:
    command = [str(yt_dlp_path), "--flat-playlist", "--dump-single-json", playlist_url]
    completed = subprocess.run(command, check=True, capture_output=True, text=True)
    payload = json.loads(completed.stdout)
    entries = payload.get("entries") or []
    if not entries:
        raise SystemExit("No playlist entries returned by yt-dlp.")
    return entries


def sanitize_title(title: str) -> str:
    cleaned = title.replace("/", "∕").replace("\0", "")
    cleaned = "".join(ch if ord(ch) >= 32 else " " for ch in cleaned)
    return " ".join(cleaned.split())


def iter_source_candidates(root: Path) -> Iterable[Path]:
    if not root.exists():
        return []
    return sorted(root.iterdir())


def find_existing_video(source_root: Path, video_id: str) -> Path | None:
    marker = f"[{video_id}]"
    for path in iter_source_candidates(source_root):
        if not path.is_file():
            continue
        if path.name.endswith(".part"):
            continue
        if path.suffix.lower() not in VIDEO_EXTENSIONS:
            continue
        if YT_DLP_FRAGMENT_STEM_RE.search(path.stem):
            continue
        if marker not in path.name:
            continue
        return path
    return None


def ensure_archive_entries(archive_file: Path, ids: Iterable[str]) -> None:
    archive_file.parent.mkdir(parents=True, exist_ok=True)
    existing = set()
    if archive_file.exists():
        existing = {
            line.strip()
            for line in archive_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        }
    new_lines = []
    for video_id in ids:
        line = f"youtube {video_id}"
        if line not in existing:
            new_lines.append(line)
            existing.add(line)
    if new_lines:
        with archive_file.open("a", encoding="utf-8") as handle:
            for line in new_lines:
                handle.write(f"{line}\n")


def main() -> int:
    args = parse_args()
    workspace = args.workspace.expanduser()
    yt_dlp_path = resolve_ytdlp(args.yt_dlp, workspace)
    playlist_id = extract_playlist_id(args.playlist_url)
    download_root = args.download_root.expanduser()
    download_dir = download_root / args.download_subdir
    source_roots = [download_root / subdir for subdir in args.source_subdir]

    entries = load_playlist_entries(yt_dlp_path, args.playlist_url)
    print(f"Playlist ID: {playlist_id}")
    print(f"Target directory: {download_dir}")
    print(f"Source directories: {', '.join(str(p) for p in source_roots) if source_roots else '(none)'}")

    linked_ids: list[str] = []
    linked_count = 0
    skipped_existing = 0

    if not args.dry_run:
        download_dir.mkdir(parents=True, exist_ok=True)

    for offset, entry in enumerate(entries, start=1):
        video_id = str(entry.get("id", "")).strip()
        if not video_id:
            continue
        title = sanitize_title(str(entry.get("title") or f"video-{video_id}"))
        playlist_index = int(entry.get("playlist_index") or offset)

        source_match: Path | None = None
        for source_root in source_roots:
            source_match = find_existing_video(source_root, video_id)
            if source_match is not None:
                break
        if source_match is None:
            continue

        target_name = f"{playlist_index:03d} - {title} [{video_id}]{source_match.suffix}"
        target_path = download_dir / target_name

        if target_path.exists() or target_path.is_symlink():
            skipped_existing += 1
            linked_ids.append(video_id)
            continue

        relative_source = Path(os.path.relpath(source_match, start=download_dir))

        print(f"Linking {target_path.name} -> {relative_source}")
        if not args.dry_run:
            target_path.symlink_to(relative_source)
        linked_ids.append(video_id)
        linked_count += 1

    if not args.dry_run:
        ensure_archive_entries(args.archive_file.expanduser(), linked_ids)

    print(f"Created symlinks: {linked_count}")
    print(f"Already present: {skipped_existing}")
    print(f"Marked duplicate IDs in archive: {len(linked_ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
