# Prompt Pack: Strategic Leadership

## Purpose

This prompt pack turns the strategic leadership template family into a usable intake -> outline -> draft -> evaluation workflow for Codex or Claude Code.

It is designed to produce a reviewable executive charter, not a polished mayoral speech.

## Shared Inputs

Every pack may reference:

- `toolkit/templates/strategic-leadership/template-enterprise-ai-strategy-charter.md`
- `toolkit/templates/strategic-leadership/adapter-notes/enterprise-ai-strategy-charter-adapter-notes.md`
- `toolkit/templates/governance-and-policy/template-governance-core-policy.md`
- `toolkit/evaluations/guide-module-family-review-readiness.md`
- `toolkit/evaluations/template-module-family-scorecard.md`
- `toolkit/evaluations/template-review-readiness-summary.md`
- `toolkit/evaluations/template-shared-issue-log.md`
- `toolkit/review-sprint-kit/template-contradiction-sweep-checklist.md`

## Global Rules

- Do not invent executive structures, budget authority, or portfolio maturity the city has not confirmed.
- Preserve placeholders and `[[REQUIRES_LOCAL_DECISION: ...]]` markers.
- Keep the strategy tied to city outcomes, not generic innovation language.
- Do not let the strategy promise scale-up before governance, workforce, operations, and trust dependencies are named.

## Pack 1: Strategic Leadership Intake

### When To Use

Use when the city wants an AI strategy charter but has not yet converted leadership context into a structured starting point.

### Prompt

```text
You are preparing a city-specific strategic leadership intake artifact for an enterprise AI strategy charter.

Use these files as the source of truth:
- toolkit/templates/strategic-leadership/adapter-notes/enterprise-ai-strategy-charter-adapter-notes.md
- toolkit/templates/strategic-leadership/template-enterprise-ai-strategy-charter.md

Your job is to produce:
1. Leadership context summary
2. Confirmed strategy and performance anchors
3. Confirmed executive roles and ownership
4. Missing local inputs
5. Required local decisions
6. Go / blocked recommendation for outline drafting

Rules:
- Do not draft the charter itself.
- Do not invent outcome measures or budget structures.
- If the city cannot identify an executive sponsor or portfolio owner, return "blocked".
```

## Pack 2: Strategic Leadership Outline

### When To Use

Use only after the intake pack returns a usable readiness result.

### Prompt

```text
You are building an adapted outline for a city-specific enterprise AI strategy charter.

Use these files as the source of truth:
- toolkit/templates/strategic-leadership/template-enterprise-ai-strategy-charter.md
- toolkit/templates/strategic-leadership/adapter-notes/enterprise-ai-strategy-charter-adapter-notes.md
- toolkit/templates/governance-and-policy/template-governance-core-policy.md

Use the completed strategic leadership intake artifact as the city-specific input.

Produce:
1. Adapted charter outline
2. Placeholder inventory
3. Unresolved local-decision inventory
4. Required research list
5. Linked dependency list for governance, workforce, operations, and trust

Rules:
- Preserve template section order.
- Keep scale-up prerequisites visible.
- Stop rather than guessing executive ownership or budget authority.
```

## Pack 3: Strategic Leadership Draft

### When To Use

Use only after the outline has been reviewed and accepted.

### Prompt

```text
You are turning an approved strategic leadership outline into a first working draft of an enterprise AI strategy charter.

Use these files as the source of truth:
- approved adapted outline
- toolkit/templates/strategic-leadership/template-enterprise-ai-strategy-charter.md
- toolkit/templates/strategic-leadership/adapter-notes/enterprise-ai-strategy-charter-adapter-notes.md

Produce:
1. First working draft of the charter
2. Residual placeholder list
3. Residual local-decision list
4. Module dependency handoff note

Rules:
- Keep unresolved placeholders visible.
- Do not turn assumptions into commitments.
- Do not erase dependencies on governance, workforce, operations, or community trust.
```

## Pack 4: Strategic Leadership Evaluation

### When To Use

Use after the first working draft, and optionally after the outline if leadership alignment is still weak.

### Prompt

```text
You are evaluating a strategic leadership AI charter for review readiness.

Use these files as the source of truth:
- toolkit/evaluations/guide-module-family-review-readiness.md
- toolkit/evaluations/template-module-family-scorecard.md
- toolkit/evaluations/template-review-readiness-summary.md
- toolkit/evaluations/template-shared-issue-log.md
- toolkit/review-sprint-kit/template-contradiction-sweep-checklist.md
- the draft strategic leadership artifacts under review

Produce:
1. Review-readiness assessment by dimension
2. Blocked / revise / advance recommendation
3. Shared issue-log entries
4. Required next actions by owner
5. Contradiction sweep summary

Rules:
- Flag missing ownership, fake certainty, or weak linkage to other toolkit layers as blockers.
- Do not rewrite the charter in the evaluation output.
```

## Hardening Follow-On

After the first evaluation pass, use `prompt-pack-strategic-leadership-hardening.md` for repair, contradiction resolution, score-lift work, and board-prep loops.
