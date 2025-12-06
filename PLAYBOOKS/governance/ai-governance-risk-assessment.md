# AI Governance: Risk Assessment and Automated Oversight

**Operationalizing governance with risk scoring, tiered reviews, and intelligent alerts**

---

## Overview

Effective AI governance balances **innovation velocity** with **safety and compliance**. This playbook provides:

1. **Risk Scoring Framework** - Calculate risk level for every AI agent/automation
2. **Tiered Review Process** - Light vs. Heavy review based on risk
3. **Automated Alerts** - Proactive notifications when risks emerge
4. **Ethical Risk Assessment** - Structured evaluation for AI decisions
5. **Governance Workflows** - Who reviews what, when, and how

**Key Principle:** High-risk AI gets heavy oversight, low-risk AI moves fast with light monitoring.

---

## Part 1: Risk Scoring Framework

### Risk Calculation Formula

**Total Risk Score = Impact × Likelihood × Autonomy**

Where:
- **Impact** (1-5): Severity if AI makes a mistake
- **Likelihood** (1-5): Probability of error/failure
- **Autonomy** (1-5): Level of human oversight

**Risk Score Ranges:**
- **1-25**: 🟢 Low Risk (Light Review)
- **26-75**: 🟡 Medium Risk (Standard Review)
- **76-125**: 🔴 High Risk (Heavy Review + Ongoing Monitoring)

---

### Dimension 1: Impact (Severity of Failure)

**Score 1 - Negligible:**
- Mistake affects 1-5 users
- No financial loss
- Easily reversible
- No compliance/legal risk
- **Example:** Chatbot gives wrong FAQ answer → User finds correct answer elsewhere

**Score 2 - Minor:**
- Affects 6-50 users
- Financial loss <$1K
- Reversible within 24 hours
- Minimal compliance risk
- **Example:** Lead scoring error → Sales rep wastes 1 hour on bad lead

**Score 3 - Moderate:**
- Affects 51-500 users
- Financial loss $1K-$50K
- Reversible within 1 week
- Moderate compliance risk (reportable but not severe)
- **Example:** Invoice processing error → 10 vendors not paid on time → Late fees

**Score 4 - Significant:**
- Affects 501-10,000 users
- Financial loss $50K-$500K
- Reversible but requires significant effort
- High compliance risk (regulatory scrutiny)
- **Example:** Churn predictor fails → 20 customers churn (no proactive outreach)

**Score 5 - Critical:**
- Affects >10,000 users or entire business
- Financial loss >$500K or existential threat
- Irreversible or extremely difficult to fix
- Severe compliance risk (fines, lawsuits, reputational damage)
- **Examples:** 
  - Biased hiring AI → Discrimination lawsuit
  - Autonomous trading AI → $1M loss in bad trades
  - Medical diagnosis AI → Patient harm

---

### Dimension 2: Likelihood (Probability of Error)

**Score 1 - Very Low (<5% error rate):**
- Well-tested technology (mature, proven)
- Simple, deterministic logic
- High-quality training data
- Extensive validation performed
- **Example:** Invoice data extraction from PDFs (98% accuracy)

**Score 2 - Low (5-10% error rate):**
- Proven technology, some edge cases
- Moderate complexity
- Good training data
- Standard validation
- **Example:** Lead scoring (90% accuracy in testing)

**Score 3 - Moderate (10-20% error rate):**
- New technology or novel application
- Complex logic, multiple variables
- Training data has some gaps
- Limited validation
- **Example:** Churn prediction (15% false positive rate)

**Score 4 - High (20-40% error rate):**
- Experimental technology
- High complexity, many unknowns
- Training data limited or biased
- Minimal validation
- **Example:** New AI model predicting customer lifetime value (30% error)

**Score 5 - Very High (>40% error rate):**
- Unproven technology (research-stage)
- Extremely complex or unpredictable
- Poor or no training data
- No validation
- **Example:** AGI-style reasoning (highly unreliable)

---

### Dimension 3: Autonomy (Level of Human Oversight)

**Score 1 - Fully Supervised:**
- Human reviews **every** AI decision before action
- AI provides suggestions only
- Human has final say on 100% of cases
- **Example:** Contract review AI → Lawyer reads every contract, AI highlights risks

**Score 2 - Co-pilot:**
- Human reviews **critical** decisions
- AI acts on routine cases (<$5K, low-risk)
- Human approves exceptions (>$5K, high-risk)
- **Example:** Expense approval AI → Auto-approve <$500, escalate >$500 to manager

**Score 3 - Semi-Autonomous:**
- Human reviews **samples** (10-20%)
- AI acts independently on most cases
- Human spot-checks for quality
- **Example:** Invoice processing → CFO reviews 10% random sample weekly

