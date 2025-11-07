# Squad Playbook

This playbook guides cross-functional squads delivering outcomes within the solid.ai framework.

## Mission

Deliver stakeholder value by combining human expertise with AI agents, anchored by the solid.ai principles.

## Foundational Principle: Business Service Ownership

**Critical:** Squads MUST be organized around **business services** (bounded contexts in Domain-Driven Design), not technical layers, features, or arbitrary divisions.

### What is a Business Service?

A **business service** is a self-contained capability that delivers specific business value:
- ✅ **"Customer Onboarding"** - Complete flow from signup to activation
- ✅ **"Order Fulfillment"** - End-to-end from purchase to delivery
- ✅ **"Invoice Processing"** - Automated AP/AR workflows
- ✅ **"Fraud Detection"** - Real-time risk assessment and prevention
- ❌ **"Frontend Team"** - Technical layer, not a business service
- ❌ **"Database Team"** - Infrastructure, not a business outcome
- ❌ **"Feature X Squad"** - Temporary feature, not sustainable service

### Why Business Services?

| Principle | Benefit | Anti-Pattern Avoided |
|-----------|---------|---------------------|
| **One Squad, One Service** | Clear ownership, accountability | Duplicate efforts, territorial conflicts |
| **Clear Boundaries** | Minimal dependencies between squads | Coordination overhead, bottlenecks |
| **Autonomous Decisions** | Squad owns end-to-end delivery | Approval chains, handoffs |
| **Scalability** | New service = new squad (not splitting) | Reorganization churn, knowledge loss |
| **Value Alignment** | Service ties directly to business outcomes | Activity theater, output vs. outcome |

### Service Boundary Questions

Before forming a squad, answer:
1. **What business capability does this serve?** (e.g., "Enable customers to manage their subscriptions")
2. **Who are the end users/stakeholders?** (e.g., "Subscription customers and billing operations")
3. **What value does it deliver independently?** (e.g., "Self-service reduces support tickets by 40%")
4. **What are the clear input/output contracts?** (e.g., "Consumes customer data, produces subscription events")
5. **Can this squad succeed without constant coordination?** (If no, boundary is wrong)

## Critical: Data Spine & Automation Mesh Integration

**Every business service MUST be properly integrated into the SOLID.AI architecture layers:**

### 1. Data Spine Integration (Required)

Each business service must define and maintain:

#### Data Contracts
- **Input Contracts:** What data/events the service consumes (schema, SLA, source)
- **Output Contracts:** What data/events the service produces (schema, SLA, consumers)
- **Data Quality SLAs:** Accuracy, completeness, timeliness guarantees
- **Schema Registry:** Versioned contracts registered in Data Catalog

**Example - Order Fulfillment Service:**
```yaml
Input Contracts:
  - Event: OrderPlaced (from Shopping Cart Service)
    Schema: order_v2.avro
    SLA: <500ms processing time
  - Data: InventoryLevels (from Data Spine)
    Schema: inventory_snapshot_v1
    Refresh: Real-time

Output Contracts:
  - Event: OrderFulfilled
    Schema: fulfillment_v1.avro
    Consumers: [Customer Notification, Analytics, Returns]
  - Event: InventoryUpdated
    Schema: inventory_delta_v1
    Consumers: [Inventory Management, Purchasing]
```

#### Business Events
- **Event Catalog:** All business events the service publishes
- **Event Ownership:** Service is authoritative source for its domain events
- **Event Reusability:** Other services can subscribe as stakeholders
- **Event Versioning:** Backward-compatible schema evolution

**Example Events:**
- `OrderFulfilled`, `OrderShipped`, `OrderDelivered` (Order Fulfillment Service)
- `CustomerActivated`, `AccountVerified` (Customer Onboarding Service)
- `FraudAlertRaised`, `RiskScoreCalculated` (Fraud Detection Service)

#### Observability & Telemetry
- **Service Metrics:** Dashboards for service health (latency, throughput, errors)
- **Data Lineage:** Track data flow through the service (input → transformation → output)
- **Quality Monitoring:** Automated alerts for data quality violations
- **Audit Trail:** Complete history of data changes for compliance

### 2. Automation Mesh Integration (Required)

Each business service must define:

#### Automated Workflows
- **SIPOC Mapping:** Suppliers → Inputs → Process → Outputs → Customers
- **Automation Opportunities:** Which steps are AI-automated vs. human-in-loop
- **Workflow Orchestration:** How the service triggers/responds to events
- **Error Handling:** Retry policies, dead letter queues, escalation paths

