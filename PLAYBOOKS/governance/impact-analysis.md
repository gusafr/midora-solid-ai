# Impact Analysis Playbook for Initiatives & Projects

**For:** Product Managers, Tech Leads, Architects, Portfolio Managers assessing internal initiatives

**Purpose:** Systematically evaluate impact across technical, organizational, operational, and architectural dimensions before committing resources

**Outcome:** Clear t-shirt size (PP/P/M/G/GG), risk assessment, resource estimate, and go/no-go recommendation

---

## Overview

### Why Impact Analysis Matters

**Problem:** Teams commit to initiatives without fully understanding:
- **Technical complexity** (how many systems affected? data migration required?)
- **Organizational impact** (how many teams involved? skills gaps?)
- **Operational risk** (downtime? rollback plan? monitoring?)
- **Architectural debt** (quick fix or strategic investment?)

**Solution:** Structured impact analysis provides:
- **Visibility:** All stakeholders see full scope before commitment
- **Prioritization:** Rank initiatives by business value vs. complexity
- **Resource planning:** Accurate estimates (not guesses)
- **Risk mitigation:** Identify blockers early, plan mitigations
- **AI assistance:** ImpactAnalyzer-Agent automates 60% of assessment work

---

## T-Shirt Sizing Framework

### Size Definitions (PP to GG)

| Size | Effort | Team Size | Duration | Complexity | Risk | Examples |
|------|--------|-----------|----------|------------|------|----------|
| **PP (Extra Small)** | 1-3 days | 1 person | <1 week | Trivial | Low | Config change, flag toggle, log level adjustment |
| **P (Small)** | 3-10 days | 1-2 people | 1-2 weeks | Low | Low-Medium | Bug fix, UI tweak, add field to existing form |
| **M (Medium)** | 10-30 days | 2-4 people | 1-2 months | Medium | Medium | New feature (single service), API endpoint, dashboard |
| **G (Large)** | 30-90 days | 4-8 people | 2-4 months | High | High | Multi-service feature, data migration, new module |
| **GG (Extra Large)** | 90+ days | 8+ people | 4+ months | Very High | Very High | Platform rewrite, architecture overhaul, system migration |

---

### Sizing Criteria Matrix

**Use this matrix to determine t-shirt size across 4 dimensions:**

| Dimension | PP | P | M | G | GG |
|-----------|----|----|----|----|-----|
| **Technical Complexity** | Single file change | Single service | 2-3 services | 4+ services | System-wide |
| **Data Impact** | No data changes | Read-only | CRUD (single table) | Multi-table migration | Database redesign |
| **Dependencies** | None | 1 internal | 2-3 internal | 4+ internal OR 1 external | Multiple external |
| **Testing Required** | Unit tests | Unit + integration | E2E tests | Performance tests | Load + chaos testing |
| **Documentation** | Code comments | README update | API docs + runbook | Architecture docs | Full system redesign docs |
| **Rollback Complexity** | Instant (revert commit) | <1 hour | <1 day | 1-3 days | >3 days (may be irreversible) |
| **Teams Involved** | 1 team | 1 team | 2 teams | 3-4 teams | 5+ teams |
| **Skills Required** | Existing team skills | 1 new skill | 2-3 new skills | Cross-functional | Specialized experts |

**How to Size:**
1. Score each dimension (PP/P/M/G/GG)
2. Take the **maximum score** across all dimensions
3. If 2+ dimensions are high (G/GG), escalate size by 1 level

**Example:**
- Technical: P (single service)
- Data: M (multi-table update)
- Dependencies: P (1 internal)
- Testing: M (E2E tests)
- **Result:** M (Medium) — highest score is M

---

## Impact Dimensions

### 1. Technical Impact

**Questions to Ask:**

- [ ] **How many services/applications affected?**
  - 1 service → PP/P
  - 2-3 services → M
  - 4+ services → G
  - System-wide → GG

