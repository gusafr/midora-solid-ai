# ADR-0002: Business Service Organization for Squads

**Status:** ✅ Accepted  
**Date:** 2025-11-05  
**Deciders:** Framework Team  
**Related:** ADR-0001 (Mermaid for diagrams), DOCS/03-organizational-model.md, PLAYBOOKS/organizational/squads.md

---

## Context

AI-native organizations need clear squad boundaries to enable:
- Autonomous deployment (3x/week vs. quarterly releases)
- Clear ownership (one source of truth per capability)
- Minimal coordination overhead (no cross-team handoffs)
- Scalable growth (add squads without reorganization)

Traditional squad organization approaches fail in AI-native contexts:

**Anti-Pattern 1: Technical Layer Organization**
- Frontend Squad, Backend Squad, Database Squad, QA Squad
- **Problem:** Every feature requires 4-team coordination → slow delivery
- **Impact:** 2-4 week lead time due to handoffs

**Anti-Pattern 2: Feature-Based Organization**
- "Shopping Cart Feature Squad," "Search Feature Squad"
- **Problem:** Temporary scope leads to frequent reorganization → knowledge loss
- **Impact:** 30-40% productivity loss during reorgs

**Anti-Pattern 3: Arbitrary Division**
- "Squad A," "Squad B," "Squad C" (no clear boundaries)
- **Problem:** Duplicate efforts, unclear ownership
- **Impact:** 20-30% wasted effort on duplicated work

Without a clear organizational principle, companies struggle to scale beyond 50-100 people.

---

## Decision

**Squads MUST be organized around business services (bounded contexts from Domain-Driven Design), not technical layers, features, or arbitrary divisions.**

### Definition of Business Service

A **business service** is a self-contained capability that:
1. Delivers specific business value independently
2. Has clear stakeholders/end users
3. Owns end-to-end delivery (not just one technical layer)
4. Has explicit input/output contracts
5. Can succeed without constant cross-team coordination
6. Has sustainable scope (not too broad, not too narrow)

### Examples of Valid Business Services

**E-Commerce:**
- Order Fulfillment (purchase → payment → inventory → shipping)
- Customer Onboarding (signup → verification → activation)
- Returns & Refunds (request → validation → refund → restock)
- Fraud Detection (analysis → risk scoring → alerts)

**SaaS:**
- Subscription Management (plans → billing → cancellation)
- Usage Analytics & Billing (metering → aggregation → invoicing)
- Integration Marketplace (connector catalog → OAuth → sync)

**Finance:**
- Invoice Processing (ingestion → validation → approval → payment)
- Payment Processing (authorization → settlement → reconciliation)
- Regulatory Reporting (data collection → audit → submission)

### Validation Criteria

Before forming a squad, answer 6 questions:

1. **What business capability does this serve?**
2. **Who are the end users/stakeholders?**
3. **What value does it deliver independently?**
4. **What are the clear input/output contracts?**
5. **Can this squad succeed without constant coordination?**
6. **Is the scope sustainable (not too broad/narrow)?**

If any answer is unclear → service boundary needs refinement.

---

## Consequences

### Positive Outcomes

✅ **Clear Ownership**
- One squad = one source of truth for a business capability
- No "whose job is this?" confusion
- Accountability is explicit

✅ **Autonomous Delivery**
- Squads deploy independently 3x/week (vs. quarterly releases)
- No cross-team approval chains
- No handoff delays

✅ **No Duplication**
- Service boundaries prevent duplicate implementations
- Shared capabilities exposed as events/contracts (Data Spine)
- DRY principle at organizational level

✅ **Scalable Growth**
- New business capability = new squad (clear trigger)
- No reorganization needed as company grows 50 → 100 → 500 people
- Knowledge stays with squad (no reorg churn)

✅ **Value Alignment**
- Squad OKRs/KPIs map directly to business outcomes
- Revenue/cost/NPS impact is measurable per squad
- No "activity theater" (story points without business value)

