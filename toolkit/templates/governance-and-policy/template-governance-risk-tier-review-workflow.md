# Governance Risk-Tier And Review Workflow Template

## Purpose

This template defines the review path for a city AI governance system.

It is the operational companion to the governance core policy template. The core policy explains what the city governs. This template explains how a request, system, or use case moves through intake, risk-tier assignment, approval, registration, monitoring, appeal, pace concern handling, and incident escalation.

This is a reusable draft template. It is not city-final language.

## Intended Use

Use this template when a city needs a clear workflow for:

- deciding whether an AI use is low, medium, high, or prohibited risk
- routing the request to the right local reviewers
- recording who approved it and who owns it
- deciding whether the use moves into an accountability record
- handling monitoring, appeals, pace concerns, and incidents after approval

## How To Read This Template

- text outside brackets is intended to stay structurally stable across cities
- text inside placeholders must be replaced with local values
- text marked as `[[REQUIRES_LOCAL_DECISION: ...]]` must stay visible until the city decides it
- text marked as `[[REQUIRES_LOCAL_RESEARCH: ...]]` must be researched before drafting is finalized
- text marked as `[[REQUIRES_LEGAL_REVIEW: ...]]` must be reviewed by the city's legal or equivalent authority

## Required Local Inputs

Before adapting this template, the city must identify:

- `[[CITY_NAME]]`
- `[[AI_GOVERNANCE_LEAD_ROLE]]`
- `[[IT_SECURITY_LEAD_ROLE]]`
- `[[EXECUTIVE_APPROVAL_ROLE]]`
- `[[LEGAL_REVIEW_ROLE]]`
- `[[EQUITY_REVIEW_ROLE]]`
- `[[DEPARTMENT_LEADER_ROLE]]`
- `[[CROSS_FUNCTIONAL_GOVERNANCE_BODY]]`
- `[[NAMED_HUMAN_OWNER_TERM]]`
- `[[AI_REGISTER_NAME]]`
- `[[PUBLIC_FEEDBACK_PATH]]`
- `[[INTERNAL_REQUEST_SYSTEM]]`
- `[[APPROVAL_TIMELINE_BY_TIER]]`
- `[[ANNUAL_REVIEW_WINDOW]]`

The city must also decide:

- `[[REQUIRES_LOCAL_DECISION: tier model]]`
- `[[REQUIRES_LOCAL_DECISION: approval chain]]`
- `[[REQUIRES_LOCAL_DECISION: public register model]]`
- `[[REQUIRES_LOCAL_DECISION: pace concern process]]`
- `[[REQUIRES_LOCAL_DECISION: appeal pathway]]`
- `[[REQUIRES_LOCAL_DECISION: incident disclosure threshold]]`
- `[[REQUIRES_LOCAL_DECISION: department supplements]]`

## Core Workflow

1. A use case, tool, request, or internal build is identified.
2. The requester completes intake or self-assessment.
3. A local reviewer assigns a risk tier.
4. The request is routed to the appropriate approval path.
5. Required reviewers sign off or request revision.
6. The approved use is logged in `[[AI_REGISTER_NAME]]` or the city's equivalent accountability record.
7. The owner begins monitoring and reporting obligations.
8. Appeals, pace concerns, and incidents move through their separate paths when needed.

## Review Path Summary

### Tier 1

Tier 1 is for low-risk use.

Default structure:

- low-risk use
- fast approval path
- limited review burden
- clear owner and basic monitoring

Local decisions:

- `[[REQUIRES_LOCAL_DECISION: tier 1 approval chain]]`
- `[[REQUIRES_LOCAL_DECISION: tier 1 monitoring cadence]]`
- `[[REQUIRES_LOCAL_DECISION: tier 1 pre-approved use list model]]`

### Tier 2

Tier 2 is for medium-risk use.

Default structure:

- broader review than Tier 1
- explicit human review before public-facing or materially significant use
- owner and monitoring requirements remain visible

Local decisions:

- `[[REQUIRES_LOCAL_DECISION: tier 2 approval chain]]`
- `[[REQUIRES_LOCAL_DECISION: tier 2 monitoring cadence]]`
- `[[REQUIRES_LOCAL_DECISION: tier 2 legal or procurement review rule]]`

### Tier 3

Tier 3 is for high-risk use.

Default structure:

- stronger executive, legal, and operational scrutiny
- explicit human oversight
- registration and monitoring obligations
- more detailed review packet before approval

Local decisions:

- `[[REQUIRES_LOCAL_DECISION: tier 3 approval chain]]`
- `[[REQUIRES_LOCAL_DECISION: tier 3 review window]]`
- `[[REQUIRES_LOCAL_DECISION: tier 3 council briefing rule]]`
- `[[REQUIRES_LOCAL_DECISION: tier 3 monitoring cadence]]`

