"""Evidence-driven investigator with weighted, auditable reasoning."""

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


SOURCE_WEIGHTS = {
    "metrics": 1.25,
    "logs": 1.15,
    "deploy": 1.10,
    "deployment": 1.10,
    "trace": 1.20,
    "alert": 1.00,
}


def _source_weight(source: str) -> float:
    return SOURCE_WEIGHTS.get(source.lower(), 1.0)


def investigate(evidence: list[Evidence]) -> list[Hypothesis]:
    """Rank hypotheses using evidence strength, source quality and contradictions."""

    timeline = reconstruct_timeline(evidence)
    candidates: dict[str, Hypothesis] = {}

    for item in timeline:
        weight = _source_weight(item.source)

        for cause in item.supports:
            current = candidates.get(
                cause,
                Hypothesis(cause, [], [], 0.0),
            )

            candidates[cause] = Hypothesis(
                cause,
                current.supporting_evidence + [item.detail],
                current.counter_evidence,
                current.score + weight,
            )

        for cause in item.contradicts:
            current = candidates.get(
                cause,
                Hypothesis(cause, [], [], 0.0),
            )

            candidates[cause] = Hypothesis(
                cause,
                current.supporting_evidence,
                current.counter_evidence + [item.detail],
                current.score - (0.90 * weight),
            )

    return sorted(
        candidates.values(),
        key=lambda h: (-h.score, h.root_cause),
    )
