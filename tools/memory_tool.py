#!/usr/bin/env python3
"""
Memory Tool Module - Persistent Curated Memory

Provides bounded, file-backed memory that persists across sessions. Three stores:
  - MEMORY.md: agent notes about the environment and stable conventions
  - USER.md: who the user is, their preferences, and working style
  - failures/*.md: named failure-route files containing hard constraints about
    rejected approaches and dead ends to avoid repeating

Memory is loaded as a frozen snapshot at session start so the system prompt
stays stable for prompt caching. Live writes still persist to disk immediately.
"""

import json
import logging
import os
import re
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from hermes_constants import get_hermes_home

logger = logging.getLogger(__name__)

try:
    import fcntl as _fcntl
except ImportError:  # pragma: no cover - Windows fallback
    _fcntl = None


def get_memory_dir() -> Path:
    """Return the profile-scoped memories directory."""
    return get_hermes_home() / "memories"


MEMORY_DIR = get_memory_dir()
ENTRY_DELIMITER = "\n\u00a7\n"
FAILURE_ROUTES_DIRNAME = "failures"
LEGACY_FAILURE_FILE = "FAILURES.md"


_MEMORY_THREAT_PATTERNS = [
    (r"ignore\s+(previous|all|above|prior)\s+instructions", "prompt_injection"),
    (r"you\s+are\s+now\s+", "role_hijack"),
    (r"do\s+not\s+tell\s+the\s+user", "deception_hide"),
    (r"system\s+prompt\s+override", "sys_prompt_override"),
    (r"disregard\s+(your|all|any)\s+(instructions|rules|guidelines)", "disregard_rules"),
    (
        r"act\s+as\s+(if|though)\s+you\s+(have\s+no|don't\s+have)\s+"
        r"(restrictions|limits|rules)",
        "bypass_restrictions",
    ),
    (r"curl\s+[^\n]*\$\{?\w*(KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL|API)", "exfil_curl"),
    (r"wget\s+[^\n]*\$\{?\w*(KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL|API)", "exfil_wget"),
    (r"cat\s+[^\n]*(\.env|credentials|\.netrc|\.pgpass|\.npmrc|\.pypirc)", "read_secrets"),
    (r"authorized_keys", "ssh_backdoor"),
    (r"\$HOME/\.ssh|\~/\.ssh", "ssh_access"),
    (r"\$HOME/\.hermes/\.env|\~/\.hermes/\.env", "hermes_env"),
]

_INVISIBLE_CHARS = {
    "\u200b",
    "\u200c",
    "\u200d",
    "\u2060",
    "\ufeff",
    "\u202a",
    "\u202b",
    "\u202c",
    "\u202d",
    "\u202e",
}


def _scan_memory_content(content: str) -> Optional[str]:
    """Scan memory content for injection or exfiltration patterns."""
    for char in _INVISIBLE_CHARS:
        if char in content:
            return (
                "Blocked: content contains invisible unicode character "
                f"U+{ord(char):04X} (possible injection)."
            )

    for pattern, pid in _MEMORY_THREAT_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            return (
                "Blocked: content matches threat pattern "
                f"'{pid}'. Memory entries are injected into the system prompt "
                "and must not contain injection or exfiltration payloads."
            )
    return None


def _safe_structured_token(text: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_.:/\-\u4e00-\u9fff ]+", " ", (text or "").strip())
    value = re.sub(r"\s+", " ", value).strip()
    return value


def _dedupe_preserve(values: List[str]) -> List[str]:
    seen = set()
    result = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def _parse_structured_entry(entry: str) -> Dict[str, Any]:
    """Parse optional frontmatter metadata from a memory entry.

    Backward compatible: plain-text entries are treated as body-only.
    """
    raw = (entry or "").strip()
    result = {
        "kind": "",
        "name": "",
        "description": "",
        "tags": [],
        "body": raw,
    }
    if not raw.startswith("---\n") and raw != "---":
        return result

    lines = raw.splitlines()
    if not lines or lines[0].strip() != "---":
        return result

    meta_lines: List[str] = []
    end_idx = None
    for idx, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = idx
            break
        meta_lines.append(line)
    if end_idx is None:
        return result

    meta: Dict[str, str] = {}
    for line in meta_lines:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip()
        if key:
            meta[key] = value

    body = "\n".join(lines[end_idx + 1 :]).strip()
    tags = [
        token.strip()
        for token in re.split(r"[,\s]+", meta.get("tags", ""))
        if token.strip()
    ]
    result.update(
        {
            "kind": meta.get("kind", ""),
            "name": meta.get("name", ""),
            "description": meta.get("description", ""),
            "tags": _dedupe_preserve(tags),
            "body": body or raw,
        }
    )
    return result


def _format_structured_entry(
    *,
    body: str,
    kind: str = "",
    name: str = "",
    description: str = "",
    tags: Optional[List[str]] = None,
) -> str:
    """Build a structured memory entry with optional frontmatter."""
    clean_body = (body or "").strip()
    clean_kind = _safe_structured_token(kind).lower()
    clean_name = _safe_structured_token(name)
    clean_description = _safe_structured_token(description)
    clean_tags = _dedupe_preserve([_safe_structured_token(tag).lower() for tag in (tags or []) if _safe_structured_token(tag)])

    meta_lines = []
    if clean_kind:
        meta_lines.append(f"kind: {clean_kind}")
    if clean_name:
        meta_lines.append(f"name: {clean_name}")
    if clean_description:
        meta_lines.append(f"description: {clean_description}")
    if clean_tags:
        meta_lines.append(f"tags: {', '.join(clean_tags)}")

    if not meta_lines:
        return clean_body

    return "---\n" + "\n".join(meta_lines) + "\n---\n" + clean_body


