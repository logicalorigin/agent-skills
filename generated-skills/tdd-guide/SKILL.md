---
name: tdd-guide
description: Drive test-first development around observable behavior, including red-green-refactor, missing tests, fixtures, coverage, and test quality.
---

# TDD Guide

Use tests to define and protect behavior, not to freeze incidental implementation details.

## Workflow

1. Define the observable behavior, contract, acceptance criteria, and important edge or failure cases before choosing test structure.
2. Write the smallest meaningful failing test for one behavior.
3. Confirm the test fails for the expected reason; fix the test or setup if the failure is unrelated.
4. Implement the minimum production change needed to make the test pass.
5. Run the relevant test scope, then refactor while preserving behavior.
6. Repeat for boundaries, errors, state transitions, security-sensitive paths, and integration seams that matter to the feature.
7. Use coverage to find unexamined paths, not as a target to game. Prioritize risk and behavior over a percentage alone.
8. Match the repository's existing framework, naming, fixtures, and mocking style unless migration is part of the request.

## Bundled resources

- `format_detector.py`, `framework_adapter.py`, `test_generator.py`, `fixture_generator.py`
- `coverage_analyzer.py`, `metrics_calculator.py`, `tdd_workflow.py`, `output_formatter.py`
- Sample inputs, `sample_coverage_report.lcov`, `expected_output.json`, `README.md`, `HOW_TO_USE.md`

## Guardrails

- Do not weaken assertions, delete valid tests, or alter expected behavior merely to make the suite pass.
- Prefer public behavior and stable contracts over private implementation details.
- Distinguish unit, integration, contract, and end-to-end concerns rather than mocking everything by default.
- Do not add broad production refactors that are unnecessary for the tested behavior.
- Treat flaky, timing-dependent, and environment-dependent tests as defects to diagnose, not failures to ignore.

## Output

Return the tests or TDD step, expected behavior, relevant implementation scope, validation result, and any remaining high-risk untested paths.
