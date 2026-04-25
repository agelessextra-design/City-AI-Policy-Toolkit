# City AI Policy Toolkit

This repository is a reusable toolkit for small and mid-sized city teams building municipal AI systems with clear leadership, governance, workforce, operations, and community-trust layers.

This repository is the public toolkit bundle for reuse and further hardening. It is structured to stand on its own without exposing the internal build workspace.

## What This Repo Is

- a modular toolkit for turning source-backed planning material into reusable policy assets
- a place to keep reusable surface area separate from workspace-only build materials
- a starting point for city teams that need a clear workflow for source audit, neutralization, drafting, evaluation, and review
- a toolkit organized around five city-system module families:
  - strategic leadership
  - governance and policy
  - workforce and learning
  - operations and service delivery
  - community trust
- an AI-assistant operating path for cities using Codex, Claude Code, or similar tools

## What This Repo Is Not

- a copy of the internal build workspace
- a dump of scratch notes or reverse-engineering work
- a final city-specific policy package
- a replacement for legal, records, labor, accessibility, or leadership review

## Public Versus Internal Boundary

Only publish assets that are reusable beyond one city and that have been reviewed for public release.

Keep workspace-only material out of the public repo, including:

- source-audit working notes
- internal planning artifacts
- scratch files
- unresolved extraction drafts
- internal comparison notes that exist only to support build coordination

If an artifact depends on local city facts, keep the local decision visible or leave it outside the public surface until it is neutralized.

## Suggested Root Structure

This repository is organized around a small set of stable entry points:

- `docs/` for quickstart, workflow, and adaptation guidance
- `toolkit/` for reusable prompts, templates, evaluations, review-sprint materials, and education assets
- `examples/` for annotated examples that clearly separate reusable pattern from local adaptation
- `.github/` for issue templates, pull request guidance, and workflow automation

Only the public-facing parts should land in the repository root or the public documentation paths.

## How To Start

1. Read the quickstart.
2. If you are using an AI assistant, read `AGENTS.md` and `docs/quickstart/use-with-ai-assistants.md`.
3. Choose the module family you are starting from.
4. Read the workflow orientation.
5. Decide which inputs are local and which can be generalized.
6. Use the relevant template, prompt, or evaluation guide.
7. Keep unresolved decisions explicit.

## What To Read Next

- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `AGENTS.md`
- `SECURITY.md`
- `CHANGELOG.md`

## How The Toolkit Is Organized

The public repo should mirror the internal build logic without exposing the build workspace itself.

- reusable structure lives in toolkit folders
- the toolkit should expose a clear entry point for each of the five module families
- workflow guidance explains how the layers fit together
- AI-assistant guidance explains how to turn city inputs into policy and operating-system artifacts
- examples show how source-backed material can be adapted safely
- evaluation and review materials explain how quality gates work before publication

## Examples Versus Core Material

Examples are not default policy text.

Use examples to show how a pattern works, not to imply that one city’s choices should become another city’s default.

Core material should stay generic, reusable, and clearly separated from city-specific decisions.

## Maintenance Notes

- keep naming consistent and searchable
- preserve placeholder conventions when local decisions are still unresolved
- do not promote internal planning docs into public guidance without review
- keep this root documentation aligned with the public toolkit structure as the repo matures
