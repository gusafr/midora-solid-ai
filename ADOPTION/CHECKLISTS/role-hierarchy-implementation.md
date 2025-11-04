# Role Hierarchy Implementation Checklist

**For:** Organizations deploying the 4-level framework (Low, Intermediate, High, Executive) for humans + AI agents

**Goal:** Create clear career paths, autonomy levels, decision authority, and compensation for all roles (human and AI)

**Time:** 4-6 weeks for initial deployment, ongoing refinement

---

## Why Role Hierarchy Matters

**Traditional Problem:**
- Flat titles ("Software Engineer I-V") without clear autonomy/decision authority
- No career path for AI agents (where do they fit?)
- Compensation not tied to decision-making scope
- Humans + AI agents compete rather than complement

**SOLID.AI Solution:**
- **4 Levels:** Low (Assistants/Analysts) → Intermediate (Consultants/Coordinators) → High (Strategists/Experts) → Executive (C-Suite)
- **Clear Boundaries:** Each level has defined autonomy, decision authority, tasks, compensation
- **Humans + AI Together:** Both mapped to same framework, collaboration is explicit
- **Career Paths:** "Junior Analyst (Low) → Senior Analyst (Intermediate) → Manager (High) → VP (Executive)"

**See:** [Role Hierarchy Documentation](../DOCS/10-role-hierarchy.md)

---

## Step 1: Review the 4-Level Framework

### **Low-Level Roles** (Assistants/Analysts)

- [ ] **Understand Low-Level Characteristics:**
  - **Tasks:** Structured, repetitive, rule-based (e.g., data entry, lead qualification, expense categorization)
  - **Autonomy:** Minimal — follow scripts, escalate edge cases
  - **Decision Authority:** Execute pre-defined rules, no strategic discretion
  - **Compensation (Human):** $40K-$60K/year (junior salary)
  - **Compensation (AI):** $200-$500/month (AI agent subscription)

- [ ] **Examples:**
  - Human: Junior accountant, SDR (Sales Development Rep), recruiting coordinator, customer support rep
  - AI: ExpenseCategorizer-Agent, LeadQualifier-Agent, ResumeScreener-Agent, TicketTriager-Agent

---

### **Intermediate-Level Roles** (Consultants/Coordinators)

- [ ] **Understand Intermediate-Level Characteristics:**
  - **Tasks:** Semi-structured, require judgment/context (e.g., proposal generation, budget forecasting, cross-team coordination)
  - **Autonomy:** Moderate — interpret requirements, make recommendations, escalate high-stakes decisions
  - **Decision Authority:** Tactical decisions within defined scope (e.g., "Which leads to prioritize?", "How to allocate budget across departments?")
  - **Compensation (Human):** $70K-$120K/year (mid-level salary)
  - **Compensation (AI):** $1K-$3K/month (advanced AI agent or orchestration)

- [ ] **Examples:**
  - Human: Senior analyst, account manager, project coordinator, technical lead
  - AI: ProposalGenerator-Agent, BudgetForecaster-Agent, RevenueOps-Coordinator, SprintPlanner-Agent

---

### **High-Level Roles** (Strategists/Experts)

- [ ] **Understand High-Level Characteristics:**
  - **Tasks:** Unstructured, strategic, require deep expertise (e.g., product vision, market expansion, technical architecture)
  - **Autonomy:** High — set priorities, make strategic decisions, guide teams
  - **Decision Authority:** Strategic decisions within function (e.g., "Should we build Feature X?", "Expand to Market Y?")
  - **Compensation (Human):** $150K-$250K/year (senior leadership)
  - **Compensation (AI):** Currently rare (AI not yet capable of strategic synthesis, but emerging)

- [ ] **Examples:**
  - Human: VP Sales, CFO, Head of Product, Chief Architect
  - AI: Not widely deployed yet (2025), but research emerging (StrategicAdvisor-Agent)

---

### **Executive-Level Roles**

- [ ] **Understand Executive-Level Characteristics:**
  - **Tasks:** Set vision, allocate capital, manage board/investors, ultimate accountability
  - **Autonomy:** Full — define company direction, hire/fire leadership, M&A
  - **Decision Authority:** All strategic decisions (company-wide)
  - **Compensation (Human):** $200K+ (equity, bonuses, board compensation)
  - **Compensation (AI):** Not applicable (AI cannot replace CEO fiduciary duty, vision-setting, stakeholder relationships)

- [ ] **Examples:**
  - Human: CEO, COO, CTO, Board of Directors
  - AI: None (AI can advise, but cannot hold executive accountability)

---

## Step 2: Map Existing Roles to 4-Level Framework

### **Audit Current Roles**

- [ ] **List all roles in your organization** (use HRIS or org chart)

