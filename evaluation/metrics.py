"""Metrics shared by baseline and advanced solutions."""

from __future__ import annotations


def accuracy(predictions: list[str], expected: list[str]) -> float:
    if not expected or len(predictions) != len(expected):
        return 0.0
    return sum(p == e for p, e in zip(predictions, expected)) / len(expected)


def improvement(baseline: float, advanced: float) -> float:
    return advanced - baseline


def robustness_score(stable_replays: int, total_replays: int) -> float:
    return stable_replays / total_replays if total_replays else 0.0
