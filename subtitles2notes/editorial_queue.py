#!/usr/bin/env python3
"""Run source-aware editorial revision as a durable, manifest-driven queue."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

import editorial_revision as revision  # noqa: E402


COURSE_INPUT_RE = re.compile(r"\\input\{chapters/([^/]+)/content\.tex\}")
TERMINAL_STATES = {"complete", "complete_with_blocks"}
REASONING_LEVELS = {"low", "medium", "high", "xhigh", "ultra"}


def timestamp() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def canonical_json(value: object) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def atomic_write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(canonical_json(value), encoding="utf-8")
    temporary.replace(path)


def manifest_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


@dataclass(frozen=True)
class CourseSpec:
    course_rel: str
    expected_chapters: int
    references: tuple[Path, ...]
    publish: bool


@dataclass(frozen=True)
class QueueConfig:
    repo_root: Path
    manifest_path: Path
    output_root: Path
    markdown_root: Path
    video_root: Path
    state_root: Path
    model: str
    reasoning: str
    max_repair_passes: int
    courses: tuple[CourseSpec, ...]
    publish_script: Path | None


def resolve_manifest_path(repo_root: Path, raw: str) -> Path:
    expanded = raw.replace("${REPO_ROOT}", str(repo_root)).replace("{repo_root}", str(repo_root))
    path = Path(expanded).expanduser()
    return path.resolve() if path.is_absolute() else (repo_root / path).resolve()


def load_manifest(repo_root: Path, manifest_path: Path, state_root: Path | None = None) -> QueueConfig:
    raw = json.loads(manifest_path.read_text(encoding="utf-8"))
    if raw.get("schema_version") != 1:
        raise ValueError("editorial queue manifest schema_version must be 1")

    output_root = resolve_manifest_path(repo_root, raw.get("output_root", "generated_course_notes"))
    markdown_root = resolve_manifest_path(repo_root, raw.get("markdown_root", "markdown"))
    video_root = resolve_manifest_path(repo_root, raw.get("video_root", "susskind_lecture_videos"))
    runtime = state_root or resolve_manifest_path(
        repo_root, raw.get("state_root", ".editorial-revision-work/queue")
    )
    model = str(raw.get("model") or "gpt-5.6-sol")
    reasoning = str(raw.get("reasoning") or "ultra")
    if reasoning not in REASONING_LEVELS:
        raise ValueError(f"unsupported reasoning level: {reasoning}")
    max_repair_passes = int(raw.get("max_repair_passes", 2))
    if max_repair_passes < 0:
        raise ValueError("max_repair_passes must be non-negative")

    courses: list[CourseSpec] = []
    seen: set[str] = set()
    for item in raw.get("courses") or []:
        course_rel = str(item.get("course") or "").strip("/")
        if not course_rel or course_rel in seen:
            raise ValueError(f"missing or duplicate course: {course_rel!r}")
        seen.add(course_rel)
        references: list[Path] = []
        for reference in item.get("references") or []:
            if isinstance(reference, str):
                reference_path = reference
                optional = False
            else:
                reference_path = str(reference.get("path") or "")
                optional = bool(reference.get("optional", False))
            resolved = resolve_manifest_path(repo_root, reference_path)
            if not resolved.exists():
                if optional:
                    continue
                raise ValueError(f"reference does not exist for {course_rel}: {resolved}")
            if is_relative_to(resolved, output_root):
                raise ValueError(f"generated notes cannot be references: {resolved}")
            references.append(resolved)
        courses.append(
            CourseSpec(
                course_rel=course_rel,
                expected_chapters=int(item.get("expected_chapters") or 0),
                references=tuple(references),
                publish=bool(item.get("publish", True)),
            )
        )

    expected_courses = int(raw.get("expected_courses") or len(courses))
    if len(courses) != expected_courses:
        raise ValueError(f"expected {expected_courses} courses, found {len(courses)}")
    publish_raw = str(raw.get("publish_script") or "").strip()
    publish_script = resolve_manifest_path(repo_root, publish_raw) if publish_raw else None
    if publish_script is not None and not publish_script.exists():
        raise ValueError(f"publish script does not exist: {publish_script}")
    return QueueConfig(
        repo_root=repo_root,
        manifest_path=manifest_path,
        output_root=output_root,
        markdown_root=markdown_root,
        video_root=video_root,
        state_root=runtime,
        model=model,
        reasoning=reasoning,
        max_repair_passes=max_repair_passes,
        courses=tuple(courses),
        publish_script=publish_script,
    )


def ordered_chapters(course_root: Path) -> list[str]:
    course_tex = course_root / "course.tex"
    ordered = COURSE_INPUT_RE.findall(course_tex.read_text(encoding="utf-8", errors="replace"))
    available = {
        path.name
        for path in (course_root / "chapters").glob("lecture_*")
        if (path / "content.tex").exists()
    }
    result = [slug for slug in ordered if slug in available]
    result.extend(sorted(available.difference(result)))
    return result


def chapter_preflight(config: QueueConfig, spec: CourseSpec, slug: str) -> list[str]:
    problems: list[str] = []
    chapter_dir = config.output_root / spec.course_rel / "chapters" / slug
    metadata_path = chapter_dir / "metadata.json"
    if not metadata_path.exists():
        problems.append(f"missing metadata: {metadata_path}")
        return problems
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    transcript_rel = str(metadata.get("transcript_rel") or "")
    video_rel = str(metadata.get("video_rel") or "")
    if not transcript_rel or not (config.markdown_root / transcript_rel).exists():
        problems.append(f"missing transcript for {spec.course_rel}/{slug}: {transcript_rel}")
    if not video_rel or not (config.video_root / video_rel).exists():
        problems.append(f"missing video for {spec.course_rel}/{slug}: {video_rel}")
    return problems


def validate_inventory(config: QueueConfig) -> tuple[dict[str, list[str]], list[str]]:
    inventory: dict[str, list[str]] = {}
    problems: list[str] = []
    total = 0
    for spec in config.courses:
        course_root = config.output_root / spec.course_rel
        if not course_root.exists():
            problems.append(f"missing course: {spec.course_rel}")
            continue
        chapters = ordered_chapters(course_root)
        inventory[spec.course_rel] = chapters
        total += len(chapters)
        if spec.expected_chapters and len(chapters) != spec.expected_chapters:
            problems.append(
                f"{spec.course_rel}: expected {spec.expected_chapters} chapters, found {len(chapters)}"
            )
        for slug in chapters:
            problems.extend(chapter_preflight(config, spec, slug))
    raw = json.loads(config.manifest_path.read_text(encoding="utf-8"))
    expected_total = int(raw.get("expected_chapters") or total)
    if total != expected_total:
        problems.append(f"expected {expected_total} total chapters, found {total}")
    return inventory, problems


def initial_state(config: QueueConfig, inventory: dict[str, list[str]]) -> dict:
    return {
        "schema_version": 1,
        "manifest_sha256": manifest_hash(config.manifest_path),
        "status": "pending",
        "model": config.model,
        "reasoning": config.reasoning,
        "started_at": timestamp(),
        "updated_at": timestamp(),
        "heartbeat_at": timestamp(),
        "current": None,
        "courses": {
            course: {
                "status": "pending",
                "chapters": {
                    slug: {"status": "pending", "attempts": 0} for slug in chapters
                },
            }
            for course, chapters in inventory.items()
        },
    }


def load_state(config: QueueConfig, inventory: dict[str, list[str]], force_manifest: bool) -> dict:
    path = config.state_root / "state.json"
    if not path.exists():
        return initial_state(config, inventory)
    state = json.loads(path.read_text(encoding="utf-8"))
    current_hash = manifest_hash(config.manifest_path)
    if state.get("manifest_sha256") != current_hash:
        if not force_manifest:
            raise RuntimeError("queue manifest changed; rerun with --force-manifest after review")
        fresh = initial_state(config, inventory)
        for course, course_state in fresh["courses"].items():
            previous = (state.get("courses") or {}).get(course, {})
            for slug, chapter_state in course_state["chapters"].items():
                old = (previous.get("chapters") or {}).get(slug)
                if old and old.get("status") in {"complete", "blocked"}:
                    chapter_state.update(old)
        return fresh
    return state


def checkpoint(config: QueueConfig, state: dict, stage: str, current: str | None = None) -> None:
    state["updated_at"] = timestamp()
    state["heartbeat_at"] = timestamp()
    state["stage"] = stage
    state["current"] = current
    atomic_write_json(config.state_root / "state.json", state)
    (config.state_root / "heartbeat").write_text(
        f"{state['heartbeat_at']} {stage} {current or ''}\n", encoding="utf-8"
    )


def run_logged(command: list[str], cwd: Path, log_path: Path, env: dict[str, str] | None = None) -> int:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"\n[{timestamp()}] $ {' '.join(command)}\n")
        handle.flush()
        completed = subprocess.run(
            command,
            cwd=cwd,
            env=env,
            text=True,
            stdout=handle,
            stderr=subprocess.STDOUT,
            check=False,
        )
        handle.write(f"[{timestamp()}] exit={completed.returncode}\n")
        return completed.returncode


def validate_chapter(config: QueueConfig, spec: CourseSpec, slug: str) -> list[str]:
    chapter_dir = config.output_root / spec.course_rel / "chapters" / slug
    required = (
        chapter_dir / "content.tex",
        chapter_dir / "lecture.pdf",
        chapter_dir / "editorial_audit.json",
        chapter_dir / "editorial_fidelity.json",
        chapter_dir / "source_map.json",
    )
    problems = [f"missing {path.name}" for path in required if not path.exists()]
    if problems:
        return problems
    content = chapter_dir / "content.tex"
    scan_ok, findings = revision.hard_scan_passes(content)
    if not scan_ok:
        problems.extend(f"hard scan: {item['rule']} line {item['line']}" for item in findings)
    fidelity = json.loads((chapter_dir / "editorial_fidelity.json").read_text(encoding="utf-8"))
    fidelity_ok, fidelity_problems = revision.fidelity_passes(content, fidelity)
    if not fidelity_ok:
        problems.extend(fidelity_problems)
    source_map = json.loads((chapter_dir / "source_map.json").read_text(encoding="utf-8"))
    if not source_map.get("entries"):
        problems.append("source map has no entries")
    return problems


def revision_command(
    config: QueueConfig,
    spec: CourseSpec,
    slug: str,
    force: bool,
    repair_passes: int,
) -> list[str]:
    command = [
        sys.executable,
        str(MODULE_ROOT / "subtitles2notes" / "editorial_revision.py"),
        "--repo-root",
        str(config.repo_root),
        "--output-root",
        str(config.output_root),
        "--course",
        spec.course_rel,
        "--chapter",
        slug,
        "--rewrite",
        "--resume",
        "--model",
        config.model,
        "--reasoning",
        config.reasoning,
        "--max-repair-passes",
        str(repair_passes),
    ]
    for reference in spec.references:
        command.extend(("--reference", str(reference)))
    if force:
        command.append("--force")
    return command


def commit_chapter(config: QueueConfig, spec: CourseSpec, slug: str, log_path: Path) -> None:
    base = config.output_root.relative_to(config.repo_root) / spec.course_rel
    command = [
        "bash",
        str(MODULE_ROOT / "scripts" / "codex_commit_push.sh"),
        str(config.repo_root),
        f"Polish {spec.course_rel} {slug}",
        str(base / "chapters" / slug),
        str(base / "common_preamble.tex"),
        str(base / "course.tex"),
        str(base / "course.pdf"),
    ]
    env = os.environ.copy()
    env.setdefault("CODEX_COMMIT_MODEL", "gpt-5.4-mini")
    env.setdefault("CODEX_COMMIT_REASONING", "low")
    if run_logged(command, config.repo_root, log_path, env) != 0:
        raise RuntimeError(f"commit/push failed for {spec.course_rel}/{slug}")


def process_chapter(
    config: QueueConfig,
    spec: CourseSpec,
    slug: str,
    state: dict,
    no_commit: bool,
    final_sweep: bool = False,
) -> bool:
    key = f"{spec.course_rel}/{slug}"
    chapter_state = state["courses"][spec.course_rel]["chapters"][slug]
    log_path = config.state_root / "logs" / spec.course_rel / f"{slug}.log"
    attempts = 1 if final_sweep else 2
    for local_attempt in range(attempts):
        chapter_state["status"] = "running"
        chapter_state["attempts"] = int(chapter_state.get("attempts") or 0) + 1
        checkpoint(config, state, "chapter_revision", key)
        force = final_sweep or local_attempt > 0
        repair_passes = config.max_repair_passes + (1 if force else 0)
        status = run_logged(
            revision_command(config, spec, slug, force, repair_passes),
            config.repo_root,
            log_path,
        )
        problems = validate_chapter(config, spec, slug) if status == 0 else [f"revision exit {status}"]
        if not problems:
            checkpoint(config, state, "chapter_commit", key)
            if not no_commit:
                commit_chapter(config, spec, slug, log_path)
            chapter_state.update(
                {"status": "complete", "completed_at": timestamp(), "problems": []}
            )
            checkpoint(config, state, "chapter_complete", key)
            return True
        chapter_state["problems"] = problems
        checkpoint(config, state, "chapter_retry", key)
        if local_attempt + 1 < attempts:
            time.sleep(15)
    chapter_state["status"] = "blocked"
    chapter_state["blocked_at"] = timestamp()
    checkpoint(config, state, "chapter_blocked", key)
    return False


def publish_course(config: QueueConfig, spec: CourseSpec, state: dict, no_publish: bool) -> bool:
    if no_publish or not spec.publish or config.publish_script is None:
        return True
    course_state = state["courses"][spec.course_rel]
    checkpoint(config, state, "course_publish", spec.course_rel)
    log_path = config.state_root / "logs" / spec.course_rel / "publish.log"
    env = os.environ.copy()
    env["VIDEO2BOOK_ROOT"] = str(MODULE_ROOT)
    env["NOTE_MODEL"] = config.model
    env["NOTE_REASONING"] = config.reasoning
    command = [
        "bash",
        str(config.publish_script),
        "--repo-root",
        str(config.repo_root),
        "--course",
        spec.course_rel,
    ]
    status = run_logged(command, config.repo_root, log_path, env)
    if status != 0:
        course_state["publish_error"] = f"publish exit {status}"
        checkpoint(config, state, "course_publish_failed", spec.course_rel)
        return False
    course_state["published_at"] = timestamp()
    checkpoint(config, state, "course_published", spec.course_rel)
    return True


def run_queue(config: QueueConfig, args: argparse.Namespace) -> int:
    inventory, problems = validate_inventory(config)
    if problems:
        raise RuntimeError("queue preflight failed:\n- " + "\n- ".join(problems))
    if args.dry_run:
        for spec in config.courses:
            print(f"{len(inventory[spec.course_rel]):3} {spec.course_rel}")
        print(f"TOTAL {len(config.courses)} courses {sum(map(len, inventory.values()))} chapters")
        return 0

    config.state_root.mkdir(parents=True, exist_ok=True)
    lock_path = config.state_root / "queue.lock"
    with lock_path.open("w", encoding="utf-8") as lock_handle:
        try:
            fcntl.flock(lock_handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeError("another editorial queue worker already holds the lock") from error
        lock_handle.write(f"pid={os.getpid()} started={timestamp()}\n")
        lock_handle.flush()

        state = load_state(config, inventory, args.force_manifest)
        state["status"] = "running"
        state["model"] = config.model
        state["reasoning"] = config.reasoning
        checkpoint(config, state, "queue_start")

        for spec in config.courses:
            course_state = state["courses"][spec.course_rel]
            course_state["status"] = "running"
            checkpoint(config, state, "course_start", spec.course_rel)
            for slug in inventory[spec.course_rel]:
                chapter_state = course_state["chapters"][slug]
                if chapter_state.get("status") == "complete":
                    continue
                process_chapter(config, spec, slug, state, args.no_commit)

            blocked = [
                slug
                for slug, chapter_state in course_state["chapters"].items()
                if chapter_state.get("status") == "blocked"
            ]
            for slug in blocked:
                process_chapter(config, spec, slug, state, args.no_commit, final_sweep=True)

            incomplete = [
                slug
                for slug, chapter_state in course_state["chapters"].items()
                if chapter_state.get("status") != "complete"
            ]
            if incomplete:
                course_state["status"] = "blocked"
                course_state["blocked_chapters"] = incomplete
                checkpoint(config, state, "course_blocked", spec.course_rel)
                continue
            if not publish_course(config, spec, state, args.no_publish):
                course_state["status"] = "publish_failed"
                continue
            course_state["status"] = "complete"
            course_state["completed_at"] = timestamp()
            checkpoint(config, state, "course_complete", spec.course_rel)

        blocked_courses = [
            course
            for course, course_state in state["courses"].items()
            if course_state.get("status") != "complete"
        ]
        state["blocked_courses"] = blocked_courses
        state["status"] = "complete_with_blocks" if blocked_courses else "complete"
        state["completed_at"] = timestamp()
        checkpoint(config, state, state["status"])
        return 0 if not blocked_courses else 2


def parser() -> argparse.ArgumentParser:
    parsed = argparse.ArgumentParser(description=__doc__)
    parsed.add_argument("--repo-root", type=Path, default=Path.cwd())
    parsed.add_argument("--manifest", type=Path, required=True)
    parsed.add_argument("--state-root", type=Path)
    parsed.add_argument("--model")
    parsed.add_argument("--reasoning", choices=sorted(REASONING_LEVELS))
    parsed.add_argument("--dry-run", action="store_true")
    parsed.add_argument("--force-manifest", action="store_true")
    parsed.add_argument("--no-commit", action="store_true")
    parsed.add_argument("--no-publish", action="store_true")
    return parsed


def main() -> int:
    args = parser().parse_args()
    repo_root = args.repo_root.expanduser().resolve()
    manifest_path = args.manifest.expanduser()
    if not manifest_path.is_absolute():
        manifest_path = (repo_root / manifest_path).resolve()
    state_root = args.state_root.expanduser().resolve() if args.state_root else None
    config = load_manifest(repo_root, manifest_path, state_root)
    if args.model or args.reasoning:
        config = QueueConfig(
            **{
                **config.__dict__,
                "model": args.model or config.model,
                "reasoning": args.reasoning or config.reasoning,
            }
        )
    return run_queue(config, args)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(f"editorial queue error: {error}", file=sys.stderr)
        sys.exit(1)
