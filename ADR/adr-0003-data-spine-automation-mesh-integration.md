# ADR-0003: Required Data Spine and Automation Mesh Integration for Business Services

**Status:** ✅ Accepted  
**Date:** 2025-11-05  
**Deciders:** Framework Team  
**Related:** ADR-0002 (Business Service Organization), DOCS/02-architecture.md, PLAYBOOKS/organizational/squads.md

---

## Context

After establishing business service organization (ADR-0002), we observed that squads were operating in isolation without standardized integration patterns. This created several problems:

**Problem 1: Invisible Services**
- No observability into service health or data quality
- Issues discovered by end users, not proactive monitoring
- **Impact:** 2-4 hour MTTR (Mean Time To Recovery)

**Problem 2: Unreusable Events**
- Services duplicated event implementations
- No clear ownership of business events
- Breaking changes broke downstream consumers
- **Impact:** 30-40% duplicate effort, frequent production incidents

**Problem 3: Unmeasurable Business Value**
- Squads tracked activity (story points) not outcomes (revenue, cost, NPS)
- No connection between squad work and company OKRs
- **Impact:** Difficulty prioritizing investments, justifying headcount

**Problem 4: Ungoverned Data**
- No compliance validation (GDPR, SOX, HIPAA)
- Data classification unclear (PII vs. sensitive vs. public)
- Audit trails missing for regulators
- **Impact:** Regulatory risk, potential fines up to 4% revenue

Without standardized integration requirements, business services remained organizational units instead of becoming true architectural components.

---

## Decision

**Every business service MUST integrate with 4 architectural layers:**

### 1. Data Spine Integration (Required)

**What:** Connect service to organizational nervous system for data contracts, events, and observability

**Requirements (7 checklist items):**
- ✅ Input/output contracts defined and registered in Data Catalog
- ✅ Business events documented in Event Catalog
- ✅ Data quality SLAs defined and monitored
- ✅ Observability dashboards configured (Grafana/Datadog)
- ✅ Data lineage tracking enabled
- ✅ Schema registry configured (Avro/Protobuf)
- ✅ Compliance requirements mapped (PII, retention, access)

**Example - Order Fulfillment Service:**
```yaml
Input Contracts:
  - Event: OrderPlaced
    Source: Shopping Cart Service
    Schema: order_v2.avro
    SLA: <500ms processing time
  
  - Data: InventoryLevels
    Source: Data Spine
    Schema: inventory_snapshot_v1
    Refresh: Real-time

Output Contracts:
  - Event: OrderFulfilled
    Consumers: [Customer Notifications, Analytics, Returns, Billing]
    Schema: fulfillment_v1.avro
    SLA: <1s latency
  
  - Event: InventoryUpdated
    Consumers: [Inventory Management, Purchasing]
    Schema: inventory_delta_v1
    SLA: <2s latency

Observability:
  Dashboard: https://grafana.company.com/order-fulfillment
  Metrics:
    - Latency: p50=150ms, p95=450ms, p99=800ms
    - Throughput: 500 req/s
    - Error rate: 0.1%
  Data Lineage: OrderPlaced → Inventory Check → OrderFulfilled
  Quality SLAs: Accuracy 99.9%, Completeness 100%, Timeliness <1s
```

---

### 2. Automation Mesh Integration (Required)

**What:** Define workflows, automation strategy, event-driven architecture, error handling

**Requirements (7 checklist items):**
- ✅ SIPOC workflow documented (Suppliers, Inputs, Process, Outputs, Customers)
- ✅ Automation opportunities identified (AI vs. human-in-loop)
- ✅ Event subscriptions configured (what events service consumes)
- ✅ Event publications registered (what events service produces)
- ✅ Workflow orchestration defined
- ✅ Error handling designed (retry, DLQ, escalation)
- ✅ Circuit breakers for dependencies

