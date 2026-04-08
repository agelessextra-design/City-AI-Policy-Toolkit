# Shared Issue Log

## Purpose

Use this template as the canonical issue log for intake, outline, draft, and review-packet evaluation across all toolkit families.

## When To Use

Use this template when:

- evaluating any artifact type in the shared toolkit workflow
- capturing blockers, gaps, contradictions, or threshold misses
- preparing the issue summary that feeds the routing register and review packet

Do not fork a new schema for each family. Use the same table and filter it when a family-specific view is needed.

## Canonical Fields

| Issue ID | Source Family | Workflow Stage | Source Artifact | Section or Location | Issue Type | Severity | Rubric Dimension | Description | Evidence | Recommended Fix | Owner | Disposition | Next Action | Due State |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ISS-001 |  |  |  |  |  |  |  |  |  |  |  | open |  | blocks next stage |

## Field Guidance

- `Issue ID`: stable reference for the finding.
- `Source Family`: the family or module that produced the finding, such as governance, ownership/register, internal tools and shadow AI, or a generic shared evaluation pass.
- `Workflow Stage`: the stage being evaluated, such as intake, outline, draft, or review packet.
- `Source Artifact`: the specific artifact under review.
- `Section or Location`: the exact section, page, or artifact location affected.
- `Issue Type`: use a controlled type such as missing local decision, unsupported legal assumption, contradiction, structural gap, placeholder misuse, or missing owner.
- `Severity`: use `critical`, `major`, `moderate`, or `minor`.
- `Rubric Dimension`: name the rubric area the issue affects.
- `Description`: concise statement of the problem.
- `Evidence`: short source-backed note, not a long commentary block.
- `Recommended Fix`: the smallest useful change that would address the issue.
- `Owner`: the person or role responsible for action.
- `Disposition`: use `open`, `in progress`, `resolved`, `deferred`, `accepted risk`, or `out of scope`.
- `Next Action`: the immediate next step.
- `Due State`: state whether the issue blocks the next stage.

## Usage Rules

- Write one row per distinct finding.
- Use the same row structure for all families.
- Filter by `Source Family` and `Workflow Stage` when you need a narrower view.
- Keep the shared values vocabulary stable even when the family changes.
- If one finding affects several sections, keep one primary row and add sibling rows only when the fixes differ.
- If a finding becomes a decision, mirror it in the decision log rather than overloading the issue log.

## Routing Rules

- `critical` issues block advancement.
- `major` issues should be fixed before human sprint review.
- Every blocker must have a named owner.
- Every issue with unresolved policy meaning must have a path to a named owner or explicit local decision.
- Every open issue should be readable by the review packet builder without reconstructing the draft.

## Relation To Downstream Artifacts

- The issue log is the source of open-item detail.
- The review packet consumes the issue log summary and routing register together.
- The review-sprint brief uses the same issue rows to define scope, blockers, and owners.

## Family-Specific View Guidance

If a family needs a narrower view, use the shared log and filter it rather than defining a new schema.

Recommended family-specific view pattern:

1. Set `Source Family` to the family name.
2. Filter rows by `Workflow Stage`.
3. Keep the core columns unchanged.
4. Add only family-specific explanatory text outside the table.

Family-specific views should not rename, reorder, or reinterpret the core fields.
