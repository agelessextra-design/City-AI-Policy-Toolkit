# AI Assistant Operating Guide

This guide tells AI coding assistants and writing agents how to use this repository with a city team.

Use it when a user asks for help building a municipal AI policy system, governance workflow, operating model, or related business system from this toolkit.

## Operating Rules

- Treat the repo as a public toolkit, not as a finished city-specific policy package.
- Start with `docs/quickstart/use-with-ai-assistants.md`, then use `docs/quickstart/start-here.md`.
- Ask for local city inputs before drafting final policy language.
- Do not invent legal, records, procurement, privacy, accessibility, labor, civil-rights, cybersecurity, budget, or executive-authority facts.
- Preserve `[[REQUIRES_LOCAL_DECISION: ...]]`, `[[REQUIRES_LOCAL_RESEARCH: ...]]`, and `[[REQUIRES_LEGAL_REVIEW: ...]]` markers until the city resolves them.
- Use examples only as examples. Do not treat them as default policy choices.
- Produce outlines before final prose.
- Run evaluation and review-readiness checks before saying an artifact is ready for leadership, council, public, or operational use.
- Keep local assumptions visible in the output.

## Required Starting Questions

Before drafting, ask the city for enough information to choose a path:

- city name and intended audience
- current AI maturity: no program, pilots, scattered tools, or formal program
- target artifacts: policy, charter, review workflow, operating playbook, training plan, public-trust framework, or full system
- executive sponsor or unresolved ownership question
- governance lead or unresolved ownership question
- legal, records, privacy, procurement, accessibility, labor, security, and communications reviewers
- known AI use cases or likely first pilots
- resident-facing or staff-only scope
- desired risk model, if already chosen
- timeline and review body
- known local constraints that must not be guessed

If the city cannot answer a required question, route it through `docs/quickstart/recover-missing-inputs.md`.

## Path Selection

Choose the module family based on the user's bottleneck:

- strategic leadership: executive sponsorship, portfolio direction, investment sequencing
- governance and policy: approval rules, risk tiers, accountability, registers
- workforce and learning: staff readiness, manager duties, HR or labor coordination
- operations and service delivery: intake, testing, launch, support, monitoring, pause, rollback
- community trust: public notice, explanation, accessibility, engagement, questions, redress

For a full city AI system, build in this order unless the city has a clear reason to start elsewhere:

1. Strategic leadership charter
2. Governance core policy and risk-tier review workflow
3. Operations and service delivery playbook
4. Workforce enablement and learning plan
5. Public trust and engagement framework
6. Evaluation, issue log, review-readiness summary, and review-sprint packet

## Artifact Map

Use these files as the primary toolkit surface:

- templates: `toolkit/templates/module-family-index.md`
- prompts: `toolkit/prompts/module-family-index.md`
- evaluations: `toolkit/evaluations/evaluation-entry-index.md`
- review sprint: `toolkit/review-sprint-kit/review-entry-index.md`
- examples: `examples/example-entry-index.md`
- workflow: `docs/workflow/workflow-overview.md`
- release readiness: `docs/workflow/release-readiness.md`

## Build Pattern

For each selected module:

1. Read the matching template and adapter notes.
2. Read the matching prompt pack.
3. Run the intake prompt or convert the user's answers into an intake summary.
4. Produce an outline with unresolved local decisions marked.
5. Draft only from the approved outline.
6. Create a residual placeholder list.
7. Evaluate using `toolkit/evaluations/template-module-family-scorecard.md`.
8. Log issues in `toolkit/evaluations/template-shared-issue-log.md`.
9. Summarize readiness with `toolkit/evaluations/template-review-readiness-summary.md`.
10. If needed, run hardening prompts before human review.

## Business-System Outputs

When the user asks to build the city's AI business systems, translate policy into operating assets such as:

- AI intake path
- risk-tier review workflow
- approval authority map
- AI system register or inventory fields
- issue and escalation log
- launch-readiness checklist
- monitoring and material-change process
- pause, rollback, and retirement process
- staff learning and manager support plan
- public notice, engagement, and redress workflow
- review cadence and ownership model

Do not treat these as software systems unless the user explicitly asks to implement software. By default, build documented workflows, forms, registers, checklists, and governance routines.

## Stop Conditions

Stop and ask for city review when:

- legal authority is unclear
- procurement or vendor obligations are unresolved
- records retention or public disclosure implications are unresolved
- labor, HR, or job-classification impacts are unresolved
- accessibility, language access, or civil-rights impacts are unresolved
- cybersecurity or data classification is unresolved
- the policy would imply final approval without a named local authority
- resident-facing use lacks public notice or redress logic

## Completion Standard

Do not say the city has a ready AI policy system until the output includes:

- the selected artifacts
- visible local decisions and unresolved markers
- a scorecard or evaluation summary
- a shared issue log
- review-readiness summary
- clear next human reviewers
- implementation or operating-system next steps

