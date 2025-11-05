# Squad Charter Template

Use this template to define your squad's purpose, scope, and operating model.

---

# Squad Charter Template

**Purpose:** Define squad identity, mission, team, and operating model aligned with SOLID.AI principles

**Critical:** Squad MUST be organized around a **business service** (bounded context), not a technical layer or temporary feature.

---

## Business Service Definition

**Service Name:** [Name of the business capability this squad owns]

**Examples:**
- ✅ "Customer Onboarding" (signup → activation)
- ✅ "Order Fulfillment" (purchase → delivery)
- ✅ "Fraud Detection" (real-time risk assessment)
- ❌ "Frontend Team" (technical layer)
- ❌ "Database Squad" (infrastructure)
- ❌ "Feature X" (temporary scope)

**Service Description:** [1-2 sentences describing what business value this service delivers]

**Service Boundaries:**
- **In Scope:** [What this service owns end-to-end]
- **Out of Scope:** [What other squads/services own]
- **Input Contracts:** [Data/events this service consumes]
- **Output Contracts:** [Data/events this service produces]

**Why This is a Business Service:**
- [ ] Delivers independent business value
- [ ] Has clear domain boundaries (bounded context)
- [ ] No overlap with other squads (avoids duplication)
- [ ] Can operate autonomously with minimal dependencies
- [ ] Maps to stakeholder outcomes, not technical tasks

---

## Squad Identity

**Squad Name:** [Choose a meaningful name that reflects your mission]

**Formation Date:** [When this squad was formed]

**Squad Lead:** [Name and contact]

**Team Members:**
- [Name] - [Role]
- [Name] - [Role]
- [Add more as needed]

---

## Purpose & Mission

### Mission Statement
_Why does this squad exist? What outcome are you driving?_