**Score 4 - Autonomous:**
- Human reviews **outcomes** only (not individual decisions)
- AI acts independently, human monitors metrics
- Human intervenes only if metrics degrade
- **Example:** Chatbot → Human reviews monthly satisfaction score, not every conversation

**Score 5 - Fully Autonomous:**
- Human reviews **rarely** (quarterly or less)
- AI operates with minimal oversight
- Human only involved in catastrophic failure
- **Example:** High-frequency trading AI (makes 10,000 trades/day, human reviews quarterly P&L)

---

### Risk Score Calculation Examples

#### Example 1: **FAQ Chatbot**

```
Agent: ChatbotSupport-Agent
Purpose: Answer customer FAQs (tier 1 support)

Impact: 2 (Minor - wrong answer frustrates 1 customer, easily corrected)
Likelihood: 2 (Low - 92% accuracy in testing)
Autonomy: 4 (Autonomous - escalates complex questions, human reviews monthly)

Risk Score = 2 × 2 × 4 = 16 (🟢 Low Risk - Light Review)
```

**Governance Decision:**
- ✅ Light review (monthly metrics check)
- ✅ Fast deployment (minimal approval process)
- ✅ Standard monitoring (track satisfaction, escalation rate)

---

#### Example 2: **Churn Predictor**

```
Agent: ChurnPredictor-Agent
Purpose: Identify at-risk customers, suggest retention actions

Impact: 4 (Significant - missed churn = $50K-500K ARR loss)
Likelihood: 3 (Moderate - 15% false positive rate)
Autonomy: 2 (Co-pilot - CSM reviews daily, decides whether to reach out)

Risk Score = 4 × 3 × 2 = 24 (🟢 Low Risk - Light Review)
```

**Governance Decision:**
- ✅ Light review (weekly CSM feedback on accuracy)
- ✅ Standard monitoring (track churn prediction accuracy, false positive rate)
- ⚠️ If accuracy drops <70% → Escalate to Medium Risk (pause, retrain)

---

#### Example 3: **Credit Approval AI**

```
Agent: CreditApprover-Agent
Purpose: Auto-approve/deny small business loans (<$50K)

Impact: 4 (Significant - denial affects livelihoods, approval risk = bad debt)
Likelihood: 3 (Moderate - 18% error rate in validation)
Autonomy: 3 (Semi-autonomous - human reviews 20% random sample)

Risk Score = 4 × 3 × 3 = 36 (🟡 Medium Risk - Standard Review)
```

**Governance Decision:**
- ⚠️ Standard review (quarterly audit by Compliance team)
- ⚠️ Bias testing (quarterly demographic fairness analysis)
- ⚠️ Enhanced monitoring (track approval rate by demographics, flag disparate impact)

---

#### Example 4: **Hiring Resume Screener**

```
Agent: ResumeScreener-Agent
Purpose: Score resumes, recommend top 20 candidates for interview

Impact: 5 (Critical - biased hiring = discrimination lawsuit, reputational damage)
Likelihood: 3 (Moderate - 20% false negative rate - miss good candidates)
Autonomy: 2 (Co-pilot - recruiter reviews all "rejected" candidates before final decision)

Risk Score = 5 × 3 × 2 = 30 (🟡 Medium Risk - Standard Review)
```

