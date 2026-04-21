---
sidebar_position: 3
title: "Persistent Memory"
description: "How Hermes Agent remembers across sessions — MEMORY.md, USER.md, failure routes, and session search"
---

# Persistent Memory

Hermes Agent has bounded, curated memory that persists across sessions. This lets it remember your preferences, your projects, your environment, and things it has learned.

## How It Works

Three built-in stores make up the agent's memory:

| File / Path | Purpose | Char Limit |
|------|---------|------------|
| **MEMORY.md** | Agent's personal notes — environment facts, conventions, things learned | 2,200 chars (~800 tokens) |
| **USER.md** | User profile — your preferences, communication style, expectations | 1,375 chars (~500 tokens) |
| **failures/\*.md** | Failure routes — rejected approaches and hard constraints to avoid repeating | 6,000 chars total |

All are stored in `~/.hermes/memories/`. `MEMORY.md` and `USER.md` are injected into the system prompt as a frozen snapshot at session start. Failure routes are recalled selectively at API-call time only when the current task matches them. The agent manages all three via the `memory` tool.

:::info
Character limits keep memory focused. When memory is full, the agent consolidates or replaces entries to make room for new information.
:::

## How Memory Appears in the System Prompt

At the start of every session, built-in memory entries are loaded from disk and rendered into the system prompt as frozen blocks:

```
══════════════════════════════════════════════
MEMORY (your personal notes) [67% — 1,474/2,200 chars]
══════════════════════════════════════════════
User's project is a Rust web service at ~/code/myapi using Axum + SQLx
§
This machine runs Ubuntu 22.04, has Docker and Podman installed
§
User prefers concise responses, dislikes verbose explanations
```

The format includes:
- A header showing which store (MEMORY or USER PROFILE)
- Usage percentage and character counts so the agent knows capacity
- Individual entries separated by `§` (section sign) delimiters
- Entries can be multiline

**Frozen snapshot pattern:** The system prompt injection is captured once at session start and never changes mid-session. This preserves the LLM's prefix cache for performance.

There is now a second layer of **query-time recall**:

- The frozen `MEMORY.md` / `USER.md` snapshot stays stable for caching
- Before each API call, Hermes can inject a small **relevant-memory overlay** for the current task
- Failure routes are also recalled only when their filenames/content match the current task

This gives you better recall without constantly rebuilding the system prompt.

## Memory Tool Actions

The agent uses the `memory` tool with these actions:

- **add** — Add a new memory entry
- **replace** — Replace an existing entry with updated content (uses substring matching via `old_text`)
- **remove** — Remove an entry that's no longer relevant (uses substring matching via `old_text`)

There is no `read` action — the agent receives memory automatically through the frozen system-prompt snapshot plus task-relevant recall overlays.

### Substring Matching

The `replace` and `remove` actions use short unique substring matching — you don't need the full entry text. The `old_text` parameter just needs to be a unique substring that identifies exactly one entry:

```python
# If memory contains "User prefers dark mode in all editors"
memory(action="replace", target="memory",
       old_text="dark mode",
       content="User prefers light mode in VS Code, dark mode in terminal")
```

If the substring matches multiple entries, an error is returned asking for a more specific match.

## Three Targets Explained

### `memory` — Agent's Personal Notes

For information the agent needs to remember about the environment, workflows, and lessons learned:

- Environment facts (OS, tools, project structure)
- Project conventions and configuration
- Tool quirks and workarounds discovered
- Durable workflow notes
- Stable technical facts that matter again later

### `user` — User Profile

For information about the user's identity, preferences, and communication style:

- Name, role, timezone
- Communication preferences (concise vs detailed, format preferences)
- Pet peeves and things to avoid
- Workflow habits
- Technical skill level

### `failure` — Failure Routes

For rejected approaches and hard constraints that should actively steer the agent away from repeating a known bad route:

- Dead ends that looked plausible but failed
- Drafting patterns that produced low-quality output
- Environment-specific traps
- Approaches the user explicitly rejected

Failure entries are stored in named files under `~/.hermes/memories/failures/`. Hermes first matches route filenames against the current task, then loads only those files. This is intentionally more selective than normal memory injection.

## What to Save vs Skip

### Save These (Proactively)

The agent saves automatically — you don't need to ask. It saves when it learns:

- **User preferences:** "I prefer TypeScript over JavaScript" → save to `user`
- **Environment facts:** "This server runs Debian 12 with PostgreSQL 16" → save to `memory`
- **Corrections:** "Don't use `sudo` for Docker commands, user is in docker group" → save to `memory`
- **Conventions:** "Project uses tabs, 120-char line width, Google-style docstrings" → save to `memory`
- **Failure lesson:** "Do not show unreviewed draft output to the user" → save to `failure`
- **Explicit requests:** "Remember that my API key rotation happens monthly" → save to `memory`

### Skip These

- **Trivial/obvious info:** "User asked about Python" — too vague to be useful
- **Easily re-discovered facts:** "Python 3.12 supports f-string nesting" — can web search this
- **Raw data dumps:** Large code blocks, log files, data tables — too big for memory
- **Session-specific ephemera:** Temporary file paths, one-off debugging context
- **Information already in context files:** SOUL.md and AGENTS.md content

## Capacity Management

Memory has strict character limits to keep system prompts bounded:

| Store | Limit | Typical entries |
|-------|-------|----------------|
| memory | 2,200 chars | 8-15 entries |
| user | 1,375 chars | 5-10 entries |
| failure | 6,000 chars total | 5-20 route-scoped lessons |

### What Happens When Memory is Full

When you try to add an entry that would exceed the limit, the tool returns an error:

