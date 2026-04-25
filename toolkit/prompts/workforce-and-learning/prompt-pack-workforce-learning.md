# Prompt Pack: Workforce Learning

## Purpose

This prompt pack turns the workforce and learning template family into a usable workflow for building a city-specific workforce enablement and learning plan.

## Shared Inputs

Every pack may reference:

- `toolkit/templates/workforce-and-learning/template-workforce-enablement-and-learning-plan.md`
- `toolkit/templates/workforce-and-learning/adapter-notes/workforce-enablement-and-learning-plan-adapter-notes.md`
- `toolkit/templates/governance-and-policy/template-governance-core-policy.md`
- `toolkit/evaluations/guide-module-family-review-readiness.md`
- `toolkit/evaluations/template-module-family-scorecard.md`
- `toolkit/evaluations/template-review-readiness-summary.md`
- `toolkit/evaluations/template-shared-issue-log.md`

## Global Rules

- Do not imply job redesign, bargaining outcomes, or performance changes the city has not decided.
- Preserve workforce, labor, and research gaps as visible issues.
- Keep the plan tied to actual approved or likely use cases.
- Do not let training become a generic literacy memo.
- If a proposed use may materially affect staff workflow, duties, supervision, or staffing assumptions, add a labor-trigger owner, fallback review route, blocked actions, and decision deadline instead of leaving the issue generic.

## Pack 1: Workforce Intake

### Prompt

```text
You are preparing a workforce-readiness intake artifact for a city AI enablement plan.

Use these files as the source of truth:
- toolkit/templates/workforce-and-learning/adapter-notes/workforce-enablement-and-learning-plan-adapter-notes.md
- toolkit/templates/workforce-and-learning/template-workforce-enablement-and-learning-plan.md

Produce:
1. Affected workforce summary
2. Confirmed training and support owners
3. Known labor or HR constraints
4. Missing local inputs
5. Required local decisions
6. Go / blocked recommendation for outline drafting

Rules:
- Do not invent labor posture or workforce impacts.
- If the city cannot identify affected workforce groups or any training owner, return "blocked".
- If a labor trigger is plausible, return a usable intake artifact only if the trigger owner and fallback review route are named or visibly unresolved.
```

## Pack 2: Workforce Outline

### Prompt

```text
You are building an adapted outline for a city workforce enablement and learning plan for AI.

Use these files as the source of truth:
- toolkit/templates/workforce-and-learning/template-workforce-enablement-and-learning-plan.md
- toolkit/templates/workforce-and-learning/adapter-notes/workforce-enablement-and-learning-plan-adapter-notes.md
- toolkit/templates/governance-and-policy/template-governance-core-policy.md

Use the completed workforce intake artifact as the city-specific input.

Produce:
1. Adapted workforce plan outline
2. Placeholder inventory
3. Unresolved local-decision inventory
4. Required labor, HR, legal, or accessibility review list
5. Required research list

Rules:
- Preserve template section order.
- Keep manager, labor, and support responsibilities explicit.
- Stop rather than guessing workforce impact depth or support ownership.
- If a labor trigger exists, state what may proceed before labor review and what remains blocked until the city decides whether consultation is required.
```

## Pack 3: Workforce Draft

### Prompt

```text
You are turning an approved workforce outline into a first working draft of a city AI workforce enablement and learning plan.

Use these files as the source of truth:
- approved adapted outline
- toolkit/templates/workforce-and-learning/template-workforce-enablement-and-learning-plan.md
- toolkit/templates/workforce-and-learning/adapter-notes/workforce-enablement-and-learning-plan-adapter-notes.md

Produce:
1. First working draft of the workforce plan
2. Residual placeholder list
3. Residual local-decision list
4. Draft handoff note for governance and operations alignment

Rules:
- Keep unresolved markers visible.
- Do not turn provisional staffing expectations into commitments.
- Do not erase labor, HR, or manager responsibilities.
- If the use may change staff workflows materially, add the labor-trigger operating pattern rather than a generic labor note.
```

## Pack 4: Workforce Evaluation

### Prompt

```text
You are evaluating a workforce enablement and learning plan for review readiness.

Use these files as the source of truth:
- toolkit/evaluations/guide-module-family-review-readiness.md
- toolkit/evaluations/template-module-family-scorecard.md
- toolkit/evaluations/template-review-readiness-summary.md
- toolkit/evaluations/template-shared-issue-log.md
- the draft workforce artifacts under review

Produce:
1. Review-readiness assessment by dimension
2. Blocked / revise / advance recommendation
3. Shared issue-log entries
4. Required next actions by owner

Rules:
- Flag hidden workforce impacts, weak manager support, or absent labor/HR touchpoints as blockers.
- Do not rewrite the plan in the evaluation output.
```

## Hardening Follow-On

After the first evaluation pass, use `prompt-pack-workforce-learning-hardening.md` for repair, contradiction resolution, score-lift work, and board-prep loops.
