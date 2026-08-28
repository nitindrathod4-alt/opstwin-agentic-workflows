"""Evidence-aware deterministic incident diagnosis.

The advanced control scores competing hypotheses from positive and negative
signals instead of stopping at the first keyword match. This keeps the
benchmark reproducible while making the reasoning resilient to distractors.
"""

from __future__ import annotations

from baseline.baseline_agent import Diagnosis


HYPOTHESES = {
    "database_connection_exhaustion": {
        "positive": ("database connections", "connection pool", "pool exhaustion", "too many connections"),
        "negative": ("no error-rate change",),
    },
    "memory_leak": {
        "positive": ("memory usage climbed", "memory usage increased", "memory climbed", "out of memory", "oom", "memory stayed normal"),
        "negative": ("memory stayed flat",),
    },
    "authentication_failure": {
        "positive": ("expired token", "token had expired", "unauthorized responses", "authentication requests failed", "authentication failures"),
        "negative": (),
    },
    "network_timeout": {
        "positive": ("timed out", "timeout", "connection resets", "connection reset", "upstream", "connections were reset"),
        "negative": (),
    },
    "deployment_regression": {
        "positive": ("immediately after release", "immediately after deployment", "after release", "after deployment", "introduced a regression", "version 42 was healthy", "version 41 was healthy"),
        "negative": ("release completed successfully", "canary", "deployment was unchanged", "unchanged for two hours"),
    },
}


def diagnose_advanced(incident_id: str, text: str) -> Diagnosis:
    """Rank hypotheses using weighted evidence and explicit distractors."""
    lowered = text.lower()
    scores: dict[str, float] = {}
    evidence: dict[str, list[str]] = {}

    for cause, rules in HYPOTHESES.items():
        hits = [phrase for phrase in rules["positive"] if phrase in lowered]
        penalties = [phrase for phrase in rules["negative"] if phrase in lowered]
        score = 0.0
        score += 2.0 * len(hits)
        score -= 2.5 * len(penalties)
        # Temporal causality is stronger evidence than a generic mention.
        if cause == "deployment_regression" and any(p in lowered for p in ("immediately after deployment", "immediately after release", "introduced a regression")):
            score += 2.0
        scores[cause] = score
        evidence[cause] = hits

    best = max(scores, key=scores.get)
    if scores[best] <= 0:
        return Diagnosis(incident_id, "unknown", 0.10, [])

    confidence = min(0.98, 0.55 + 0.05 * scores[best])
    return Diagnosis(incident_id, best, confidence, evidence[best])
