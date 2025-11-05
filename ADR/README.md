# Architecture Decision Records (ADRs)

This directory contains Architecture Decision Records documenting critical architectural and technical decisions made in the SOLID.AI Framework.

## What is an ADR?

An **Architecture Decision Record** (ADR) captures an important architectural decision along with its context and consequences. ADRs help teams:
- Understand why decisions were made (rationale)
- Evaluate alternatives that were considered
- Track the evolution of the architecture over time
- Onboard new contributors quickly

## Format

Each ADR follows this structure:
1. **Title:** Concise description of the decision
2. **Status:** Proposed | Accepted | Deprecated | Superseded
3. **Context:** Problem being solved, constraints, requirements
4. **Decision:** What was decided and how it works
5. **Consequences:** Positive outcomes, trade-offs, risks
6. **Alternatives Considered:** Other options and why they were rejected
7. **Implementation:** How to apply the decision
8. **Validation:** Proof that it works (metrics, tests, examples)
9. **References:** Related documentation, external resources

## Active ADRs

### ADR-0001: Adopt Mermaid for Diagrams
- **Status:** ✅ Accepted
- **Date:** 2025-11-02
- **Decision:** Use Mermaid (.mmd) as canonical diagramming language
- **Rationale:** Version-controlled, Markdown-friendly, MkDocs integration
- **Impact:** All framework diagrams created with Mermaid (21+ diagrams)
- **File:** [adr-0001-mermaid-choice.md](adr-0001-mermaid-choice.md)

---

### ADR-0002: Business Service Organization for Squads
- **Status:** ✅ Accepted
- **Date:** 2025-11-05
- **Decision:** Squads MUST be organized around business services (bounded contexts), not technical layers
- **Rationale:** Enables autonomy, clear ownership, scalable growth, eliminates coordination overhead
- **Impact:** Foundational organizational principle; 11 framework files updated
- **Examples:** Order Fulfillment, Customer Onboarding, Fraud Detection, Invoice Processing
- **File:** [adr-0002-business-service-organization.md](adr-0002-business-service-organization.md)

**Related Resources:**
- [Organizational Model](../DOCS/03-organizational-model.md)
- [Squad Playbook](../PLAYBOOKS/organizational/squads.md)
- [Squad Formation Checklist](../ADOPTION/CHECKLISTS/squad-formation.md)
- [Squad Charter Template](../ADOPTION/TEMPLATES/squad-charter-template.md)
- [Diagram: Business Service Organization](../DIAGRAMS/squad-business-service-organization.mmd)
- [Quick Reference](../ADOPTION/REFERENCE-CARDS/squad-organization-quick-ref.md)

---

### ADR-0003: Required Data Spine and Automation Mesh Integration
- **Status:** ✅ Accepted
- **Date:** 2025-11-05
- **Decision:** Every business service MUST integrate with Data Spine + Automation Mesh (4 required integrations)
- **Rationale:** Makes services observable, measurable, governed, and automated
- **Impact:** 22-item integration checklist, 8 framework files updated
- **Requirements:**
  1. **Data Spine Integration** (7 items): Contracts, events, observability, governance
  2. **Automation Mesh Integration** (7 items): SIPOC, event-driven, error handling
  3. **OKRs & KPIs** (4 items): Service-level objectives, dashboards, business value
  4. **Data Governance** (4 items): Event ownership, compliance, audit logging
- **File:** [adr-0003-data-spine-automation-mesh-integration.md](adr-0003-data-spine-automation-mesh-integration.md)

