---
name: content-trend-researcher
description: Research current content trends and audience signals to prioritize timely topics, platform angles, and evidence-backed outlines.
---

# Content Trend Researcher

Turn current evidence into useful content decisions without fabricating popularity signals.

## Workflow

1. Define the audience, platforms, objective, geography if relevant, and freshness window.
2. Gather current evidence when live sources are available. Record dates and distinguish observed signals from durable patterns or hypotheses.
3. Identify themes, questions, narratives, and formats that repeat across credible evidence.
4. Score or prioritize opportunities based on relevance, evidence strength, novelty, brand fit, and execution feasibility—not invented search volume or engagement.
5. Use the bundled analyzers when structured input is available; treat their scores as decision aids rather than objective truth.
6. Convert the strongest opportunities into angles or outlines tied to audience intent and the available evidence.
7. Flag weak evidence, conflicting signals, stale data, and topics whose momentum cannot be verified.

## Bundled resources

- `intent_analyzer.py` — classify audience and topic intent.
- `trend_analyzer.py` — structure trend evidence.
- `platform_insights.py` — organize platform-specific observations.
- `outline_generator.py` — convert selected opportunities into outlines.
- `sample_input.json`, `expected_output.json`, `HOW_TO_USE.md`.

## Guardrails

- Never invent search volume, ranking, engagement, virality, or platform data.
- Do not present old examples as current trends.
- Separate evidence from interpretation and prediction.
- Prefer a few well-supported opportunities over a long speculative list.
- Treat platform differences as meaningful; do not assume one platform's signal transfers directly to another.

## Output

Return prioritized themes or topics, supporting evidence and freshness, recommended angles, optional outlines, and the main uncertainties or data gaps.
