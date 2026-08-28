"""Incident replay and counterfactual analysis.

This module simulates removal of one evidence item at a time. It never changes
production state and helps answer: which evidence actually drove the diagnosis?
"""

from __future__ import annotations

from dataclasses import dataclass

from agents.investigator import Hypothesis, investigate
from tools.evidence import Evidence


@dataclass(frozen=True)
class Counterfactual:
    removed_evidence: str
    original_top: str | None
    replay_top: str | None
    diagnosis_changed: bool


def replay_without(evidence: list[Evidence], index: int) -> Counterfactual:
    original = investigate(evidence)
    modified = evidence[:index] + evidence[index + 1 :]
    replayed = investigate(modified)
    original_top = original[0].root_cause if original else None
    replay_top = replayed[0].root_cause if replayed else None
    return Counterfactual(
        removed_evidence=evidence[index].detail,
        original_top=original_top,
        replay_top=replay_top,
        diagnosis_changed=original_top != replay_top,
    )


def replay_all(evidence: list[Evidence]) -> list[Counterfactual]:
    return [replay_without(evidence, i) for i in range(len(evidence))]
