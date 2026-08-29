# OpsTwin — Agentic Incident Investigation

> **Frontier Engineering Challenge 2026**

OpsTwin is an evidence-driven incident investigation system designed to evaluate whether an agent can reason through ambiguous software incidents, compare competing root-cause hypotheses, verify conclusions safely, and produce an auditable investigation trail.

The project deliberately separates a simple deterministic baseline from an advanced evidence-aware investigation workflow so that improvement can be **measured rather than claimed**.

---

## Executive Summary

Traditional incident automation often produces a plausible root cause from the first matching signal.

OpsTwin takes a different approach:

**collect evidence → reconstruct the timeline → generate competing hypotheses → weigh supporting and contradicting evidence → verify safely → replay counterfactuals → produce an auditable conclusion**

The system is simulation-first. It does not execute destructive production actions.

### Current measured result

| Evaluation | Baseline | Advanced |
|---|---:|---:|
| Fixed benchmark | 80% | **100%** |
| Adversarial benchmark | — | **100% (5/5)** |
| Absolute improvement | — | **+20 percentage points** |

All benchmark results are produced from the fixed synthetic datasets included in the repository.

---

## Why OpsTwin?

An incident diagnosis is not valuable merely because it sounds convincing.

A reliable investigation system should be able to answer:

- What evidence supports the diagnosis?
- What evidence contradicts it?
- Were competing hypotheses considered?
- Is the evidence ordered in time?
- Can the conclusion survive removal of important evidence?
- Was verification performed safely?
- Can another engineer reproduce the result?

OpsTwin treats these questions as first-class engineering requirements.

---

## System Architecture

```text
                    ┌──────────────────────┐
                    │   Incident / Case    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Evidence Collection  │
                    │ source + time + data  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Timeline Reconstruction│
                    └──────────┬───────────┘
                               │
                               ▼
                 ┌─────────────────────────────┐
                 │ Competing Hypothesis Engine │
                 │                             │
                 │ + Supporting evidence       │
                 │ - Contradicting evidence    │
                 │ + Evidence weighting        │
                 └──────────────┬──────────────┘
                                │
                     ┌──────────┴──────────┐
                     ▼                     ▼
            ┌─────────────────┐   ┌──────────────────┐
            │ Safe Verification│   │ Counterfactual  │
            │ / Sandbox        │   │ Replay          │
            └────────┬────────┘   └────────┬─────────┘
                     │                     │
                     └──────────┬──────────┘
                                ▼
                    ┌──────────────────────┐
                    │ Auditable Report     │
                    │ + Evidence Trail     │
                    └──────────────────────┘
