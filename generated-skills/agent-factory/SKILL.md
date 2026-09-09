---
name: agent-factory
description: Design or revise focused coding-agent and subagent definitions for a specific repository or workflow. Use for agent responsibilities, prompts, tool access, permissions, and static delegation boundaries. Do not use to supervise or orchestrate an active subagent workflow.
---

# Agent Factory

Create the smallest useful agent definition for the requested job.

## Workflow

1. Inspect the target project's existing agent conventions before choosing a schema, location, or supported fields.
2. Restate the agent's responsibility as one outcome. Split unrelated responsibilities instead of creating a broad do-everything agent.
3. Define when the agent should be used and when the parent agent should work directly.
4. Give the agent only the tools and permissions needed for that responsibility. Prefer read-only access unless edits or external actions are required.
5. Write a concise prompt covering objective, relevant context, decision rules, output contract, and high-impact constraints.
6. Reuse repository conventions. Do not invent frontmatter fields, tool names, model identifiers, orchestration settings, or capabilities the target environment does not support.
7. Validate the generated definition and report the final path plus material assumptions.

## Bundled resources

- `agent_generator.py` — generate an agent definition from structured input.
- `sample_input.json` and `expected_output.json` — generator contract examples.
- `generated-agents/software-architect.md` — example output, not a universal template.
- `HOW_TO_USE.md` — detailed usage notes.

## Guardrails

- This is a design-time skill. Runtime decomposition, assignment, monitoring, escalation, and integration of subagent work belong to `agent-supervision`.
- Avoid delegation for trivial, single-step work.
- Do not hard-code model names or platform-specific fields unless the target project already uses them or current documentation confirms them.
- Treat tool access, shell execution, network actions, and writes as explicit capabilities.
- Prefer behavior and success criteria over persona, slogans, or long expertise lists.
- If multiple agents are useful, define non-overlapping ownership and a clear handoff rather than relying on arbitrary parallelism limits.

## Output

Return the agent definition or exact changes, followed by a short rationale covering responsibility, tools, trigger conditions, and residual risks.