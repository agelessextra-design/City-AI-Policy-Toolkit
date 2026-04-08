# [[CITY_NAME]] AI Governance Core Policy

## Purpose

This policy sets the core governance rules for how [[CITY_NAME]] uses artificial intelligence in public-sector work.

It defines the citywide standards for accountability, risk review, oversight, prohibited uses, monitoring, transparency, and policy maintenance.

This policy is the structural spine of the governance toolkit. Role-specific guidance, workflow details, and local implementation choices belong in companion documents.

## Scope

This policy applies to:

- all city employees
- contractors and vendors acting on behalf of the city
- internally built tools, scripts, macros, automations, prompts, and dashboards that use AI
- vendor tools, hosted tools, and free or publicly available AI services when used for city work

This policy does not replace:

- role-based guidance
- department-specific supplements
- procurement procedures
- incident response procedures
- training materials
- legal, privacy, or accessibility requirements that must be mapped locally

[[REQUIRES_LOCAL_DECISION: department supplements]]

## Definitions

For this policy, an AI system means any software, platform, script, macro, automation, custom prompt, chatbot, model, or dashboard that uses artificial intelligence, machine learning, or large language model technology to generate, analyze, predict, classify, or recommend.

An AI system can be:

- purchased
- subscribed to
- built internally
- embedded in another product
- accessed through a free web interface

[[REQUIRES_LOCAL_RESEARCH: local legal and privacy definitions]]

### Key Terms

- `[[NAMED_HUMAN_OWNER_TERM]]`: the person responsible for the AI system before and after approval
- `[[AI_GOVERNANCE_LEAD_ROLE]]`: the role that coordinates AI governance for the city
- `[[IT_SECURITY_LEAD_ROLE]]`: the role that reviews technical and security implications
- `[[EXECUTIVE_APPROVAL_ROLE]]`: the role that provides final executive approval where required
- `[[LEGAL_REVIEW_ROLE]]`: the role that reviews legal, procurement, privacy, or records implications
- `[[EQUITY_REVIEW_ROLE]]`: the role that reviews equity, accessibility, or public impact issues where applicable
- `[[CROSS_FUNCTIONAL_GOVERNANCE_BODY]]`: the citywide advisory or review body for AI governance

[[REQUIRES_LOCAL_DECISION: approval chain]]

## Core Principles

[[CITY_NAME]] uses AI only in ways that support public service, human accountability, and public trust.

The city will:

- keep human judgment visible
- use proportionate review
- make responsible ownership explicit
- protect sensitive data
- explain important AI uses to the extent required by local policy or law
- review and update governance as the city learns

The city will not:

- let AI replace human accountability
- use AI as an excuse to hide responsibility
- deploy AI into prohibited uses
- treat a tool as approved just because it is available

## Governance Model

The city uses a tiered governance model to match review depth to risk.

[[REQUIRES_LOCAL_DECISION: tier model]]

### Tier 1

Tier 1 covers low-risk uses that can move quickly with basic oversight.

Typical Tier 1 uses may include:

- drafting internal material
- summarizing public information
- routine research support
- scheduling or administrative assistance

Tier 1 uses must still have:

- a named human owner
- a clear intended use
- a review path defined by the city
- basic monitoring after use begins

[[APPROVAL_TIMELINE_BY_TIER]]

### Tier 2

Tier 2 covers medium-risk uses that need broader review before use becomes routine or public-facing.

Tier 2 uses must have:

- explicit human review
- clear ownership
- review of public impact, data use, and operational fit
- any required legal, privacy, or procurement review identified locally

[[REQUIRES_LOCAL_DECISION: public register model]]

### Tier 3

Tier 3 covers high-risk uses that affect residents, rights, benefits, employment, enforcement, safety, or other material decisions.

Tier 3 uses must have:

- explicit executive and governance review where required locally
- human oversight built into the workflow
- monitoring after deployment
- clear escalation and incident response expectations

[[REQUIRES_LOCAL_DECISION: prohibited uses]]

### Tier 4

Tier 4 covers uses that the city prohibits or only allows through an explicit exception path.

The city must define:

- which uses are prohibited
- whether any exception path exists
- who can authorize that exception, if anyone

[[REQUIRES_LOCAL_DECISION: appeal pathway]]

## Approval And Escalation

No AI system may be used for city work until the required local review path is complete.

The local review path must identify:

- who initiates review
- who approves the use
- who can pause use
- who hears appeals
- who receives escalation when something goes wrong

The city should not assume that one office owns every decision.

[[REQUIRES_LOCAL_DECISION: approval chain]]
[[REQUIRES_LOCAL_DECISION: pace concern process]]

## Accountability

Every deployed AI system must have a named human owner.