- [ ] **Code complexity?**
  - Config change → PP
  - Single module → P
  - Multiple modules → M
  - Refactor required → G
  - Rewrite required → GG

- [ ] **Data model changes?**
  - No changes → PP
  - Read-only → P
  - Add fields (backward compatible) → P/M
  - Schema migration (breaking changes) → G
  - Database redesign → GG

- [ ] **API changes?**
  - No API changes → PP/P
  - New endpoint (backward compatible) → M
  - Breaking API changes → G
  - API versioning required → GG

- [ ] **Performance impact?**
  - No performance concern → PP/P
  - Minor optimization → M
  - Requires caching/indexing → G
  - Requires infrastructure scaling → GG

---

### 2. Organizational Impact

**Questions to Ask:**

- [ ] **How many teams involved?**
  - 1 team → PP/P/M
  - 2 teams → M/G
  - 3-4 teams → G
  - 5+ teams → GG

- [ ] **Cross-functional coordination?**
  - Single function (e.g., only Engineering) → PP/P/M
  - 2 functions (e.g., Eng + Product) → M/G
  - 3+ functions (e.g., Eng + Product + Sales + Legal) → G/GG

- [ ] **Skills gap?**
  - Team has all skills → PP/P/M
  - 1-2 new skills needed (can learn on the job) → M/G
  - Specialized skills (requires hiring/training) → G/GG

- [ ] **Change management?**
  - No user-facing changes → PP/P
  - Internal users (small training) → M
  - External users (communication plan required) → G
  - Large user base (phased rollout) → GG

- [ ] **Stakeholder alignment?**
  - Single stakeholder (Tech Lead) → PP/P
  - 2-3 stakeholders (Product Owner + Tech Lead) → M
  - 4+ stakeholders (requires steering committee) → G/GG

---

### 3. Operational Impact

**Questions to Ask:**

- [ ] **Deployment complexity?**
  - Standard CI/CD pipeline → PP/P
  - Blue-green deployment → M
  - Canary rollout → G
  - Multi-region phased rollout → GG

- [ ] **Downtime required?**
  - No downtime → PP/P
  - <1 hour maintenance window → M
  - >1 hour planned downtime → G
  - Multi-day migration → GG

- [ ] **Rollback plan?**
  - Instant (revert commit) → PP
  - <1 hour (database rollback) → P/M
  - 1-3 days (complex rollback) → G
  - Irreversible (migration only) → GG

- [ ] **Monitoring & alerting?**
  - Existing metrics sufficient → PP/P
  - New metrics required → M
  - New dashboards + alerts → G
  - Full observability redesign → GG

- [ ] **Security/compliance review?**
  - No review needed → PP/P
  - Standard security review → M
  - Full compliance audit (GDPR, SOC2) → G/GG

---

### 4. Architectural Impact

**Questions to Ask:**

- [ ] **Architectural pattern?**
  - Fits existing patterns → PP/P/M
  - Introduces new pattern (e.g., event-driven) → G
  - Requires architecture redesign → GG

- [ ] **Technical debt?**
  - No debt introduced → PP/P/M
  - Tactical solution (debt acceptable) → M/G
  - Strategic investment (removes debt) → G/GG

- [ ] **Scalability?**
  - Scales with existing infrastructure → PP/P/M
  - Requires horizontal scaling → G
  - Requires new infrastructure (e.g., Kafka, Redis) → GG

- [ ] **Integration complexity?**
  - Internal APIs only → PP/P/M
  - 1 external integration → M/G
  - Multiple external integrations → G/GG

- [ ] **Long-term maintainability?**
  - Easy to maintain (standard stack) → PP/P/M
  - Requires specialized knowledge → G
  - Tech stack migration (e.g., Java → Go) → GG

---

## Impact Analysis Template

### Initiative: [Initiative Name]

**Proposed by:** _______________  
**Date:** _______________  
**Stakeholders:** _______________  

---

