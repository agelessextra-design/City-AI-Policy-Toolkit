# Prompt Pack: Governance Pilot

## Purpose

This prompt pack provides the first usable prompt sequence for adapting the governance toolkit family into city-specific working outputs.

It is designed to work with Codex or Claude Code without relying on hidden conversation context.

## Shared Inputs

Every pack may reference these canonical artifacts:

- `toolkit/templates/governance-and-policy/template-governance-core-policy.md`
- `toolkit/templates/governance-and-policy/template-governance-risk-tier-review-workflow.md`
- `toolkit/templates/governance-and-policy/adapter-notes/governance-core-policy-adapter-notes.md`
- `toolkit/evaluations/guide-module-family-review-readiness.md`
- `toolkit/evaluations/template-module-family-scorecard.md`
- `toolkit/evaluations/template-review-readiness-summary.md`
- `toolkit/evaluations/template-shared-issue-log.md`
- `toolkit/review-sprint-kit/template-contradiction-sweep-checklist.md`
- `toolkit/review-sprint-kit/template-review-sprint-brief.md`
- `toolkit/review-sprint-kit/template-review-sprint-routing-register.md`
- `toolkit/review-sprint-kit/template-board-review-packet.md`

## Global Rules

- Do not invent local authority structures.
- Preserve `[[PLACEHOLDER]]` values until the city supplies them.
- Preserve `[[REQUIRES_LOCAL_DECISION: ...]]` and `[[REQUIRES_LOCAL_RESEARCH: ...]]` markers until resolved.
- Do not draft final prose before the outline exists.
- Return structured artifacts, not free-form essays.

## Pack 1: Governance Intake

### When To Use

Use when the city has chosen the governance family but has not yet confirmed the local governance context.

### Prompt

```text
You are preparing a city-specific adaptation of the governance family for a municipal AI policy toolkit.

Use these artifacts as the source of truth:
- toolkit/templates/governance-and-policy/template-governance-core-policy.md
- toolkit/templates/governance-and-policy/template-governance-risk-tier-review-workflow.md
- toolkit/templates/governance-and-policy/adapter-notes/governance-core-policy-adapter-notes.md
- the city's local context brief, intake packet, or source notes if available

Your job is to produce a governance intake artifact, not a draft policy.

Required output sections:
1. Local context summary
2. Confirmed roles and authorities
3. Missing local inputs
4. Required local decisions
5. Required local research tasks
6. Go / blocked recommendation for outline drafting

Rules:
- Do not invent missing facts.
- Keep unresolved placeholders visible.
- If the city cannot identify its approval chain, governance lead, or legal review role, return "blocked".
```

### Output Type

- readiness summary
- missing-input list
- local-decision list
- research task list

## Pack 2: Governance Outline

### When To Use

Use only after the intake pack returns a usable readiness result.

### Prompt

```text
You are building an adapted governance outline for a city-specific AI governance package.

Use these artifacts as the source of truth:
- toolkit/templates/governance-and-policy/template-governance-core-policy.md
- toolkit/templates/governance-and-policy/template-governance-risk-tier-review-workflow.md
- toolkit/templates/governance-and-policy/adapter-notes/governance-core-policy-adapter-notes.md

Use the completed governance intake artifact as the city-specific input.

Your job is to produce:
1. Adapted governance core policy outline
2. Adapted governance workflow outline
3. Placeholder inventory
4. Unresolved local-decision inventory
5. Required legal-review list
6. Required research list

Rules:
- Preserve template section order.
- Do not convert unresolved decisions into final prose.
- If a section depends on unknown local facts, keep the research marker visible.
- Stop rather than guessing.
```

### Stop Conditions

- approval chain still unknown
- tier model unresolved with no provisional decision
- legal or procurement structure completely unknown

## Pack 3: Governance Draft

### When To Use

Use only after the outline has been reviewed and accepted.

### Prompt

```text
You are turning an approved governance outline into a first working draft.

Use these artifacts as the source of truth:
- approved adapted outline
- toolkit/templates/governance-and-policy/template-governance-core-policy.md
- toolkit/templates/governance-and-policy/template-governance-risk-tier-review-workflow.md
- toolkit/templates/governance-and-policy/adapter-notes/governance-core-policy-adapter-notes.md

Your job is to produce:
1. First working draft of the governance core policy
2. First working draft of the governance review workflow
3. Residual placeholder list
4. Residual local-decision list
5. Draft handoff note for evaluation

Rules:
- Keep unresolved placeholders visible.
- Do not invent legal, procurement, or authority claims.
- Do not collapse the workflow into the core policy.
- Produce clear draft prose, but keep it visibly incomplete where the city has not decided.
```

### Stop Conditions

- unresolved core authority mapping would force fabricated language
- unresolved prohibited-use stance would make policy text misleading
- workflow and core policy begin to contradict each other

## Pack 4: Governance Evaluation

### When To Use

Use after the first working draft, and optionally after the outline if an earlier gate is needed.

### Prompt

```text
You are evaluating a draft governance package for review readiness.

Use these artifacts as the source of truth:
- toolkit/evaluations/guide-module-family-review-readiness.md
- toolkit/evaluations/template-module-family-scorecard.md
- toolkit/evaluations/template-review-readiness-summary.md
- toolkit/evaluations/template-shared-issue-log.md
- toolkit/review-sprint-kit/template-contradiction-sweep-checklist.md
- toolkit/review-sprint-kit/template-review-sprint-brief.md
- toolkit/review-sprint-kit/template-review-sprint-routing-register.md
- toolkit/review-sprint-kit/template-board-review-packet.md
- the draft governance artifacts under review

Your job is to produce:
1. Review-readiness assessment by dimension
2. Blocked / revise / advance recommendation
3. Governance issue log entries
4. Required next actions by owner
5. Contradiction sweep summary
6. Review packet assembly note

Rules:
- Surface blockers explicitly.
- Do not rewrite the governance package in the evaluation output.
- If contradictions, hidden local assumptions, or buried legal issues exist, mark the package blocked.
- Use the issue log, contradiction sweep, review-sprint brief, and routing register to assemble the review packet, not just the narrative evaluation.
```

## Handoff Rules

- Intake hands off to outline only if minimum local context exists.
- Outline hands off to draft only if the template structure is preserved and unresolved decisions are visible.
- Draft hands off to evaluation only if the package is coherent enough to assess.
- Evaluation hands off to review sprint only if blockers are resolved or explicitly isolated and the review-sprint brief plus routing register can be populated from the issue log.

## Open Questions

- Should evaluation become mandatory after the outline as well as after the draft?
- Should mature cities be allowed to skip the intake pack if they already have a context brief?
- Should unresolved placeholders be allowed in the first draft or should some categories block drafting immediately?

## Hardening Follow-On

After the first evaluation pass, use `prompt-pack-governance-hardening.md` for repair, contradiction resolution, score-lift work, and board-prep loops.
