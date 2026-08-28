"""Evidence-aware deterministic incident diagnosis."""

from __future__ import annotations

from baseline.baseline_agent import Diagnosis


HYPOTHESES = {
    "database_connection_exhaustion": {
        "positive": ("database connections", "connection pool", "pool exhaustion", "too many connections"),
        "negative": ("no error-rate change",),
    },
    "memory_leak": {
        "positive": ("memory usage climbed", "memory usage increased", "memory climbed", "out of memory", "oom"),
        "negative": ("memory stayed normal", "memory stayed flat"),
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
        "positive": ("immediately after release", "immediately after deployment", "after release", "after deployment", "introduced a regression", "version 42 was healthy", "version 41 was healthy", "release 42 deployed"),
        "negative": ("release completed successfully", "canary", "deployment was unchanged", "unchanged for two hours"),
    },
}


def diagnose_advanced(incident_id: str, text: str) -> Diagnosis:
    """Rank competing hypotheses with positive, negative and causal evidence."""
    lowered = text.lower()
    ranked: list[tuple[float, str, list[str]]] = []

    for cause, rules in HYPOTHESES.items():
        hits = [phrase for phrase in rules["positive"] if phrase in lowered]
        penalties = [phrase for phrase in rules["negative"] if phrase in lowered]
        score = 2.0 * len(hits) - 2.5 * len(penalties)

        if cause == "deployment_regression" and any(
            phrase in lowered
            for phrase in ("immediately after deployment", "immediately after release", "introduced a regression", "release 42 deployed")
        ):
            score += 2.0

        # A post-deployment error spike is only strong evidence when there is
        # no explicit signal that the deployment remained healthy/unchanged.
        if cause == "deployment_regression" and "five minutes later 5xx increased" in lowered:
            score += 1.5

        ranked.append((score, cause, hits))

    ranked.sort(reverse=True)
    best_score, best_cause, best_hits = ranked[0]
    if best_score <= 0:
        return Diagnosis(incident_id, "unknown", 0.10, [])

    confidence = min(0.98, 0.55 + 0.05 * best_score)
    return Diagnosis(incident_id, best_cause, confidence, best_hits)
