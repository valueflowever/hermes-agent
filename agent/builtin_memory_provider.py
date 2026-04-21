"""Compatibility shim for the built-in memory provider.

Historically the built-in provider lived in ``agent.builtin_memory_provider``.
The provider abstraction was later simplified, but some call sites and tests
still import the old module path.  Keep this lightweight shim so the built-in
provider remains addressable without reintroducing a heavier backend.
"""

from __future__ import annotations

from typing import Any, Dict, List

from agent.memory_provider import MemoryProvider


class BuiltinMemoryProvider(MemoryProvider):
    """Minimal built-in provider placeholder used by MemoryManager.

    Hermes' file-backed built-in memory is handled elsewhere; this provider
    mainly preserves provider ordering and initialization semantics.
    """

    @property
    def name(self) -> str:
        return "builtin"

    def is_available(self) -> bool:
        return True

    def initialize(self, session_id: str, **kwargs) -> None:
        self._session_id = session_id
        self._init_kwargs = dict(kwargs)

    def get_tool_schemas(self) -> List[Dict[str, Any]]:
        return []

