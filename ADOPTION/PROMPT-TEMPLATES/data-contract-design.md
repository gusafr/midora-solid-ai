# Data Contract Design Prompt

**Category:** Data Architecture | **Framework:** SOLID.AI | **Use Case:** Creating data interfaces

---

## When to Use This Prompt

Use this prompt when **defining any new data contract** for the Data Spine to ensure clear ownership, quality, and interoperability.

**Ideal for:**
- Designing APIs or events
- Creating new data models
- Establishing service contracts
- Enabling cross-team data sharing

---

## The Prompt

```
I need to design a data contract for: [ENTITY, EVENT, OR API]

Context:
- Producer: [Team/system creating this data]
- Consumers: [Teams/systems using this data]
- Purpose: [Why this data exists]

Help me create a comprehensive data contract following SOLID.AI Data Spine principles:

1. **Contract Identity**
   - Name: [Clear, semantic name]
   - Version: [Semantic versioning strategy]
   - Type: [Entity / Event / API / Stream]

2. **Semantic Definition**
   - What does this data represent in business terms?
   - What real-world concepts or events does it model?
   - How does it relate to other contracts in our domain?

3. **Schema**
   - Fields with types, constraints, and semantic meaning
   - Required vs. optional fields
   - Enumerations and valid value ranges
   - Nesting and relationships

4. **Ownership & Lifecycle**
   - Owner: [Team responsible for this contract]
   - Lifecycle: [Creation, updates, deletion/expiry rules]
   - Change management: [How breaking changes are handled]
   - SLA: [Availability, freshness, latency commitments]

5. **Quality Expectations**
   - Completeness: [What fields must always be present?]
   - Accuracy: [What validation rules apply?]
   - Freshness: [How recent must data be?]
   - Consistency: [What invariants must hold?]

6. **Privacy & Security**
   - Sensitivity level: [Public / Internal / Confidential / Restricted]
   - PII/PHI present: [Yes/No - which fields?]
   - Access controls: [Who can read/write?]
   - Encryption requirements: [At rest, in transit]
   - Retention policy: [How long is data kept?]

7. **Consuming Systems**
   - Current consumers: [List teams/systems]
   - Use cases: [What they do with this data]
   - Dependencies: [Critical vs. nice-to-have]

8. **Observability**
   - Monitoring: [What health metrics are tracked?]
   - Alerts: [What triggers notifications?]
   - Lineage: [How is data flow tracked?]

9. **Evolution Strategy**
   - Versioning approach: [Backward compatible, versioned endpoints, etc.]
   - Deprecation policy: [How old versions are sunset]
   - Migration support: [How consumers are helped to upgrade]

10. **Examples & Documentation**
    - Sample data (valid examples)
    - Edge cases and special scenarios
    - Integration guide for new consumers

Generate the contract in YAML or JSON Schema format.
```

---

## Example Usage

### Input

```
I need to design a data contract for: User enrollment events when students join a course

Context:
- Producer: Enrollment Service
- Consumers: Analytics, Email Service, Recommendation Engine
- Purpose: Track student course enrollments for notifications, analytics, and personalization

Help me create a comprehensive data contract following SOLID.AI Data Spine principles:
[... paste full prompt above ...]
```

### Expected Output (YAML format)

