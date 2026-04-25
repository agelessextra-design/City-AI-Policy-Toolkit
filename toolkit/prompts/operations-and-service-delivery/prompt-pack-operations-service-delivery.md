# Prompt Pack: Operations Service Delivery

## Purpose

This prompt pack turns the operations and service delivery template family into a usable workflow for building a city-specific AI service delivery operating playbook.

## Shared Inputs

Every pack may reference:

- `toolkit/templates/operations-and-service-delivery/template-ai-service-delivery-operating-playbook.md`
- `toolkit/templates/operations-and-service-delivery/adapter-notes/ai-service-delivery-operating-playbook-adapter-notes.md`
- `toolkit/templates/governance-and-policy/template-governance-core-policy.md`
- `toolkit/evaluations/guide-module-family-review-readiness.md`
- `toolkit/evaluations/template-module-family-scorecard.md`
- `toolkit/evaluations/template-review-readiness-summary.md`
- `toolkit/evaluations/template-shared-issue-log.md`

## Global Rules

- Do not imply a mature delivery organization the city does not have.
- Preserve support, rollback, vendor, and resident-impact gaps.
- Keep governance and workforce dependencies visible.
- Do not skip testing, support, or retirement logic because a pilot seems small.
- If a required owner is unresolved, add a fallback route, authority limits, blocked actions, and a decision deadline instead of treating the gap as ordinary ambiguity.

## Pack 1: Operations Intake

### Prompt

```text
You are preparing an operational intake artifact for a city AI service delivery playbook.

Use these files as the source of truth:
- toolkit/templates/operations-and-service-delivery/adapter-notes/ai-service-delivery-operating-playbook-adapter-notes.md
- toolkit/templates/operations-and-service-delivery/template-ai-service-delivery-operating-playbook.md

Produce:
1. Service or workflow context summary
2. Confirmed service, delivery, and support owners
3. Known governance and vendor dependencies
4. Missing local inputs
5. Required local decisions
6. Go / blocked recommendation for outline drafting

Rules:
- Do not invent intake channels, support ownership, or incident processes.
- If the city cannot identify a service or delivery owner, return "blocked".
```

## Pack 2: Operations Outline

### Prompt

```text
You are building an adapted outline for a city AI service delivery operating playbook.

Use these files as the source of truth:
- toolkit/templates/operations-and-service-delivery/template-ai-service-delivery-operating-playbook.md
- toolkit/templates/operations-and-service-delivery/adapter-notes/ai-service-delivery-operating-playbook-adapter-notes.md
- toolkit/templates/governance-and-policy/template-governance-core-policy.md

Use the completed operations intake artifact as the city-specific input.

Produce:
1. Adapted operating playbook outline
2. Placeholder inventory
3. Unresolved local-decision inventory
4. Required vendor, legal, accessibility, and resident-support review list
5. Required research list

Rules:
- Preserve template section order.
- Keep service ownership and support obligations explicit.
- Stop rather than guessing pause authority, launch authority, or resident-support pathways.
- Before treating a resident-facing or resident-adjacent launch path as usable, require a concern intake owner, response target, escalation path, and pause authority.
```

## Pack 3: Operations Draft

### Prompt

```text
You are turning an approved operations outline into a first working draft of a city AI service delivery operating playbook.

Use these files as the source of truth:
- approved adapted outline
- toolkit/templates/operations-and-service-delivery/template-ai-service-delivery-operating-playbook.md
- toolkit/templates/operations-and-service-delivery/adapter-notes/ai-service-delivery-operating-playbook-adapter-notes.md

Produce:
1. First working draft of the operating playbook
2. Residual placeholder list
3. Residual local-decision list
4. Draft handoff note for service owners and governance reviewers

Rules:
- Keep unresolved markers visible.
- Do not hide support or rollback gaps.
- Do not collapse operational stages into generic project-management language.
- If any resident-support, complaint, or escalation field remains unresolved, state whether launch is blocked or provisionally limited.
```

## Pack 4: Operations Evaluation

### Prompt

```text
You are evaluating an AI service delivery operating playbook for review readiness.

Use these files as the source of truth:
- toolkit/evaluations/guide-module-family-review-readiness.md
- toolkit/evaluations/template-module-family-scorecard.md
- toolkit/evaluations/template-review-readiness-summary.md
- toolkit/evaluations/template-shared-issue-log.md
- the draft operations artifacts under review

Produce:
1. Review-readiness assessment by dimension
2. Blocked / revise / advance recommendation
3. Shared issue-log entries
4. Required next actions by owner

Rules:
- Flag missing ownership, weak testing, absent pause authority, or hidden resident-support gaps as blockers.
- Do not rewrite the playbook in the evaluation output.
```

## Hardening Follow-On

After the first evaluation pass, use `prompt-pack-operations-service-delivery-hardening.md` for repair, contradiction resolution, score-lift work, and board-prep loops.
