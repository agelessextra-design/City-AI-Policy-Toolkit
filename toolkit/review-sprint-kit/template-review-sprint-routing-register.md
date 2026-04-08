# Review Sprint Routing Register

## Purpose

Use this register after a review sprint to route revisions, track aging issues, and keep unresolved major issues from disappearing.

## Routing Table

| Item ID | Source Issue ID | Section | Decision State | Revision Owner | Supporting Reviewer | Due Window | Escalation Trigger | Current Status |
|---|---|---|---|---|---|---|---|---|
| RR-001 | ISS-001 |  |  |  |  |  |  | open |

## Field Guidance

- `Decision State`: accepted change, rejected change, deferred for local decision, requires legal review, requires research, requires rewrite and re-evaluation
- `Revision Owner`: person or role doing the next edit
- `Supporting Reviewer`: optional reviewer who must confirm the fix
- `Due Window`: near-term expected completion window
- `Escalation Trigger`: when this item must return to the main agent, legal review, or a later sprint

## Usage Rules

- every sprint decision that creates follow-up work should appear here
- do not let major items remain ownerless
- route changed sections to targeted signoff where possible
- if a change reopens structure or authority assumptions, escalate rather than hiding it in local edits
