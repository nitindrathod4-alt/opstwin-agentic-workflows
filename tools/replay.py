"""Incident replay and counterfactual evidence analysis."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence

from tools.evidence import Evidence


@dataclass(frozen=True)
class ReplayResult:
    scenario: str
    diagnosis: str
    confidence: float
    removed_evidence: tuple[str, ...]


def replay(
    scenario: str,
    evidence: Sequence[Evidence],
    diagnose: Callable[[list[Evidence]], tuple[str, float]],
    remove_sources: Sequence[str] = (),
) -> ReplayResult:
    """Re-run diagnosis after removing selected evidence sources.

    This is a simulation-only experiment. It never mutates production systems.
    """
    removed = tuple(sorted(set(remove_sources)))
    remaining = [item for item in evidence if item.source not in removed]
    diagnosis, confidence = diagnose(remaining)
    return ReplayResult(scenario, diagnosis, confidence, removed)