**Example - Invoice Processing Service:**
```
SIPOC Workflow:
  Suppliers: Vendors, Procurement System
  Inputs: Invoice PDFs, Purchase Orders
  
  Process:
    1. Extract data from PDF (AI Agent - 95% automated)
    2. Validate against PO (Rule Engine - 100% automated)
    3. Flag discrepancies (AI Agent - alerts human for >$1K variance)
    4. Route for approval (Workflow - 100% automated)
    5. Schedule payment (Integration - 100% automated)
  
  Outputs: InvoiceApproved event, Payment scheduled
  Customers: Finance Team, Vendor Portal, Analytics

Event-Driven Architecture:
  Subscribe To:
    - InvoiceReceived (from Email Monitoring)
    - PurchaseOrderCreated (from Procurement)
    - VendorUpdated (from Vendor Management)
  
  Publish:
    - InvoiceProcessed (to Analytics, Auditing)
    - PaymentScheduled (to Treasury, Vendor Portal)
    - DiscrepancyDetected (to AP Team, Vendor)

Error Handling:
  Retry Policy: Exponential backoff (1s, 2s, 4s, 8s), max 3 attempts
  Dead Letter Queue: Failed events for manual review
  Circuit Breaker: If vendor API fails 5x, queue for retry
  Compensation: If payment fails, publish InvoiceCancelled event
```

---

### 3. OKRs & KPIs Integration (Required)

**What:** Measure business impact and service health continuously

**Requirements (4 checklist items):**
- ✅ Service-level OKRs defined (aligned with company strategy)
- ✅ KPI dashboard configured with real-time metrics
- ✅ AI augmentation metrics tracked
- ✅ Quarterly review cadence established

**Example - Customer Onboarding Service:**
```
Service-Level OKRs (Q4 2025):

Objective 1: Accelerate time-to-value for new customers
  KR1: Reduce signup-to-activation time from 48h to 12h
  KR2: Increase activation rate from 60% to 80%
  KR3: Achieve NPS >70 for onboarding experience

Objective 2: Scale efficiently with AI augmentation
  KR1: Handle 2x user volume with same team size
  KR2: Automate 80% of verification steps (up from 40%)
  KR3: Reduce manual review time by 60%

KPI Dashboard:
  Category          | Metric                  | Target | Current | Trend
  ------------------|-------------------------|--------|---------|-------
  Business Impact   | Monthly Active Users    | 100K   | 95K     | ↗️
  Efficiency        | Cost per Transaction    | $5     | $7      | ↘️
  Quality           | Success Rate            | 99%    | 97%     | ↗️
  Speed             | Avg Processing Time     | <5s    | 6s      | ↘️
  AI Augmentation   | Automation Rate         | 80%    | 72%     | ↗️
  Reliability       | Service Uptime          | 99.9%  | 99.95%  | →
  Data Quality      | Contract Compliance     | 100%   | 98%     | ↗️

Business Value Metrics:
  - Revenue Impact: $2M increase from faster onboarding
  - Cost Savings: 40% reduction in manual processing ($500K/year)
  - Customer Satisfaction: NPS increased from 50 to 70 (+40%)
  - Operational Efficiency: 2x throughput with same team size
```

---

### 4. Data Governance Integration (Required)

**What:** Ensure safe event reuse, compliance, and clear ownership

**Requirements (6 checklist items):**
- ✅ Event ownership documented
- ✅ Stakeholder/consumer list maintained
- ✅ Breaking change policy (RFC + 90-day migration)
- ✅ Data classification applied (PII, sensitive, public)
- ✅ Retention policies defined (GDPR, SOX)
- ✅ Access controls enabled (RBAC)
- ✅ Audit logging configured

**Example - Fraud Detection Service:**
```
Event Ownership:

Event: FraudAlertRaised
  Owner: Fraud Detection Squad (authoritative source)
  Definition: Real-time risk assessment of transactions
  
  Stakeholders (Consumers):
    - Order Fulfillment Squad (blocks high-risk orders)
    - Customer Support Squad (flags accounts for review)
    - Analytics Team (fraud trend dashboards)
    - Compliance Team (regulatory reporting)
  
  Schema: fraud_alert_v1.avro
  SLA: Published within 500ms of assessment

Breaking Change Policy:
  Additive Changes: Deploy immediately (backward compatible)
    Example: Add optional field "customer_segment"
  
  Breaking Changes: RFC + 90-day migration period
    Example: Rename field "user_id" to "customer_id"
    Process: Publish RFC → Notify stakeholders → Dual schema → Sunset old version
  
  Deprecation: 90-day notice with migration guide
    Example: Retire "OrderShipped" event, consolidate into "OrderFulfilled"

Data Governance:
  Classification: Sensitive (customer risk data)
  Retention: 7 years (financial compliance - SOX)
  Access Controls: RBAC (Security + Compliance + Leadership only)
  Audit Logging: Every access logged (user, timestamp, purpose)
  Compliance: GDPR (EU), CCPA (CA), SOX (financial), PCI-DSS (payments)
```

