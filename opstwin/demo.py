"""Small deterministic OpsTwin demo for local verification."""

from agents.investigator import investigate
from agents.reporter import render_report
from tools.evidence import Evidence
from agents.verifier import verify_in_sandbox


def main() -> None:
    evidence = [
        Evidence("deployments", "2026-08-29T10:01:00Z", "change", "Release v42 deployed", ("deployment_regression",), ()),
        Evidence("logs", "2026-08-29T10:03:00Z", "error", "5xx rate increased", ("deployment_regression",), ()),
        Evidence("metrics", "2026-08-29T10:04:00Z", "signal", "CPU remained normal", (), ("memory_leak",)),
    ]
    hypotheses = investigate(evidence)
    print(render_report("DEMO-001", hypotheses))
    if hypotheses:
        verification = verify_in_sandbox(hypotheses[0].root_cause, lambda: True)
        print(f"\nVerification: {verification.observation}")


if __name__ == "__main__":
    main()
