# Process Mapping & Integration: SIPOC and Automation Contracts

**Mapping processes, defining integration contracts, and connecting to the automation mesh and data spine**

---

## Overview

In AI-native organizations, **processes are automated workflows** that connect humans, AI agents, and systems. This playbook provides:

1. **SIPOC Mapping Framework** - Map any process (Suppliers, Inputs, Process, Outputs, Customers)
2. **Integration Contracts** - Define clear interfaces between components
3. **Data Spine Integration** - Connect processes to unified data layer
4. **Automation Mesh Patterns** - Common workflow architectures
5. **Implementation Templates** - Ready-to-use SIPOC and contract templates

**Key Principle:** Well-defined processes with clear contracts enable reliable automation at scale.

---

## Part 1: SIPOC Framework for AI-Native Processes

### What is SIPOC?

**SIPOC** = **S**uppliers → **I**nputs → **P**rocess → **O**utputs → **C**ustomers

**Traditional use:** Business process improvement (Six Sigma, Lean)

**AI-Native adaptation:** Map human-AI hybrid workflows, identify automation opportunities

---

### The SIPOC Template

```
┌─────────────────────────────────────────────────────────────────┐
│ PROCESS: [Name of the process]                                  │
├─────────────────────────────────────────────────────────────────┤
│ SUPPLIERS          │ Who/what provides inputs?                  │
│ (Who provides)     │ • Upstream systems, teams, AI agents       │
├─────────────────────────────────────────────────────────────────┤
│ INPUTS             │ What inputs are needed?                    │
│ (What they provide)│ • Data, triggers, requests, events         │
├─────────────────────────────────────────────────────────────────┤
│ PROCESS            │ What are the process steps?                │
│ (What we do)       │ • High-level steps (5-7 max)              │
│                    │ • Indicate: Human, AI, or System          │
├─────────────────────────────────────────────────────────────────┤
│ OUTPUTS            │ What does the process produce?             │
│ (What we deliver)  │ • Results, decisions, data, notifications  │
├─────────────────────────────────────────────────────────────────┤
│ CUSTOMERS          │ Who receives the outputs?                  │
│ (Who receives)     │ • Downstream teams, systems, customers     │
└─────────────────────────────────────────────────────────────────┘
```

---

### Example 1: Customer Onboarding Process (SIPOC)

```yaml
PROCESS_NAME: "Customer Onboarding"
OWNER: "Customer Success Team"
FREQUENCY: "50 new customers/month"
CYCLE_TIME: "3 days (target), 5 days (current)"

SUPPLIERS:
  - source: "Sales Team"
    provides: "Signed contract, customer contact info"
    
  - source: "Stripe (Payment System)"
    provides: "Payment confirmation event"
    
  - source: "Salesforce CRM"
    provides: "Customer profile, purchased SKU"

INPUTS:
  - name: "Contract Signed Event"
    format: "Webhook (JSON)"
    schema: "contract_signed_v1"
    required: true
    
  - name: "Customer Profile"
    format: "API response (JSON)"
    fields: ["company_name", "contact_email", "plan_tier", "ARR"]
    required: true
    
  - name: "Payment Confirmation"
    format: "Stripe webhook"
    required: true

PROCESS_STEPS:
  1_trigger:
    name: "Detect contract signed"
    type: "Event trigger"
    system: "Zapier (automation platform)"
    
  2_provision:
    name: "Provision account"
    type: "AI Agent"
    agent: "AccountProvisioner-Agent"
    actions:
      - "Create tenant in product database"
      - "Generate API keys"
      - "Set up user permissions"
    sla: "< 5 minutes"
    
  3_notify:
    name: "Send welcome email"
    type: "AI Agent"
    agent: "OnboardingCopilot-Agent"
    actions:
      - "Generate personalized welcome email (based on plan tier)"
      - "Include setup guide, API docs, support contact"
    human_review: "No (auto-send for standard plans)"
    
  4_schedule:
    name: "Schedule kickoff call"
    type: "AI + Human"
    agent: "SchedulerBot-Agent"
    human: "CSM (Customer Success Manager)"
    actions:
      - "AI suggests 3 time slots (based on CSM calendar)"
      - "AI sends calendar invite"
      - "CSM confirms attendance"
    
  5_handoff:
    name: "Create customer success record"
    type: "System"
    system: "Gainsight (CS platform)"
    actions:
      - "Create customer health scorecard"
      - "Assign CSM based on ARR tier"
      - "Set 30/60/90 day check-in milestones"
    
  6_monitor:
    name: "Track onboarding progress"
    type: "AI Agent"
    agent: "OnboardingMonitor-Agent"
    actions:
      - "Monitor product usage (first login, first API call)"
      - "Alert CSM if no activity within 48 hours"
      - "Auto-send helpful tips based on usage patterns"

OUTPUTS:
  - name: "Provisioned Account"
    destination: "Product database"
    includes: ["Tenant ID", "API keys", "Admin user"]
    
  - name: "Welcome Email Sent"
    destination: "Customer inbox"
    includes: ["Setup guide", "Support contact", "Kickoff meeting invite"]
    
  - name: "Customer Success Record"
    destination: "Gainsight"
    includes: ["Customer profile", "Health score", "CSM assignment", "Milestones"]
    
  - name: "Onboarding Metrics"
    destination: "Data Warehouse"
    includes: ["Time to first login", "Kickoff call scheduled", "Health score"]

CUSTOMERS:
  - customer: "New customer"
    receives: "Welcome email, account credentials, kickoff invite"
    
  - customer: "CSM (Customer Success Manager)"
    receives: "Customer assignment, health scorecard, alert if no activity"
    
  - customer: "Product team"
    receives: "Usage analytics (aggregate), feature adoption trends"

AUTOMATION_LEVEL: "70% (steps 1-3, 5-6 automated, step 4 hybrid)"
HUMAN_TOUCHPOINTS: "Step 4 (CSM confirms kickoff), exception handling"

INTEGRATION_CONTRACTS:
  - contract_id: "CONTRACT-001"
    interface: "Salesforce → OnboardingOrchestrator"
    event: "opportunity.closed_won"
    
  - contract_id: "CONTRACT-002"
    interface: "Stripe → OnboardingOrchestrator"
    event: "payment.succeeded"
    
  - contract_id: "CONTRACT-003"
    interface: "OnboardingOrchestrator → Product DB"
    api: "POST /tenants/provision"
    
  - contract_id: "CONTRACT-004"
    interface: "OnboardingOrchestrator → Gainsight"
    api: "POST /customers"

DATA_SPINE_CONNECTIONS:
  - entity: "Customer"
    fields_written: ["tenant_id", "onboarding_status", "csm_assigned", "kickoff_date"]
    
  - entity: "OnboardingEvent"
    events_published:
      - "onboarding.started"
      - "account.provisioned"
      - "welcome_email.sent"
      - "kickoff.scheduled"
      - "onboarding.completed"
```

