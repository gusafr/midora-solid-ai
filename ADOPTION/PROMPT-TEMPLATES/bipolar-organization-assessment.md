# Bipolar Organization Assessment Prompt Template

**When to Use:** Before starting organization-wide AI transformation (especially for SMEs with 50+ employees)

**Purpose:** Identify friction between IT practices and business practices to determine pilot function and transformation sequence

**Level:** Intermediate-Level Analysis

**Typical User:** CEO, COO, CTO, Transformation Lead

---

## Overview

**The Bipolar Organization Problem:**

Many organizations operate at two speeds:
- **IT/Engineering:** Waterfall planning, 12-month roadmaps, committee approvals, risk-averse, legacy systems
- **Business (Sales/Marketing/Finance):** Agile, weekly iterations, individual autonomy, fast experimentation, latest AI tools

This creates friction:
- IT can't keep up with business demands ("Why does it take 6 months to add a CRM field?")
- Business works around IT (shadow IT, spreadsheets, personal AI subscriptions)
- AI transformation fails if started in wrong function (IT rigidity kills momentum)

**Solution:** Assess coherence between IT and business practices, then:
- **High Coherence (score >20/25):** Start transformation anywhere (low friction)
- **Moderate Coherence (score 15-19):** Start in business function (Finance/Sales/HR), then IT
- **Low Coherence (score <15):** Start in business function, postpone IT transformation until culture shifts

**See:** [Whole-Organization Transformation — Bipolar Organization Section](../DOCS/09-whole-organization-transformation.md)

---

## Prompt Template

### **System Prompt**

```
You are a Bipolar Organization Assessment Analyst.

Your role is to assess organizational coherence by comparing IT/Engineering practices with Business Function practices (Finance, Sales, Marketing, HR, Operations).

You will evaluate 5 dimensions:
1. **Planning Horizon:** Waterfall (12+ month roadmaps) vs. Agile (weekly/monthly iterations)
2. **Decision Speed:** Committee-driven (30+ days) vs. Individual autonomy (same-day decisions)
3. **Technology Adoption:** Legacy systems (5+ year cycles) vs. Latest tools (monthly experimentation)
4. **Data Access:** Gated (IT controls access) vs. Self-serve (business users access via BI/APIs)
5. **Risk Tolerance:** Minimize change (99.9% uptime) vs. Experiment fast (fail fast, iterate)

For each dimension, you will score:
- **1 = High friction** (IT and business operate completely differently)
- **2 = Moderate friction** (some misalignment)
- **3 = Neutral** (neither aligned nor misaligned)
- **4 = Low friction** (mostly aligned)
- **5 = Aligned** (IT and business operate the same way)

**Total Score Interpretation:**
- **20-25:** High coherence — low friction, can start AI transformation in any function
- **15-19:** Moderate coherence — start in business function (Finance/Sales/HR) first, then IT
- **<15:** Low coherence — high friction, start in business function, postpone IT until culture shifts

Your output should be a structured assessment with:
- Scorecard (5 dimensions, 1-5 score each)
- Total coherence score
- Friction zones (where IT and business clash)
- Recommended pilot function (Finance, Sales, HR, IT, or other)
- Transformation sequence (which functions to transform in what order)
- Risks & mitigation

Tone: Professional, data-driven, diplomatic (don't blame IT or business — diagnose system)
Format: Markdown with clear sections
```

---

### **User Prompt (Fill-In Template)**

