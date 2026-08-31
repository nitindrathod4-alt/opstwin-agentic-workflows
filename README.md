# OpsTwin — Agentic Incident Investigation Platform

OpsTwin is an evidence-driven incident investigation platform designed to help engineers analyze incidents, compare competing root-cause hypotheses, verify conclusions in a deterministic sandbox, and preserve an auditable investigation trail.

> **Safety:** Simulation-only workflow. No production mutations are exposed.

## Demo

🎥 **Video Demo:** https://youtu.be/nqDnM9DVgZo

## Screenshots

### 1. Incident Command Center — Overview
The main command center provides incident selection, live analysis, diagnosis confidence, safety posture, incident timeline, and competing hypotheses.

![OpsTwin Overview](assets/01-overview.png)

### 2. Incident Timeline — Live Case View
Shows the investigation timeline with incident signals, evidence analysis, competing hypotheses, and sandbox verification.

![Incident Timeline](assets/02-timeline.png)

### 3. Evidence Explorer & Counterfactual Replay
Compare supporting and contradicting evidence, then remove evidence sources to test whether the diagnosis survives.

![Evidence Explorer and Counterfactual Replay](assets/03-evidence-replay.png)

### 4. Benchmark Performance
Displays baseline vs advanced accuracy, improvement, adversarial performance, and results across the fixed incident dataset.

![Benchmark Performance](assets/04-benchmark.png)

### 5. Audit Trail & Reproducible Report
Preserves evidence inspection, timestamps, competing hypotheses, counter-evidence, sandbox verification, human checkpoint, and generated incident report.

![Audit Trail and Report](assets/05-audit-report.png)

## Core Workflow

1. **Inspect** — Read incident evidence and constraints.
2. **Timeline** — Order events by timestamp and source.
3. **Compete** — Compare supporting and contradicting signals.
4. **Verify** — Use deterministic sandbox experiments.
5. **Report** — Preserve evidence, uncertainty, and decisions.

## Key Capabilities

- Evidence-driven incident diagnosis
- Competing root-cause hypotheses
- Supporting vs counter-evidence analysis
- Counterfactual evidence-removal replay
- Deterministic sandbox verification
- Baseline and advanced benchmark evaluation
- Adversarial test coverage
- Reproducible incident reports
- Auditable reasoning trail
- Human checkpoint before operational decisions
- Simulation-only safety posture

## Benchmark Snapshot

| Metric | Result |
|---|---:|
| Baseline accuracy | 80% |
| Advanced accuracy | 100% |
| Improvement | +20 percentage points |
| Adversarial performance | 100% |
| Fixed incidents | 10 |

## Safety & Auditability

OpsTwin is presented as a **safe simulation environment**. The workflow records evidence, verification, uncertainty, and decisions while keeping production mutation disabled.

## Project

**OpsTwin — Agentic Incident Investigation Platform**

Built around an agentic workflow for evidence-driven, reproducible incident investigation.
