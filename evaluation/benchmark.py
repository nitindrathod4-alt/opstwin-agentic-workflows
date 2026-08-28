"""Benchmark report for the fixed incident set."""

from __future__ import annotations

import json
from pathlib import Path

from baseline.baseline_agent import diagnose
from evaluation.metrics import accuracy

ROOT = Path(__file__).parents[1]
CASES = ROOT / "data" / "incidents" / "cases.json"


def load_cases() -> list[dict[str, object]]:
    """Load the fixed benchmark cases."""
    return json.loads(CASES.read_text(encoding="utf-8"))


def run_baseline() -> dict[str, object]:
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    predictions = [diagnose(c["id"], c["text"]).root_cause for c in cases]
    expected = [c["expected_root_cause"] for c in cases]
    return {"name": "baseline", "accuracy": accuracy(predictions, expected), "total": len(cases)}


if __name__ == "__main__":
    print(json.dumps(run_baseline(), indent=2))
