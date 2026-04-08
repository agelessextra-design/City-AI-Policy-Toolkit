# Board Review Scorecard Template

## Purpose

Use this scorecard for board-style milestone reviews once a batch is stable enough for external-lens scrutiny.

This template supports the three planned review lenses:

- `Board.OpenAI`
- `Board.Claude`
- `Board.Gemini`

## Scorecard Header

- review date:
- board lens:
- milestone batch:
- reviewer:
- overall decision:

## Core Review Questions

| Question | Score (0-4) | Evidence | Main Concern |
|---|---:|---|---|
| Is the workflow clear and executable? |  |  |  |
| Can a normal user proceed safely without hidden context? |  |  |  |
| Are evaluation and review gates credible? |  |  |  |
| Does the toolkit show full-system completeness? |  |  |  |
| Is the packaging and onboarding path strong enough for adoption? |  |  |  |
| Would you allow this batch to move closer to public release? |  |  |  |

## Review-Lens Emphasis

### `Board.OpenAI`

Focus on:

- workflow clarity
- toolability
- evaluation rigor
- prompt and skill discipline
- end-to-end execution logic

### `Board.Claude`

Focus on:

- structure
- user guidance
- handoff quality
- reasoning quality
- safe usability for a normal user

### `Board.Gemini`

Focus on:

- completeness
- scale readiness
- public-sector robustness
- comparison logic
- packaging readiness

## Pass / Fail Reasons

### Pass Reasons

- 

### Fail Reasons

- 

## Routed Findings

- issue-log rows added:
- sections affected:
- immediate owner:

## Board Average

Use this after all three scorecards exist:

```text
board_average = (OpenAI + Claude + Gemini) / 3
```
