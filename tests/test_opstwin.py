from agents.investigator import Hypothesis, investigate
from agents.reporter import render_report
from agents.verifier import verify_in_sandbox
from tools.evidence import Evidence
from tools.timeline import reconstruct_timeline


def test_timeline_is_reproducible():
    evidence = [
        Evidence("logs", "2026-01-01T00:02:00Z", "error", "second"),
        Evidence("deploy", "2026-01-01T00:01:00Z", "change", "first"),
    ]
    assert [x.detail for x in reconstruct_timeline(evidence)] == ["first", "second"]


def test_hypothesis_ranking_uses_counter_evidence():
    evidence = [
        Evidence("logs", "2026-01-01T00:01:00Z", "signal", "db pool", ("db_exhaustion",), ()),
        Evidence("metrics", "2026-01-01T00:02:00Z", "signal", "normal memory", (), ("memory_leak",)),
    ]
    results = investigate(evidence)
    assert results[0].root_cause == "db_exhaustion"


def test_verification_is_sandboxed_contract():
    result = verify_in_sandbox("db_exhaustion", lambda: True)
    assert result.passed is True


def test_report_is_auditable():
    report = render_report("INC-TEST", [Hypothesis("db_exhaustion", ["pool"], [], 1.0)])
    assert "INC-TEST" in report
    assert "db_exhaustion" in report


def test_strong_counter_evidence_can_overrule_weak_signal():
    evidence = [
        Evidence(
            "deploy",
            "2026-01-01T00:01:00Z",
            "change",
            "release completed successfully",
            ("deployment_regression",),
            ("deployment_regression",),
        ),
        Evidence(
            "metrics",
            "2026-01-01T00:02:00Z",
            "signal",
            "database connection pool exhausted",
            ("database_connection_exhaustion",),
            (),
        ),
    ]

    results = investigate(evidence)

    assert results[0].root_cause == "database_connection_exhaustion"
    assert results[0].score > results[1].score


def test_reliable_metrics_source_gets_higher_weight():
    evidence = [
        Evidence(
            "metrics",
            "2026-01-01T00:01:00Z",
            "signal",
            "memory usage increased",
            ("memory_leak",),
            (),
        ),
        Evidence(
            "unknown",
            "2026-01-01T00:02:00Z",
            "signal",
            "network timeout observed",
            ("network_timeout",),
            (),
        ),
    ]

    results = investigate(evidence)

    assert results[0].root_cause == "memory_leak"
    assert results[0].score > results[1].score


def test_tie_breaking_is_deterministic():
    evidence = [
        Evidence(
            "logs",
            "2026-01-01T00:01:00Z",
            "signal",
            "network signal",
            ("network_timeout",),
            (),
        ),
        Evidence(
            "logs",
            "2026-01-01T00:02:00Z",
            "signal",
            "memory signal",
            ("memory_leak",),
            (),
        ),
    ]

    first = investigate(evidence)
    second = investigate(evidence)

    assert [(h.root_cause, h.score) for h in first] == [
        (h.root_cause, h.score) for h in second
    ]


def test_multiple_supporting_signals_accumulate():
    evidence = [
        Evidence(
            "logs",
            "2026-01-01T00:01:00Z",
            "signal",
            "connection pool warning",
            ("database_connection_exhaustion",),
            (),
        ),
        Evidence(
            "metrics",
            "2026-01-01T00:02:00Z",
            "signal",
            "database connections exhausted",
            ("database_connection_exhaustion",),
            (),
        ),
    ]

    results = investigate(evidence)

    assert results[0].root_cause == "database_connection_exhaustion"
    assert len(results[0].supporting_evidence) == 2
    assert results[0].score > 2.0
