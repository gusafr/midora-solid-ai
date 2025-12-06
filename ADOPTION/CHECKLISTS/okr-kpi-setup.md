# AI-Native OKR/KPI Setup Checklist

**Purpose:** Establish metrics that measure both AI agent performance and human-AI collaboration effectiveness

**Framework:** SOLID.AI | **Version:** 1.0  
**Reference:** [AI-Native OKRs & KPIs Playbook](../../PLAYBOOKS/people-culture/ai-native-okrs-kpis.md)

---

## Phase 1: Define Universal AI Agent KPIs (Week 1)

### 8 Universal KPIs for All AI Agents

**Set up tracking for these metrics across all agents:**

- [ ] **1. Automation Rate**
  - Formula: `Tasks Completed by AI / Total Tasks × 100`
  - Target: ___% (typical: 60-80% for mature agents)
  - Data source: ______________________________

- [ ] **2. Accuracy/Precision**
  - Formula: `Correct Outputs / Total Outputs × 100`
  - Target: ___% (typical: 95%+ for production)
  - Validation method: ______________________________

- [ ] **3. Human Intervention Rate**
  - Formula: `Tasks Escalated to Humans / Total Tasks × 100`
  - Target: ___% (typical: 5-10%)
  - Escalation reasons tracked: ☐ Yes ☐ No

- [ ] **4. Latency/Response Time**
  - Metric: _____ (seconds/minutes for agent to respond)
  - Target: _____ (typical: <30 seconds)
  - P50/P95/P99 tracked: ☐ Yes ☐ No

- [ ] **5. Cost per Task**
  - Formula: `Total AI Costs / Tasks Completed`
  - Target: $_____ (typical: $0.01-$1.00 per task)
  - Breakdown: API costs, compute, human validation

- [ ] **6. Human Validation Rate**
  - Formula: `Tasks Validated by Humans / Total Tasks × 100`
  - Target: ___% (typical: 10-30% initially, decreasing over time)
  - Validation SLA: _____ hours/days

- [ ] **7. Learning Velocity**
  - Metric: How fast agent improves accuracy (% improvement per month)
  - Target: +___% per month (typical: +2-5%)
  - Tracking method: ______________________________

- [ ] **8. User Satisfaction (for agent)**
  - Metric: Thumbs up/down or 1-5 star rating
  - Target: ___/5 (typical: 4.0+)
  - Feedback collection method: ______________________________

**Dashboard Setup:**
- [ ] Create unified AI Agent KPI dashboard (tools: Tableau, Grafana, Looker, etc.)
- [ ] Update frequency: ☐ Real-time ☐ Hourly ☐ Daily
- [ ] Accessible to: ☐ Everyone ☐ Managers+ ☐ Execs only

---

## Phase 2: Calculate Augmentation Factors (Week 2)

### Baseline Human Performance (Pre-AI)

**Choose 3-5 key roles to measure first:**

**Role 1:** ______________________________
- Metric: ______________________________ (e.g., cases handled per week)
- Baseline (pre-AI): _____ per week
- Quality baseline: _____% accuracy

**Role 2:** ______________________________
- Metric: ______________________________ (e.g., sales per rep)
- Baseline (pre-AI): $_____ per month
- Quality baseline: _____% win rate

**Role 3:** ______________________________
- Metric: ______________________________ (e.g., code commits per engineer)
- Baseline (pre-AI): _____ commits per week
- Quality baseline: _____% tests pass

---

### Measure Post-AI Performance

**After 1 month of AI agent deployment:**

**Role 1:** ______________________________
- Current metric: _____ per week
- Quality metric: _____% accuracy
- Augmentation factor: Current ÷ Baseline = _____ (e.g., 1.5x = 50% improvement)

**Role 2:** ______________________________
- Current metric: $_____ per month
- Quality metric: _____% win rate
- Augmentation factor: _____ 

**Role 3:** ______________________________
- Current metric: _____ commits per week
- Quality metric: _____% tests pass
- Augmentation factor: _____ 

**Overall Augmentation Factor (Company-Wide):**
- Revenue per employee: Pre-AI $_____ → Post-AI $_____ = _____x
- Tasks per employee: Pre-AI _____ → Post-AI _____ = _____x
- Costs per employee: Pre-AI $_____ → Post-AI $_____ = _____x (lower is better)

---

### Track Monthly Augmentation Trends

**Monitor improvement over time:**

