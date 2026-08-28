from agents.replay import replay_without
from tools.evidence import Evidence


def test_counterfactual_replay_can_change_diagnosis():
    evidence = [
        Evidence("deploy", "2026-01-01T00:01:00Z", "signal", "release", ("deployment_regression",), ()),
        Evidence("db", "2026-01-01T00:02:00Z", "signal", "pool exhausted", ("database_connection_exhaustion",), ()),
    ]
    result = replay_without(evidence, 0)
    assert result.original_top == "deployment_regression"
    assert result.replay_top == "database_connection_exhaustion"
    assert result.diagnosis_changed is True
