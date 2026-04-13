# playlist2videos

This module vendors the practical `yt-dlp` workflow used to build the Leonard Susskind lecture archive. It is intentionally separate from the Windows GUI app found elsewhere in `/home/lachlan/ProjectsLFS/YoutubeDownloader`.

## Defaults

- Playlist URL:
  - <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>
- Workspace:
  - `/home/lachlan/ProjectsLFS/YoutubeDownloader`
- Downloads:
  - `/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/<playlist_id>/`
- Logs:
  - `/home/lachlan/ProjectsLFS/YoutubeDownloader/logs/`

## Entry points

- Python:
  - [download_playlist.py](/home/lachlan/ProjectsLFS/Video2Book/playlist2videos/download_playlist.py)
- Shell:
  - [download_susskind_playlist.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/download_susskind_playlist.sh)

## Usage

```bash
./scripts/download_susskind_playlist.sh
./scripts/download_susskind_playlist.sh --dry-run
./scripts/download_susskind_playlist.sh --playlist-start 120 --playlist-end 130
./scripts/download_susskind_playlist.sh -- --write-info-json
```
