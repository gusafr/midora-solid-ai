# Human-AI Collaboration Assessment Prompt Template

**When to Use:** Before deploying AI agents to a new function or process

**Purpose:** Determine where humans should lead, where AI should lead, and where they should collaborate

**Level:** Intermediate-Level Analysis

**Typical User:** Product Owner, Department Head, Transformation Lead

---

## Overview

Not all work should be automated. This prompt helps assess a process or function to determine the optimal Human-AI collaboration model:

1. **Human-Led, AI-Assisted:** Human makes decisions, AI provides data/recommendations (e.g., CFO sets strategy, AI forecasts scenarios)
2. **AI-Led, Human-Supervised:** AI executes tasks, human audits/overrides (e.g., AI categorizes expenses, human reviews monthly)
3. **Balanced Collaboration:** Human + AI work together in real-time (e.g., sales proposal: human writes narrative, AI generates pricing)
4. **Fully Human:** AI cannot add value (e.g., board-level strategy, creative vision, high-touch relationships)
5. **Fully AI:** Routine, high-volume, rule-based (e.g., invoice processing, lead qualification)

**See:** [Human-AI Collaboration Documentation](../DOCS/08-human-ai-collaboration.md)

---

## Prompt Template

### **System Prompt**

```
You are a Human-AI Collaboration Assessment Analyst.

Your role is to analyze a process or function and recommend the optimal collaboration model between humans and AI agents.

You will assess:
1. **Task Characteristics:** Is the work structured (rule-based) or unstructured (creative/strategic)?
2. **Volume:** How many transactions/tasks per day/month?
3. **Risk:** What's the impact of errors? (low = minor inconvenience, high = financial/legal/reputational damage)
4. **Variability:** Do tasks follow a pattern, or is every case unique?
5. **Human Strengths:** Where do humans excel? (creativity, empathy, judgment, relationships)
6. **AI Strengths:** Where does AI excel? (speed, consistency, pattern recognition, 24/7 availability)

Based on this assessment, you will recommend one of 5 collaboration models:

**Model 1: Human-Led, AI-Assisted**
- Human makes all decisions, AI provides data/insights/recommendations
- Example: CFO sets financial strategy, AI runs scenario forecasts
- When to use: Unstructured, high-stakes, requires human judgment

**Model 2: AI-Led, Human-Supervised**
- AI executes tasks autonomously, human audits/reviews periodically
- Example: AI categorizes expenses, human reviews monthly for errors
- When to use: Structured, high-volume, low-risk, but requires oversight

**Model 3: Balanced Collaboration**
- Human + AI work together in real-time, neither fully autonomous
- Example: Sales proposal (human writes narrative, AI generates pricing/terms)
- When to use: Semi-structured, moderate risk, benefits from both strengths

**Model 4: Fully Human**
- AI cannot add value or is inappropriate
- Example: Board-level strategy, creative vision, sensitive employee issues
- When to use: Unstructured, high-stakes, requires empathy/relationships

**Model 5: Fully AI**
- AI handles 100% of work, human rarely intervenes
- Example: Invoice processing, lead scoring, data backup
- When to use: Structured, high-volume, low-risk, routine

Your output should be a structured assessment report with:
- Process/function analyzed
- Task characteristics (structured/unstructured, volume, risk, variability)
- Recommended collaboration model (1-5)
- Rationale (why this model?)
- Implementation steps (how to deploy?)
- Risks & mitigation (what could go wrong?)

Tone: Professional, data-driven, actionable
Format: Markdown with clear sections
```

---

### **User Prompt (Fill-In Template)**

