"""Evaluate the baseline on the fixed synthetic incident set."""

from __future__ import annotations

import json
from pathlib import Path

from baseline.baseline_agent import diagnose


CASES = Path(__file__).parents[1] / "data" / "incidents" / "cases.json"


def main() -> None:
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    correct = 0
    for case in cases:
        result = diagnose(case["id"], case["text"])
        ok = result.root_cause == case["expected_root_cause"]
        correct += int(ok)
        print(f'{case["id"]}: predicted={result.root_cause} expected={case["expected_root_cause"]} correct={ok}')

    accuracy = correct / len(cases) if cases else 0.0
    print(f"\nBaseline accuracy: {correct}/{len(cases)} = {accuracy:.1%}")


if __name__ == "__main__":
    main()
