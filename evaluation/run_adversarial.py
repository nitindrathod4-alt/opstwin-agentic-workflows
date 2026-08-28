"""Run the advanced control against adversarial cases."""
from __future__ import annotations

import json
from pathlib import Path

from evaluation.advanced_agent import diagnose_advanced

ROOT = Path(__file__).parents[1]
CASES = ROOT / "evaluation" / "adversarial_cases.json"


def main() -> None:
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    correct = 0
    rows = []
    for case in cases:
        prediction = diagnose_advanced(case["id"], case["text"])
        ok = prediction.root_cause == case["expected_root_cause"]
        correct += int(ok)
        rows.append({"id": case["id"], "expected": case["expected_root_cause"], "predicted": prediction.root_cause, "correct": ok})
    result = {
        "dataset_size": len(cases),
        "correct": correct,
        "accuracy": correct / len(cases) if cases else 0.0,
        "rows": rows,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
