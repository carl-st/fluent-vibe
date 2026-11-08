# Fluent Hooks and Helper Scripts

This directory contains the Python helper scripts and the one project hook that manage data integrity and backups for the Fluent language learning system running in Mistral Vibe.

## 📋 Contents

| File | Role |
|------|------|
| `validate-data.py` | Vibe `post_tool` hook — validates learner JSON and keeps timestamped backups after every write |
| `fluent_paths.py` | Shared data-directory resolution (`data_dir()`, `ensure_data_dir()`, backups dir, UTF-8 I/O helper) |
| `read-db.py` | Loads all 6 databases plus computed fields in one call (called at session start by every skill) |
| `update-db.py` | Atomically updates all 6 databases from one JSON session report on stdin (called at session end; takes a pre-write backup of every file) |
| `ensure_data_dir.py` | Tiny wrapper that prints the resolved data directory, creating it if missing |

## 🪝 Hook: `validate-data.py`

Registered in [`.vibe/hooks.toml`](../.vibe/hooks.toml):

```toml
[[hooks]]
name = "fluent-validate-data"
type = "post_tool"
match = "re:write_file|edit"
command = "python3 hooks/validate-data.py"
timeout = 10.0
```

It fires on every `write_file` / `edit` tool call. If the touched file is a `.json` inside the resolved data directory, the hook:

1. Validates the JSON structure
2. Creates a timestamped backup: `data/file.json.backup-YYYYMMDD-HHMMSS` (last 10 kept per file)
3. Reports back through the Vibe hook protocol:
   - **Valid JSON** — structured response with a `system_message` note
   - **Invalid JSON** — `decision: "deny"`; the tool output the model sees is replaced with the validation error, so the tutor fixes the file immediately

Vibe runs hooks with the session directory as cwd, so the `hooks/`… path resolves from the repo root. The folder must be trusted for `.vibe/hooks.toml` to load — check the startup warnings box if the hook seems inactive, and use `/reload` after editing it.

### Test the hook manually

```bash
echo '{"hook_event_name":"post_tool","tool_name":"file_system.write_file","tool_input":{"path":"data/learner-profile.json"}}' | python3 hooks/validate-data.py
```

## 🔄 What replaced the old session hooks

Earlier versions had SessionStart / SessionEnd / PreCompact hooks (Claude Code). Mistral Vibe's hook lifecycle only has `pre_tool`, `post_tool`, and `post_agent`, so that work moved into the skills:

| Old hook | Now handled by |
|----------|----------------|
| SessionStart welcome + stats | Every session skill greets the learner (name, streak, due reviews) from `read-db.py` output |
| SessionEnd daily snapshot | `update-db.py` backs up all 6 databases before writing, and the `fluent-db-updater` skill commits + pushes the session's progress |
| PreCompact safety backup | `update-db.py` pre-write backups (plus git history — every session is a commit) |

## 📂 Backup Strategy

1. **Per-write backups** — `data/*.json.backup-YYYYMMDD-HHMMSS` (validate-data hook; last 10 kept)
2. **Pre-update snapshots** — `<data_dir>/.backups/pre-update-<session_id>/` before every `update-db.py` run
3. **Git history** — every session ends with a commit of `data/` and `results/`, so any clone is a full backup

All backup locations are excluded from git via `.gitignore`.

## 🔍 Troubleshooting

- **Hook not running** — the folder must be trusted (Vibe prompts on first launch); check the warnings box at startup; test manually as shown above.
- **Invalid JSON flagged** — check `ls -t data/*.backup-* | head -1`, then restore: `cp data/file.json.backup-XXXXXX data/file.json`
- **Data in the wrong place** — see the resolution order in the [main README](../README.md); force a location with `FLUENT_DATA_DIR`.

## 📚 Additional Resources

- [Mistral Vibe hooks documentation](https://docs.mistral.ai/vibe/code/overview)
- [Fluent Main README](../README.md)
- [Learning System Guide](../LEARNING_SYSTEM.md)