**Key Insights from this SIPOC:**
- **70% automated** (5 of 7 steps), 30% human touchpoints
- **3 AI agents involved**: AccountProvisioner, OnboardingCopilot, OnboardingMonitor
- **4 integration contracts** with upstream/downstream systems
- **Clear data spine connection** (Customer entity, OnboardingEvent stream)
- **SLA defined**: Account provisioned in <5 minutes

---

### Example 2: Invoice Processing (SIPOC)

```yaml
PROCESS_NAME: "Accounts Payable - Invoice Processing"
OWNER: "Finance Team"
FREQUENCY: "500 invoices/month"
CYCLE_TIME: "2 hours (target), 3 days (current - manual)"

SUPPLIERS:
  - source: "Vendors"
    provides: "Invoice (PDF via email or upload)"
    
  - source: "Procurement Team"
    provides: "Purchase orders (approval context)"
    
  - source: "Approvers (Department Heads)"
    provides: "Approval/rejection decisions"

INPUTS:
  - name: "Invoice PDF"
    format: "PDF document"
    delivery: "Email attachment or file upload"
    
  - name: "Purchase Order (PO)"
    format: "JSON from procurement system"
    fields: ["po_number", "vendor", "amount", "approver", "gl_code"]
    
  - name: "Vendor Master Data"
    format: "Database record"
    fields: ["vendor_id", "bank_account", "payment_terms", "tax_id"]

PROCESS_STEPS:
  1_receive:
    name: "Receive invoice"
    type: "System"
    system: "Email gateway or upload portal"
    
  2_extract:
    name: "Extract data from invoice"
    type: "AI Agent"
    agent: "InvoiceExtractor-Agent"
    technology: "OCR + GPT-4 Vision"
    fields_extracted:
      - "vendor_name"
      - "invoice_number"
      - "invoice_date"
      - "due_date"
      - "line_items" # array of {description, quantity, unit_price, total}
      - "subtotal"
      - "tax"
      - "total_amount"
      - "payment_terms"
    accuracy: "96.5% (validated monthly)"
    sla: "< 30 seconds per invoice"
    
  3_validate:
    name: "Validate against PO"
    type: "AI Agent"
    agent: "InvoiceValidator-Agent"
    checks:
      - "Does invoice match PO? (vendor, amount within 5% tolerance)"
      - "Is invoice a duplicate? (check invoice_number + vendor)"
      - "Are GL codes correct? (based on line items)"
      - "Is amount within approval threshold? (<$5K auto, >$5K manual)"
    output: "validation_status: [approved, needs_review, rejected]"
    
  4_route:
    name: "Route for approval"
    type: "Automation"
    system: "Workflow engine (Zapier/n8n)"
    logic: |
      IF validation_status == "approved" AND amount < $5,000:
        → Auto-approve (skip step 5)
      ELSE IF validation_status == "needs_review":
        → Route to approver (email + Slack notification)
      ELSE IF validation_status == "rejected":
        → Route to AP clerk for manual review
        
  5_approve:
    name: "Human approval (if needed)"
    type: "Human"
    role: "Department Head or AP Manager"
    interface: "Email link or Slack approval button"
    sla: "24 hours"
    
  6_pay:
    name: "Schedule payment"
    type: "System"
    system: "Bill.com or bank payment portal"
    actions:
      - "Create payment batch"
      - "Schedule payment based on terms (Net 30, etc.)"
      - "Send remittance advice to vendor"
    
  7_record:
    name: "Record in accounting system"
    type: "System"
    system: "QuickBooks / NetSuite"
    actions:
      - "Create journal entry (debit expense, credit AP)"
      - "Update general ledger"
      - "Mark invoice as paid"

OUTPUTS:
  - name: "Payment Scheduled"
    destination: "Bank / Bill.com"
    includes: ["Vendor bank details", "Amount", "Payment date"]
    
  - name: "Accounting Entry"
    destination: "General Ledger"
    includes: ["Journal entry", "GL codes", "Invoice metadata"]
    
  - name: "Vendor Notification"
    destination: "Vendor email"
    includes: ["Payment confirmation", "Expected payment date", "Remittance advice"]
    
  - name: "AP Metrics"
    destination: "Finance Dashboard"
    includes: ["Invoices processed", "Auto-approval rate", "Cycle time", "Errors"]

CUSTOMERS:
  - customer: "Vendors"
    receives: "Timely payment, remittance advice"
    
  - customer: "Finance team"
    receives: "Clean books, audit trail, process metrics"
    
  - customer: "Auditors"
    receives: "Complete audit trail (who approved, when, why)"

AUTOMATION_LEVEL: "85% (steps 1-3, 6-7 automated, steps 4-5 hybrid)"
HUMAN_TOUCHPOINTS: 
  - "Step 5: Approval for >$5K or flagged invoices (15% of total)"
  - "Exception handling: Validation failures, duplicate detection"

INTEGRATION_CONTRACTS:
  - contract_id: "CONTRACT-010"
    interface: "Email → InvoiceExtractor"
    trigger: "New email with PDF attachment in ap@company.com"
    
  - contract_id: "CONTRACT-011"
    interface: "InvoiceExtractor → InvoiceValidator"
    api: "POST /validate"
    payload: "extracted_invoice_data (JSON)"
    
  - contract_id: "CONTRACT-012"
    interface: "InvoiceValidator → Procurement System"
    api: "GET /purchase_orders/{po_number}"
    
  - contract_id: "CONTRACT-013"
    interface: "Workflow Engine → Bill.com"
    api: "POST /payments"
    
  - contract_id: "CONTRACT-014"
    interface: "Workflow Engine → QuickBooks"
    api: "POST /journal_entries"

DATA_SPINE_CONNECTIONS:
  - entity: "Invoice"
    schema: |
      {
        invoice_id: UUID,
        vendor_id: UUID,
        invoice_number: string,
        invoice_date: date,
        due_date: date,
        total_amount: decimal,
        status: enum[received, validated, approved, paid],
        approver: string (email),
        approved_at: timestamp,
        paid_at: timestamp,
        gl_code: string
      }
    
  - entity: "InvoiceProcessingEvent"
    events_published:
      - "invoice.received"
      - "invoice.extracted" # includes accuracy_score
      - "invoice.validated" # includes validation_result
      - "invoice.approved" # includes approver, approval_timestamp
      - "invoice.paid" # includes payment_date, payment_method
      - "invoice.rejected" # includes rejection_reason

PERFORMANCE_METRICS:
  baseline_manual:
    cycle_time: "3 days (from receipt to payment scheduled)"
    cost_per_invoice: "$15 (30 min × $30/hour AP clerk)"
    error_rate: "8% (wrong GL code, duplicate payments)"
    
  target_ai_automated:
    cycle_time: "2 hours (85% auto-approved within 2 hours)"
    cost_per_invoice: "$0.50 (AI processing cost)"
    error_rate: "2% (AI validation catches most errors)"
    
  roi:
    time_saved: "500 invoices × 30 min = 250 hours/month"
    cost_savings: "500 × ($15 - $0.50) = $7,250/month = $87K/year"
    quality_improvement: "8% → 2% error rate (75% reduction)"
```

