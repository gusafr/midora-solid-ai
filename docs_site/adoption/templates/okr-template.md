# OKR Template (AI-Native)

**Purpose:** Copy-paste YAML template for setting AI-native OKRs with augmentation factors and AI agent KPIs.

---

## How to Use This Template

1. **Copy the YAML below** into your quarterly OKR planning documentation
2. **Define your Objective** (what you want to achieve)
3. **Set 3-4 Key Results** with baseline → target metrics
4. **Calculate Augmentation Factor** (Human+AI output) / (Human-only output)
5. **Track 8 Universal AI Agent KPIs** (if using AI agents)
6. **Review weekly** and adjust as needed

---

## Template Contents

This template includes:
- ✅ **Objective + Key Results** - Standard OKR format with AI components
- ✅ **Augmentation Factor Calculation** - Measure Human+AI performance vs Human-only
- ✅ **8 Universal AI Agent KPIs** - Automation rate, accuracy, latency, cost, error rate, uptime, adoption, feedback
- ✅ **Weekly Check-Ins** - Track progress and confidence
- ✅ **End-of-Quarter Review** - Retrospective and learnings
- ✅ **Complete Examples** - Sales and Engineering OKRs

---

## Download Template

**File:** [`okr-template.yaml`](okr-template.yaml)

---

## Template Preview