```yaml
contract:
  identity:
    name: "user-enrollment-event"
    version: "1.0.0"
    type: "event"
  
  semantic_definition:
    description: "Emitted when a student successfully enrolls in a course"
    business_concepts: ["student", "course", "enrollment", "academic_term"]
    related_contracts:
      - "user-profile-entity"
      - "course-catalog-entity"
      - "enrollment-cancelled-event"
  
  schema:
    format: "JSON Schema v2020-12"
    fields:
      - name: "event_id"
        type: "string (UUID)"
        required: true
        description: "Unique identifier for this event instance"
      
      - name: "timestamp"
        type: "string (ISO 8601)"
        required: true
        description: "When the enrollment occurred (UTC)"
      
      - name: "user_id"
        type: "string (UUID)"
        required: true
        description: "Student's unique identifier"
        pii: true
      
      - name: "course_id"
        type: "string"
        required: true
        description: "Course identifier from catalog"
      
      - name: "enrollment_type"
        type: "enum"
        required: true
        values: ["free", "paid", "scholarship", "audit"]
        description: "Type of enrollment"
      
      - name: "payment_amount"
        type: "number (decimal)"
        required: false
        description: "Amount paid (if enrollment_type=paid)"
        constraint: ">= 0"
      
      - name: "referral_source"
        type: "string"
        required: false
        description: "How student found the course (marketing attribution)"
        values: ["organic", "email", "social", "partner", "direct"]
  
  ownership:
    owner_team: "Enrollment Service Team"
    maintainer: "enrollment-team@company.com"
    lifecycle:
      created: "At successful enrollment transaction"
      updated: "Events are immutable (publish new event for changes)"
      retention: "7 years (regulatory requirement)"
    
    sla:
      availability: "99.9%"
      freshness: "Events published within 5 seconds of enrollment"
      latency: "p95 delivery < 500ms"
  
  quality_expectations:
    completeness: "All required fields must be present; events missing required fields are rejected"
    accuracy: "user_id and course_id must exist in respective systems before event emission"
    freshness: "timestamp must be within last 60 seconds when published"
    consistency: "If enrollment_type=paid, payment_amount must be present and >0"
  
  privacy_security:
    sensitivity: "confidential"
    pii_fields: ["user_id"]
    access_controls:
      read: ["analytics-team", "email-service", "recommendation-engine"]
      write: ["enrollment-service"]
    encryption:
      at_rest: "AES-256"
      in_transit: "TLS 1.3"
    retention: "7 years, then anonymized (user_id hashed)"
  
  consumers:
    - name: "Analytics Service"
      use_case: "Track enrollment trends, funnel analysis, cohort reports"
      criticality: "high"
    
    - name: "Email Service"
      use_case: "Send welcome email and course access details"
      criticality: "high"
    
    - name: "Recommendation Engine"
      use_case: "Personalize course recommendations based on enrollment patterns"
      criticality: "medium"
  
  observability:
    monitoring:
      - "Event publish rate (events/second)"
      - "Schema validation failure rate"
      - "Consumer lag (time to process)"
    
    alerts:
      - condition: "Schema validation failures > 1% over 5 minutes"
        severity: "high"
      - condition: "No events published for > 10 minutes during business hours"
        severity: "critical"
    
    lineage:
      source: "enrollment-service database (enrollments table)"
      transformations: "Enriched with course metadata from catalog service"
      destinations: ["analytics-datalake", "email-queue", "recommendation-cache"]
  
  evolution:
    versioning: "Semantic versioning; breaking changes require new major version"
    deprecation_policy: "90-day notice for breaking changes; 6-month support for old versions"
    migration_support: "Dual-publish during transition; migration guides in docs"
  
  examples:
    valid_example:
      event_id: "a3bb189e-8bf9-4f3f-8ae0-3e5f79c3c3e7"
      timestamp: "2025-11-02T14:30:00Z"
      user_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
      course_id: "CS101"
      enrollment_type: "paid"
      payment_amount: 299.99
      referral_source: "email"
    
    edge_case_free_enrollment:
      event_id: "b4cc299f-9cg0-5g4g-9bf1-4f6g80d4d4f8"
      timestamp: "2025-11-02T15:45:00Z"
      user_id: "g58bd21c-69dd-5483-b678-1f13c3d4e570"
      course_id: "INTRO-FREE"
      enrollment_type: "free"
      referral_source: "organic"
  
  documentation:
    integration_guide: "https://docs.company.com/data-contracts/user-enrollment-event"
    changelog: "https://github.com/company/data-contracts/blob/main/CHANGELOG.md#user-enrollment-event"
```

---

## Customization Tips

**For real-time streams:**
Add: "What partitioning strategy ensures scalability?"

**For sensitive data:**
Add: "What data masking or anonymization is required?"

**For high-volume data:**
Add: "What sampling or aggregation reduces load?"

**For regulatory compliance:**
Add: "What audit trail or compliance requirements exist?"

---

## Follow-Up Prompts

After generating the contract:

```
Review this data contract for potential privacy risks or GDPR compliance issues.
```

```
Generate tests to validate this contract's schema and quality expectations.
```

```
Create a migration plan for existing consumers to adopt this contract.
```

```
Design monitoring dashboards to track this contract's health and usage.
```

---

## SOLID.AI Principles Applied

- ✅ **Data Spine** - Creates shared, trusted data contracts
- ✅ **Purpose-Led Decisions** - Grounds data in business meaning
- ✅ **Ethical Automation** - Bakes in privacy and security
- ✅ **Scalable Simplicity** - Clear, semantic, evolvable contracts
- ✅ **Continuous Learning** - Enables observability and iteration

---

## Related Resources

- **Data Spine RFC:** [RFC/rfc-0002-data-layer.md](../../RFC/rfc-0002-data-layer.md)
- **Architecture:** [DOCS/02-architecture.md](../../DOCS/02-architecture.md)
- **Template:** [TEMPLATES/data-contract-template.yaml](../TEMPLATES/data-contract-template.yaml)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Share Your Results:** [GitHub Discussions](https://github.com/gusafr/midora-solid-ai/discussions)
