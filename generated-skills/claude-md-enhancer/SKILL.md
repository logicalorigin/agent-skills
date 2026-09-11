---
name: claude-md-enhancer
description: Audit or rewrite repository instruction files such as CLAUDE.md to remove stale, conflicting, duplicated, or overbroad guidance.
---

# Project Instructions Enhancer

Make project instructions easier for coding agents to follow without turning them into a second README.

## Workflow

1. Locate the instruction hierarchy and determine which files apply at repository, package, or directory scope.
2. Separate durable project facts and commands from generic coding advice, prose, historical notes, and duplicated documentation.
3. Identify conflicts, stale paths, unsupported commands, contradictory rules, and instructions that are too broad for their scope.
4. Preserve project-specific invariants: architecture boundaries, build and test commands, generated-file rules, security constraints, deployment restrictions, and conventions that materially affect correctness.
5. Rewrite for direct execution: short sections, concrete commands, narrow conditions, and explicit exceptions where needed.
6. Move deep explanations or examples to supporting documentation when the target environment supports progressive disclosure.
7. Validate referenced paths, scripts, package commands, and important assumptions where practical before finalizing.

## Bundled resources

- `analyzer.py` — inspect instruction quality and structure.
- `generator.py` — generate revised instruction content.
- `template_selector.py` — choose a suitable structure.
- `validator.py` — validate generated instructions.
- `workflow.py` — orchestrate the analysis and generation flow.
- `examples/`, `README.md`, `HOW_TO_USE.md` — supporting examples and usage notes.

## Guardrails

- Do not invent commands, dependencies, directory structure, or repository policy.
- Do not expose or copy secrets into instruction files.
- Reserve strong imperative language for actual invariants, safety constraints, and workflow requirements.
- Do not overwrite a useful existing structure merely to match a template.
- Prefer local, scoped instructions over globally repeating rules that only apply to one subsystem.

## Output

Return the revised instructions or exact patch, then summarize removed redundancy, resolved conflicts, preserved invariants, and any facts that still require verification.