### Trade-offs

⚠️ **Initial Effort Required**
- Teams must learn Domain-Driven Design (DDD) concepts
- Service boundary definition requires upfront analysis (5-10 hours)
- May require refactoring existing organizational structure

⚠️ **Shared Capabilities Challenge**
- Some capabilities (Design, DevOps, Data) don't fit service model
- **Solution:** Pool model (on-demand support for all squads)
- Documented in DOCS/03-organizational-model.md

⚠️ **Cross-Service Workflows**
- Business processes may span multiple services (e.g., Order → Fulfillment → Returns)
- **Solution:** Event-driven architecture via Data Spine (ADR-0003)
- Services communicate asynchronously, no tight coupling

### Risks & Mitigations

**Risk 1: Teams define services too narrowly (10+ squads for 20-person company)**
- **Mitigation:** "Sustainable scope" validation question
- **Guideline:** 1 squad per 5-10 people (startup), 1 squad per 8-12 people (scale-up)

**Risk 2: Teams define services too broadly (1 squad for entire company)**
- **Mitigation:** "Can succeed without constant coordination?" question
- **Guideline:** If >15 people needed, split into 2 services

**Risk 3: Conway's Law (org structure mirrors technical architecture)**
- **Mitigation:** This is DESIRED behavior (inverse Conway's Law)
- **Benefit:** Organizational design intentionally shapes system architecture

---

## Alternatives Considered

### Alternative 1: Technical Layer Organization (Traditional)

**Structure:** Frontend Squad, Backend Squad, Database Squad, QA Squad

**Pros:**
- Familiar to most engineering teams
- Technical specialization is clear
- Easy to hire (role-based: "Frontend Developer")

**Cons:**
- ❌ Every feature requires 4-team coordination
- ❌ Handoff delays (2-4 weeks per feature)
- ❌ Unclear ownership ("whose bug is this?")
- ❌ Doesn't scale (coordination overhead grows exponentially)

**Why Rejected:** Antithetical to AI-native autonomy and speed

---

### Alternative 2: Feature-Based Organization

**Structure:** Shopping Cart Squad, Search Squad, Recommendations Squad

**Pros:**
- Clear short-term focus
- Easy to understand for product managers
- Can pivot quickly (dissolve/reform squads)

**Cons:**
- ❌ Features are temporary → constant reorganization
- ❌ Knowledge loss during reorgs (30-40% productivity drop)
- ❌ No clear ownership after feature "launch"
- ❌ Duplicated infrastructure across feature teams

**Why Rejected:** Unsustainable for long-term operations

---

### Alternative 3: Hybrid (Business Services + Technical Platforms)

**Structure:** Order Fulfillment Squad, Customer Onboarding Squad + Platform Engineering Team

**Pros:**
- Combines service autonomy with shared platform
- Platform team provides reusable components
- Business squads focus on domain logic

**Cons:**
- ⚠️ Risk of platform becoming bottleneck (all squads depend on it)
- ⚠️ "Platform team" can become catch-all for everything

**Why Partially Accepted:**
- ✅ Use **Pool Model** instead of dedicated platform team
- ✅ Shared capabilities (DevOps, Data, Design) provided on-demand
- ✅ Pools support all squads without becoming bottleneck
- Documented in DOCS/03-organizational-model.md

---

### Alternative 4: Matrix Organization (Functional + Product)

**Structure:** Engineers report to Engineering Manager + work on Product Squad

**Pros:**
- Maintains functional expertise
- Career paths are clear (IC track, Management track)
- Resource sharing across product initiatives

**Cons:**
- ❌ Dual reporting creates confusion
- ❌ Product managers fight for engineering time
- ❌ Slows decision-making (need 2 approvals)

**Why Rejected:** Adds coordination overhead instead of removing it

---

## Implementation

### Phase 1: Identify Business Services (Week 1)

1. Workshop with leadership + architects
2. Map current capabilities to business services
3. Validate each service using 6-question criteria
4. Document service boundaries in squad charters

**Deliverable:** List of 5-15 business services (depends on company size)

---

### Phase 2: Form Squads (Week 2-4)

1. Use `ADOPTION/CHECKLISTS/squad-formation.md`
2. Fill out `ADOPTION/TEMPLATES/squad-charter-template.md`
3. Define input/output contracts for each service
4. Assign Product Owner + System Architect + Project Manager (Triad)

**Deliverable:** Squad charters for all services

---

### Phase 3: Establish Integration (Week 5-8)

Per ADR-0003, each business service must integrate with:
1. **Data Spine** (contracts, events, observability)
2. **Automation Mesh** (SIPOC workflows, event-driven architecture)
3. **OKRs/KPIs** (service-level objectives, dashboards)
4. **Data Governance** (event ownership, compliance)

**Deliverable:** 35-item integration checklist completed per squad

---

### Phase 4: Validate Autonomy (Week 9-12)

**Success Criteria:**
- Squads deploy independently 3x/week (no cross-squad approvals)
- <10% of work requires cross-squad coordination
- Service boundaries are clear (no "whose job is this?")
- OKRs/KPIs show business impact per squad

**Metrics:**
- Deployment frequency (per squad)
- Lead time for changes (idea → production)
- Cross-squad dependency rate (% of work requiring coordination)
- Business impact (revenue/cost/NPS per squad)

---

## Validation

### Framework Files Updated (11 files)

**Core Documentation (4 files):**
- DOCS/01-principles.md (added to "Intelligent Decentralization")
- DOCS/03-organizational-model.md (expanded squad definition)
- PLAYBOOKS/organizational/squads.md (comprehensive section, ~150 lines)
- DIAGRAMS/squad-business-service-organization.mmd (anti-pattern vs. best practice)

**Adoption Pack (2 files):**
- ADOPTION/CHECKLISTS/squad-formation.md (6 new validation items)
- ADOPTION/TEMPLATES/squad-charter-template.md (service definition section)

**Website (5 files):**
- docs_site/ copies of all updated files

### Real-World Validation

This pattern has been proven at:
- **Spotify** (squads organized by user journey: Discovery, Playback, Social)
- **Amazon** (two-pizza teams organized by business capability: Recommendations, Checkout, Prime)
- **Netflix** (microservices aligned with business domains: Content Delivery, Recommendations, Billing)

Industry patterns supporting this approach:
- **Domain-Driven Design (DDD):** Bounded Contexts = Business Services
- **Team Topologies:** Stream-Aligned Teams = Business Service Squads
- **Microservices:** Service boundaries = Business capabilities
- **Conway's Law (Inverse):** Design organization for desired architecture

---

## References

**Internal Documentation:**
- [Organizational Model](../DOCS/03-organizational-model.md) - Squad, pool, and topology definitions
- [Squad Playbook](../PLAYBOOKS/organizational/squads.md) - Comprehensive squad formation guide
- [Squad Formation Checklist](../ADOPTION/CHECKLISTS/squad-formation.md) - Step-by-step validation
- [Squad Charter Template](../ADOPTION/TEMPLATES/squad-charter-template.md) - Service definition template
- [Business Service Organization Diagram](../DIAGRAMS/squad-business-service-organization.mmd) - Visual reference
- [Integration Requirements (ADR-0003)](adr-0003-data-spine-automation-mesh-integration.md) - Required integrations

**External Resources:**
- Evans, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software* (2003)
- Skelton & Pais. *Team Topologies: Organizing Business and Technology Teams for Fast Flow* (2019)
- Conway, Melvin. "How Do Committees Invent?" (1968) - Conway's Law
- Newman, Sam. *Building Microservices* (2021) - Service boundaries

---

**Status:** ✅ Accepted  
**Date:** 2025-11-05  
**Version:** 1.0  
**ADR Sponsor:** Framework Team  
**Supersedes:** N/A  
**Superseded by:** N/A (current)
