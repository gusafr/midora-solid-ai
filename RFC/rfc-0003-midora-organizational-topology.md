# RFC-0003: Midora Organizational Topology

- **Status:** Draft
- **Authors:** Gustavo Freitas, Midora Education Labs
- **Created:** 2025-11-02
- **Issue:** #3 (placeholder)
- **Supersedes:** None
- **Related RFCs:** RFC-0001
- **Related ADRs:** None

## Summary

Define Midora's specific organizational topology implementing the solid.ai framework through lean Product Triad squads, six specialized capability pools, and fully automated operational areas governed by SIPOC matrices.

## Motivation

While solid.ai provides the foundational framework for AI-native organizations, Midora requires a concrete implementation that balances:
- **Lean squad structures** for agility and outcome focus
- **Specialized pools** for deep expertise and reusable capabilities
- **100% operational automation** to scale without manual overhead
- **Hybrid human-AI collaboration** across all organizational layers

This RFC codifies Midora's specific topology as a reference implementation of the solid.ai framework.

## Proposal

### 1. Squad Structure: Product Triad

Each squad consists of a **three-person core** forming a Product Triad:

| Role | Responsibilities | Framework Layer Alignment |
|------|-----------------|---------------------------|
| **Product Owner** | Purpose alignment, stakeholder management, value prioritization | Purpose Layer |
| **System Architect** | Technical design, data contracts, AI agent orchestration | Data Spine + Cognitive Layer |
| **Project Manager** | Execution coordination, dependencies, observability tracking | Automation Mesh + Organizational Layer |

**Key Characteristics:**
- Squads are **outcome-oriented**, not project-bound
- Each triad role can be filled by a **human or AI agent**
- Squads draw on pools for specialized skills (development, QA, design, etc.)
- Squads maintain accountability for end-to-end delivery

### 2. Pool Structure: Six Capability Hubs

| Pool | Core Responsibilities | Framework Layer | Engagement Model |
|------|----------------------|-----------------|------------------|
| **Multidisciplinary Developers** | Backend, frontend, AI/ML, data engineering, mobile development | Cognitive + Automation Mesh | Embedded in squads or on-demand pairing |
| **PMO Pool** | Portfolio governance, budget tracking, financial planning, capacity management | Organizational Layer | Oversight and reporting dashboards |
| **Agile Coaching Pool** | Process optimization, retrospective facilitation, continuous improvement | Organizational Layer | Embedded coaches, workshops, metrics analysis |
| **Quality Pool** | System QA, process QA, compliance testing, observability validation | Governance & Ethics Layer | Embedded testers, automated quality gates |
| **Portfolio Pool** | Market strategy, product engineering, go-to-market, customer research | Purpose Layer | Strategic roadmap input, user insights |
| **Solutions Architecture Pool** | Cross-functional technical leadership, platform decisions, architecture governance | Data Spine + Cognitive Layer | Technical reviews, ADR approval, platform evolution |

### 3. Operational Automation via SIPOC

All operational areas (finance, HR, infrastructure, compliance) operate under **100% automation principles**:

1. **SIPOC Mapping:** Every operational process documented as a SIPOC matrix
2. **Automation-First:** No manual execution; all processes orchestrated by the Automation Mesh
3. **Human Oversight:** Humans curate policies, review exceptions, and improve automations
4. **Continuous Learning:** Feedback loops feed observability data back to process refinement

**Example SIPOC Matrix (Finance Operations):**

| Stage | Description | Implementation |
|-------|-------------|----------------|
| **Suppliers** | Accounting system, bank APIs, employee expense platform | Integrated data sources |
| **Inputs** | Invoices, receipts, payroll data, budget allocations | Automated ingestion via APIs |
| **Process** | Validation → Approval routing → Payment execution → Reconciliation | Event-driven workflow orchestration |
| **Outputs** | Financial reports, compliance logs, payment confirmations | Auto-generated dashboards |
| **Customers** | CFO, auditors, leadership council, pool leads | Real-time access to financial health |

## Implementation Details

### Midora's Technology Landscape

Midora's technical architecture is organized into four primary systems:

| System | Domain | Components | Purpose |
|--------|--------|------------|---------|
| **midora-core** | Platform | Backend services, API gateway, IDP backstage | Core infrastructure and service mesh |
| **midora-intelligence** | Intelligence | ML service, MAGI orchestration | AI/ML capabilities and agent orchestration |
| **learning-apps** | Learning Experience | Frontend apps (Flutter, TypeScript), course generator, legacy portal | Student-facing applications and content delivery |
| **content-pipeline** | Content | Course generator service workers | Automated content generation and curation |

**Key Repositories:**
- `midora-back-end-py` — Core backend services (Python)
- `midora-api-openapi` — API specifications and contracts
- `midora-ml-service` — ML model serving and inference
- `midora-magi-py` — Multi-agent orchestration (MAGI pattern)
- `midora-course-generator-py` — Automated course content generation
- `midora-front-end-fl-v2` — Modern Flutter-based learning app
- `midora-front-end-ts` — TypeScript web application
- `midora-portal-ph` — Legacy PHP portal (maintenance mode)
- `midora-idp-backstage` — Internal Developer Platform (Backstage)

### Squad-Pool Collaboration Model

