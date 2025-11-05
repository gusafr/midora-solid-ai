# Risk Assessment Template

**Purpose:** Copy-paste YAML template for AI governance risk assessment using the Impact × Likelihood × Autonomy framework.

---

## How to Use This Template

1. **Copy the YAML below** into your project's governance documentation
2. **Fill in your AI initiative details** (name, description, owner)
3. **Score each dimension** (Impact, Likelihood, Autonomy)
4. **Calculate risk score** automatically (Impact × Likelihood × Autonomy)
5. **Configure alerts** for your specific use case
6. **Complete all sections** through sign-off

---

## Template Contents

This template includes:
- ✅ **Risk Scoring Framework** - 5 dimensions of impact, likelihood, autonomy scoring
- ✅ **Automated Tier Calculation** - Maps 1-125 risk score to 5 tiers
- ✅ **Alert Configuration** - 5 alert types (confidence, high-impact, edge case, bias, performance)
- ✅ **Mitigation Planning** - Structured risk mitigation approach
- ✅ **Bias Assessment** - Fairness and ethics evaluation
- ✅ **Accountability Assignment** - Clear DRI and review process
- ✅ **Complete Example** - Invoice processing automation risk assessment

---

## Download Template

**File:** [`risk-assessment-template.yaml`](risk-assessment-template.yaml)

---

## Template Preview