**Related Resources:**
- [Architecture](../DOCS/02-architecture.md)
- [Squad Playbook - Integration Section](../PLAYBOOKS/organizational/squads.md#critical-data-spine--automation-mesh-integration)
- [Squad Formation Checklist - Integration Items](../ADOPTION/CHECKLISTS/squad-formation.md)
- [Squad Charter Template - Integration Sections](../ADOPTION/TEMPLATES/squad-charter-template.md)
- [Diagram: Full Integration Architecture](../DIAGRAMS/business-service-full-integration.mmd)
- [Integration Update Summary](../BUSINESS-SERVICE-ARCHITECTURE-INTEGRATION-UPDATE.md)

---

### ADR-0004: ReportLab for PDF Book Generation
- **Status:** ✅ Accepted
- **Date:** 2025-11-05
- **Decision:** Use ReportLab (pure Python) for PDF generation instead of WeasyPrint
- **Rationale:** Windows compatibility, zero external dependencies, fast and reliable
- **Impact:** 350-page PDF book generation works on all platforms
- **Performance:** 18 seconds, 0.71 MB file size, <100 MB memory
- **File:** [adr-0004-reportlab-pdf-generation.md](adr-0004-reportlab-pdf-generation.md)

**Related Resources:**
- [PDF Generator Script](../scripts/generate_pdf_book_reportlab.py)
- [Windows Fix Documentation](../PDF-GENERATOR-WINDOWS-FIX.md)

**Supersedes:** WeasyPrint approach (informal, no ADR)

---

## Deprecated ADRs

None yet.

---

## Superseded ADRs

None yet.

---

## Creating a New ADR

### When to Create an ADR

Create an ADR when making decisions about:
- **Architecture:** Core framework layers, integration patterns
- **Technology:** Tool choices, library selection (if not trivial)
- **Organizational:** Squad models, role structures, governance
- **Process:** Development workflows, deployment strategies (if significant)

**Don't create an ADR for:**
- Minor implementation details
- Content updates (documentation, examples)
- Bug fixes
- Refactoring without architectural change

### ADR Template

```markdown
# ADR-XXXX: [Decision Title]

**Status:** Proposed | Accepted | Deprecated | Superseded  
**Date:** YYYY-MM-DD  
**Deciders:** [Team/Person]  
**Related:** [Other ADRs, RFCs, files]

---

## Context

[Problem being solved, constraints, requirements, business impact]

---

## Decision

[What was decided, how it works, technical details]

---

## Consequences

### Positive Outcomes
[Benefits, improvements, capabilities enabled]

### Trade-offs
[Costs, limitations, complexity added]

### Risks & Mitigations
[Potential issues and how to address them]

---

## Alternatives Considered

### Alternative 1: [Name]
**Pros:** [Benefits]  
**Cons:** [Drawbacks]  
**Why Rejected:** [Reason]

---

## Implementation

[How to apply this decision, steps, examples]

---

## Validation

[Proof that it works: metrics, tests, examples, files updated]

---

## References

**Internal Documentation:**
- [Link to related docs]

**External Resources:**
- [Link to books, articles, standards]

---

**Status:** [Current status]  
**Date:** [Original date]  
**Version:** [Version number]  
**ADR Sponsor:** [Team/Person]  
**Supersedes:** [Previous ADR if any]  
**Superseded by:** [Later ADR if any]
```

### ADR Numbering

ADRs are numbered sequentially:
- ADR-0001, ADR-0002, ADR-0003, etc.
- Leading zeros for sorting (up to 4 digits: 0001-9999)
- File naming: `adr-XXXX-kebab-case-title.md`

### ADR Process

1. **Draft:** Create ADR in `Proposed` status
2. **Review:** Circulate for feedback (team, community)
3. **Decide:** Accept, reject, or iterate
4. **Document:** Update status to `Accepted`
5. **Implement:** Apply the decision
6. **Validate:** Confirm it works in practice

### Updating ADRs

ADRs are **immutable once accepted**. If a decision changes:
1. Create a new ADR with `Superseded` status pointing to the new ADR
2. Update the new ADR with `Supersedes: ADR-XXXX` reference
3. Update this index to show deprecated/superseded ADRs

---

## ADR Statistics

- **Total ADRs:** 4
- **Active:** 4 (100%)
- **Deprecated:** 0 (0%)
- **Superseded:** 0 (0%)
- **Average Length:** ~800 lines (comprehensive documentation)

**Coverage:**
- Diagramming: 1 ADR (Mermaid)
- Organizational: 2 ADRs (Business Services, Integration)
- Technical: 1 ADR (PDF Generation)

---

## References

**ADR Methodology:**
- Nygard, Michael. "Documenting Architecture Decisions" (2011)
- ThoughtWorks Technology Radar - ADR practice
- GitHub ADR Organization: https://adr.github.io/

**SOLID.AI Framework:**
- [Core Documentation](../DOCS/)
- [Playbooks](../PLAYBOOKS/)
- [Adoption Pack](../ADOPTION/)
- [Diagrams](../DIAGRAMS/)

---

**Maintained by:** SOLID.AI Framework Team  
**Last Updated:** 2025-11-05  
**License:** MIT