**Example - Invoice Processing Service SIPOC:**
```
Suppliers: Vendors, Procurement System
Inputs: Invoice PDFs, Purchase Orders
Process:
  1. Extract data (AI Agent - 95% automated)
  2. Validate against PO (Rule Engine - 100% automated)
  3. Flag discrepancies (AI Agent - alerts human for >$1K variance)
  4. Route for approval (Workflow - automated)
  5. Schedule payment (Integration - automated)
Outputs: InvoiceApproved event, Payment scheduled
Customers: Finance Team, Vendor Portal, Analytics
```

#### Cross-Service Orchestration
- **Event-Driven Architecture:** Services communicate via Data Spine events (not direct APIs)
- **Saga Patterns:** Multi-service workflows with compensation logic
- **Circuit Breakers:** Graceful degradation when dependencies fail
- **Async-First:** Prefer asynchronous event processing over synchronous calls

### 3. OKRs & KPIs (Required)

Each business service must have measurable outcomes tied to business value:

#### Service-Level OKRs
Define quarterly objectives and key results for the service:

**Example - Customer Onboarding Service:**
```
Objective: Accelerate time-to-value for new customers
  KR1: Reduce signup-to-activation time from 48h to 12h
  KR2: Increase activation rate from 60% to 80%
  KR3: Achieve NPS >70 for onboarding experience

Objective: Scale efficiently with AI augmentation
  KR1: Handle 2x user volume with same team size
  KR2: Automate 80% of verification steps (up from 40%)
  KR3: Reduce manual review time by 60%
```

#### Service KPIs Dashboard
Each service maintains real-time metrics:

| Category | Metric | Target | Current | Trend |
|----------|--------|--------|---------|-------|
| **Business Impact** | Monthly Active Users | 100K | 95K | ↗️ |
| **Efficiency** | Cost per Activation | $5 | $7 | ↘️ |
| **Quality** | Activation Success Rate | 80% | 75% | ↗️ |
| **Speed** | Avg Time-to-Activate | 12h | 16h | ↘️ |
| **AI Augmentation** | Automation Rate | 80% | 72% | ↗️ |
| **Reliability** | Service Uptime | 99.9% | 99.95% | → |
| **Data Quality** | Contract Compliance | 100% | 98% | ↗️ |

### 4. Data Governance (Required)

Each business service must comply with:

#### Event Ownership & Reusability
- **Authoritative Source:** Service owns the definition and quality of its domain events
- **Stakeholder Management:** Document which other services consume your events
- **Breaking Changes:** RFC process for schema changes that affect consumers
- **Deprecation Policy:** 90-day notice for event retirement

**Example - Fraud Detection Service:**
```
Event: FraudAlertRaised
  Owner: Fraud Detection Squad
  Stakeholders (Consumers):
    - Order Fulfillment (blocks high-risk orders)
    - Customer Support (flags accounts for review)
    - Analytics (fraud trend dashboards)
    - Compliance (regulatory reporting)
  
  Change Policy:
    - Additive changes: Can deploy immediately (backward compatible)
    - Breaking changes: Require RFC + 90-day migration period
    - Deprecation: Notify stakeholders, provide migration guide
```

#### Compliance Integration
- **Data Classification:** PII, sensitive, public (enforced by Data Spine)
- **Retention Policies:** How long service data is kept (GDPR, SOX, etc.)
- **Access Controls:** Who can read/write service data (role-based)
- **Audit Logging:** All data access logged for compliance

### 5. Integration Checklist

Before a business service squad can operate, validate:

**Data Spine Integration:**
- [ ] Input contracts defined and registered in Data Catalog
- [ ] Output contracts defined with schema versioning
- [ ] Business events documented in Event Catalog
- [ ] Data quality SLAs defined and monitored
- [ ] Observability dashboards configured (Grafana/Datadog/etc.)
- [ ] Data lineage tracking enabled
- [ ] Compliance requirements mapped (PII, retention, access)

**Automation Mesh Integration:**
- [ ] SIPOC workflow documented
- [ ] Automation opportunities identified (AI vs. human-in-loop)
- [ ] Event subscriptions configured (what events service consumes)
- [ ] Event publications registered (what events service produces)
- [ ] Error handling and retry policies defined
- [ ] Circuit breakers configured for dependencies
- [ ] Dead letter queues for failed events

