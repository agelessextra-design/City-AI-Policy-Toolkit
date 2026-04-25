# [[CITY_NAME]] AI Service Delivery Operating Playbook

## Purpose

This playbook defines how [[CITY_NAME]] moves approved AI initiatives from intake through deployment, support, monitoring, and improvement.

It is intended for operational leaders, service owners, digital teams, and cross-functional partners who need a shared delivery model.

## Scope

This playbook applies to:

- approved internal workflow automations using AI
- resident-facing service changes that use AI
- analytics or decision-support tools used in operational environments
- vendor-hosted or internally configured AI tools supporting city services

This playbook does not replace:

- governance approval requirements
- procurement or contracting controls
- workforce enablement plans
- resident notice or public accountability materials

## Service Delivery Principles

Operational AI work should:

- start from a clear service problem or operational need
- assign a named service owner and named delivery owner
- match rollout depth to service risk
- include testing, support, and rollback planning
- document resident or staff impact before scale-up
- generate evidence for continuous improvement

## Intake And Prioritization

The city should define how new AI-enabled service ideas enter the operational pipeline.

The intake path should identify:

- requesting department
- service problem being addressed
- expected users and affected populations
- data and system dependencies
- required governance tier or review path
- staffing, procurement, and support implications

[[REQUIRES_LOCAL_DECISION: operational intake owner]]
[[REQUIRES_LOCAL_RESEARCH: current project, ticket, or innovation intake channels]]

## Delivery Stages

The city should use explicit stages rather than treating implementation as one step.

Recommended stages:

- problem framing
- feasibility and dependency check
- pilot design
- testing and validation
- launch decision
- monitored production use
- review, pause, scale, or retirement

The city may rename stages, but should preserve the logic.

## Roles And Ownership

Every operational AI initiative should name:

- `[[SERVICE_OWNER_ROLE]]`
- `[[DELIVERY_OWNER_ROLE]]`
- `[[TECHNICAL_SUPPORT_OWNER_ROLE]]`
- `[[GOVERNANCE_LIAISON_ROLE]]`
- `[[RESIDENT_SUPPORT_OR_COMMUNICATIONS_ROLE]]` when applicable

If the city does not have distinct roles, the document should say so explicitly rather than imply a mature operating model that does not exist.

## Testing And Readiness

Before launch, the city should define minimum testing expectations.

Testing may include:

- workflow testing with real users or designated reviewers
- output-quality testing against representative scenarios
- accessibility and language testing where resident interaction is involved
- data and recordkeeping checks
- fallback and rollback testing

The city must decide:

- which tests are mandatory by risk level
- who approves readiness to launch
- what evidence is required for scale-up

[[REQUIRES_LOCAL_DECISION: launch-readiness authority]]

## Rollout And Change Control

Rollout should be intentional.

The playbook should specify:

- whether rollout is pilot-only, phased, or citywide
- how the city handles material changes to tools, models, prompts, or vendors
- when a changed workflow must return to governance review
- how staff and managers are notified about changes

[[REQUIRES_LOCAL_DECISION: material change threshold]]

## Support And Incident Handling

The city must define where service or tool problems go once a system is live.

At minimum, specify:

- support intake channel
- who triages operational issues
- who can pause or disable the tool
- how resident-impacting incidents are escalated
- how fixes and lessons learned are tracked

[[REQUIRES_LOCAL_DECISION: pause authority]]
[[REQUIRES_LOCAL_RESEARCH: incident and service management baseline]]

## Vendor And Data Dependencies

Operational AI work often depends on vendors, internal platforms, and sensitive datasets.

The city should identify:

- vendor support expectations
- contract or service-level dependencies
- data refresh and retention obligations
- recordkeeping responsibilities
- security and privacy review checkpoints

[[REQUIRES_LEGAL_REVIEW: vendor obligations and records impacts]]

## Resident Experience And Service Equity

If a use case affects residents, the city should define:

- what the resident experiences directly
- how residents can request help or correction
- what accessibility and language-access supports apply
- how the city avoids creating a two-tier service experience

[[OPTIONAL_IF: use case is internal only]]
[[REQUIRES_LOCAL_DECISION: resident support channel]]

No resident-facing or resident-adjacent launch should proceed unless the draft names:

- a reachable complaint or concern intake owner
- a response target
- an escalation owner for material complaints or resident-impacting incidents

If the permanent owner is not yet decided, use an interim owner marker rather than leaving the field blank.

## Metrics And Continuous Improvement

The city should measure whether the operational change is actually helping.

Measures may include:

- service timeliness
- quality or error trends
- staff workload effects
- resident satisfaction or complaints
- incident frequency
- tool utilization within approved scope

For this city, operational measures include:

- `[[OPERATIONS_MEASURE_1]]`
- `[[OPERATIONS_MEASURE_2]]`
- `[[OPERATIONS_MEASURE_3]]`

## Review And Retirement

The city should specify:

- how often active services are reviewed
- what triggers a pause, redesign, or retirement
- who decides whether a pilot becomes a standing service
- how lessons are carried into future deployments

[[REQUIRES_LOCAL_DECISION: retirement decision authority]]
