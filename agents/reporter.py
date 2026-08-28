"""Structured incident report generation."""

from __future__ import annotations

from agents.investigator import Hypothesis


def render_report(incident_id: str, hypotheses: list[Hypothesis]) -> str:
    lines = [f"# OpsTwin Incident Report — {incident_id}", "", "## Ranked hypotheses"]
    for index, hypothesis in enumerate(hypotheses, start=1):
        lines.append(f"{index}. **{hypothesis.root_cause}** — score {hypothesis.score:.2f}")
        lines.append(f"   - Supporting evidence: {len(hypothesis.supporting_evidence)}")
        lines.append(f"   - Counter-evidence: {len(hypothesis.counter_evidence)}")
    return "\n".join(lines)
