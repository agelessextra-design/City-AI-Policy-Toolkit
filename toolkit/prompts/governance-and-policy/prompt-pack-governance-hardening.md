# Prompt Pack: Governance Hardening

## Purpose

This prompt pack is used after the first governance build pass to repair issues, resolve contradictions, lift weak scores, and prepare the package for board-style review.

## Shared Inputs

- `toolkit/prompts/governance-and-policy/prompt-pack-governance-pilot.md`
- `toolkit/evaluations/guide-module-family-review-readiness.md`
- `toolkit/evaluations/template-module-family-scorecard.md`
- `toolkit/evaluations/template-shared-issue-log.md`
- `toolkit/review-sprint-kit/template-contradiction-sweep-checklist.md`
- `toolkit/review-sprint-kit/template-review-sprint-brief.md`

## Pack 5: Governance Repair

Use when the evaluator has returned `revise` or `advance with flags`.

Return:

1. issue-by-issue repair plan
2. files or sections to revise
3. unresolved decisions that still block clean repair
4. revised handoff target

Rules:

- repair the named issues only
- do not widen scope without saying so
- keep unresolved local decisions visible
- when unresolved ownership remains, add fallback routing, authority limits, blocked actions, and decision deadlines before closing the issue

## Pack 6: Governance Contradiction Resolution

Use when the issue log contains contradictions across policy, workflow, register, or trust linkages.

Return:

1. contradiction inventory
2. preferred resolution path
3. impacted artifacts
4. required owner decisions

Rules:

- do not normalize contradictions silently
- identify the authoritative artifact if one exists

## Pack 7: Governance Upgrade

Use when a governance artifact is usable but below the target score.

Return:

1. score-lift plan by dimension
2. highest-leverage rewrites
3. missing artifacts or evidence
4. next evaluation checkpoint

## Pack 8: Governance Board Prep

Use when the package is nearing milestone stability.

Return:

1. likely board objections
2. proof points already present
3. weak spots that still need hardening
4. review packet additions needed before board simulation
