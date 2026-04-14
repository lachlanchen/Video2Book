#!/usr/bin/env python3
"""Generate a book cover image with GRS AI Nano Banana 2."""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


DEFAULT_HOST = "https://grsaiapi.com"
DEFAULT_MODEL = "nano-banana-2"
DEFAULT_ASPECT_RATIO = "2:3"
DEFAULT_IMAGE_SIZE = "2K"
DEFAULT_TONE = "clean, modern, editorial nonfiction"
DEFAULT_AVOID = (
    "watermarks, mockup scenes, clutter, stock-photo cliches, distorted typography, "
    "unreadable tiny text"
)
REPO_ROOT = Path(__file__).resolve().parents[1]
TRANSIENT_HTTP_CODES = {408, 425, 429, 500, 502, 503, 504}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a front-cover image via the GRS AI Nano Banana draw API and "
            "save the prompt, request metadata, polling results, and final image."
        )
    )
    prompt_group = parser.add_mutually_exclusive_group()
    prompt_group.add_argument("--prompt", help="Explicit prompt text.")
    prompt_group.add_argument(
        "--prompt-file",
        type=Path,
        help="Path to a UTF-8 text file containing the full prompt.",
    )
    parser.add_argument("--title", help="Book title used to build a prompt.")
    parser.add_argument("--subtitle", default="", help="Optional subtitle.")
    parser.add_argument("--author", default="", help="Optional author or curator line.")
    parser.add_argument(
        "--visual-direction",
        default="",
        help="Optional art-direction note, such as visual metaphor or composition.",
    )
    parser.add_argument(
        "--palette",
        default="",
        help="Optional palette note, such as 'cream, charcoal, muted teal'.",
    )
    parser.add_argument("--tone", default=DEFAULT_TONE, help="Overall tone for the cover.")
    parser.add_argument(
        "--avoid",
        default=DEFAULT_AVOID,
        help="Things the cover should avoid.",
    )
    parser.add_argument(
        "--reference-image",
        action="append",
        default=[],
        help="Reference image URL or local file path. May be passed multiple times.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        type=Path,
        help="Directory for prompt, payload, manifests, and downloaded image.",
    )
    parser.add_argument(
        "--output-stem",
        default="book_cover",
        help="Filename stem for downloaded result images.",
    )
    parser.add_argument("--host", default=DEFAULT_HOST, help="GRS AI API host.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Nano Banana model name.")
    parser.add_argument(
        "--aspect-ratio",
        default=DEFAULT_ASPECT_RATIO,
        help="Aspect ratio sent to the draw API.",
    )
    parser.add_argument(
        "--image-size",
        default=DEFAULT_IMAGE_SIZE,
        help="Image size sent to the draw API.",
    )
    parser.add_argument(
        "--webhook",
        default="-1",
        help="Webhook value sent to the draw API. Use -1 for task polling.",
    )
    parser.add_argument(
        "--shut-progress",
        action="store_true",
        help="Set shutProgress=true in the request payload.",
    )
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=5.0,
        help="Polling interval in seconds.",
    )
    parser.add_argument(
        "--poll-timeout",
        type=float,
        default=900.0,
        help="Polling timeout in seconds.",
    )
    parser.add_argument(
        "--request-timeout",
        type=float,
        default=300.0,
        help="HTTP request timeout in seconds.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Reuse an existing task_manifest.json in the output directory when possible.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write the prompt and redacted payload without calling the API.",
    )
    return parser.parse_args()


def load_grsai_key() -> str:
    api_key = os.environ.get("GRSAI", "").strip()
    if api_key:
        return api_key

    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        for raw_line in env_path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[len("export ") :]
            if line.startswith("GRSAI="):
                value = line.split("=", 1)[1].strip().strip("'").strip('"')
                if value:
                    return value

    raise RuntimeError("Missing GRSAI env var and no GRSAI entry found in .env")


