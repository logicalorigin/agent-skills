---
name: social-media-analyzer
description: Analyze supplied social-media campaign and content metrics across platforms, including engagement, traffic, cost efficiency, ROI inputs, audience patterns, and test opportunities. Use for performance reviews and campaign optimization.
---

# Social Media Analyzer

Turn supplied campaign data into comparable metrics and testable recommendations.

## Workflow

1. Identify the platforms, date range, campaign objectives, paid versus organic scope, and available metrics.
2. Normalize metric definitions before comparing periods or platforms. Do not assume similarly named metrics are calculated identically everywhere.
3. Calculate engagement, traffic, spend, conversion, or return metrics only when the required inputs exist.
4. Compare against the user's own baseline or a clearly identified external benchmark. Label missing denominators and incomplete attribution.
5. Identify patterns by content type, audience, timing, creative, or campaign segment while considering sample size and confounders.
6. Convert the strongest findings into prioritized tests or operational changes with a measurable success criterion.

## Bundled resources

- `calculate_metrics.py` — core metric calculations.
- `analyze_performance.py` — performance analysis and recommendation support.
- `sample_input.json`, `expected_output.json`, `HOW_TO_USE.md`.

## Guardrails

- Never invent impressions, reach, conversions, spend, follower counts, attribution, or benchmark data.
- Do not infer causality from correlation alone.
- Keep paid and organic performance separate unless the analysis explicitly models both.
- Avoid cross-platform ranking when metrics or objectives are not comparable.
- State when ROI cannot be calculated because revenue or conversion value is missing.

## Output

Return key metrics, strongest findings, material data-quality caveats, and prioritized tests or actions tied to the campaign objective.