---

## Integration Checklist

Before a business service can operate in production, complete all 22 items:

### ✅ Data Spine Integration (7 items)
1. Input/output contracts defined and registered
2. Business events documented in Event Catalog
3. Data quality SLAs defined
4. Observability dashboards configured
5. Data lineage tracking enabled
6. Schema registry configured
7. Compliance requirements mapped

### ✅ Automation Mesh Integration (7 items)
8. SIPOC workflow documented
9. Automation opportunities identified
10. Event subscriptions configured
11. Event publications registered
12. Workflow orchestration defined
13. Error handling designed
14. Circuit breakers configured

### ✅ OKRs & KPIs (4 items)
15. Service-level OKRs defined
16. KPI dashboard configured
17. AI augmentation metrics tracked
18. Quarterly review cadence

### ✅ Data Governance (4 items)
19. Event ownership documented
20. Breaking change policy communicated
21. Data classification applied
22. Compliance validated

---

## Consequences

### Positive Outcomes

✅ **Observability (Problem 1 Solved)**
- Real-time dashboards show service health
- Proactive alerts before users report issues
- MTTR reduced from 2-4 hours to <15 minutes
- Data lineage enables root cause analysis

✅ **Reusability (Problem 2 Solved)**
- Events have single authoritative source
- Safe consumption by multiple downstream services
- Breaking changes managed with 90-day migration
- Duplicate implementations eliminated (30-40% efficiency gain)

✅ **Measurability (Problem 3 Solved)**
- Service-level OKRs tied to company strategy
- Real-time KPI dashboards show business impact
- Revenue/cost/NPS tracked per squad
- Investment decisions data-driven (not gut-feel)

✅ **Compliance (Problem 4 Solved)**
- Automated governance (GDPR, SOX, HIPAA)
- Data classification enforced by Data Spine
- Audit trails for regulators
- Legal risk minimized (avoid fines up to 4% revenue)

✅ **AI-Native Operations**
- SIPOC workflow shows where AI augments humans
- Automation levels quantified (95% extraction, 100% validation)
- AI augmentation factor tracked as KPI
- Continuous improvement of automation strategy

### Trade-offs

⚠️ **Upfront Investment Required**
- 35-item integration checklist takes 2-4 weeks per squad
- Teams need training on Data Spine, Event Catalog, Observability
- Initial setup cost: $25K-$50K per squad (tooling, training, implementation)

**Mitigation:** Start with 1-2 pilot services, iterate, then scale

⚠️ **Tooling Complexity**
- Requires: Schema registry, Event Catalog, Observability platform (Grafana/Datadog), RBAC system
- Ongoing maintenance: Schema updates, dashboard monitoring, compliance audits

**Mitigation:** Use existing tools where possible (Confluent Schema Registry, AWS Glue, Datadog)

⚠️ **Governance Overhead**
- Breaking changes require RFC process + 90-day migration
- Event ownership requires stakeholder management
- Compliance reviews add 1-2 weeks to feature delivery

**Mitigation:** Automate compliance checks (schema validation, PII detection, retention policies)

### Risks & Mitigations

**Risk 1: Teams skip integration to move faster**
- **Mitigation:** Make integration checklist part of squad formation approval (governance gate)
- **Enforcement:** Cannot deploy to production without completing checklist

**Risk 2: Integration becomes bureaucratic**
- **Mitigation:** Provide templates, examples, automation
- **Goal:** 80% checklist completion in Week 1 (not 100% perfection)

**Risk 3: Schema registry becomes bottleneck**
- **Mitigation:** Self-service schema registration (automated approval for non-breaking changes)
- **Escalation:** Only breaking changes require manual review

---

## Alternatives Considered

### Alternative 1: Optional Integration (Lightweight Approach)

**Structure:** Integration recommended but not required

**Pros:**
- Faster initial squad formation (no 2-4 week setup)
- Less tooling complexity
- Teams choose what's relevant

