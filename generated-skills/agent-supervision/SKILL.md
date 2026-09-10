---
name: agent-supervision
description: Supervise subagents directly controlled by the current parent agent for runtime delegation, escalation, verification, and integration. Not peer/terminal agents.
---

# Agent Supervision

Use intelligence where ambiguity is expensive; use cheaper execution where the work is already understood.

## Scope

This skill applies only when the current agent is the **parent/supervisor** of subagents and remains responsible for the final result.

It is not a multi-terminal coordinator, peer-agent protocol, external-agent bridge, or general project-management skill. For creating or revising agent definitions, use `agent-factory` instead.

## Operating Model

Use a **diagnose -> dispatch -> verify** loop.

1. **Diagnose minimally.** Before delegation, resolve only the uncertainty needed to choose a safe plan: the real problem, relevant constraints, dependencies, risk, and success criteria. Do not explore broadly when the task is already obvious.
2. **Spend capability on judgment.** When the runtime supports model or effort selection, use a higher-capability reasoning tier for ambiguous diagnosis, architecture, decomposition, migrations, security-sensitive choices, cross-cutting changes, conflict resolution, and failed assumptions.
3. **Dispatch bounded execution downward.** Use the lowest-capability tier that can reliably complete deterministic or well-specified work: localized implementation, mechanical refactors, test additions, targeted inspection, formatting, repetitive changes, or straightforward verification.
4. **Send a compact execution packet.** Include only: objective, necessary files/symbols/context, constraints, allowed write scope, expected deliverable, acceptance criteria, and escalation conditions. If the subagent can read the repository, prefer paths and symbols over pasted source.
5. **Avoid rediscovery.** Pass established decisions and evidence rather than asking each subagent to repeat diagnosis. Use independent duplicate investigation only when verification is worth its cost.
6. **Batch related work.** Prefer one coherent delegation over many microtasks when the tasks share context. Spawning and reintegrating a subagent has a cost.
7. **Parallelize only independent work.** Run tasks concurrently when they do not depend on one another or modify overlapping state. Serialize dependent or conflicting work.
8. **Escalate judgment upward.** Stop lower-tier execution and return control when assumptions break, requirements are ambiguous, architecture or contracts change, security/data-loss risk appears, repeated failure occurs, or a decision falls outside the brief.
9. **Verify cheaply first.** Prefer deterministic checks such as tests, type checks, linters, builds, schema validation, and focused diffs. Use higher-capability review for material logic, risky changes, unresolved failures, or integration decisions rather than rereading every mechanical output in full.
10. **Integrate centrally.** The supervisor owns conflicts, final acceptance, unresolved risk, and the user-facing result.

## Delegation Test

Delegate only when:

`execution savings > context transfer + spawn overhead + supervision + integration`

Good subagent work is separable, well-specified, inexpensive to verify, and does not require shared evolving context.

Work directly when the task is trivial, sequential, tightly coupled, single-file, or when explaining it costs roughly as much as completing it.

## Token Discipline

- Keep supervisor state to: goal, accepted decisions, active tasks, unresolved risks, and completion evidence.
- Do the expensive reasoning once; send conclusions, not reasoning transcripts.
- Do not pass hidden chain-of-thought. Pass decisions, assumptions, evidence, constraints, and acceptance criteria.
- Ask subagents for diffs, artifacts, test results, or concise findings—not essays.
- Do not poll subagents for narration. Use completion results or only necessary checkpoints.
- Do not use a higher-capability tier for work already reduced to deterministic instructions.
- Do not repeatedly retry a failing lower-tier agent. After a material failure, re-diagnose the assumption or raise capability.
- Consolidate adjacent work when shared context would otherwise be resent.

## Guardrails

- The supervisor retains ownership; delegation does not transfer accountability.
- Do not supervise peer agents or separate terminal sessions with this skill.
- Avoid recursive subagent delegation by default. The supervisor should remain the orchestration root.
- Do not spawn subagents merely to summarize context already available to the supervisor.
- Do not maximize delegation or concurrency for its own sake.
- Do not hard-code model names, prices, context limits, or orchestration fields unless verified for the active runtime.
- Keep high-impact judgment at the supervisor level; push execution downward only after ambiguity is sufficiently removed.

## Output

Track only what helps orchestration:
- plan and dependencies,
- task -> capability tier -> scope -> acceptance criteria,
- escalations or changed assumptions,
- verification evidence and unresolved risk.

Keep supervision state operational and concise; do not turn it into a second project-management system.