**Key Insights:**
- **85% automation** (6 of 7 steps), AI handles data extraction and validation
- **$87K/year savings** (30 min → automated)
- **Error reduction**: 8% → 2% (AI validation more consistent than humans)
- **Clear escalation**: >$5K or validation failures → human review
- **Complete audit trail** via data spine (every event logged)

---

## Part 2: Integration Contracts

### What is an Integration Contract?

**Definition:** A formal agreement between two components (systems, agents, teams) defining:
- **What** data/events are exchanged
- **When** (triggers, frequency)
- **How** (API, webhook, message queue)
- **Quality** (schema, SLA, error handling)

**Why contracts matter:**
- **Reliability**: Both sides know what to expect
- **Debugging**: When integration fails, contract shows who's responsible
- **Versioning**: Contracts evolve (v1 → v2), backward compatibility managed
- **Governance**: Central registry of all integrations

---

### Integration Contract Template

```yaml
# INTEGRATION CONTRACT

contract_id: "CONTRACT-XXX"
version: "1.0"
status: "active" # draft, active, deprecated
created: "2025-11-01"
updated: "2025-11-01"
owner: "Platform Team"

# PARTIES
provider:
  name: "Salesforce CRM"
  team: "Sales Ops"
  contact: "salesops@company.com"
  
consumer:
  name: "OnboardingOrchestrator-Agent"
  team: "Customer Success Engineering"
  contact: "cs-eng@company.com"

# INTERFACE
interface_type: "webhook" # options: webhook, api, message_queue, file_transfer
direction: "push" # push (provider sends) or pull (consumer requests)

# TRIGGER
trigger:
  event: "opportunity.closed_won"
  description: "Fired when a sales opportunity is marked as Closed-Won"
  frequency: "~50 times/month"
  
# PAYLOAD
payload_format: "JSON"
payload_schema: |
  {
    "event_type": "opportunity.closed_won",
    "event_id": "UUID (unique event identifier)",
    "timestamp": "ISO 8601 datetime",
    "opportunity": {
      "id": "Salesforce Opportunity ID",
      "account_id": "Salesforce Account ID",
      "account_name": "string",
      "contact_email": "string (primary contact)",
      "contact_name": "string",
      "amount": "decimal (ARR)",
      "close_date": "ISO 8601 date",
      "product_sku": "string",
      "plan_tier": "enum[starter, professional, enterprise]"
    }
  }

payload_example: |
  {
    "event_type": "opportunity.closed_won",
    "event_id": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2025-11-05T14:32:15Z",
    "opportunity": {
      "id": "006xx000001X8U8AAK",
      "account_id": "001xx000003DGb0AAG",
      "account_name": "Acme Corp",
      "contact_email": "john.doe@acme.com",
      "contact_name": "John Doe",
      "amount": 50000.00,
      "close_date": "2025-11-05",
      "product_sku": "PROD-ENT-001",
      "plan_tier": "enterprise"
    }
  }

# DELIVERY
delivery:
  method: "HTTPS POST"
  endpoint: "https://api.company.com/webhooks/salesforce/opportunity"
  authentication: "Bearer token (OAuth 2.0)"
  retry_policy: "Exponential backoff (1s, 2s, 4s, 8s, 16s)"
  timeout: "10 seconds"
  
# SLA
sla:
  availability: "99.5% (provider guarantees webhook fires)"
  latency: "< 30 seconds (from Salesforce event to webhook delivery)"
  order_guarantee: "At-least-once delivery (consumer must handle duplicates)"
  
# ERROR HANDLING
error_handling:
  consumer_down:
    action: "Provider retries for 1 hour, then alerts provider team"
    
  invalid_payload:
    action: "Consumer returns HTTP 400, logs error, alerts consumer team"
    
  provider_rate_limit:
    action: "Consumer backs off, retries after 60 seconds"

# MONITORING
monitoring:
  metrics_tracked:
    - "webhook_delivery_success_rate"
    - "webhook_delivery_latency_p95"
    - "consumer_processing_time"
    - "payload_validation_failures"
    
  alerting:
    - trigger: "Success rate < 95% for 5 minutes"
      notify: ["provider team", "consumer team", "platform team"]
      
    - trigger: "Latency p95 > 60 seconds"
      notify: ["provider team"]

# VERSIONING
versioning:
  current_version: "1.0"
  backward_compatible: true
  deprecation_notice: "90 days before breaking change"
  
# DEPENDENCIES
depends_on:
  - contract_id: "CONTRACT-002" # Stripe payment confirmation
    relationship: "OnboardingOrchestrator waits for both Salesforce + Stripe events"

# TESTING
testing:
  sandbox_endpoint: "https://api.sandbox.company.com/webhooks/salesforce/opportunity"
  test_payload_available: true
  integration_test_frequency: "Weekly (automated)"

# GOVERNANCE
governance:
  change_approval_required: true
  approval_authority: "Platform Architecture Committee"
  last_reviewed: "2025-11-01"
  next_review: "2026-02-01" # quarterly
```