**Cons:**
- ❌ Leads to fragmentation (every squad does it differently)
- ❌ Observability gaps (can't see what you don't measure)
- ❌ Reusability suffers (duplicate implementations return)
- ❌ Compliance risk (manual audits, potential fines)

**Why Rejected:** Framework would fragment back to pre-integration chaos

---

### Alternative 2: Phased Integration (Gradual Rollout)

**Structure:**
- Phase 1: Observability only (dashboards)
- Phase 2: Add event catalog
- Phase 3: Add governance
- Phase 4: Add OKRs/KPIs

**Pros:**
- Easier to learn incrementally
- Quick wins with Phase 1 (observability)
- Can validate each phase before next

**Cons:**
- ⚠️ Takes 6-12 months to reach full integration
- ⚠️ Governance gaps in early phases (compliance risk)
- ⚠️ Teams resist adding "more process" later

**Why Partially Accepted:**
- ✅ Use for pilot services (validate approach)
- ✅ Start with observability (easiest, high value)
- ❌ Require all 4 integrations before production deployment

---

### Alternative 3: Centralized Integration Team

**Structure:** Dedicated team handles all Data Spine/Automation Mesh setup for squads

**Pros:**
- Squads don't need to learn tooling
- Consistency guaranteed (experts do the work)
- Faster initial setup

**Cons:**
- ❌ Creates bottleneck (all squads wait for central team)
- ❌ Knowledge doesn't transfer to squads (dependency remains)
- ❌ Doesn't scale (central team can't support 20+ squads)

**Why Rejected:** Defeats purpose of squad autonomy

**Alternative:** Use Pools (on-demand support) instead of dedicated team

---

### Alternative 4: AI-Powered Auto-Integration

**Structure:** AI agent analyzes service and auto-generates contracts, events, dashboards

**Pros:**
- Zero manual effort (AI does it all)
- Consistency guaranteed (AI follows templates)
- Instant setup (minutes, not weeks)

