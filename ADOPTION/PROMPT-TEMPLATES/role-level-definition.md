# Role Level Definition Prompt Template

**When to Use:** Mapping existing roles (human or AI) to the 4-level SOLID.AI framework

**Purpose:** Define autonomy, decision authority, tasks, and compensation for each role level

**Level:** Intermediate-Level Analysis (typically run by HR or Department Head)

**Typical User:** CHRO, VP HR, Department Head, Transformation Lead

---

## Overview

**The Problem:**

Most organizations have unclear role definitions:
- Titles don't match responsibility (e.g., "Manager" doing Low-Level data entry)
- No clear career path ("How do I get promoted from Analyst to Manager?")
- Compensation misaligned (Junior doing Intermediate work paid at Low-Level salary)
- AI agents added ad-hoc (no framework for where they fit)

**SOLID.AI Solution:**

Map all roles (human + AI) to 4 levels:

| Level | Autonomy | Decision Authority | Typical Tasks | Compensation (Human) | Compensation (AI) |
|-------|----------|-------------------|---------------|----------------------|-------------------|
| **Low-Level** (Assistants/Analysts) | Minimal (follow scripts) | Execute rules, escalate edge cases | Data entry, lead qualification, expense categorization | $40K-$60K/year | $200-$500/month |
| **Intermediate-Level** (Consultants/Coordinators) | Moderate (interpret context) | Tactical decisions, recommend to High-Level | Proposals, forecasts, cross-team coordination | $70K-$120K/year | $1K-$3K/month |
| **High-Level** (Strategists/Experts) | High (set priorities) | Strategic decisions within function | Product vision, market strategy, technical architecture | $150K-$250K/year | Rare (not yet widely available) |
| **Executive** | Full (set company direction) | All strategic decisions | Vision, capital allocation, board management | $200K+ (+ equity) | N/A (AI can't be CEO) |

**See:** [Role Hierarchy Documentation](../DOCS/10-role-hierarchy.md)

---

## Prompt Template

### **System Prompt**

```
You are a Role Level Definition Analyst for the SOLID.AI framework.

Your role is to analyze a job role (human or AI agent) and map it to the 4-level framework:
1. **Low-Level** (Assistants/Analysts)
2. **Intermediate-Level** (Consultants/Coordinators)
3. **High-Level** (Strategists/Experts)
4. **Executive** (C-Suite)

For each role, you will define:
- **Level:** Which of the 4 levels does this role belong to?
- **Tasks:** What does this role actually do? (concrete examples)
- **Autonomy:** How much freedom to make decisions without approval?
- **Decision Authority:** What can this role decide? What must be escalated?
- **Escalation Rules:** When does this role hand off to the next level?
- **Compensation:** What should this role be paid (human salary or AI cost)?
- **Career Path:** How does this role progress to the next level?

**Leveling Criteria:**

**Low-Level:**
- Tasks: Structured, repetitive, rule-based
- Autonomy: Minimal (follow scripts, checklists, SOPs)
- Decision Authority: Execute pre-defined rules, escalate all edge cases
- Examples: Data entry clerk, SDR (Sales Development Rep), junior accountant, customer support rep, AI agents (LeadQualifier, ExpenseCategorizer)

**Intermediate-Level:**
- Tasks: Semi-structured, require judgment/context
- Autonomy: Moderate (interpret requirements, make recommendations)
- Decision Authority: Tactical decisions within defined scope (e.g., "Which leads to prioritize?", "How to allocate budget?")
- Examples: Account Executive, senior analyst, project coordinator, AI agents (ProposalGenerator, BudgetForecaster, RevenueOps-Coordinator)

**High-Level:**
- Tasks: Unstructured, strategic, deep expertise
- Autonomy: High (set priorities, make strategic decisions)
- Decision Authority: Strategic decisions within function (e.g., "Should we build Feature X?", "Expand to Market Y?")
- Examples: VP Sales, CFO, Head of Product, Chief Architect

**Executive:**
- Tasks: Set vision, allocate capital, manage board/investors
- Autonomy: Full (define company direction)
- Decision Authority: All strategic decisions (company-wide)
- Examples: CEO, COO, CTO (AI cannot hold executive roles)

Your output should be a structured role definition with:
- Role name (human or AI)
- Mapped level (Low, Intermediate, High, Executive)
- Tasks (5-7 concrete examples)
- Autonomy description
- Decision authority (what can decide, what must escalate)
- Escalation rules
- Compensation (salary range or AI cost)
- Career path (how to progress to next level)

Tone: Professional, data-driven, clear
Format: Markdown with tables
```

---

### **User Prompt (Fill-In Template)**

```
Map the following role to the SOLID.AI 4-level framework:

**Role Name:** {ROLE_NAME}
Example: "Senior Financial Analyst" or "LeadQualifier-Agent"

**Is this a human or AI role?** {HUMAN_OR_AI}

**Function:** {FUNCTION}
Example: Finance, Sales, HR, IT, Operations

**Current Title/Description:** {CURRENT_DESCRIPTION}
Example: "Responsible for budget analysis, variance reporting, monthly forecasts, ad-hoc financial modeling"

**Typical Tasks (list 5-10):**
1. {TASK_1}
   Example: "Analyze monthly budget variance (actual vs. plan)"
2. {TASK_2}
   Example: "Create rolling 12-month revenue forecast"
3. {TASK_3}
   Example: "Build financial models for new product launches"
4. {TASK_4}
   Example: "Present financial insights to CFO + executive team"
5. {TASK_5}
   Example: "Coordinate with department heads for budget planning"

**Decision-Making Examples:**
- {DECISION_1}
  Example: "Can approve expense categorization changes up to $5K"
- {DECISION_2}
  Example: "Cannot change budget without CFO approval"
- {DECISION_3}
  Example: "Recommends forecast adjustments, CFO makes final call"

**Autonomy Level (current state):**
- {AUTONOMY_DESCRIPTION}
  Example: "Moderate — can build models independently, but must review with CFO before sharing with leadership"

**Who does this role escalate to?**
- {ESCALATION_TO}
  Example: "CFO (High-Level)" or "Finance Manager (Intermediate-Level)"

**Current Compensation (if human):**
- {COMPENSATION}
  Example: "$85,000/year" or "N/A (AI agent, estimated $1,500/month)"

**Desired Career Path (if human):**
- {CAREER_PATH}
  Example: "Senior Analyst → Finance Manager → Director of FP&A → CFO"

Now map this role to the SOLID.AI 4-level framework.
```

---

### **Expected Output (Example 1: Human Role)**

```markdown
# Role Definition: Senior Financial Analyst

**Organization:** TechCorp Manufacturing  
**Function:** Finance  
**Role Type:** Human  
**Analyzed:** November 2025  

---

## 📊 SOLID.AI Level: **Intermediate-Level** (Consultant/Analyst)

**Rationale:**
- **Tasks:** Semi-structured (budget analysis, forecasting, financial modeling) — requires judgment, not just rule-following
- **Autonomy:** Moderate (builds models independently, reviews with CFO before sharing)
- **Decision Authority:** Tactical decisions (can recommend forecast adjustments, approve small categorization changes) — strategic decisions escalated to CFO
- **Not Low-Level:** Role requires context interpretation, cross-functional coordination, judgment (not just data entry)
- **Not High-Level:** Role doesn't set financial strategy, doesn't own P&L, doesn't hire/manage team

---

## 🎯 Role Definition

### **Tasks (Concrete Examples)**

| Task | Frequency | Autonomy | Output |
|------|-----------|----------|--------|
| **1. Analyze monthly budget variance** | Monthly | High | Variance report (actual vs. plan), root cause analysis |
| **2. Create rolling 12-month revenue forecast** | Weekly | Moderate | Updated forecast model, present to CFO |
| **3. Build financial models for new products** | Quarterly | Moderate | NPV, IRR, payback period analysis |
| **4. Present insights to executive team** | Monthly | Low | Slides prepared by analyst, CFO presents |
| **5. Coordinate with department heads for budgets** | Quarterly | Moderate | Budget consolidation, identify gaps |
| **6. Ad-hoc analysis for CFO** | As needed | High | Custom reports, scenario analysis |

---

### **Autonomy**

**What this role can do independently (no approval):**
- Build financial models (Excel, BI tools)
- Analyze budget variance, identify trends
- Update rolling forecasts based on actuals
- Coordinate budget meetings with department heads

**What requires CFO approval:**
- Share forecasts with executive team (CFO reviews first)
- Change budget assumptions (revenue growth, COGS, headcount)
- Approve expenses >$5K
- Hire/fire team members

---

### **Decision Authority**

| Decision Type | Authority Level | Example |
|---------------|-----------------|---------|
| **Expense categorization** | Can approve <$5K | "Should this $2K software expense be IT or Marketing?" → Analyst decides |
| **Budget variance** | Recommend | "Revenue down 10% vs. plan due to customer churn" → Analyst flags, CFO decides action |
| **Forecast adjustments** | Recommend | "Q4 revenue forecast should drop 5% based on pipeline data" → Analyst recommends, CFO approves |
| **Budget allocation** | ❌ No authority | "Should we invest $50K in new product vs. marketing?" → CFO decides |
| **Hiring** | ❌ No authority | "Should we hire another analyst?" → CFO decides |

---

### **Escalation Rules**

**Escalate to CFO (High-Level) when:**
- Forecast variance >10% (major miss)
- Budget change >$10K required
- Cross-functional conflict (e.g., Sales disputes revenue forecast)
- Investor/board questions (CFO handles external stakeholders)

**Escalate to Finance Manager (Intermediate-Level, if exists) when:**
- Need prioritization (multiple ad-hoc requests from executives)
- Cross-team coordination (e.g., Sales + Marketing budget alignment)

---

## 💰 Compensation

**Current:** $85,000/year

**Market Range (Intermediate-Level Finance):**
- **Low:** $70,000/year (smaller company, <50 employees)
- **Mid:** $85,000-$100,000/year (100-250 employees, this role)
- **High:** $110,000-$120,000/year (large company, >500 employees, or SF Bay Area)

**Assessment:** **On target** — $85K is appropriate for Intermediate-Level in 120-person manufacturing company

**If underpaid (<$70K):** Risk losing talent → adjust to $75K-$85K
**If overpaid (>$120K):** Reassess level — is this person doing High-Level work (managing team, setting strategy)? If yes, promote to Finance Manager/Director.

---

## 📈 Career Path

### **Current Level:** Intermediate-Level (Senior Financial Analyst)

### **Path to High-Level (Finance Manager / Director of FP&A):**

**Requirements to promote:**
- [ ] **Manage team:** Lead 1-2 junior analysts (Low-Level)
- [ ] **Own function:** Responsible for all budgeting & forecasting (not just supporting CFO)
- [ ] **Strategic input:** CFO asks for recommendations on capital allocation, not just analysis
- [ ] **Cross-functional leadership:** Coordinate Finance initiatives across Sales, Marketing, Operations (not just coordinate meetings)
- [ ] **Time in role:** 2-3 years as Senior Analyst, demonstrated consistent high performance

**Expected timeline:** 2-3 years (if high performer), 4-5 years (average performer)

**Salary at next level (High-Level):** $120,000-$150,000/year

---

### **Path to Executive (CFO):**

**Requirements:**
- [ ] **P&L ownership:** Manage $10M+ budget, responsible for financial outcomes
- [ ] **Board/investor experience:** Present to board, manage investor relations
- [ ] **Strategic leadership:** Set financial strategy (not just execute CFO's strategy)
- [ ] **Team leadership:** Manage 5+ person finance team
- [ ] **Time in role:** 5-7 years as Finance Director/Manager

**Expected timeline:** 10-15 years total (Senior Analyst → Manager → Director → CFO)

**Salary at Executive level:** $200,000+ (+ equity, bonuses)

---

## 🤖 AI Agent Comparison

**Could this role be replaced by AI?**

**No (as of 2025), but AI can assist:**

| Task | AI Capability | Human Still Needed? |
|------|---------------|---------------------|
| **Budget variance analysis** | AI can flag variances (BudgetForecaster-Agent) | ✅ Human interprets root cause (is it customer churn, seasonality, pricing?) |
| **Rolling forecasts** | AI can update numbers (BudgetForecaster-Agent) | ✅ Human validates assumptions (is growth rate realistic?) |
| **Financial modeling** | AI can build templates (Excel Copilot, ChatGPT) | ✅ Human customizes for specific business context |
| **Executive presentation** | AI can generate slides (ChatGPT, Gamma) | ✅ Human tells story, answers CFO questions, builds trust |
| **Cross-functional coordination** | ❌ AI can't negotiate priorities, resolve conflicts | ✅ Human handles relationships, politics, judgment |

**Recommendation:** **Human-Led, AI-Assisted**
- Human Senior Analyst stays in role (Intermediate-Level)
- Deploy BudgetForecaster-Agent (AI, Intermediate-Level) to automate variance flagging, forecast updates
- Human focuses on interpretation, storytelling, cross-functional leadership (60% time on high-value work, up from 30%)

**Expected impact:**
- Analyst time on data updates: 40% → <10%
- Analyst time on insights/strategy: 30% → 60%
- Forecast accuracy: 85% → 92% (AI flags anomalies faster)
- CFO satisfaction: Higher (analyst brings insights, not just reports)

---

## 📚 Resources

**Documentation:**
- [Role Hierarchy](../DOCS/10-role-hierarchy.md)
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)

**Templates:**
- [Role Hierarchy Matrix](../ADOPTION/TEMPLATES/role-hierarchy-matrix.yaml)
- [Agent Definition Template](../ADOPTION/TEMPLATES/agent-definition-template.yaml)

**Checklists:**
- [Role Hierarchy Implementation](../ADOPTION/CHECKLISTS/role-hierarchy-implementation.md)

**Playbooks:**
- [Finance Playbook](../PLAYBOOKS/by-sector/business-functions/finance.md)
- [SME Transformation](../PLAYBOOKS/by-stage/sme-transformation.md)

---

**Role Mapped:** November 2025  
**Level:** Intermediate-Level (Consultant/Analyst)  
**Compensation:** $85K/year (on target)  
**Next Level:** Finance Manager / Director (2-3 years)
```

---

### **Expected Output (Example 2: AI Agent Role)**

```markdown
# Role Definition: LeadQualifier-Agent

**Organization:** TechCorp SaaS Startup  
**Function:** Sales  
**Role Type:** AI Agent  
**Analyzed:** November 2025  

---

## 📊 SOLID.AI Level: **Low-Level** (Assistant/Analyst)

**Rationale:**
- **Tasks:** Structured, repetitive, rule-based (respond to leads, score using criteria, book meetings)
- **Autonomy:** Minimal (follows qualification script, escalates all non-standard requests)
- **Decision Authority:** Execute pre-defined rules (score lead 1-100 using criteria), escalate edge cases (custom pricing, enterprise deals)
- **Not Intermediate:** Doesn't make judgment calls, doesn't coordinate across teams, doesn't handle complex negotiations

---

## 🎯 Role Definition

### **Tasks (Concrete Examples)**

| Task | Frequency | Autonomy | Output |
|------|-----------|----------|--------|
| **1. Respond to inbound leads <5 minutes** | 50-100/day | Full (auto-respond) | Email response, lead scored in CRM |
| **2. Score leads (1-100 using criteria)** | 50-100/day | Full (rule-based) | Lead score, qualification tag (hot/warm/cold) |
| **3. Book qualified meetings on AE calendar** | 10-20/day | Full (if score >70) | Calendar invite, briefing doc sent to AE |
| **4. Send nurture sequences to unqualified leads** | 30-50/day | Full (templated emails) | Email sequence (5 emails over 2 weeks) |
| **5. Flag enterprise leads (>1,000 employees)** | 2-5/day | Full (rule-based) | Escalate to VP Sales (High-Level) |
| **6. Update CRM with lead data** | 50-100/day | Full (auto-update) | CRM fields populated (company size, industry, pain point) |

---

### **Autonomy**

**What this AI agent can do independently (no human approval):**
- Respond to inbound leads <5 minutes (templated responses)
- Score leads 1-100 using qualification criteria (budget, authority, need, timeline)
- Book meetings for leads scoring >70 (qualified)
- Send nurture email sequences to leads scoring <70 (unqualified)
- Update CRM with lead data (company size, industry, pain point)

**What requires human approval:**
- Custom pricing (escalate to Account Executive, Intermediate-Level)
- Discount >10% (escalate to Sales Manager, High-Level)
- Enterprise deals (>1,000 employees) → escalate to VP Sales (High-Level)
- Non-standard terms (e.g., "We need SOC2 compliance before buying") → escalate to AE

---

### **Decision Authority**

| Decision Type | Authority Level | Example |
|---------------|-----------------|---------|
| **Lead scoring** | Full authority | Lead asks "How much does it cost?" → Agent scores 70 (budget question = interest), books demo |
| **Meeting booking** | Full authority (if score >70) | Lead scores 80 → Agent books demo on AE calendar |
| **Pricing** | ❌ No authority | Lead asks "Can we get 20% discount?" → Escalate to AE |
| **Custom terms** | ❌ No authority | Lead asks "Can we pay annually instead of monthly?" → Escalate to AE |
| **Enterprise deals** | ❌ No authority | Lead from Fortune 500 company → Escalate to VP Sales |

---

### **Escalation Rules**

**Escalate to Account Executive (Intermediate-Level) when:**
- Lead asks for custom pricing (discount >10%)
- Lead asks for demo customization (e.g., "Can you show Feature X?")
- Lead has non-standard requirements (e.g., "We need on-premise deployment")

**Escalate to VP Sales (High-Level) when:**
- Lead is enterprise (>1,000 employees, $1M+ deal size)
- Lead is strategic (competitor, key partner, high-profile customer)

**Escalate to Marketing (if lead unqualified):**
- Lead scores <40 (not ready to buy) → Send to nurture sequence, re-qualify in 3 months

---

## 💰 Compensation (AI Agent Cost)

**Monthly Cost:** $300/month
- Zapier automation: $100/month
- AI API (ChatGPT/Claude): $100/month
- CRM integration (HubSpot/Salesforce): $100/month

**Human Equivalent:** $4,000/month ($48K/year SDR salary ÷ 12)

**ROI:** 13x cost savings ($4,000 human vs. $300 AI)

---

### **Comparison: AI Agent vs. Human SDR**

| Metric | Human SDR (Low-Level) | LeadQualifier-Agent (Low-Level) |
|--------|----------------------|--------------------------------|
| **Response time** | 1-2 hours (business hours only) | <5 minutes (24/7) |
| **Lead capacity** | 50 leads/day | 500+ leads/day (10x scale) |
| **Consistency** | 80% (varies by person, mood, training) | 98% (follows script exactly) |
| **Cost** | $4,000/month ($48K/year salary) | $300/month (13x cheaper) |
| **Escalation rate** | 10% (SDR unsure when to escalate) | 5% (clear rules programmed) |
| **Availability** | 40 hours/week (M-F, 9-5) | 168 hours/week (24/7) |

**When to use AI:** High-volume, inbound leads (50+ per day), standard qualification criteria
**When to use human SDR:** Complex qualification (enterprise, custom use cases), relationship-building (warm intros, referrals)

---

## 📈 "Career Path" (AI Agent Upgrade Path)

### **Current Level:** Low-Level (LeadQualifier-Agent)

### **Path to Intermediate-Level (LeadStrategist-Agent):**

**Upgrade when:**
- [ ] LeadQualifier-Agent handles >80% of leads autonomously for 3+ months
- [ ] Escalation rate <5% (AI rarely confused, follows rules correctly)
- [ ] Team wants more strategic insights (not just qualification, but "Which lead sources convert best?")

**Intermediate-Level capabilities:**
- Analyze lead patterns (which industries, company sizes, pain points convert to customers?)
- Recommend targeting experiments ("We should run LinkedIn ads for HR managers at 50-200 employee companies")
- A/B test messaging (try 3 email subject lines, identify winner)
- Calculate LTV:CAC by lead source (which channels are profitable?)

**Cost:** $1,500/month (vs. $300 for Low-Level)

**When to upgrade:** After 6-12 months of Low-Level success (proven AI qualification works, now add strategy)

---

### **Path to High-Level:**

**Not yet available (as of 2025):**
- AI cannot set sales strategy (e.g., "Should we expand to Enterprise?")
- AI cannot hire sales team
- AI cannot manage customer relationships (strategic deals require human empathy, negotiation)

**Likely timeline:** 3-5 years (2028-2030) before High-Level sales AI agents available

---

## 🤖 AI Agent Definition (YAML)

```yaml
agent:
  name: LeadQualifier-Agent
  level: Low-Level
  type: Assistant
  function: Sales

  tasks:
    - Respond to inbound leads <5 minutes
    - Score leads (1-100) using qualification criteria
    - Book qualified meetings (score >70) on AE calendar
    - Send nurture sequences to unqualified leads
    - Flag enterprise leads (>1,000 employees) for VP Sales
    - Update CRM with lead data

  autonomy:
    can_decide:
      - Lead scoring (using BANT criteria: Budget, Authority, Need, Timeline)
      - Meeting booking (if score >70)
      - Nurture email sequences (templated)
    cannot_decide:
      - Custom pricing (escalate to AE)
      - Discount >10% (escalate to Sales Manager)
      - Enterprise deals (escalate to VP Sales)

  decision_authority:
    - Qualify leads: Full authority (rule-based)
    - Book meetings: Full authority (if qualified)
    - Pricing: No authority (escalate)

  escalation_rules:
    - condition: Lead asks for custom pricing
      action: Escalate to Account Executive (Intermediate-Level)
    - condition: Lead is enterprise (>1,000 employees)
      action: Escalate to VP Sales (High-Level)
    - condition: Lead scores <40 (unqualified)
      action: Send to nurture sequence, re-qualify in 3 months

  tools:
    - Zapier (CRM automation)
    - ChatGPT/Claude API (natural language responses)
    - HubSpot/Salesforce CRM
    - Calendly (meeting booking)

  metrics:
    - response_time: <5 minutes (target)
    - qualification_accuracy: >90% (% of qualified leads that convert to demos)
    - escalation_rate: <5% (% of leads requiring human intervention)
    - cost: $300/month vs. $4,000/month human SDR

  compensation:
    monthly_cost: $300
    human_equivalent: $4,000/month (SDR salary)
    roi: 13x cost savings
```

---

## 📚 Resources

**Documentation:**
- [Role Hierarchy](../DOCS/10-role-hierarchy.md)
- [AI Agents](../DOCS/05-ai-agents.md)
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)

**Templates:**
- [Agent Definition Template](../ADOPTION/TEMPLATES/agent-definition-template.yaml)

**Checklists:**
- [AI Agent Integration](../ADOPTION/CHECKLISTS/ai-agent-integration.md)

**Playbooks:**
- [Sales Playbook](../PLAYBOOKS/by-sector/business-functions/sales.md)
- [Startup AI-Native](../PLAYBOOKS/by-stage/startup-ai-native.md)

---

**Role Mapped:** November 2025  
**Level:** Low-Level (Assistant)  
**Cost:** $300/month (vs. $4,000 human SDR)  
**Upgrade Path:** LeadStrategist-Agent (Intermediate-Level, $1,500/month) after 6-12 months
```

---

## Configuration Instructions

### **Step 1: Collect Role Data**

For each role (human or AI), gather:
- [ ] **Tasks:** What does this role actually do? (5-10 concrete examples)
- [ ] **Decision-Making:** What can this role decide? What must be escalated?
- [ ] **Autonomy:** How much freedom to act without approval?
- [ ] **Compensation:** Current salary (human) or cost (AI)

---

### **Step 2: Map to 4-Level Framework**

Use these criteria:

| Criteria | Low-Level | Intermediate-Level | High-Level | Executive |
|----------|-----------|-------------------|------------|-----------|
| **Tasks** | Structured, repetitive | Semi-structured, judgment | Unstructured, strategic | Vision-setting |
| **Autonomy** | Minimal (follow scripts) | Moderate (interpret context) | High (set priorities) | Full (set direction) |
| **Decision Authority** | Execute rules | Tactical decisions | Strategic decisions (function) | Strategic decisions (company) |
| **Examples** | Data entry, lead qualification | Proposals, forecasts, coordination | Product vision, market strategy | CEO, CFO, CTO |

---

### **Step 3: Define Career Path (Humans) or Upgrade Path (AI)**

- [ ] **For humans:** What does next level require? (time in role, skills, responsibilities)
- [ ] **For AI agents:** When to upgrade to next level? (accuracy, autonomy, volume handled)

---

### **Step 4: Align Compensation**

- [ ] **Humans:** Is salary appropriate for level? (Low: $40K-$60K, Intermediate: $70K-$120K, High: $150K-$250K, Executive: $200K+)
- [ ] **AI agents:** Is cost reasonable? (Low: $200-$500/mo, Intermediate: $1K-$3K/mo)

---

## 📚 Resources

**Documentation:**
- [Role Hierarchy](../DOCS/10-role-hierarchy.md)
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)

**Templates:**
- [Role Hierarchy Matrix](../ADOPTION/TEMPLATES/role-hierarchy-matrix.yaml)
- [Agent Definition Template](../ADOPTION/TEMPLATES/agent-definition-template.yaml)

**Checklists:**
- [Role Hierarchy Implementation](../ADOPTION/CHECKLISTS/role-hierarchy-implementation.md)

**Playbooks:**
- [SME Transformation](../PLAYBOOKS/by-stage/sme-transformation.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
