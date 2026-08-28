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