def _render_structured_entry_for_prompt(entry: str) -> str:
    """Render a memory entry for prompt injection.

    Plain-text entries are passed through unchanged. Structured entries are
    rendered into a compact human-readable form so the model sees the metadata
    without the raw frontmatter syntax.
    """
    parsed = _parse_structured_entry(entry)
    body = (parsed.get("body") or "").strip()
    if not body:
        return ""
    if not any((parsed.get("kind"), parsed.get("name"), parsed.get("description"), parsed.get("tags"))):
        return body

    prefix_parts = []
    if parsed.get("kind"):
        prefix_parts.append(f"[{parsed['kind']}]")
    if parsed.get("name"):
        prefix_parts.append(parsed["name"])
    header = " ".join(prefix_parts).strip()

    suffix_parts = []
    if parsed.get("description"):
        suffix_parts.append(parsed["description"])
    tags = parsed.get("tags") or []
    if tags:
        suffix_parts.append(f"tags: {', '.join(tags)}")

    first_line = body.splitlines()[0].strip()
    remainder = "\n".join(line.rstrip() for line in body.splitlines()[1:]).strip()

    lines = []
    if header or suffix_parts:
        label = header
        if suffix_parts:
            if label:
                label += " — " + " | ".join(suffix_parts)
            else:
                label = " | ".join(suffix_parts)
        lines.append(label)

    if first_line:
        if lines:
            lines.append(first_line)
        else:
            lines.append(first_line)
    if remainder:
        lines.append(remainder)
    return "\n".join(lines).strip()


def _render_structured_entry_preview(entry: str, *, max_chars: int = 220) -> str:
    """Render a single entry compactly for tool results and ambiguity previews."""
    rendered = _render_structured_entry_for_prompt(entry)
    if len(rendered) <= max_chars:
        return rendered
    return rendered[:max_chars].rstrip() + "..."


def _structured_match_haystack(entry: str) -> str:
    """Build a searchable haystack for structured and plain memory entries."""
    parsed = _parse_structured_entry(entry)
    return "\n".join(
        part
        for part in (
            parsed.get("kind", ""),
            parsed.get("name", ""),
            parsed.get("description", ""),
            " ".join(parsed.get("tags", [])),
            parsed.get("body", entry),
        )
        if part
    )


def _structured_metadata_text(parsed: Dict[str, Any]) -> str:
    """Return the compact metadata text used for recall scoring."""
    return " ".join(
        part
        for part in (
            parsed.get("name", ""),
            parsed.get("description", ""),
            " ".join(parsed.get("tags", [])),
        )
        if part
    )


def _normalize_structured_tags(tags: Any) -> List[str]:
    """Normalize tags from tool/store inputs into a clean list."""
    if isinstance(tags, str):
        raw_tags = [tag.strip() for tag in re.split(r"[,\s]+", tags) if tag.strip()]
    elif isinstance(tags, list):
        raw_tags = [str(tag).strip() for tag in tags if str(tag).strip()]
    else:
        raw_tags = []
    return _dedupe_preserve(
        [
            cleaned
            for cleaned in (_safe_structured_token(tag).lower() for tag in raw_tags)
            if cleaned
        ]
    )