---

### Integration Contract Registry (Example)

**All contracts in central repository (wiki, git, or governance platform)**

| Contract ID | Provider | Consumer | Type | Status | Owner |
|-------------|----------|----------|------|--------|-------|
| CONTRACT-001 | Salesforce | OnboardingOrchestrator | Webhook | Active | CS Eng |
| CONTRACT-002 | Stripe | OnboardingOrchestrator | Webhook | Active | CS Eng |
| CONTRACT-003 | OnboardingOrchestrator | Product DB | API | Active | CS Eng |
| CONTRACT-004 | OnboardingOrchestrator | Gainsight | API | Active | CS Eng |
| CONTRACT-010 | Email Gateway | InvoiceExtractor | Email | Active | Finance Eng |
| CONTRACT-011 | InvoiceExtractor | InvoiceValidator | API | Active | Finance Eng |
| CONTRACT-012 | InvoiceValidator | Procurement System | API | Active | Finance Eng |
| CONTRACT-013 | Workflow Engine | Bill.com | API | Active | Finance Eng |
| CONTRACT-014 | Workflow Engine | QuickBooks | API | Active | Finance Eng |
| CONTRACT-020 | Product Events | DataWarehouse | Kafka | Active | Platform |
| CONTRACT-021 | DataWarehouse | ChurnPredictor | API | Active | Data Science |

**Benefits:**
- **Visibility**: See all integrations in one place
- **Impact analysis**: "If Salesforce changes API, which systems affected?" → Query contracts
- **Onboarding**: New engineers understand system architecture from contracts
- **Governance**: Track which contracts need review, deprecation

---

## Part 3: Data Spine Integration

### What is the Data Spine?

**Data Spine** (Layer 2 of SOLID.AI) = Unified data foundation that all systems connect to

**Purpose:**
- **Single source of truth** for core entities (Customer, User, Product, Order, etc.)
- **Event stream** for real-time data flow
- **Schema registry** for consistent data contracts

**Components:**
1. **Entity Database** (master data)
2. **Event Bus** (Kafka, EventBridge, Pub/Sub)
3. **Schema Registry** (Avro, Protobuf, or JSON Schema)
4. **Data Contracts** (define entity structure)

---

### Data Contract Template (Entity)

