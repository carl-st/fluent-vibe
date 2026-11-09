# 🌍 Fluent
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Mistral Vibe](https://img.shields.io/badge/Powered%20by-Mistral%20Vibe-orange)](https://mistral.ai)

**The AI Language Learning Kit for Mistral Vibe**

This is a fork of [fluent by m98](https://github.com/m98/fluent)

*A comprehensive set of rules, guidance, and intelligent tracking systems that transform Mistral Vibe into your personal language tutor. Master any language through adaptive practice powered by proven cognitive science—spaced repetition, active recall, and progress tracking that learns from you.*


---


## 🚀 Quick Start

Fluent lives inside the repository: clone it, trust the folder, and the skills are available as slash commands from any device.

### 1. Install

```bash
git clone https://github.com/carl-st/fluent-vibe.git
cd fluent-vibe
uv tool install mistral-vibe   # if Vibe is not installed yet
vibe                           # launch from the repo root, trust the folder when prompted
```

### 2. Start learning

```
/fluent-setup     # onboard: name, target language, level, goals
/fluent-learn     # begin your first session
```

That's it. Every session ends with a git commit (and push, if a remote is configured), so clone the repo on another device and continue exactly where you left off.

---

### Requirements

- [Mistral Vibe](https://mistral.ai) installed (`uv tool install mistral-vibe`)
- **Python 3.8+** (most systems already have it — check with `python3 --version`). Install via [python.org](https://www.python.org/downloads/), `brew install python3`, or your distro's package manager. No pip packages needed — Fluent uses only the standard library.

### Update

```bash
git pull            # inside the repo — gets skills, fixes, and (on the same branch) your progress
```

### Where your data lives

Fluent resolves the data directory in this order — first match wins:

1. `$FLUENT_DATA_DIR` if set (override everything).
2. `./data/` if it has `learner-profile.json` (Vibe session with the repo as working directory).
3. `<repo-root>/data/` (repo checkout — covers the first run before the profile exists).
4. `~/.vibe/fluent-data/` (fallback when running outside the repo).

Set `FLUENT_DATA_DIR` to run multiple learners on one machine:

```bash
export FLUENT_DATA_DIR=~/.fluent/dutch
```

Check where Fluent is currently looking:

```bash
python3 -c "import sys; sys.path.insert(0, 'hooks'); from fluent_paths import data_dir; print(data_dir())"
```

---

## 💡 Why This Actually Works

Most language learning apps fail because they're built for engagement metrics, not actual learning. This system is different.

### 🎯 Three Reasons This Works Where Others Fail:

**1. Zero Distractions, Pure Focus**
- ❌ No ads interrupting your flow
- ❌ No gamification gimmicks designed to waste your time
- ❌ No unreliable fancy UI that breaks
- ✅ Just you, the language, and an AI that adapts to your needs

**2. Infinitely Adaptable Intelligence**
- 🧠 Want to practice job interview phrases? Just ask.
- 🧠 Need help with a specific grammar rule? It explains it.
- 🧠 Want to focus on restaurant vocabulary? It creates exercises instantly.
- 🧠 **You're in control.** The AI does exactly what you need, when you need it.

**3. Your Private, Smart Tutor**
- 📊 **Tracks everything** - Every answer, every mistake, every improvement
- 🔄 **Learns about YOU** - Knows your weak patterns and strengths
- 📈 **Adapts to YOU** - Adjusts difficulty based on your performance
- 🔒 **Private** - All data stays on your machine, no external tracking
- 🎯 **Personal** - Like having a tutor who knows your exact level and learning style

**The Result?** A learning system that feels like a conversation with an expert friend who remembers everything, tracks your progress scientifically, and makes learning actually enjoyable.

---

## 📖 What Is This?

This is a comprehensive, **open-source language learning system** that transforms [Mistral Vibe](https://mistral.ai) into your personal AI language tutor.

The system uses **evidence-based learning methodologies** including:
- **Spaced Repetition (SM-2 algorithm)** - Review at optimal intervals
- **Active Recall** - Test yourself before seeing answers
- **Adaptive Difficulty** - Always challenging, never frustrating
- **Comprehensive Tracking** - Every answer tracked and analyzed

### ✨ Key Features

- 🎯 **Multi-Language Support** - Learn any language (French, Spanish, German, Japanese, vibe, Arabic, Dutch, etc.)
- 📊 **Comprehensive Tracking** - Automatic progress monitoring with detailed statistics
- 🧠 **Spaced Repetition** - SM-2 algorithm schedules reviews just before you forget
- 🎮 **Gamification** - Streaks, achievements, mastery levels (0-5 stars)
- 🔄 **Adaptive Difficulty** - Automatically adjusts to your performance (targets 60-70% success rate)
- 📝 **Multi-Modal Practice** - Writing, speaking, vocabulary, reading, listening
- ⚡ **Immediate Feedback** - Clear explanations with every correction
- 🎨 **Interactive Sessions** - One question at a time, conversational feel
- 📈 **Progress Visualization** - Detailed statistics and trend analysis
- 💾 **Automatic Backups** - Hooks ensure your data is always safe

---

## 📚 How It Works

### The Learning Loop

Every practice session follows this intelligent cycle:

| Step | What Happens | Why It Matters |
|------|--------------|----------------|
| **1. You Practice** | Answer a question in your target language | Active recall forces your brain to retrieve information |
| **2. AI Analyzes** | System evaluates your response instantly | Identifies exactly what you got right or wrong |
| **3. Get Feedback** | Clear explanation of mistakes + correct version | Learning happens when you understand WHY |
| **4. System Tracks** | Updates 4 databases automatically | Remembers your weak spots and strengths |
| **5. Adapts** | Next question matches your current level | Always challenging, never frustrating |

**What Gets Tracked:**
- ✅ **Error Patterns** - Which grammar/vocab you struggle with
- ✅ **Mastery Levels** - Your skill rating (0-5 stars) for each topic
- ✅ **Review Schedule** - When to review based on SM-2 algorithm
- ✅ **Progress Stats** - Accuracy trends, streak days, total practice time

### Evidence-Based Methods

This system implements proven learning science:

**1. Active Recall** - You retrieve from memory before seeing answers
- 🔬 Research shows: **2-3x better retention** than passive review

**2. Spaced Repetition (SM-2 Algorithm)** - Reviews appear just before you forget
- 🔬 Research shows: **Prevents forgetting curve**, optimizes long-term retention

**3. Immediate Feedback** - Mistakes corrected within seconds
- 🔬 Research shows: **Faster learning** when feedback is immediate

**4. Interleaving** - Mix topics to prevent drilling fatigue
- 🔬 Research shows: **Better discrimination** and long-term retention

**5. Comprehensible Input (i+1)** - Content slightly above your level
- 🔬 Research shows: **Optimal learning zone** (Krashen's Input Hypothesis)

**6. Desirable Difficulty** - Targets 60-70% success rate
- 🔬 Research shows: **Too easy = no learning, too hard = frustration**

---

## 🎮 Available Commands & Skills

Fluent is built as **Mistral Vibe skills** — 12 of them living in `.vibe/skills/`, loaded whenever you launch Vibe in the repo. Skills work two ways:

1. **Type the slash command** (`/fluent-learn`, `/fluent-vocab`, etc.) — you explicitly start a session. Learner-facing skills are gated so they only run this way. No accidental 20-minute session triggered by a chat message.
2. **Ask naturally** — read-only skills like `/fluent-progress` auto-trigger when you ask "how am I doing?" or "what's my streak?". Helper skills (SM-2 math, feedback formatter, DB updater, session analyzer) auto-load whenever the tutor needs them during a session.

All 12 skills appear in your `/` menu so you can always invoke any of them manually.

### Learner-facing commands

These are the commands you'll use daily. Each is backed by a dedicated skill under `.vibe/skills/`.

#### Core Commands

| Command | What It Does | When & Why to Use It |
|---------|--------------|----------------------|
| **`/fluent-setup`** | **One-time onboarding** - Asks you questions about your name, target language, current level, goals, and timeline. Creates your personalized learning profile. | **First time only** - Run this once to set up your account. The system generates a custom learning plan based on your answers. |
| **`/fluent-learn`** | **Adaptive mixed practice** - Combines different exercise types (vocabulary, grammar, sentences) based on your weak areas. Adjusts difficulty in real-time based on your performance. | **Daily core practice** - Your main command for general improvement. The AI decides what you need to practice most. Best after `/fluent-review`. |
| **`/fluent-review`** | **Spaced repetition session** - Shows you items that are due for review today based on the SM-2 algorithm. Focuses on things you learned before that need reinforcement. | **Start every day here!** - Review before learning new content. This is scientifically proven to be the most effective way to retain what you've learned. |

#### Skill-Specific Commands

| Command | What It Does | When & Why to Use It |
|---------|--------------|----------------------|
| **`/fluent-vocab`** | **Flashcard-style vocabulary drills** - Rapid-fire translation practice (target language ↔ native language). Tracks which words you struggle with. | **2-3x per week** - When you need to build vocabulary quickly. Great for preparing for specific topics (travel, business, etc.). |
| **`/fluent-writing`** | **Writing practice** - Practice emails, letters, essays, or forms in your target language. Get detailed corrections with grammar explanations. | **Daily for exam prep** - Essential if you're preparing for language exams. Also great for building confidence in real-world communication. |
| **`/fluent-speaking`** | **Conversation practice** - Role-play scenarios through typed dialogue. Practice natural conversations, asking for directions, ordering food, etc. | **2-3x per week** - Builds confidence for real conversations. Typed practice helps you think through responses without pressure. |
| **`/fluent-reading`** | **Reading comprehension** - Read short texts (stories, articles, dialogues) then answer comprehension questions. Expands vocabulary in context. | **2-3x per week** - Improves overall understanding. Best for intermediate+ learners. Reading is one of the fastest ways to absorb grammar patterns. |

#### Progress Command

| Command | What It Does | When & Why to Use It |
|---------|--------------|----------------------|
| **`/fluent-progress`** | **Statistics dashboard** - Shows your accuracy trends, streak days, mastery levels, achievements unlocked, and weak areas. Visual progress charts. | **Weekly check-in** - Read-only and safe to auto-invoke. Ask "how am I doing?" and the dashboard opens automatically. |

### Helper skills (behind the scenes)

These skills don't change what the learner-facing commands do — they let the tutor apply the same algorithms, feedback format, and database logic consistently across every session. You can still invoke them via `/` if curious.

| Skill | What It Does | When It Runs |
|-------|--------------|--------------|
| **`/fluent-sm2-calculator`** | SM-2 spaced-repetition algorithm reference: quality scale, interval formula, easiness-factor update, mastery-level transitions. | Auto-loaded whenever a review item is scored. |
| **`/fluent-feedback-formatter`** | Canonical per-answer feedback template — severity tagging (🔴 critical / 🟡 moderate / 🟢 minor), category labels, tone rules. | Auto-loaded every time the tutor grades an answer. |
| **`/fluent-db-updater`** | How to call `update-db.py` with a single JSON payload that atomically updates all 6 databases at session end. | Auto-loaded when a session ends. |
| **`/fluent-session-analyzer`** | Parses `/results/fluent-{skill}-session-{ID}.md` files to extract error patterns, strengths, and focus areas for the next session. | Auto-loaded when planning the next session. |

### 📅 Recommended Daily Routine

**🌅 Morning Session (15 min)**
```bash
/fluent-review    # Must do first - Review what you learned before
/fluent-vocab     # Learn 5-10 new words
```
**Why?** Your brain is fresh. Reviewing first reinforces old knowledge, then new vocabulary sticks better.

**🌙 Evening Session (15 min)**
```bash
/fluent-writing   # Practice real-world writing
/fluent-learn     # Let AI choose what you need most
```
**Why?** Writing solidifies what you learned today. `/fluent-learn` fills in any gaps.

**📊 Weekly Check-In (5 min)**
```bash
/fluent-progress  # See your stats and celebrate progress!
```
**Why?** Seeing improvement = motivation. You need to see you're getting better!

---

## 📁 System Architecture

### Data Layer (`/data` directory)

**Your learning data is tracked in 6 JSON databases** (created automatically by `/fluent-setup`):

| File | Purpose | Created When |
|------|---------|--------------|
| `learner-profile.json` | Your info, level, preferences, streak | `/fluent-setup` - One time |
| `progress-db.json` | Overall statistics and trends | `/fluent-setup` - Updated every session |
| `mistakes-db.json` | Error patterns with frequency and examples | `/fluent-setup` - Updated when you make mistakes |
| `mastery-db.json` | Skill mastery levels (0-5 stars) | `/fluent-setup` - Updated after practice |
| `spaced-repetition.json` | Review queue (SM-2 algorithm) | `/fluent-setup` - Updated after each answer |
| `session-log.json` | Complete session history | `/fluent-setup` - New entry each session |

**📋 Want to see the structure?** Check `/data-examples/` for template files showing the complete schema.

**🔄 Cross-device:** Progress is committed to git at the end of every session, so you can continue learning from any device that clones this repo. ⚠️ If your fork is public, your learning data is public too — use a private repository.

### Intelligence Layer

The AI follows these guides:

- **`LEARNING_SYSTEM.md`** - Complete methodology (how to teach)
- **`TUTOR.md`** - AI tutor's role and personality
- **`PRACTICE.md`** - Pattern analysis and tracking
- **`docs/`** - Shared templates (SM-2 worked examples, feedback template, DB payload schema, session-file format) that every skill references

### Interface Layer

- **Skills** (`.vibe/skills/`) — 12 skills total. 8 learner-facing (`/fluent-setup`, `/fluent-learn`, `/fluent-vocab`, `/fluent-writing`, `/fluent-speaking`, `/fluent-reading`, `/fluent-review`, `/fluent-progress`) run when you invoke them. 4 helper skills (`/fluent-sm2-calculator`, `/fluent-feedback-formatter`, `/fluent-db-updater`, `/fluent-session-analyzer`) auto-load whenever the tutor needs them during a session — and are also directly `/`-invokable if you want to read the reference.
- **Project Hooks** (`.vibe/hooks.toml`) — a `post_tool` validator that JSON-validates every write to a learner database and keeps timestamped backups. Wired up automatically when Vibe runs in the folder you trust.
- **Session Results** (`/results/`) — Detailed practice logs per session, parsed by `fluent-session-analyzer` to plan future sessions.

---

## 🎯 Learning Principles

### Spaced Repetition (SM-2 Algorithm)

**Example progression for a difficult word:**

```
Day 1:  Make a mistake → Review tomorrow (interval = 1 day)
Day 2:  Answer correctly → Review in 6 days
Day 8:  Correct again → Review in 2 weeks
Day 22: Still remember → Monthly review (mastered!)
```

The system tracks for each item:
- **Easiness Factor** - How easy it is for YOU specifically
- **Interval Days** - When to review next
- **Repetitions** - Practice count
- **Quality Score** - Your performance (0-5)

### Mastery Levels

Every skill and pattern gets a star rating:

- ⭐☆☆☆☆ (1) - Just started
- ⭐⭐☆☆☆ (2) - Learning
- ⭐⭐⭐☆☆ (3) - Good understanding
- ⭐⭐⭐⭐☆ (4) - Strong skill
- ⭐⭐⭐⭐⭐ (5) - Mastered!

### Adaptive Difficulty

The system automatically adjusts:

- **Success rate 40-50%** → Too hard, makes easier
- **Success rate 60-70%** → Perfect challenge! ✨
- **Success rate 80-90%** → Too easy, makes harder

**Goal:** Keep you in the "sweet spot" where learning happens.

---

## 🔬 Technical Details

### Technology Stack

- **Platform:** Mistral Vibe (Mistral AI), running directly in the repo
- **AI Model:** Any Vibe-configured model (Mistral models by default)
- **Data Format:** JSON (human-readable)
- **Skills:** Markdown `SKILL.md` files with YAML frontmatter (12 total — 8 learner-facing + 4 helper)
- **Hooks:** Python, triggered on post_tool (Write/Edit)
- **Algorithm:** SM-2 (SuperMemo 2)
- **Version Control:** Git

### Data Privacy & Security

- ✅ **Cross-device sync** — every session ends with a git commit (+ push) of `data/` and `results/`
- ✅ **No external API calls** (except your AI provider's API through Vibe)
- ✅ **Automatic backups** to `.backups/` directory
- ✅ **No tracking, no analytics, no telemetry**
- ⚠️ **Learning data is committed to the repo** — keep the repository private if you don't want your name, goals, and session transcripts visible

### Hooks System (Automated Data Management)

Fluent uses a Vibe project hook to ensure your data is always safe and validated:

**🔄 post_tool Hook** (after every write_file / edit on a learner JSON)
- ✅ Validates the JSON structure automatically
- ✅ Alerts the tutor immediately if data is malformed (the tool output is replaced with the validation error)
- ✅ Creates timestamped backup: `data/file.json.backup-20231117-143022` (last 10 kept)

The welcome message and session stats that previous versions showed via SessionStart/SessionEnd hooks are now part of the skills themselves — every session skill greets with your name, streak, and due reviews from `read-db.py`, and `update-db.py` takes a pre-write backup of all 6 databases on every session-end update.

**You'll never lose your progress.** All backups are automatic and excluded from git.

See [`hooks/README.md`](hooks/README.md) for technical details.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Mistral AI** - For Mistral Vibe and the AI capabilities
- **The original [m98/fluent](https://github.com/m98/fluent) project** - This kit started as its fork
- **SuperMemo** - For the SM-2 algorithm
- **Anki** - For inspiring the flashcard approach
- **Language learning research** - Krashen, Bjork, Ebbinghaus, and many others
- **Open-source community** - For making this possible

---

## 📞 Support & Community

- 📖 **Documentation:** [Full docs in this repo](docs/)

---

## 📈 Project Stats

- **Skills:** 12 (8 learner-facing + 4 helper)
- **Hooks:** 1 project hook + DB helper scripts
- **Databases:** 6 JSON tracking files
- **Install paths:** 1 (git clone — skills load from the repo)
- **Languages Supported:** All (system is fully language-agnostic)
- **Learning Methods:** 6 evidence-based principles
- **Contributors:** [See contributors](https://github.com/m98/fluent/graphs/contributors)

---


## 🛠️ Troubleshooting

**`python3: command not found` when hooks run.**
Install Python 3.8+ and make sure `python3` is on your PATH. On macOS: `brew install python3`. On Debian/Ubuntu: `sudo apt install python3`. On Windows: install via [python.org](https://www.python.org/downloads/) or use WSL.

**Hooks silently do nothing.**
The project hook (`.vibe/hooks.toml`) only loads when the folder is trusted. Use `/reload` after editing it, and check the startup warnings box for hook load errors. The hook itself is plain Python — it works on native Windows.

**Learner data is showing up in the wrong place.**
Check the data-dir resolution order (see above). Set `FLUENT_DATA_DIR` explicitly in your shell to force a specific location.

**JSON validation fails after a manual edit.**
The post_tool hook flags malformed JSON in the tool output and keeps the last 10 backups at `<data_dir>/<filename>.json.backup-<timestamp>`. Restore with: `cp <data_dir>/learner-profile.json.backup-XXXXXX <data_dir>/learner-profile.json`.

**Skills don't appear in the `/` menu.**
You're probably not in the repo folder, or the folder isn't trusted yet. Launch `vibe` from the repo root, trust it when prompted, then check the `/` menu. Inside a session, `/reload` re-reads skills from disk.

---

## 🔗 Useful Links

- [Mistral Vibe Documentation](https://docs.mistral.ai/vibe/code/overview)
- [Mistral Vibe on GitHub](https://github.com/mistralai/mistral-vibe)
- [SM-2 Algorithm Explained](https://www.supermemo.com/en/archives1990-2015/english/ol/sm2)
- [CEFR Levels](https://www.coe.int/en/web/common-european-framework-reference-languages/level-descriptions)
- [Spaced Repetition Research](https://www.gwern.net/Spaced-repetition)
- [Active Recall Benefits](https://en.wikipedia.org/wiki/Testing_effect)

---

## ❓ FAQ

**Q: How is this different from Duolingo/Babbel/etc?**
A: It’s ultra-minimalistic, just a terminal and pure learning. No extra distributions, no ads, no gimmicks. Infinitely adaptable. You ask it to teach you something, and it does. And best of all, everything stays private on your machine.

**Q: Do I need to know how to code?**
A: No! Just install Vibe, clone the repo, and run `/fluent-setup`. That's it.

**Q: How long until I see progress?**
A: Most learners see measurable improvement within the first week. The system tracks everything so you can see exactly how you're improving.

**Q: Can I use this for exam preparation?**
A: Yes! The system adapts to your goals. Tell it you're preparing for DELE/DELF/TestDaF/etc. and it'll focus on exam-relevant content.

**Q: Is my data safe?**
A: Absolutely. Everything stays on your machine (and whichever remote you push the repo to). No cloud storage, no external servers (except your AI provider's API).

**Q: Can I export my progress?**
A: Yes! All data is in human-readable JSON. You can export, analyze, or migrate it anytime.

**Q: Can I use a different AI CLI instead of Mistral Vibe?**
A: This kit is specifically optimized for Mistral Vibe and its capabilities (project skills,
`.vibe/hooks.toml`, AGENTS.md discovery). The original upstream supports other AI CLIs — see
[m98/fluent](https://github.com/m98/fluent) — but using another platform may not yield the same
results here.


---

*Start your language learning journey today!* 🚀

```bash
git clone https://github.com/carl-st/fluent-vibe.git
cd fluent-vibe
vibe
/fluent-setup
```