```
Assess organizational coherence (IT practices vs. Business practices) for:

**Organization:** {COMPANY_NAME}
**Size:** {EMPLOYEE_COUNT} employees
**Industry:** {INDUSTRY}
**Revenue:** ${REVENUE}

---

## Dimension 1: Planning Horizon

**IT/Engineering Practices:**
- {IT_PLANNING_DESCRIPTION}
  Example: "Annual roadmap (12 months), quarterly releases, waterfall sprints (plan → build → test → deploy over 3 months)"

**Business Function Practices (Finance/Sales/Marketing/HR):**
- {BUSINESS_PLANNING_DESCRIPTION}
  Example: "Weekly sprint planning, monthly OKRs, continuous experimentation (A/B tests, campaign tweaks)"

**Coherence Score (1-5):** {SCORE_1}
- 1 = IT plans 12+ months ahead, business plans weekly (high friction)
- 5 = Both plan on same horizon (aligned)

---

## Dimension 2: Decision Speed

**IT/Engineering Practices:**
- {IT_DECISION_DESCRIPTION}
  Example: "New tool requires CAB (Change Advisory Board) approval, 30-60 day process, committee of 5 people"

**Business Function Practices:**
- {BUSINESS_DECISION_DESCRIPTION}
  Example: "Sales manager can approve new lead gen tool same-day (up to $5K/month), no committee"

**Coherence Score (1-5):** {SCORE_2}
- 1 = IT decisions take 30+ days, business decisions same-day (high friction)
- 5 = Both decide at same speed (aligned)

---

## Dimension 3: Technology Adoption

**IT/Engineering Practices:**
- {IT_TECH_DESCRIPTION}
  Example: "ERP system from 2015 (9 years old), CRM from 2018 (6 years old), no AI tools deployed"

**Business Function Practices:**
- {BUSINESS_TECH_DESCRIPTION}
  Example: "Marketing uses ChatGPT (2024), Jasper (2024), HubSpot AI features (2024), Sales uses Gong (2023)"

**Coherence Score (1-5):** {SCORE_3}
- 1 = IT uses legacy systems (5+ years), business uses latest AI tools (high friction)
- 5 = Both use modern tools (aligned)

---

## Dimension 4: Data Access

**IT/Engineering Practices:**
- {IT_DATA_DESCRIPTION}
  Example: "All data access via IT tickets, SQL queries require DBA approval (3-5 day SLA), no self-serve BI"

**Business Function Practices:**
- {BUSINESS_DATA_DESCRIPTION}
  Example: "Finance uses Tableau (self-serve dashboards), Sales uses Salesforce reports (no IT involved), Marketing uses Google Analytics"

**Coherence Score (1-5):** {SCORE_4}
- 1 = IT gates all data, business wants self-serve (high friction)
- 5 = Both have self-serve data access (aligned)

---

## Dimension 5: Risk Tolerance

**IT/Engineering Practices:**
- {IT_RISK_DESCRIPTION}
  Example: "Zero tolerance for downtime (99.9% SLA), all changes require testing in staging (2-week cycle), no production hotfixes"

**Business Function Practices:**
- {BUSINESS_RISK_DESCRIPTION}
  Example: "Sales experiments with new lead gen tools monthly (10% fail, 90% iterate), Marketing runs A/B tests weekly (50% win rate acceptable)"

**Coherence Score (1-5):** {SCORE_5}
- 1 = IT avoids all risk, business experiments constantly (high friction)
- 5 = Both have same risk tolerance (aligned)

---

## Additional Context

**Symptoms of Friction (if any):**
- {SYMPTOM_1}
  Example: "Sales built their own lead database in Google Sheets because CRM too slow to update"
  
- {SYMPTOM_2}
  Example: "Marketing uses personal ChatGPT accounts because IT banned AI tools (security concerns)"
  
- {SYMPTOM_3}
  Example: "Finance waits 2 weeks for IT to export data from ERP → they demand self-serve BI"

**Recent Conflicts:**
- {CONFLICT_1}
  Example: "IT shut down Marketing's AI chatbot pilot (security risk), Marketing escalated to CEO"
  
- {CONFLICT_2}
  Example: "Sales wants Salesforce Einstein AI, IT says 'not in roadmap until 2026'"

**Leadership Alignment:**
- **CTO/CIO view:** {CTO_VIEW}
  Example: "We need stability, security, compliance — can't move fast and break things"
  
- **CMO/VP Sales view:** {BUSINESS_VIEW}
  Example: "We need AI now to compete — waiting 2 years means we lose market share"

Now generate the Bipolar Organization Assessment.
```

---

### **Expected Output (Example)**

