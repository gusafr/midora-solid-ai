# Glossary

## Core Framework Terms

| Term | Definition |
| --- | --- |
| **SOLID.AI** | Strategic Organization Leveraging Intelligent Design for AI. A comprehensive framework for AI-native organizations where humans and AI agents collaborate as teammates. |
| **Intelligent Hybrid Organization** | The ultimate goal of SOLID.AI: An enterprise where humans and AI agents work as peers in a sustainable, scalable, and ethically governed ecosystem. Characterized by hybrid workforce, intelligent operations, sustainable scalability, ethical governance, and adaptive evolution. |
| **AI-Native Organization** | An organization where all functions (not just IT) operate at AI speed through human-AI collaboration. A key milestone toward becoming an Intelligent Hybrid Organization. |
| **Bipolar Organization** | Anti-pattern where IT operates at digital speed (agile, AI-assisted) while business functions remain analog (manual, hierarchical), creating organizational dysfunction. |
| **Whole-Organization Coherence** | The principle that ALL functions must transform together (Sales, Finance, HR, Marketing, Operations) to achieve sustainable competitive advantage and build an Intelligent Hybrid Organization. |

## Organizational Structure

| Term | Definition |
| --- | --- |
| **Squad** | Cross-functional, outcome-oriented team of 3-7 humans + AI agents organized around a **business service** (not technical layers). Owns end-to-end delivery. In Scaled Scrum models, squads are grouped into Communities. |
| **Communities (Scaled Scrum)** | Groups of related squads organized around shared domains, technologies, or business capabilities (e.g., Customer Experience Community, Data Platform Community, AI/ML Community). Communities facilitate knowledge sharing, technical standards, and cross-squad collaboration while maintaining squad autonomy. Types include Communities of Practice (CoP) and Business Communities. |
| **Pool** | Shared capability hub (e.g., Data, AI Ops, Design) that provides specialized expertise on demand to multiple squads. |
| **Business Service** | A self-contained capability that delivers stakeholder value with clear inputs/outputs. Examples: Customer Onboarding, Order Fulfillment, Fraud Detection. Squads are anchored to business services, not features or technical layers. |
| **Bounded Context** | Domain-Driven Design concept defining clear boundaries for a business service. Each service owns its data models, business logic, and domain events. |
| **MIDORA Topology** | Organizational design pattern: **M**odular (clear boundaries), **I**ntelligent (data-driven), **D**ecentralized (edge autonomy), **O**bservable (transparent), **R**esilient (fault-tolerant), **A**daptive (continuous learning). |
| **Governance Circle** | Multi-disciplinary group overseeing ethics, compliance, and decision quality across the organization. |

## Team Composition

| Term | Definition |
| --- | --- |
| **Mixed Team** | Squad composition including both humans and AI agents as peers (e.g., 3 humans + 2 AI agents). Default recommendation for most use cases. |
| **AI-Only Team** | Squad composed entirely of AI agents with periodic human oversight. Used for 24/7 operations, extreme scale, or dangerous/repetitive work. |
| **Human-Only Team** | Squad composed entirely of humans. Used when empathy, trust, strategic judgment, or ethical gray zones are paramount (e.g., executive leadership, crisis counseling). |

## AI Agent Concepts

| Term | Definition |
| --- | --- |
| **AI Agent** | Autonomous software entity with defined identity, role, capabilities, guardrails, and accountability. Operates as a workforce member, not a tool. Synonymous with "Cognitive Agent". |
| **Cognitive Agent** | See **AI Agent**. Terms are interchangeable in SOLID.AI framework. |
| **Cognitive Workforce** | The collection of AI agents operating as accountable teammates with defined roles, responsibilities, and success metrics. |
| **Agent Identity** | An AI agent's name, role, persona, and level (e.g., "LeadQualifier-Agent, Low-Level Assistant, diligent researcher"). |
| **Agent Capabilities** | Specific tasks an AI agent can perform (e.g., "Score 500 leads/day", "Generate variance reports"). |
| **Agent Guardrails** | Rules defining what an AI agent is prohibited from doing (e.g., "Do not auto-approve invoices >$5K") and boundaries requiring escalation. |
| **Human Oversight** | Required human review and approval for AI agent decisions. Varies by autonomy level (supervised, co-pilot, automated, advisory-only). |

## Role Hierarchy

| Term | Definition |
| --- | --- |
| **Low Level (Assistant/Analyst)** | Entry-level roles focused on **tactical asset delivery** (code, reports, tasks). Linear scalability, procedural work, supervised autonomy. Examples: SDR, Data Analyst, InvoiceProcessor-Agent. |
| **Intermediate Level (Consultant/Coordinator)** | Mid-level roles focused on **coordination & expertise** (workflows, advice). Process efficiency, semi-autonomous. Examples: Sales Engineer, Program Manager, DemoPersonalizer-Agent. |
| **High Level (Specialist/Manager)** | Senior roles focused on **scalable solution creation** (architecture, strategy). Exponential impact, high creativity, autonomous. Examples: Principal Engineer, Sales Manager, SupplyChainOptimizer-Agent. |
| **Executive Level (Director)** | Leadership roles focused on **strategic vision & transformation**. Organizational impact, visionary creativity, governing authority. Examples: VP Engineering, CFO, StrategicPlanning-Agent. |
| **Role Progression** | Career advancement pathway from Low → Intermediate → High → Executive based on scalability impact, creativity, and autonomy. Applies to both humans and AI agents. |

