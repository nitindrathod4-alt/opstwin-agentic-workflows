"""Deterministic timeline reconstruction from incident evidence."""

from __future__ import annotations

from tools.evidence import Evidence


def reconstruct_timeline(evidence: list[Evidence]) -> list[Evidence]:
    """Return evidence ordered by timestamp for reproducible reasoning."""
    return sorted(evidence, key=lambda item: item.timestamp)