**Governance Decision:**
- ⚠️ **Standard review + Enhanced ethical oversight**
- ⚠️ Bias audit **monthly** (not quarterly)
- ⚠️ Legal team reviews model every 6 months
- ⚠️ Human reviews 100% of "rejected" candidates (AI doesn't auto-reject)

**Note:** Even though score = 30 (just above Low threshold), **hiring is sensitive** → Treat as Medium+ risk

---

#### Example 5: **Autonomous Trading AI**

```
Agent: TradingBot-Agent
Purpose: Execute stock trades based on market signals

Impact: 5 (Critical - bad trades = $1M+ loss)
Likelihood: 4 (High - market unpredictable, 30% of trades lose money)
Autonomy: 4 (Autonomous - makes 100+ trades/day, human reviews weekly P&L)

Risk Score = 5 × 4 × 4 = 80 (🔴 High Risk - Heavy Review + Continuous Monitoring)
```

**Governance Decision:**
- 🚨 **Heavy review required**
- 🚨 Real-time monitoring (alert if single-day loss >$10K)
- 🚨 Daily review by CFO (P&L, positions, risk exposure)
- 🚨 Weekly review by Governance Circle (strategy, model performance)
- 🚨 Hard limits: Max $50K/day trading volume, no short-selling, auto-pause if loss >$25K

---

## Part 2: Tiered Review Process

### Review Tier 1: 🟢 Light Review (Risk Score 1-25)

**Frequency:** Monthly or quarterly  
**Reviewer:** Squad lead or delegate  
**Time Investment:** 15-30 minutes/month

**Review Checklist:**

- [ ] **Performance Metrics Review**
  - Accuracy: Is it maintaining >80% target?
  - Error rate: Has it increased >5% from baseline?
  - User satisfaction: Any complaints?

- [ ] **Volume Check**
  - Processing volume: Normal range or anomaly?
  - Escalation rate: Increasing (sign of declining performance)?

- [ ] **Incident Log**
  - Any errors/failures logged?
  - Root cause identified and fixed?

**Action if Issue Detected:**
- Minor issue → Squad lead fixes, documents
- Major issue (accuracy drop >10%) → Escalate to Medium Risk tier

**Example Agents:**
- FAQ chatbot
- Invoice data extraction
- Standup summary generation

---

### Review Tier 2: 🟡 Standard Review (Risk Score 26-75)

**Frequency:** Monthly  
**Reviewer:** Squad lead + Governance delegate  
**Time Investment:** 1-2 hours/month

**Review Checklist:**

- [ ] **Performance Deep Dive**
  - Accuracy trend (last 3 months)
  - False positive/negative rate
  - Edge case handling (review 5 recent exceptions)

- [ ] **Bias & Fairness Check**
  - Demographic analysis (if applicable)
  - Disparate impact testing
  - Complaints or ethical concerns logged?

- [ ] **Data Quality Validation**
  - Training data freshness (when last updated?)
  - Data drift detected (input distribution changing?)
  - Schema changes that could affect model?

- [ ] **Audit Trail Verification**
  - Are all decisions logged?
  - Can we explain any decision from last month?
  - Retention policy followed (old logs purged)?

- [ ] **Human Oversight Effectiveness**
  - Are humans overriding AI frequently (>20%)?
  - Why? (AI wrong, or humans not trusting AI?)
  - Feedback loop working (overrides → model improvement)?

**Action if Issue Detected:**
- Accuracy drop >15% → Pause agent, retrain, re-validate
- Bias detected → Immediate investigation, Legal team notified
- Data quality issue → Fix data pipeline before resuming
- High override rate → Re-calibrate model or increase autonomy if AI is correct

**Example Agents:**
- Churn predictor
- Lead scoring
- Expense approval
- Contract risk analysis

---

### Review Tier 3: 🔴 Heavy Review (Risk Score 76-125)

**Frequency:** Weekly (some daily)  
**Reviewer:** Governance Circle (multi-disciplinary team)  
**Time Investment:** 2-4 hours/week

**Review Checklist:**

- [ ] **Real-Time Monitoring Dashboard**
  - Key metrics updated hourly/daily
  - Alerts configured for anomalies
  - Human on-call rotation (24/7 if critical)

- [ ] **Sample Decision Review**
  - Manually review 10-20 recent AI decisions
  - Validate correctness, fairness, reasoning
  - Check for pattern of errors

- [ ] **Ethical Compliance Audit**
  - Bias testing (demographic parity, equal opportunity)
  - Explainability verification (can we explain decisions?)
  - Privacy compliance (PII handled correctly?)

- [ ] **Safety Guardrails Check**
  - Are prohibited actions being respected?
  - Have boundary conditions triggered correctly?
  - Any attempts to bypass guardrails (adversarial inputs)?

- [ ] **Incident Response Readiness**
  - Is runbook up-to-date (how to handle AI failure)?
  - Have we tested fail-safe mechanisms?
  - Communication plan ready (who to notify if catastrophic failure)?

- [ ] **Model Drift Analysis**
  - Performance degrading over time?
  - Concept drift (world changing, model outdated)?
  - Retraining schedule appropriate?

- [ ] **Stakeholder Feedback**
  - What are users saying (support tickets, surveys)?
  - Any regulatory inquiries or complaints?
  - Media coverage (is AI controversial)?

**Action if Issue Detected:**
- Critical safety violation → **Immediate shutdown**, investigate
- Bias detected → Pause, Legal review, remediation plan
- Performance degradation → Reduce autonomy, increase human oversight
- Regulatory concern → Compliance team leads response

**Example Agents:**
- Hiring/resume screening
- Credit approval
- Medical diagnosis support
- Autonomous trading
- Content moderation (hate speech, illegal content)

---

## Part 3: Automated Alert System

### Alert Framework

**Philosophy:** Proactive alerts prevent issues before they become crises

**Alert Levels:**
- 🟢 **Info**: FYI, no action required (e.g., "Monthly metrics report ready")
- 🟡 **Warning**: Investigate within 24-48 hours (e.g., "Accuracy dropped 5%")
- 🔴 **Critical**: Immediate action required (e.g., "Agent made prohibited action")
- 🚨 **Emergency**: All-hands response (e.g., "Bias detected in production")

---

### Alert Categories

#### Category 1: Performance Degradation

**Trigger Conditions:**

```yaml
alert:
  name: "Agent Performance Degradation"
  level: warning
  conditions:
    - accuracy < 80% (for 2 consecutive days)
    - error_rate > 15% (increase >5% from baseline)
    - processing_latency > 10 seconds (p95)
  
  notification:
    channels: [Slack #ai-governance, Email to squad lead]
    frequency: once_per_day (don't spam)
  
  action:
    required_within: 48 hours
    owner: Squad lead
    steps:
      - Investigate root cause (data quality? Model drift?)
      - If fixable → Apply fix, monitor for 7 days
      - If not fixable → Escalate to Governance Circle
```

**Example Alert Message:**
```
🟡 PERFORMANCE WARNING: ChurnPredictor-Agent

Accuracy: 72% (target: >80%)
Duration: 3 days
Baseline: 87% (2 weeks ago)

Possible Causes:
- Data quality issue (usage events pipeline delayed?)
- Seasonal pattern (end-of-quarter customer behavior different?)
- Model drift (customer base changing?)

Action Required:
- Squad lead: Investigate within 48 hours
- Review: Last 50 predictions vs. actual churn outcomes
- Report findings: #ai-governance channel
```

---

#### Category 2: Ethical Risk (Bias, Fairness)

**Trigger Conditions:**

```yaml
alert:
  name: "Bias Detected"
  level: emergency
  conditions:
    - disparate_impact_ratio > 1.2 (e.g., approve 80% male, 65% female)
    - demographic_parity_difference > 0.1
    - equal_opportunity_difference > 0.15
  
  notification:
    channels: [Slack #ai-governance, Email to Legal, Page on-call]
    frequency: immediate
  
  action:
    required_within: 4 hours
    owner: Governance Circle + Legal
    steps:
      - PAUSE agent immediately (stop making decisions)
      - Convene emergency review (within 4 hours)
      - Analyze: Historical decisions for bias pattern
      - Remediate: Retrain model, adjust weights, or retire agent
      - Communicate: Notify affected users if harm occurred
```

**Example Alert Message:**
```
🚨 EMERGENCY: Bias Detected - ResumeScreener-Agent

Disparate Impact Ratio: 1.35 (legal threshold: 1.2)
  - Male candidates: 78% recommended for interview
  - Female candidates: 58% recommended for interview

Status: AGENT PAUSED (no new decisions being made)

Immediate Actions:
1. Legal team: Assess liability exposure
2. Governance Circle: Emergency meeting in 2 hours
3. Data Science: Analyze last 500 decisions for bias pattern
4. HR: Review recent hires (any bias in actual hiring outcomes?)

Next Steps:
- Retrain model with balanced dataset
- Add bias mitigation (re-weight protected attributes)
- Test thoroughly before re-enabling
- Consider: Contact candidates previously rejected (offer re-review)
```

---

#### Category 3: Safety Violation (Guardrail Breach)

**Trigger Conditions:**

```yaml
alert:
  name: "Guardrail Violation"
  level: critical
  conditions:
    - prohibited_action_attempted (e.g., agent tried to send email without human review)
    - boundary_condition_exceeded (e.g., trading loss >$10K in single day)
    - confidence_threshold_violated (e.g., acted on prediction with <70% confidence)
  
  notification:
    channels: [Slack #ai-governance, Page on-call, Email to CTO]
    frequency: immediate (every occurrence)
  
  action:
    required_within: 1 hour
    owner: On-call engineer + Governance delegate
    steps:
      - Assess damage (did prohibited action complete? What's the impact?)
      - Rollback if possible (reverse transaction, recall email, etc.)
      - Root cause analysis (bug? Adversarial input? Model confusion?)
      - Fix and test (patch code, strengthen guardrails)
```

**Example Alert Message:**
```
🔴 CRITICAL: Guardrail Violation - InvoiceProcessor-Agent

Violation: Auto-approved invoice >$10K (limit: $5K)
  Invoice: INV-9876
  Amount: $12,500
  Vendor: "Acme Consulting"
  Timestamp: 2025-11-04 14:32:15 UTC

Status: Payment HELD (not yet sent to bank)

Immediate Actions:
1. Finance: Manual review of INV-9876 (legitimate vendor?)
2. Engineering: Why did agent bypass $5K limit? (code bug?)
3. If legitimate: Approve manually
4. If fraud: Reject, add vendor to blacklist
5. Fix guardrail: Add hard database constraint (payment >$5K = auto-reject)

Root Cause Investigation:
- Agent logs show: confidence = 98% (very certain)
- But guardrail logic had bug (checked amount < 5000, should be <=)
- Fix: Update guardrail logic, add unit test
```

---

#### Category 4: Data Quality Issues

**Trigger Conditions:**

```yaml
alert:
  name: "Data Quality Degradation"
  level: warning
  conditions:
    - null_rate > 15% (required field missing in >15% of records)
    - schema_change_detected (upstream system changed data format)
    - data_freshness > 24_hours (real-time pipeline delayed)
    - volume_anomaly (50% drop in incoming data)
  
  notification:
    channels: [Slack #data-engineering, Email to Data team]
    frequency: once_per_hour (don't spam)
  
  action:
    required_within: 12 hours
    owner: Data Engineering team
    steps:
      - Investigate data pipeline (which stage failed?)
      - Fix root cause (API down? Schema mismatch?)
      - Backfill missing data if possible
      - Notify AI agent owners (may need to retrain if data distribution changed)
```

**Example Alert Message:**
```
🟡 DATA QUALITY WARNING: customer_usage_events

Issue: Volume drop detected
Current: 150 events/hour (avg: 600 events/hour)
Duration: Last 6 hours
Impact: ChurnPredictor-Agent may have stale data

Possible Causes:
- Segment pipeline down (check Segment status page)
- Product analytics SDK issue (check app logs)
- Database write lock (check DB performance metrics)

Action Required:
- Data Engineering: Investigate within 12 hours
- If critical: Manually backfill missing 6 hours of data
- Notify: AI team that churn predictions may be inaccurate today
```

---

#### Category 5: Compliance & Audit Triggers

**Trigger Conditions:**

```yaml
alert:
  name: "Compliance Event"
  level: info (or warning if regulatory deadline)
  conditions:
    - audit_log_retention_expiring (logs older than 6.5 years, need to purge by 7 years)
    - data_subject_access_request (GDPR: user requested "download my data")
    - data_deletion_request (GDPR: user requested "delete my data")
    - model_retrain_overdue (quarterly retraining missed deadline)
  
  notification:
    channels: [Email to Compliance team, Slack #legal]
    frequency: once (don't repeat)
  
  action:
    required_within: 30 days (GDPR) or per schedule
    owner: Compliance team + relevant squad
    steps:
      - Log request in compliance tracker
      - Execute required action (export data, delete data, retrain model)
      - Verify completion
      - Respond to user (if GDPR request)
```

**Example Alert Message:**
```
🟢 INFO: Data Subject Access Request (GDPR)

User: john.doe@example.com
Request: "Download all my data"
Received: 2025-11-04
Deadline: 2025-12-04 (30 days)

Action Required:
- Compliance team: Log request in GDPR tracker
- Data team: Export data from all systems (CRM, product DB, warehouse)
- Format: JSON (machine-readable per GDPR Article 20)
- Review: Legal team ensures no third-party data included
- Send: Secure link to user (expires in 7 days)

Systems to Export:
✅ Salesforce (customer profile)
✅ Product DB (usage events)
✅ Zendesk (support tickets)
✅ Stripe (billing history)
✅ Data warehouse (aggregated analytics)
```

---

### Alert Configuration Example

**Implementation (using monitoring tool like Datadog, PagerDuty, or custom):**

```python
# Example: Bias detection alert
from monitoring import Alert, Metric, Threshold

bias_alert = Alert(
    name="ResumeScreener-Bias-Alert",
    metric=Metric(
        name="approval_rate_by_gender",
        query="""
        SELECT 
            gender,
            COUNT(*) as total,
            SUM(CASE WHEN recommended = true THEN 1 ELSE 0 END) as approved,
            (SUM(CASE WHEN recommended = true THEN 1 ELSE 0 END) * 1.0 / COUNT(*)) as approval_rate
        FROM resume_screening_decisions
        WHERE timestamp > NOW() - INTERVAL '7 days'
        GROUP BY gender
        """
    ),
    condition=Threshold(
        type="disparate_impact",
        threshold=1.2,  # Approval rate ratio must be < 1.2
        window="7 days"
    ),
    severity="emergency",
    notification={
        "slack": "#ai-governance",
        "email": ["legal@company.com", "governance@company.com"],
        "pagerduty": "oncall-ai-ethics"
    },
    action_required={
        "owner": "Governance Circle + Legal",
        "sla": "4 hours",
        "runbook": "https://wiki.company.com/ai-governance/bias-response"
    }
)

# Deploy alert to production monitoring
bias_alert.deploy()
```

---

## Part 4: Ethical Risk Assessment (Detailed)

### When to Conduct Ethical Risk Assessment

**Trigger any of these:**
- [ ] New AI agent being deployed
- [ ] Existing agent autonomy level increasing
- [ ] AI making decisions about people (hiring, credit, pricing, content moderation)
- [ ] Handling sensitive data (PII, health, financial)
- [ ] Regulatory scrutiny likely (GDPR, CCPA, HIPAA, Fair Lending)

**Frequency:**
- **Pre-deployment:** Always (before agent goes to production)
- **Ongoing:** Quarterly (for high-risk agents), annually (for medium-risk)

---

### Ethical Risk Assessment Template

```yaml
# ETHICAL RISK ASSESSMENT

## 1. BASIC INFORMATION
agent_name: "ResumeScreener-Agent"
purpose: "Score resumes, recommend top candidates for interview"
owner: "Head of Talent"
deployment_date: "2025-12-01"
review_date: "2025-11-01"
reviewer: "Sarah Johnson (Governance Circle), Mark Lee (Legal)"

## 2. IMPACT ASSESSMENT

### 2.1 Who is affected?
affected_parties:
  - Job applicants (primary)
  - Hiring managers (use AI recommendations)
  - Company (risk of discrimination lawsuit)
  - Society (perpetuating or reducing hiring bias)

### 2.2 What decisions does AI make?
decisions:
  - Scores resumes (0-100)
  - Recommends top 20 for interview
  - Does NOT make final hiring decision (human does)

### 2.3 What are consequences if AI is wrong?
consequences:
  - False positive: Waste recruiter time on bad candidate (minor)
  - False negative: Miss great candidate (significant - candidate loses opportunity)
  - Bias: Systematically reject protected groups (critical - legal/reputational damage)

## 3. BIAS & FAIRNESS ANALYSIS

### 3.1 Protected Attributes
protected_attributes: [gender, race, age, disability_status, veteran_status]
data_contains_protected_attributes: false (intentionally excluded)
proxy_attributes_risk: high (university name, zip code correlate with race/income)

### 3.2 Training Data Bias
training_data_source: "10,000 historical resumes (2020-2025)"
bias_in_training_data:
  - Historical hiring was 70% male, 30% female (company was biased)
  - Historical hiring favored Ivy League schools (socioeconomic bias)
  - Resumes from certain zip codes overrepresented

mitigation_applied:
  - Re-balanced dataset (50/50 male/female)
  - Downweighted university name as feature
  - Tested for disparate impact before deployment

### 3.3 Disparate Impact Testing
test_dataset: "1,000 resumes (500 male, 500 female)"
results:
  - Male approval rate: 22% (110/500)
  - Female approval rate: 20% (100/500)
  - Disparate impact ratio: 1.1 (within acceptable threshold of 1.2)

bias_mitigation_status: ✅ PASS (no significant bias detected)

## 4. TRANSPARENCY & EXPLAINABILITY

### 4.1 Can AI explain its decisions?
explainability: yes
explanation_format: "Resume scored 78/100 because:
  - 5 years experience in Python (requirement: 3+)
  - Led 2 teams (requirement: leadership experience)
  - Worked at Fortune 500 company (relevant experience)
  - Missing: ML certification (preferred but not required)"

### 4.2 Can applicants challenge decisions?
appeal_process: yes
process: "Applicants can request human review via careers@company.com"
human_review_rate: "100% of rejected applicants reviewed by recruiter"

## 5. ACCOUNTABILITY & OVERSIGHT

### 5.1 Human Oversight Model
autonomy_level: "Co-pilot"
human_reviews: "Recruiter reviews all AI recommendations before final decision"
override_rate: "Expected 10-15% (recruiter disagrees with AI)"

### 5.2 Monitoring & Auditing
monitoring_frequency: monthly
bias_audit_frequency: quarterly
responsible_party: "Head of Talent + Legal"

audit_trail:
  - All resume scores logged (can reproduce any decision)
  - Retention: 7 years (compliance with EEOC)

## 6. PRIVACY & DATA PROTECTION

### 6.1 Personal Data Handling
data_collected: [name, email, work_history, education, skills]
sensitive_data: no (no race, gender, age collected)
consent: yes (applicants submit resume voluntarily)

storage:
  - Encrypted at rest (AES-256)
  - Access restricted (HR team only)
  - Retention: 3 years (then deleted per GDPR)

### 6.2 GDPR/CCPA Compliance
right_to_access: ✅ "Applicants can request resume + score"
right_to_deletion: ✅ "Applicants can request deletion (within 30 days)"
right_to_explanation: ✅ "Applicants receive score explanation"

## 7. SAFETY & SECURITY

### 7.1 Worst-Case Scenario
worst_case: "Biased AI systematically rejects qualified women/minorities → Discrimination lawsuit ($1M+ settlement + reputational damage)"

### 7.2 Guardrails
prohibited_actions:
  - "Do NOT auto-reject applicants (human reviews all)"
  - "Do NOT use protected attributes in scoring"

boundary_conditions:
  - "If disparate impact ratio >1.2, pause and alert Legal"
  - "If override rate >25%, retrain model (AI not aligned with human judgment)"

fail_safe:
  - "If bias detected, revert to manual resume review"

### 7.3 Security
adversarial_risk: low (applicants can't easily game the system)
security_review: ✅ Completed (no PII exposed, access controlled)

## 8. COMPLIANCE & LEGAL

### 8.1 Applicable Regulations
regulations: [EEOC (US), GDPR (EU), CCPA (CA)]
legal_review: ✅ Completed (Nov 1, 2025 - Mark Lee, General Counsel)

### 8.2 Certifications
required_certifications: none
audit_schedule: Annual EEOC self-audit

## 9. RISK SCORE CALCULATION

impact: 5 (critical - discrimination lawsuit risk)
likelihood: 2 (low - extensive testing, human oversight)
autonomy: 2 (co-pilot - human reviews all)

total_risk_score: 5 × 2 × 2 = 20 (🟢 Low Risk)

NOTE: Despite low calculated risk, hiring is ethically sensitive → Treat as MEDIUM+ risk

## 10. GOVERNANCE DECISION

recommendation: ✅ APPROVED (with conditions)

conditions:
  - Monthly bias monitoring (not quarterly)
  - Legal team reviews quarterly (not annually)
  - 100% human review of recommendations (AI cannot auto-reject)
  - Annual third-party fairness audit

approval_authority: Governance Circle + Legal
approved_by: "Sarah Johnson (Governance), Mark Lee (Legal)"
approval_date: "2025-11-01"
next_review: "2026-02-01" (3 months)

deployment_authorized: yes
deployment_date: "2025-12-01"
```

---

## Part 5: Governance Workflows (Who Does What, When)

### Workflow 1: Pre-Deployment Review

**When:** Before any AI agent goes to production

```
WEEK -4: Squad initiates
  ↓
  Squad completes Ethical Risk Assessment (template above)
  ↓
WEEK -3: Governance Circle reviews
  ↓
  If LOW RISK: Approve with light monitoring
  If MEDIUM RISK: Approve with standard monitoring + conditions
  If HIGH RISK: Deep review, may require external audit
  ↓
WEEK -2: Conditions met (bias testing, legal review, etc.)
  ↓
WEEK -1: Final approval
  ↓
WEEK 0: Deploy to production (with monitoring enabled)
  ↓
WEEK +1: Post-deployment review (metrics look good? Any issues?)
```

---

### Workflow 2: Ongoing Monitoring (Monthly/Quarterly)

**Monthly Review (Medium/High Risk Agents):**

```
Week 1 of Month:
  ↓
  Automated alert system generates report:
    - Performance metrics (accuracy, error rate)
    - Bias metrics (disparate impact, demographic parity)
    - Data quality (freshness, completeness)
    - Incident log (any guardrail violations?)
  ↓
  Squad lead reviews report (30 min)
  ↓
  If no issues: Document "reviewed, no action"
  If issues: Create action plan, escalate if needed
  ↓
  Report submitted to Governance Circle (for high-risk agents)
```

**Quarterly Review (All Agents):**

```
End of Quarter:
  ↓
  Governance Circle convenes (2-hour meeting)
  ↓
  Review all agents:
    - Risk score re-calculation (has risk changed?)
    - Performance trends (improving or degrading?)
    - Ethical compliance (any bias creeping in?)
    - User feedback (satisfaction, complaints)
  ↓
  Decisions:
    - Continue as-is (no changes)
    - Increase monitoring (move to higher tier)
    - Decrease autonomy (add human oversight)
    - Retire agent (not performing, too risky)
  ↓
  Document decisions, communicate to squads
```

---

### Workflow 3: Incident Response (When Alerts Fire)

**🟡 Warning Alert (e.g., accuracy drop):**

```
Alert fires → Slack notification
  ↓
Squad lead investigates (within 24-48 hours)
  ↓
Root cause found:
  - If fixable: Apply fix, monitor for 7 days
  - If not fixable: Escalate to Governance Circle
  ↓
Document incident, share learnings
```

**🔴 Critical Alert (e.g., guardrail violation):**

```
Alert fires → Slack + Page on-call
  ↓
On-call engineer investigates immediately (within 1 hour)
  ↓
Assess damage, rollback if possible
  ↓
If minor: Fix, document, resume
If major: Escalate to Governance Circle + CTO
  ↓
Root cause analysis (within 24 hours)
  ↓
Fix deployed, tested, incident closed
```

**🚨 Emergency Alert (e.g., bias detected):**

```
Alert fires → All-hands notification (Slack, email, page)
  ↓
PAUSE AGENT IMMEDIATELY (stop all decisions)
  ↓
Convene emergency response team (within 4 hours):
  - Governance Circle
  - Legal team
  - Squad lead
  - CTO/CEO (if reputational risk)
  ↓
Damage assessment:
  - How many decisions affected?
  - Is harm reversible?
  - Do we need to contact affected users?
  ↓
Remediation plan:
  - Retrain model (remove bias)
  - Contact affected users (if legally required)
  - Public statement (if media coverage)
  ↓
Legal review before re-enabling agent
  ↓
Post-mortem (what went wrong? How to prevent?)
```

---

## Part 6: Governance Circle Structure

### Governance Circle Composition

**Purpose:** Multi-disciplinary oversight of AI systems

**Members (5-7 people):**
1. **Technical Lead** (CTO or VP Engineering) - Understands AI/ML
2. **Legal/Compliance** (General Counsel or delegate) - Regulatory expertise
3. **Ethics Representative** (could be HR, DEI officer, or external advisor) - Ethical lens
4. **Business Leader** (CFO, COO, or business unit head) - Business context
5. **Data/Analytics Lead** (Chief Data Officer or senior analyst) - Data quality oversight
6. **Customer Advocate** (CS leader or customer rep) - User impact perspective
7. **Security/Risk** (CISO or Risk Manager) - Security and operational risk

**Meeting Cadence:**
- **Monthly:** Standard review (2 hours)
- **Quarterly:** Deep dive (4 hours, strategic)
- **Ad-hoc:** Emergency response (as needed)

**Responsibilities:**
- Review and approve high-risk AI agents
- Monitor ongoing performance and ethics
- Respond to incidents
- Update governance policies
- Report to Board (quarterly summary)

---

### Escalation Matrix

| Situation | Escalate To | Timeline |
|-----------|-------------|----------|
| Performance degradation (accuracy drop <10%) | Squad lead | 48 hours |
| Performance degradation (accuracy drop >10%) | Governance Circle | 24 hours |
| Guardrail violation (minor) | Squad lead + On-call | 1 hour |
| Guardrail violation (major) | Governance Circle + CTO | Immediate |
| Bias detected | Legal + Governance Circle + CEO | 4 hours (emergency) |
| Data breach / PII exposure | Legal + CISO + CEO + Board | Immediate (emergency) |
| Regulatory inquiry | Legal + Governance Circle + CEO | Immediate |
| Media coverage (negative) | PR + Legal + CEO | Immediate |

---

## Conclusion: Operationalizing Governance

**The Goal:** Make governance **proactive, data-driven, and sustainable** (not bureaucratic)

**Key Principles:**

1. **Risk-Based:** High-risk AI gets heavy oversight, low-risk moves fast
2. **Automated Alerts:** Catch issues early (before they become crises)
3. **Clear Ownership:** Every agent has a human owner who's accountable
4. **Tiered Reviews:** Don't treat all AI the same (tailor oversight to risk)
5. **Continuous Monitoring:** Governance isn't one-time approval, it's ongoing

**Success Metrics:**

✅ **Zero bias incidents** in production (caught in testing)  
✅ **<24 hour** mean time to detection (alerts fire before users complain)  
✅ **>90% alert accuracy** (minimal false alarms)  
✅ **100% high-risk agents** reviewed quarterly  
✅ **<5% governance overhead** (teams don't feel slowed down)

**Start Small:**

1. **Week 1:** Implement risk scoring for existing agents
2. **Week 2:** Set up basic alerts (performance, safety)
3. **Month 1:** Establish Governance Circle, conduct first reviews
4. **Month 3:** Refine based on learnings, expand coverage

**Remember:** Governance enables innovation by building trust. Without trust, AI initiatives get shut down. With trust, they scale.

---

**Next Steps:**
- [Quality & Ethics Playbook](../implementation/ai-native-agile-quality-ethics.md) - DoR/DoD checklists
- [Implementing AI Agents](../implementation/implementing-ai-agents-practical-guide.md) - Build with governance in mind
- [Governance & Ethics](../../DOCS/06-governance-ethics.md) - Foundational principles

**ADOPTION Resources:**
- **Checklist:** [Governance & Ethics Review](../../ADOPTION/CHECKLISTS/governance-ethics-review.md) - Risk scoring & automated alerts setup
- **Template:** [Risk Assessment Template](../../ADOPTION/TEMPLATES/risk-assessment-template.yaml) - Complete YAML with examples
- **Diagram:** [Risk Scoring Framework](../../DIAGRAMS/risk-scoring-framework.mmd) - Decision tree with 5 risk tiers & examples

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Framework:** SOLID.AI  
**License:** MIT