### 1. Initiative Description

**Problem Statement:**
[What problem are we solving? Why now?]

**Proposed Solution:**
[High-level approach — what will we build/change?]

**Business Value:**
- [ ] Revenue impact: $ _______________ (increase/protect)
- [ ] Cost savings: $ _______________ (reduced manual work, infrastructure)
- [ ] Customer satisfaction: _______________ (CSAT improvement, NPS)
- [ ] Risk mitigation: _______________ (security, compliance, reliability)

---

### 2. Technical Impact Assessment

| Criteria | Score (PP/P/M/G/GG) | Rationale |
|----------|---------------------|-----------|
| **Services Affected** | ___ | [List services: Service A, Service B, etc.] |
| **Code Complexity** | ___ | [Single module? Refactor? Rewrite?] |
| **Data Model Changes** | ___ | [Schema migration? Breaking changes?] |
| **API Changes** | ___ | [New endpoints? Breaking changes?] |
| **Performance Impact** | ___ | [Caching? Scaling? Optimization?] |

**Technical Complexity:** ___ (highest score above)

**Key Technical Risks:**
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

### 3. Organizational Impact Assessment

| Criteria | Score (PP/P/M/G/GG) | Rationale |
|----------|---------------------|-----------|
| **Teams Involved** | ___ | [List teams: Engineering, Product, DevOps, etc.] |
| **Cross-Functional Coordination** | ___ | [How many functions?] |
| **Skills Gap** | ___ | [New skills needed? Training? Hiring?] |
| **Change Management** | ___ | [User impact? Communication plan?] |
| **Stakeholder Alignment** | ___ | [How many decision-makers?] |

**Organizational Complexity:** ___ (highest score above)

**Key Organizational Risks:**
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

### 4. Operational Impact Assessment

| Criteria | Score (PP/P/M/G/GG) | Rationale |
|----------|---------------------|-----------|
| **Deployment Complexity** | ___ | [CI/CD? Blue-green? Canary?] |
| **Downtime Required** | ___ | [Zero downtime? Maintenance window?] |
| **Rollback Plan** | ___ | [Instant? Hours? Days? Irreversible?] |
| **Monitoring & Alerting** | ___ | [Existing metrics? New dashboards?] |
| **Security/Compliance** | ___ | [Review required? Audit?] |

**Operational Complexity:** ___ (highest score above)

**Key Operational Risks:**
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

### 5. Architectural Impact Assessment

| Criteria | Score (PP/P/M/G/GG) | Rationale |
|----------|---------------------|-----------|
| **Architectural Pattern** | ___ | [Fits existing? New pattern?] |
| **Technical Debt** | ___ | [Introduces debt? Removes debt?] |
| **Scalability** | ___ | [Horizontal scaling? New infrastructure?] |
| **Integration Complexity** | ___ | [Internal? External? How many?] |
| **Long-Term Maintainability** | ___ | [Standard stack? Specialized?] |

**Architectural Complexity:** ___ (highest score above)

**Key Architectural Risks:**
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

### 6. Overall T-Shirt Size

**Dimension Scores:**

| Dimension | Score |
|-----------|-------|
| Technical | ___ |
| Organizational | ___ |
| Operational | ___ |
| Architectural | ___ |

**Overall T-Shirt Size:** ___ (maximum score across all dimensions)

**Escalation Rule Applied?**
- [ ] Yes — 2+ dimensions are G/GG, escalate by 1 level
- [ ] No — use maximum score as-is

**Final T-Shirt Size:** ___

---

### 7. Resource Estimate

**Effort:**

| Role | Estimated Days | Justification |
|------|----------------|---------------|
| Backend Engineer | ___ days | [Work involved] |
| Frontend Engineer | ___ days | [Work involved] |
| DevOps Engineer | ___ days | [Work involved] |
| QA Engineer | ___ days | [Work involved] |
| Product Manager | ___ days | [Work involved] |
| Designer | ___ days | [Work involved] |
| Data Engineer | ___ days | [Work involved] |
| **Total** | **___ days** | **___ person-months** |

