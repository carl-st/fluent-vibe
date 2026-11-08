# Data Directory

This directory contains your personal learning data in JSON format.

## 🚀 Getting Started

**This directory is empty by design!**

When you run `/fluent-setup` for the first time, the system will automatically create:

- `learner-profile.json` - Your name, target language, level, goals
- `progress-db.json` - Overall statistics and trends
- `mistakes-db.json` - Error patterns you're working on
- `mastery-db.json` - Skill mastery levels (0-5 stars)
- `spaced-repetition.json` - Review schedule (SM-2 algorithm)
- `session-log.json` - Complete session history

## 🔄 Cross-Device Sync

**Progress in this directory is committed to git on purpose.**

- ✅ Every session ends with a commit of `data/` and `results/` (see the `fluent-db-updater` skill)
- ✅ The next session on any device starts with `git pull --rebase --autostash` — so you can continue learning wherever you cloned this repo
- ✅ Commit history doubles as a long-term progress log

## 🔒 Privacy

⚠️ **Your learning data is committed to your git repository and pushed to its remote.**

- ✅ Human-readable JSON - Easy to export/analyze
- ✅ Automatically backed up - See `.backups/` directory (kept out of git)
- ⚠️ If the remote repository is **public**, anyone can see your name, goals, mistakes, and full session transcripts — use a private repository if you don't want that
- ⚠️ If you don't want a detail recorded, say so during the session; the tutor writes what you typed
- ✅ To stop syncing: reset this repo and set `FLUENT_DATA_DIR` to a folder outside git

## 📊 File Structure

### learner-profile.json
Contains your basic information and preferences:
```json
{
  "learner": {
    "name": "Your Name",
    "target_language": "Spanish",
    "current_level": "A2",
    "target_level": "B2"
  },
  "current_streak_days": 0,
  "skills": {...}
}
```

### progress-db.json
Tracks your statistics over time:
```json
{
  "overall_stats": {
    "total_exercises": 0,
    "total_correct": 0,
    "accuracy_rate": 0
  },
  "accuracy_trend": []
}
```

### mistakes-db.json
Records error patterns with examples:
```json
{
  "error_patterns": {
    "pattern_name": {
      "frequency": 0,
      "mastery_level": 0,
      "examples": []
    }
  }
}
```

### mastery-db.json
Tracks mastery levels for each skill:
```json
{
  "skills": {
    "writing": {"mastery_level": 0},
    "speaking": {"mastery_level": 0},
    "vocabulary": {"mastery_level": 0}
  }
}
```

### spaced-repetition.json
Manages review scheduling (SM-2 algorithm):
```json
{
  "review_queue": {
    "today": [],
    "tomorrow": [],
    "this_week": [],
    "later": []
  }
}
```

### session-log.json
Complete history of all practice sessions:
```json
{
  "sessions": [
    {
      "id": "001",
      "date": "2025-11-17",
      "duration_minutes": 30,
      "accuracy": 0.85
    }
  ]
}
```

## 🔄 How It Works

1. **First time:** Run `/fluent-setup` to create your profile
2. **Every session:** Files update automatically as you practice
3. **Backup:** Automatic backups to `.backups/` via hooks
4. **Export:** All data is JSON - easy to analyze or migrate

## 📁 Data Examples

Want to see the structure before running `/fluent-setup`?

Check the `/data-examples` directory for template files with the complete schema.

## ⚠️ Important Notes

- **Never edit these files manually** - Let the system manage them
- **Don't delete while learning** - You'll lose your progress!
- **To reset:** Delete all `.json` files and run `/fluent-setup` again
- **To backup:** Copy entire `/data` directory

---

**Ready to start?** Run `/fluent-setup` to begin your language learning journey! 🚀
