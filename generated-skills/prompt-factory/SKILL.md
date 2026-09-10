---
name: prompt-factory
description: Create or optimize reusable prompts when goals, inputs, constraints, outputs, examples, or tool instructions need refinement.
---

# Prompt Factory

Produce the shortest prompt that reliably communicates the real task.

## Workflow

1. Extract the task goal, intended user or runtime, available inputs, required output, constraints, and definition of success.
2. Remove requirements that are merely stylistic ceremony unless they materially improve the target task.
3. Build the prompt around: objective, necessary context, inputs, decision rules, constraints, output contract, and evaluation criteria.
4. Mention tools, files, APIs, models, or capabilities only when they actually exist in the target environment.
5. Add examples only when they resolve ambiguity or demonstrate a difficult boundary condition; do not use examples as filler.
6. Make uncertainty behavior explicit when factual accuracy, external evidence, or missing information matters.
7. Run optimization or validation when useful, then remove duplicated instructions, conflicting rules, unnecessary persona language, and excessive emphasis.
8. Test mentally or with available tooling against the normal case, an edge case, and a failure or missing-input case.

## Bundled resources

- `scripts/generate_prompt.py` — structured prompt generation.
- `scripts/optimizer.py` — prompt reduction and refinement.
- `scripts/validator.py` — structural validation.
- `scripts/batch_generator.py` — batch generation.
- `templates/presets/` — domain-specific starting points; adapt rather than copy blindly.
- `references/best-practices-reference.md`, `README.md`, `HOW_TO_USE.md` — supporting material.

## Guardrails

- Do not invent expertise, permissions, tools, data access, or unsupported model features.
- Do not request hidden chain-of-thought. Ask for conclusions, evidence, checks, assumptions, or concise rationale instead.
- Avoid repetitive MUST/CRITICAL language unless a true safety or correctness constraint warrants it.
- Keep hard requirements distinct from preferences and optional heuristics.
- Preserve the user's actual objective when shortening an existing prompt.
- Prefer task-specific decision rules over generic advice such as “be thorough” or “act as an expert.”

## Output

Return the finished prompt first. Add only a short note on key assumptions, deliberate omissions, or validation findings when they materially help reuse.
