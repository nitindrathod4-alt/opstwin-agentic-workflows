"""Provider-neutral interface for an optional coding/LLM agent.

The competition requires agent use, but the core evaluator must remain
reproducible. This adapter keeps model calls outside deterministic scoring.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Sequence

from tools.evidence import Evidence


class AgentProvider(Protocol):
    def reason(self, prompt: str) -> str: ...


@dataclass(frozen=True)
class AgentSuggestion:
    hypothesis: str
    rationale: str
    evidence_queries: tuple[str, ...]


def request_suggestion(provider: AgentProvider, incident: str, evidence: Sequence[Evidence]) -> AgentSuggestion:
    evidence_text = "\n".join(f"[{x.timestamp}] {x.source}: {x.detail}" for x in evidence)
    prompt = (
        "Analyze this synthetic incident. Propose one falsifiable root-cause hypothesis, "
        "explain the evidence, and list concrete evidence queries that could disprove it. "
        "Do not recommend production actions.\n\n"
        f"Incident: {incident}\nEvidence:\n{evidence_text}"
    )
    rationale = provider.reason(prompt)
    return AgentSuggestion("agent_generated", rationale, ("logs", "metrics", "deployments"))