1. **Squad Formation:** Product Triad assembles based on outcome (e.g., "Launch AI-powered assessment engine")
2. **Pool Engagement:** Squad requests capabilities from pools via intake boards
3. **Repository Alignment:** Squads typically own 1-3 related repositories within a system domain
4. **Embedded vs On-Demand:** 
   - Developers: Embedded full-time in squads, working across system boundaries
   - QA: Embedded during sprint cycles, validating across repositories
   - Agile Coaches: On-demand for retrospectives and process audits
   - PMO: Oversight through automated dashboards tracking multi-repo metrics
   - Portfolio: Strategic input at quarterly planning
   - Solutions Architecture: Technical reviews ensuring cross-system coherence

### Human vs AI Agent Allocation

**Phase 1 (Current State):**
- Product Owners: 100% human
- System Architects: 100% human
- Project Managers: 70% human, 30% AI-assisted (scheduling, reporting)
- Developers: 100% human with AI co-pilots
- QA: 50% human exploratory testing, 50% automated AI agents
- Coaches: 100% human
- PMO: 80% automated dashboards, 20% human strategic oversight

**Phase 2 (6-12 months):**
- Project Managers: 40% human, 60% AI agents with human oversight
- Developers: Hybrid pairing (human creativity + AI code generation)
- QA: 30% human, 70% AI agents
- PMO: 90% automated with AI-generated insights

**Phase 3 (12-24 months):**
- Fully adaptive: AI agents autonomously handle routine decisions
- Humans focus on purpose alignment, ethics, and creative innovation
- All roles support both human and AI agent occupants

### Metrics and Observability

| Metric Category | Key Indicators | Frequency |
|----------------|----------------|-----------|
| **Squad Health** | Cycle time, delivery rate, stakeholder satisfaction | Weekly |
| **Pool Utilization** | Capacity vs demand, reuse rate, expertise coverage | Biweekly |
| **Automation Coverage** | % of operational processes automated, manual intervention rate | Monthly |
| **AI Agent Performance** | Decision accuracy, escalation rate, learning velocity | Weekly |
| **Organizational Coherence** | Cross-squad alignment, RFC approval time, knowledge sharing | Monthly |

### Example: AI Assessment Squad Implementation

**Outcome:** "Launch AI-powered personalized assessment engine"

**Product Triad:**
- **Product Owner:** Head of Learning Experience (Human)
- **System Architect:** AI Engineering Lead (Human)
- **Project Manager:** AI Agent ("AssessmentPM-01") with human oversight

**Repository Scope:**
- Primary: `midora-ml-service` (new assessment model endpoints)
- Secondary: `midora-magi-py` (assessment orchestration logic)
- Tertiary: `midora-front-end-fl-v2` (student assessment UI)
- Supporting: `midora-api-openapi` (assessment API contracts)

**Pool Engagements:**
- **Multidisciplinary Developers:** 2 ML engineers (embedded), 1 Flutter developer (embedded)
- **Quality Pool:** 1 QA engineer (embedded for 4 weeks)
- **Solutions Architecture:** Code reviews on MAGI integration patterns
- **Data Pool:** On-demand support for assessment data modeling
- **PMO Pool:** Automated dashboard tracking progress across 4 repos

**Automation Mesh Integration:**
- SIPOC for automated model retraining pipeline
- Event-driven triggers for assessment result notifications
- Automated quality gates in CI/CD across all 4 repositories

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Triad bottlenecks** | Squad blocked by single role unavailability | Cross-train backup roles; AI agents as fallback |
| **Pool fragmentation** | Competing priorities across squads | PMO pool coordinates capacity allocation |
| **Over-automation** | Loss of human judgment in edge cases | Mandatory human checkpoints for high-risk decisions |
| **AI agent drift** | Agents deviate from purpose or ethics | Continuous observability + Governance Circle reviews |
| **Knowledge silos** | Pool expertise not accessible to squads | Playbooks, RFC documentation, learning sessions |

## Success Criteria

1. **Squad Velocity:** 90% of squads meet quarterly outcome commitments
2. **Pool Response Time:** <2 days from request to engagement
3. **Operational Automation:** 95% of operational processes execute without manual intervention
4. **AI Agent Integration:** At least 30% of Project Manager and QA roles filled by AI agents within 12 months
5. **Coherence:** <5% of RFCs rejected due to misalignment with framework principles

## Alternatives Considered

### Traditional Functional Teams
- **Rejected:** Too slow for AI-native pace; creates handoff inefficiencies

### Fully Autonomous Squads (No Pools)
- **Rejected:** Leads to duplicated effort and expertise gaps

### Matrix Organizations
- **Rejected:** Ambiguous accountability; conflicts with purpose-driven clarity

### Manual Operations
- **Rejected:** Doesn't scale; contradicts AI-native principles

## Open Questions

1. How do we handle squad transitions when outcomes are achieved? (Dissolve or pivot?)
2. What's the right ratio of embedded vs on-demand pool engagement?
3. Should Solutions Architecture pool have veto power over technical decisions?
4. How do we ensure fair AI agent "hiring" across squads?

## Decision

Pending review by Governance Circle and operational leadership.

## References

- RFC-0001: solid.ai Foundations
- DOCS/03-organizational-model.md
- PLAYBOOKS/playbook-squads.md
- PLAYBOOKS/playbook-pools.md
- DOCS/04-automation-sipoc.md