```
Assess the following process/function for Human-AI collaboration:

**Function/Process:** {FUNCTION_NAME}
Example: "Accounts Payable (invoice processing)"

**Description:** {PROCESS_DESCRIPTION}
Example: "Receive vendor invoices via email/portal → Extract data (amount, due date, vendor) → Categorize expense → Route for approval → Schedule payment"

**Current State:**
- **Who does this work today?** {CURRENT_TEAM}
  Example: "2 AP clerks (Low-Level), 1 AP manager (Intermediate-Level)"
  
- **Volume:** {VOLUME}
  Example: "150 invoices/month, peak 250/month during quarter-end"
  
- **Time spent:** {TIME_SPENT}
  Example: "AP clerks spend 60% of time on data entry, 20% on categorization, 20% on follow-up"

**Task Characteristics:**
- **Structured or Unstructured?** {STRUCTURED_LEVEL}
  Example: "Mostly structured (90% follow standard format), 10% require custom handling (missing fields, unclear vendor)"

- **Rule-based or Judgment-based?** {DECISION_TYPE}
  Example: "Rule-based categorization (travel = T&E, software = IT), but approval thresholds require manager judgment"

- **Variability:** {VARIABILITY}
  Example: "Low variability — 80% of invoices are recurring vendors (same format every month)"

**Risk Assessment:**
- **Impact of errors:** {ERROR_IMPACT}
  Example: "Medium risk — incorrect categorization causes budget variance (annoying but not catastrophic), duplicate payments cause financial loss (rare but serious)"

- **Compliance requirements:** {COMPLIANCE}
  Example: "Must retain invoices for 7 years (IRS requirement), must segregate duties (no one person can approve + pay)"

**Human Strengths Needed:**
- {HUMAN_STRENGTH_1}
  Example: "Judgment for unusual invoices (e.g., disputed charges, incorrect amounts)"
  
- {HUMAN_STRENGTH_2}
  Example: "Vendor relationship management (negotiate payment terms, resolve disputes)"

**AI Strengths Applicable:**
- {AI_STRENGTH_1}
  Example: "Fast data extraction from PDFs (OCR + NLP)"
  
- {AI_STRENGTH_2}
  Example: "Consistent categorization (95%+ accuracy if trained on historical data)"
  
- {AI_STRENGTH_3}
  Example: "24/7 availability (can process invoices overnight)"

**Current Pain Points:**
- {PAIN_POINT_1}
  Example: "Manual data entry takes 60% of AP clerk time (tedious, low-value)"
  
- {PAIN_POINT_2}
  Example: "Invoice processing time: 5 days (should be <24h to capture early payment discounts)"
  
- {PAIN_POINT_3}
  Example: "Error rate: 5% (incorrect categorization causes budget variance)"

**Desired Outcomes:**
- {OUTCOME_1}
  Example: "Reduce invoice processing time from 5 days to <24 hours"
  
- {OUTCOME_2}
  Example: "Free AP clerks from data entry → focus on vendor relationship management + exception handling"
  
- {OUTCOME_3}
  Example: "Improve categorization accuracy from 95% to >98%"

Now generate the Human-AI Collaboration Assessment.
```

---

### **Expected Output (Example)**

