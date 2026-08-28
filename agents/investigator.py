"""Evidence-driven investigator skeleton.

The policy is deliberately deterministic for the first milestone. A coding
agent/LLM can later be plugged in behind the same interface without changing
the evaluation contract.
"""

from __future__ import annotations

from dataclasses import dataclass

from tools.evidence import Evidence
from tools.timeline import reconstruct_timeline


@dataclass(frozen=True)
class Hypothesis:
    root_cause: str
    supporting_evidence: list[str]
    counter_evidence: list[str]
    score: float


def investigate(evidence: list[Evidence]) -> list[Hypothesis]:
    timeline = reconstruct_timeline(evidence)
    candidates: dict[str, Hypothesis] = {}
    for item in timeline:
        for cause in item.supports:
            current = candidates.get(cause, Hypothesis(cause, [], [], 0.0))
            candidates[cause] = Hypothesis(
                cause,
                current.supporting_evidence + [item.detail],
                current.counter_evidence,
                current.score + 1.0,
            )
        for cause in item.contradicts:
            current = candidates.get(cause, Hypothesis(cause, [], [], 0.0))
            candidates[cause] = Hypothesis(
                cause,
                current.supporting_evidence,
                current.counter_evidence + [item.detail],
                current.score - 0.75,
            )

    return sorted(candidates.values(), key=lambda h: h.score, reverse=True)
