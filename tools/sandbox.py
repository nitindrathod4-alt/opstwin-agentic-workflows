"""Safe, deterministic simulation environment.

Only in-memory state is supported. This is intentionally not an execution
interface for production infrastructure.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Sandbox:
    state: dict[str, str] = field(default_factory=dict)

    def set_state(self, key: str, value: str) -> None:
        self.state[key] = value

    def get_state(self, key: str) -> str | None:
        return self.state.get(key)

    def simulate(self, key: str, expected: str) -> bool:
        return self.state.get(key) == expected
