---
name: hook-factory
description: Create or revise coding-agent hooks for tool, file, test, formatting, notification, or workflow events.
---

# Hook Factory

Create the narrowest hook that safely automates the requested event.

## Workflow

1. Identify the target environment, configuration scope, trigger event, matcher, and intended side effect.
2. Verify the current hook schema and event names when exact configuration compatibility matters; do not assume historical examples are still authoritative.
3. Choose the narrowest event and matcher that capture the intended workflow without firing on unrelated actions.
4. Implement minimal logic with explicit input handling, quoting, timeouts, idempotency where relevant, and clear blocking versus non-blocking behavior.
5. Validate the configuration and script before installation.
6. Test the exact trigger plus at least one non-trigger or failure case.
7. Install or modify live configuration only when the user's request authorizes it; otherwise return the generated files and installation instructions.

## Bundled resources

- `hook_factory.py`, `generator.py`, `validator.py`, `installer.py`
- `install-hook.sh`, `templates.json`
- `examples/` — reference implementations, not guaranteed current schemas.
- `README.md` — detailed background and usage notes.

## Guardrails

- Never log credentials, tokens, private file contents, or other secrets.
- Avoid automatic commit, push, deploy, delete, or other high-impact actions by default.
- Prevent recursive hook loops and repeated side effects.
- Make failure policy explicit; a formatting helper and a security gate should not fail the workflow the same way.
- Keep shell commands narrowly scoped and safely quoted.
- Do not install hooks globally when project scope is sufficient.

## Output

Return the hook configuration and supporting script when needed, plus trigger scope, side effects, failure behavior, validation result, and installation status.
