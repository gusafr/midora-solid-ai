# Organizational Model

solid.ai organizes humans and AI agents into adaptive structures optimized for co-creation, learning, and resilience.

## Structural Elements

--8<-- "DIAGRAMS/organizational-flow.mmd"

- **Squads:** Cross-functional units focused on delivering customer or stakeholder outcomes. **Organized around business services** (bounded contexts) to ensure clear ownership, minimize dependencies, and avoid duplication.
- **Pools:** Shared capability hubs (e.g., Data, AI Ops, Design) that provide expertise on demand.
- **Cognitive Agents:** AI teammates embedded in squads or pools with defined responsibilities.
- **Governance Circle:** Multi-disciplinary group that reviews ethics, observability, and compliance.

### Squad Organization Principle: Business Service Ownership

--8<-- "DIAGRAMS/squad-business-service-organization.mmd"

Squads are **anchored to business services**, not technical layers or temporary features. This ensures:

1. **No Duplication:** Each business service has exactly one owning squad
2. **Clear Boundaries:** Services have well-defined inputs/outputs (data contracts)
3. **Autonomous Operation:** Squads can deliver end-to-end without constant handoffs
4. **Scalable Growth:** New squads = new business services (not reorganizing existing ones)
5. **Integrated Architecture:** Each service properly integrated with Data Spine and Automation Mesh

**Example Business Services:**
- Customer Onboarding (not "Frontend Squad")
- Order Fulfillment (not "Logistics Team")  
- Fraud Detection (not "ML Platform Team")
- Invoice Processing (not "Finance Automation")

Each service is self-contained, outcome-focused, and maps directly to stakeholder value.

### Required Integrations for Every Business Service

--8<-- "DIAGRAMS/business-service-full-integration.mmd"

**1. Data Spine Integration:**
- Input/output data contracts (schema, SLA, versioning)
- Business events catalog (domain events the service owns)
- Event stakeholders (who consumes your events)
- Observability dashboards (metrics, lineage, quality)
- Data governance (PII classification, retention, access controls)

**2. Automation Mesh Integration:**
- SIPOC workflow mapping (suppliers → inputs → process → outputs → customers)
- Automation strategy (AI-automated vs. human-in-loop steps)
- Event-driven architecture (subscriptions and publications)
- Error handling (retry policies, circuit breakers, dead letter queues)

**3. OKRs & KPIs:**
- Service-level objectives aligned with business strategy
- Real-time KPI dashboards (business impact, efficiency, quality, AI augmentation)
- Quarterly review cadence with stakeholders

**4. Data Governance:**
- Event ownership (squad is authoritative source for domain events)
- Breaking change policy (RFC process for schema changes)
- Compliance requirements (GDPR, SOX, HIPAA, PCI-DSS)
- Audit logging (all data access tracked)

**Benefits of Integrated Services:**
- **Observability:** Real-time visibility into service health and business impact
- **Reusability:** Other services safely consume your events (event-driven architecture)
- **Autonomy:** Squad owns end-to-end delivery without dependencies
- **Measurability:** Business value tracked continuously via OKRs/KPIs
- **Compliance:** Data governance enforced automatically
- **AI-Native:** Automation opportunities explicit in SIPOC mapping

See [Squad Playbook](../PLAYBOOKS/organizational/squads.md) for detailed integration requirements.

## Operating Rhythm

| Cadence | Activity | Participants |
| --- | --- | --- |
| Weekly | Outcome review & adaptive planning | Squad leads, embedded agents |
| Biweekly | Governance sync | Governance Circle members, compliance officers |
| Monthly | Portfolio alignment | Executive sponsors, pool leads |
| Quarterly | Strategy iteration & manifesto review | Leadership council |

## Decision Flows

1. Squads identify opportunities and produce RFC drafts.
2. Pools validate feasibility, data readiness, and AI agent design.
3. Governance Circle assesses ethical impact and observability requirements.
4. Approved RFCs trigger updates to playbooks, automation flows, and documentation.

## Roles & Responsibilities

- **Human Lead:** Maintains purpose alignment and stakeholder engagement.
- **AI Orchestrator:** Automates data gathering, summarization, and decision support.
- **Ops Steward:** Ensures compliance, telemetry, and incident response readiness.
- **Learning Curator:** Synthesizes feedback, publishes retrospectives, updates knowledge bases.

## Talent Development

- Promote rotational programs between squads and pools to diffuse expertise.
- Provide AI literacy training and ethical decision-making workshops.
- Encourage shared ownership of AI-assisted deliverables.

## Change Management

- Major structural shifts require RFC approval.
- ADRs document tooling and platform choices that impact organizational behavior.
- Retired structures should leave a knowledge trail in playbooks and docs.
---

## Next Steps

**Understand Squad Roles:**
- [Human-AI Collaboration](08-human-ai-collaboration.md) — Human vs. AI responsibilities
- [Role Hierarchy](10-role-hierarchy-human-ai.md) — Career progression within squads

**Integrate with Agile:**
- [AI-Native Agile](11-ai-native-agile.md) — Blend squads with Scrum/SAFe
- [Automation SIPOC](04-automation-sipoc.md) — Workflow patterns for squads

**Form Your First Squad:**
- [Adoption Pack](../ADOPTION/) — Squad charter template and checklist
- [Playbooks](../PLAYBOOKS/) — Sector-specific squad configurations

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