```yaml
---
# AI GOVERNANCE: RISK ASSESSMENT TEMPLATE
# Purpose: Assess AI initiatives using Impact × Likelihood × Autonomy framework
# Framework: SOLID.AI
# Version: 1.0
# Last Updated: November 2025

# ========================================
# STEP 1: AI INITIATIVE DETAILS
# ========================================
initiative:
  name: "[Your AI Initiative Name]"
  description: "[What this AI agent/automation does]"
  function: "[Sales | Finance | Engineering | Marketing | CS | HR | Operations]"
  owner: "[DRI - Directly Responsible Individual]"
  date_created: "YYYY-MM-DD"
  status: "[Planning | In Development | In Production]"

# ========================================
# STEP 2: RISK SCORING - IMPACT (1-5)
# ========================================
# Score the MAXIMUM potential negative impact if AI makes a mistake
# Take the HIGHEST score across all 5 dimensions

impact:
  # Dimension 1: Financial Impact
  financial:
    score: [1-5]  # 1=<$1K, 2=$1K-$10K, 3=$10K-$100K, 4=$100K-$1M, 5=>$1M
    rationale: "[Why this score?]"
    
  # Dimension 2: Reputational Impact
  reputational:
    score: [1-5]  # 1=Internal only, 2=Minor customer, 3=Customer complaint, 4=PR issue, 5=Brand damage
    rationale: "[Why this score?]"
    
  # Dimension 3: Legal/Compliance Impact
  legal:
    score: [1-5]  # 1=None, 2=Policy violation, 3=Regulatory report, 4=Fine, 5=Lawsuit/Shutdown
    rationale: "[Why this score?]"
    
  # Dimension 4: Operational Impact
  operational:
    score: [1-5]  # 1=Minor delay, 2=Process disruption, 3=Service degradation, 4=Outage, 5=Critical failure
    rationale: "[Why this score?]"
    
  # Dimension 5: Human Safety/Well-being
  human_safety:
    score: [1-5]  # 1=None, 2=Inconvenience, 3=Stress, 4=Health risk, 5=Life-threatening
    rationale: "[Why this score?]"
  
  # FINAL IMPACT SCORE (take MAX of above 5)
  final_score: [1-5]

# ========================================
# STEP 3: RISK SCORING - LIKELIHOOD (1-5)
# ========================================
# How likely is it that the AI will make a mistake?

likelihood:
  score: [1-5]  # 1=Rare (<1%), 2=Unlikely (1-5%), 3=Possible (5-20%), 4=Likely (20-50%), 5=Almost Certain (>50%)
  rationale: "[Based on: model accuracy, data quality, edge cases, validation]"
  supporting_data:
    - model_accuracy: "[e.g., 98% on test set]"
    - edge_case_coverage: "[% of scenarios covered by validation]"
    - historical_error_rate: "[if available]"

# ========================================
# STEP 4: RISK SCORING - AUTONOMY (1-5)
# ========================================
# How much autonomy does the AI have? (Less human oversight = higher autonomy)

autonomy:
  score: [1-5]  # 1=Human reviews all, 2=Human spot-checks, 3=Auto (low-value), 4=Auto (high-value), 5=No human in loop
  rationale: "[Describe the human oversight model]"
  human_in_loop:
    review_frequency: "[All | Daily | Weekly | Monthly | None]"
    approval_required: "[Yes | No | Conditional]"
    conditions_for_escalation: "[e.g., Amount >$5K, Confidence <90%]"

# ========================================
# STEP 5: CALCULATE TOTAL RISK SCORE
# ========================================
risk_score:
  impact: [1-5]
  likelihood: [1-5]
  autonomy: [1-5]
  total: [1-125]  # Impact × Likelihood × Autonomy
  
# ========================================
# STEP 6: DETERMINE RISK TIER
# ========================================
# Based on total risk score, determine tier and required approvals

risk_tier:
  tier: [1-5]  # 1=Minimal, 2=Low, 3=Medium, 4=High, 5=Extreme
  tier_definition:
    tier_1: "1-8 (Minimal Risk - DRI approval, same-day review)"
    tier_2: "9-27 (Low Risk - Manager approval, 1-day review)"
    tier_3: "28-64 (Medium Risk - Director + Compliance approval, 2-day review)"
    tier_4: "65-100 (High Risk - VP + Legal approval, 3-day review)"
    tier_5: "101-125 (Extreme Risk - Board approval, 5-day review)"
  
  required_approvals:
    - role: "[e.g., Manager, Director, VP, Board]"
      name: "[Approver name]"
      approved: "[Yes | No | Pending]"
      date: "YYYY-MM-DD"
      
  review_sla: "[Same-day | 1-day | 2-day | 3-day | 5-day]"

# ========================================
# STEP 7: CONFIGURE AUTOMATED ALERTS
# ========================================
# Set up 5 types of alerts to catch issues proactively

alerts:
  # Alert Type 1: Low Confidence Alerts
  low_confidence:
    enabled: [true | false]
    threshold: "[e.g., <80% confidence]"
    action: "[e.g., Escalate to human, Log for review]"
    notification_channel: "[Slack, Email, Dashboard]"
    
  # Alert Type 2: High-Impact Decision Alerts
  high_impact:
    enabled: [true | false]
    threshold: "[e.g., >$10K transaction, >100 users affected]"
    action: "[e.g., Require human approval, Notify VP]"
    notification_channel: "[Slack, Email, Dashboard]"
    
  # Alert Type 3: Edge Case Alerts
  edge_case:
    enabled: [true | false]
    definition: "[e.g., Data outside training distribution, Unusual pattern]"
    action: "[e.g., Flag for review, Log for retraining]"
    notification_channel: "[Slack, Email, Dashboard]"
    
  # Alert Type 4: Bias/Fairness Alerts
  bias:
    enabled: [true | false]
    monitored_groups: "[e.g., Demographics, Regions, Customer segments]"
    threshold: "[e.g., >5% disparity across groups]"
    action: "[e.g., Escalate to Ethics Circle, Pause rollout]"
    notification_channel: "[Slack, Email, Dashboard]"
    
  # Alert Type 5: Performance Degradation Alerts
  performance:
    enabled: [true | false]
    metrics:
      - accuracy: "[e.g., <95%]"
      - latency: "[e.g., >2 seconds]"
      - error_rate: "[e.g., >1%]"
    action: "[e.g., Rollback, Notify on-call]"
    notification_channel: "[Slack, Email, PagerDuty]"

# ========================================
# STEP 8: RISK MITIGATION PLAN
# ========================================
mitigation:
  # Pre-Deployment Mitigations
  pre_deployment:
    - action: "[e.g., Human-in-loop review for 30 days]"
      owner: "[Name]"
      due_date: "YYYY-MM-DD"
      status: "[Not Started | In Progress | Complete]"
      
  # Post-Deployment Monitoring
  post_deployment:
    - metric: "[e.g., Weekly accuracy review]"
      target: "[e.g., >98% accuracy]"
      review_cadence: "[Daily | Weekly | Monthly]"
      owner: "[Name]"
      
  # Rollback Plan
  rollback:
    trigger: "[When to rollback? e.g., Accuracy <95%, >5 customer complaints]"
    steps:
      - "[Step 1: Disable AI, revert to manual process]"
      - "[Step 2: Notify stakeholders]"
      - "[Step 3: Root cause analysis]"
    owner: "[Name]"

# ========================================
# STEP 9: BIAS & FAIRNESS ASSESSMENT
# ========================================
bias_assessment:
  protected_groups_considered: "[Yes | No]"
  groups:
    - "[e.g., Gender, Age, Geography, Customer segment]"
  
  fairness_metrics:
    - metric: "[e.g., Equal Opportunity, Demographic Parity]"
      target: "[e.g., <5% disparity]"
      current_value: "[Measured value]"
      status: "[Pass | Fail | Needs Improvement]"
      
  bias_mitigation:
    - action: "[e.g., Retrain with balanced dataset]"
      owner: "[Name]"
      due_date: "YYYY-MM-DD"

# ========================================
# STEP 10: ACCOUNTABILITY & SIGN-OFF
# ========================================
accountability:
  dri: "[Directly Responsible Individual]"
  governance_circle_review:
    reviewed_by: "[Name]"
    date: "YYYY-MM-DD"
    approval: "[Approved | Conditional | Rejected]"
    conditions: "[If conditional, what needs to be addressed?]"
    
  final_sign_off:
    approver: "[VP, Director, Board - based on tier]"
    date: "YYYY-MM-DD"
    approval: "[Approved | Rejected]"
    notes: "[Any final comments]"

# ========================================
# EXAMPLE: INVOICE PROCESSING AUTOMATION
# ========================================
# Below is a complete example for reference

example_invoice_processing:
  initiative:
    name: "Automated Invoice Processing"
    description: "AI extracts data from PDF invoices, validates against PO, routes for approval"
    function: "Finance"
    owner: "Jane Smith (Finance Ops Lead)"
    date_created: "2025-11-01"
    status: "In Production"
    
  impact:
    financial:
      score: 3  # Could approve $10K-$100K incorrectly
      rationale: "Max invoice value is $50K, but catches most errors"
    reputational:
      score: 2  # Minor vendor complaint if payment delayed
      rationale: "Internal process, low external visibility"
    legal:
      score: 2  # Could violate payment terms
      rationale: "No regulatory impact, just contract compliance"
    operational:
      score: 3  # Could delay payments, disrupt vendor relationships
      rationale: "If AI fails, manual backup takes 3 days"
    human_safety:
      score: 1  # No safety impact
      rationale: "Finance process, no physical risk"
    final_score: 3  # MAX of above
    
  likelihood:
    score: 2  # Unlikely (1-5% error rate)
    rationale: "Model tested at 97% accuracy, human spot-checks catch most errors"
    supporting_data:
      - model_accuracy: "97% on 10K invoice test set"
      - edge_case_coverage: "90% of vendor formats covered"
      - historical_error_rate: "2% (since deployment)"
      
  autonomy:
    score: 4  # Auto-approves <$5K, escalates >$5K
    rationale: "Human reviews only high-value or low-confidence invoices"
    human_in_loop:
      review_frequency: "Daily (for escalations only)"
      approval_required: "Yes (for >$5K)"
      conditions_for_escalation: "Amount >$5K OR Confidence <90%"
      
  risk_score:
    impact: 3
    likelihood: 2
    autonomy: 4
    total: 24  # 3 × 2 × 4
    
  risk_tier:
    tier: 2  # Low Risk (9-27)
    required_approvals:
      - role: "Finance Manager"
        name: "John Doe"
        approved: "Yes"
        date: "2025-11-01"
    review_sla: "1-day"
    
  alerts:
    low_confidence:
      enabled: true
      threshold: "<90% confidence"
      action: "Escalate to human"
      notification_channel: "Slack #finance-ops"
    high_impact:
      enabled: true
      threshold: ">$5K"
      action: "Require human approval"
      notification_channel: "Email to Finance Manager"
    edge_case:
      enabled: true
      definition: "New vendor format not in training data"
      action: "Log for retraining"
      notification_channel: "Dashboard"
    bias:
      enabled: false  # Not applicable for invoice processing
    performance:
      enabled: true
      metrics:
        - accuracy: "<95%"
        - latency: ">5 seconds"
        - error_rate: ">3%"
      action: "Notify on-call engineer"
      notification_channel: "PagerDuty"
      
  mitigation:
    pre_deployment:
      - action: "Human-in-loop for 30 days (review all invoices)"
        owner: "Jane Smith"
        due_date: "2025-10-01"
        status: "Complete"
    post_deployment:
      - metric: "Weekly accuracy review"
        target: ">97% accuracy"
        review_cadence: "Weekly"
        owner: "Jane Smith"
    rollback:
      trigger: "Accuracy <95% for 2 consecutive weeks"
      steps:
        - "Disable AI, revert to manual entry"
        - "Notify Finance team and vendors"
        - "Debug model, retrain if needed"
      owner: "Jane Smith"
      
  bias_assessment:
    protected_groups_considered: "No (not applicable)"
    groups: []
    fairness_metrics: []
    
  accountability:
    dri: "Jane Smith"
    governance_circle_review:
      reviewed_by: "Governance Circle (3 members)"
      date: "2025-10-28"
      approval: "Approved"
      conditions: "Monitor weekly, report to Finance VP monthly"
    final_sign_off:
      approver: "Finance Manager (John Doe)"
      date: "2025-11-01"
      approval: "Approved"
      notes: "Proceed with production rollout, maintain human review for >$5K"

---

# Related Resources

**Playbooks:**
- [AI Governance & Risk Assessment](../../playbooks/governance/ai-governance-risk-assessment.md)

**Checklists:**
- [Governance & Ethics Review](../checklists/governance-ethics-review.md)

**Diagrams:**
- [Risk Scoring Framework](../../diagrams.md#risk-scoring-framework) - Decision tree with examples

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Framework:** SOLID.AI  
**License:** MIT
```

---

## Next Steps

1. **Download the template** (YAML file above)
2. **Fill in your initiative details**
3. **Calculate risk score** and determine tier
4. **Submit for governance review**
5. **Configure alerts** in your monitoring system
6. **Monitor post-deployment** and adjust as needed

For detailed guidance, see the [AI Governance & Risk Assessment Playbook](../../playbooks/governance/ai-governance-risk-assessment.md).