**Timeline:**

- Estimated duration: ___ weeks/months
- Dependencies: _______________ (blocked by? blocks?)
- Milestones:
  1. _______________ (date: _______)
  2. _______________ (date: _______)
  3. _______________ (date: _______)

---

### 8. Risk Assessment

**Risk Level:** ___ (Low / Medium / High / Very High)

| Risk | Likelihood (1-5) | Impact (1-5) | Score | Mitigation |
|------|------------------|--------------|-------|------------|
| [Risk 1] | ___ | ___ | ___ | [How to mitigate?] |
| [Risk 2] | ___ | ___ | ___ | [How to mitigate?] |
| [Risk 3] | ___ | ___ | ___ | [How to mitigate?] |

**Risk Score Calculation:** Likelihood × Impact (1-25 scale)
- 1-5: Low risk
- 6-12: Medium risk
- 13-20: High risk
- 21-25: Very high risk

---

### 9. Dependencies & Blockers

**Internal Dependencies:**

| Dependency | Team | Status | ETA | Blocker? |
|------------|------|--------|-----|----------|
| [Dependency 1] | ___ | Not Started / In Progress / Done | _____ | Yes / No |
| [Dependency 2] | ___ | Not Started / In Progress / Done | _____ | Yes / No |

**External Dependencies:**

| Dependency | Vendor/Team | Status | ETA | Blocker? |
|------------|-------------|--------|-----|----------|
| [External API] | ___ | Not Started / In Progress / Done | _____ | Yes / No |
| [3rd Party Tool] | ___ | Not Started / In Progress / Done | _____ | Yes / No |

---

### 10. Go/No-Go Recommendation

**Recommendation:** ___ (Go / No-Go / Defer)

**Rationale:**

- **Business Value:** _______________ (High / Medium / Low)
- **Complexity:** _______________ (T-shirt size: PP/P/M/G/GG)
- **Risk:** _______________ (Low / Medium / High / Very High)
- **Resource Availability:** _______________ (Team has capacity? Need to hire?)
- **Strategic Alignment:** _______________ (Aligns with roadmap? Ad-hoc request?)

**Decision Matrix:**

| Business Value | Complexity | Risk | Recommendation |
|----------------|------------|------|----------------|
| High | PP/P/M | Low/Medium | **Go** — prioritize high |
| High | G/GG | Medium/High | **Go** — allocate resources, plan carefully |
| Medium | PP/P | Low | **Go** — quick win |
| Medium | M/G | Medium | **Go (conditional)** — if capacity available |
| Medium | GG | High | **Defer** — wait for more capacity |
| Low | PP/P | Low | **Defer** — backlog for future |
| Low | M/G/GG | Any | **No-Go** — not worth investment |

**Final Recommendation:** _______________

**Conditions (if conditional go):**
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

### 11. Approval & Sign-Off

**Reviewed by:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | _______________ | _______________ | _____ |
| Tech Lead | _______________ | _______________ | _____ |
| Architect | _______________ | _______________ | _____ |
| Engineering Manager | _______________ | _______________ | _____ |

**Approval Status:** ___ (Approved / Rejected / Needs Revision)

**Next Steps:**

- [ ] Add to roadmap (if approved)
- [ ] Create epic/feature in Jira/Linear
- [ ] Break down into stories
- [ ] Assign to squad
- [ ] Schedule kickoff meeting

---

## AI Agent: ImpactAnalyzer-Agent

### Purpose

Automate 60% of impact analysis work by:
- Analyzing codebase to identify affected services
- Calculating technical complexity scores
- Identifying dependencies (internal/external)
- Recommending t-shirt size based on historical data
- Flagging risks based on past incidents

---

### Agent Definition