| Month | Role 1 Aug. Factor | Role 2 Aug. Factor | Role 3 Aug. Factor | Company Aug. Factor |
|-------|-------------------|-------------------|-------------------|---------------------|
| Baseline | 1.0x | 1.0x | 1.0x | 1.0x |
| Month 1 | ___x | ___x | ___x | ___x |
| Month 2 | ___x | ___x | ___x | ___x |
| Month 3 | ___x | ___x | ___x | ___x |
| Month 6 | ___x | ___x | ___x | ___x |

**Target:** 1.3-1.5x augmentation factor within 6 months

---

## Phase 3: Set Function-Specific OKRs (Week 3)

### Sales Function

**Objective:** Increase sales productivity and win rates with AI-augmented reps

**Key Results (Q__ 20__):**
- [ ] **KR1:** AI-augmented reps close ___% more deals than non-augmented (target: +30%)
  - Measurement: CRM data, control group comparison
  - Current: _____% | Target: _____% 

- [ ] **KR2:** Lead scoring AI achieves ___% accuracy (target: 80%)
  - Measurement: Close rate of "high score" leads
  - Current: _____% | Target: _____% 

- [ ] **KR3:** Average deal size increases by ___% (target: +20%)
  - Measurement: AI-surfaced upsell opportunities
  - Current: $_____ | Target: $_____

**Dashboard:** _____________________________ (link to Sales AI dashboard)

---

### Finance & Accounting Function

**Objective:** Automate routine tasks and improve forecast accuracy with AI

**Key Results (Q__ 20__):**
- [ ] **KR1:** ___% of invoices processed without human intervention (target: 80%)
  - Measurement: Invoice processing system logs
  - Current: _____% | Target: _____%

- [ ] **KR2:** Forecast accuracy improves to ___% MAPE (target: <10%)
  - Measurement: Mean Absolute Percentage Error
  - Current: _____% | Target: _____%

- [ ] **KR3:** Month-end close time reduces by ___% (target: -40%)
  - Measurement: Days to close books
  - Current: _____ days | Target: _____ days

**Dashboard:** _____________________________ (link to Finance AI dashboard)

---

### Product & Engineering Function

**Objective:** Accelerate development velocity and improve code quality with AI

**Key Results (Q__ 20__):**
- [ ] **KR1:** Engineers using AI co-pilots ship ___% more features (target: +40%)
  - Measurement: Story points per sprint, feature releases
  - Current: _____ | Target: _____

- [ ] **KR2:** Bug density decreases by ___% (target: -30%)
  - Measurement: Bugs per 1000 lines of code
  - Current: _____ | Target: _____

- [ ] **KR3:** AI-assisted testing covers ___% of code (target: 80%)
  - Measurement: Code coverage reports
  - Current: _____% | Target: _____%

**Dashboard:** _____________________________ (link to Engineering AI dashboard)

---

### Marketing Function

**Objective:** Scale content production and improve personalization with AI

**Key Results (Q__ 20__):**
- [ ] **KR1:** Content output increases by ___% while maintaining quality (target: +100%)
  - Measurement: Blog posts, social posts, emails per month
  - Current: _____ | Target: _____
  - Quality check: Human review score >4/5

- [ ] **KR2:** Email open rates improve by ___% with AI personalization (target: +25%)
  - Measurement: Campaign analytics
  - Current: _____% | Target: _____%

- [ ] **KR3:** SEO rankings improve for ___% of target keywords (target: 70%)
  - Measurement: Keyword position tracking
  - Current: _____% | Target: _____%

**Dashboard:** _____________________________ (link to Marketing AI dashboard)

---

### Customer Success Function

**Objective:** Improve response time and customer satisfaction with AI support

**Key Results (Q__ 20__):**
- [ ] **KR1:** ___% of Tier 1 support handled by AI without escalation (target: 70%)
  - Measurement: Support ticket logs
  - Current: _____% | Target: _____%

- [ ] **KR2:** Average response time decreases to _____ (target: <5 min)
  - Measurement: Time to first response
  - Current: _____ | Target: _____

- [ ] **KR3:** Customer satisfaction (CSAT) increases to _____ (target: 90%+)
  - Measurement: Post-interaction surveys
  - Current: _____% | Target: _____%

**Dashboard:** _____________________________ (link to CS AI dashboard)

---

### Human Resources Function

**Objective:** Streamline recruiting and improve employee experience with AI

**Key Results (Q__ 20__):**
- [ ] **KR1:** Time-to-hire decreases by ___% (target: -30%)
  - Measurement: Days from job posting to offer acceptance
  - Current: _____ days | Target: _____ days

