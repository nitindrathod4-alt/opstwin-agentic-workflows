# OpsTwin Agent Policy

The coding agent must work in a sandbox and produce auditable artifacts.

## Required loop
1. Read the incident and constraints.
2. Collect or inspect permitted evidence.
3. Build a timestamped timeline.
4. Generate multiple plausible hypotheses.
5. Seek supporting and contradicting evidence.
6. Run safe verification experiments in simulation/sandbox.
7. Record human checkpoints for consequential decisions.
8. Produce a reproducible report with evidence references.

## Non-negotiable rules
- Never expose or commit secrets.
- Never perform destructive production actions.
- Use synthetic/public/approved data only.
- Do not claim an experiment passed without recorded evidence.
- Preserve representative agent trajectories for submission.