```markdown
# Human-AI Collaboration Assessment: Accounts Payable (Invoice Processing)

**Assessed by:** AI Collaboration Analyst  
**Date:** November 2025  
**Function:** Finance — Accounts Payable  

---

## 📊 Process Overview

**Process:** Accounts Payable (Invoice Processing)

**Description:**
1. Receive vendor invoices (email/portal)
2. Extract data (amount, due date, vendor, line items)
3. Categorize expense (travel, software, office supplies, etc.)
4. Route for approval (manager approves >$1K)
5. Schedule payment (ACH/check)

**Current Team:**
- 2 AP clerks (Low-Level): Data entry, categorization, follow-up
- 1 AP manager (Intermediate-Level): Approvals, vendor relationships, month-end close

**Volume:** 150 invoices/month (peak 250/month)

**Current Processing Time:** 5 days (median)

**Current Error Rate:** 5% (incorrect categorization)

---

## 🔍 Task Characteristics Analysis

| Dimension | Assessment | Score (1-5) | Notes |
|-----------|------------|-------------|-------|
| **Structured** | High | 4/5 | 90% of invoices follow standard format, 10% require custom handling |
| **Rule-Based** | High | 4/5 | Categorization follows clear rules (travel=T&E, software=IT), approvals threshold-based |
| **Volume** | High | 4/5 | 150-250 invoices/month = 7-12/day (high enough for automation ROI) |
| **Variability** | Low | 2/5 | 80% recurring vendors (same format), 20% one-time vendors (varied format) |
| **Risk (Errors)** | Medium | 3/5 | Incorrect categorization = budget variance (annoying), duplicate payment = financial loss (rare but serious) |
| **Human Judgment Needed** | Low | 2/5 | Most tasks rule-based, judgment only for exceptions (disputed charges, missing data) |

**Overall Automation Suitability:** **4.2/5** — High (good candidate for AI-led automation with human supervision)

---

## 🤖 Recommended Collaboration Model

### **Model 2: AI-Led, Human-Supervised**

**Rationale:**
- **High structure + high volume + low variability** = AI can handle 90%+ of invoices autonomously
- **Medium risk** = Requires human oversight (monthly audit), not full autonomy
- **Low judgment needed** = Rule-based categorization and approval routing don't require strategic thinking

**How It Works:**
1. **AI Agent (InvoiceProcessor-Agent, Low-Level) handles 90% of invoices:**
   - Extracts data from PDF/email (OCR + NLP)
   - Categorizes expense (trained on 2 years of historical data, 95%+ accuracy)
   - Routes for approval if >$1K
   - Schedules payment if approved

2. **Human AP Clerk (Low-Level) handles 10% of exceptions:**
   - Invoices with missing data (no amount, unclear vendor)
   - Disputed charges (vendor charged wrong amount)
   - First-time vendors (no historical data for categorization)

3. **Human AP Manager (Intermediate-Level) supervises monthly:**
   - Audits 10% sample of AI-processed invoices (check categorization accuracy)
   - Reviews exceptions handled by clerk
   - Manages vendor relationships (negotiate terms, resolve disputes)

**Expected Impact:**
- **Processing time:** 5 days → <24 hours (AI processes invoices same-day)
- **AP clerk time on data entry:** 60% → <10% (AI handles bulk, clerks handle exceptions)
- **AP clerk time on high-value work:** 40% → 90% (vendor relationships, exception handling, process improvement)
- **Categorization accuracy:** 95% → >98% (AI more consistent than humans)
- **Cost:** $500/month (AI agent subscription) vs. $8,000/month (additional AP clerk hire)

---

## 🛠️ Implementation Steps

### **Step 1: Deploy InvoiceProcessor-Agent (Week 1-2)**

- [ ] **Choose AI Tool:**
  - Option 1: Bill.com (invoice automation SaaS, $500/month)
  - Option 2: Stampli (invoice processing + approval workflows, $800/month)
  - Option 3: Custom (Zapier + ChatGPT API, $300/month)

- [ ] **Train AI Agent:**
  - Upload last 2 years of invoice history (categorization labels)
  - Train on your expense categories (T&E, IT, office supplies, etc.)
  - Test on 50 sample invoices, validate >95% accuracy

- [ ] **Set Escalation Rules:**
  - If invoice missing required fields (amount, vendor, due date) → escalate to AP clerk
  - If invoice >$1K → route to AP manager for approval
  - If vendor not in system → escalate to AP clerk (new vendor setup)

### **Step 2: Run Parallel for 1 Month (Week 3-6)**

- [ ] **AI processes invoices, humans verify:**
  - AI extracts data → Human reviews before saving
  - AI categorizes → Human approves categorization
  - Goal: Build trust, catch edge cases, refine AI training

- [ ] **Track Metrics:**
  - AI accuracy: ___% (target: >95%)
  - Time savings: ___ hours/week (target: 50%+ reduction in data entry)
  - Exceptions flagged: ___% (should be <10%)

### **Step 3: Increase AI Autonomy (Week 7+)**

- [ ] **AI processes invoices autonomously:**
  - 90%+ of invoices fully automated (no human review)
  - <10% escalated to humans for exceptions

- [ ] **Human shifts to supervision:**
  - AP clerk: Handle exceptions only (10% of invoices)
  - AP manager: Monthly audit (review 10% sample of AI-processed invoices)

---

## ⚠️ Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **AI categorization error** | Medium | Medium | Human audits 10% sample monthly, AI learns from corrections |
| **Duplicate payment** | Low | High | AI flags duplicates (same vendor + amount + due date), requires human approval |
| **Vendor relationship damage** | Low | Medium | Human AP manager still owns vendor relationships (AI doesn't interact with vendors) |
| **Compliance violation** | Low | High | AI retains invoices for 7 years (IRS requirement), segregation of duties enforced (AI can't approve + pay) |
| **AP clerks fear job loss** | High | Medium | Reframe: AI handles tedious work, clerks upskill to vendor management (career growth) |

---

## 📈 Success Metrics (6 Months)

| Metric | Baseline | Target | Month 1 | Month 3 | Month 6 |
|--------|----------|--------|---------|---------|---------|
| Invoice processing time | 5 days | <24h | ___ | ___ | ___ |
| Categorization accuracy | 95% | >98% | ___ | ___ | ___ |
| AP clerk time on data entry | 60% | <10% | ___ | ___ | ___ |
| AP clerk time on high-value work | 40% | >90% | ___ | ___ | ___ |
| Cost (AI vs. additional hire) | N/A | $500/mo vs. $8K/mo | ___ | ___ | ___ |

---

## 🎯 Alternative Models Considered

### **Why NOT Model 1 (Human-Led, AI-Assisted)?**
- Invoice processing is 90% structured, rule-based → AI can lead, not just assist
- Having humans review every AI recommendation wastes time (defeats automation purpose)

### **Why NOT Model 3 (Balanced Collaboration)?**
- Real-time collaboration not needed — AI can process invoices overnight (no human waiting)
- Human involvement only needed for exceptions (<10% of cases)

### **Why NOT Model 5 (Fully AI)?**
- Medium risk (compliance, financial loss) requires human oversight
- 10% of invoices have exceptions (missing data, disputes) that AI can't handle yet

---

## 📚 Next Steps

1. **Get buy-in:** Present this assessment to CFO + AP manager
2. **Budget approval:** $500/month AI agent cost (vs. $8K/month additional hire)
3. **Pilot:** Deploy InvoiceProcessor-Agent, run parallel for 1 month
4. **Scale:** Increase autonomy after 1 month, shift humans to supervision
5. **Measure:** Track metrics monthly, iterate based on accuracy/time savings

---

## 📖 Resources

**Documentation:**
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)
- [AI Agents](../DOCS/05-ai-agents.md)
- [Automation SIPOC](../DOCS/04-automation-sipoc.md)

**Templates:**
- [Agent Definition Template](../ADOPTION/TEMPLATES/agent-definition-template.yaml)

**Playbooks:**
- [Finance Playbook](../PLAYBOOKS/by-sector/business-functions/finance.md)
- [SME Transformation](../PLAYBOOKS/by-stage/sme-transformation.md)

---

**Assessment Completed:** November 2025  
**Recommendation:** Deploy AI-Led, Human-Supervised model for Accounts Payable invoice processing  
**Expected ROI:** 16x cost savings ($500/month AI vs. $8K/month human hire), 5 days → <24h processing time
```