### Tier 4

Tier 4 is for prohibited or no-go use.

Default structure:

- not allowed unless the city explicitly creates an exception path
- any exception must be obvious, narrow, and reviewed at the highest appropriate level

Local decisions:

- `[[REQUIRES_LOCAL_DECISION: tier 4 exception policy]]`
- `[[REQUIRES_LOCAL_DECISION: tier 4 exception authority]]`
- `[[REQUIRES_LOCAL_RESEARCH: prohibited use categories]]`

## Intake And Self-Assessment

The intake step must capture:

- purpose
- affected people or services
- data involved
- intended output or decision
- intended owner
- intended department
- intended audience
- known risks
- known dependencies

If the requester cannot answer the required local fields, stop and route to `[[REQUIRES_LOCAL_RESEARCH: intake gap]]` or `[[REQUIRES_LOCAL_DECISION: missing owner]]`.

## Review Routing

The city should route the request to the appropriate reviewers based on tier and topic.

Reusable routing pattern:

- the `[[NAMED_HUMAN_OWNER_TERM]]` submits or initiates the request
- `[[AI_GOVERNANCE_LEAD_ROLE]]` reviews governance fit
- `[[IT_SECURITY_LEAD_ROLE]]` reviews technical and security fit
- `[[LEGAL_REVIEW_ROLE]]` reviews legal and policy fit when required
- `[[EQUITY_REVIEW_ROLE]]` reviews impact and accessibility when required
- `[[DEPARTMENT_LEADER_ROLE]]` reviews operational fit and local authority
- `[[EXECUTIVE_APPROVAL_ROLE]]` handles the highest approval path when required

Local decision marker:

- `[[REQUIRES_LOCAL_DECISION: review routing model]]`

## Approval And Escalation

Approval must be explicit. The workflow should require:

- named approver
- tier assigned
- conditions for approval
- conditions for revision
- conditions for escalation
- conditions for pause or revocation

Required local markers:

- `[[REQUIRES_LOCAL_DECISION: pause authority]]`
- `[[REQUIRES_LOCAL_DECISION: revocation authority]]`
- `[[REQUIRES_LOCAL_DECISION: escalation threshold]]`

## Register Handoff

After approval, the use should be recorded in `[[AI_REGISTER_NAME]]` or the city's equivalent accountability record.

The register record should include:

- owner
- purpose
- tier
- approval date
- approver
- review outcome
- monitoring requirement
- public or internal visibility status

Register choices that stay local:

- `[[REQUIRES_LOCAL_DECISION: public register model]]`
- `[[REQUIRES_LOCAL_DECISION: register publication cadence]]`
- `[[REQUIRES_LOCAL_DECISION: register required fields]]`

## Monitoring

The template should require the owner to define:

- how performance will be checked
- how trust or service quality will be checked
- how material changes are detected
- how issues are escalated
- who receives monitoring reports

Local decisions:

- `[[REQUIRES_LOCAL_DECISION: monitoring cadence]]`
- `[[REQUIRES_LOCAL_DECISION: material change definition]]`
- `[[REQUIRES_LOCAL_DECISION: monitoring owner]]`

## Appeals, Pace Concerns, And Incident Escalation

The workflow must preserve a visible challenge path, a safe way to say the rollout is moving too fast, and a clear post-approval incident path.

Local decisions:

- `[[REQUIRES_LOCAL_DECISION: appeal pathway]]`
- `[[REQUIRES_LOCAL_DECISION: appeal timeline]]`
- `[[REQUIRES_LOCAL_DECISION: appeal authority]]`
- `[[REQUIRES_LOCAL_DECISION: pace concern process]]`
- `[[REQUIRES_LOCAL_DECISION: pace concern response window]]`
- `[[REQUIRES_LOCAL_DECISION: pace concern owner]]`
- `[[REQUIRES_LOCAL_DECISION: incident definition]]`
- `[[REQUIRES_LOCAL_DECISION: incident response path]]`
- `[[REQUIRES_LOCAL_DECISION: incident disclosure threshold]]`
- `[[REQUIRES_LEGAL_REVIEW: incident response obligations]]`

## What Must Stay Out Of The Template

Do not hard-code:

- source-city role names
- source-city dates or SLA values
- source-city routing channels
- one city's department examples as universal defaults
- city-specific legal assumptions

## Completion Criteria

This template is usable when:

- the tier model is visible
- approval and escalation are visible
- register handoff is visible
- monitoring is visible
- appeals are visible
- pace concerns are visible
- incident escalation is visible
- local decisions are still visible where the city has not yet chosen
