# AI Maturity Assessment Checklist

**Purpose:** Assess your organization's AI maturity level (L0-L5) and create a transformation roadmap

**Framework:** SOLID.AI Maturity Model | **Version:** 1.0  
**Reference:** [Maturity Model Playbook](../../PLAYBOOKS/foundation/solid-ai-maturity-model.md)

---

## Quick Assessment (15 minutes)

### Step 1: Score Each Dimension (0-100)

Rate your organization on each dimension using the criteria below:

#### 1. Technology & Infrastructure (____/100)

- [ ] **0-20:** Siloed systems, manual integration, no AI infrastructure
- [ ] **21-40:** Point AI tools (ChatGPT, Copilot), no integration
- [ ] **41-60:** AI platform (APIs), basic integration (5-10 systems), data warehouse
- [ ] **61-80:** Data spine operational (20+ systems), automation mesh, observability
- [ ] **81-95:** Full mesh integration, intelligent data spine, self-healing systems
- [ ] **96-100:** Proprietary AI infrastructure, ecosystem integration

**Your Score:** ____/100

**Key Questions:**
- How many systems publish to a central data spine? (0 / 1-5 / 6-20 / 21+)
- What % of processes have automation? (0-5% / 5-15% / 15-35% / 35-60% / 60-80% / 80%+)
- Do you have real-time event streaming? (No / Planning / Pilot / Production / Advanced)

---

#### 2. Data & Analytics (____/100)

- [ ] **0-20:** Data in silos, manual reports, no single source of truth
- [ ] **21-40:** Data warehouse, BI dashboards, manual analytics
- [ ] **41-60:** Entity models defined, basic data contracts, weekly reporting
- [ ] **61-80:** Real-time data spine, event streaming, AI-driven insights
- [ ] **81-95:** Predictive analytics, continuous learning loops, automated insights
- [ ] **96-100:** AI-curated data, synthetic data generation, self-improving models

**Your Score:** ____/100

**Key Questions:**
- Can you correlate customer journey across all touchpoints? (No / Partial / Yes / Real-time)
- How long from event to insight? (Days / Hours / Minutes / Seconds)
- Do AI agents learn from feedback? (No / Quarterly / Monthly / Weekly / Daily)

---

#### 3. AI Capabilities (____/100)

- [ ] **0-20:** No AI use, traditional automation (RPA, scripts)
- [ ] **21-40:** 1-3 AI pilots, pre-built tools (ChatGPT), no custom models
- [ ] **41-60:** 5-10 AI use cases, API integrations, basic prompt engineering
- [ ] **61-80:** 20+ AI agents, multi-model orchestration, fine-tuned models
- [ ] **81-95:** 50+ AI agents, autonomous coordination, continuous learning
- [ ] **96-100:** Custom foundation models, novel architectures, research contributions

**Your Score:** ____/100

**Key Questions:**
- How many AI agents in production? (0 / 1-3 / 4-10 / 11-30 / 31-100 / 100+)
- Do you use multiple AI models? (No / 1 model / 2-3 / 5+ / Custom)
- Can agents coordinate with each other? (No / Manual / Semi / Autonomous)

---

#### 4. Governance & Risk (____/100)

- [ ] **0-20:** No AI governance, traditional IT policies only
- [ ] **21-40:** Ad hoc governance, no formal policies, reactive
- [ ] **41-60:** Written policies, AI council formed, manual reviews
- [ ] **61-80:** Automated risk scoring, tiered reviews, real-time monitoring
- [ ] **81-95:** Self-regulating governance (AI monitors AI), predictive risk
- [ ] **96-100:** Industry-leading governance, standards contributions

**Your Score:** ____/100