[Write 1-3 sentences capturing your squad's core purpose]

### Vision
_What does success look like in 6-12 months?_

[Describe the future state you're working toward]

### Alignment
_How does this squad's work connect to company strategy and values?_

[Explain how your mission serves the broader organizational purpose]

---

## Data Spine Integration

### Input Contracts
_What data/events does this service consume?_

| Data/Event | Source | Schema | SLA | Purpose |
|------------|--------|--------|-----|---------|
| [Event name] | [Service/System] | [schema_v1.avro] | [<500ms] | [Why we need this] |
| [Data product] | [Data Spine] | [product_v2] | [Hourly refresh] | [How we use it] |

**Example:**
| Data/Event | Source | Schema | SLA | Purpose |
|------------|--------|--------|-----|---------|
| OrderPlaced | Shopping Cart Service | order_v2.avro | <500ms | Trigger fulfillment workflow |
| InventoryLevels | Data Spine | inventory_snapshot_v1 | Real-time | Check stock availability |

### Output Contracts
_What data/events does this service produce?_

| Data/Event | Consumers | Schema | SLA | Description |
|------------|-----------|--------|-----|-------------|
| [Event name] | [Service 1, Service 2] | [schema_v1.avro] | [<1s] | [What this event represents] |

**Example:**
| Data/Event | Consumers | Schema | SLA | Description |
|------------|-----------|--------|-----|-------------|
| OrderFulfilled | Customer Notifications, Analytics, Returns | fulfillment_v1.avro | <1s | Order shipped successfully |
| InventoryUpdated | Inventory Mgmt, Purchasing | inventory_delta_v1 | <2s | Stock level changed |

### Business Events Catalog
_Domain events this service owns and publishes:_

- **[Event Name]** - [When it's published] - [Who consumes it]
- **[Event Name]** - [When it's published] - [Who consumes it]

**Example:**
- **OrderFulfilled** - When package ships - [Customer Notifications, Analytics, Returns, Billing]
- **FulfillmentFailed** - When order cannot be fulfilled - [Customer Support, Inventory, Purchasing]

### Data Quality SLAs
_Guarantees this service makes about its data:_

- **Accuracy:** [e.g., 99.9% of orders have correct address]
- **Completeness:** [e.g., All orders include customer contact info]
- **Timeliness:** [e.g., Events published within 1 second of occurrence]
- **Consistency:** [e.g., Inventory updates match warehouse system within 5 minutes]

### Observability & Telemetry
_How we monitor this service:_

- **Dashboard URL:** [Link to Grafana/Datadog/etc.]
- **Key Metrics:** [Latency p95, Throughput req/s, Error rate %]
- **Alerts:** [What triggers on-call notifications]
- **Data Lineage:** [How we track data flow through the service]

---

## Automation Mesh Integration

### SIPOC Workflow
_End-to-end process this service executes:_

| Element | Details |
|---------|---------|
| **Suppliers** | [Who provides inputs to this service] |
| **Inputs** | [What data/events/requests we receive] |
| **Process** | [Step-by-step workflow - mark AI-automated vs. human-in-loop] |
| **Outputs** | [What data/events we produce] |
| **Customers** | [Who consumes our outputs] |

**Example - Invoice Processing Service:**
- **Suppliers:** Vendors, Procurement System
- **Inputs:** Invoice PDFs, Purchase Orders
- **Process:**
  1. Extract data from PDF (AI Agent - 95% automated)
  2. Validate against PO (Rule Engine - 100% automated)
  3. Flag discrepancies (AI Agent - alerts human for >$1K variance)
  4. Route for approval (Workflow - automated)
  5. Schedule payment (Integration - automated)
- **Outputs:** InvoiceApproved event, Payment scheduled
- **Customers:** Finance Team, Vendor Portal, Analytics

### Event-Driven Architecture
_How this service communicates with others:_

**Events We Subscribe To:**
- [EventName] from [SourceService] → [What we do when we receive it]

**Events We Publish:**
- [EventName] → Consumed by [ConsumerService1, ConsumerService2]

**Example:**
- **Subscribe:** OrderPlaced from Shopping Cart → Start fulfillment workflow
- **Subscribe:** PaymentConfirmed from Payment Service → Release inventory
- **Publish:** OrderFulfilled → Trigger customer email, update analytics, enable returns
- **Publish:** FulfillmentFailed → Alert customer support, restock inventory

### Automation Strategy
_Which parts are AI-automated vs. human-in-loop:_

| Step | Automation Level | AI Agent/Tool | Human Role |
|------|------------------|---------------|------------|
| [Process step] | [100% / 80% / Human-led] | [Agent name] | [Oversight/Exception handling] |

**Example:**
| Step | Automation Level | AI Agent/Tool | Human Role |
|------|------------------|---------------|------------|
| Data extraction | 95% automated | DocumentAI-Agent | Review edge cases |
| Validation | 100% automated | RuleEngine | None (alerts on failure) |
| Approval routing | 100% automated | WorkflowEngine | Final approval (>$10K) |
| Exception handling | Human-led | None | Investigate discrepancies |

### Error Handling
_How we handle failures:_

- **Retry Policy:** [e.g., Exponential backoff, max 3 retries]
- **Dead Letter Queue:** [Where failed events go for manual review]
- **Circuit Breaker:** [Fallback behavior when dependency fails]
- **Escalation:** [When/how we alert humans]

---

## OKRs & KPIs

### Service-Level OKRs
_Quarterly objectives and key results for this service:_

**Objective 1:** [Business outcome we're driving]
- **KR 1.1:** [Measurable result]
- **KR 1.2:** [Measurable result]
- **KR 1.3:** [Measurable result]

**Objective 2:** [Technical/operational improvement]
- **KR 2.1:** [Measurable result]
- **KR 2.2:** [Measurable result]

**Example - Customer Onboarding Service:**
- **Objective:** Accelerate time-to-value for new customers
  - **KR 1:** Reduce signup-to-activation time from 48h to 12h
  - **KR 2:** Increase activation rate from 60% to 80%
  - **KR 3:** Achieve NPS >70 for onboarding experience

### KPI Dashboard
_Real-time metrics we track:_

| Category | Metric | Target | Current | Trend |
|----------|--------|--------|---------|-------|
| **Business Impact** | [e.g., Monthly Active Users] | [100K] | [95K] | [↗️/↘️/→] |
| **Efficiency** | [e.g., Cost per Transaction] | [$5] | [$7] | [↗️/↘️/→] |
| **Quality** | [e.g., Success Rate] | [99%] | [97%] | [↗️/↘️/→] |
| **Speed** | [e.g., Avg Processing Time] | [<5s] | [6s] | [↗️/↘️/→] |
| **AI Augmentation** | [e.g., Automation Rate] | [80%] | [72%] | [↗️/↘️/→] |
| **Reliability** | [e.g., Service Uptime] | [99.9%] | [99.95%] | [↗️/↘️/→] |
| **Data Quality** | [e.g., Contract Compliance] | [100%] | [98%] | [↗️/↘️/→] |

### Business Value Metrics
_How this service contributes to company goals:_

- **Revenue Impact:** [e.g., $500K ARR from improved conversion]
- **Cost Savings:** [e.g., 40% reduction in manual processing]
- **Customer Satisfaction:** [e.g., NPS increased from 50 to 70]
- **Operational Efficiency:** [e.g., 2x throughput with same team size]

---

## Data Governance

### Event Ownership
_This squad is the authoritative source for:_

- [Event/Data Domain] - [What we guarantee about it]

**Stakeholders (Event Consumers):**
- [Service/Team] - [How they use our events]
- [Service/Team] - [How they use our events]

**Example:**
- **FraudAlertRaised Event** - Authoritative fraud risk assessment
  - Order Fulfillment Squad (blocks high-risk orders)
  - Customer Support Squad (flags accounts for review)
  - Analytics Team (fraud trend dashboards)
  - Compliance Team (regulatory reporting)

### Breaking Change Policy
_How we manage schema evolution:_

- **Additive Changes:** [Can deploy immediately - backward compatible]
- **Breaking Changes:** [Require RFC + 90-day migration period]
- **Deprecation:** [Notify stakeholders, provide migration guide, 90-day sunset]

### Compliance Requirements
_Regulatory/legal constraints:_

- **Data Classification:** [PII / Sensitive / Public]
- **Retention Policy:** [e.g., 7 years for financial data, 30 days for logs]
- **Access Controls:** [Who can read/write this service's data]
- **Audit Logging:** [What actions are logged for compliance]
- **Regulatory Standards:** [e.g., GDPR, SOX, HIPAA, PCI-DSS]

**Example - Customer Onboarding Service:**
- **Data Classification:** PII (email, name, phone)
- **Retention:** 7 years (regulatory requirement)
- **Access:** Only Customer Support + Leadership roles
- **Audit Log:** All PII access logged
- **Standards:** GDPR (EU customers), CCPA (CA customers)

---

## Scope & Boundaries

### In Scope
_What is this squad responsible for?_

- [Domain or product area]
- [Key deliverables]
- [Add more]

### Out of Scope
_What is this squad NOT responsible for?_

- [What belongs to other squads or teams]
- [Explicit exclusions]
- [Add more]

### Dependencies
_What other squads, pools, or systems does this squad depend on?_

| Dependency | Type | Contact | Notes |
|------------|------|---------|-------|
| [Team/System name] | [Squad/Pool/Platform] | [Contact] | [What you need from them] |

---

## Key Results & Metrics

### OKRs or Goals
_What are your measurable objectives for this quarter/period?_

**Objective 1:** [Outcome-focused objective]
- **Key Result 1.1:** [Measurable result]
- **Key Result 1.2:** [Measurable result]

**Objective 2:** [Outcome-focused objective]
- **Key Result 2.1:** [Measurable result]

### Success Metrics
_How do you measure squad health and impact?_

**User/Customer Metrics:**
- [e.g., Adoption rate, satisfaction, outcomes]

**Delivery Metrics:**
- [e.g., Velocity, cycle time, deployment frequency]

**Team Health Metrics:**
- [e.g., Engagement, psychological safety, skill growth]

**AI Performance Metrics** (if applicable):
- [e.g., Agent accuracy, latency, cost-efficiency]

---

## Operating Model

### Rituals & Cadence
_How does this squad work together?_

| Ritual | Frequency | Duration | Purpose |
|--------|-----------|----------|---------|
| Stand-up / Check-in | [Daily/3x week] | [15 min] | Synchronize, surface blockers |
| Sprint Planning | [Bi-weekly/Weekly] | [1-2 hours] | Prioritize and commit to work |
| Demo / Review | [End of sprint] | [30-60 min] | Show progress, gather feedback |
| Retrospective | [End of sprint] | [60 min] | Reflect and improve |
| Stakeholder Sync | [Weekly/Bi-weekly] | [30 min] | Update stakeholders, align |

### Communication Channels
- **Primary chat:** [e.g., #squad-name in Slack]
- **Email list:** [squad email if exists]
- **Documentation:** [Wiki/Confluence/GitHub location]
- **Task board:** [Jira/Asana/GitHub Projects link]

### Decision-Making
_How does the squad make decisions?_

**Autonomous Decisions** (squad can decide):
- [e.g., Technical implementation choices within scope]
- [e.g., Work prioritization within sprint]

**Collaborative Decisions** (consult stakeholders):
- [e.g., Scope changes, roadmap shifts]

**Escalation Required** (leadership approval):
- [e.g., Budget changes, cross-squad dependencies]

---

## AI & Automation

### AI Agents Supporting This Squad
_Which AI agents does this squad use or manage?_

| Agent Name | Role | Owner | Notes |
|------------|------|-------|-------|
| [Agent name] | [What it does] | [This squad/Other team] | [How squad uses it] |

### Data Contracts
_What key data does this squad produce or consume?_

| Contract Name | Producer/Consumer | Purpose |
|---------------|-------------------|---------|
| [Contract] | [Producer/Consumer] | [Why squad needs this] |

---

## Working Agreements

### How We Collaborate
- [e.g., "We assume positive intent and focus on systems, not people"]
- [e.g., "We speak up when we disagree or see risks"]
- [e.g., "We share context openly and avoid information hoarding"]
- [Add more]

### How We Handle Conflict
- [e.g., "We address disagreements directly and respectfully"]
- [e.g., "We escalate to squad lead if we can't resolve ourselves"]

### Work-Life Balance
- [e.g., "No expectation to respond after 6pm or on weekends unless critical incident"]
- [e.g., "We respect focus time and minimize unnecessary meetings"]

---

## Continuous Learning

### Skill Development
_What skills is the squad building?_

- [e.g., "Machine learning ops and model monitoring"]
- [e.g., "Domain expertise in education technology"]

### Knowledge Sharing
_How does the squad capture and share learnings?_

- [e.g., "Document decisions as ADRs in GitHub"]
- [e.g., "Demo learnings at All-Hands quarterly"]
- [e.g., "Contribute to company playbooks and RFCs"]

---

## Governance & Ethics

### Ethical Considerations
_What ethical responsibilities does this squad have?_

- [e.g., "Ensure AI recommendations don't discriminate by demographics"]
- [e.g., "Protect student privacy in all data handling"]

### Compliance Requirements
_What regulatory or policy constraints apply?_

- [e.g., "FERPA compliance for student data"]
- [e.g., "GDPR right-to-delete within 30 days"]

### Review & Oversight
_Who reviews this squad's work for ethics and governance?_

- **Reviewer/Body:** [e.g., Ethics Review Board, Data Protection Officer]
- **Frequency:** [e.g., Quarterly, or on major feature launches]

---

## Reflection & Evolution

### Charter Review
_When will this charter be reviewed and updated?_

- **Initial review:** [30 days after squad formation]
- **Regular reviews:** [Quarterly, or as mission changes]

### Success Indicators
_How do we know this squad is healthy and effective?_

✅ **Healthy squad shows:**
- Clear purpose and everyone can articulate the mission
- Consistent delivery of value
- Team engagement and psychological safety
- Learning and continuous improvement
- Alignment with company strategy

### Off-Ramp
_How would this squad sunset if mission is complete or no longer viable?_

- [e.g., "Celebrate success, document learnings, transition team members to new squads"]

---

## Signatures & Approval

**Squad Lead:** ___________________________  Date: __________

**Sponsor/Leadership:** ___________________________  Date: __________

_(Optional: Add signatures of key stakeholders or team members)_

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| [Date] | Charter created | [Name] |
| [Date] | Updated scope after Q2 review | [Name] |

---

**Version:** 1.0 | **Framework:** SOLID.AI

**Related Resources:**
- **Squad Formation Checklist:** [CHECKLISTS/squad-formation.md](../CHECKLISTS/squad-formation.md)
- **Squad Playbook:** [PLAYBOOKS/playbook-squads.md](../../PLAYBOOKS/playbook-squads.md)
- **Organizational Model:** [DOCS/03-organizational-model.md](../../DOCS/03-organizational-model.md)