```yaml
agent:
  identity:
    name: ImpactAnalyzer-Agent
    level: Intermediate (Analyst)
    role: Automate impact assessment for initiatives
  
  capabilities:
    - task: Identify affected services
      input: Initiative description (text)
      output: List of services likely affected (with confidence scores)
      method: |
        - Parse initiative description for keywords (e.g., "checkout", "payment", "authentication")
        - Search codebase for matching services/modules
        - Analyze service dependency graph (from architecture docs or code)
      performance: 85% accuracy (validated against human assessments)
    
    - task: Calculate technical complexity score
      input: Affected services, data model changes, API changes
      output: T-shirt size (PP/P/M/G/GG) with rationale
      method: |
        - Count # services affected
        - Analyze code churn (lines changed in similar past initiatives)
        - Check for data migrations (schema changes)
        - Check for API version bumps
      performance: ±1 size accuracy (90% of cases)
    
    - task: Identify dependencies
      input: Affected services
      output: List of internal dependencies, external integrations
      method: |
        - Parse service dependency graph
        - Check import statements in code
        - Scan API contracts for external dependencies
      performance: 95% recall (finds 95% of dependencies)
    
    - task: Recommend t-shirt size
      input: Initiative description + affected services + dependencies
      output: Recommended t-shirt size (PP/P/M/G/GG) + confidence score
      method: |
        - Score each dimension (Technical, Org, Ops, Arch)
        - Apply sizing rules (max score + escalation rule)
        - Compare to historical initiatives (similarity matching)
      performance: 80% match with human assessments
    
    - task: Flag risks
      input: Initiative description + affected services
      output: List of risks (with likelihood + impact scores)
      method: |
        - Check incident history (past outages, bugs in affected services)
        - Identify high-churn areas (frequently changed code = higher risk)
        - Flag external dependencies (vendor downtime history)
      performance: 70% of flagged risks materialize (precision)
  
  human_oversight:
    autonomy_level: Assisted (AI recommends, human reviews)
    review_required: Product Owner + Tech Lead review all recommendations
    escalation: If AI confidence <70%, escalate to Architect for manual assessment
  
  tools:
    - Codebase search (GitHub API, GitLab API)
    - Dependency graph analysis (Dependabot, npm/pip dependency trees)
    - Service mesh metadata (Istio, Linkerd service maps)
    - Incident history (PagerDuty API, Jira bug history)
    - ChatGPT/Claude API (natural language processing of initiative descriptions)
  
  metrics:
    - accuracy: 80% (t-shirt size matches human assessment)
    - time_savings: 60% (3 hours → 1.2 hours per assessment)
    - coverage: 95% (finds 95% of dependencies, 85% of affected services)
  
  cost:
    monthly: $500 (API costs + compute)
    human_equivalent: $3,000/month (Product Manager time on impact assessments)
    roi: 6x cost savings
```

---

### How to Use ImpactAnalyzer-Agent

**Step 1: Provide Initiative Description**

```
Input to AI Agent:
"We need to add OAuth 2.0 authentication to our API gateway. 
Currently using basic auth. Will affect 15 downstream services 
that call the gateway. Need to migrate existing API keys to OAuth tokens."
```

---

**Step 2: AI Analyzes & Recommends**

