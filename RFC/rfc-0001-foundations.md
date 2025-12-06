# RFC-0001: solid.ai Foundations

- **Status:** Draft
- **Authors:** Gustavo Freitas
- **Created:** 2025-11-02
- **Issue:** #1 (placeholder)
- **Supersedes:** None
- **Related ADRs:** ADR-0001

## Summary

Establish the solid.ai framework as the organizational nervous system for AI-native companies, defining purpose, architectural layers, governance principles, and documentation strategy.

## Motivation

Organizations adopting AI at scale lack a cohesive model that integrates purpose, data, intelligence, automation, and human structures. This RFC codifies foundational concepts to guide future RFCs, ADRs, and playbooks.

## Proposal

1. Adopt the Manifesto v1.0 as the primary philosophical artifact.
2. Define six layers: Purpose, Data Spine, Cognitive, Automation Mesh, Organizational, Governance & Ethics.
3. Create repository structure with documentation, diagrams, RFC/ADR processes, and playbooks.
4. Publish documentation via MkDocs Material and GitHub Pages.

## Details

- Manifesto content curated in `MANIFESTO/solid-ai-manifesto-v1.md`.
- Numbered docs in `DOCS/` describe principles, architecture, organizational model, automation SIPOC, AI agents, governance & ethics, and observability.
- Mermaid diagrams in `DIAGRAMS/` visualize layer interaction, safe AI models, and organizational flows.
- Playbooks deliver operational guidance for squads, pools, operations, and AI integration.

## Risks & Mitigations

| Risk | Mitigation |
| --- | --- |
| Overlap with other frameworks | Provide clear mappings and interoperability guidance |
| Documentation drift | Enforce RFC/ADR references in PR checklist |
| Governance complexity | Introduce lightweight governance circle rituals |

## Alternatives Considered

- **Pure technical reference:** Rejected; lacks organizational context.
- **Vendor-specific blueprint:** Rejected; conflicts with open standard goals.

## Unresolved Questions

- Hosting location and cadence for community discussions.
- Tooling stack for automation examples in future releases.

## Decision

Pending community review.