**Cons:**
- ⚠️ Technology not mature enough (2025)
- ⚠️ Requires human validation (AI can't understand business context)
- ⚠️ Custom integrations hard to automate

**Why Deferred to Future:**
- Promising approach for 2026-2027
- Currently use AI to assist (generate draft contracts) but require human review
- Documented in PLAYBOOKS/implementation/process-mapping-sipoc-integration.md

---

## Implementation

### Phase 1: Pilot Services (Month 1-2)

**Select 1-2 Services:**
- Clear business value (Order Fulfillment, Invoice Processing)
- Moderate complexity (not too simple/complex)
- Engaged squad (willing to iterate)

**Complete Integration:**
- Week 1: Define data contracts (input/output)
- Week 2: Create business events catalog
- Week 3: Set up observability dashboards
- Week 4: Document SIPOC + automation strategy
- Week 5-6: Define OKRs/KPIs
- Week 7-8: Establish data governance

**Deliverable:** 2 fully integrated services with 22/22 checklist items complete

---

### Phase 2: Validate Benefits (Month 3)

**Measure:**
- Deployment frequency (before/after)
- MTTR (before/after)
- Cross-squad coordination rate (before/after)
- Business impact (revenue, cost, NPS)

**Gather Feedback:**
- Squad retrospectives (what worked, what didn't)
- Stakeholder interviews (downstream consumers of events)
- Compliance team review (audit readiness)

**Refine:**
- Update templates based on learnings
- Simplify checklist where possible
- Add automation for repetitive tasks

**Deliverable:** Lessons learned document + updated templates

---

### Phase 3: Scale to Remaining Services (Month 4-12)

**Onboard 2-3 Services per Sprint:**
- Use refined templates from pilot
- Assign "integration buddy" (pilot squad member helps new squad)
- Target: 80% checklist completion in Week 1

**Build Reusable Assets:**
- Schema library (common event formats)
- Dashboard templates (clone and customize)
- SIPOC examples by domain (E-Commerce, SaaS, Finance)

**Deliverable:** 15-20 fully integrated services by Month 12

---

## Validation

### Framework Files Updated (8 files)

**Core Documentation (2 files):**
- PLAYBOOKS/organizational/squads.md (~350 lines added - integration sections)
- DOCS/03-organizational-model.md (integration summary)

**Adoption Pack (2 files):**
- ADOPTION/CHECKLISTS/squad-formation.md (31 new checklist items)
- ADOPTION/TEMPLATES/squad-charter-template.md (260 lines - 5 integration sections)

**Visual Diagrams (1 NEW file):**
- DIAGRAMS/business-service-full-integration.mmd (comprehensive architecture diagram)

**Documentation (2 NEW files):**
- BUSINESS-SERVICE-ARCHITECTURE-INTEGRATION-UPDATE.md (600-line framework guide)
- INTEGRATION-COMPLETE-SUMMARY.md (deployment checklist)

**Website (5 files):**
- docs_site/ copies of all updated files

### Real-World Validation

This integration model synthesizes proven patterns:

**Domain-Driven Design (DDD):**
- Bounded Contexts = Business Services
- Domain Events = Business Events Catalog
- Ubiquitous Language = Data Contracts (schema registry)

**Event-Driven Architecture:**
- Event Sourcing = Business events as source of truth
- CQRS = Commands (input contracts) vs. Queries (output contracts)
- Saga Pattern = Error handling and compensation

**Microservices Best Practices:**
- Service Contracts = Data Spine contracts
- API Gateway = Data Spine as event bus
- Circuit Breaker = Automation Mesh error handling
- Distributed Tracing = Data lineage tracking

**SRE (Site Reliability Engineering):**
- SLOs/SLIs = Data quality SLAs, service KPIs
- Error Budgets = Tracked in KPI dashboard
- Observability = Metrics, logs, traces (dashboards)

**Compliance Frameworks:**
- GDPR = Data classification, retention, right to erasure
- SOX = Audit trails, 7-year retention
- PCI-DSS = Encryption, access controls
- HIPAA = PHI classification, audit logging

Companies using similar approaches:
- **Netflix:** Microservices with event-driven architecture
- **Amazon:** Two-pizza teams with clear service contracts
- **Spotify:** Squads with observable metrics and OKRs

---

## Success Metrics

Track quarterly to validate integration benefits:

| Metric | Baseline | 6-Month Target | 12-Month Target |
|--------|----------|----------------|-----------------|
| **Service Autonomy** | <50% independent deploys | >70% | >90% |
| **Data Contract Coverage** | 0% of services | 50% | 100% |
| **Event Reusability** | 1 consumer per event | 2-3 consumers | 3-5 consumers |
| **Observability** | Manual checks | Dashboards for 50% | Dashboards for 100% |
| **Compliance Automation** | Manual audits | 50% automated | 80% automated |
| **AI Augmentation** | Ad-hoc automation | 50% workflows mapped | 80% workflows |
| **Business Value Visibility** | Unknown | 50% of services | 100% of services |

**Leading Indicators (Month 1-3):**
- Number of data contracts defined
- Number of events in catalog
- Number of dashboards configured

**Lagging Indicators (Month 6-12):**
- Deployment frequency increase
- Lead time reduction
- Business impact (revenue, cost, NPS)

---

## References

**Internal Documentation:**
- [Architecture](../DOCS/02-architecture.md) - 6-layer framework (Data Spine, Automation Mesh)
- [Squad Playbook](../PLAYBOOKS/organizational/squads.md) - Integration requirements detail
- [Squad Formation Checklist](../ADOPTION/CHECKLISTS/squad-formation.md) - 31 integration items
- [Squad Charter Template](../ADOPTION/TEMPLATES/squad-charter-template.md) - Integration templates
- [Integration Diagram](../DIAGRAMS/business-service-full-integration.mmd) - Visual reference
- [Business Service Organization (ADR-0002)](adr-0002-business-service-organization.md) - Organizational principle

**External Resources:**
- Richardson, Chris. *Microservices Patterns* (2018) - Service contracts, event-driven
- Stopford, Ben. *Designing Event-Driven Systems* (2018) - Event sourcing, CQRS
- Beyer et al. *Site Reliability Engineering* (2016) - SLOs, observability
- Kleppmann, Martin. *Designing Data-Intensive Applications* (2017) - Data lineage, quality

---

**Status:** ✅ Accepted  
**Date:** 2025-11-05  
**Version:** 1.0  
**ADR Sponsor:** Framework Team  
**Supersedes:** N/A  
**Superseded by:** N/A (current)
