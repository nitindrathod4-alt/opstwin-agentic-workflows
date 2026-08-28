"""Run the same fixed dataset through baseline and advanced controls."""
from __future__ import annotations

import json

from baseline.baseline_agent import diagnose
from evaluation.advanced_agent import diagnose_advanced
from evaluation.benchmark import load_cases


def main() -> None:
    cases = load_cases()
    baseline_correct = 0
    advanced_correct = 0
    rows = []
    for case in cases:
        b = diagnose(case["id"], case["text"])
        a = diagnose_advanced(case["id"], case["text"])
        expected = case["expected_root_cause"]
        baseline_correct += b.root_cause == expected
        advanced_correct += a.root_cause == expected
        rows.append({"id": case["id"], "expected": expected, "baseline": b.root_cause, "advanced": a.root_cause})

    result = {
        "dataset_size": len(cases),
        "baseline_accuracy": baseline_correct / len(cases),
        "advanced_accuracy": advanced_correct / len(cases),
        "absolute_improvement": (advanced_correct - baseline_correct) / len(cases),
        "rows": rows,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
