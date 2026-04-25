# Use This Toolkit With AI Assistants

## Purpose

This guide helps a city use the toolkit with AI assistants such as Codex, Claude Code, or similar tools.

The assistant can help organize, draft, evaluate, and harden the city's AI policy system. The city still owns the local decisions.

## What The City Must Provide

Before asking an assistant to draft, gather as much of this as possible:

- city name and intended audience
- current AI activity and known tools
- desired first outcome: policy, charter, workflow, operating playbook, training plan, public-trust plan, or full system
- executive sponsor or unresolved sponsor decision
- governance lead or unresolved governance owner
- legal, records, privacy, procurement, accessibility, labor, security, and communications reviewers
- known use cases or likely pilots
- whether the work affects residents, staff, vendors, or all three
- existing approval, project intake, service delivery, incident, and public communication processes
- local constraints the assistant must not guess

Missing inputs are allowed. They must stay visible as unresolved decisions or research items.

## Recommended Assistant Instruction

Use this instruction when starting a session:

```text
Read this repository, especially AGENTS.md and docs/quickstart/use-with-ai-assistants.md.

Help us build our city AI policy system. Start by asking for the local inputs you need. Do not invent legal, procurement, labor, privacy, accessibility, records, cybersecurity, budget, or executive-authority facts. Keep unresolved items visible with the toolkit's placeholder markers.

Use the repo's templates, prompt packs, evaluation tools, examples, and review-sprint materials. Build outlines before final prose. For each artifact, produce a residual placeholder list, issue log items, and review-readiness notes.

We want policy and operating systems, including intake, review, approval, register, launch, monitoring, training, public notice, and escalation workflows.
```

## Recommended Order For A Full System

Use this order unless the city's immediate bottleneck requires a different start:

1. Strategic leadership charter
2. Governance core policy
3. Risk-tier review workflow
4. Operations and service delivery playbook
5. Workforce enablement and learning plan
6. Public trust and engagement framework
7. Evaluation and issue log
8. Review-readiness summary and review-sprint packet

## What The Assistant Should Produce

At minimum, the assistant should produce:

- intake summary
- selected module path
- outline before prose
- draft artifact using the matching template
- residual placeholder list
- local-decision, local-research, and legal-review markers
- scorecard or evaluation notes
- shared issue log entries
- review-readiness summary
- recommended next human reviewers

For business-system work, the assistant should also produce:

- intake workflow
- role and approval map
- AI system register fields
- launch-readiness checklist
- monitoring and material-change workflow
- pause, rollback, and retirement workflow
- staff training and support workflow
- public notice, engagement, and redress workflow

## What The Assistant Must Not Do

The assistant must not:

- turn examples into default policy
- hide missing local decisions in smooth prose
- claim legal, procurement, records, labor, accessibility, privacy, or security readiness without local review
- treat staff-only tools as exempt from governance
- claim the city is ready for publication without evaluation and review-readiness evidence
- replace leadership, legal, public records, procurement, labor, accessibility, security, or community review

## If Inputs Are Missing

Use `docs/quickstart/recover-missing-inputs.md`.

The assistant should convert missing information into one of these visible markers:

- `[[REQUIRES_LOCAL_DECISION: ...]]`
- `[[REQUIRES_LOCAL_RESEARCH: ...]]`
- `[[REQUIRES_LEGAL_REVIEW: ...]]`
- `[[OPTIONAL_IF: ...]]`

## Readiness Gate

Before sharing outputs beyond the working team, run:

- `toolkit/evaluations/template-module-family-scorecard.md`
- `toolkit/evaluations/template-shared-issue-log.md`
- `toolkit/evaluations/template-review-readiness-summary.md`
- `toolkit/review-sprint-kit/template-board-review-packet.md` when leadership or board review is needed

Do not treat the output as ready if unresolved critical issues remain.