```markdown
# Bipolar Organization Assessment: TechCorp Manufacturing

**Assessed by:** Bipolar Organization Analyst  
**Date:** November 2025  
**Organization:** TechCorp Manufacturing  
**Size:** 120 employees  
**Industry:** Industrial equipment manufacturing  
**Revenue:** $25M/year  

---

## 📊 Coherence Scorecard

| Dimension | IT Practices | Business Practices | Score (1-5) | Friction Level |
|-----------|--------------|-----------------------|-------------|----------------|
| **Planning Horizon** | Annual roadmap, quarterly releases | Weekly sprints, monthly OKRs | **2** | High friction 🔴 |
| **Decision Speed** | CAB approval, 30-60 days | Manager approval, same-day | **1** | High friction 🔴 |
| **Technology Adoption** | ERP (2015), CRM (2018) | ChatGPT, Gong, HubSpot AI (2024) | **1** | High friction 🔴 |
| **Data Access** | IT tickets, 3-5 day SLA | Self-serve (Tableau, Salesforce) | **3** | Moderate friction 🟡 |
| **Risk Tolerance** | 99.9% uptime, no hotfixes | Monthly experiments, 50% fail rate OK | **2** | High friction 🔴 |

**Total Coherence Score:** **9/25** — **Low Coherence, High Friction** 🔴

---

## 🔥 Friction Zones (Where IT and Business Clash)

### **1. Technology Adoption (Score: 1/5)**

**Problem:**
- IT uses legacy ERP (2015, 9 years old) and CRM (2018, 6 years old)
- Business functions adopted AI tools in 2024 (ChatGPT, Jasper, Gong, HubSpot AI)
- **Gap:** 6-9 year technology lag between IT and business

**Symptoms:**
- Sales built lead database in Google Sheets (CRM too slow to update)
- Marketing uses personal ChatGPT accounts (IT banned AI tools for security)
- Finance demands BI tool (waiting 2 weeks for IT to export data from ERP is unacceptable)

**Impact:** Business works around IT (shadow IT), IT loses credibility

---

### **2. Decision Speed (Score: 1/5)**

**Problem:**
- IT requires Change Advisory Board (CAB) approval for new tools (30-60 day process)
- Business managers approve tools same-day (up to $5K/month)
- **Gap:** 30+ days vs. same-day decisions

**Symptoms:**
- Sales wanted Salesforce Einstein AI → IT said "not in roadmap until 2026" → Sales escalated to CEO
- Marketing launched AI chatbot pilot → IT shut it down (security risk) → Marketing furious

**Impact:** Business perceives IT as blocker, not enabler

---

### **3. Planning Horizon (Score: 2/5)**

**Problem:**
- IT plans 12 months ahead (annual roadmap, quarterly releases)
- Business plans weekly (sprints) and monthly (OKRs)
- **Gap:** 12 months vs. 1 week/month

**Symptoms:**
- By the time IT delivers feature (6 months later), business requirements have changed
- Business feels "IT is always 6 months behind"

**Impact:** IT delivers work that's no longer valuable

---

### **4. Risk Tolerance (Score: 2/5)**

**Problem:**
- IT minimizes risk (99.9% uptime, no production hotfixes, 2-week staging cycle)
- Business experiments constantly (monthly tool trials, 50% fail rate acceptable)
- **Gap:** Zero-risk culture vs. fail-fast culture

**Symptoms:**
- IT won't allow AI tools (security risk, no vendor assessment yet)
- Business willing to try AI tools with 80% confidence (not 99.9%)

**Impact:** Business moves faster than IT can approve → shadow IT proliferates

---

### **5. Data Access (Score: 3/5) — Moderate Friction**

**Problem:**
- IT gates some data (SQL queries require DBA approval, 3-5 day SLA)
- But business has self-serve for some tools (Tableau, Salesforce reports, Google Analytics)
- **Gap:** Partial self-serve (better than full gating, but still friction)

**Symptoms:**
- Finance uses Tableau (good), but can't access ERP data without IT ticket (frustrating)

**Impact:** Less friction than other dimensions, but still slows business

---

## 🎯 Recommended Pilot Function

### **Finance (Recommended First)**

**Why Finance?**
1. **Predictable processes:** AP, AR, expense management, month-end close (structured, rule-based)
2. **Clear ROI metrics:** Invoice processing time, DSO, month-end close time (easy to measure success)
3. **Low IT dependency:** Finance can pilot AI tools (QuickBooks AI, Bill.com, Expensify) without IT infrastructure
4. **High pain:** Finance waits 2 weeks for IT to export ERP data → desperate for self-serve

**Expected Impact:**
- Invoice processing: 5 days → <24h
- Month-end close: 15 days → <5 days
- Finance team time on data entry: 60% → <20%
- **Proof point:** "Finance transformed in 3 months without IT roadmap changes"

---

### **Why NOT IT?** (Postpone Until Phase 2-3)

**Reasons to delay IT transformation:**
1. **Low coherence score (9/25):** IT culture is rigid (99.9% uptime, CAB approvals, legacy systems) — not ready for AI experimentation
2. **Business frustration:** If IT transformation fails, business loses faith in entire initiative
3. **Change takes time:** IT needs 6-12 months to shift from waterfall → agile, committee → autonomy, legacy → modern

**Recommendation:** Transform Finance → Sales → HR first (12 months), THEN tackle IT after business success builds momentum

---

## 🗺️ Transformation Sequence (24 Months)

### **Phase 0: Assessment (Month 1-2)**
- ✅ Complete this bipolar assessment
- ✅ Choose pilot function: **Finance** (low IT dependency, clear ROI)
- ✅ Set 24-month goals (revenue, headcount, G&A %, AI agents deployed)

### **Phase 1: Finance Pilot (Month 3-5)**
- Deploy 6 AI agents: ExpenseCategorizer, InvoiceProcessor, ReconciliationBot, FinancialReporting, BudgetForecaster, ComplianceMonitor
- Target: Invoice processing <24h, month-end close <5 days
- **Key:** Do this WITHOUT IT involvement (use SaaS tools: Bill.com, QuickBooks AI, Expensify)

### **Phase 2: Expand to Sales + HR (Month 6-12)**
- **Sales:** LeadQualifier, EmailSequencer, MeetingPrep, ProposalGenerator, DealCoordinator
- **HR:** ResumeScreener, OnboardingGuide, PerformanceTracker, BenefitsAdvisor
- **Key:** Prove AI works in 3 functions (Finance, Sales, HR) before touching IT

### **Phase 3: IT Transformation (Month 13-18)**
- **Only after business success** → IT sees proof AI works
- Start IT agile transformation: Waterfall → sprints, CAB → individual autonomy, legacy → modern tools
- Deploy IT AI agents: TicketTriager, SecurityMonitor, BackupCoordinator, CodeReviewer

### **Phase 4: Whole-Org (Month 19-24)**
- Operations, Marketing, Customer Success
- Cross-functional coordinators (RevenueOps, FinOps, TalentOps)

---

## ⚠️ Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **IT blocks Finance pilot** ("Not approved, security risk") | High | High | CEO mandate: "Finance can pilot SaaS AI tools without IT approval (use approved vendors: Bill.com, QuickBooks)" |
| **Finance pilot fails** (AI accuracy <80%) | Medium | High | Run parallel for 1 month (AI + human), validate >90% accuracy before going live |
| **IT feels sidelined** ("Why didn't you ask us?") | High | Medium | Include CTO in steering committee, explain: "We're starting simple (Finance SaaS tools), IT transformation comes later (Phase 3)" |
| **Business expectations too high** ("AI will automate 90% in 3 months") | Medium | Medium | Set realistic goals: 60% automation in 6 months (not 90% in 3) |
| **Shadow IT proliferates** (every function buys own AI tools) | High | Medium | Create "approved AI vendor list" (security vetted), centralize procurement |

---

## 📈 Success Criteria (6 Months)

| Metric | Baseline | Target | Month 3 | Month 6 |
|--------|----------|--------|---------|---------|
| **Finance:** Invoice processing time | 5 days | <24h | ___ | ___ |
| **Finance:** Month-end close time | 15 days | <5 days | ___ | ___ |
| **Sales:** Lead response time | 2 hours | <5min | ___ | ___ |
| **HR:** Time-to-fill open roles | 45 days | <30 days | ___ | ___ |
| **IT Friction:** Coherence score | 9/25 | 15+/25 | ___ | ___ |
| **Organization:** AI agents deployed | 0 | 15-20 | ___ | ___ |

---

## 💡 Key Insights

### **Why This Matters:**

1. **Starting in IT would fail:** Low coherence (9/25) means IT not ready for AI experimentation — rigid culture would kill pilot
2. **Finance is safe bet:** Low IT dependency, clear ROI, high pain → quick win builds momentum
3. **Business success changes IT:** After Finance/Sales/HR prove AI works, IT will want to join (FOMO)
4. **Culture shift takes 12-24 months:** Can't force IT to change overnight — let business success pull IT forward

### **What to Communicate to Leadership:**

- **To CEO:** "We have organizational friction (IT slow, business fast). Start transformation in Finance (safe, high ROI), then expand. Don't start in IT (would fail)."
- **To CTO:** "We're not sidelining IT — we're building proof points in Finance first, then bringing IT in Phase 3 (with budget, executive support, proven AI patterns)."
- **To CFO/VP Sales/VP HR:** "You get to pilot AI first (Finance, Sales, HR). Prove it works, then we'll transform IT."

---

## 📚 Next Steps

1. **Get CEO buy-in:** Present this assessment to executive team
2. **Pilot Finance (Month 3-5):** Deploy 6 AI agents, target invoice processing <24h
3. **Track coherence score:** Re-assess every 6 months (goal: 9 → 15 → 20 over 24 months)
4. **IT transformation (Month 13+):** Only after Finance/Sales/HR prove success

---

## 📖 Resources

**Documentation:**
- [Whole-Organization Transformation](../DOCS/09-whole-organization-transformation.md)
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)
- [Organizational Model](../DOCS/03-organizational-model.md)

**Playbooks:**
- [SME Transformation](../PLAYBOOKS/by-stage/sme-transformation.md)
- [Finance Playbook](../PLAYBOOKS/by-sector/business-functions/finance.md)

**Checklists:**
- [SME Transformation Roadmap](../ADOPTION/CHECKLISTS/sme-transformation-roadmap.md)

---

**Assessment Completed:** November 2025  
**Coherence Score:** 9/25 (Low Coherence, High Friction)  
**Recommendation:** Start in Finance, postpone IT until Phase 3 (Month 13+)
```