**OKRs & KPIs:**
- [ ] Service-level OKRs defined (aligned with company strategy)
- [ ] KPI dashboard configured with real-time metrics
- [ ] Business impact metrics tracked (revenue, cost, satisfaction)
- [ ] AI augmentation metrics tracked (automation rate, efficiency)
- [ ] Quarterly review cadence established

**Data Governance:**
- [ ] Event ownership documented
- [ ] Stakeholder/consumer list maintained
- [ ] Breaking change policy communicated
- [ ] Data classification applied (PII, sensitive, public)
- [ ] Compliance requirements validated (legal/security review)
- [ ] Audit logging enabled

### Benefits of Integrated Services

When business services are properly integrated with Data Spine and Automation Mesh:

| Benefit | Description | Example |
|---------|-------------|---------|
| **Observability** | Real-time visibility into service health | Order Fulfillment dashboard shows 99.8% on-time delivery |
| **Reusability** | Other services consume your events safely | Fraud Detection events used by 4 downstream services |
| **Autonomy** | Squad owns end-to-end without dependencies | Customer Onboarding deploys 3x/week independently |
| **Measurability** | Business impact tracked continuously | Invoice Processing reduced AP costs by 40% (measurable) |
| **Scalability** | Add services without breaking existing ones | New "Returns Processing" service launched in 2 weeks |
| **Compliance** | Data governance enforced automatically | PII access logged, retention policies enforced |
| **AI-Native** | Automation opportunities explicit | 80% of Invoice Processing automated (up from 20%) |

### Squad Categories & Common Business Services

Squads are organized into four strategic categories based on their primary function and stakeholder focus:

#### 1. Tech Core (Platform & Enablement)
Squads that build and maintain the technical foundation enabling other squads:

**Platform Services:**
- Infrastructure & DevOps (CI/CD, Container Orchestration, Cloud Operations)
- API Gateway & Service Mesh
- Identity & Access Management
- Monitoring & Observability Platform

**Data Platform:**
- Data Engineering & Pipeline Automation
- Data Warehouse & Lake Management
- Master Data Management
- Data Quality & Governance

**AI/ML Platform:**
- Model Training & MLOps
- AI Agent Infrastructure
- Feature Store & Experimentation Platform
- ML Model Registry & Serving

**Security & Compliance:**
- Security Operations Center (SOC)
- Vulnerability Management
- Compliance Automation (SOX, GDPR, HIPAA)
- Incident Response

**Developer Experience:**
- Internal Developer Portal
- SDK & Library Management
- Documentation Platform
- Development Environment Automation

#### 2. Business Core (Customer & Revenue)
Squads that directly deliver customer value or generate revenue:

**E-Commerce:**
- Product Catalog Management
- Shopping Cart & Checkout
- Order Fulfillment
- Returns & Refunds
- Customer Support Automation

**SaaS:**
- User Onboarding & Activation
- Subscription Management
- Usage Analytics & Billing
- Integration Marketplace
- Customer Success Operations

**Financial Services:**
- Payment Processing
- Fraud Detection & Prevention
- Credit Risk Assessment
- Investment Portfolio Management
- Customer Account Management

**Healthcare:**
- Patient Registration & Scheduling
- Clinical Documentation & EHR
- Telemedicine Platform
- Care Coordination
- Patient Engagement

**Marketing & Growth:**
- Customer Acquisition (SEO, SEM, Campaigns)
- Conversion Optimization
- Personalization & Recommendations
- Retention & Loyalty Programs

#### 3. Operations Core (Enterprise Functions)
Squads that enable internal operations and administrative functions:

**Finance Operations:**
- Accounts Payable/Receivable Automation
- Reconciliation & Settlement
- Financial Planning & Analysis (FP&A)
- Regulatory Reporting
- Procurement & Vendor Management

**HR Operations:**
- Recruiting & Applicant Tracking
- Employee Onboarding & Offboarding
- Payroll & Benefits Administration
- Performance Management
- Learning & Development

**Legal & Compliance:**
- Contract Lifecycle Management
- Regulatory Compliance Automation
- IP & Patent Management
- Litigation Support
- Policy & Risk Management

**Supply Chain & Logistics:**
- Inventory Management
- Warehouse Automation
- Shipping & Distribution
- Demand Planning
- Supplier Relationship Management

**Facilities & Administration:**
- Workplace Management
- Asset Tracking & Maintenance
- Travel & Expense Management
- Document Management