```yaml
# DATA CONTRACT: Customer Entity

entity_name: "Customer"
version: "2.0"
owner: "Data Platform Team"
classification: "PII - Sensitive"

# SCHEMA
schema:
  customer_id:
    type: "UUID"
    required: true
    primary_key: true
    
  external_ids:
    type: "object"
    properties:
      salesforce_account_id: "string"
      stripe_customer_id: "string"
      zendesk_organization_id: "string"
    description: "IDs from external systems (for mapping)"
    
  company_name:
    type: "string"
    required: true
    max_length: 200
    
  contact_email:
    type: "string"
    format: "email"
    required: true
    pii: true
    
  contact_name:
    type: "string"
    max_length: 100
    pii: true
    
  plan_tier:
    type: "enum"
    values: ["starter", "professional", "enterprise"]
    required: true
    
  arr:
    type: "decimal"
    precision: 10
    scale: 2
    description: "Annual Recurring Revenue in USD"
    
  mrr:
    type: "decimal"
    precision: 10
    scale: 2
    description: "Monthly Recurring Revenue in USD"
    
  status:
    type: "enum"
    values: ["trial", "active", "churned", "suspended"]
    required: true
    
  health_score:
    type: "integer"
    min: 0
    max: 100
    description: "Customer health score (AI-calculated)"
    
  churn_risk:
    type: "enum"
    values: ["low", "medium", "high"]
    description: "Churn risk (AI-predicted)"
    
  csm_assigned:
    type: "string"
    format: "email"
    description: "Assigned Customer Success Manager"
    
  created_at:
    type: "timestamp"
    required: true
    
  updated_at:
    type: "timestamp"
    required: true

# WRITE PERMISSIONS
write_permissions:
  - system: "OnboardingOrchestrator"
    fields: ["company_name", "contact_email", "plan_tier", "arr", "csm_assigned"]
    
  - system: "ChurnPredictor-Agent"
    fields: ["health_score", "churn_risk"]
    
  - system: "Stripe-Integration"
    fields: ["mrr", "status"]
    
  - system: "Salesforce-Sync"
    fields: ["external_ids.salesforce_account_id", "contact_name"]

# READ PERMISSIONS
read_permissions:
  - system: "*" # all systems can read (subject to RBAC)
    use_cases: ["Analytics", "Reporting", "AI model training"]

# DATA QUALITY RULES
data_quality:
  - rule: "contact_email must be unique"
    enforcement: "database constraint"
    
  - rule: "arr must match Stripe subscription value (within 5%)"
    enforcement: "daily reconciliation job"
    
  - rule: "health_score recalculated every 24 hours"
    enforcement: "ChurnPredictor-Agent cron job"
    
  - rule: "PII fields encrypted at rest"
    enforcement: "database-level encryption"

# RETENTION POLICY
retention:
  active_records: "Indefinite (while customer active)"
  churned_records: "7 years (for analytics, compliance)"
  pii_deletion: "30 days after customer requests deletion (GDPR)"

# VERSIONING
versioning:
  changelog:
    - version: "2.0"
      date: "2025-10-01"
      changes: "Added churn_risk field (AI prediction)"
      
    - version: "1.5"
      date: "2025-06-01"
      changes: "Added health_score field"
      
    - version: "1.0"
      date: "2024-01-01"
      changes: "Initial schema"
```

---

### Data Contract Template (Event)

```yaml
# DATA CONTRACT: Customer Lifecycle Events

event_stream: "customer_events"
version: "1.0"
owner: "Data Platform Team"
platform: "Kafka" # or AWS EventBridge, Google Pub/Sub
topic: "customers.lifecycle"

# EVENT TYPES
event_types:
  - event_name: "customer.created"
    description: "New customer account created"
    producer: "OnboardingOrchestrator"
    consumers: ["DataWarehouse", "Analytics", "ChurnPredictor"]
    
  - event_name: "customer.plan_changed"
    description: "Customer upgraded or downgraded plan"
    producer: "Billing-Agent"
    consumers: ["DataWarehouse", "Salesforce-Sync", "CSM-Dashboard"]
    
  - event_name: "customer.health_score_updated"
    description: "Customer health score recalculated"
    producer: "ChurnPredictor-Agent"
    consumers: ["Gainsight", "CSM-Dashboard", "AlertingSystem"]
    
  - event_name: "customer.churned"
    description: "Customer cancelled subscription"
    producer: "Billing-Agent"
    consumers: ["DataWarehouse", "Salesforce-Sync", "Analytics", "CSM-Dashboard"]

# EVENT SCHEMA (example: customer.created)
event_schema: |
  {
    "event_id": "UUID (unique event identifier)",
    "event_type": "string (e.g., 'customer.created')",
    "event_version": "string (e.g., '1.0')",
    "timestamp": "ISO 8601 datetime (when event occurred)",
    "source": "string (system that produced event)",
    "trace_id": "UUID (for distributed tracing)",
    
    "data": {
      "customer_id": "UUID",
      "company_name": "string",
      "contact_email": "string",
      "plan_tier": "enum[starter, professional, enterprise]",
      "arr": "decimal",
      "created_at": "ISO 8601 datetime"
    },
    
    "metadata": {
      "producer_version": "string (e.g., 'OnboardingOrchestrator-v2.3')",
      "idempotency_key": "string (for deduplication)"
    }
  }

# DELIVERY GUARANTEES
delivery:
  guarantee: "at-least-once" # consumers must handle duplicates
  ordering: "partition-ordered" # events for same customer_id in order
  retention: "7 days (Kafka retention)"
  
# SCHEMA EVOLUTION
schema_evolution:
  compatibility: "backward" # new fields can be added, existing fields can't be removed
  validation: "Schema registry enforces compatibility on publish"
  
# MONITORING
monitoring:
  metrics:
    - "event_publish_rate (events/second)"
    - "event_lag (consumer lag per partition)"
    - "event_processing_time (consumer latency)"
    - "schema_validation_failures"
    
  alerts:
    - trigger: "consumer lag > 1000 messages"
      notify: ["platform-team", "consumer-owner"]
```

---

### How Processes Connect to Data Spine

**Pattern 1: Write to Entity (Master Data)**

```
Process: OnboardingOrchestrator
  ↓
Step 5: Create customer record
  ↓
Data Spine API: POST /entities/customers
  ↓
Customer entity written to database
  ↓
Other systems read Customer entity (single source of truth)
```

**Pattern 2: Publish Event (Real-Time Stream)**

