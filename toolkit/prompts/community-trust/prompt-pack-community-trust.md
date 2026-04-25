# Prompt Pack: Community Trust

## Purpose

This prompt pack turns the community trust template family into a usable workflow for building a city-specific public trust and engagement framework for AI.

## Shared Inputs

Every pack may reference:

- `toolkit/templates/community-trust/template-public-trust-and-engagement-framework.md`
- `toolkit/templates/community-trust/adapter-notes/public-trust-and-engagement-framework-adapter-notes.md`
- `toolkit/templates/governance-and-policy/template-governance-core-policy.md`
- `toolkit/evaluations/guide-module-family-review-readiness.md`
- `toolkit/evaluations/template-module-family-scorecard.md`
- `toolkit/evaluations/template-review-readiness-summary.md`
- `toolkit/evaluations/template-shared-issue-log.md`

## Global Rules

- Do not reduce trust to a public webpage or disclosure paragraph.
- Preserve unresolved notice, accessibility, engagement, and redress decisions.
- Keep the framework tied to actual resident-facing or publicly meaningful uses.
- Do not claim public accountability channels the city has not confirmed.
- If a required trust owner is unresolved, add an interim intake owner, response target, escalation owner, blocked actions, and a decision deadline rather than stopping at a placeholder.
- If the use is publicly controversial or politically sensitive, add a packet-style explanation of what the city is and is not doing, what remains blocked, and where public concerns route.

## Pack 1: Community Trust Intake

### Prompt

```text
You are preparing a community-trust intake artifact for a city AI public trust and engagement framework.

Use these files as the source of truth:
- toolkit/templates/community-trust/adapter-notes/public-trust-and-engagement-framework-adapter-notes.md
- toolkit/templates/community-trust/template-public-trust-and-engagement-framework.md

Produce:
1. Public-impact context summary
2. Confirmed communications, engagement, and accessibility partners
3. Known inquiry, complaint, or redress channels
4. Missing local inputs
5. Required local decisions
6. Go / blocked recommendation for outline drafting

Rules:
- Do not invent public engagement posture or complaint pathways.
- If the city cannot identify any public explanation or concern channel, return "blocked".
- If the city lacks a permanent complaint or redress owner but can name an interim intake route, return a usable intake artifact with the unresolved marker plus the interim pattern.
```

## Pack 2: Community Trust Outline

### Prompt

```text
You are building an adapted outline for a city AI public trust and engagement framework.

Use these files as the source of truth:
- toolkit/templates/community-trust/template-public-trust-and-engagement-framework.md
- toolkit/templates/community-trust/adapter-notes/public-trust-and-engagement-framework-adapter-notes.md
- toolkit/templates/governance-and-policy/template-governance-core-policy.md

Use the completed community-trust intake artifact as the city-specific input.

Produce:
1. Adapted trust framework outline
2. Placeholder inventory
3. Unresolved local-decision inventory
4. Required legal, accessibility, and communications review list
5. Required research list

Rules:
- Preserve template section order.
- Keep inquiry, concern, and redress pathways explicit.
- Stop rather than guessing notice thresholds or engagement obligations.
- If no final complaint owner exists, include an interim intake owner, response target, escalation path, and blocked launch rule for resident-facing use.
```

## Pack 3: Community Trust Draft

### Prompt

```text
You are turning an approved community-trust outline into a first working draft of a city AI public trust and engagement framework.

Use these files as the source of truth:
- approved adapted outline
- toolkit/templates/community-trust/template-public-trust-and-engagement-framework.md
- toolkit/templates/community-trust/adapter-notes/public-trust-and-engagement-framework-adapter-notes.md

Produce:
1. First working draft of the trust framework
2. Residual placeholder list
3. Residual local-decision list
4. Draft handoff note for governance and service-delivery review

Rules:
- Keep unresolved markers visible.
- Do not hide accessibility, language-access, or redress gaps.
- Do not imply public trust is satisfied by disclosure alone.
- If complaint or redress ownership is unresolved, do not allow the framework to stop at a placeholder. Include the interim path and state what cannot launch until the permanent model is decided.
```

## Pack 4: Community Trust Evaluation

### Prompt

```text
You are evaluating a city AI public trust and engagement framework for review readiness.

Use these files as the source of truth:
- toolkit/evaluations/guide-module-family-review-readiness.md
- toolkit/evaluations/template-module-family-scorecard.md
- toolkit/evaluations/template-review-readiness-summary.md
- toolkit/evaluations/template-shared-issue-log.md
- the draft community-trust artifacts under review

Produce:
1. Review-readiness assessment by dimension
2. Blocked / revise / advance recommendation
3. Shared issue-log entries
4. Required next actions by owner

Rules:
- Flag weak notice logic, absent accessibility ownership, or missing redress pathways as blockers.
- Do not rewrite the framework in the evaluation output.
```

## Hardening Follow-On

After the first evaluation pass, use `prompt-pack-community-trust-hardening.md` for repair, contradiction resolution, score-lift work, and board-prep loops.