```
Output from ImpactAnalyzer-Agent:

📊 IMPACT ANALYSIS: OAuth 2.0 Migration

🔍 Affected Services (Confidence: 85%)
1. api-gateway (Primary)
2. auth-service (New OAuth provider)
3. user-service (Token storage)
4. 15 downstream services (API callers):
   - checkout-service
   - payment-service
   - inventory-service
   - ... (12 more)

📐 Technical Complexity: G (Large)
- Services affected: 17 (15+ = Large)
- Data migration: OAuth tokens + API key deprecation (Medium-High)
- API changes: Breaking (auth headers change from Basic to Bearer)
- Rollback complexity: 1-3 days (requires dual-auth support during migration)

👥 Organizational Complexity: G (Large)
- Teams involved: 4 (Gateway team, Auth team, Platform team, 3 product teams)
- Skills gap: OAuth 2.0 implementation (1 new skill, can learn)
- Change management: High (all API consumers must update clients)

⚙️ Operational Complexity: G (Large)
- Deployment: Phased rollout required (dual-auth support for 2 weeks)
- Downtime: Zero (backward compatible during transition)
- Rollback: Medium (3 days to revert if issues)
- Monitoring: New OAuth metrics required (token issuance rate, expiry, refresh)

🏗️ Architectural Complexity: G (Large)
- Pattern: Introduces OAuth 2.0 (new auth pattern)
- Technical debt: Removes basic auth (strategic investment)
- Scalability: Requires Redis for token caching
- Integration: External OAuth provider (e.g., Auth0, Okta) OR build in-house

📏 RECOMMENDED T-SHIRT SIZE: G (Large)
- All 4 dimensions scored G
- Escalation rule: Not applied (no GG scores)
- Confidence: 85%

⚠️ KEY RISKS (Flagged by AI):
1. Breaking API changes → downstream services must update (Likelihood: 5, Impact: 4, Score: 20 — HIGH)
   - Mitigation: Dual-auth support for 2 weeks, phased migration
2. Auth0 vendor dependency → outage if provider down (Likelihood: 2, Impact: 5, Score: 10 — MEDIUM)
   - Mitigation: Failover to basic auth, SLA guarantees
3. Token expiry edge cases → users logged out unexpectedly (Likelihood: 3, Impact: 3, Score: 9 — MEDIUM)
   - Mitigation: Refresh token flow, graceful expiry handling

🔗 DEPENDENCIES:
Internal:
- auth-service (must implement OAuth provider)
- user-service (token storage schema)
External:
- Auth0/Okta (if using external provider)

⏱️ ESTIMATED EFFORT: 65 days (3 person-months)
- Backend: 30 days (OAuth implementation, token management)
- DevOps: 15 days (Redis setup, monitoring, deployment)
- API consumers: 20 days (update 15 services to use OAuth)

📅 TIMELINE: 2.5-3 months

💡 RECOMMENDATION: Go (with conditions)
- Business value: High (security improvement, modern auth standard)
- Complexity: G (Large, but manageable)
- Risk: High (breaking changes, vendor dependency)
- Conditions:
  1. Dual-auth support for 2-week migration period
  2. Phased rollout (5 services/week)
  3. Dedicated DevOps support for monitoring
```

---

**Step 3: Human Review & Finalize**

Product Owner + Tech Lead review AI recommendations:

- **Agree with t-shirt size?** Yes/No → If no, adjust manually
- **Agree with risks?** Yes/No → Add missed risks, refine mitigations
- **Agree with recommendation?** Yes/No → Final go/no-go decision

**Save finalized assessment** (Jira, Confluence, or PDF)

---

## Example Assessments

### Example 1: PP (Extra Small) — Change Log Level

**Initiative:** Increase log level for payment service from INFO to DEBUG

**Impact:**
- **Technical:** PP (config change, no code)
- **Organizational:** PP (1 person, 1 team)
- **Operational:** PP (deploy via CI/CD, no downtime, instant rollback)
- **Architectural:** PP (no architecture change)

**T-Shirt Size:** PP  
**Effort:** 1 hour  
**Risk:** Low  
**Recommendation:** Go

---

### Example 2: P (Small) — Add CSV Export Button

**Initiative:** Add "Export to CSV" button on analytics dashboard

**Impact:**
- **Technical:** P (single service, new API endpoint, no data migration)
- **Organizational:** P (1 team, frontend + backend)
- **Operational:** P (standard deployment, no downtime)
- **Architectural:** P (fits existing pattern)

**T-Shirt Size:** P  
**Effort:** 5 days  
**Risk:** Low  
**Recommendation:** Go

---

