"""OpsTwin agent orchestration pipeline.

The orchestrator keeps investigation stages explicit and auditable so an LLM
coding agent can be used for reasoning without hiding the engineering loop.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from agents.investigator import Hypothesis, investigate
from agents.reporter import render_report
from tools.evidence import Evidence
from tools.timeline import reconstruct_timeline


@dataclass(frozen=True)
class InvestigationResult:
    incident_id: str
    timeline: list[Evidence]
    hypotheses: list[Hypothesis]
    report: str


def run_investigation(incident_id: str, evidence: Sequence[Evidence]) -> InvestigationResult:
    timeline = reconstruct_timeline(list(evidence))
    hypotheses = investigate(timeline)
    report = render_report(incident_id, hypotheses)
    return InvestigationResult(incident_id, timeline, hypotheses, report)