#### 4. Innovation & Intelligence (Experimental & Strategic)
Squads exploring new capabilities, conducting research, or driving strategic initiatives:

**Research & Development:**
- Emerging Technology Exploration (Blockchain, Quantum, etc.)
- Proof-of-Concept Development
- Innovation Lab Projects
- Technology Scouting

**Advanced Analytics & BI:**
- Predictive Analytics
- Business Intelligence Dashboards
- Data Science Research
- Customer Insights & Segmentation

**Strategic Initiatives:**
- Digital Transformation Programs
- New Market Exploration
- Partnership & Ecosystem Development
- M&A Integration Projects

### Category Characteristics

| Category | Primary Focus | Success Metrics | Governance Intensity |
|----------|--------------|-----------------|---------------------|
| **Tech Core** | Platform reliability, developer productivity | Uptime, API latency, developer satisfaction | High (security, compliance) |
| **Business Core** | Customer value, revenue growth | Revenue, NPS, activation rate, retention | Medium (product quality, data privacy) |
| **Operations Core** | Efficiency, cost reduction, compliance | Cost per transaction, automation rate, audit score | High (regulatory, audit trails) |
| **Innovation & Intelligence** | Learning, experimentation, future readiness | Experiments run, insights generated, tech adoption | Low (fast iteration, controlled risk) |

### Cross-Category Collaboration

**Example: Fraud Detection Service**
- **Business Core Squad:** Owns "Fraud Detection" business service (customer-facing)
- **Tech Core Dependency:** Consumes ML Platform (model serving) and Data Platform (real-time streams)
- **Operations Core Integration:** Feeds compliance reporting (suspicious activity reports)
- **Innovation Input:** R&D squad tested new anomaly detection algorithm, graduated to production

**Collaboration Patterns:**
- **Tech Core → Business Core:** Platform services enable customer-facing features
- **Business Core → Operations Core:** Customer data flows into finance/HR processes
- **Innovation → All Categories:** Validated experiments graduate into production squads
- **Operations Core → Tech Core:** Compliance requirements drive platform capabilities

## Squad Models

Squads can organize in different patterns based on outcome complexity and organizational maturity:

### Product Triad (Recommended for Lean Operations)

A **three-person core** optimized for agility and clear accountability:

| Role | Responsibilities | Can be AI Agent? |
|------|-----------------|------------------|
| **Product Owner** | Purpose alignment, stakeholder management, value prioritization | Phase 2+ |
| **System Architect** | Technical design, data contracts, AI agent orchestration | Phase 2+ |
| **Project Manager** | Execution coordination, dependencies, observability tracking | Yes (with human oversight) |

**When to use:** Fast-moving initiatives, clear scope, access to specialized pools for deeper skills.

### Extended Squad

Larger squads with embedded specialists:

- **Squad Lead:** Aligns work with purpose, manages stakeholder expectations.
- **Human Specialists:** Designers, engineers, analysts, domain experts.
- **AI Agents:** Embedded cognitive teammates providing insights or automation.
- **Ops Steward:** Ensures observability, compliance, and incident readiness.

**When to use:** Complex initiatives requiring sustained deep expertise, longer-term engagements.

## Cadence

| Frequency | Ritual | Focus |
| --- | --- | --- |
| Daily | Sync or async stand-up | Progress, blockers, agent status |
| Weekly | Outcome review | Inspect metrics, adjust backlog |
| Biweekly | Learning session | Share insights, update knowledge base |
| Monthly | Governance checkpoint | Validate adherence to RFC/ADR decisions |

## Workflow

1. Intake opportunity, validate purpose alignment, and capture in backlog.
2. Draft RFC if change extends beyond squad scope.
3. Collaborate with pools for specialized skills or data products.
4. Implement with AI agents in co-pilot or auto-resolve mode.
5. Observe outcomes, log insights, and update documentation.

## Squad-Pool Collaboration

Squads draw on **capability pools** for specialized expertise:

- **Embedded engagement:** Pool member joins squad for full sprint/cycle
- **On-demand engagement:** Pool provides time-boxed consultation or pairing
- **Self-service:** Squad consumes pool-managed assets (data products, templates, tools)

See **playbook-pools.md** for detailed pool engagement models.

## KPIs

- Outcome delivery rate vs. planned objectives.
- Quality of agent-assisted outputs (accuracy, explainability).
- Incident rate and resolution time.
- Learning contributions (RFCs, ADRs, playbook updates).
