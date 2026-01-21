# Hyper Intensive Markdown

Create dense, structured Markdown deliverables for component extraction work, migration guides, and sketch wireframes.

## Included

- `SKILL.md` with the workflow and formatting rules
- `references/one-shot-pack.md` template
- `references/wireframe-diagram.md` diagram patterns
- `generate_pack.py` sample generator
- `sample_input.json` and `expected_output.md` examples

## Installation

Copy the folder into your skills directory:

```bash
cp -r hyper-intensive-markdown ~/.codex/skills/
```

## Quick Start

Ask for a one-shot pack:

```
I need a one-shot component extraction pack with a migration guide and wireframe for the Property Verification Card.
```

## Generate Example Output

```bash
python generate_pack.py --input sample_input.json --output expected_output.md
```