```yaml
---
# AI-NATIVE OKR TEMPLATE
# Purpose: Set quarterly objectives with AI augmentation factors
# Framework: SOLID.AI
# Version: 1.0
# Last Updated: November 2025

# ========================================
# OKR OVERVIEW
# ========================================
okr:
  quarter: "[Q1 | Q2 | Q3 | Q4] YYYY"
  function: "[Sales | Engineering | Finance | Marketing | CS | HR | Operations | Executive]"
  owner: "[DRI - Directly Responsible Individual]"
  team: "[Team name]"
  last_updated: "YYYY-MM-DD"

# ========================================
# OBJECTIVE
# ========================================
objective:
  statement: "[What do you want to achieve this quarter?]"
  # Example: "Scale customer acquisition without increasing headcount"
  # Example: "Improve engineering velocity while maintaining quality"
  
  why_it_matters: "[Why is this important to the business?]"
  # Example: "Hit $5M ARR milestone, prove product-market fit"
  
  ai_role: "[How will AI help achieve this?]"
  # Example: "AI automates lead research, personalized outreach, forecasting"

# ========================================
# KEY RESULT 1
# ========================================
key_result_1:
  statement: "[Specific, measurable outcome]"
  # Example: "Increase closed deals from 20/month to 30/month"
  
  metric: "[What are you measuring?]"
  baseline: "[Current state at start of quarter]"
  target: "[Goal by end of quarter]"
  
  ai_component:
    description: "[How AI contributes]"
    # Example: "AI generates personalized emails, qualifies leads 3x faster"
    ai_agents_involved:
      - "[Agent 1: e.g., LeadResearchBot]"
      - "[Agent 2: e.g., OutreachAutomationAgent]"
      
  augmentation_factor:
    calculation: "(Human+AI Output) / (Human-Only Output)"
    baseline_human_only: "[e.g., 20 deals/month without AI]"
    target_human_plus_ai: "[e.g., 30 deals/month with AI]"
    expected_factor: "[e.g., 1.5x = 50% improvement]"
    
  milestones:
    week_4: "[e.g., 23 deals/month, 1.15x factor]"
    week_8: "[e.g., 26 deals/month, 1.3x factor]"
    week_12: "[e.g., 30 deals/month, 1.5x factor]"
    
  confidence: "[70% | 80% | 90% | 100%]"
  # How confident are you in hitting this target?

# ========================================
# KEY RESULT 2
# ========================================
key_result_2:
  statement: "[Specific, measurable outcome]"
  metric: "[What are you measuring?]"
  baseline: "[Current state]"
  target: "[Goal]"
  
  ai_component:
    description: "[How AI contributes]"
    ai_agents_involved: []
      
  augmentation_factor:
    calculation: "(Human+AI Output) / (Human-Only Output)"
    baseline_human_only: "[Value]"
    target_human_plus_ai: "[Value]"
    expected_factor: "[e.g., 1.3x]"
    
  milestones:
    week_4: "[Intermediate target]"
    week_8: "[Intermediate target]"
    week_12: "[Final target]"
    
  confidence: "[70% | 80% | 90% | 100%]"

# ========================================
# KEY RESULT 3
# ========================================
key_result_3:
  statement: "[Specific, measurable outcome]"
  metric: "[What are you measuring?]"
  baseline: "[Current state]"
  target: "[Goal]"
  
  ai_component:
    description: "[How AI contributes]"
    ai_agents_involved: []
      
  augmentation_factor:
    calculation: "(Human+AI Output) / (Human-Only Output)"
    baseline_human_only: "[Value]"
    target_human_plus_ai: "[Value]"
    expected_factor: "[e.g., 2.0x]"
    
  milestones:
    week_4: "[Intermediate target]"
    week_8: "[Intermediate target]"
    week_12: "[Final target]"
    
  confidence: "[70% | 80% | 90% | 100%]"

# ========================================
# KEY RESULT 4 (Optional)
# ========================================
key_result_4:
  statement: "[Specific, measurable outcome]"
  metric: "[What are you measuring?]"
  baseline: "[Current state]"
  target: "[Goal]"
  
  ai_component:
    description: "[How AI contributes]"
    ai_agents_involved: []
      
  augmentation_factor:
    calculation: "(Human+AI Output) / (Human-Only Output)"
    baseline_human_only: "[Value]"
    target_human_plus_ai: "[Value]"
    expected_factor: "[e.g., 1.4x]"
    
  milestones:
    week_4: "[Intermediate target]"
    week_8: "[Intermediate target]"
    week_12: "[Final target]"
    
  confidence: "[70% | 80% | 90% | 100%]"

# ========================================
# 8 UNIVERSAL AI AGENT KPIs
# ========================================
# Track these KPIs for ALL AI agents involved in this OKR

ai_agent_kpis:
  # KPI 1: Automation Rate
  automation_rate:
    definition: "% of tasks handled by AI without human intervention"
    target: "[e.g., 80% of lead research automated]"
    current: "[Measured weekly]"
    
  # KPI 2: Accuracy
  accuracy:
    definition: "% of AI outputs that are correct/usable"
    target: "[e.g., 95% of emails require no editing]"
    current: "[Measured via spot-checks]"
    
  # KPI 3: Latency
  latency:
    definition: "Time for AI to complete a task"
    target: "[e.g., <2 seconds for lead scoring]"
    current: "[Measured via monitoring]"
    
  # KPI 4: Cost per Task
  cost_per_task:
    definition: "Cost of AI execution (API calls, compute)"
    target: "[e.g., <$0.10 per email generated]"
    current: "[Measured via billing]"
    
  # KPI 5: Error Rate
  error_rate:
    definition: "% of tasks that fail or require retry"
    target: "[e.g., <2% error rate]"
    current: "[Measured via logs]"
    
  # KPI 6: Uptime/Availability
  uptime:
    definition: "% of time AI is available (not down)"
    target: "[e.g., 99.5% uptime]"
    current: "[Measured via monitoring]"
    
  # KPI 7: Adoption Rate
  adoption:
    definition: "% of team actively using AI"
    target: "[e.g., 90% of AEs use AI weekly]"
    current: "[Measured via usage analytics]"
    
  # KPI 8: User Satisfaction
  user_satisfaction:
    definition: "NPS or satisfaction score from users"
    target: "[e.g., NPS >50]"
    current: "[Measured via monthly survey]"

# ========================================
# RISKS & DEPENDENCIES
# ========================================
risks:
  - risk: "[What could prevent you from hitting this OKR?]"
    mitigation: "[How will you reduce this risk?]"
    owner: "[Who's responsible for mitigation?]"
    
dependencies:
  - dependency: "[What do you need from other teams?]"
    status: "[Blocked | In Progress | Complete]"
    owner: "[Who's responsible?]"

# ========================================
# GOVERNANCE METRICS (if applicable)
# ========================================
# Include these if your OKR involves high-risk AI or customer-facing AI

governance:
  bias_fairness:
    metric: "Disparity across customer segments"
    target: "<5% disparity"
    current: "[Measured monthly]"
    
  transparency:
    metric: "% of AI decisions explainable"
    target: "100% of high-value decisions logged"
    current: "[Measured via audit trail]"
    
  privacy:
    metric: "% of AI tasks compliant with data policy"
    target: "100% compliance (zero PII leaks)"
    current: "[Measured via governance circle reviews]"
    
  incidents:
    metric: "AI governance incidents (errors, misuse)"
    target: "<5 incidents per quarter"
    current: "[Measured via incident reports]"

# ========================================
# WEEKLY CHECK-INS
# ========================================
# Track progress every week (12 weeks per quarter)

weekly_checkins:
  week_1:
    kr1_progress: "[e.g., 21 deals]"
    kr2_progress: "[...]"
    kr3_progress: "[...]"
    blockers: "[Any issues?]"
    confidence: "[70-100%]"
    
  week_2:
    kr1_progress: ""
    kr2_progress: ""
    kr3_progress: ""
    blockers: ""
    confidence: ""
    
  # ... weeks 3-12 ...
  
  week_12:
    kr1_progress: "[Final: 30 deals]"
    kr2_progress: "[Final: ...]"
    kr3_progress: "[Final: ...]"
    blockers: ""
    confidence: "[100% (achieved) or <100% (missed)]"

# ========================================
# END-OF-QUARTER REVIEW
# ========================================
end_of_quarter_review:
  objective_achieved: "[Yes | Partial | No]"
  final_scores:
    kr1: "[0.0-1.0, e.g., 0.9 = 90% of target]"
    kr2: "[0.0-1.0]"
    kr3: "[0.0-1.0]"
    kr4: "[0.0-1.0]"
    overall: "[Average of KRs]"
    
  augmentation_factor_achieved:
    kr1: "[e.g., 1.5x as planned]"
    kr2: "[e.g., 1.2x, missed 1.3x target]"
    kr3: "[...]"
    
  what_worked:
    - "[What went well?]"
    - "[e.g., AI email automation saved 10h/week]"
    
  what_didnt_work:
    - "[What didn't go as planned?]"
    - "[e.g., Lead scoring model had 15% error rate, needed retraining]"
    
  lessons_learned:
    - "[What did you learn about AI?]"
    - "[e.g., AI works best with clean data - invest in data quality upfront]"
    
  next_quarter_adjustments:
    - "[What will you do differently next quarter?]"
    - "[e.g., Add human review for leads >$50K]"

# ========================================
# EXAMPLE 1: SALES OKR (Scaling Deals)
# ========================================
example_sales:
  okr:
    quarter: "Q1 2026"
    function: "Sales"
    owner: "Sarah Johnson (VP Sales)"
    team: "Sales Team (10 AEs)"
    last_updated: "2025-12-15"
    
  objective:
    statement: "Scale customer acquisition 50% without increasing headcount"
    why_it_matters: "Hit $5M ARR milestone, prove product-market fit before Series A"
    ai_role: "AI automates lead research, personalized outreach, and forecasting, freeing AEs for closing"
    
  key_result_1:
    statement: "Increase closed deals from 20/month to 30/month"
    metric: "Closed deals per month"
    baseline: "20 deals/month (without AI)"
    target: "30 deals/month (with AI)"
    ai_component:
      description: "AI generates personalized emails for 100 leads/day, scores top 20% for AE follow-up"
      ai_agents_involved:
        - "LeadResearchBot (researches companies, finds pain points)"
        - "OutreachAutomationAgent (writes 1:1 emails, not templates)"
        - "DealScorePredictor (predicts close likelihood)"
    augmentation_factor:
      calculation: "30 deals / 20 deals"
      baseline_human_only: "20 deals/month"
      target_human_plus_ai: "30 deals/month"
      expected_factor: "1.5x"
    milestones:
      week_4: "23 deals/month (1.15x)"
      week_8: "26 deals/month (1.3x)"
      week_12: "30 deals/month (1.5x)"
    confidence: "80%"
    
  key_result_2:
    statement: "Reduce time-to-close from 45 days to 30 days"
    metric: "Average days from lead to closed deal"
    baseline: "45 days"
    target: "30 days"
    ai_component:
      description: "AI flags at-risk deals, suggests next-best actions, automates follow-ups"
      ai_agents_involved:
        - "DealHealthMonitor (predicts deal risk)"
        - "NextBestActionBot (suggests what AE should do next)"
    augmentation_factor:
      calculation: "45 days / 30 days"
      baseline_human_only: "45 days"
      target_human_plus_ai: "30 days"
      expected_factor: "1.5x faster"
    milestones:
      week_4: "40 days"
      week_8: "35 days"
      week_12: "30 days"
    confidence: "70%"
    
  key_result_3:
    statement: "Maintain 90%+ forecast accuracy (no regression with AI)"
    metric: "Forecast accuracy (predicted vs. actual deals)"
    baseline: "90% accuracy (manual forecasting)"
    target: "90%+ accuracy (AI-powered forecasting)"
    ai_component:
      description: "AI analyzes historical data, predicts close rates, adjusts forecasts weekly"
      ai_agents_involved:
        - "ForecastingBot (predicts monthly deals based on pipeline)"
    augmentation_factor:
      calculation: "Accuracy maintained (not degraded)"
      baseline_human_only: "90% accuracy"
      target_human_plus_ai: "90%+ accuracy"
      expected_factor: "1.0x (maintain quality while scaling)"
    milestones:
      week_4: "88% accuracy (learning phase)"
      week_8: "90% accuracy (on par)"
      week_12: "92% accuracy (better than baseline)"
    confidence: "90%"
    
  ai_agent_kpis:
    automation_rate:
      target: "80% of lead research automated"
      current: "Measured weekly via Salesforce logs"
    accuracy:
      target: "95% of AI emails require no editing"
      current: "Spot-check 20 emails/week"
    latency:
      target: "<5 seconds to generate email"
      current: "Monitored via agent logs"
    cost_per_task:
      target: "<$0.10 per email"
      current: "OpenAI API billing"
    error_rate:
      target: "<2% failed emails"
      current: "Error logs"
    uptime:
      target: "99.5% uptime"
      current: "Monitoring dashboard"
    adoption:
      target: "100% of AEs use AI weekly"
      current: "Usage analytics"
    user_satisfaction:
      target: "NPS >50"
      current: "Monthly survey"
      
  end_of_quarter_review:
    objective_achieved: "Yes"
    final_scores:
      kr1: "1.0 (30 deals achieved)"
      kr2: "0.8 (36 days, missed 30-day target)"
      kr3: "1.0 (92% forecast accuracy)"
      overall: "0.93 (93% OKR completion)"
    augmentation_factor_achieved:
      kr1: "1.5x (as planned)"
      kr2: "1.25x (vs. 1.5x target)"
      kr3: "1.02x (slight improvement)"
    what_worked:
      - "AI email generation saved 15h/week per AE"
      - "Lead scoring improved conversion 20%"
    what_didnt_work:
      - "Deal health monitor had false positives (flagged healthy deals as at-risk)"
    lessons_learned:
      - "AI works best with clean CRM data - we had to clean 6 months of data first"
      - "AEs needed 2 weeks of training to trust AI suggestions"
    next_quarter_adjustments:
      - "Retrain deal health model with more data"
      - "Add human review for deals >$50K"

# ========================================
# EXAMPLE 2: ENGINEERING OKR (Velocity + Quality)
# ========================================
example_engineering:
  okr:
    quarter: "Q1 2026"
    function: "Engineering"
    owner: "Alex Chen (VP Engineering)"
    team: "Product Engineering (20 engineers)"
    last_updated: "2025-12-15"
    
  objective:
    statement: "Increase engineering velocity 40% while maintaining <2% production bugs"
    why_it_matters: "Ship more features faster to hit product roadmap, prove we can scale without hiring"
    ai_role: "AI writes 60% of boilerplate code, reviews all PRs, automates testing"
    
  key_result_1:
    statement: "Increase story points completed from 40/sprint to 56/sprint"
    metric: "Story points completed per 2-week sprint"
    baseline: "40 points/sprint (without AI)"
    target: "56 points/sprint (with AI)"
    ai_component:
      description: "GitHub Copilot writes boilerplate, tests, documentation"
      ai_agents_involved:
        - "GitHub Copilot (code generation)"
        - "CodeReviewBot (automated PR reviews)"
    augmentation_factor:
      calculation: "56 points / 40 points"
      baseline_human_only: "40 points/sprint"
      target_human_plus_ai: "56 points/sprint"
      expected_factor: "1.4x"
    milestones:
      week_4: "45 points/sprint (1.125x)"
      week_8: "50 points/sprint (1.25x)"
      week_12: "56 points/sprint (1.4x)"
    confidence: "85%"
    
  key_result_2:
    statement: "Maintain <2% production bugs (no regression with AI code)"
    metric: "% of releases with critical bugs"
    baseline: "1.5% bug rate (manual coding)"
    target: "<2% bug rate (AI-assisted coding)"
    ai_component:
      description: "AI reviews all PRs, flags potential bugs, generates tests"
      ai_agents_involved:
        - "CodeReviewBot (checks for anti-patterns, security issues)"
        - "TestGeneratorBot (writes unit tests)"
    augmentation_factor:
      calculation: "Quality maintained (not degraded)"
      baseline_human_only: "1.5% bug rate"
      target_human_plus_ai: "<2% bug rate"
      expected_factor: "1.0x (maintain quality)"
    milestones:
      week_4: "2.0% (learning phase)"
      week_8: "1.8%"
      week_12: "<1.5% (better than baseline)"
    confidence: "90%"
    
  key_result_3:
    statement: "Reduce code review time from 24h to 4h"
    metric: "Average time from PR open to merge"
    baseline: "24 hours"
    target: "4 hours"
    ai_component:
      description: "AI does initial review, humans only review logic/design"
      ai_agents_involved:
        - "CodeReviewBot (auto-approves simple PRs, flags complex ones)"
    augmentation_factor:
      calculation: "24h / 4h"
      baseline_human_only: "24 hours"
      target_human_plus_ai: "4 hours"
      expected_factor: "6.0x faster"
    milestones:
      week_4: "16 hours"
      week_8: "8 hours"
      week_12: "4 hours"
    confidence: "75%"

---

# Related Resources

**Playbooks:**
- [AI-Native OKRs & KPIs](../../playbooks/people-culture/ai-native-okrs-kpis.md)

**Checklists:**
- [OKR & KPI Setup](../checklists/okr-kpi-setup.md)

**Diagrams:**
- [Augmentation Factor Calculation](../../diagrams.md#augmentation-factor-calculation) - Formula + role examples

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Framework:** SOLID.AI  
**License:** MIT
```

---

## Next Steps

1. **Download the template** (YAML file above)
2. **Set your Objective** (what you want to achieve this quarter)
3. **Define 3-4 Key Results** with AI components
4. **Calculate Augmentation Factors** (measure Human+AI performance)
5. **Track weekly** and adjust as needed
6. **Review at end of quarter** and learn

For detailed guidance, see the [AI-Native OKRs & KPIs Playbook](../../playbooks/people-culture/ai-native-okrs-kpis.md).
