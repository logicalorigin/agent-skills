---
name: semantic-clarifier
description: Distinguish naming, formatting, convention, and representation differences from changes that affect behavior, correctness, architecture, security, performance, compatibility, or user-visible outcomes. Use during code review, refactors, migrations, API or schema work, cross-repo comparisons, and legacy-code analysis.
---

# Semantic Clarifier

Focus effort on substantive invariants without ignoring semantics that actually carry contractual meaning.

## Workflow

1. Restate the task behaviorally: what must remain true or become true?
2. Classify each disputed detail:
   - **Semantic-only** — naming, formatting, equivalent representation, or convention with no downstream effect.
   - **Behavioral** — changes runtime behavior, data shape or flow, side effects, errors, security, performance, compatibility, or user experience.
   - **Mixed** — appears cosmetic but participates in an external contract, reflection, serialization, generated code, schema, query, routing, policy, or tooling.
3. Preserve semantic-only differences unless consistency is a stated requirement or the difference materially increases maintenance or correctness risk.
4. Analyze substantive invariants first: inputs and outputs, state transitions, ownership, data flow, failure modes, security boundaries, performance constraints, compatibility, migrations, and rollback.
5. Verify mixed cases before dismissing them. Search usages and contracts rather than arguing from naming alone.
6. Test behavior and interfaces. Prefer assertions about observable outcomes over exact internal phrasing or representation unless that representation is the contract.
7. Keep the change scoped. Do not turn a fix, review, or migration into broad cleanup merely because nearby semantics differ.
8. Summarize substantive changes or risks, semantic-only differences intentionally left alone, and mixed or uncertain items that still need verification.

## Decision rules

- If two forms are behaviorally equivalent and both are valid in context, do not block progress on preference.
- If a name, string, key, path, field, or identifier is consumed outside the local code, treat it as potentially behavioral until verified.
- If a convention affects generated artifacts, API compatibility, schema evolution, security policy, build tooling, or operational workflows, it is not just semantics.
- If evidence is incomplete, state the uncertainty and inspect the narrowest relevant contract or usage.
- If a difference only changes how a correct solution is expressed, preserve the working form unless changing it materially improves clarity or future safety.

## Guardrails

- Do not use “semantic” as a reason to ignore readability when readability affects correctness or future change safety.
- Do not enforce consistency for its own sake across a large or legacy codebase.
- Do not rewrite stable interfaces merely to align vocabulary.
- Do not assume a cosmetic-looking string is harmless in reflective, dynamic, serialized, generated, or configuration-heavy systems.
- Prefer minimal changes that satisfy the behavioral goal and preserve compatibility.

## Output

Lead with the substantive conclusion. Then identify semantic-only items and any remaining contract-sensitive uncertainty.
