---
name: scrum-master-agent
description: Analyze sprint and backlog data for blockers, dependencies, WIP, goal risk, delivery health, and next actions.
---

# Scrum Master Agent

Use delivery data to improve flow and decision-making, not to manufacture productivity scores.

## Workflow

1. Identify the source system, team scope, sprint or time window, stated sprint goal, and the decision the analysis should support.
2. Normalize issue data and distinguish committed work, added scope, blocked work, dependencies, and completed work.
3. Surface the constraints that threaten the goal: blockers, excessive WIP, aging work, dependency queues, unclear ownership, or unstable scope.
4. Calculate available metrics as signals, not verdicts. Explain important assumptions and missing data.
5. Prioritize backlog or next actions using business value, risk, dependency order, effort, and goal alignment; do not rely on a single score when tradeoffs matter.
6. Recommend the smallest actions likely to improve flow or unblock delivery.
7. Mutate tickets, send notifications, or publish updates only when the user requested those actions and the integration supports them.

## Bundled resources

- `parse_input.py`, `detect_context.py`, `calculate_metrics.py`
- `prioritize_backlog.py`, `tool_adapters.py`, `format_output.py`, `notify_channels.py`
- `config.example.yaml`, sample inputs, `expected_output.json`, `README.md`, `HOW_TO_USE.md`

## Guardrails

- Do not use velocity, story points, ticket counts, or cycle time to rank individual people.
- Do not treat estimates as promises or metric movement as proof of causality.
- Distinguish team process problems from missing product decisions or external dependencies.
- Avoid changing priorities or issue state automatically unless the requested workflow authorizes it.
- Prefer actionable blocker removal over generic Scrum ceremony advice.

## Output

Return goal status, material blockers and flow risks, relevant metrics with context, prioritized actions, and uncertainties that could change the recommendation.
