---
name: codex-cli-bridge
description: Translate repository context and coding tasks into safe Codex CLI workflows, including AGENTS.md generation, command construction, execution planning, and result handoff. Use when bridging project instructions or tasks to Codex CLI.
---

# Codex CLI Bridge

Preserve the user's task and repository constraints while translating them into the target CLI's current interface.

## Workflow

1. Inspect the repository structure and existing instruction files before generating bridge context.
2. Extract only task-relevant project rules, commands, architecture constraints, and file boundaries.
3. Generate or update `AGENTS.md` only when it improves the target workflow; avoid copying entire documentation sets into it.
4. Construct the smallest command or execution plan that satisfies the request.
5. Verify installed CLI capabilities and current syntax before relying on model names, flags, approval modes, or configuration fields that may have changed.
6. Apply safety checks before execution: working directory, write scope, shell commands, network actions, and destructive operations.
7. Execute only when the user requested execution; otherwise return a ready-to-run plan or command.
8. Capture the result, changed files, failures, and unresolved assumptions for handoff.

## Bundled resources

- `bridge.py`, `project_analyzer.py`, `claude_parser.py`
- `agents_md_generator.py`, `codex_executor.py`, `safety_mechanism.py`
- `skill_documenter.py`, `sample_input.json`, `expected_output.json`
- `README.md`, `HOW_TO_USE.md`, `INSTALL.md`

## Guardrails

- Do not hard-code model identifiers or CLI flags without confirming the target version.
- Do not weaken repository instructions during translation.
- Avoid destructive shell commands or broad write scopes unless the task requires them.
- Never place credentials or secrets in generated commands or instruction files.
- Keep bridge context concise enough that task-specific instructions remain prominent.

## Output

Provide the command or execution result, affected files, safety scope, and any compatibility assumptions that should be checked.