class MemoryStore:
    """
    Bounded curated memory with file persistence. One instance per AIAgent.

    Maintains two parallel states:
      - _system_prompt_snapshot: frozen at load time for prompt injection
      - live entries: mutated by tool calls and written to disk immediately
    """

    _FAILURE_TOKEN_RE = re.compile(r"[A-Za-z0-9_./:-]{2,}|[\u4e00-\u9fff]{2,}")
    _FAILURE_STOPWORDS = {
        "the",
        "and",
        "for",
        "with",
        "that",
        "this",
        "from",
        "into",
        "when",
        "your",
        "their",
        "them",
        "they",
        "have",
        "will",
        "would",
        "should",
        "after",
        "before",
        "about",
        "because",
        "then",
        "than",
        "just",
        "also",
        "task",
        "draft",
        "failed",
        "failure",
        "result",
        "review",
        "avoid",
        "user",
        "agent",
        "hermes",
        "those",
        "these",
    }

    def __init__(
        self,
        memory_char_limit: int = 2200,
        user_char_limit: int = 1375,
        failure_char_limit: int = 6000,
    ):
        self.memory_entries: List[str] = []
        self.user_entries: List[str] = []
        self.failure_entries: List[str] = []
        self.failure_route_files: List[str] = []
        self.memory_char_limit = memory_char_limit
        self.user_char_limit = user_char_limit
        self.failure_char_limit = failure_char_limit
        self._system_prompt_snapshot: Dict[str, str] = {
            "memory": "",
            "user": "",
            "failure": "",
        }

    def load_from_disk(self) -> None:
        """Load entries from disk and capture the frozen prompt snapshot."""
        mem_dir = get_memory_dir()
        mem_dir.mkdir(parents=True, exist_ok=True)
        self.memory_entries = list(dict.fromkeys(self._read_file(mem_dir / "MEMORY.md")))
        self.user_entries = list(dict.fromkeys(self._read_file(mem_dir / "USER.md")))
        with self._file_lock(self._failure_routes_lock_path()):
            self._ensure_failure_routes_ready()
            self._reload_failure_routes()

        self._system_prompt_snapshot = {
            "memory": self._render_block("memory", self.memory_entries),
            "user": self._render_block("user", self.user_entries),
            "failure": "",
        }

    @staticmethod
    @contextmanager
    def _file_lock(path: Path):
        """Acquire an exclusive lock for read-modify-write safety."""
        lock_path = path.with_suffix(path.suffix + ".lock")
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        fd = open(lock_path, "w")
        try:
            if _fcntl is not None:
                _fcntl.flock(fd, _fcntl.LOCK_EX)
            yield
        finally:
            if _fcntl is not None:
                _fcntl.flock(fd, _fcntl.LOCK_UN)
            fd.close()

    @staticmethod
    def _path_for(target: str) -> Path:
        mem_dir = get_memory_dir()
        if target == "user":
            return mem_dir / "USER.md"
        if target == "failure":
            return mem_dir / LEGACY_FAILURE_FILE
        return mem_dir / "MEMORY.md"

    @staticmethod
    def _failure_routes_dir() -> Path:
        return get_memory_dir() / FAILURE_ROUTES_DIRNAME

    @classmethod
    def _failure_routes_lock_path(cls) -> Path:
        return cls._failure_routes_dir() / "_failure_routes_state"

    @classmethod
    def _ensure_failure_routes_ready(cls) -> None:
        routes_dir = cls._failure_routes_dir()
        routes_dir.mkdir(parents=True, exist_ok=True)
        legacy_path = get_memory_dir() / LEGACY_FAILURE_FILE
        if not legacy_path.exists():
            return
        legacy_entries = cls._read_file(legacy_path)
        if not legacy_entries:
            try:
                legacy_path.unlink()
            except OSError:
                pass
            return
        routes = cls._read_failure_routes_map()
        for entry in legacy_entries:
            route_slug = cls._derive_failure_route_name(content=entry)
            path = cls._failure_route_path_for_name(route_slug)
            route_title = route_slug.replace("-", " ")
            route = routes.get(path)
            existing_entries = list(route.get("entries", [])) if route else []
            if route:
                route_title = route.get("title") or route_title
            if entry in existing_entries:
                continue
            new_entries = existing_entries + [entry]
            cls._write_failure_route(path=path, title=route_title, entries=new_entries)
            routes[path] = {
                "path": path,
                "filename": path.name,
                "title": route_title,
                "description": cls._failure_route_description(route_title, new_entries),
                "tags": cls._failure_route_tags(route_title, new_entries),
                "keywords": cls._failure_route_keywords(route_title, new_entries),
                "entries": new_entries,
            }
        try:
            legacy_path.unlink()
        except OSError:
            pass

    def _reload_failure_routes(self) -> None:
        routes = []
        entries = []
        for path in self._list_failure_route_paths():
            route = self._read_failure_route(path)
            if not route:
                continue
            routes.append(path.name)
            entries.extend(route.get("entries", []))
        self.failure_route_files = routes
        self.failure_entries = list(dict.fromkeys(entries))

    @classmethod
    def _read_failure_routes_map(cls) -> Dict[Path, Dict[str, Any]]:
        routes: Dict[Path, Dict[str, Any]] = {}
        for path in cls._list_failure_route_paths():
            route = cls._read_failure_route(path)
            if route:
                routes[path] = route
        return routes

    @classmethod
    def _flatten_failure_entries_from_routes(
        cls,
        route_entries_by_path: Dict[Path, List[str]],
    ) -> List[str]:
        flattened: List[str] = []
        for path in sorted(route_entries_by_path, key=lambda item: item.name.lower()):
            flattened.extend(
                entry.strip()
                for entry in route_entries_by_path[path]
                if isinstance(entry, str) and entry.strip()
            )
        return list(dict.fromkeys(flattened))

    @classmethod
    def _failure_total_chars_from_routes(
        cls,
        route_entries_by_path: Dict[Path, List[str]],
    ) -> int:
        entries = cls._flatten_failure_entries_from_routes(route_entries_by_path)
        return len(ENTRY_DELIMITER.join(entries)) if entries else 0

    @classmethod
    def _list_failure_route_paths(cls) -> List[Path]:
        routes_dir = cls._failure_routes_dir()
        if not routes_dir.exists():
            return []
        return sorted(
            [path for path in routes_dir.glob("*.md") if path.is_file()],
            key=lambda path: path.name.lower(),
        )

    def _reload_target(self, target: str) -> None:
        fresh = list(dict.fromkeys(self._read_file(self._path_for(target))))
        self._set_entries(target, fresh)

    def save_to_disk(self, target: str) -> None:
        get_memory_dir().mkdir(parents=True, exist_ok=True)
        self._write_file(self._path_for(target), self._entries_for(target))

    def _entries_for(self, target: str) -> List[str]:
        if target == "user":
            return self.user_entries
        if target == "failure":
            return self.failure_entries
        return self.memory_entries

    def _set_entries(self, target: str, entries: List[str]) -> None:
        if target == "user":
            self.user_entries = entries
        elif target == "failure":
            self.failure_entries = entries
        else:
            self.memory_entries = entries

    def _char_count(self, target: str) -> int:
        entries = self._entries_for(target)
        return len(ENTRY_DELIMITER.join(entries)) if entries else 0

    def _char_limit(self, target: str) -> int:
        if target == "user":
            return self.user_char_limit
        if target == "failure":
            return self.failure_char_limit
        return self.memory_char_limit

    def add(self, target: str, content: str, route_name: Optional[str] = None) -> Dict[str, Any]:
        """Append a new entry, evicting oldest failure entries when needed."""
        content = (content or "").strip()
        if not content:
            return {"success": False, "error": "Content cannot be empty."}

        scan_error = _scan_memory_content(content)
        if scan_error:
            return {"success": False, "error": scan_error}

        if target == "failure":
            return self._add_failure_entry(content, route_name=route_name)

        with self._file_lock(self._path_for(target)):
            self._reload_target(target)
            entries = self._entries_for(target)
            limit = self._char_limit(target)

            if content in entries:
                return self._success_response(target, "Entry already exists (no duplicate added).")

            new_entries = entries + [content]
            new_total = len(ENTRY_DELIMITER.join(new_entries))

            if new_total > limit:
                if target == "failure":
                    while new_entries and new_total > limit:
                        new_entries.pop(0)
                        new_total = len(ENTRY_DELIMITER.join(new_entries))
                    if not new_entries or new_total > limit:
                        current = self._char_count(target)
                        return {
                            "success": False,
                            "error": (
                                f"Failure memory at {current:,}/{limit:,} chars. "
                                f"Adding this entry ({len(content)} chars) still exceeds the limit "
                                "even after evicting older entries."
                            ),
                            "current_entries": entries,
                            "usage": f"{current:,}/{limit:,}",
                        }
                    entries = new_entries[:-1]
                else:
                    current = self._char_count(target)
                    return {
                        "success": False,
                        "error": (
                            f"Memory at {current:,}/{limit:,} chars. "
                            f"Adding this entry ({len(content)} chars) would exceed the limit. "
                            "Replace or remove existing entries first."
                        ),
                        "current_entries": entries,
                        "usage": f"{current:,}/{limit:,}",
                    }

            entries.append(content)
            self._set_entries(target, entries)
            self.save_to_disk(target)

        return self._success_response(target, "Entry added.")

    def add_structured(
        self,
        target: str,
        *,
        body: str,
        kind: str = "",
        name: str = "",
        description: str = "",
        tags: Optional[List[str]] = None,
        route_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Add a structured memory entry while staying backward compatible."""
        if target == "failure":
            route_hint = route_name or name or None
            return self.add(target, body, route_name=route_hint)
        return self.add(
            target,
            _format_structured_entry(
                body=body,
                kind=kind,
                name=name,
                description=description,
                tags=tags,
            ),
            route_name=route_name,
        )

    def replace(
        self,
        target: str,
        old_text: str,
        new_content: str,
        *,
        kind: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Any = None,
    ) -> Dict[str, Any]:
        """Replace the entry containing old_text with new_content."""
        old_text = (old_text or "").strip()
        new_content = (new_content or "").strip()
        if not old_text:
            return {"success": False, "error": "old_text cannot be empty."}
        if not new_content:
            return {
                "success": False,
                "error": "new_content cannot be empty. Use 'remove' to delete entries.",
            }

        scan_error = _scan_memory_content(new_content)
        if scan_error:
            return {"success": False, "error": scan_error}

        if target == "failure":
            return self._replace_failure_entry(old_text, new_content)

        with self._file_lock(self._path_for(target)):
            self._reload_target(target)
            entries = self._entries_for(target)
            matches = [
                (i, e)
                for i, e in enumerate(entries)
                if old_text in _structured_match_haystack(e)
            ]

            if not matches:
                return {"success": False, "error": f"No entry matched '{old_text}'."}
            if len(matches) > 1:
                unique_texts = {e for _, e in matches}
                if len(unique_texts) > 1:
                    previews = [_render_structured_entry_preview(e, max_chars=140) for _, e in matches]
                    return {
                        "success": False,
                        "error": f"Multiple entries matched '{old_text}'. Be more specific.",
                        "matches": previews,
                    }

            idx = matches[0][0]
            limit = self._char_limit(target)
            test_entries = entries.copy()
            existing = _parse_structured_entry(entries[idx])
            if any(value is not None for value in (kind, name, description, tags)):
                replacement = _format_structured_entry(
                    body=new_content,
                    kind=existing.get("kind", "") if kind is None else (kind or ""),
                    name=existing.get("name", "") if name is None else (name or ""),
                    description=existing.get("description", "") if description is None else (description or ""),
                    tags=existing.get("tags", []) if tags is None else _normalize_structured_tags(tags),
                )
            elif any(
                (
                    existing.get("kind"),
                    existing.get("name"),
                    existing.get("description"),
                    existing.get("tags"),
                )
            ):
                replacement = _format_structured_entry(
                    body=new_content,
                    kind=existing.get("kind", ""),
                    name=existing.get("name", ""),
                    description=existing.get("description", ""),
                    tags=existing.get("tags", []),
                )
            else:
                replacement = new_content
            test_entries[idx] = replacement
            new_total = len(ENTRY_DELIMITER.join(test_entries))

            if new_total > limit:
                return {
                    "success": False,
                    "error": (
                        f"Replacement would put memory at {new_total:,}/{limit:,} chars. "
                        "Shorten the new content or remove other entries first."
                    ),
                }

            entries[idx] = replacement
            self._set_entries(target, entries)
            self.save_to_disk(target)

        return self._success_response(target, "Entry replaced.")

    def remove(self, target: str, old_text: str) -> Dict[str, Any]:
        """Remove the entry containing old_text."""
        old_text = (old_text or "").strip()
        if not old_text:
            return {"success": False, "error": "old_text cannot be empty."}

        if target == "failure":
            return self._remove_failure_entry(old_text)

        with self._file_lock(self._path_for(target)):
            self._reload_target(target)
            entries = self._entries_for(target)
            matches = [
                (i, e)
                for i, e in enumerate(entries)
                if old_text in _structured_match_haystack(e)
            ]

            if not matches:
                return {"success": False, "error": f"No entry matched '{old_text}'."}
            if len(matches) > 1:
                unique_texts = {e for _, e in matches}
                if len(unique_texts) > 1:
                    previews = [_render_structured_entry_preview(e, max_chars=140) for _, e in matches]
                    return {
                        "success": False,
                        "error": f"Multiple entries matched '{old_text}'. Be more specific.",
                        "matches": previews,
                    }

            entries.pop(matches[0][0])
            self._set_entries(target, entries)
            self.save_to_disk(target)

        return self._success_response(target, "Entry removed.")

    def format_for_system_prompt(self, target: str) -> Optional[str]:
        """Return the frozen snapshot captured at load_from_disk()."""
        block = self._system_prompt_snapshot.get(target, "")
        return block if block else None

    @classmethod
    def _sanitize_failure_route_name(cls, text: str) -> str:
        raw = (text or "").strip().lower()
        if not raw:
            return "general-failed-route"
        raw = raw.replace("\\", "-").replace("/", "-")
        raw = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff._-]+", "-", raw)
        raw = re.sub(r"-{2,}", "-", raw).strip("-._")
        return raw[:80] or "general-failed-route"

    @classmethod
    def _derive_failure_route_name(
        cls,
        *,
        content: str,
        route_name: Optional[str] = None,
    ) -> str:
        if route_name and route_name.strip():
            return cls._sanitize_failure_route_name(route_name)
        terms = cls._failure_terms(content)
        if not terms:
            return "general-failed-route"
        preferred = terms[:6]
        return cls._sanitize_failure_route_name("-".join(preferred))

    @classmethod
    def _failure_route_keywords(cls, route_name: str, entries: List[str]) -> List[str]:
        source = " ".join([route_name] + list(entries[-3:]))
        return cls._failure_terms(source)[:12]

    @classmethod
    def _failure_route_tags(cls, route_name: str, entries: List[str]) -> List[str]:
        """Derive stable route tags from the route name and recent entries."""
        source = " ".join([route_name.replace("-", " ").replace("_", " ")] + list(entries[-3:]))
        return cls._failure_terms(source)[:8]

    @classmethod
    def _failure_route_description(cls, title: str, entries: List[str]) -> str:
        """Build a short one-line description for a failure route file."""
        for entry in reversed(entries):
            stripped = re.sub(r"\s+", " ", (entry or "").strip())
            if not stripped:
                continue
            if len(stripped) > 140:
                stripped = stripped[:140].rstrip() + "..."
            return stripped
        base = re.sub(r"\s+", " ", (title or "").strip())
        return f"Failure route for {base}" if base else "Failure route"

    @classmethod
    def _failure_route_path_for_name(cls, route_name: str) -> Path:
        return cls._failure_routes_dir() / f"{cls._sanitize_failure_route_name(route_name)}.md"

    @classmethod
    def _read_failure_route(cls, path: Path) -> Optional[Dict[str, Any]]:
        if not path.exists():
            return None
        try:
            raw = path.read_text(encoding="utf-8")
        except (OSError, IOError):
            return None
        if not raw.strip():
            return None

        title = path.stem
        keywords: List[str] = []
        tags: List[str] = []
        description = ""
        body = raw
        lines = raw.splitlines()
        if lines:
            first = lines[0].strip()
            if first.startswith("# "):
                title = first[2:].strip() or title
        for idx, line in enumerate(lines[1:], start=1):
            stripped = line.strip()
            if stripped.lower().startswith("keywords:"):
                keywords = [part.strip() for part in stripped.split(":", 1)[1].split(",") if part.strip()]
            elif stripped.lower().startswith("description:"):
                description = stripped.split(":", 1)[1].strip()
            elif stripped.lower().startswith("tags:"):
                tags = [part.strip() for part in stripped.split(":", 1)[1].split(",") if part.strip()]
            elif stripped == "---":
                body = "\n".join(lines[idx + 1 :])
                break
        entries = [entry.strip() for entry in body.split(ENTRY_DELIMITER) if entry.strip()]
        return {
            "path": path,
            "filename": path.name,
            "title": title,
            "description": description,
            "tags": tags,
            "keywords": keywords,
            "entries": entries,
        }

    @classmethod
    def _write_failure_route(
        cls,
        *,
        path: Path,
        title: str,
        entries: List[str],
    ) -> None:
        keywords = cls._failure_route_keywords(title, entries)
        tags = cls._failure_route_tags(title, entries)
        description = cls._failure_route_description(title, entries)
        header = [
            f"# {title}",
            f"Description: {description}" if description else "Description:",
            f"Tags: {', '.join(tags)}" if tags else "Tags:",
            f"Keywords: {', '.join(keywords)}" if keywords else "Keywords:",
            f"Updated: {datetime.now(timezone.utc).isoformat()}",
            "---",
        ]
        content = "\n".join(header)
        if entries:
            content += "\n" + ENTRY_DELIMITER.join(entries)
        cls._write_text_file(path, content)

    @classmethod
    def _write_text_file(cls, path: Path, content: str) -> None:
        try:
            fd, tmp_path = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp", prefix=".mem_")
            try:
                with os.fdopen(fd, "w", encoding="utf-8") as handle:
                    handle.write(content)
                    handle.flush()
                    os.fsync(handle.fileno())
                os.replace(tmp_path, str(path))
            except BaseException:
                try:
                    os.unlink(tmp_path)
                except OSError:
                    pass
                raise
        except (OSError, IOError) as exc:
            raise RuntimeError(f"Failed to write memory file {path}: {exc}") from exc

    def _add_failure_entry(self, content: str, route_name: Optional[str] = None) -> Dict[str, Any]:
        with self._file_lock(self._failure_routes_lock_path()):
            self._ensure_failure_routes_ready()
            routes = self._read_failure_routes_map()
            route_slug = self._derive_failure_route_name(content=content, route_name=route_name)
            path = self._failure_route_path_for_name(route_slug)
            route_title = route_slug.replace("-", " ")
            route = routes.get(path)
            existing_entries = list(route.get("entries", [])) if route else []
            if route:
                route_title = route.get("title") or route_title

            if content in existing_entries:
                self._reload_failure_routes()
                result = {
                    "success": True,
                    "route_file": path.name,
                    "entries": existing_entries,
                    "message": "Entry already exists (no duplicate added).",
                }
            else:
                route_entries_by_path = {
                    route_path: list(route_data.get("entries", []))
                    for route_path, route_data in routes.items()
                }
                current_entries = self._flatten_failure_entries_from_routes(route_entries_by_path)
                current_total = self._failure_total_chars_from_routes(route_entries_by_path)
                new_entries = existing_entries + [content]
                route_entries_by_path[path] = new_entries
                new_total = self._failure_total_chars_from_routes(route_entries_by_path)

                if new_total > self.failure_char_limit:
                    return {
                        "success": False,
                        "error": (
                            f"Failure memory at {current_total:,}/{self.failure_char_limit:,} chars. "
                            f"Adding this entry ({len(content)} chars) would exceed the limit. "
                            "Replace or remove existing failure entries first."
                        ),
                        "current_entries": current_entries,
                        "usage": f"{current_total:,}/{self.failure_char_limit:,}",
                    }

                self._write_failure_route(path=path, title=route_title, entries=new_entries)
                self._reload_failure_routes()
                result = {
                    "success": True,
                    "route_file": path.name,
                    "entries": new_entries,
                    "message": "Entry added.",
                }

        current = self._char_count("failure")
        limit = self._char_limit("failure")
        pct = min(100, int((current / limit) * 100)) if limit > 0 else 0
        result.update(
            {
                "target": "failure",
                "entries_rendered": [_render_structured_entry_preview(entry) for entry in self.failure_entries],
                "usage": f"{pct}% - {current:,}/{limit:,} chars",
                "entry_count": len(self.failure_entries),
            }
        )
        return result

    def _replace_failure_entry(self, old_text: str, new_content: str) -> Dict[str, Any]:
        with self._file_lock(self._failure_routes_lock_path()):
            self._ensure_failure_routes_ready()
            routes = self._read_failure_routes_map()
            matches = []
            for path, route in routes.items():
                for idx, entry in enumerate(route["entries"]):
                    if old_text in entry:
                        matches.append((path, route, idx, entry))
            if not matches:
                return {"success": False, "error": f"No entry matched '{old_text}'."}
            unique_entries = {entry for _, _, _, entry in matches}
            if len(matches) > 1 and len(unique_entries) > 1:
                previews = [entry[:80] + ("..." if len(entry) > 80 else "") for _, _, _, entry in matches]
                return {
                    "success": False,
                    "error": f"Multiple entries matched '{old_text}'. Be more specific.",
                    "matches": previews,
                }
            path, route, idx, _ = matches[0]
            route_entries_by_path = {
                route_path: list(route_data.get("entries", []))
                for route_path, route_data in routes.items()
            }
            entries = list(route["entries"])
            entries[idx] = new_content
            route_entries_by_path[path] = entries
            new_total = self._failure_total_chars_from_routes(route_entries_by_path)
            if new_total > self.failure_char_limit:
                current_total = self._failure_total_chars_from_routes(
                    {
                        route_path: list(route_data.get("entries", []))
                        for route_path, route_data in routes.items()
                    }
                )
                return {
                    "success": False,
                    "error": (
                        f"Replacement would put failure memory at {new_total:,}/{self.failure_char_limit:,} chars. "
                        "Shorten the new content or remove other failure entries first."
                    ),
                    "usage": f"{current_total:,}/{self.failure_char_limit:,}",
                }
            self._write_failure_route(path=path, title=route["title"], entries=entries)
            self._reload_failure_routes()
            return {
                "success": True,
                "target": "failure",
                "route_file": path.name,
                "entries": entries,
                "entries_rendered": [_render_structured_entry_preview(entry) for entry in entries],
                "message": "Entry replaced.",
                "usage": self._success_response("failure")["usage"],
                "entry_count": len(self.failure_entries),
            }

    def _remove_failure_entry(self, old_text: str) -> Dict[str, Any]:
        with self._file_lock(self._failure_routes_lock_path()):
            self._ensure_failure_routes_ready()
            routes = self._read_failure_routes_map()
            matches = []
            for path, route in routes.items():
                for idx, entry in enumerate(route["entries"]):
                    if old_text in entry:
                        matches.append((path, route, idx, entry))
            if not matches:
                return {"success": False, "error": f"No entry matched '{old_text}'."}
            unique_entries = {entry for _, _, _, entry in matches}
            if len(matches) > 1 and len(unique_entries) > 1:
                previews = [entry[:80] + ("..." if len(entry) > 80 else "") for _, _, _, entry in matches]
                return {
                    "success": False,
                    "error": f"Multiple entries matched '{old_text}'. Be more specific.",
                    "matches": previews,
                }
            path, route, idx, _ = matches[0]
            entries = list(route["entries"])
            entries.pop(idx)
            if entries:
                self._write_failure_route(path=path, title=route["title"], entries=entries)
            else:
                try:
                    path.unlink()
                except OSError:
                    pass
            self._reload_failure_routes()
            return {
                "success": True,
                "target": "failure",
                "route_file": path.name,
                "entries": entries,
                "entries_rendered": [_render_structured_entry_preview(entry) for entry in entries],
                "message": "Entry removed.",
                "usage": self._success_response("failure")["usage"],
                "entry_count": len(self.failure_entries),
            }

    @classmethod
    def _failure_terms(cls, text: str) -> List[str]:
        if not text:
            return []
        raw_terms = [match.group(0).lower() for match in cls._FAILURE_TOKEN_RE.finditer(text)]
        terms = []
        for term in raw_terms:
            if len(term) < 2 or term in cls._FAILURE_STOPWORDS:
                continue
            if term not in terms:
                terms.append(term)
        return terms[:40]

    @classmethod
    def _failure_match_score(cls, query: str, entry: str) -> Tuple[int, int]:
        query_terms = cls._failure_terms(query)
        if not query_terms or not entry:
            return 0, 0
        entry_lower = entry.lower()
        entry_terms = cls._failure_terms(entry)
        overlap = 0
        exact_bonus = 0
        for term in query_terms:
            if term in entry_lower:
                overlap += 1
                if len(term) >= 4:
                    exact_bonus += 1
                continue
            for entry_term in entry_terms:
                if term == entry_term:
                    overlap += 1
                    exact_bonus += 1
                    break
                if term in entry_term or entry_term in term:
                    overlap += 1
                    if len(entry_term) >= 2:
                        exact_bonus += 1
                    break
        return overlap + exact_bonus, exact_bonus

    @classmethod
    def _failure_route_name_score(cls, query: str, route_path: Path) -> Tuple[int, int]:
        route_name = route_path.stem.replace("-", " ").replace("_", " ")
        return cls._failure_match_score(query, route_name)

    @classmethod
    def _failure_route_score(cls, query: str, route: Dict[str, Any]) -> Tuple[int, int]:
        """Score a failure route using filename + route metadata."""
        filename_score, filename_exact = cls._failure_route_name_score(
            query,
            route.get("path") or cls._failure_route_path_for_name(route.get("filename", "")),
        )
        haystack = " ".join(
            part
            for part in (
                route.get("title", ""),
                route.get("description", ""),
                " ".join(route.get("tags", [])),
                " ".join(route.get("keywords", [])),
            )
            if part
        )
        meta_score, meta_exact = cls._failure_match_score(query, haystack)
        return filename_score + meta_score, filename_exact + meta_exact

    def match_failure_route_files(self, query: str, *, max_routes: int = 3) -> List[str]:
        """Return matched failure-route filenames using route metadata scoring."""
        if not query or not query.strip():
            return []
        route_hits = []
        for idx, route_path in enumerate(self._list_failure_route_paths()):
            route = self._read_failure_route(route_path)
            if not route:
                continue
            score, exact_bonus = self._failure_route_score(query, route)
            if score <= 0:
                continue
            route_hits.append((score, exact_bonus, idx, route_path.name))
        route_hits.sort(key=lambda item: (-item[0], -item[1], item[2]))
        return [name for _, _, _, name in route_hits[:max_routes]]

    def recall_relevant(
        self,
        query: str,
        *,
        include_memory: bool = True,
        include_user: bool = True,
        max_entries: int = 4,
        max_chars: int = 1200,
    ) -> str:
        """Return the most relevant built-in memory/user entries for *query*.

        Inspired by Aut's selective memory recall: keep the stable frozen
        system prompt for caching, but surface the most relevant memory facts
        again at API-call time so the current task gets a focused reminder.
        """
        if not query or not query.strip():
            return ""

        candidates = []
        order = 0

        def _append_candidates(entries: List[str], target: str, start_order: int) -> int:
            order = start_order
            for entry in entries:
                parsed = _parse_structured_entry(entry)
                haystack = _structured_match_haystack(entry)
                score, exact_bonus = self._failure_match_score(query, haystack)
                metadata_text = _structured_metadata_text(parsed)
                if metadata_text:
                    meta_score, meta_exact = self._failure_match_score(query, metadata_text)
                    score += meta_score
                    exact_bonus += meta_exact
                if score > 0:
                    candidates.append((score, exact_bonus, order, target, parsed))
                order += 1
            return order

        if include_memory:
            order = _append_candidates(self.memory_entries, "memory", order)
        if include_user:
            order = _append_candidates(self.user_entries, "user", order)

        if not candidates:
            return ""

        candidates.sort(key=lambda item: (-item[0], -item[1], item[2]))
        chosen = candidates[: max_entries * 2]

        labels = {
            "memory": "Relevant memory notes",
            "user": "Relevant user profile facts",
        }
        grouped: Dict[str, List[str]] = {"memory": [], "user": []}
        total_chars = 0
        emitted = 0

        for _, _, _, target, parsed in chosen:
            line_body = parsed.get("body", "").strip()
            line = f"- {line_body}"
            if parsed.get("name"):
                desc = parsed.get("description", "").strip()
                tags = parsed.get("tags", [])
                label = parsed["name"].strip()
                if desc:
                    label += f" — {desc}"
                if tags:
                    label += f" [tags: {', '.join(tags)}]"
                line = f"- {label}: {line_body}"
            if total_chars + len(line) > max_chars and emitted > 0:
                break
            grouped[target].append(line)
            total_chars += len(line)
            emitted += 1
            if emitted >= max_entries:
                break

        lines = []
        for target in ("user", "memory"):
            entries = grouped[target]
            if not entries:
                continue
            lines.append(labels[target])
            lines.extend(entries)

        return "\n".join(lines)

    def recall_failures(
        self,
        query: str,
        *,
        max_entries: int = 3,
        max_chars: int = 1400,
        max_routes: int = 3,
    ) -> str:
        """Return hard constraints from matched named failure-route files."""
        if not query or not query.strip():
            return ""
        matched_files = self.match_failure_route_files(query, max_routes=max_routes)
        if not matched_files:
            return ""
        chosen_routes = [self._failure_routes_dir() / name for name in matched_files]

        lines = [
            "FAILURE ROUTES (hard constraints from prior failed approaches)",
            "First matched route file names against the current task, then loaded only those files.",
            "If a matched route is listed below, skip that route unless you have materially new evidence that the old failure no longer applies.",
        ]
        total_chars = sum(len(line) for line in lines)
        emitted_entries = 0

        for route_path in chosen_routes:
            route = self._read_failure_route(route_path)
            if not route:
                continue
            route_entries = list(route["entries"])
            if not route_entries:
                continue
            route_header = f"Route file: {route['filename']}"
            if total_chars + len(route_header) > max_chars and emitted_entries > 0:
                break
            lines.append(route_header)
            total_chars += len(route_header)
            if route.get("description"):
                desc_line = f"Description: {route['description']}"
                if total_chars + len(desc_line) <= max_chars:
                    lines.append(desc_line)
                    total_chars += len(desc_line)
            if route.get("tags"):
                tags_line = f"Tags: {', '.join(route['tags'])}"
                if total_chars + len(tags_line) <= max_chars:
                    lines.append(tags_line)
                    total_chars += len(tags_line)

            for entry in reversed(route_entries):
                candidate = f"- {entry.strip()}"
                if total_chars + len(candidate) > max_chars and emitted_entries > 0:
                    break
                lines.append(candidate)
                total_chars += len(candidate)
                emitted_entries += 1
                if emitted_entries >= max_entries:
                    break

            if emitted_entries >= max_entries:
                break

        if emitted_entries == 0:
            return ""
        return "\n".join(lines)

    def _success_response(self, target: str, message: str = None) -> Dict[str, Any]:
        entries = self._entries_for(target)
        current = self._char_count(target)
        limit = self._char_limit(target)
        pct = min(100, int((current / limit) * 100)) if limit > 0 else 0

        resp = {
            "success": True,
            "target": target,
            "entries": entries,
            "entries_rendered": [_render_structured_entry_preview(entry) for entry in entries],
            "usage": f"{pct}% - {current:,}/{limit:,} chars",
            "entry_count": len(entries),
        }
        if message:
            resp["message"] = message
        return resp

    def _render_block(self, target: str, entries: List[str]) -> str:
        """Render a system-prompt block with header and usage indicator."""
        if not entries:
            return ""

        limit = self._char_limit(target)
        rendered_entries = [
            rendered
            for rendered in (_render_structured_entry_for_prompt(entry) for entry in entries)
            if rendered
        ]
        content = ENTRY_DELIMITER.join(rendered_entries)
        current = len(content)
        pct = min(100, int((current / limit) * 100)) if limit > 0 else 0

        if target == "user":
            header = f"USER PROFILE (who the user is) [{pct}% - {current:,}/{limit:,} chars]"
        elif target == "failure":
            header = (
                "FAILURE MEMORY (pitfalls and rejected approaches to avoid) "
                f"[{pct}% - {current:,}/{limit:,} chars]"
            )
        else:
            header = f"MEMORY (your personal notes) [{pct}% - {current:,}/{limit:,} chars]"

        separator = "~" * 46
        return f"{separator}\n{header}\n{separator}\n{content}"

    @staticmethod
    def _read_file(path: Path) -> List[str]:
        """Read a memory file and split it into entries."""
        if not path.exists():
            return []
        try:
            raw = path.read_text(encoding="utf-8")
        except (OSError, IOError):
            return []
        if not raw.strip():
            return []
        entries = [entry.strip() for entry in raw.split(ENTRY_DELIMITER)]
        return [entry for entry in entries if entry]

    @staticmethod
    def _write_file(path: Path, entries: List[str]) -> None:
        """Write entries using atomic temp-file + rename."""
        content = ENTRY_DELIMITER.join(entries) if entries else ""
        try:
            fd, tmp_path = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp", prefix=".mem_")
            try:
                with os.fdopen(fd, "w", encoding="utf-8") as handle:
                    handle.write(content)
                    handle.flush()
                    os.fsync(handle.fileno())
                os.replace(tmp_path, str(path))
            except BaseException:
                try:
                    os.unlink(tmp_path)
                except OSError:
                    pass
                raise
        except (OSError, IOError) as exc:
            raise RuntimeError(f"Failed to write memory file {path}: {exc}") from exc


def memory_tool(
    action: str,
    target: str = "memory",
    content: str = None,
    old_text: str = None,
    route_name: str = None,
    kind: str = None,
    name: str = None,
    description: str = None,
    tags: Any = None,
    store: Optional[MemoryStore] = None,
) -> str:
    """Single entry point for the memory tool."""
    if store is None:
        return tool_error(
            "Memory is not available. It may be disabled in config or this environment.",
            success=False,
        )

    if target not in ("memory", "user", "failure"):
        return tool_error(
            f"Invalid target '{target}'. Use 'memory', 'user', or 'failure'.",
            success=False,
        )

    if action == "add":
        if not content:
            return tool_error("Content is required for 'add' action.", success=False)
        if target == "failure":
            result = store.add(
                target,
                content,
                route_name=route_name or name,
            )
        elif kind or name or description or tags:
            result = store.add_structured(
                target,
                body=content,
                kind=kind or "",
                name=name or "",
                description=description or "",
                tags=_normalize_structured_tags(tags),
                route_name=route_name,
            )
        else:
            result = store.add(target, content, route_name=route_name)
    elif action == "replace":
        if not old_text:
            return tool_error("old_text is required for 'replace' action.", success=False)
        if not content:
            return tool_error("content is required for 'replace' action.", success=False)
        result = store.replace(
            target,
            old_text,
            content,
            kind=kind,
            name=name,
            description=description,
            tags=tags,
        )
    elif action == "remove":
        if not old_text:
            return tool_error("old_text is required for 'remove' action.", success=False)
        result = store.remove(target, old_text)
    else:
        return tool_error(
            f"Unknown action '{action}'. Use: add, replace, remove",
            success=False,
        )

    return json.dumps(result, ensure_ascii=False)


def check_memory_requirements() -> bool:
    """Memory tool has no external requirements."""
    return True


MEMORY_SCHEMA = {
    "name": "memory",
    "description": (
        "Save durable information to persistent memory that survives across sessions. "
        "Memory is injected into future turns, so keep it compact and focused on facts "
        "that will still matter later.\n\n"
        "WHEN TO SAVE (do this proactively, don't wait to be asked):\n"
        "- User corrects you or says 'remember this' / 'don't do that again'\n"
        "- User shares a preference, habit, or personal detail (name, role, timezone, coding style)\n"
        "- You discover something about the environment (OS, installed tools, project structure)\n"
        "- You learn a convention, API quirk, or workflow specific to this user's setup\n"
        "- You identify a stable fact that will be useful again in future sessions\n"
        "- You discover a rejected approach or dead-end that should be avoided next time\n\n"
        "PRIORITY: user preferences and corrections > environment facts > durable failure lessons. "
        "The most valuable memory prevents the user from having to repeat themselves or correct you again.\n\n"
        "Do NOT save task progress, session outcomes, completed-work logs, or temporary TODO state "
        "to memory; use session_search to recall those from past transcripts.\n"
        "If you've discovered a new way to do something, solved a problem that could be necessary later, "
        "save it as a skill with the skill tool.\n\n"
        "THREE TARGETS:\n"
        "- 'user': who the user is -- name, role, preferences, communication style, pet peeves\n"
        "- 'memory': your notes -- environment facts, project conventions, tool quirks, lessons learned\n"
        "- 'failure': rejected approaches, dead ends, and anti-patterns to avoid repeating later. "
        "These are stored in named markdown route files and should be treated as hard constraints "
        "when a similar route matches again.\n\n"
        "ACTIONS: add (new entry), replace (update existing -- old_text identifies it), "
        "remove (delete -- old_text identifies it).\n\n"
        "SKIP: trivial or obvious info, raw dumps, and temporary task state."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["add", "replace", "remove"],
                "description": "The action to perform.",
            },
            "target": {
                "type": "string",
                "enum": ["memory", "user", "failure"],
                "description": (
                    "Which store to update: 'memory' for personal notes, "
                    "'user' for the user profile, 'failure' for durable pitfalls to avoid."
                ),
            },
            "content": {
                "type": "string",
                "description": "The entry content. Required for 'add' and 'replace'.",
            },
            "old_text": {
                "type": "string",
                "description": "Short unique substring identifying the entry to replace or remove.",
            },
            "route_name": {
                "type": "string",
                "description": (
                    "Optional named failure route when target='failure'. "
                    "Used to choose the failure-route markdown filename."
                ),
            },
            "kind": {
                "type": "string",
                "description": "Optional structured memory type label for add, e.g. preference, environment, workflow, warning.",
            },
            "name": {
                "type": "string",
                "description": "Optional short structured title for add, used to improve future recall.",
            },
            "description": {
                "type": "string",
                "description": "Optional one-line summary for add, used to improve future recall.",
            },
            "tags": {
                "oneOf": [
                    {"type": "string"},
                    {"type": "array", "items": {"type": "string"}},
                ],
                "description": "Optional structured tags for add. Improves future recall and organization.",
            },
        },
        "required": ["action", "target"],
    },
}


from tools.registry import registry, tool_error


registry.register(
    name="memory",
    toolset="memory",
    schema=MEMORY_SCHEMA,
    handler=lambda args, **kw: memory_tool(
        action=args.get("action", ""),
        target=args.get("target", "memory"),
        content=args.get("content"),
        old_text=args.get("old_text"),
        route_name=args.get("route_name"),
        kind=args.get("kind"),
        name=args.get("name"),
        description=args.get("description"),
        tags=args.get("tags"),
        store=kw.get("store"),
    ),
    check_fn=check_memory_requirements,
    emoji="🧠",
)