def build_prompt(args: argparse.Namespace) -> str:
    if args.prompt:
        prompt = args.prompt.strip()
        if not prompt:
            raise SystemExit("--prompt must not be empty")
        return prompt
    if args.prompt_file:
        prompt = args.prompt_file.expanduser().read_text(encoding="utf-8").strip()
        if not prompt:
            raise SystemExit(f"Prompt file is empty: {args.prompt_file}")
        return prompt
    if not args.title:
        raise SystemExit("Pass --title, --prompt, or --prompt-file.")

    pieces = [
        f'Design a polished front-cover image for a book titled "{args.title}".',
        "This should look like a real bookstore-ready cover, not a poster or social graphic.",
        f"Portrait composition with aspect ratio {args.aspect_ratio}.",
        f"Overall tone: {args.tone}.",
        "Reserve strong, readable space for the title and author typography.",
        (
            "If exact typography becomes unstable, prefer a clean typographic zone over "
            "garbled fake text."
        ),
    ]
    if args.subtitle:
        pieces.append(
            f'Include the subtitle "{args.subtitle}" if the typography stays clean and legible.'
        )
    if args.author:
        pieces.append(
            f'Include the author or curator line "{args.author}" if the typography stays clean and legible.'
        )
    if args.visual_direction:
        pieces.append(f"Visual direction: {args.visual_direction}.")
    if args.palette:
        pieces.append(f"Color palette: {args.palette}.")
    if args.avoid:
        pieces.append(f"Avoid {args.avoid}.")
    pieces.append("Front cover only. No spine. No back cover. No watermark.")
    return " ".join(piece.strip() for piece in pieces if piece.strip())


def data_uri_from_file(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def resolve_reference_images(items: list[str]) -> tuple[list[str], list[str]]:
    urls: list[str] = []
    redacted: list[str] = []
    for item in items:
        if item.startswith(("http://", "https://", "data:")):
            urls.append(item)
            if item.startswith("data:"):
                redacted.append(f"<data-uri length={len(item)}>")
            else:
                redacted.append(item)
            continue
        path = Path(item).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"Reference image not found: {path}")
        data_uri = data_uri_from_file(path)
        urls.append(data_uri)
        redacted.append(f"<{path.name} data-uri length={len(data_uri)}>")
    return urls, redacted


def request_raw(
    url: str,
    payload: dict[str, Any],
    api_key: str,
    *,
    timeout_s: float,
    retries: int,
    context: str,
) -> str:
    body = json.dumps(payload).encode("utf-8")
    last_error: BaseException | None = None
    for attempt in range(retries + 1):
        try:
            request = urllib.request.Request(url, data=body, method="POST")
            request.add_header("Content-Type", "application/json")
            request.add_header("Authorization", f"Bearer {api_key}")
            with urllib.request.urlopen(request, timeout=timeout_s) as response:
                return response.read().decode("utf-8", errors="ignore")
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code not in TRANSIENT_HTTP_CODES or attempt >= retries:
                raise
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            last_error = exc
            if attempt >= retries:
                raise
        time.sleep(2.0 + attempt * 2.0)
    raise RuntimeError(f"{context} failed after retries: {last_error}")


def parse_json(raw: str) -> dict[str, Any]:
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass

    last_obj: dict[str, Any] | None = None
    for line in raw.splitlines():
        chunk = line.strip()
        if not chunk:
            continue
        if chunk.startswith("data:"):
            chunk = chunk[5:].strip()
        try:
            parsed = json.loads(chunk)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            last_obj = parsed
    if last_obj is None:
        raise RuntimeError("Failed to parse API response as JSON")
    return last_obj


def poll_result(
    *,
    host: str,
    task_id: str,
    api_key: str,
    interval_s: float,
    timeout_s: float,
    request_timeout_s: float,
) -> dict[str, Any]:
    poll_url = host.rstrip("/") + "/v1/draw/result"
    started = time.time()
    while True:
        raw = request_raw(
            poll_url,
            {"id": task_id},
            api_key,
            timeout_s=request_timeout_s,
            retries=4,
            context="poll",
        )
        result = parse_json(raw)
        data = result.get("data") or {}
        status = result.get("status") or data.get("status")
        progress = result.get("progress")
        if progress is None:
            progress = data.get("progress")
        print(f"poll status={status!r} progress={progress!r} id={task_id}", flush=True)
        if status in {"succeeded", "failed"}:
            return result
        if time.time() - started > timeout_s:
            raise RuntimeError(f"Polling timed out after {timeout_s}s for task {task_id}")
        time.sleep(interval_s)