---

## Configuration Instructions

### **Step 1: Gather Process Data**

Before running this prompt, collect:
- [ ] Process description (step-by-step workflow)
- [ ] Current team (who does this work? titles, time allocation)
- [ ] Volume metrics (transactions/day, peak periods)
- [ ] Time spent (% on data entry vs. judgment vs. relationships)
- [ ] Error rate (% of tasks requiring rework)
- [ ] Pain points (what frustrates team most?)

---

### **Step 2: Run Assessment**

- [ ] Fill in user prompt template with process data
- [ ] Submit to AI (ChatGPT, Claude, or custom LLM)
- [ ] Review output: Does recommended model make sense?

---

### **Step 3: Validate with Team**

- [ ] Share assessment with:
  - Department head (do they agree with model?)
  - Team members doing the work (do they feel AI would help or hinder?)
  - IT/compliance (any technical or regulatory blockers?)

- [ ] Adjust based on feedback (e.g., if team fears job loss, emphasize career growth)

---

### **Step 4: Pilot & Iterate**

- [ ] Deploy recommended model on small scale (1 month pilot)
- [ ] Track metrics (time savings, accuracy, employee satisfaction)
- [ ] Iterate: If Model 2 (AI-Led) causes too many errors, downgrade to Model 3 (Balanced) or upgrade AI training

---

## 📚 Resources

**Documentation:**
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)
- [AI Agents](../DOCS/05-ai-agents.md)
- [Automation SIPOC](../DOCS/04-automation-sipoc.md)

**Checklists:**
- [AI Agent Integration](../ADOPTION/CHECKLISTS/ai-agent-integration.md)
- [SME Transformation Roadmap](../ADOPTION/CHECKLISTS/sme-transformation-roadmap.md)

**Playbooks:**
- [Finance](../PLAYBOOKS/by-sector/business-functions/finance.md)
- [Sales](../PLAYBOOKS/by-sector/business-functions/sales.md)
- [HR](../PLAYBOOKS/by-sector/business-functions/hr.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
