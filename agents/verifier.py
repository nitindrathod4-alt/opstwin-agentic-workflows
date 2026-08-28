"""Safe verification contract for sandbox-only experiments."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class VerificationResult:
    hypothesis: str
    passed: bool
    observation: str


def verify_in_sandbox(hypothesis: str, experiment: Callable[[], bool]) -> VerificationResult:
    """Run a supplied simulation and return an auditable verification result.

    Production changes are intentionally not supported by this interface.
    """
    passed = bool(experiment())
    return VerificationResult(
        hypothesis=hypothesis,
        passed=passed,
        observation="sandbox experiment passed" if passed else "sandbox experiment failed",
    )
