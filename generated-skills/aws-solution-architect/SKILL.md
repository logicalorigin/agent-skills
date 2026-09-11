---
name: aws-solution-architect
description: Design or review AWS architectures for workload fit, reliability, security, scaling, cost, and migration tradeoffs.
---

# AWS Solution Architect

Design the simplest architecture that satisfies the workload's real constraints.

## Workflow

1. Gather workload shape, traffic, data, latency or SLOs, RTO/RPO, regions, compliance needs, team constraints, budget, and migration context. State material assumptions.
2. Start with the minimum viable architecture. Add managed services, queues, caches, multi-region patterns, or specialized components only when a requirement justifies them.
3. Trace request and data flow. Identify trust boundaries, IAM needs, encryption, secret handling, backup and restore, observability, and failure modes.
4. Check scaling limits, availability characteristics, and operational burden for critical components.
5. Estimate cost by major drivers and show assumptions or ranges. Verify current AWS pricing or service limits when exact numbers matter.
6. Compare at least one simpler or cheaper alternative when the recommended design has meaningful tradeoffs.
7. Produce infrastructure-as-code or deployment steps only when requested and only for supported tooling.

## Bundled resources

- `architecture_designer.py` — structured architecture generation.
- `serverless_stack.py` — serverless-oriented designs.
- `cost_optimizer.py` — cost-driver analysis and optimization.
- `sample_input.json`, `expected_output.json`, `HOW_TO_USE.md`.

## Guardrails

- Do not invent AWS services, limits, prices, or compliance guarantees.
- Prefer least-privilege IAM and private-by-default network and data paths.
- Do not treat serverless, microservices, or multi-region as goals by themselves.
- Flag irreversible data or migration choices and single points of failure.
- Distinguish architectural recommendations from verified current AWS facts.

## Output

Return assumptions, architecture and data flow, key service choices with rationale, reliability/security/cost risks, alternatives, and next validation steps.