```
Process: OnboardingOrchestrator
  ↓
Step 6: Account provisioned successfully
  ↓
Data Spine Event Bus: Publish "customer.created" event
  ↓
Consumers receive event:
  - DataWarehouse (store for analytics)
  - ChurnPredictor (initialize health score)
  - CSM-Dashboard (add to CSM's queue)
  - Salesforce-Sync (update external CRM)
```

**Pattern 3: Read from Entity (Query)**

```
Process: ChurnPredictor-Agent
  ↓
Step 1: Get customer data
  ↓
Data Spine API: GET /entities/customers/{customer_id}
  ↓
Returns: Customer entity (health_score, usage_metrics, etc.)
  ↓
Step 2: Calculate churn risk
  ↓
Step 3: Update Customer entity with new churn_risk value
  ↓
Data Spine API: PATCH /entities/customers/{customer_id}
  ↓
Step 4: Publish event "customer.churn_risk_changed"
```

---

## Part 4: Automation Mesh Patterns

### What is the Automation Mesh?

**Automation Mesh** (Layer 4 of SOLID.AI) = Network of interconnected workflows, agents, and systems

**Key Concepts:**
- **Orchestration**: Central controller (workflow engine) coordinates steps
- **Choreography**: Decentralized (components react to events, no central controller)
- **Hybrid**: Combination of both (most real-world architectures)

---

### Pattern 1: Linear Workflow (Orchestration)

**Use case:** Simple, sequential process (A → B → C → D)

**Example:** Invoice Processing

```
┌─────────────────────────────────────────────────────┐
│ LINEAR WORKFLOW: Invoice Processing                 │
├─────────────────────────────────────────────────────┤
│                                                      │
│  [1] Email → [2] Extract → [3] Validate →           │
│  [4] Route → [5] Approve → [6] Pay → [7] Record     │
│                                                      │
│  Orchestrator: Zapier / n8n                          │
│  Human touchpoint: Step 5 (approval if >$5K)        │
│                                                      │
└─────────────────────────────────────────────────────┘
```

**Implementation (n8n workflow):**

```yaml
workflow:
  name: "Invoice Processing"
  trigger:
    type: "email"
    filter: "to:ap@company.com AND has:attachment"
    
  nodes:
    - id: "extract"
      type: "http_request"
      action: "POST"
      url: "https://api.company.com/ai/invoice-extractor"
      payload: "{email.attachment}"
      
    - id: "validate"
      type: "http_request"
      action: "POST"
      url: "https://api.company.com/ai/invoice-validator"
      payload: "{extract.output}"
      
    - id: "route"
      type: "conditional"
      logic: |
        if validate.status == "approved" and extract.amount < 5000:
          → next_node: "pay"
        else:
          → next_node: "approval_request"
          
    - id: "approval_request"
      type: "email"
      to: "{extract.approver_email}"
      subject: "Invoice Approval Required: {extract.vendor} - ${extract.amount}"
      body: "Click to approve: {approval_link}"
      wait_for_response: true
      timeout: "24 hours"
      
    - id: "pay"
      type: "http_request"
      action: "POST"
      url: "https://api.bill.com/payments"
      payload: "{extract.vendor, extract.amount, extract.bank_account}"
      
    - id: "record"
      type: "http_request"
      action: "POST"
      url: "https://api.quickbooks.com/journal_entries"
      payload: "{extract.gl_code, extract.amount}"
      
    - id: "publish_event"
      type: "kafka"
      topic: "invoice_events"
      event: "invoice.paid"
      payload: "{invoice_id, vendor, amount, paid_at}"
```

---

### Pattern 2: Event-Driven (Choreography)

**Use case:** Loosely coupled, multiple independent systems react to same event

**Example:** Customer Onboarding

```
┌─────────────────────────────────────────────────────────────┐
│ EVENT-DRIVEN: Customer Onboarding                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Trigger: "customer.created" event published                │
│                                                              │
│  Independent consumers (react in parallel):                 │
│  ├─ AccountProvisioner → Provisions tenant                  │
│  ├─ WelcomeEmailer → Sends welcome email                    │
│  ├─ Gainsight → Creates CS record                           │
│  ├─ DataWarehouse → Stores for analytics                    │
│  └─ ChurnPredictor → Initializes health score              │
│                                                              │
│  No central orchestrator (each consumer independent)        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Benefits:**
- **Decoupled**: Add new consumer without changing producer
- **Scalable**: Each consumer scales independently
- **Resilient**: If one consumer fails, others continue

**Challenges:**
- **Harder to debug**: No single place to see full workflow
- **Ordering complexity**: Events may arrive out of order
- **Eventual consistency**: Different systems may have different views temporarily

---

### Pattern 3: Hybrid (Orchestration + Choreography)

**Use case:** Complex process with both sequential steps and parallel reactions

**Example:** Customer Onboarding (Hybrid)

```
┌──────────────────────────────────────────────────────────────┐
│ HYBRID: Customer Onboarding                                  │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  ORCHESTRATED PART (sequential):                             │
│  [1] Receive contract → [2] Validate payment →               │
│  [3] Provision account → [4] Publish "account.provisioned"   │
│                                                               │
│  EVENT-DRIVEN PART (parallel):                               │
│  Event: "account.provisioned"                                │
│    ├─ WelcomeEmailer → Send email                            │
│    ├─ SchedulerBot → Book kickoff call                       │
│    ├─ Gainsight → Create CS record                           │
│    └─ DataWarehouse → Store analytics                        │
│                                                               │
│  ORCHESTRATED PART (wait for dependencies):                  │
│  [5] Wait for "welcome_email.sent" + "kickoff.scheduled"     │
│  [6] Publish "onboarding.completed"                          │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

