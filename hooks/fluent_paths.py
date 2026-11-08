"""
Fluent path resolution for the Mistral Vibe project setup.

Data directory resolution precedence:
  1. $FLUENT_DATA_DIR if set (absolutized)
  2. ./data if ./data/learner-profile.json exists (running from the repo root)
  3. <repo-root>/data (Vibe sessions run with the repo root as cwd; also
     covers the first run before learner-profile.json exists, so progress
     lives in git and syncs across devices from day one)
  4. ~/.vibe/fluent-data (fallback when running outside the repo)

Pure resolvers (data_dir / repo_root / backups_dir) do not create directories.
Call ensure_data_dir() before writing.
"""
from __future__ import annotations

import os
import sys
from functools import lru_cache
from pathlib import Path


def force_utf8_io() -> None:
    """Make stdout/stderr UTF-8 so emoji/CJK output doesn't crash on Windows.

    Windows consoles default to a legacy code page (cp1252/gbk); printing the
    emoji in the hook summaries raises UnicodeEncodeError there. No-op on
    platforms whose streams are already UTF-8 or predate ``reconfigure``.
    Call once at the top of any hook that prints.
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


@lru_cache(maxsize=1)
def repo_root() -> Path:
    """Resolve the repository root directory (parent of hooks/)."""
    return Path(__file__).resolve().parents[1]


@lru_cache(maxsize=1)
def data_dir() -> Path:
    """Resolve the runtime data directory (pure — does not create it)."""
    env = os.environ.get("FLUENT_DATA_DIR")
    if env:
        return Path(env).expanduser().resolve()

    cwd_data = (Path.cwd() / "data").resolve()
    if (cwd_data / "learner-profile.json").exists():
        return cwd_data

    root = repo_root()
    if (root / "data").exists():
        root_data = (root / "data").resolve()
        try:
            cwd = Path.cwd().resolve()
        except OSError:
            cwd = None
        if cwd is None or cwd == root or root in cwd.parents:
            return root_data

    return (Path.home() / ".vibe" / "fluent-data").resolve()


def ensure_data_dir() -> Path:
    """Resolve the data directory and create it if missing. Call before writing."""
    d = data_dir()
    d.mkdir(parents=True, exist_ok=True)
    return d


@lru_cache(maxsize=1)
def backups_dir() -> Path:
    """Resolve the backups directory. Always nested inside data_dir to avoid
    collisions when the fallback ~/.vibe/fluent-data is used (the parent
    ~/.vibe/ is shared across projects)."""
    return data_dir() / ".backups"


def ensure_backups_dir() -> Path:
    """Resolve the backups directory and create it if missing."""
    b = backups_dir()
    b.mkdir(parents=True, exist_ok=True)
    return b
