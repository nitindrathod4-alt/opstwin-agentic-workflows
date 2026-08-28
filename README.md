# OpsTwin — Evidence-Driven AI Incident Investigator

OpsTwin is a hackathon project for investigating software incidents using agentic workflows. It is designed around evidence, competing hypotheses, verification, reproducibility, and measurable improvement.

## Competition approach

We will build two versions against the same evaluation cases:

1. **Baseline** — a simple incident diagnosis workflow.
2. **Advanced** — evidence collection, timeline reconstruction, competing hypotheses, counter-evidence, sandbox verification, and structured reporting.

No production systems or destructive actions are used. Evaluation data will be synthetic/public and consequential actions remain simulated or require human approval.

## Status

🚧 Initial scaffold. Baseline and evaluation harness are the first implementation targets.

## Planned structure

```text
opstwin/
├── agents/
├── tools/
├── data/
│   ├── incidents/
│   └── scenarios/
├── baseline/
├── evaluation/
├── tests/
├── README.md
├── CHANGELOG.md
└── requirements.txt
```

## Reproducibility

Commands and dependency versions will be added as the implementation stabilizes. Secrets must never be committed to the repository.

## License / competition note

This repository is being developed for the micro1 Frontier Engineering Challenge 2026. Pre-existing components, if any, will be clearly identified separately from competition-created work.