- [ ] **KR2:** Candidate quality score increases to _____ (target: 80%+)
  - Measurement: First-year performance reviews
  - Current: _____% | Target: _____%

- [ ] **KR3:** Employee engagement score increases to _____ (target: 4.5/5)
  - Measurement: Quarterly engagement surveys
  - Current: _____/5 | Target: _____/5

**Dashboard:** _____________________________ (link to HR AI dashboard)

---

## Phase 4: Establish Governance & Ethical KPIs (Week 4)

### Bias & Fairness Metrics
- [ ] **Demographic Parity** (for hiring, lending, scoring agents)
  - Formula: `P(Positive Outcome | Group A) ≈ P(Positive Outcome | Group B)`
  - Acceptable variance: ±___% (typical: ±5%)
  - Groups tracked: Gender, race, age, etc.
  - Audit frequency: ☐ Monthly ☐ Quarterly

- [ ] **Equal Opportunity** (for classification agents)
  - Formula: `P(Predicted Positive | True Positive, Group A) ≈ P(Predicted Positive | True Positive, Group B)`
  - Target: ___% (typical: >95% parity)

---

### Transparency & Explainability
- [ ] **Explainability Coverage**
  - Metric: % of agent decisions with explanations provided
  - Target: ___% (typical: 100% for high-stakes decisions)
  - Explanation quality: Human-understandable (1-5 rating)

- [ ] **Audit Trail Completeness**
  - Metric: % of agent actions logged
  - Target: 100%
  - Retention period: _____ months (typical: 12-24)

---

### Human Accountability
- [ ] **Human Validation Rate**
  - High-stakes decisions: ___% validated (target: 100%)
  - Medium-stakes: ___% validated (target: 30-50%)
  - Low-stakes: ___% validated (target: 5-10%)

- [ ] **Escalation Response Time**
  - Metric: Time from agent escalation to human review
  - Target: _____ hours (typical: <4 hours)
  - SLA breach rate: <___% (typical: <5%)

---

### Privacy & Security
- [ ] **Data Privacy Compliance**
  - Metric: % of agents GDPR/CCPA compliant
  - Target: 100%
  - Audit frequency: ☐ Monthly ☐ Quarterly

- [ ] **Security Incident Rate**
  - Metric: Security incidents per month (data leaks, breaches)
  - Target: 0
  - Detection time: _____ minutes (typical: <15 min)

---

## Phase 5: Build Dashboards & Reporting (Week 5)

### Executive Dashboard (CEO, Leadership Team)

**Metrics to include:**
- [ ] Company-wide augmentation factor (revenue/employee, tasks/employee)
- [ ] AI agent count and coverage (% of processes automated)
- [ ] Overall automation rate and accuracy
- [ ] Cost savings from AI (vs. hiring more people)
- [ ] Top 5 highest-impact AI agents (by business value)
- [ ] Governance red flags (bias, privacy violations, escalations)

**Update frequency:** Weekly  
**Access:** Executive team  
**Tool:** _____________________________ (Tableau, Looker, custom dashboard)

---

### Function-Specific Dashboards (Department Heads)

**Create dashboards for:**
- [ ] Sales (lead scoring accuracy, deal velocity, augmentation factor)
- [ ] Finance (invoice automation, forecast accuracy, close time)
- [ ] Engineering (velocity, bug density, test coverage)
- [ ] Marketing (content output, engagement rates, SEO)
- [ ] CS (automation rate, response time, CSAT)
- [ ] HR (time-to-hire, candidate quality, engagement)

**Update frequency:** Daily  
**Access:** Function leaders + their teams  
**Tool:** _____________________________

---

### AI Agent-Specific Dashboards (Agent Owners/DRIs)

**For each AI agent, track:**
- [ ] 8 universal KPIs (automation rate, accuracy, latency, cost, etc.)
- [ ] Agent-specific metrics (e.g., "contracts reviewed per hour" for legal agent)
- [ ] User feedback and satisfaction
- [ ] Learning velocity (improvement trends)
- [ ] Escalation reasons (categorized)

**Update frequency:** Real-time or hourly  
**Access:** Agent DRI, data team, engineering  
**Tool:** _____________________________

---

### Governance Dashboard (Legal, Compliance, Ethics Board)

**Metrics to include:**
- [ ] Bias/fairness metrics (demographic parity, equal opportunity)
- [ ] Privacy compliance status (GDPR, CCPA)
- [ ] Security incidents (count, severity, resolution time)
- [ ] Human validation rates (by decision type)
- [ ] Escalation SLA breaches
- [ ] Audit trail completeness

