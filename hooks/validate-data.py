#!/usr/bin/env python3
"""
Fluent Data Validation Hook (Mistral Vibe `post_tool` hook)

Runs after every write_file / edit. If the written file is a learner database
inside the resolved data dir, it validates the JSON, keeps a timestamped
backup (last 10), and reports back via the Vibe hook protocol:

- valid JSON   -> exit 0, structured response with a `system_message` note
- invalid JSON -> exit 0, structured response with a `deny` decision; the
  tool output the model sees is replaced with the validation error so the
  tutor immediately fixes the file.

Vibe parses stdout as JSON; stderr is reserved for diagnostics. Exit codes
are only used for hard failures (Vibe fails the hook open on non-zero exit).
"""
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fluent_paths import data_dir, force_utf8_io  # noqa: E402

force_utf8_io()
MAX_BACKUPS_PER_FILE = 10


def rotate_backups(file_path: str, keep: int = MAX_BACKUPS_PER_FILE) -> None:
    """Keep only the most recent `keep` .backup-* files for a given data file."""
    parent = Path(file_path).parent
    stem = Path(file_path).name
    backups = sorted(parent.glob(f"{stem}.backup-*"), reverse=True)
    for old in backups[keep:]:
        try:
            old.unlink()
        except OSError:
            pass


def respond(payload: dict) -> None:
    """Emit a structured hook response on stdout and exit 0."""
    print(json.dumps(payload, ensure_ascii=False))
    sys.exit(0)


def main():
    try:
        hook_input = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid hook input: {e}", file=sys.stderr)
        sys.exit(1)

    tool_input = hook_input.get("tool_input", {})
    if not isinstance(tool_input, dict):
        sys.exit(1)
    # write_file uses `path`, edit uses `file_path`
    file_path = (
        tool_input.get("file_path")
        or tool_input.get("path")
        or tool_input.get("file_name")
        or ""
    )

    if not file_path or not file_path.endswith(".json"):
        sys.exit(0)

    # Only validate files inside the resolved data dir
    data = data_dir().resolve()
    try:
        resolved = Path(file_path).resolve()
        resolved.relative_to(data)
    except (ValueError, OSError):
        sys.exit(0)

    if not os.path.exists(file_path):
        sys.exit(0)

    try:
        with open(file_path, 'r') as f:
            json.load(f)
    except json.JSONDecodeError as e:
        respond({
            "decision": "deny",
            "reason": (
                f"[Fluent] ⚠️ Invalid JSON in {file_path}: {e} — "
                "fix the JSON; a timestamped backup may exist next to the file."
            ),
        })

    try:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_path = f"{file_path}.backup-{timestamp}"
        shutil.copy2(file_path, backup_path)
        rotate_backups(file_path)
    except Exception as e:  # backup failure is not worth failing the write
        print(f"[Fluent] Backup failed: {e}", file=sys.stderr)
        respond({"system_message": f"[Fluent] ✓ Data saved and validated: {file_path}"})

    respond({
        "system_message": (
            f"[Fluent] ✓ Data saved and validated: {file_path} · "
            f"💾 Backup: {Path(backup_path).name}"
        )
    })


if __name__ == "__main__":
    main()
