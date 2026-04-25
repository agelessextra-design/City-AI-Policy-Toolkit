# Contributing

Thanks for helping improve the City AI Policy Toolkit.

This contribution guide explains how to keep public toolkit changes usable, reusable, and reviewable.

## What Contributions Should Improve

- reusable toolkit content
- clarity of workflow guidance
- placeholder discipline
- evaluation and review mechanics
- example labeling and adaptation notes
- public documentation quality

## What Contributions Should Not Do

- introduce workspace-only planning artifacts into the public repo
- blur the line between reusable toolkit material and city-specific source material
- remove visible local decisions just to make text look finished
- add automation before the repo structure is stable
- publish raw reverse-engineering notes as final guidance

## Before You Open A Change

Please include:

- what module or folder the change belongs to
- what stage of the workflow it affects
- which assumptions you made
- which open questions remain
- which files changed

If the change depends on local city facts, keep those facts explicit and do not generalize them by accident.

## Content Rules

- keep naming consistent with the toolkit folder structure
- use placeholder tokens when a value is intentionally unresolved
- keep examples clearly labeled as examples
- keep evaluation materials aligned with the issue taxonomy and review workflow
- keep public docs readable without requiring access to the internal workspace

## Review Expectations

Expect maintainers to check:

- whether the change is reusable beyond one city
- whether the change preserves the public/internal boundary
- whether the wording introduces hidden assumptions
- whether the artifact belongs in the public repo at all

If a submission belongs in the internal build workspace instead of the public repo, it should be redirected rather than merged.

## Suggested Contribution Checklist

- [ ] The change is scoped to one module or doc set
- [ ] The change does not leak workspace-only internals
- [ ] The change keeps unresolved decisions visible
- [ ] The change uses consistent naming and placeholders
- [ ] The change includes enough context for review

## Questions And Follow-Up

If you are unsure whether something belongs in the public repo, raise the question in review rather than guessing.

For now, use a concise issue description and include:

- the affected file path
- the intended audience
- the reason the change is reusable
- any local assumptions that still need resolution
