<div align="center">

# 🧠 OpsTwin
### Agentic Incident Investigation Platform

**Evidence-driven diagnosis • Hypothesis competition • Sandbox verification • Auditability**

<p>
  <img src="https://img.shields.io/badge/AI-Agentic%20Workflows-7C3AED?style=for-the-badge&logo=sparkles&logoColor=white" />
  <img src="https://img.shields.io/badge/Incident%20Investigation-06B6D4?style=for-the-badge&logo=opsgenie&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.x-2563EB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Simulation%20Only-EC4899?style=for-the-badge&logo=shield&logoColor=white" />
</p>

<p>
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-product-flow">Product Flow</a> •
  <a href="#-benchmark">Benchmark</a> •
  <a href="#-tech-stack">Tech Stack</a>
</p>

</div>

---

## ✨ What is OpsTwin?

**OpsTwin** is an agentic incident investigation platform built to reason about **simulated production incidents** using an evidence-first workflow.

Instead of jumping directly to a root cause, OpsTwin follows a structured investigation loop:

> **Inspect → Timeline → Compete → Verify → Report**

The platform can analyze incident evidence, rank competing root-cause hypotheses, challenge its own diagnosis with counter-evidence, verify conclusions in a sandbox, replay counterfactual scenarios, and preserve the full investigation trail.

> 🛡️ **Safety boundary:** OpsTwin is designed for simulation and evaluation. No production mutations are exposed.

---

## 🤖 Core Capabilities

| Capability | What it does |
|---|---|
| 🔎 **Evidence Explorer** | Inspects logs, signals, constraints and investigation evidence |
| 🕒 **Timeline Reconstruction** | Organizes incident events into a causal sequence |
| 🧠 **Hypothesis Competition** | Compares multiple root-cause candidates instead of assuming one answer |
| ⚔️ **Counter-Evidence** | Actively looks for evidence that could disprove a hypothesis |
| 🧪 **Sandbox Verification** | Tests conclusions in a deterministic, isolated environment |
| 🔁 **Counterfactual Replay** | Explores what could change under alternative conditions |
| 📊 **Benchmarking** | Measures baseline, advanced and adversarial performance |
| 🧾 **Audit Trail** | Preserves investigation steps for review and reproduction |

---

## 🧭 Product Flow

```text
                    ┌──────────────────────┐
                    │   📥 Incident Input   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │   🔎 Inspect Evidence │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │   🕒 Build Timeline   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ 🧠 Compete Hypotheses │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │   🧪 Verify in        │
                    │      Sandbox          │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │   📋 Generate Report  │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    🧾 Audit Trail     │
                    └──────────────────────┘

              ↺ Counterfactual Replay feeds back
                into hypothesis evaluation.
```

---

## 🖥️ Product Screens

### 01 · Overview — Incident Command Center

<p align="center">
  <img src="assets/opstwin-5-panels.jpg" alt="OpsTwin Overview Dashboard" width="100%">
</p>

The overview brings the complete investigation into one command-center experience, including incident analysis, accuracy metrics, safety posture, timeline, and competing hypotheses.

### 02 · Investigation — Evidence-First Diagnosis

<p align="center">
  <img src="assets/opstwin-5-panels.jpg" alt="OpsTwin Investigation View" width="100%">
</p>

The investigation workspace focuses on supporting evidence, counter-evidence, hypothesis ranking, verification, and the final investigation report.

### 03 · Benchmark — Reproducible Evaluation

<p align="center">
  <img src="assets/opstwin-5-panels.jpg" alt="OpsTwin Benchmark View" width="100%">
</p>

The benchmark workspace compares OpsTwin against a fixed incident set and surfaces measurable evaluation results.

### 04 · Baseline vs Advanced

<p align="center">
  <img src="assets/opstwin-5-panels.jpg" alt="OpsTwin Baseline versus Advanced" width="100%">
</p>

This view highlights the impact of the advanced agentic workflow across diagnosis quality, evidence handling, verification, and adversarial evaluation.

### 05 · Audit Trail — Explainable Investigation History

