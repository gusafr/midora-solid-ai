# Architecture

The solid.ai architecture connects six interdependent layers. Each layer is modular yet synchronized through shared contracts, data flows, and governance policies.

## Layer Overview

1. **Purpose Layer** – Sets strategic intent, missions, and ethical guardrails.
2. **Data Spine** – Provides unified access to data products, observability, and lineage.
3. **Cognitive Layer** – Hosts AI agents, orchestration engines, and learning loops.
4. **Automation Mesh** – Executes cross-domain workflows through event-driven automation.
5. **Organizational Layer** – Defines human and AI team topology, roles, and rituals.
6. **Governance & Ethics Layer** – Ensures compliance, accountability, and trust.

## Integration Patterns

- **Event Streams:** Connect Cognitive outputs to Automation actions using shared event schemas.
- **Contracts:** APIs, data products, and prompts share versioned contracts stored in the Data Spine.
- **Feedback Loops:** Telemetry from the Automation Mesh and Organizational Layer feeds learning systems.

## Technology Agnostic

solid.ai is intentionally technology-neutral. It focuses on patterns that can be implemented with cloud-native, on-premises, or hybrid stacks. Reference implementations may use tools such as:

- Data: Lakehouse platforms, semantic layers, data catalogs.
- Cognitive: Orchestration frameworks (e.g., MAGI), LLM service layers, agent runtimes.
- Automation: Low-code orchestrators, BPMN engines, event-driven platforms, RPA.
- Observability: OpenTelemetry, model monitoring solutions, governance dashboards.

## Interoperability

- Use open standards wherever possible (JSON Schema, AsyncAPI, OpenAPI, SQL, GraphQL).
- Provide adapters for proprietary systems while preserving transparent interfaces.
- Expect multiple AI providers; design for model-agnostic orchestration.

## Resilience and Fail-Safes

- Design layered fallback modes for critical processes.
- Establish human-in-the-loop checkpoints for high-risk decisions.
- Monitor saturation points (compute cost, data freshness, queue depth) and trigger alerts.

## Diagram

See `DIAGRAMS/solid-ai-architecture.mmd` for a Mermaid representation of the layer interactions.
---

## Next Steps

**Deep Dive into Each Layer:**
- [Principles](01-principles.md) — Foundational principles that govern each layer
- [Organizational Model](03-organizational-model.md) — How squads and pools implement the Organizational Layer
- [AI Agents](05-ai-agents.md) — Defining the Cognitive Layer with AI agents
- [Automation SIPOC](04-automation-sipoc.md) — Patterns for the Automation Layer

**Governance & Operations:**
- [Governance & Ethics](06-governance-ethics.md) — Accountability across all layers
- [Observability](07-observability.md) — Monitor health of all 6 layers

**Apply to Your Context:**
- [Playbooks](../PLAYBOOKS/) — See architecture in action across sectors
- [Reference Cards](../ADOPTION/REFERENCE-CARDS/) — AI prompts aligned to each layer

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
