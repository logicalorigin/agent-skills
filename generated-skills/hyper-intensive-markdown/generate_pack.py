#!/usr/bin/env python3
"""
Generate a one-shot component extraction pack in Markdown from JSON input.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _to_text(value, default="N/A"):
    if value is None:
        return default
    if isinstance(value, list):
        if not value:
            return default
        return ", ".join(str(item) for item in value)
    return str(value)


def _md_list(items, indent=""):
    items = [str(item) for item in _as_list(items) if item is not None and str(item).strip()]
    if not items:
        return f"{indent}- N/A\n"
    return "".join(f"{indent}- {item}\n" for item in items)


def _md_table(headers, rows):
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join("---" for _ in headers) + "|")
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n"


def _node_id(label, seen):
    base = re.sub(r"[^A-Za-z0-9]+", "_", label).strip("_") or "node"
    node = base
    index = 1
    while node in seen:
        node = f"{base}_{index}"
        index += 1
    seen.add(node)
    return node


def _mermaid_flow(wireframe, fallback_title):
    nodes = _as_list(wireframe.get("nodes") if isinstance(wireframe, dict) else None)
    edges = _as_list(wireframe.get("edges") if isinstance(wireframe, dict) else None)
    if not nodes and not edges:
        nodes = [fallback_title]

    label_to_id = {}
    seen_ids = set()

    def get_id(label):
        if label in label_to_id:
            return label_to_id[label]
        node = _node_id(label, seen_ids)
        label_to_id[label] = node
        return node

    lines = ["flowchart LR"]
    if edges:
        for edge in edges:
            if not isinstance(edge, list) or len(edge) != 2:
                continue
            left, right = str(edge[0]), str(edge[1])
            left_id = get_id(left)
            right_id = get_id(right)
            left_label = left.replace("]", ")")
            right_label = right.replace("]", ")")
            lines.append(f'  {left_id}["{left_label}"] --> {right_id}["{right_label}"]')
    else:
        for label in nodes:
            node_id = get_id(str(label))
            safe_label = str(label).replace("]", ")")
            lines.append(f'  {node_id}["{safe_label}"]')

    return "\n".join(lines)


def build_markdown(data):
    component_name = _to_text(data.get("component_name"))
    summary = data.get("summary", {}) if isinstance(data.get("summary"), dict) else {}
    scope = data.get("scope", {}) if isinstance(data.get("scope"), dict) else {}
    current = data.get("current_state", {}) if isinstance(data.get("current_state"), dict) else {}
    target = data.get("target_state", {}) if isinstance(data.get("target_state"), dict) else {}
    migration = data.get("migration", {}) if isinstance(data.get("migration"), dict) else {}

    component_rows = []
    for item in _as_list(data.get("component_inventory")):
        if not isinstance(item, dict):
            continue
        component_rows.append(
            [
                _to_text(item.get("component")),
                _to_text(item.get("responsibility")),
                _to_text(item.get("inputs")),
                _to_text(item.get("outputs")),
                _to_text(item.get("state")),
                _to_text(item.get("notes")),
            ]
        )
    if not component_rows:
        component_rows = [["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]]

    file_move_rows = []
    for item in _as_list(data.get("file_moves")):
        if not isinstance(item, dict):
            continue
        file_move_rows.append(
            [
                _to_text(item.get("from")),
                _to_text(item.get("to")),
                _to_text(item.get("notes")),
            ]
        )
    if not file_move_rows:
        file_move_rows = [["N/A", "N/A", "N/A"]]

    dependency_rows = []
    for item in _as_list(data.get("dependency_changes")):
        if not isinstance(item, dict):
            continue
        dependency_rows.append(
            [
                _to_text(item.get("dependency")),
                _to_text(item.get("change")),
                _to_text(item.get("rationale")),
            ]
        )
    if not dependency_rows:
        dependency_rows = [["N/A", "N/A", "N/A"]]

    api_rows = []
    for item in _as_list(migration.get("api_mapping")):
        if not isinstance(item, dict):
            continue
        api_rows.append(
            [
                _to_text(item.get("old")),
                _to_text(item.get("new")),
                _to_text(item.get("change_type")),
                _to_text(item.get("deprecation")),
                _to_text(item.get("notes")),
            ]
        )
    if not api_rows:
        api_rows = [["N/A", "N/A", "N/A", "N/A", "N/A"]]

    risk_rows = []
    for item in _as_list(data.get("risks")):
        if not isinstance(item, dict):
            continue
        risk_rows.append(
            [
                _to_text(item.get("risk")),
                _to_text(item.get("impact")),
                _to_text(item.get("mitigation")),
            ]
        )
    if not risk_rows:
        risk_rows = [["N/A", "N/A", "N/A"]]

    mermaid = _mermaid_flow(data.get("wireframe", {}), component_name)

    sections = []
    sections.append(f"# Component Extraction Pack: {component_name}\n")
    sections.append("## Summary\n")
    sections.append(f"- Goal: {_to_text(summary.get('goal'))}\n")
    sections.append(f"- Why now: {_to_text(summary.get('why_now'))}\n")
    sections.append(f"- Primary outcome: {_to_text(summary.get('primary_outcome'))}\n")
    sections.append("\n## Assumptions\n")
    sections.append(_md_list(data.get("assumptions")))
    sections.append("\n## Scope\n\n### In Scope\n")
    sections.append(_md_list(scope.get("in_scope")))
    sections.append("\n### Out of Scope\n")
    sections.append(_md_list(scope.get("out_of_scope")))
    sections.append("\n## Current State\n")
    sections.append(f"- Location: {_to_text(current.get('location'))}\n")
    sections.append(f"- Ownership: {_to_text(current.get('ownership'))}\n")
    sections.append("- Key dependencies:\n")
    sections.append(_md_list(current.get("dependencies"), indent="  "))
    sections.append("- Known pain points:\n")
    sections.append(_md_list(current.get("pain_points"), indent="  "))
    sections.append("\n## Target State\n")
    sections.append(f"- New location: {_to_text(target.get('location'))}\n")
    sections.append(f"- Ownership: {_to_text(target.get('ownership'))}\n")
    sections.append("- Success criteria:\n")
    sections.append(_md_list(target.get("success_criteria"), indent="  "))
    sections.append("\n## Component Inventory\n\n")
    sections.append(_md_table(
        ["Component", "Responsibility", "Inputs/Props", "Outputs/Events", "State", "Notes"],
        component_rows,
    ))
    sections.append("\n## Extraction Plan\n\n")
    sections.append(_md_list(data.get("extraction_plan")))
    sections.append("\n### File and Module Moves\n\n")
    sections.append(_md_table(["From", "To", "Notes"], file_move_rows))
    sections.append("\n### Dependency Changes\n\n")
    sections.append(_md_table(["Dependency", "Change", "Rationale"], dependency_rows))
    sections.append("\n## Migration Guide\n\n### Prerequisites\n")
    sections.append(_md_list(migration.get("prerequisites")))
    sections.append("\n### Step-by-Step\n")
    sections.append(_md_list(migration.get("steps")))
    sections.append("\n### API Mapping\n\n")
    sections.append(_md_table(["Old API", "New API", "Change Type", "Deprecation", "Notes"], api_rows))
    sections.append("\n### Rollout and Deprecation\n")
    sections.append(_md_list(migration.get("rollout")))
    sections.append("\n### Testing and Verification\n")
    sections.append(_md_list(migration.get("testing")))
    sections.append("\n### Validation\n")
    sections.append(_md_list(migration.get("validation")))
    sections.append("\n### Rollback\n")
    sections.append(_md_list(migration.get("rollback")))
    sections.append("\n## Wireframe Sketch\n\n```mermaid\n")
    sections.append(mermaid)
    sections.append("\n```\n")
    sections.append("\n## Risks\n\n")
    sections.append(_md_table(["Risk", "Impact", "Mitigation"], risk_rows))
    sections.append("\n## Open Questions\n")
    sections.append(_md_list(data.get("open_questions")))
    return "".join(sections)


def main():
    parser = argparse.ArgumentParser(description="Generate a one-shot extraction pack in Markdown.")
    parser.add_argument("--input", required=True, help="Path to JSON input.")
    parser.add_argument("--output", help="Optional output path. Defaults to stdout.")
    args = parser.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    markdown = build_markdown(data)

    if args.output:
        Path(args.output).write_text(markdown, encoding="utf-8")
    else:
        print(markdown)


if __name__ == "__main__":
    main()