**Update frequency:** Daily  
**Access:** Governance team, legal, ethics board  
**Tool:** _____________________________

---

## Phase 6: Quarterly OKR Reviews & Iteration (Ongoing)

### Quarter 1 Review

**Date:** ___________________________  
**Attendees:** ___________________________

**Review each function's OKRs:**
- [ ] **Sales:** KR1: _____% achieved | KR2: _____% achieved | KR3: _____% achieved
- [ ] **Finance:** KR1: _____% achieved | KR2: _____% achieved | KR3: _____% achieved
- [ ] **Engineering:** KR1: _____% achieved | KR2: _____% achieved | KR3: _____% achieved
- [ ] **Marketing:** KR1: _____% achieved | KR2: _____% achieved | KR3: _____% achieved
- [ ] **CS:** KR1: _____% achieved | KR2: _____% achieved | KR3: _____% achieved
- [ ] **HR:** KR1: _____% achieved | KR2: _____% achieved | KR3: _____% achieved

**Overall Assessment:**
- Company augmentation factor: _____ (target: 1.3x by Q2)
- AI agent count: _____ (target: 10-20 by Q2)
- Governance metrics: All green ☐ Some yellow ☐ Any red ☐

---

### Identify What Worked & What Didn't

**What Worked:**
1. _____________________________________________________
2. _____________________________________________________
3. _____________________________________________________

**What Didn't Work:**
1. _____________________________________________________
2. _____________________________________________________
3. _____________________________________________________

**Adjustments for Q2:**
- [ ] Revise OKR targets (up or down based on learning)
- [ ] Add new KPIs (if gaps discovered)
- [ ] Remove unhelpful metrics (if not driving behavior)
- [ ] Improve data collection (if metrics unreliable)

---

### Set Q2 OKRs

**Repeat the process for each function:**
- [ ] Sales: New objective and 3 key results
- [ ] Finance: New objective and 3 key results
- [ ] Engineering: New objective and 3 key results
- [ ] Marketing: New objective and 3 key results
- [ ] CS: New objective and 3 key results
- [ ] HR: New objective and 3 key results

**Q2 Company-Wide Goal:** _____________________________

---

## Success Criteria

**After 3 months, you should have:**
- [x] 8 universal AI agent KPIs tracked for all agents
- [x] Augmentation factor calculated for 3-5 key roles
- [x] Function-specific OKRs set for 6 functions
- [x] Dashboards live for executives, functions, agents, governance
- [x] Q1 OKR review completed

**After 6 months, you should have:**
- [x] Augmentation factor >1.3x company-wide
- [x] All functions hitting 70%+ of their KRs
- [x] Governance metrics all green (no red flags)
- [x] OKR process operating smoothly (quarterly reviews)
- [x] Data-driven decisions on AI agent investments

---

## Common Pitfalls to Avoid

❌ **Vanity metrics** - Tracking AI usage without business impact  
✅ **Solution:** Always tie KPIs to business outcomes (revenue, costs, quality)

❌ **Too many metrics** - Tracking 50+ KPIs per agent  
✅ **Solution:** Start with 8 universal KPIs + 3-5 agent-specific KPIs

❌ **No governance KPIs** - Only tracking business metrics  
✅ **Solution:** Equally weight governance (bias, privacy, accountability)

❌ **Annual OKRs** - Too slow for AI pace  
✅ **Solution:** Quarterly OKRs with monthly check-ins

❌ **Agent-only metrics** - Ignoring human-AI collaboration  
✅ **Solution:** Augmentation factor measures combined human+AI output

---

## Resources

**Related Playbooks:**
- [AI-Native OKRs & KPIs](../../PLAYBOOKS/people-culture/ai-native-okrs-kpis.md) - Full framework
- [AI Governance & Risk](../../PLAYBOOKS/governance/ai-governance-risk-assessment.md) - Governance metrics
- [Maturity Model](../../PLAYBOOKS/foundation/solid-ai-maturity-model.md) - Maturity KPIs

**Templates:**
- [OKR Template](../TEMPLATES/okr-template.yaml) - Copy-paste OKR format
- [AI Agent Integration Checklist](./ai-agent-integration.md) - Agent deployment
- [Governance & Ethics Review](./governance-ethics-review.md) - Governance process

**Dashboarding Tools:**
- Tableau, Looker, Grafana, Metabase, custom dashboards

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Framework:** SOLID.AI