**Key Questions:**
- Do you have AI governance policies? (No / Draft / Approved / Enforced / Automated)
- How do you assess AI risk? (Don't / Manual / Scorecard / Automated / Predictive)
- Do you monitor AI in production? (No / Manual / Dashboards / Alerts / Self-healing)

---

#### 5. Human-AI Collaboration (____/100)

- [ ] **0-20:** Humans only, no AI tools
- [ ] **21-40:** AI assists individuals (Copilot, ChatGPT), no process integration
- [ ] **41-60:** AI embedded in workflows, human-in-loop, hybrid teams forming
- [ ] **61-80:** AI-native processes, clear handoffs, trust established
- [ ] **81-95:** Seamless human-AI teams, AI autonomy with oversight, high trust
- [ ] **96-100:** AI as strategic partner, augments leadership

**Your Score:** ____/100

**Key Questions:**
- What % of employees use AI daily? (0-20% / 21-50% / 51-80% / 81-95% / 95%+)
- Are AI outputs trusted or always double-checked? (Always check / Usually check / Spot check / Trust)
- Do teams include AI agents as "members"? (No / Informal / Formal / Equals)

---

#### 6. Organizational Capacity (____/100)

- [ ] **0-20:** Traditional org structure, no AI roles, functional silos
- [ ] **21-40:** 1-2 AI enthusiasts, no formal program, grassroots only
- [ ] **41-60:** AI training program, 50%+ trained, 2-3 dedicated AI roles
- [ ] **61-80:** 80%+ trained, AI in job descriptions, cross-functional AI teams
- [ ] **81-95:** 95%+ proficient, roles redefined, AI-native culture
- [ ] **96-100:** AI-native DNA, thought leadership, talent magnet

**Your Score:** ____/100

**Key Questions:**
- What % of employees AI-trained? (0-20% / 21-50% / 51-80% / 81-95% / 95%+)
- Do you have dedicated AI roles? (No / 1-2 / 3-10 / 11-30 / 30+)
- Is AI in performance reviews? (No / Informal / Tracked / Formal KPI / Core expectation)

---

#### 7. Process Maturity (____/100)

- [ ] **0-20:** Undocumented processes, tribal knowledge, high variation
- [ ] **21-40:** Some documentation, manual execution, no AI
- [ ] **41-60:** SIPOC mapped (5-10 processes), AI assisting execution
- [ ] **61-80:** 20+ processes AI-native, integration contracts, automation mesh
- [ ] **81-95:** 50+ processes optimized, continuous improvement loops
- [ ] **96-100:** All processes AI-first design, autonomous optimization

**Your Score:** ____/100

**Key Questions:**
- How many processes SIPOC-mapped? (0 / 1-5 / 6-20 / 21-50 / 50+)
- Are processes designed for AI or retrofitted? (Retrofitted / Hybrid / AI-first)
- Do you have integration contracts? (No / 1-5 / 6-20 / 21-50 / 50+)

---

#### 8. Business Impact (____/100)

- [ ] **0-20:** No AI impact, baseline performance
- [ ] **21-40:** Anecdotal benefits, no ROI measurement
- [ ] **41-60:** 2-3x ROI, +20% revenue/employee, localized impact
- [ ] **61-80:** 5-10x ROI, +50-100% revenue/employee, company-wide
- [ ] **81-95:** 15-25x ROI, +150-300% revenue/employee, competitive moat
- [ ] **96-100:** Market leader, AI products, ecosystem influence

**Your Score:** ____/100

**Key Questions:**
- What's your AI ROI? (Unknown / Break-even / 2-3x / 5-10x / 15x+)
- Revenue per employee vs. industry? (Below / Average / +20-50% / +50-100% / +100%+)
- Is AI a competitive advantage? (No / Minor / Significant / Core / Defining)

---

### Step 2: Calculate Your Maturity Level

```
TOTAL SCORE: _____ / 800
AVERAGE SCORE: _____ / 100 (divide total by 8)
```

**Your Maturity Level:**

| Average Score | Level | Description |
|---------------|-------|-------------|
| 0-20 | **Level 0: Traditional** | Pre-AI, manual processes dominate |
| 21-40 | **Level 1: Experimentation** | AI pilots, no enterprise strategy |
| 41-60 | **Level 2: Adoption** | AI strategy defined, 50%+ trained, measurable ROI |
| 61-80 | **Level 3: Integration** | Data spine operational, 20+ agents, AI-native processes |
| 81-95 | **Level 4: Optimization** | 50+ agents, continuous learning, strategic AI |
| 96-100 | **Level 5: Leadership** | Industry pioneer, AI products, ecosystem play |

---

## Step 3: Identify Gaps

**Find dimensions >10 points below your average:**

```
Example:
Average score: 55 (Level 2)

Dimensions:
  Technology: 60 ✅
  Data: 58 ✅
  AI Capabilities: 52 ✅
  Governance: 40 ⚠️ (15 points below - TOP PRIORITY)
  Human-AI: 62 ✅
  Org Capacity: 48 🔴 (7 points below - SECONDARY)
  Process: 56 ✅
  Business Impact: 64 ✅
```

**Your Gaps:**

1. **Biggest gap** (>10 points below average): _________________________
2. **Secondary gap** (5-10 points below): _________________________
3. **Tertiary gap** (5-10 points below): _________________________

---

## Step 4: Create Your 6-12 Month Action Plan

### Priority 1: Close Biggest Gap

**Gap:** _________________________  
**Current Score:** ____  
**Target Score (6 months):** ____

**3-5 Key Actions:**
1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________
4. _________________________________________________________________
5. _________________________________________________________________

**Owner (DRI):** _________________________  
**Budget Needed:** $_____________  
**Success Metrics:** _________________________________________________________________

---

### Priority 2: Close Secondary Gap

**Gap:** _________________________  
**Current Score:** ____  
**Target Score (6 months):** ____

**3-5 Key Actions:**
1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

**Owner (DRI):** _________________________

---

### Priority 3: Maintain Strengths

**Strongest Dimension:** _________________________  
**Current Score:** ____

**Actions to maintain/improve:**
1. _________________________________________________________________
2. _________________________________________________________________

---

## Step 5: Set Quarterly Milestones

### Q1 (Next 3 months)
- [ ] _________________________________________________________________ (Priority 1, Action 1)
- [ ] _________________________________________________________________ (Priority 1, Action 2)
- [ ] _________________________________________________________________ (Priority 2, Action 1)

**Target scores:** Priority 1: ____ → ____  /  Priority 2: ____ → ____

---

### Q2 (Months 4-6)
- [ ] _________________________________________________________________ (Priority 1, Action 3-5)
- [ ] _________________________________________________________________ (Priority 2, Action 2-3)
- [ ] _________________________________________________________________ (Begin Priority 3)

**Target scores:** Priority 1: ____ → ____  /  Priority 2: ____ → ____

---

### Q3-Q4 (Next 6-12 months) - Optional Long-Term Planning
- [ ] Level up to next maturity level (Current: L___ → Target: L___)
- [ ] _________________________________________________________________ (Major capability build)
- [ ] _________________________________________________________________ (Organizational transformation)

---

## Step 6: Monthly Check-Ins

**Repeat this assessment monthly** (lightweight version):
- Re-score only your gap dimensions (Priority 1, 2, 3)
- Track progress: Are scores improving?
- Adjust actions if not making progress
- Celebrate wins when scores increase

**Monthly Tracking:**

| Month | Priority 1 Score | Priority 2 Score | Average Score | Notes |
|-------|------------------|------------------|---------------|-------|
| Baseline | ____ | ____ | ____ | Starting point |
| Month 1 | ____ | ____ | ____ | |
| Month 2 | ____ | ____ | ____ | |
| Month 3 | ____ | ____ | ____ | Q1 review |
| Month 4 | ____ | ____ | ____ | |
| Month 5 | ____ | ____ | ____ | |
| Month 6 | ____ | ____ | ____ | Q2 review - reassess all 8 dimensions |

---

## Resources for Each Gap

### If Governance is your gap:
→ Read: [Governance & Risk Assessment](../../PLAYBOOKS/governance/ai-governance-risk-assessment.md)  
→ Use: [Governance Checklist](governance-ethics-review.md)

### If Organizational Capacity is your gap:
→ Read: [Learning & Development](../../PLAYBOOKS/people-culture/ai-learning-development.md)  
→ Read: [Organizational Scalability](../../PLAYBOOKS/people-culture/organizational-scalability.md)

### If Technology/Data is your gap:
→ Read: [Data Spine Structuring](../../PLAYBOOKS/implementation/data-spine-structuring-governance.md)  
→ Use: [Data Spine Checklist](data-spine-implementation.md)

### If AI Capabilities is your gap:
→ Read: [Implementing AI Agents](../../PLAYBOOKS/implementation/implementing-ai-agents-practical-guide.md)  
→ Use: [AI Agent Integration Checklist](ai-agent-integration.md)

### If Process Maturity is your gap:
→ Read: [Process Mapping (SIPOC)](../../PLAYBOOKS/implementation/process-mapping-sipoc-integration.md)

### If Business Impact is your gap:
→ Read: [OKRs & KPIs](../../PLAYBOOKS/people-culture/ai-native-okrs-kpis.md)  
→ Read: [Data Analytics & Insights](../../PLAYBOOKS/implementation/data-spine-analytics-insights.md)

---

## Success Criteria

You've completed this assessment when:
- [x] All 8 dimensions scored
- [x] Maturity level determined (L0-L5)
- [x] Top 2-3 gaps identified
- [x] 6-month action plan created with owners and metrics
- [x] Q1 milestones defined
- [x] Monthly check-in cadence established

**Next Step:** Share this assessment with leadership and get buy-in for the action plan.

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Framework:** SOLID.AI
