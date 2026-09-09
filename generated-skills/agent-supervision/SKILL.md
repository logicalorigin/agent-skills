---
name: agent-supervision
description: Supervise a parent-agent workflow that delegates bounded work to subagents. Use when one agent owns decomposition, assignment, monitoring, validation, and integration of subagent work. Do not use for coordinating peer agents, external terminal agents, or ordinary single-agent tasks.
---

# Agent Supervision

Use intelligence where ambiguity is expensive; use cheaper execution where the work is already understood.

## Scope

This skill applies only when the current agent is the **parent/supervisor** of one or more subagents and remains responsible for the final outcome.

Do not use it to coordinate separate terminal sessions, peer agents, external agent runners, or independent agents that the current agent does not directly supervise. Do not delegate trivial work that is faster to complete directly.

## Workflow

1. **Diagnose before delegating.** The supervisor establishes the real problem, relevant constraints, likely root cause, architecture/contract implications, risks, and success criteria before spawning execution work.
2. **Plan at the highest useful capability.** Use the higher-capability reasoning tier for ambiguity, decomposition, architectural decisions, dependency ordering, security-sensitive judgment, migrations, cross-cutting changes, and recovery from failed assumptions. Do not spend this tier on mechanical execution once the path is clear.
3. **Delegate bounded execution downward.** Send lower-cost/lower-capability subagents narrowly defined tasks such as localized implementation, mechanical refactors, test additions, targeted inspection, formatting, or verification that does not require unresolved judgment.
4. **Minimize the handoff.** Give each subagent only the objective, necessary context/files, constraints, write scope, expected deliverable, acceptance criteria, and escalation conditions. Pass conclusions and decisions instead of the supervisor's full conversation or reasoning history.
5. **Avoid duplicate discovery.** Do not ask multiple subagents to rediscover facts the supervisor already established unless independent verification is itself valuable.
6. **Parallelize only independent work.** Run tasks concurrently when they do not share mutable state or depend on one another. Serialize dependency-bound or overlapping edits to avoid conflicts and rework.
7. **Escalate judgment upward.** A subagent should stop and return control when it encounters material ambiguity, a contradicted assumption, unexpected architecture, contract/schema changes, security or data-loss risk, repeated failure, or a decision outside its brief.
8. **Verify and integrate centrally.** The supervisor reviews outputs against the original success criteria, resolves conflicts, runs or assigns the necessary validation, and owns the final integrated result.

## Delegation Test

Delegate only when the expected savings from isolated execution exceed the cost of context transfer, supervision, and integration. Good subagent work is separable, well-specified, and cheaply verifiable.

Prefer direct supervisor work for simple lookups, sequential single-file changes, tightly coupled reasoning, or tasks where explaining the context costs as much as doing the work.

## Token Discipline

- Keep the supervisor's working state compact: goal, accepted decisions, active tasks, unresolved risks, and evidence needed for completion.
- Prefer one strong diagnosis followed by concise execution packets over repeated full-context reasoning by every subagent.
- Request artifacts, diffs, test results, or concise findings rather than long narratives.
- Do not pass hidden chain-of-thought. Pass decisions, assumptions, evidence, constraints, and acceptance criteria.
- Use the lowest-capability tier that can reliably complete the bounded task; raise capability only when uncertainty or failure justifies it.
- After a materially failed execution attempt, reassess the plan before spending tokens on repeated retries.

## Guardrails

- The supervisor retains ownership; delegation does not transfer accountability.
- Avoid recursive subagent delegation unless the runtime requires it and the added layer clearly reduces total work.
- Do not spawn subagents merely to summarize context already available to the supervisor.
- Do not maximize concurrency for its own sake; integration cost is part of the decision.
- Do not hard-code model names, prices, context limits, or platform-specific orchestration fields unless verified for the active runtime.
- Keep high-impact decisions and final acceptance at the supervisor level unless the task is genuinely mechanical.

## Output

When useful, track only:
- current plan and dependencies,
- delegated task -> capability tier -> scope -> acceptance criteria,
- escalations or changed assumptions,
- final verification and unresolved risk.

Keep supervision state operational and concise; do not turn it into a second project-management system.
