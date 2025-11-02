# Contributing to solid.ai

First off—thank you for helping shape the solid.ai framework. We welcome issues, ideas, documentation updates, and new playbooks that advance ethical, adaptive, AI-native organizations.

## Contribution Workflow

1. **Open an Issue**
   - Describe the change you propose, link to prior discussions, and outline expected impact.
   - Label the issue (`docs`, `rfc`, `adr`, `playbook`, `manifesto`, etc.) to guide triage.
2. **Draft an RFC**
   - For evolutions to the core architecture, governance, or operating model, create a Request for Comments in `/RFC/` using the `rfc-XXXX-title.md` naming convention.
   - Reference the issue number in the document header.
3. **Submit a Pull Request**
   - Branch from `dev`; include the RFC or ADR in the PR description.
   - Ensure documentation, diagrams, and playbooks stay synchronized.
4. **Merge & Update Docs**
   - Once approved, merge into `main` via the PR. Update related documentation, diagrams, and changelog entries where applicable.

## Architecture Decision Records (ADRs)

- Capture technical decisions in `/ADR/` using the `adr-XXXX-title.md` pattern.
- Link ADRs to the RFC or issue that prompted the decision.
- When superseding a decision, update the status in both ADRs.

## Manifesto Changes

- The manifesto is versioned: `MANIFESTO/solid-ai-manifesto-v1.md`.
- Propose updates via RFC. Approved revisions should increment the semantic version (e.g., `v1.1`, `v2.0`).
- Include a summary of changes and rationale in the pull request description.

## Documentation & Diagrams

- Documentation lives under `/DOCS/`. Each numbered file is ordered within the MkDocs navigation.
- Diagrams use Mermaid (`.mmd`). Keep diagrams updated when underlying flows or models change.
- Run `mkdocs serve` to preview documentation prior to submitting a PR.

## Style Guidelines

- Write in accessible, inclusive language.
- Use present tense and active voice wherever possible.
- Call out assumptions, dependencies, and observability expectations.
- Favor tables, lists, and diagrams when they improve readability.

## Development Setup

- Requirements: Python 3.9+, `pip`, and `mkdocs-material`.
- Optional tooling: `pre-commit`, `markdownlint`, Mermaid live preview extensions.
- Keep commits focused. Squash or rebase before merging if asked by maintainers.

## Community & Support

- GitHub Discussions (coming soon) will host community RFC debates and office hours.
- For urgent matters or conduct concerns, email `conduct@solid.ai`.

We are building a living framework. Thank you for bringing your expertise and curiosity to solid.ai.
