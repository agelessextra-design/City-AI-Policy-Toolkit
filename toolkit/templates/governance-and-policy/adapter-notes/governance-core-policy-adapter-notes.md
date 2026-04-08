# Governance Core Policy Adapter Notes

## What This Template Is For

Use `toolkit/templates/governance-and-policy/template-governance-core-policy.md` to create the city's core governance policy for AI use.

This template is the policy spine for the governance family. It is where the city defines:

- what counts as AI for governance purposes
- who the policy applies to
- how risk tiers work at a high level
- what accountability and oversight are required
- what is prohibited
- how review, transparency, and policy maintenance are expected to work

It is not the place to write the entire operating workflow. Workflow detail belongs in `toolkit/templates/governance-and-policy/template-governance-risk-tier-review-workflow.md` and later companion templates.

## When To Use It

Use this template when the city has enough local context to define a governance stance, but has not yet finalized all supporting procedures.

Minimum readiness:

- the city has identified the intended governance scope
- the city can name at least provisional governance, technical, executive, and legal roles
- the city knows whether it wants a tiered review model
- the city is prepared to keep unresolved local decisions visible instead of improvising them

Do not use this template as the first step if the city has not yet gathered:

- local governance ownership
- local legal and procurement context
- basic public accountability expectations
- any sense of which departments or use cases are high risk

## Required Local Inputs

Gather these before adapting the template.

### Required Now

- `[[CITY_NAME]]`
- `[[AI_GOVERNANCE_LEAD_ROLE]]`
- `[[IT_SECURITY_LEAD_ROLE]]`
- `[[EXECUTIVE_APPROVAL_ROLE]]`
- `[[LEGAL_REVIEW_ROLE]]`
- `[[DEPARTMENT_LEADER_ROLE]]`
- whether the city intends to use the pilot four-tier model or a modified version
- the basic approval chain by risk level
- whether the city wants an internal, public, or hybrid accountability record

### Required Before Finalization

- `[[EQUITY_REVIEW_ROLE]]` or local equivalent if applicable
- `[[CROSS_FUNCTIONAL_GOVERNANCE_BODY]]` if the city uses one
- `[[AI_REGISTER_NAME]]`
- `[[PUBLIC_FEEDBACK_PATH]]`
- `[[INTERNAL_REQUEST_SYSTEM]]`
- `[[LANGUAGE_ACCESS_REQUIREMENTS]]`
- `[[PROCUREMENT_AUTHORITY]]`
- `[[PRIVACY_COMPLIANCE_FRAMEWORK]]`
- `[[ANNUAL_REVIEW_WINDOW]]`

### May Be Researched In Parallel

- the city’s actual budget and planning cadence
- which departments need supplements
- whether a preferred-vendor approach is useful
- whether a pace-concern process should be formalized
- whether appeals should be handled inside this governance family or in a separate process

## Fixed Sections

These sections should stay structurally fixed across cities:

- Purpose
- Scope
- Definitions
- Core Principles
- Governance Model
- Approval And Escalation
- Accountability
- Review And Monitoring
- Transparency And Public Accountability
- Internal Tools And Shadow AI
- Procurement And Vendor Review
- Prohibited Uses
- Policy Maintenance

Why:

- these are the minimum governance elements the source family consistently supports
- removing them weakens accountability, reviewability, or public-sector fit

## Flexible Sections

These elements are expected to vary by city:

- role titles
- approval authorities
- register structure and publication model
- legal and procurement references
- language-access and accessibility commitments
- timelines and review windows
- which departments get supplements
- whether specific advanced modules launch now or later

Flexibility rule:

- change local values and structure where needed
- do not remove the underlying governance function unless the city is intentionally deferring it

## Placeholder Handling

Guidance:

- resolve label placeholders when the city has a confirmed local answer
- leave `[[REQUIRES_LOCAL_DECISION: ...]]` markers visible until a city decision exists
- leave `[[REQUIRES_LOCAL_RESEARCH: ...]]` markers visible until the fact is verified
- do not replace a missing role with a generic title just to make the text read smoothly

## Legal And Risk Gates

Do not treat legal review as a proofreading pass.

Flag these before the draft advances:

- procurement clauses and vendor obligations
- privacy and records requirements
- sensitive-data restrictions
- employment or labor implications
- public accountability and disclosure claims
- civil-rights, accessibility, or equity obligations
- authority language for approvals, pause rights, and appeals

If the city has not reviewed these areas, keep the markers visible.

## Research Gates

Research is required before finalizing the draft where the city does not yet know:

- who actually owns AI governance
- who approves by tier
- which privacy and records rules apply
- what procurement gates already exist
- what public-language and accessibility requirements apply
- what the city’s routing system is
- which departments need extra governance coverage

The right output for a missing fact is a research task, not a guess.

## Common Mistakes

Avoid these:

- hard-coding CAIO, CIO, or City Manager roles as if every city uses them
- copying source-city timelines or fiscal structure into reusable text
- collapsing the governance family into one giant AI policy
- smoothing away unresolved decisions to make the draft sound finished
- hiding legal review inside narrative prose
- treating the public accountability layer as optional decoration
- copying department examples as universal defaults

## Template To Outline Workflow

Use this sequence:

1. Read the template and this adapter note together.
2. Capture all required local inputs.
3. Mark unresolved local decisions explicitly.
4. Resolve straightforward placeholders only where the city has evidence.
5. Keep legal and research markers visible.
6. Convert the template into an adapted outline that preserves section order.
7. Hand the adapted outline into the governance pilot draft workflow.

The outline should be accepted before drafting prose.

## Completion Criteria

The adapter pass is complete when:

- required local roles are named or explicitly missing
- all legal and research gates are visible
- all local-decision markers are still visible where unresolved
- the outline can be drafted without inventing a city structure
- the city team can explain why each section exists

## Open Questions To Carry Forward

- Should the AI register remain core-required or maturity-gated in the public toolkit?
- Should the toolkit eventually standardize a generic advisory-body label?
- Should experienced cities be allowed to skip some intake steps when context is already documented?