```json
{
  "success": false,
  "error": "Memory at 2,100/2,200 chars. Adding this entry (250 chars) would exceed the limit. Replace or remove existing entries first.",
  "current_entries": ["..."],
  "usage": "2,100/2,200"
}
```

The agent should then:
1. Read the current entries (shown in the error response)
2. Identify entries that can be removed or consolidated
3. Use `replace` to merge related entries into shorter versions
4. Then `add` the new entry

**Best practice:** When memory is above 80% capacity (visible in the system prompt header), consolidate entries before adding new ones. For example, merge three separate "project uses X" entries into one comprehensive project description entry.

### Structured Memory Entries

`memory(action="add")` still accepts plain text, but Hermes now also supports optional structured fields:

- `kind`
- `name`
- `description`
- `tags`

These fields are stored as lightweight frontmatter ahead of the entry body. They improve future recall because task-time memory selection can match on metadata as well as body text.

Example:

```python
memory(
  action="add",
  target="memory",
  kind="environment",
  name="docker-networking",
  description="bridge subnet override for this project",
  tags=["docker", "networking", "bridge"],
  content="Project runs in Docker bridge mode and needs a custom subnet to avoid VPN collisions."
)
```

Older plain-text entries still work unchanged.

### Practical Examples of Good Memory Entries

**Compact, information-dense entries work best:**

```
# Good: Packs multiple related facts
User runs macOS 14 Sonoma, uses Homebrew, has Docker Desktop and Podman. Shell: zsh with oh-my-zsh. Editor: VS Code with Vim keybindings.

# Good: Specific, actionable convention
Project ~/code/api uses Go 1.22, sqlc for DB queries, chi router. Run tests with 'make test'. CI via GitHub Actions.

# Good: Lesson learned with context
The staging server (10.0.1.50) needs SSH port 2222, not 22. Key is at ~/.ssh/staging_ed25519.

# Bad: Too vague
User has a project.

# Bad: Too verbose
On January 5th, 2026, the user asked me to look at their project which is
located at ~/code/api. I discovered it uses Go version 1.22 and...
```

## Duplicate Prevention

The memory system automatically rejects exact duplicate entries. If you try to add content that already exists, it returns success with a "no duplicate added" message.

## Security Scanning

Memory entries are scanned for injection and exfiltration patterns before being accepted, since they're injected into the system prompt. Content matching threat patterns (prompt injection, credential exfiltration, SSH backdoors) or containing invisible Unicode characters is blocked.

## Failure Routes

Failure routes are built-in durable anti-pattern memory. They are designed for lessons like:

- "Do not leak unreviewed drafts to the user"
- "Do not assume SSH_AUTH_SOCK exists inside Docker"
- "Do not remove required Node.js packages while slimming the image"

When Hermes stores a failure memory, it can place it in a named route file such as:

```text
~/.hermes/memories/failures/output-review-unreviewed-draft.md
```

Each route file now carries lightweight metadata alongside the entries:

- `Description:` — one-line summary of what the route is about
- `Tags:` — compact topical tags derived from the route name and recent entries
- `Keywords:` — broader lexical hints used for matching

This metadata improves route matching without forcing every failure route into every prompt.

At runtime Hermes:

1. Matches route filenames against the current task
2. Loads only the best-matching route files
3. Injects them as a temporary failure-memory block

This means failure lessons remain precise and low-noise instead of polluting every session prompt.

## Session Search

Beyond MEMORY.md and USER.md, the agent can search its past conversations using the `session_search` tool:

- All CLI and messaging sessions are stored in SQLite (`~/.hermes/state.db`) with FTS5 full-text search
- Search queries return relevant past conversations with Gemini Flash summarization
- The agent can find things it discussed weeks ago, even if they're not in its active memory

```bash
hermes sessions list    # Browse past sessions
```

### session_search vs memory

| Feature | Persistent Memory | Session Search |
|---------|------------------|----------------|
| **Capacity** | ~1,300 tokens total | Unlimited (all sessions) |
| **Speed** | Instant (in system prompt) | Requires search + LLM summarization |
| **Use case** | Key facts always available | Finding specific past conversations |
| **Management** | Manually curated by agent | Automatic — all sessions stored |
| **Token cost** | Fixed per session (~1,300 tokens) | On-demand (searched when needed) |

**Memory** is for critical facts that should always be in context. **Session search** is for "did we discuss X last week?" queries where the agent needs to recall specifics from past conversations.

## Configuration

```yaml
# In ~/.hermes/config.yaml
memory:
  memory_enabled: true
  user_profile_enabled: true
  failure_memory_enabled: true
  memory_char_limit: 2200   # ~800 tokens
  user_char_limit: 1375     # ~500 tokens
  failure_char_limit: 6000

  # Task-time recall overlay for built-in memory/user entries
  memory_recall_enabled: true
  memory_recall_max_entries: 4
  memory_recall_max_chars: 1200

  # Task-time failure-route recall
  failure_recall_max_entries: 3
  failure_recall_max_chars: 1400
```

## External Memory Providers

For deeper, persistent memory that goes beyond MEMORY.md and USER.md, Hermes ships with 8 external memory provider plugins — including Honcho, OpenViking, Mem0, Hindsight, Holographic, RetainDB, ByteRover, and Supermemory.

External providers run **alongside** built-in memory (never replacing it) and add capabilities like knowledge graphs, semantic search, automatic fact extraction, and cross-session user modeling.

```bash
hermes memory setup      # pick a provider and configure it
hermes memory status     # check what's active
```

See the [Memory Providers](./memory-providers.md) guide for full details on each provider, setup instructions, and comparison.
