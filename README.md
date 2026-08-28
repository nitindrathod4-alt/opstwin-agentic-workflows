# OpsTwin — Agentic Incident Investigation

> **Frontier Engineering Challenge 2026**

OpsTwin is an evidence-driven incident investigation system designed to show what happens when a coding agent reasons about an ambiguous software incident rather than merely generating code.

## Core idea

OpsTwin separates a simple keyword baseline from an advanced, auditable investigation loop:

```text
Incident → Evidence → Timeline → Competing hypotheses
                         ↓
              Supporting + contradicting evidence
                         ↓
                 Sandbox verification / replay
                         ↓
                 Reproducible incident report
```

The system is simulation-first and does not execute destructive production actions.

## Baseline vs Advanced

**Baseline:** deterministic keyword matching.

**Advanced:** explicit orchestration, timestamped evidence, competing hypotheses, counter-evidence, safe verification, incident replay and counterfactual analysis.

Both versions use the same fixed synthetic dataset so improvement can be measured rather than claimed.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m evaluation.evaluate_baseline
python -m opstwin.demo
pytest -q
```

## Agent-use policy

Coding-agent use is required by the competition. The investigation loop is documented in `agents/agent_policy.md`. Representative agent trajectories should be preserved separately from secrets and included in the final archive as required by the challenge.

## Dataset

`data/incidents/cases.json` contains synthetic evaluation cases. Existing benchmark cases should not be changed after measurement without recording a dataset-version change in `CHANGELOG.md`.

## Reproducibility

A clean environment must be able to run the baseline, advanced demo and tests using the commands above. Results should be recorded with the exact dataset and dependency versions used.

## Improvement Changelog

See `CHANGELOG.md` for iteration-by-iteration decisions and evidence.

## Main failure mode

The system can become overconfident when evidence is sparse, correlated or misleading. Counter-evidence and reproducible verification are therefore first-class signals.

## Hot take

**The strongest incident agent is not the one that guesses the root cause fastest; it is the one that can show why its conclusion survived attempts to disprove it.**

## Competition note

Pre-existing components and competition-created work should be clearly identified in the final submission. Never commit credentials or private information.
