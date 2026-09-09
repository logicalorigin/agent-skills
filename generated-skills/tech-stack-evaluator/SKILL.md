---
name: tech-stack-evaluator
description: Compare technologies or complete stacks using decision criteria such as fit, ecosystem, cost, security, operations, performance, and migration risk. Use for architecture choices, provider comparisons, TCO analysis, or migration decisions.
---

# Tech Stack Evaluator

Make the decision criteria and evidence visible before assigning scores or declaring a winner.

## Workflow

1. Frame the decision: workload, users, scale, team skills, existing stack, constraints, budget, timeline, compliance needs, and acceptable migration risk.
2. Identify the few criteria that can actually change the decision. Use user-supplied weights when available; otherwise state how priorities are being inferred.
3. Separate current evidence from assumptions and generic characteristics. Verify live pricing, release status, ecosystem health, vulnerabilities, and service capabilities when they materially affect the choice.
4. Compare options on the decision-critical criteria first; avoid giant feature matrices filled with irrelevant parity items.
5. Model TCO with ranges and explicit assumptions rather than false precision.
6. Evaluate security and compliance as requirements and control gaps, not certification claims.
7. For migrations, assess compatibility, data movement, rollout strategy, rollback, testing, organizational cost, and operational risk.
8. Perform sensitivity analysis when small changes in weights or assumptions could reverse the recommendation.

## Bundled resources

- `format_detector.py`, `stack_comparator.py`, `tco_calculator.py`
- `ecosystem_analyzer.py`, `security_assessor.py`, `migration_analyzer.py`, `report_generator.py`
- Sample inputs, `expected_output_comparison.json`, `README.md`, `HOW_TO_USE.md`

## Guardrails

- Never invent GitHub, package-download, CVE, pricing, benchmark, or market data.
- Do not present arbitrary normalized scores as objective fact.
- Avoid multi-year cost or viability certainty when the inputs are speculative.
- Do not claim a stack is compliant merely because it supports relevant controls.
- Prefer the simpler option when additional complexity does not buy a requirement the user values.

## Output

Return the recommendation, decisive criteria, evidence and assumptions, key tradeoffs, TCO or migration detail when relevant, sensitivity or confidence notes, and the conditions that would change the decision.