### Example 3: M (Medium) — Implement Notification Preferences

**Initiative:** Allow users to configure email/SMS/push notification preferences

**Impact:**
- **Technical:** M (2 services: user-service + notification-service, database migration for preferences table)
- **Organizational:** M (2 teams, frontend + backend)
- **Operational:** M (E2E tests required, new monitoring for notification delivery)
- **Architectural:** M (fits existing event-driven pattern)

**T-Shirt Size:** M  
**Effort:** 20 days  
**Risk:** Medium (notification delivery edge cases)  
**Recommendation:** Go

---

### Example 4: G (Large) — Migrate from MySQL to PostgreSQL

**Initiative:** Migrate database from MySQL to PostgreSQL for better JSON support

**Impact:**
- **Technical:** G (all services affected, schema migration, SQL syntax differences)
- **Organizational:** G (3 teams: Engineering, DevOps, QA)
- **Operational:** G (requires downtime OR complex dual-write strategy, rollback = 3 days)
- **Architectural:** G (strategic investment, removes MySQL-specific workarounds)

**T-Shirt Size:** G  
**Effort:** 60 days  
**Risk:** High (data loss, downtime, SQL compatibility issues)  
**Recommendation:** Go (with conditions: dedicated DBA, phased migration, extensive testing)

---

### Example 5: GG (Extra Large) — Microservices Migration

**Initiative:** Migrate monolithic Ruby on Rails app to microservices (Node.js)

**Impact:**
- **Technical:** GG (rewrite entire application, service boundaries, API contracts)
- **Organizational:** GG (5+ teams, new skills required: Node.js, Docker, Kubernetes)
- **Operational:** GG (new deployment pipeline, service mesh, multi-region rollout)
- **Architectural:** GG (architecture redesign, event-driven patterns, distributed tracing)

**T-Shirt Size:** GG  
**Effort:** 18 months (50 person-months)  
**Risk:** Very High (business continuity, team learning curve, tech stack migration)  
**Recommendation:** Go (with conditions: executive sponsorship, dedicated team, 6-month pilot)

---

## Prioritization Framework

### Value vs. Complexity Matrix

```
High Value │ P2 │ P1 │
           │ Go │ Go │
           │────┼────│
Medium Val │ P3 │ P2 │
           │ Go │ Go │
           │────┼────│
Low Value  │ P4 │ P3 │
           │Defer│Defer│
           └────┴────┘
             PP/P/M   G/GG
             (Low)   (High)
            Complexity
```

**Priority Levels:**

- **P1 (Highest):** High value + Low complexity → Quick wins, prioritize immediately
- **P2:** High value + High complexity OR Medium value + Low complexity → Plan carefully, allocate resources
- **P3:** Medium value + High complexity OR Low value + Low complexity → Defer until capacity available
- **P4 (Lowest):** Low value + Any complexity → Backlog or reject

---

### RICE Scoring (Alternative)

**RICE = (Reach × Impact × Confidence) / Effort**

| Factor | Definition | Scale |
|--------|------------|-------|
| **Reach** | # users/customers affected per quarter | 100, 1000, 10000+ |
| **Impact** | How much does it improve their experience? | 0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive) |
| **Confidence** | How sure are we of Reach/Impact estimates? | 50% (low), 80% (medium), 100% (high) |
| **Effort** | T-shirt size converted to person-months | PP=0.1, P=0.5, M=2, G=4, GG=12 |

**Example:**

- Reach: 10,000 users/quarter
- Impact: 2 (high — significantly improves workflow)
- Confidence: 80%
- Effort: M (2 person-months)

**RICE Score:** (10,000 × 2 × 0.8) / 2 = **8,000**

**Prioritize initiatives by RICE score** (higher = higher priority)

---

## Implementation Guide

### Step 1: Adopt Impact Analysis Template (Week 1)

