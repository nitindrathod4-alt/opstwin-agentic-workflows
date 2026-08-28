"""Demonstrate how evidence removal can change or preserve a diagnosis."""

from __future__ import annotations

from agents.investigator import investigate
from tools.evidence import Evidence
from tools.replay import replay


def diagnose(evidence: list[Evidence]) -> tuple[str, float]:
    hypotheses = investigate(evidence)
    if not hypotheses:
        return "unknown", 0.0
    top = hypotheses[0]
    return top.root_cause, max(0.0, min(1.0, top.score / 3.0))


def main() -> None:
    evidence = [
        Evidence("deployment", "2026-08-29T10:01:00Z", "change", "v42 deployed", ("deployment_regression",), ()),
        Evidence("logs", "2026-08-29T10:03:00Z", "error", "5xx increased", ("deployment_regression",), ()),
        Evidence("metrics", "2026-08-29T10:04:00Z", "signal", "memory normal", (), ("memory_leak",)),
    ]
    for removed in ((), ("deployment",), ("logs",)):
        result = replay("DEMO-001", evidence, diagnose, removed)
        print(result)


if __name__ == "__main__":
    main()
