# Changelog

All notable changes to Fluent will be documented in this file.

## [0.4.0] — 2026-11-08

### Changed — Mistral Vibe native

This fork now targets **Mistral Vibe** instead of Claude Code.

- Skills moved from `.claude/skills/` to `.vibe/skills/` (loaded by Vibe
  when the repo folder is trusted); skill frontmatter adapted
  (`allowed-tools` now lists Vibe tool names: `read_file`, `write_file`,
  `bash`, `ask_user_question`). `disable-model-invocation: true` gating
  is unchanged.
- Added `.vibe/hooks.toml` with a single `post_tool` hook
  (`hooks/validate-data.py`) that JSON-validates learner data writes and
  keeps timestamped backups. It now speaks the Vibe hook protocol
  (structured stdout; a `deny` decision replaces the tool output the model
  sees when JSON is invalid).
- README updated: git-commit sync of `data/` + `results/` at session end
  and `git pull` at session start, so progress continues on any device.
- `hooks/fluent_paths.py` simplified: data dir resolves `$FLUENT_DATA_DIR` →
  `./data/` (with profile) → `<repo>/data/` → `~/.vibe/fluent-data/`.
- Skill support files moved next to their skills
  (`payload.example.json`, `feedback-template.md`, `worked-examples.md`);
  `docs/session-file-template.md` moved to `docs/`.

### Removed

- Claude Code plugin machinery: `.claude-plugin/` (marketplace + plugin
  manifests), `.claude/settings.json`, `hooks/hooks.json`.
- `session-start.py`, `session-end.py`, and the PreCompact backup —
  Vibe's hook lifecycle has no session start/end/compaction events.
  Their responsibilities moved into the session skills (greeting/stats
  from `read-db.py`) and `update-db.py` (pre-write backups + git commit).
- `CLAUDE.md` renamed to `TUTOR.md` (same role definition; referenced
  from `AGENTS.md`, which Vibe auto-loads).

### Upgrade

If you previously used the Claude Code plugin install, remove it
(`claude plugin uninstall`) and switch to launching `vibe` inside your
clone of this repository. Existing `data/` continues to work as-is.

## [0.3.0] — 2026-06-15

### Added

- Milestones support in the `update-db.py` session payload. The new
  `milestones[]` field accepts either a bare string or an object
  `{ "milestone": <required non-empty string>, "date": <optional YYYY-MM-DD,
  defaults to the session date> }`. Each milestone is recorded in both
  `session-log.milestones[]` and `learner-profile.achievements[]`. Validation
  rejects malformed entries (exit `1`, no files written); an unparseable
  `date` falls back to the session date.

## [0.2.1] — 2026-06-11

### Fixed

- Hooks no longer fail on Windows with `No such file or directory` (#5).
  Plugin hook commands in `hooks.json` used the bash default-value syntax
  `${CLAUDE_PLUGIN_ROOT:-${CLAUDE_PROJECT_DIR:-.}}`, which Claude Code's own
  variable substitution does not understand on Windows — it replaced the
  variable names but left the `:-` separators literal, producing a single
  garbage path. Hook commands now use plain `${CLAUDE_PLUGIN_ROOT}` (always
  set for plugin hooks) and invoke scripts via an explicit `python3`/`bash`
  interpreter so they don't depend on shebang handling under Git Bash.

## [0.2.0] — 2026-05-14

### Breaking changes

All 12 skills renamed with a `fluent-` prefix to prevent collisions with other
plugins and Claude Code built-ins. Update any muscle memory or external
references.

| Old | New |
|-----|-----|
| `/setup` | `/fluent-setup` |
| `/learn` | `/fluent-learn` |
| `/review` | `/fluent-review` |
| `/vocab` | `/fluent-vocab` |
| `/writing` | `/fluent-writing` |
| `/speaking` | `/fluent-speaking` |
| `/reading` | `/fluent-reading` |
| `/progress` | `/fluent-progress` |
| `sm2-calculator` | `fluent-sm2-calculator` |
| `db-updater` | `fluent-db-updater` |
| `feedback-formatter` | `fluent-feedback-formatter` |
| `session-analyzer` | `fluent-session-analyzer` |

New session result files use `/results/fluent-{skill}-session-{NNN}.md`.
Existing files using the older `{skill}-session-{NNN}.md` naming are still
read by `fluent-session-analyzer` — no migration required.

### Fixed

- Plugin install no longer fails on first DB read. Skills now invoke helper
  scripts via `${CLAUDE_PLUGIN_ROOT:-${CLAUDE_PROJECT_DIR:-.}}/.claude/hooks/...`
  so the path resolves regardless of CWD.
- Added missing `.claude/hooks/ensure_data_dir.py` referenced by
  `fluent-setup`.

### Migration

```bash
claude plugin update fluent@m98
```

Then use the new slash commands. Your data (`~/.claude/fluent-data/` or
`./data/`) is unchanged.

## [0.1.0] — 2026-03-15

Initial release.