- [ ] Download template (use above markdown template)
- [ ] Add to Confluence/Notion/Google Docs
- [ ] Train Product Owners + Tech Leads on how to fill out
- [ ] Run 3 pilot assessments (mix of PP, M, G sizes)

---

### Step 2: Deploy ImpactAnalyzer-Agent (Week 2-3)

- [ ] Set up AI agent (ChatGPT API or Claude API)
- [ ] Connect to codebase (GitHub API, dependency graph tools)
- [ ] Train on historical initiatives (past 20-50 assessments)
- [ ] Test accuracy (compare AI vs. human assessments)
- [ ] Launch with human-in-the-loop (AI recommends, human reviews)

---

### Step 3: Establish Governance Process (Week 4)

- [ ] Define approval workflow:
  - PP/P: Tech Lead approves
  - M: Product Owner + Tech Lead approve
  - G/GG: Architecture review + Executive approval
- [ ] Set up monthly impact review meeting (review all G/GG initiatives)
- [ ] Track metrics:
  - # initiatives assessed per month
  - Accuracy of t-shirt sizing (actual effort vs. estimate)
  - % initiatives that go over budget/timeline
  - % initiatives that deliver expected business value

---

### Step 4: Iterate & Improve (Ongoing)

- [ ] Quarterly retrospective: What's working? What's not?
- [ ] Refine sizing criteria (based on actuals vs. estimates)
- [ ] Update AI agent training data (new assessments)
- [ ] Adjust prioritization framework (RICE scores, value matrix)

---

## Common Pitfalls

### Pitfall #1: Under-Sizing Complexity

**Problem:** Teams consistently under-estimate (G initiatives sized as M)

**Solution:**
- Escalation rule: If 2+ dimensions are G/GG, escalate by 1 level
- Historical calibration: Compare actuals to estimates quarterly
- AI agent learns from past under-estimates

---

### Pitfall #2: Analysis Paralysis

**Problem:** Teams spend 2 weeks analyzing instead of building

**Solution:**
- Time-box assessments: PP/P (30 min), M (1 hour), G (2 hours), GG (4 hours)
- Use ImpactAnalyzer-Agent to automate 60% of work
- Accept uncertainty: Confidence scores <80% are OK for M/G initiatives

---

### Pitfall #3: Ignoring Organizational Impact

**Problem:** Technical assessment looks easy (PP), but requires 4 teams to coordinate (actually M/G)

**Solution:**
- Score **all 4 dimensions** (Technical, Organizational, Operational, Architectural)
- Take **maximum score** across dimensions (not average)
- Flag cross-team dependencies early

---

### Pitfall #4: No Follow-Up

**Problem:** Assessments done, but actuals never compared to estimates

**Solution:**
- Post-mortem after G/GG initiatives: Was sizing accurate?
- Track estimation accuracy metric: Actual effort / Estimated effort (target: 0.8-1.2x)
- Refine sizing criteria based on learnings

---

## Resources

**Framework Documentation:**
- [AI Agents](../../DOCS/05-ai-agents.md) — ImpactAnalyzer-Agent definition
- [Governance & Ethics](../../DOCS/06-governance-ethics.md) — Approval workflows
- [Human-AI Collaboration](../../DOCS/08-human-ai-collaboration.md) — AI recommends, humans decide

**Templates:**
- [Impact Analysis Template](../../ADOPTION/TEMPLATES/impact-analysis-template.md) — Fillable template
- [RFC Template](../../ADOPTION/TEMPLATES/rfc-template.md) — For G/GG initiatives requiring architecture review

**Checklists:**
- [AI Agent Integration](../../ADOPTION/CHECKLISTS/ai-agent-integration.md) — Deploy ImpactAnalyzer-Agent

**Playbooks:**
- [AI-Native Agile](../../DOCS/11-ai-native-agile.md) — Epic → Feature → Story breakdown
- [AI-Native Kanban](../../DOCS/12-ai-native-kanban.md) — Sizing for continuous flow teams

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