---

## Configuration Instructions

### **Step 1: Gather Organizational Data**

Before running assessment, collect:
- [ ] **IT Practices:** Planning cycles, decision approval process, technology stack age, data access policies, risk tolerance
- [ ] **Business Practices:** Planning cycles, decision speed, tools adopted (especially AI), data access (self-serve?), experimentation culture
- [ ] **Friction Symptoms:** Shadow IT, recent conflicts (IT vs. business), escalations to CEO
- [ ] **Leadership Views:** What does CTO think? What does CMO/VP Sales think?

---

### **Step 2: Score Each Dimension**

Use this rubric:

| Score | Planning Horizon | Decision Speed | Technology Adoption | Data Access | Risk Tolerance |
|-------|------------------|----------------|---------------------|-------------|----------------|
| **1** | IT: 12+ mo, Biz: weekly | IT: 30+ days, Biz: same-day | IT: 5+ yr old, Biz: latest | IT: gated, Biz: wants self-serve | IT: zero risk, Biz: fail fast |
| **3** | Both quarterly | IT: 1 week, Biz: same-day | IT: 2-3 yr old, Biz: 1-2 yr | Partial self-serve | IT: low risk, Biz: moderate experiments |
| **5** | Both use same horizon | Both same-day | Both use latest tools | Both self-serve | Both same risk tolerance |

---

### **Step 3: Interpret Total Score**

- **20-25 (High Coherence):** Low friction → Start AI transformation anywhere (Finance, Sales, IT — all work)
- **15-19 (Moderate Coherence):** Moderate friction → Start in business function (Finance/Sales/HR), then IT
- **<15 (Low Coherence):** High friction → Start in business function, postpone IT until culture shifts

---

### **Step 4: Communicate Results**

- [ ] **To CEO:** "Here's where friction exists, here's recommended pilot function, here's why"
- [ ] **To CTO:** "We're not blaming IT — we're diagnosing system. IT transformation comes later (with support, budget, proof points)"
- [ ] **To Business Leaders:** "You get to pilot first — prove AI works, then we expand"

---

## 📚 Resources

**Documentation:**
- [Whole-Organization Transformation](../DOCS/09-whole-organization-transformation.md)
- [Organizational Model](../DOCS/03-organizational-model.md)
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)

**Checklists:**
- [SME Transformation Roadmap](../ADOPTION/CHECKLISTS/sme-transformation-roadmap.md)

**Playbooks:**
- [SME Transformation](../PLAYBOOKS/by-stage/sme-transformation.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
