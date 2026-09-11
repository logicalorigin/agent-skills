---
name: slash-command-factory
description: Create or revise a coding-assistant slash command for one repeatable workflow, including arguments, tool scope, and validation.
---

# Slash Command Factory

Create one command for one clear job using the target environment's current supported mechanism.

## Workflow

1. Identify the target coding assistant or CLI and the command's single intended outcome.
2. Verify the current command mechanism, file location, frontmatter, argument syntax, and supported tools when compatibility matters; do not force a legacy format onto a newer environment.
3. Define the minimum required inputs or arguments and a clear output contract.
4. Choose the smallest valid command structure and include only supported metadata.
5. Add repository context, file references, shell commands, or subagent delegation only when necessary to complete the job.
6. Scope executable commands narrowly and make destructive or external actions explicit.
7. Generate the command file, validate syntax and naming, then test a representative invocation and one missing-input or edge case.
8. Return installation or placement instructions appropriate to the verified target environment.

## Bundled resources

- `command_generator.py` — command generation.
- `validator.py` — command validation.
- `presets.json` — reusable starting points, not authoritative platform documentation.
- `sample_input.json`, `expected_output.json`, `HOW_TO_USE.md`.

## Guardrails

- Do not invent frontmatter fields, tool names, model identifiers, or argument features.
- Avoid unrestricted shell access when narrower commands are sufficient.
- Never embed credentials or secrets.
- Do not make deploy, delete, commit, push, or other high-impact actions implicit defaults.
- If a reusable skill is a better fit than a command wrapper, say so instead of forcing the workflow into command syntax.

## Output

Return the ready-to-use command, its intended location, inputs, allowed side effects, validation result, and any target-version assumptions.