## AI Autonomy Levels

| Term | Definition |
| --- | --- |
| **Supervised** | AI agent requires human approval before every action. Used for Low-Level agents (100% oversight). |
| **Co-Pilot** | AI agent provides recommendations, human makes final decision. Used for Intermediate/High-Level agents (20-50% oversight). |
| **Automated** | AI agent acts independently, human reviews exceptions. Used for High-Level agents (5-10% oversight). |
| **Advisory-Only** | AI agent provides strategic analysis only, never takes action. Used for Executive-Level agents (100% human decision). |

## Architecture Layers

| Term | Definition |
| --- | --- |
| **Purpose Layer** | Foundational layer setting strategic intent, missions, ethical guardrails, and human oversight. |
| **Data Spine** | Unified data foundation that governs access, quality, observability, and contracts across the organization. |
| **Cognitive Layer** | Layer responsible for intelligence—AI agents, orchestration engines, and learning systems. |
| **Automation Mesh** | Network of orchestrated workflows connecting AI, data, and human actions across the organization. |
| **Organizational Layer** | Layer defining human and AI team topology, roles, rituals, and adaptive structures. |
| **Governance & Ethics Layer** | Layer ensuring compliance, accountability, transparency, and trust across all operations. |

## Data & Integration

| Term | Definition |
| --- | --- |
| **Data Contract** | Formal agreement defining schema, SLA, versioning, and ownership for data shared between services. Enforced by Data Spine. |
| **Event-Driven Architecture** | Design pattern where services communicate via asynchronous events (e.g., "OrderPlaced", "PaymentCompleted"). Enables loose coupling and scalability. |
| **Business Event** | Domain-specific event published by a business service (e.g., "CustomerOnboarded", "FraudDetected"). Consumed by other services for integration. |
| **Data Lineage** | Tracking where data originates, how it transforms, and where it flows. Critical for governance and debugging. |

## Workflow Patterns

| Term | Definition |
| --- | --- |
| **SIPOC** | Supplier-Input-Process-Output-Customer model used to map workflows and identify automation opportunities. Aligns processes with purpose and ethics. |
| **Automation Strategy** | Decision framework for which workflow steps are AI-automated vs. human-in-loop vs. fully manual. Documented in SIPOC mapping. |

## Governance & Compliance

| Term | Definition |
| --- | --- |
| **Human Curatorship** | The principle that human oversight remains the moral compass for all AI-driven decisions. |
| **Observability** | The practice of instrumenting systems to make internal states visible through metrics, logs, and traces. |
| **Ops Steward** | Role responsible for ensuring observability, compliance, and incident response readiness. |
| **Audit Trail** | Immutable log of all AI agent decisions and human interventions. Required for compliance and governance. |

## Agile Integration

| Term | Definition |
| --- | --- |
| **AI-Native Agile** | Integration of AI agents into Scrum/SAFe workflows (ceremonies, value streams, Portfolio/Program/Team levels). Accelerates delivery 64% (17 weeks → 6 weeks). |
| **Epic** | Large feature or initiative in Agile workflow, decomposed into Features → Stories → Tasks → Code. |
| **Value Stream** | End-to-end flow of work from concept to customer value delivery. AI agents accelerate every stage. |

## Documentation

| Term | Definition |
| --- | --- |
| **ADR (Architecture Decision Record)** | Lightweight document capturing a significant technical decision, context, and consequences. |
| **RFC (Request for Comments)** | Proposal document for material changes to architecture, governance, or organizational design. |
| **Manifesto** | Foundational narrative defining purpose, principles, and roadmap for SOLID.AI. |
| **Playbook** | Task-oriented guide describing how squads, pools, or operations implement the framework. |

## Metrics & Performance

| Term | Definition |
| --- | --- |
| **OKR (Objectives & Key Results)** | Goal-setting framework aligning squad objectives with organizational strategy. Reviewed quarterly. |
| **KPI (Key Performance Indicator)** | Measurable metric tracking business impact, efficiency, quality, or AI augmentation. Monitored real-time. |
| **SLA (Service Level Agreement)** | Commitment to response time, uptime, or quality (e.g., "99.9% uptime", "< 5 min response time"). |

## Implementation Tools

| Term | Definition |
| --- | --- |
| **MAGI** | Reference orchestration pattern for coordinating multiple models and agents (pluggable implementation). |
| **Living Architecture** | Design philosophy treating the organization as a living organism that learns and evolves continuously. |

---

## Next Steps

**Start Learning:**
- [Overview](00-overview.md) — Framework introduction
- [Reading Paths](README.md) — Recommended learning sequence
- [Quick Start Guide](../QUICK-START-GUIDE.md) — 5-minute introduction

**Deep Dive:**
- [Architecture](02-architecture.md) — Understand all 6 layers
- [AI Agents](05-ai-agents.md) — Define AI teammates
- [AI-Native Agile](11-ai-native-agile.md) — Integrate with Scrum/SAFe

**Get Started:**
- [Adoption Pack](../ADOPTION/) — Templates, checklists, prompts
- [Playbooks](../PLAYBOOKS/) — Sector-specific guides

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