| Current Title | Function | # People | Current Salary Range |
|---------------|----------|----------|----------------------|
| Junior Accountant | Finance | 2 | $45K-$50K |
| Senior Accountant | Finance | 1 | $75K |
| Finance Manager | Finance | 1 | $120K |
| CFO | Finance | 1 | $200K |
| SDR | Sales | 3 | $50K-$60K |
| Account Executive | Sales | 5 | $80K-$100K + commission |
| VP Sales | Sales | 1 | $180K + commission |
| ... | ... | ... | ... |

- [ ] **Map each role to 4-level framework:**

| Current Title | Mapped Level | Why? |
|---------------|--------------|------|
| Junior Accountant | Low-Level | Rule-based tasks (expense categorization, AP/AR data entry) |
| Senior Accountant | Intermediate-Level | Budget analysis, forecast variance, cross-functional coordination |
| Finance Manager | High-Level | Strategic financial planning, M&A support, risk management |
| CFO | Executive | Capital allocation, investor relations, board reporting |
| SDR | Low-Level | Follow lead qualification scripts, book meetings |
| Account Executive | Intermediate-Level | Custom proposals, deal negotiation, relationship management |
| VP Sales | High-Level | Sales strategy, territory planning, team hiring |

**Output:** `ROLE-MAPPING.md` file

---

### **Identify Gaps & Overlaps**

- [ ] **Gaps:** Are there levels with no humans? (e.g., no Intermediate-Level in Finance → consider promoting Senior Accountant or hiring)
- [ ] **Overlaps:** Are multiple people doing Low-Level work that AI could handle? (e.g., 3 SDRs qualifying leads → consider LeadQualifier-Agent + 1 human AE)
- [ ] **Title Inflation:** Are people titled "Manager" but doing Low-Level work? (common problem — fix with honest leveling)

---

## Step 3: Define Autonomy & Decision Authority for Each Level

### **Create Decision Authority Matrix**

For each function (Finance, Sales, HR, etc.), define what each level can decide:

**Example: Finance Function**

| Decision Type | Low-Level | Intermediate-Level | High-Level | Executive |
|---------------|-----------|-------------------|------------|-----------|
| **Expense approval** | <$100 (auto-approve) | $100-$5K (review, approve) | $5K-$50K (strategic judgment) | >$50K (final authority) |
| **Budget allocation** | ❌ No authority | Recommend (cross-dept) | Allocate within function | Allocate company-wide |
| **Hiring decisions** | ❌ No authority | Screen candidates | Hire for team | Hire executives |
| **Vendor contracts** | ❌ No authority | $0-$10K/year | $10K-$100K/year | >$100K/year |
| **Financial strategy** | ❌ No authority | ❌ No authority | Recommend (CFO decides) | Set strategy |

- [ ] **Repeat for all functions:** Sales, HR, Operations, IT, etc.
- [ ] **Document edge cases:** What happens when Low-Level agent encounters $101 expense? (escalate to Intermediate)

**Output:** `DECISION-AUTHORITY-MATRIX.md`

---

### **Define Escalation Rules**

- [ ] **Low-Level → Intermediate:** When to escalate?
  - Rule: "If task falls outside script/rules, escalate within 1 hour"
  - Example: LeadQualifier-Agent encounters prospect asking for custom pricing → escalate to Account Executive (Intermediate)

- [ ] **Intermediate → High:** When to escalate?
  - Rule: "If decision has >$10K impact or >3-month horizon, escalate to High-Level"
  - Example: BudgetForecaster-Agent sees 20% revenue variance → escalate to CFO (High-Level)

- [ ] **High → Executive:** When to escalate?
  - Rule: "If decision impacts company vision, capital allocation, or fiduciary duty, escalate to Executive"
  - Example: VP Sales recommends entering new market ($500K investment) → CEO decides

---

## Step 4: Map AI Agents to Role Hierarchy

### **Audit Current AI Agents**

- [ ] **List all deployed AI agents:**

| AI Agent Name | Function | Tasks | Current Level (guess) |
|---------------|----------|-------|----------------------|
| ExpenseCategorizer-Agent | Finance | Auto-categorize expenses | Low-Level |
| BudgetForecaster-Agent | Finance | Update rolling forecasts | Intermediate-Level |
| LeadQualifier-Agent | Sales | Qualify inbound leads, book meetings | Low-Level |
| ProposalGenerator-Agent | Sales | Generate custom proposals | Intermediate-Level |
| ... | ... | ... | ... |

---

### **Formalize AI Agent Levels**

- [ ] **For each AI agent, define:**
  - **Level:** Low, Intermediate, High, Executive (most AI agents are Low/Intermediate as of 2025)
  - **Autonomy:** What can it decide without human approval?
  - **Escalation Rules:** When does it hand off to human?
  - **Compensation:** What does it cost? (monthly subscription, API usage, etc.)

