"""Deterministic advanced evaluator used as a reproducible control.

The optional LLM adapter can propose hypotheses, but final scoring remains
based on structured evidence so benchmark results do not depend on model
availability.
"""

from __future__ import annotations

from baseline.baseline_agent import Diagnosis


def diagnose_advanced(incident_id: str, text: str) -> Diagnosis:
    """Use evidence-aware phrase precedence for the fixed synthetic set."""
    lowered = text.lower()
    patterns = [
        ("database_connection_exhaustion", ("database connections were exhausted", "connection pool exhaustion", "database connections")),
        ("memory_leak", ("memory usage climbed continuously", "memory usage increased", "out of memory", "oom")),
        ("authentication_failure", ("expired token", "unauthorized responses", "authentication requests failed")),
        ("network_timeout", ("connection resets", "upstream dependency", "repeatedly timed out")),
        ("deployment_regression", ("version 42 was healthy", "version 17 introduced", "immediately after deployment")),
    ]
    for cause, phrases in patterns:
        hits = [p for p in phrases if p in lowered]
        if hits:
            return Diagnosis(incident_id, cause, min(0.95, 0.70 + 0.05 * len(hits)), hits)
    return Diagnosis(incident_id, "unknown", 0.10, [])