The named human owner is responsible for:

- the approved use of the system
- keeping the system within approved scope
- coordinating updates when the system changes materially
- responding when the system creates an issue

The city must also define:

- the governance lead role
- the technical review role
- the executive approval role
- the legal review role
- the equity or inclusion review role, if applicable

## Review And Monitoring

The city will review AI use before it is deployed and after it is in use.

Review must consider:

- whether the use is still within the approved scope
- whether the system or vendor has changed
- whether the risk level has changed
- whether new legal, procurement, privacy, or accessibility issues have emerged

The city must decide locally:

- the review cadence
- who performs monitoring
- what counts as a material change
- what happens when monitoring finds a problem

[[REQUIRES_LOCAL_DECISION: transparency cadence]]
[[REQUIRES_LOCAL_DECISION: incident disclosure threshold]]

## Transparency And Public Accountability

The city will maintain a public accountability path for AI use appropriate to its local policy and legal requirements.

At minimum, the city should define:

- how residents can learn what AI is used
- how residents can raise a concern
- how the city records or registers approved AI systems
- how the city explains material changes

[[AI_REGISTER_NAME]]
[[PUBLIC_FEEDBACK_PATH]]

The city must decide locally whether the accountability record is:

- internal only
- public only
- hybrid

## Internal Tools And Shadow AI

Internal tools, scripts, prompts, automations, and dashboards that use AI are covered by this policy.

The city must not treat internal tools as exempt just because they were built in-house.

The city should define a path for:

- self-disclosure of undocumented tools
- review of internally built tools
- registration or logging of approved internal tools
- handling of good-faith builders

[[REQUIRES_LOCAL_DECISION: preferred vendor policy]]
[[REQUIRES_LOCAL_RESEARCH: local internal tool inventory]]

## Procurement And Vendor Review

AI tools and services purchased or contracted by the city must go through the city’s local procurement and review process.

The city must identify locally:

- procurement authority
- legal review requirements
- privacy and security review requirements
- records obligations
- vendor monitoring expectations

[[REQUIRES_LOCAL_RESEARCH: procurement rules]]
[[REQUIRES_LEGAL_REVIEW: procurement clauses]]
[[PROCUREMENT_AUTHORITY]]

## Prohibited Uses

The city must define a list of prohibited AI uses.

The prohibited-use list should be explicit enough that staff do not have to guess.

At minimum, the city should decide whether to prohibit:

- fully automated decisions that affect residents without human review
- uses that process sensitive data without approval
- uses that create unacceptable surveillance or discrimination risk
- uses that violate local law, labor requirements, records obligations, or public trust commitments

[[REQUIRES_LOCAL_DECISION: prohibited uses]]
[[REQUIRES_LEGAL_REVIEW: civil rights and accessibility implications]]

## Appeals And Pace Concerns

The city should provide a way to challenge a risk classification, approval decision, or rollout pace when concerns arise.

The city must decide locally:

- whether the appeal path is formal or lightweight
- who hears the appeal
- how long the appeal can take
- whether pace concerns pause a rollout or only trigger review

[[REQUIRES_LOCAL_DECISION: appeal pathway]]
[[REQUIRES_LOCAL_DECISION: pace concern process]]

## Incident Response

If an AI system causes harm, creates a serious concern, or appears to be operating outside approved scope, the city must be able to pause it and review it.

The city must define locally:

- who can pause use
- who is notified
- how incidents are documented
- what the post-incident review path is
- when public communication is required

[[REQUIRES_LOCAL_DECISION: incident disclosure threshold]]
[[REQUIRES_LEGAL_REVIEW: incident and liability language]]

## Policy Review And Change Management

This policy must be reviewed on a recurring schedule and whenever a major trigger occurs.

Recurring review should consider:

- changes in law
- changes in city priorities
- changes in risk categories or approved uses
- major incidents or recurring issues
- changes in vendor behavior or system capability

[[ANNUAL_REVIEW_WINDOW]]
[[BUDGET_CYCLE_REFERENCE]]

The city must decide locally:

- the annual review window
- the approval authority for policy updates
- whether department supplements are required

[[REQUIRES_LOCAL_DECISION: department supplements]]

## Local Completion Criteria

Before this policy is treated as complete for a city, the city should have:

- named its local governance lead
- identified the local approval chain
- identified local legal, procurement, privacy, and accessibility requirements
- resolved the tier model or marked it as configurable
- determined whether the register is internal, public, or hybrid
- determined whether appeals and pace concerns are formal features
- identified which companion documents are needed

## Placeholder And Flag Summary

This template intentionally leaves the following visible:

- placeholders for local roles and systems
- local decision points
- legal review gates
- research gates

The template should not be considered complete until those items are resolved by the city.