**Example: LeadQualifier-Agent (Low-Level)**

```yaml
agent:
  name: LeadQualifier-Agent
  level: Low-Level
  function: Sales
  tasks:
    - Respond to inbound leads <5 minutes
    - Score leads (1-100) using qualification criteria
    - Book qualified meetings on AE calendar
  autonomy:
    - Can auto-respond to 90% of leads (templated responses)
    - Can book meetings for leads scoring >70
  decision_authority:
    - Qualify leads: Yes (follow script)
    - Discount pricing: No (escalate to AE)
    - Custom terms: No (escalate to AE)
  escalation_rules:
    - If lead asks for custom pricing → escalate to Account Executive (Intermediate-Level)
    - If lead is enterprise (>1,000 employees) → escalate to VP Sales (High-Level)
  compensation:
    monthly_cost: $300 (Zapier + AI API)
    human_equivalent: $4,000/month (SDR salary)
    roi: 13x cost savings
```

- [ ] **Repeat for all AI agents**
- [ ] **Store in:** `ADOPTION/TEMPLATES/agent-definition-template.yaml`

---

## Step 5: Create Career Paths (Humans + AI)

### **Define Progression Paths**

For humans, map career progression across levels:

**Example: Finance Career Path**

| Level | Title | Salary Range | Next Level Requirements |
|-------|-------|--------------|------------------------|
| Low-Level | Junior Accountant | $40K-$60K | 1-2 years, learn budgeting/forecasting |
| Intermediate-Level | Senior Accountant | $70K-$100K | 3-5 years, lead cross-functional projects |
| High-Level | Finance Manager | $120K-$180K | 5-7 years, strategic financial planning |
| Executive | CFO | $200K+ | 10+ years, manage $10M+ budgets, board experience |

- [ ] **Repeat for all functions:** Sales, HR, Operations, IT, etc.
- [ ] **Make transparent:** Publish career paths in employee handbook, share in onboarding

---

### **AI Agent Progression**

AI agents can also "level up":

**Example: Lead Qualification Path**

| Level | Agent Name | Capabilities | Cost/Month |
|-------|------------|--------------|------------|
| Low-Level | LeadQualifier-Agent | Follow script, book meetings, basic qualification | $300 |
| Intermediate-Level | LeadStrategist-Agent | Analyze lead patterns, recommend targeting, A/B test messaging | $1,500 |
| High-Level | Not yet available (2025) | Strategic lead gen strategy, market expansion recommendations | TBD |

- [ ] **Define upgrade triggers:** When to upgrade AI agent?
  - Trigger: "If Low-Level agent handling >80% of tasks autonomously for 3 months, consider upgrading to Intermediate"
  - Example: LeadQualifier-Agent booking 100 meetings/month with 90% qualification accuracy → upgrade to LeadStrategist-Agent to optimize targeting

---

## Step 6: Align Compensation with Role Level

### **Set Compensation Bands**

- [ ] **Define salary ranges per level:**

