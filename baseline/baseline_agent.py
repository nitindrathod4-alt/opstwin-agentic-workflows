"""Deterministic baseline incident diagnosis.

This intentionally simple baseline uses keyword matching only. The advanced
agent will be evaluated against the exact same incident cases.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Diagnosis:
    incident_id: str
    root_cause: str
    confidence: float
    evidence: list[str]


RULES = [
    ("database_connection_exhaustion", ("connection pool", "too many connections", "db connection")),
    ("memory_leak", ("out of memory", "oom", "memory usage")),
    ("deployment_regression", ("deployment", "release", "version")),
    ("network_timeout", ("timeout", "connection reset", "upstream")),
    ("authentication_failure", ("unauthorized", "authentication", "token expired")),
]


def diagnose(incident_id: str, text: str) -> Diagnosis:
    lowered = text.lower()
    for cause, keywords in RULES:
        hits = [keyword for keyword in keywords if keyword in lowered]
        if hits:
            return Diagnosis(incident_id, cause, 0.60, hits)
    return Diagnosis(incident_id, "unknown", 0.10, [])


if __name__ == "__main__":
    sample = "API latency increased after deployment and upstream requests timeout."
    print(diagnose("demo-001", sample))
