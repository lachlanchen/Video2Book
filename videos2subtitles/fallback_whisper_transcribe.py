#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import torch
import whisper
from whisper.utils import format_timestamp


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Fallback direct Whisper transcription for a single file."
    )
    parser.add_argument("--input", required=True, help="Input audio or video path.")
    parser.add_argument("--json-output", required=True, help="Output JSON path.")
    parser.add_argument("--srt-output", required=True, help="Output SRT path.")
    parser.add_argument("--model", default="large-v3", help="Whisper model name.")
    parser.add_argument("--language", default="en", help="Whisper language code.")
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress Whisper segment progress output.",
    )
    return parser


def render_timestamp(seconds: float) -> str:
    return format_timestamp(
        seconds,
        always_include_hours=True,
        decimal_marker=",",
    )


def render_srt(entries: list[dict]) -> str:
    blocks: list[str] = []
    for index, entry in enumerate(entries, start=1):
        text = " ".join(str(entry["text"]).split()).strip()
        if not text:
            continue
        blocks.append(
            f"{index}\n{entry['start']} --> {entry['end']}\n{text}\n"
        )
    return "\n".join(blocks)


def main() -> int:
    args = build_parser().parse_args()
    input_path = Path(args.input)
    json_output = Path(args.json_output)
    srt_output = Path(args.srt_output)

    print(f"Loading direct Whisper model: {args.model}", flush=True)
    model = whisper.load_model(args.model)
    print(f"Transcribing with direct Whisper: {input_path}", flush=True)
    result = model.transcribe(
        str(input_path),
        language=args.language,
        fp16=torch.cuda.is_available(),
        verbose=not args.quiet,
    )

    entries: list[dict] = []
    for segment in result.get("segments", []):
        text = " ".join(str(segment.get("text", "")).split()).strip()
        if not text:
            continue
        entries.append(
            {
                "start": render_timestamp(float(segment["start"])),
                "end": render_timestamp(float(segment["end"])),
                "text": text,
            }
        )

    json_output.parent.mkdir(parents=True, exist_ok=True)
    srt_output.parent.mkdir(parents=True, exist_ok=True)
    json_output.write_text(json.dumps(entries, indent=4, ensure_ascii=False), encoding="utf-8")
    srt_output.write_text(render_srt(entries), encoding="utf-8")
    print(f"Wrote fallback JSON to {json_output}", flush=True)
    print(f"Wrote fallback SRT to {srt_output}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
