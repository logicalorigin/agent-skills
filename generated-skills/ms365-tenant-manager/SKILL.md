---
name: ms365-tenant-manager
description: Plan, generate, or review Microsoft 365 tenant administration workflows for users, groups, licensing, configuration, and PowerShell automation. Use for tenant setup, bulk administration, change scripts, or administrative audits.
---

# Microsoft 365 Tenant Manager

Make tenant administration explicit, reviewable, and least-privileged.

## Workflow

1. Identify the tenant scope, requested outcome, affected users or resources, required permissions, and whether the task is read-only or mutating.
2. Inspect current state or provided exports before proposing broad changes when the information is available.
3. Verify current module and cmdlet availability when exact PowerShell behavior matters; cloud administration interfaces change over time.
4. Generate a preview or dry-run plan before destructive, bulk, licensing, membership, or policy changes.
5. Use least privilege and scope operations to the smallest necessary set of objects.
6. For changes that can affect access or service availability, include rollback, recovery, or reconciliation steps where possible.
7. Execute only when the user explicitly wants changes applied and the required environment or authorization exists.
8. Report successes, skips, failures, and items requiring manual review.

## Bundled resources

- `tenant_setup.py` — tenant setup planning and generation.
- `user_management.py` — user administration workflows.
- `powershell_generator.py` — PowerShell generation.
- `sample_input.json`, `expected_output.json`, `HOW_TO_USE.md`.

## Guardrails

- Never embed credentials, refresh tokens, client secrets, or private keys in generated scripts.
- Do not assume admin roles or permissions the operator has not confirmed.
- Separate reporting from mutation so an audit cannot silently become a change operation.
- Avoid broad delete, disable, license removal, or policy replacement without explicit scope.
- Treat compliance and security recommendations as guidance, not certification.

## Output

Return the plan or script, affected scope, permissions required, rollback or recovery notes when relevant, and validation or execution results.
