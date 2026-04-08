# Public Bundle Inventory

## Purpose

This inventory defines what belongs in the public toolkit bundle and what does not.

It exists to keep the public bundle understandable without exposing internal workspace structure.

## Public Inclusion Rules

An asset belongs in the public bundle only when it:

- is reusable beyond one city
- preserves placeholders and local-decision markers where needed
- does not require hidden source-city context to interpret
- has passed a bounded evaluation and review pass without unresolved critical issues
- is clearly labeled as core toolkit material, not an example or internal planning note

## Public Bundle Contents

### Root And Orientation

- `README.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `CHANGELOG.md`
- `docs/quickstart/start-here.md`
- `docs/workflow/workflow-overview.md`

### Core Toolkit Layers

- `toolkit/templates/`
- `toolkit/prompts/`
- `toolkit/evaluations/`
- `toolkit/review-sprint-kit/`
- `toolkit/education/`

### Examples

- `examples/example-entry-index.md`
- `examples/annotated/guide-worked-example-midsize-city-five-layer-build.md`
- `examples/annotated/guide-worked-example-small-city-minimum-viable-five-layer-path.md`
- `examples/annotated/guide-worked-example-large-city-enterprise-five-layer-path.md`
- `examples/annotated/matrix-city-scale-adaptation-starter-comparison.md`

## Public Exclusions

Keep these out of the public bundle by default:

- orchestration logs and control-room status files
- source-audit working notes and provenance matrices
- reverse-engineering working papers that depend on source-city trace
- scratch notes and unfinished comparison files
- extraction drafts that have not been neutralized
- internal-only packaging notes that map public files back to the numbered workspace

## Packaging Checks For This Inventory

Before publication, confirm:

- every public file points only to public-bundle paths
- public docs do not name the original source city
- examples remain clearly labeled as examples
- templates and prompt packs remain self-contained
- omitted internal layers are documented in the release-boundary controls outside the public bundle

## Ownership

- `Agent.Onboarding` owns promotion of public entry and learning docs
- `Agent.Packaging` owns destination structure and public index updates
- `Agent.Templates` owns template promotion readiness
- `Agent.Prompts` owns prompt promotion readiness
- `Main Orchestrator` decides when a source asset is ready to promote
