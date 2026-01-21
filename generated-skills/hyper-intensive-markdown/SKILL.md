---
name: hyper-intensive-markdown
description: Create dense, structured Markdown deliverables for component extraction and migration work, including one-shot packs that combine extraction plan, migration guide, and sketch wireframe diagrams (Mermaid or ASCII). Use when asked for hyper intensive Markdown, component extraction docs, migration guides, or wireframe sketches.
---

# Hyper Intensive Markdown

## Overview

Produce a single, high-density Markdown deliverable that packages component extraction plans, migration guides, and wireframe sketches into a clear, actionable document.

## Workflow Decision Tree

- If the request asks for component extraction plus migration guide and a sketch wireframe, use the One-Shot Pack workflow.
- If only a subset is requested, produce only the relevant sections from the One-Shot Pack template.
- If critical context is missing, assume reasonable defaults and list assumptions explicitly instead of blocking.

## One-Shot Pack Workflow

### Step 1: Establish scope and assumptions

Capture or infer:
- Component or feature name(s)
- Current location and ownership
- Target structure or destination
- Key dependencies and integrations
- Expected API surface and breaking changes
- Timeline or rollout constraints

If any of the above is missing, proceed with explicit assumptions and list open questions at the end.

### Step 2: Draft the component extraction plan

Define:
- Component boundaries and responsibilities
- Inputs, outputs, and state ownership
- File/module moves and new directory layout
- Dependency changes and shared utilities
- Risky edges (coupling, side effects, performance, data flow)

### Step 3: Write the migration guide

Include:
- Prerequisites and compatibility notes
- Step-by-step migration instructions
- API mapping table (old to new)
- Deprecation or rollout plan
- Validation and rollback steps

### Step 4: Add a sketch wireframe diagram

Default to Mermaid flowcharts unless the user forbids Mermaid. Keep the diagram intentionally simple and readable. Use `references/wireframe-diagram.md` for patterns.

### Step 5: Assemble the final Markdown pack

Use the canonical outline in `references/one-shot-pack.md`. Remove placeholders and keep headings consistent. If a section is not applicable, mark it as `N/A` instead of removing it.

## Formatting Rules

- Use GitHub-flavored Markdown.
- Prefer tables for mappings, dependencies, and file moves.
- Use fenced code blocks with info strings (`mermaid`, `bash`, `ts`, etc.) when needed.
- Keep the document self-contained and actionable without external context.

## Resources

- `references/one-shot-pack.md` for the canonical template.
- `references/wireframe-diagram.md` for diagram patterns.