**Best of both worlds:**
- **Orchestration** for critical path (account provisioning must happen first)
- **Choreography** for parallel, independent tasks (email, scheduling, etc.)
- **Orchestration** for final coordination (wait for prerequisites)

---

### Pattern 4: Saga (Distributed Transaction)

**Use case:** Multi-step process where each step can fail, needs rollback

**Example:** Order Fulfillment

```
┌──────────────────────────────────────────────────────────────┐
│ SAGA PATTERN: Order Fulfillment                              │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  Happy Path:                                                 │
│  [1] Reserve inventory → [2] Charge payment →                │
│  [3] Ship order → [4] Notify customer                        │
│                                                               │
│  Failure Scenario (payment fails at step 2):                 │
│  [1] Reserve inventory ✅                                     │
│  [2] Charge payment ❌ FAILED                                │
│      ↓                                                        │
│  [1-rollback] Release inventory reservation                  │
│  [notify] Email customer "Payment failed, order cancelled"   │
│                                                               │
│  Each step has compensating action (undo):                   │
│  - Reserve inventory ↔ Release reservation                   │
│  - Charge payment ↔ Refund                                   │
│  - Ship order ↔ Initiate return                              │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

**Implementation:**

```yaml
saga:
  name: "Order Fulfillment"
  
  steps:
    - name: "reserve_inventory"
      action: "POST /inventory/reserve"
      compensation: "POST /inventory/release"
      
    - name: "charge_payment"
      action: "POST /payments/charge"
      compensation: "POST /payments/refund"
      
    - name: "ship_order"
      action: "POST /shipping/create_shipment"
      compensation: "POST /shipping/cancel_shipment"
      
    - name: "notify_customer"
      action: "POST /notifications/send_email"
      compensation: "POST /notifications/send_cancellation_email"
      
  on_failure:
    strategy: "rollback" # execute compensation actions in reverse order
    notify: ["ops-team", "customer"]
```

---

## Part 5: Implementation Templates

### Template 1: Process Mapping Worksheet

**Use this template to map any process:**

```markdown
# PROCESS MAPPING WORKSHEET

## Basic Information
- **Process Name:** _______________________
- **Owner:** _______________________
- **Frequency:** _______________________ (e.g., 50/month, daily, on-demand)
- **Current Cycle Time:** _______________________ (baseline)
- **Target Cycle Time:** _______________________ (goal)
- **Current Cost per Instance:** _______________________
- **Target Cost:** _______________________

## SIPOC Mapping

### SUPPLIERS (Who/what provides inputs?)
1. _______________________
2. _______________________
3. _______________________

### INPUTS (What do we need to start?)
1. _______________________
   - Format: _______________________
   - Source: _______________________
   
2. _______________________
   - Format: _______________________
   - Source: _______________________

### PROCESS STEPS (What are the high-level steps?)

| # | Step Name | Type | Owner | Current Time | Target Time | Automation Opportunity |
|---|-----------|------|-------|--------------|-------------|------------------------|
| 1 | _________ | H/AI/S | _____ | _________ | _________ | High / Medium / Low |
| 2 | _________ | H/AI/S | _____ | _________ | _________ | High / Medium / Low |
| 3 | _________ | H/AI/S | _____ | _________ | _________ | High / Medium / Low |
| 4 | _________ | H/AI/S | _____ | _________ | _________ | High / Medium / Low |
| 5 | _________ | H/AI/S | _____ | _________ | _________ | High / Medium / Low |

Legend: H=Human, AI=AI Agent, S=System

### OUTPUTS (What do we produce?)
1. _______________________
   - Destination: _______________________
   - Format: _______________________
   
2. _______________________
   - Destination: _______________________
   - Format: _______________________

### CUSTOMERS (Who receives outputs?)
1. _______________________
2. _______________________

## Automation Analysis

**Current Automation Level:** _____% (calculate: automated steps / total steps)

**Target Automation Level:** _____% (goal)

**High-Priority Automation Opportunities:**
1. Step __: _______________________ (Why: _______________________)
2. Step __: _______________________ (Why: _______________________)
3. Step __: _______________________ (Why: _______________________)

## Integration Requirements

**Upstream Systems:** (systems we get data from)
1. _______________________
2. _______________________

**Downstream Systems:** (systems we send data to)
1. _______________________
2. _______________________

**Integration Contracts Needed:**
1. Contract between ____________ and ____________
2. Contract between ____________ and ____________

## Data Spine Integration

**Entities Read:** (which entities do we query?)
1. _______________________
2. _______________________

**Entities Written:** (which entities do we update?)
1. _______________________
2. _______________________

**Events Published:** (which events do we emit?)
1. _______________________
2. _______________________

**Events Consumed:** (which events do we listen to?)
1. _______________________
2. _______________________

## Success Metrics

**KPIs to Track:**
1. _______________________ (baseline: _____, target: _____)
2. _______________________ (baseline: _____, target: _____)
3. _______________________ (baseline: _____, target: _____)

## Next Steps

1. [ ] Complete SIPOC mapping
2. [ ] Define integration contracts
3. [ ] Design data spine schema
4. [ ] Prototype high-priority automation (step ___)
5. [ ] Measure baseline metrics
6. [ ] Implement automation
7. [ ] Measure post-automation metrics
8. [ ] Iterate and improve
```

---

### Template 2: Integration Contract (Simplified)

```yaml
# INTEGRATION CONTRACT (QUICK TEMPLATE)