def save_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def download_file(url: str, destination: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": "Video2Book/1.0"})
    with urllib.request.urlopen(request, timeout=240) as response:
        destination.write_bytes(response.read())


def download_results(result_payload: dict[str, Any], output_dir: Path, output_stem: str) -> list[Path]:
    data = result_payload.get("data") or result_payload
    results = data.get("results") or []
    downloaded: list[Path] = []
    for index, item in enumerate(results, start=1):
        url = item.get("url")
        if not url:
            continue
        parsed = urllib.parse.urlparse(url)
        suffix = Path(parsed.path).suffix or ".png"
        if len(results) == 1:
            filename = f"{output_stem}{suffix}"
        else:
            filename = f"{output_stem}_{index:02d}{suffix}"
        destination = output_dir / filename
        download_file(url, destination)
        downloaded.append(destination)
    if not downloaded:
        raise RuntimeError("No downloadable result URLs were returned by the API")
    return downloaded


def timestamp_now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    prompt = build_prompt(args)
    prompt_path = output_dir / "prompt.txt"
    prompt_path.write_text(prompt + "\n", encoding="utf-8")

    reference_urls, reference_urls_redacted = resolve_reference_images(args.reference_image)
    payload = {
        "model": args.model,
        "prompt": prompt,
        "urls": reference_urls,
        "aspectRatio": args.aspect_ratio,
        "imageSize": args.image_size,
        "webHook": args.webhook,
        "shutProgress": args.shut_progress,
    }
    redacted_payload = dict(payload)
    redacted_payload["urls"] = reference_urls_redacted
    save_json(output_dir / "request_payload.redacted.json", redacted_payload)

    manifest_path = output_dir / "task_manifest.json"
    manifest: dict[str, Any] = {
        "tool": "scripts/book_cover_nanobanana.py",
        "created_at": timestamp_now(),
        "output_dir": str(output_dir),
        "prompt_file": str(prompt_path),
        "request_payload_redacted": str(output_dir / "request_payload.redacted.json"),
        "host": args.host,
        "model": args.model,
        "aspect_ratio": args.aspect_ratio,
        "image_size": args.image_size,
        "reference_images": args.reference_image,
        "status": "prepared",
    }

    if args.dry_run:
        save_json(manifest_path, manifest)
        print(f"prompt_file={prompt_path}")
        print(f"payload_file={output_dir / 'request_payload.redacted.json'}")
        print(json.dumps(redacted_payload, ensure_ascii=False, indent=2))
        return 0

    api_key = load_grsai_key()

    if args.resume and manifest_path.exists():
        prior_manifest = load_json(manifest_path)
        existing_files = [
            Path(path_str)
            for path_str in prior_manifest.get("downloaded_files", [])
            if Path(path_str).exists()
        ]
        if prior_manifest.get("status") == "succeeded" and existing_files:
            print("Existing successful cover run found; nothing to do.", flush=True)
            for path in existing_files:
                print(path)
            return 0
        if prior_manifest.get("task_id"):
            manifest.update(prior_manifest)
            print(f"Resuming task {prior_manifest['task_id']}", flush=True)

    task_id = manifest.get("task_id")
    if not task_id:
        submit_url = args.host.rstrip("/") + "/v1/draw/nano-banana"
        raw_submit = request_raw(
            submit_url,
            payload,
            api_key,
            timeout_s=args.request_timeout,
            retries=2,
            context="submit",
        )
        submit_payload = parse_json(raw_submit)
        save_json(output_dir / "submit_response.json", submit_payload)

        code = submit_payload.get("code")
        if code not in (0, "0", None):
            raise RuntimeError(
                "Submit returned non-success code: "
                + json.dumps(submit_payload, ensure_ascii=False, indent=2)
            )
        task_id = ((submit_payload.get("data") or {}).get("id")) or submit_payload.get("id")
        if not task_id:
            raise RuntimeError(
                "No task ID found in submit response: "
                + json.dumps(submit_payload, ensure_ascii=False, indent=2)
            )
        manifest["task_id"] = str(task_id)
        manifest["status"] = "submitted"
        manifest["submitted_at"] = timestamp_now()
        save_json(manifest_path, manifest)
    else:
        task_id = str(task_id)

    result_payload = poll_result(
        host=args.host,
        task_id=task_id,
        api_key=api_key,
        interval_s=args.poll_interval,
        timeout_s=args.poll_timeout,
        request_timeout_s=args.request_timeout,
    )
    save_json(output_dir / "result_response.json", result_payload)

    data = result_payload.get("data") or {}
    status = result_payload.get("status") or data.get("status")
    if status != "succeeded":
        manifest["status"] = status or "failed"
        manifest["finished_at"] = timestamp_now()
        save_json(manifest_path, manifest)
        raise RuntimeError(json.dumps(result_payload, ensure_ascii=False, indent=2))

    downloaded_files = download_results(result_payload, output_dir, args.output_stem)
    result_urls = [
        item.get("url")
        for item in (data.get("results") or [])
        if isinstance(item, dict) and item.get("url")
    ]
    manifest["status"] = "succeeded"
    manifest["finished_at"] = timestamp_now()
    manifest["downloaded_files"] = [str(path) for path in downloaded_files]
    manifest["result_urls"] = result_urls
    save_json(manifest_path, manifest)

    print(f"task_id={task_id}")
    for path in downloaded_files:
        print(path)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("Interrupted.", file=sys.stderr)
        raise SystemExit(130)