| Level | Human Salary Range | AI Agent Cost Range | Compensation Philosophy |
|-------|-------------------|---------------------|------------------------|
| Low-Level | $40K-$60K/year | $200-$500/month | Execute structured tasks, minimal discretion |
| Intermediate-Level | $70K-$120K/year | $1K-$3K/month | Judgment calls, cross-functional coordination |
| High-Level | $150K-$250K/year | $5K-$10K/month (rare) | Strategic decisions, deep expertise |
| Executive | $200K+ (+ equity) | N/A (AI can't be CEO) | Vision-setting, fiduciary duty |

- [ ] **Audit current salaries:** Are people compensated appropriately for their level?
  - Example: If Senior Accountant (Intermediate) earning $50K → underpaid, risk losing talent
  - Example: If Junior Accountant (Low-Level) earning $80K → overpaid, or they should be reclassified as Intermediate

---

### **Fair Compensation for AI-Augmented Roles**

- [ ] **If AI automates part of a human's role, do they get a raise?**
  - **Yes, if** they move to higher-level work (Low → Intermediate → High)
  - Example: Junior Accountant (Low-Level, $50K) → AI handles data entry → Human becomes Financial Analyst (Intermediate, $75K) focusing on budget analysis

- [ ] **Track career growth:**
  - Baseline: % of employees promoted year-over-year
  - Target: >20% annual promotions (AI frees people to upskill)

---

## Step 7: Implement & Communicate

### **Rollout Plan**

- [ ] **Week 1: Leadership Alignment**
  - Present Role Hierarchy framework to executive team
  - Get buy-in: "This will create clarity, career paths, and fair compensation"

- [ ] **Week 2-3: Map All Roles**
  - Work with HR + function leaders to map all roles (humans + AI) to 4 levels
  - Create `ROLE-MAPPING.md`, `DECISION-AUTHORITY-MATRIX.md`, career path documents

- [ ] **Week 4: All-Hands Communication**
  - Share Role Hierarchy framework with all employees
  - Explain: "Why we're doing this, what changes, what stays the same"
  - FAQ: "Will I be demoted? Will AI take my job? How do I get promoted?"

- [ ] **Week 5-6: 1:1 Conversations**
  - Every manager meets with direct reports to:
    - Share their mapped level
    - Discuss career path to next level
    - Address concerns

---

### **Communication Templates**

**Email to All Employees:**

> **Subject:** Introducing Role Hierarchy — Clear Career Paths for All
>
> We're implementing a 4-level Role Hierarchy (Low, Intermediate, High, Executive) to create:
> - **Clear career paths** — Know exactly what it takes to get promoted
> - **Fair compensation** — Pay aligned with decision authority + scope
> - **Human + AI collaboration** — Both mapped to same framework, no competition
>
> **What changes:**
> - Your title may change to reflect your level (e.g., "Analyst" → "Low-Level Analyst" or "Intermediate-Level Consultant")
> - Decision authority is now explicit (see attached Decision Matrix)
>
> **What stays the same:**
> - Your salary (unless you're promoted or underpaid — we'll fix that)
> - Your team, manager, responsibilities
>
> **Next steps:**
> - Your manager will share your mapped level in 1:1 this week
> - Career paths published in employee handbook by [date]
>
> Questions? Email [HR contact] or ask in #role-hierarchy Slack channel.

---

## Step 8: Monitor & Iterate

### **Track Metrics**

- [ ] **Career Mobility:**
  - % employees promoted year-over-year (target: >20%)
  - Average time to promotion (Low→Intermediate, Intermediate→High)

- [ ] **Compensation Equity:**
  - % employees within salary band for their level (target: >90%)
  - Pay gap audit (gender, race, tenure)

- [ ] **AI Agent Effectiveness:**
  - % tasks handled by Low-Level AI without escalation (target: >80%)
  - % tasks requiring Intermediate-Level AI (target: 15-20%)
  - % tasks requiring High-Level human (target: <5%)

- [ ] **Employee Satisfaction:**
  - Survey: "Do you understand your career path?" (target: >80% yes)
  - Survey: "Do you feel AI is helping your career?" (target: >70% yes)
  - Turnover rate (target: <10%)

---

### **Quarterly Reviews**

- [ ] **Every 3 months:**
  - Review all role levels — any changes needed?
  - Promote employees who've met next-level requirements
  - Upgrade AI agents that are ready for next level
  - Adjust compensation bands based on market data

---

## 🛡️ Common Pitfalls

### **Pitfall #1: Title Inflation**
- **Problem:** Everyone wants "Manager" title, even if doing Low-Level work
- **Solution:** Be honest — "Your work is valuable, but it's Low-Level (structured tasks). Here's how to get to Intermediate."

### **Pitfall #2: "AI Will Take My Job"**
- **Problem:** Employees fear Low-Level AI agents will replace them
- **Solution:** Reframe — "AI handles Low-Level tasks → you upskill to Intermediate → higher pay, more interesting work"

### **Pitfall #3: No Career Path for Low-Level**
- **Problem:** If Low-Level roles are all AI, where do junior humans start?
- **Solution:** Create "AI Trainer" or "AI Supervisor" roles (Intermediate-Level) — humans who configure/monitor Low-Level AI agents

### **Pitfall #4: Compensation Gaps**
- **Problem:** Existing employees underpaid for their level
- **Solution:** Budget for salary adjustments — don't implement Role Hierarchy without fixing pay equity

---

## 📚 Resources

**Documentation:**
- [Role Hierarchy](../DOCS/10-role-hierarchy.md)
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)
- [Organizational Model](../DOCS/03-organizational-model.md)

**Templates:**
- [Role Hierarchy Matrix](../ADOPTION/TEMPLATES/role-hierarchy-matrix.yaml)
- [Agent Definition Template](../ADOPTION/TEMPLATES/agent-definition-template.yaml)

**Prompts:**
- [Role Level Definition Prompt](../ADOPTION/PROMPT-TEMPLATES/role-level-definition.md)
- [Human-AI Collaboration Assessment](../ADOPTION/PROMPT-TEMPLATES/human-ai-collaboration-assessment.md)

**Playbooks:**
- [SME Transformation — Role Hierarchy Section](../PLAYBOOKS/by-stage/sme-transformation.md#implement-role-hierarchy)
- [HR Function Playbook](../PLAYBOOKS/by-sector/business-functions/hr.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