<p align="center">
  <img src="assets/opstwin-5-panels.jpg" alt="OpsTwin Audit Trail" width="100%">
</p>

The audit layer captures evidence inspection, timeline reconstruction, hypothesis competition, verification, human checkpoints, and diagnosis comparisons.

---

## 📊 Benchmark

OpsTwin is evaluated across **10 fixed incidents** with baseline, advanced and adversarial measurements.

| Metric | Result |
|---|---:|
| Baseline accuracy | **80%** |
| Advanced accuracy | **100%** |
| Improvement | **+20 percentage points** |
| Adversarial evaluation | **100% — 5/5 passed** |
| Fixed incidents | **10** |

### Why the advanced workflow matters

The goal is not simply to produce an answer. The advanced workflow makes the reasoning process more disciplined by introducing **competing hypotheses, counter-evidence, sandbox verification and reproducible audit artifacts**.

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[📥 Incident Evidence] --> B[🔎 Inspect]
    B --> C[🕒 Timeline]
    C --> D[🧠 Competing Hypotheses]
    D --> E[🧪 Sandbox Verification]
    E --> F[📋 Investigation Report]
    F --> G[🧾 Audit Trail]
    D --> H[🔁 Counterfactual Replay]
    H --> D
    I[📊 Benchmark] --> D
    I --> E
```

---

## 🧩 Engineering Principles

### 🔍 Evidence over assumptions
Every diagnosis is grounded in available incident evidence and explicit constraints.

### 🧠 Competing explanations
The workflow keeps multiple hypotheses in play instead of immediately locking onto the first plausible root cause.

### 🧪 Verify before concluding
Sandbox experiments help validate whether the proposed explanation is consistent with the observed behavior.

### 🧾 Make the reasoning auditable
Investigation steps and artifacts are preserved so the path from evidence to conclusion can be inspected later.

### 🛡️ Safety by design
The experience clearly separates simulation from real production operations and avoids exposing production mutation capabilities.

---

## 🧰 Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-2563EB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />
</p>

**Engineering areas:**

- Agentic investigation workflows
- Evidence analysis
- Root-cause hypothesis ranking
- Deterministic sandbox verification
- Counterfactual replay
- Benchmark & adversarial evaluation
- Audit / trajectory artifacts
- Automated testing
- CI with GitHub Actions

---

## 📂 Project Structure

```text
opstwin-agentic-workflows/
├── 🤖 agents/                 # Agentic investigation components
├── 📏 baseline/               # Baseline diagnosis workflow
├── 📊 evaluation/             # Benchmarks and evaluation logic
├── 🖥️ frontend/               # Web interface
├── 📁 data/incidents/         # Fixed incident scenarios
├── 🛠️ tools/                  # Supporting utilities
├── 🏆 submission/              # Challenge submission artifacts
├── 🖼️ assets/                 # Product screenshots and visuals
├── 🧪 tests/                  # Automated tests
├── 📦 requirements.txt        # Python dependencies
└── 📖 README.md
```

---

## 🚀 Quick Start

### 1. Clone

```bash
git clone https://github.com/nitindrathod4-alt/opstwin-agentic-workflows.git
cd opstwin-agentic-workflows
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run tests

```bash
pytest
```

### 4. Open the web application

```text
frontend/index.html
```

---

## 🏆 Built for micro1 Frontier Engineering Challenge 2026

OpsTwin was built for the **micro1 Frontier Engineering Challenge 2026** with a focus on reliable agentic engineering.

> **Reliable incident intelligence is not just about generating a diagnosis — it is about evidence, competing hypotheses, verification, reproducibility, safety, and auditability.**

---

## 👨‍💻 Author

<div align="center">

### Nitin Rathod
**DevOps / Cloud Engineer • AWS • Linux • Automation**

<a href="https://github.com/nitindrathod4-alt">
  <img src="https://img.shields.io/badge/GitHub-nitindrathod4--alt-18181B?style=for-the-badge&logo=github&logoColor=white" />
</a>

<br><br>

**🚀 Build • Investigate • Verify • Learn**

</div>
