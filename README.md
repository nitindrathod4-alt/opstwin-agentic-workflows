# OpsTwin — Agentic Incident Investigation Platform

> **Evidence-driven diagnosis with an auditable reasoning trail.**

OpsTwin is an agentic incident investigation platform for analyzing simulated production incidents. It inspects evidence, builds a timeline, compares competing root-cause hypotheses, verifies conclusions in a deterministic sandbox, and preserves an auditable investigation trail.

**Safety:** Simulation-only workflow. No production-changing actions are exposed.

## Project Structure & Where to Find Things

```text
opstwin-agentic-workflows/
├── agents/                 # Agent definitions and investigation workflow logic
├── baseline/               # Baseline investigation workflow used for comparison
├── evaluation/             # Benchmark, adversarial, and evaluation logic
├── frontend/               # Web interface / demo UI
├── data/                   # Incident datasets and supporting evidence
├── tests/                  # Automated tests
├── tools/                  # Supporting tools used by the investigation workflow
├── submission/             # Hackathon results, traces, and submission artifacts
│   ├── trajectories/       # Investigation traces / agent trajectories
│   ├── benchmark_result.json
│   ├── adversarial_result.json
│   └── counterfactual_result.txt
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration
└── README.md               # Project documentation
```

### What goes where

- **`agents/`** — Main agentic investigation components. Start here to understand how the agents reason over incident evidence.
- **`baseline/`** — Simpler baseline workflow used to compare performance against the advanced approach.
- **`evaluation/`** — Evaluation and scoring logic for measuring investigation quality.
- **`frontend/`** — User-facing interface used to interact with the project and demonstrate the workflow.
- **`data/`** — Incident inputs, evidence, and datasets used by the system.
- **`tests/`** — Tests that validate the project behaviour and investigation components.
- **`tools/`** — Reusable helper tools used during investigation and verification.
- **`submission/`** — Final evaluation outputs and audit/tracing artifacts prepared for the hackathon submission.
- **`requirements.txt`** — Packages required to install and run the Python components.
- **`pytest.ini`** — Configuration for running the test suite.

## Core Investigation Workflow

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
| Baseline accuracy | **80%** |
| Advanced accuracy | **100%** |
| Improvement | **+20 percentage points** |
| Adversarial performance | **100%** |
| Fixed incidents | **10** |

## Safety & Auditability

OpsTwin is designed as a **safe simulation environment**. Evidence, verification, uncertainty, and decisions are recorded for auditability while production mutation remains disabled.

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the test suite:

```bash
pytest
```

For the web demonstration, use the application entry point and instructions provided in `frontend/`.

## Hackathon Submission

The `submission/` directory contains the evaluation outputs and investigation traces used to demonstrate the agentic workflow and its results.

**OpsTwin — Agentic Incident Investigation Platform**