CONTRACT_ID: "CONTRACT-XXX"
STATUS: "draft" # or active, deprecated

# WHO
PROVIDER: "________________________"
CONSUMER: "________________________"

# WHAT
INTERFACE_TYPE: "webhook" # or api, message_queue, file
TRIGGER: "________________________" # event name or API endpoint

# DATA
PAYLOAD_FORMAT: "JSON" # or XML, CSV, Avro
PAYLOAD_SCHEMA: |
  {
    # Paste JSON schema or example here
  }

# HOW
DELIVERY_METHOD: "HTTPS POST" # or GET, Kafka, S3, etc.
ENDPOINT: "https://___________________________"
AUTHENTICATION: "Bearer token" # or API key, OAuth, etc.

# QUALITY
SLA_LATENCY: "< ___ seconds"
SLA_AVAILABILITY: "___ %"
RETRY_POLICY: "Exponential backoff"

# MONITORING
SUCCESS_METRIC: "________________________"
ALERT_THRESHOLD: "________________________"
OWNER: "________________________" (team responsible)

# GOVERNANCE
LAST_REVIEWED: "YYYY-MM-DD"
NEXT_REVIEW: "YYYY-MM-DD" (quarterly recommended)
```

---

### Template 3: Data Contract (Entity)

```yaml
# DATA CONTRACT: ____________ Entity

ENTITY_NAME: "____________"
VERSION: "1.0"
OWNER: "____________ Team"
CLASSIFICATION: "PII / Sensitive / Public"

# SCHEMA
SCHEMA:
  primary_key:
    type: "UUID or string"
    required: true
    
  field_2:
    type: "string / integer / decimal / timestamp / enum / object"
    required: true / false
    description: "____________"
    
  field_3:
    type: "____________"
    description: "____________"

# PERMISSIONS
WRITE_PERMISSIONS:
  - system: "____________"
    fields: ["____________", "____________"]
    
READ_PERMISSIONS:
  - system: "*" # all systems, or list specific ones

# QUALITY RULES
DATA_QUALITY:
  - rule: "____________"
    enforcement: "database constraint / daily job / manual"

# RETENTION
RETENTION:
  active: "____________" (e.g., indefinite, 7 years)
  deleted: "____________" (e.g., 30 days after request)
```

---

## Conclusion: From Chaos to Clarity

### The Transformation

**Before (Process Chaos):**
- ❌ Undocumented workflows (tribal knowledge)
- ❌ Brittle integrations (break when systems change)
- ❌ Data silos (each system has own copy, inconsistent)
- ❌ Manual handoffs (email, Slack, spreadsheets)
- ❌ No visibility (can't measure, can't improve)

**After (Process Clarity):**
- ✅ **SIPOC-mapped** processes (everyone understands flow)
- ✅ **Integration contracts** (clear interfaces, reliable)
- ✅ **Data spine** (single source of truth)
- ✅ **Automation mesh** (AI + humans collaborate seamlessly)
- ✅ **Metrics-driven** (measure, optimize, repeat)

---

### The Roadmap

**Phase 1: Map (Weeks 1-4)**
1. Select 3 high-impact processes (onboarding, invoice processing, support tickets)
2. Complete SIPOC mapping for each
3. Identify automation opportunities
4. Document baseline metrics

**Phase 2: Contract (Weeks 5-8)**
1. Define integration contracts for top 10 integrations
2. Create central contract registry
3. Establish data contracts for 5 core entities
4. Set up data spine infrastructure (event bus, schema registry)

**Phase 3: Automate (Weeks 9-16)**
1. Implement first automated process (70%+ automation)
2. Deploy AI agents for high-value steps
3. Connect to data spine (publish events, read/write entities)
4. Monitor metrics (cycle time, cost, quality)

**Phase 4: Scale (Months 5-12)**
1. Map and automate 20+ processes
2. 100+ integration contracts documented
3. Data spine adopted across organization
4. Automation mesh becomes "the way we work"

---

### Success Metrics

**Process Efficiency:**
- Cycle time: -50% average (manual → automated)
- Cost per transaction: -70% average
- Error rate: -60% average (AI validation > manual)

**Integration Reliability:**
- Contract coverage: 100% of critical integrations
- Integration failures: <1% (down from 10%+)
- Downtime from integration issues: -80%

**Data Quality:**
- Single source of truth: 100% (no data silos)
- Data freshness: <1 hour (real-time event stream)
- Data quality score: >90% (completeness, accuracy)

---

### Final Thought

> **"A process without a map is a black box. A black box cannot be automated. What cannot be automated cannot scale."**

**Your mission:** Map, contract, integrate, automate, measure, improve, repeat.

The organizations that master this will become **AI-native operating systems**—fluid, efficient, and unstoppable.

---

**Next Steps:**
- [Data Spine Guide](data-spine-structuring-governance.md) - Deep dive on Layer 2
- [Implementing AI Agents](implementing-ai-agents-practical-guide.md) - Build agents for your processes
- [Integration Guide](../foundation/solid-ai-integration-guide.md) - How everything connects
- [Architecture](../../DOCS/02-architecture.md) - SOLID.AI 6-layer framework

**ADOPTION Resources:**
- **Diagram:** [Process SIPOC Example](../../DIAGRAMS/process-sipoc-example.mmd) - Invoice processing with 6 AI agents & automation mesh
- **Diagram:** [SIPOC Automation Pattern](../../DIAGRAMS/sipoc-automation-pattern.mmd) - General automation pattern

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Framework:** SOLID.AI  
**License:** MIT