# Issue Aging And Escalation Guide

## Purpose

This guide defines how unresolved issues should age and when they must be escalated instead of silently rolling forward.

Use it to keep the review loop disciplined after sprint sessions.

## Aging Model

### Critical

- blocks advancement immediately
- must be assigned before the current stage closes
- escalates to the main agent if still open after the next revision pass

### Major

- should be fixed before human review or public promotion
- escalates if it survives two consecutive revision loops without a justified accepted-risk decision

### Moderate

- should be fixed in the current or next planned loop
- escalates only if it starts affecting readiness, contradiction status, or reviewer trust

### Minor

- does not block progression alone
- should still be recorded for cleanup

## Escalation Triggers

Escalate when:

- an issue changes meaning, authority, threshold, or delivery posture
- the same issue reappears in multiple loops
- a major issue remains open with no owner
- a contradiction survives the latest revision pass
- a review packet is being assembled with unresolved blocking items

## Required Escalation Targets

- structural or ontology drift -> main orchestrator
- legal or procurement boundary issues -> legal owner plus main orchestrator
- repeated readiness failures -> evaluation owner
- repeated sprint-routing failures -> review-sprint owner
