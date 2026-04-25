#!/usr/bin/env python3
"""Validate the public City AI Policy Toolkit bundle."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    "LICENSE",
    "SECURITY.md",
    ".github/pull_request_template.md",
    ".github/workflows/validate.yml",
    "docs/README.md",
    "docs/quickstart/start-here.md",
    "docs/quickstart/use-with-ai-assistants.md",
    "docs/workflow/workflow-overview.md",
    "toolkit/README.md",
    "toolkit/asset-promotion-manifest.md",
    "toolkit/templates/README.md",
    "toolkit/templates/module-family-index.md",
    "toolkit/prompts/README.md",
    "toolkit/prompts/module-family-index.md",
    "toolkit/evaluations/evaluation-entry-index.md",
    "toolkit/review-sprint-kit/review-entry-index.md",
    "examples/example-entry-index.md",
    "scripts/validate_public_bundle.py",
]

PROMPT_PACKS = [
    "toolkit/prompts/strategic-leadership/prompt-pack-strategic-leadership.md",
    "toolkit/prompts/strategic-leadership/prompt-pack-strategic-leadership-hardening.md",
    "toolkit/prompts/governance-and-policy/prompt-pack-governance-pilot.md",
    "toolkit/prompts/governance-and-policy/prompt-pack-governance-hardening.md",
    "toolkit/prompts/workforce-and-learning/prompt-pack-workforce-learning.md",
    "toolkit/prompts/workforce-and-learning/prompt-pack-workforce-learning-hardening.md",
    "toolkit/prompts/operations-and-service-delivery/prompt-pack-operations-service-delivery.md",
    "toolkit/prompts/operations-and-service-delivery/prompt-pack-operations-service-delivery-hardening.md",
    "toolkit/prompts/community-trust/prompt-pack-community-trust.md",
    "toolkit/prompts/community-trust/prompt-pack-community-trust-hardening.md",
]

TEMPLATE_FAMILIES = [
    "strategic-leadership",
    "governance-and-policy",
    "workforce-and-learning",
    "operations-and-service-delivery",
    "community-trust",
]

BUILD_PACK_HEADINGS = ["Intake", "Outline", "Draft", "Evaluation"]
HARDENING_PACK_HEADINGS = ["Repair", "Contradiction Resolution", "Upgrade", "Board Prep"]


def all_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and path.is_file()
    )


def line_number(text: str, index: int) -> int:
    return text[:index].count("\n") + 1


def validate_required_files(errors: list[str]) -> None:
    for relpath in REQUIRED_FILES:
        if not (ROOT / relpath).is_file():
            errors.append(f"missing required file: {relpath}")


def validate_markdown_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    inline_path_pattern = re.compile(r"`((?:docs|toolkit|examples|\.github|scripts)/[^`\s,;:)]+)`")

    for path in all_markdown_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        rel_file = path.relative_to(ROOT)

        for match in link_pattern.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if not target or re.match(r"^[a-z]+://", target) or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                continue
            if not resolved.exists():
                errors.append(
                    f"{rel_file}:{line_number(text, match.start())}: broken markdown link: {target}"
                )

        for match in inline_path_pattern.finditer(text):
            target = match.group(1).rstrip(".,")
            if target.endswith("/"):
                continue
            if not (ROOT / target).exists():
                errors.append(
                    f"{rel_file}:{line_number(text, match.start())}: missing referenced path: {target}"
                )


def validate_prompt_packs(errors: list[str]) -> None:
    for relpath in PROMPT_PACKS:
        path = ROOT / relpath
        if not path.is_file():
            errors.append(f"missing prompt pack: {relpath}")
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        expected = HARDENING_PACK_HEADINGS if "hardening" in path.name else BUILD_PACK_HEADINGS
        for heading in expected:
            if heading not in text:
                errors.append(f"{relpath}: missing expected prompt section containing '{heading}'")


def validate_template_families(errors: list[str]) -> None:
    for family in TEMPLATE_FAMILIES:
        family_dir = ROOT / "toolkit" / "templates" / family
        if not family_dir.is_dir():
            errors.append(f"missing template family directory: toolkit/templates/{family}")
            continue
        templates = list(family_dir.glob("template-*.md"))
        if not templates:
            errors.append(f"missing template file in family: toolkit/templates/{family}")
        if not (family_dir / "adapter-notes").is_dir():
            errors.append(f"missing adapter-notes directory in family: toolkit/templates/{family}")


def validate_public_boundary(errors: list[str]) -> None:
    blocked_patterns = [
        r"control-room",
        r"numbered workspace",
        r"Main Orchestrator",
        r"Agent\.",
        r"\[\[MAINTAINER_CONTACT_CHANNEL\]\]",
    ]
    for path in all_markdown_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        rel_file = path.relative_to(ROOT)
        for pattern in blocked_patterns:
            match = re.search(pattern, text, flags=re.IGNORECASE)
            if match:
                errors.append(
                    f"{rel_file}:{line_number(text, match.start())}: public-boundary term found: {match.group(0)}"
                )


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)
    validate_markdown_links(errors)
    validate_prompt_packs(errors)
    validate_template_families(errors)
    validate_public_boundary(errors)

    if errors:
        print("Public bundle validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Public bundle validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
