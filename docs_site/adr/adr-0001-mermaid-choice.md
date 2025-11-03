# ADR-0001: Adopt Mermaid for Diagrams

- **Status:** Accepted
- **Context:** 2025-11-02
- **Deciders:** Gustavo Freitas, Midora Education Labs
- **Consulted:** solid.ai community (early contributors)
- **Related RFCs:** RFC-0001, RFC-0002

## Context

solid.ai documentation requires clear, version-controlled diagrams to represent architecture, organizational flows, and governance models. Contributors need a lightweight format that fits well with Markdown-first workflows and integrates with MkDocs.

## Decision

Adopt Mermaid (`.mmd`) as the canonical diagramming language for the repository.

## Consequences

- Diagrams live in version control and are easy to review via diffs.
- MkDocs Material can render Mermaid diagrams without additional tooling.
- Contributors can edit diagrams with any text editor or Mermaid-compatible UI tools.
- Future tooling can export Mermaid diagrams to SVG or PNG for presentations.

## Alternatives Considered

- **Draw.io / Excalidraw:** Provide rich visual editing but harder to diff and automate.
- **PlantUML:** Powerful but requires additional setup and Java runtime for previews.
- **Static Images:** Simple but limit collaboration and increase maintenance overhead.
