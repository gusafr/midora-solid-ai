# Playbook: AI-Native Startup — Building from Square One

**Target Audience:** Founders, early-stage startups (0-10 people), bootstrapped or pre-seed companies with limited resources but clear purpose and intention.

**Goal:** Launch and scale a lean, AI-Native organization from day one—leverage AI agents to operate like a 50-person company with 5-10 humans.

**Context:** You have a clear vision, validated problem, and limited runway. You can't afford to hire 20+ people, but you need the operational capacity of a much larger team. SOLID.AI lets you build an AI-powered "virtual team" that handles repetitive, data-driven, and scalable work while humans focus on creativity, strategy, relationships, and product-market fit.

> **Note on Projections:** The metrics and comparisons below are **strategic projections** based on the SOLID.AI thesis and AI capability trends. [Midora](https://midora.com.br) is implementing this model from founding (2025) and will publish actual results as data becomes available. Your results will vary based on your product, market, team experience, and AI tool selection.

---

## 🎯 The AI-Native Startup Advantage

### **Traditional Startup (Reference Model):**
- **5 founders** → handling 20+ roles (sales, marketing, finance, ops, support, product, engineering)
- **80% time** on busywork (data entry, follow-ups, reporting, coordination)
- **20% time** on high-value work (vision, product, customer relationships)
- **6-12 months** to validate product-market fit
- **$500K-$1M** burn rate (salaries, tools, overhead)

### **AI-Native Startup (Projected SOLID.AI Model):**
- **5 founders + 10-15 AI agents** → same capacity as 20-person team
- **20% time** on busywork (AI handles 80% of repetitive tasks)
- **80% time** on high-value work (strategy, innovation, customer intimacy)
- **3-6 months** to validate product-market fit (2x faster iteration target)
- **$150K-$300K** burn rate (60-70% projected cost reduction)

**Projected Result:** Operate like a well-funded Series A company on a seed budget.

---

## 🚀 Phase 1: Foundation (Week 1-2)

### **Objective:** Define purpose, set up AI infrastructure, hire your first AI agents.

### **1.1 Define Your Purpose Layer**

**Human Work (4-8 hours):**

Use this prompt with your AI assistant:

```yaml
prompt:
  role: "You are a strategic advisor helping a startup define its Purpose Layer for the SOLID.AI framework."
  context: |
    Our startup is [describe your product/service]. 
    Our target customer is [describe customer].
    The problem we solve is [describe problem].
  task: |
    Help me create a Purpose Layer document that includes:
    1. Mission statement (1-2 sentences)
    2. Core values (3-5 principles)
    3. North Star metric (the ONE metric that defines success)
    4. Ethical guardrails (3-5 non-negotiables)
    5. Human oversight boundaries (where AI must defer to humans)
  format: "Markdown with YAML frontmatter"
```

**Output:** `PURPOSE.md` file defining your strategic intent.

**See:** [SOLID.AI Principles](../DOCS/01-principles.md), [Governance & Ethics](../DOCS/06-governance-ethics.md)

---

### **1.2 Hire Your First 5 AI Agents**

**Start with these essential agents:**

#### **1. CustomerInsights-Agent** (Low-Level Analyst)
```yaml
agent:
  identity:
    name: "CustomerInsights-Agent"
    level: "Low (Analyst)"
    role: "Customer research and feedback analysis"
    persona: "Data-driven analyst who surfaces customer pain points and opportunities"
  capabilities:
    - "Analyze customer conversations (emails, support tickets, sales calls)"
    - "Identify recurring themes, pain points, feature requests"
    - "Generate weekly customer insights report"
    - "Track sentiment trends over time"
  guardrails:
    - "Never share individual customer data without consent"
    - "Flag negative sentiment spikes to humans immediately"
    - "Anonymize quotes in reports"
  human_oversight:
    - decision_authority: "Supervised (100% human review)"
    - escalation_triggers:
      - "Customer churn signal detected"
      - "Unexpected sentiment shift"
      - "Ethical concern flagged"
  success_metrics:
    - "Time to insights: <24 hours from data collection"
    - "Insight quality: 80%+ actionable by product team"
    - "Feature request accuracy: 90%+ alignment with customer needs"
```

**Tools:** ChatGPT, Claude, Gemini with customer conversation transcripts

---

#### **2. LeadQualifier-Agent** (Low-Level Assistant)
```yaml
agent:
  identity:
    name: "LeadQualifier-Agent"
    level: "Low (Assistant)"
    role: "Inbound lead qualification and routing"
    persona: "Efficient gatekeeper who qualifies leads and books meetings for founders"
  capabilities:
    - "Respond to inbound inquiries within 5 minutes"
    - "Ask qualifying questions (budget, timeline, decision-maker status)"
    - "Score leads (High/Medium/Low priority)"
    - "Book discovery calls on founders' calendars"
    - "Send personalized follow-up sequences"
  guardrails:
    - "Never promise features not yet built"
    - "Escalate to human if prospect asks complex/custom questions"
    - "Never share pricing without confirming budget fit"
  human_oversight:
    - decision_authority: "Co-pilot (50% review of High-priority leads)"
    - escalation_triggers:
      - "Lead score: High (founder reviews before booking)"
      - "Enterprise deal (>$50K ARR)"
      - "Custom requirement mentioned"
  success_metrics:
    - "Response time: <5 minutes (during business hours)"
    - "Qualification accuracy: 85%+ (High leads convert at >30%)"
    - "Meeting show-up rate: >60%"
```

**Tools:** Zapier, Make.com, HubSpot AI, or custom GPT with email/CRM integration

---

#### **3. ContentGenerator-Agent** (Low-Level Assistant)
```yaml
agent:
  identity:
    name: "ContentGenerator-Agent"
    level: "Low (Assistant)"
    role: "Marketing content creation (blog posts, social media, email campaigns)"
    persona: "Creative writer who turns product updates and customer insights into engaging content"
  capabilities:
    - "Draft blog posts (800-1200 words) from product updates"
    - "Generate social media posts (LinkedIn, Twitter) 3x/week"
    - "Write email newsletters (weekly customer updates)"
    - "Create landing page copy for new features"
  guardrails:
    - "All content must be human-reviewed before publishing"
    - "Never fabricate customer quotes or case studies"
    - "Cite sources for data/statistics"
  human_oversight:
    - decision_authority: "Co-pilot (100% human review before publish)"
    - escalation_triggers:
      - "Controversial topic mentioned"
      - "Competitor comparison requested"
  success_metrics:
    - "Content draft time: <2 hours per piece"
    - "Human editing time: <30 minutes per piece (90% AI accuracy)"
    - "Engagement rate: >3% (social), >20% (email opens)"
```

**Tools:** ChatGPT, Jasper, Copy.ai with brand voice guidelines

---

#### **4. FinanceOps-Agent** (Low-Level Assistant)
```yaml
agent:
  identity:
    name: "FinanceOps-Agent"
    level: "Low (Assistant)"
    role: "Bookkeeping, expense tracking, financial reporting"
    persona: "Detail-oriented accountant who keeps financial records clean and current"
  capabilities:
    - "Categorize expenses from bank/credit card feeds"
    - "Generate monthly P&L, cash flow, burn rate reports"
    - "Track runway (months of cash remaining)"
    - "Flag unusual expenses (>$500 or out-of-category)"
    - "Prepare data for tax filings"
  guardrails:
    - "Never authorize payments without human approval"
    - "Flag discrepancies (missing receipts, duplicate charges)"
    - "Escalate cash runway warnings (<3 months)"
  human_oversight:
    - decision_authority: "Supervised (100% human review of reports)"
    - escalation_triggers:
      - "Runway <3 months"
      - "Expense anomaly detected"
      - "Tax deadline approaching"
  success_metrics:
    - "Books closed: <5 days after month-end"
    - "Categorization accuracy: >95%"
    - "Runway forecast accuracy: ±10%"
```

**Tools:** QuickBooks AI, Xero, or custom GPT with accounting data integration

---

#### **5. DevAssist-Agent** (Low-Level Assistant)
```yaml
agent:
  identity:
    name: "DevAssist-Agent"
    level: "Low (Assistant)"
    role: "Code generation, testing, documentation"
    persona: "Junior developer who handles repetitive coding tasks and writes tests/docs"
  capabilities:
    - "Generate boilerplate code (APIs, CRUD operations, database schemas)"
    - "Write unit tests for new features (80%+ coverage target)"
    - "Generate API documentation from code comments"
    - "Suggest code refactoring for readability"
    - "Flag potential bugs or security issues"
  guardrails:
    - "All code must pass human code review before merge"
    - "Never commit directly to main branch"
    - "Flag security vulnerabilities immediately"
  human_oversight:
    - decision_authority: "Co-pilot (100% code review required)"
    - escalation_triggers:
      - "Security vulnerability detected"
      - "Breaking change detected"
      - "Test coverage <70%"
  success_metrics:
    - "Code generation time: 70% faster than manual"
    - "Test coverage: >80% for new features"
    - "Bug introduction rate: <2% (AI-generated code)"
```

**Tools:** GitHub Copilot, Cursor, Tabnine, or custom GPT with codebase context

---

### **1.3 Set Up Your Data Spine**

**Goal:** Create a single source of truth for customer, product, and financial data.

**Human Work (2-4 hours):**

1. **Choose Your Stack:**
   - **CRM:** HubSpot (free tier), Pipedrive, or Airtable
   - **Project Management:** Linear, Notion, or ClickUp
   - **Finance:** QuickBooks, Xero, or Wave (free)
   - **Communication:** Slack + email
   - **Analytics:** Mixpanel, Amplitude (free tier), or Google Analytics

2. **Define Data Contracts:**

Use this prompt:

```yaml
prompt:
  role: "You are a data architect helping a startup define data contracts."
  context: |
    Our tools: [CRM], [Project Management], [Finance], [Communication]
    Our AI agents: CustomerInsights, LeadQualifier, ContentGenerator, FinanceOps, DevAssist
  task: |
    Create data contracts for:
    1. Customer data (fields, sources, access rules)
    2. Financial data (categories, reports, who can access)
    3. Product data (features, releases, metrics)
    4. AI agent telemetry (what each agent logs, where it's stored)
  format: "YAML data contracts"
```

**Output:** `DATA-CONTRACTS.md` file with schemas for each data type.

**See:** [SOLID.AI Architecture — Data Spine](../DOCS/02-architecture.md), [Data Contract Template](../ADOPTION/templates/data-contract.md)

---

### **1.4 Set Up Observability**

**Goal:** Monitor AI agent performance and human-AI collaboration quality.

**Human Work (2-4 hours):**

**Metrics Dashboard (use Notion, Airtable, or Google Sheets):**

| Agent | Success Metric | Target | Actual | Status |
|-------|----------------|--------|--------|--------|
| CustomerInsights-Agent | Time to insights | <24h | 18h | ✅ |
| LeadQualifier-Agent | Response time | <5min | 3min | ✅ |
| LeadQualifier-Agent | Qualification accuracy | >85% | 78% | ⚠️ |
| ContentGenerator-Agent | Draft quality | 90% | 92% | ✅ |
| FinanceOps-Agent | Categorization accuracy | >95% | 97% | ✅ |
| DevAssist-Agent | Test coverage | >80% | 85% | ✅ |

**Weekly Review (30 minutes):**
- What did AI agents do well this week?
- What did humans have to fix/override?
- Where should we increase AI autonomy?
- Where should we add human oversight?

**See:** [SOLID.AI Observability](../DOCS/07-observability.md)

---

## 🏗️ Phase 2: Product-Market Fit Sprint (Week 3-12)

### **Objective:** Use AI leverage to iterate 2x faster on product-market fit.

### **2.1 Run Weekly Build-Measure-Learn Cycles**

**Monday: Build (Founders + DevAssist-Agent)**
- Founders define feature requirements (2 hours)
- DevAssist-Agent generates code, tests, docs (4 hours)
- Founders review, refine, ship (2 hours)

**Tuesday-Thursday: Measure (CustomerInsights-Agent)**
- CustomerInsights-Agent monitors usage, collects feedback
- Daily insights report: What's working? What's not?

**Friday: Learn (Full Team)**
- Weekly retro: Review customer insights, update roadmap
- Decide: Pivot, persevere, or iterate?

**AI Agents in This Phase:**
- CustomerInsights-Agent: Daily feedback analysis
- LeadQualifier-Agent: Book customer interviews (10-15/week)
- ContentGenerator-Agent: Announce new features, drive adoption
- FinanceOps-Agent: Track burn rate, runway, unit economics

**Human Work:**
- Strategic decisions (pivot vs. persevere)
- Customer interviews (10-15/week)
- Feature prioritization
- Code review (DevAssist output)

**Time Saved:** 60-70% (AI handles data collection, analysis, content, code generation)

---

### **2.2 Scale Customer Acquisition (AI-Powered Growth)**

**Goal:** Go from 10 customers → 100 customers without hiring a sales/marketing team.

#### **Add 3 More AI Agents:**

**6. SocialMedia-Agent** (Low-Level Assistant)
```yaml
agent:
  identity:
    name: "SocialMedia-Agent"
    level: "Low (Assistant)"
    role: "Social media engagement and community building"
  capabilities:
    - "Monitor brand mentions across Twitter, LinkedIn, Reddit"
    - "Respond to questions/comments within 1 hour"
    - "Identify influencers/advocates in our space"
    - "Suggest content topics based on trending discussions"
  guardrails:
    - "Never engage in negative/controversial debates"
    - "Escalate brand crises to human immediately"
  human_oversight: "Co-pilot (50% review)"
  success_metrics:
    - "Response time: <1 hour"
    - "Engagement rate: >5%"
    - "Follower growth: +10%/month"
```

**7. EmailNurture-Agent** (Low-Level Assistant)
```yaml
agent:
  identity:
    name: "EmailNurture-Agent"
    level: "Low (Assistant)"
    role: "Lead nurturing and onboarding email sequences"
  capabilities:
    - "Send personalized onboarding emails (Days 1, 3, 7, 14, 30)"
    - "Trigger re-engagement campaigns for inactive users"
    - "A/B test subject lines, CTAs"
    - "Track email performance (opens, clicks, conversions)"
  guardrails:
    - "Never send >3 emails/week per contact"
    - "Honor unsubscribe immediately"
  human_oversight: "Automated (5% spot-check)"
  success_metrics:
    - "Open rate: >25%"
    - "Click rate: >5%"
    - "Conversion rate (trial→paid): >15%"
```

**8. CustomerSuccess-Agent** (Low-Level Assistant)
```yaml
agent:
  identity:
    name: "CustomerSuccess-Agent"
    level: "Low (Assistant)"
    role: "Proactive customer health monitoring and support"
  capabilities:
    - "Monitor product usage (Daily Active Users, feature adoption)"
    - "Identify at-risk customers (declining usage, support tickets)"
    - "Send proactive check-ins ('How can we help you succeed?')"
    - "Create help articles/FAQs from common support questions"
  guardrails:
    - "Escalate churn risk (red flag) to human within 24h"
    - "Never auto-cancel accounts without human approval"
  human_oversight: "Co-pilot (High-risk customers get human outreach)"
  success_metrics:
    - "Churn rate: <5%/month"
    - "Time to resolution (support tickets): <24h"
    - "Customer satisfaction (CSAT): >4.5/5"
```

---

### **2.3 Establish Weekly Operating Rhythm**

**Monday (2 hours):**
- Review metrics dashboard (all 8 AI agents)
- Prioritize week's goals (OKRs or sprint planning)
- DevAssist-Agent drafts code for top 3 features

**Tuesday-Thursday (Customer-Focused):**
- CustomerInsights-Agent analyzes feedback
- Founders run customer interviews (LeadQualifier books them)
- SocialMedia-Agent engages community
- EmailNurture-Agent sends sequences

**Friday (Learning & Planning):**
- Weekly retro: What did we learn?
- CustomerSuccess-Agent reports on health trends
- FinanceOps-Agent shares burn rate, runway
- Update roadmap for next week

**See:** [AI-Native Agile — Scrum](../DOCS/11-ai-native-agile.md)

---

## 📈 Phase 3: Scale to Product-Market Fit (Month 4-12)

### **Objective:** 100 customers → 1,000 customers with same 5-10 person team.

### **3.1 Add Intermediate-Level AI Agents**

**Now that you have product-market fit, upgrade AI agents to handle more complexity:**

#### **9. GrowthStrategist-Agent** (Intermediate-Level Consultant)
```yaml
agent:
  identity:
    name: "GrowthStrategist-Agent"
    level: "Intermediate (Consultant)"
    role: "Growth experimentation and channel optimization"
  capabilities:
    - "Analyze acquisition channels (organic, paid, referral, content)"
    - "Recommend next growth experiments (A/B tests, new channels)"
    - "Calculate LTV:CAC by channel"
    - "Predict 90-day revenue based on current funnel metrics"
  guardrails:
    - "Never recommend channels with <$10K budget without human approval"
    - "Flag experiments with <70% confidence interval"
  human_oversight: "Co-pilot (Founders approve experiments)"
  success_metrics:
    - "Experiment velocity: 2-3 new tests/month"
    - "Win rate: >30% of experiments improve metrics"
    - "LTV:CAC: >3:1"
```

#### **10. RevenueOps-Agent** (Intermediate-Level Coordinator)
```yaml
agent:
  identity:
    name: "RevenueOps-Agent"
    level: "Intermediate (Coordinator)"
    role: "Sales, marketing, and customer success alignment"
  capabilities:
    - "Orchestrate handoffs: Lead → Demo → Trial → Paid → Onboarding"
    - "Identify bottlenecks in conversion funnel"
    - "Trigger alerts when deals stall (e.g., trial user inactive Day 5)"
    - "Generate weekly revenue forecast (MRR, ARR projections)"
  guardrails:
    - "Escalate high-value deals (>$25K ARR) to human"
    - "Never auto-discount without approval"
  human_oversight: "Co-pilot (Founders handle enterprise deals)"
  success_metrics:
    - "Funnel conversion: Lead→Paid >10%"
    - "Trial→Paid conversion: >20%"
    - "Revenue forecast accuracy: ±15%"
```

---

### **3.2 Hire Your First Humans (Strategically)**

**When to hire humans vs. upgrade AI agents:**

| Role Needed | Hire Human? | Or Upgrade AI Agent? |
|-------------|-------------|----------------------|
| **Sales (SMB)** | ❌ No | ✅ Upgrade LeadQualifier to Intermediate (handles full sales cycle) |
| **Sales (Enterprise)** | ✅ Yes (1 human) | AI pre-qualifies, human closes |
| **Customer Success** | ❌ No (until 500 customers) | ✅ CustomerSuccess-Agent handles proactive outreach |
| **Marketing** | ❌ No | ✅ ContentGenerator + SocialMedia + EmailNurture agents |
| **Finance/Ops** | ❌ No (until Series A) | ✅ FinanceOps-Agent + annual CPA for taxes |
| **Product/Eng** | ✅ Yes (1-2 engineers) | DevAssist-Agent accelerates them 3x |
| **Design** | ⚠️ Depends | AI for mockups/iterations, human for brand/vision |

**Hiring Rule:** Only hire humans for:
1. **High-touch relationships** (enterprise sales, key account management)
2. **Creative vision** (brand strategy, product design)
3. **Technical depth** (senior engineers for architecture decisions)

**Result:** 5-10 person team operating with the capacity of 30-50 people.

---

### **3.3 Metrics: AI-Native Startup vs. Traditional Startup**

| Metric | Traditional Startup (20 people) | AI-Native Startup (5-10 people) |
|--------|----------------------------------|----------------------------------|
| **Headcount** | 20 | 5-10 humans + 10-15 AI agents |
| **Monthly Burn** | $150K-$200K | $50K-$80K |
| **Time to PMF** | 12-18 months | 6-12 months |
| **Customer Capacity** | 200-500 customers | 1,000-2,000 customers |
| **Revenue/Employee** | $50K-$100K ARR | $200K-$400K ARR |
| **Fundraising Need** | Seed + Series A ($3M-$5M) | Bootstrapped or small seed ($500K-$1M) |

---

## 🛡️ Governance & Ethics for Startups

### **Principle: Move Fast, But Don't Break Trust**

**AI Transparency:**
- Disclose when customers are interacting with AI (e.g., "This email was drafted by AI and reviewed by our team")
- Never pretend AI is human in sales/support conversations

**Data Privacy:**
- Only use customer data for agreed purposes
- GDPR/CCPA compliance from day one (use tools with built-in compliance)

**Human Oversight:**
- High-stakes decisions (pricing, enterprise deals, customer churn) always reviewed by humans
- Weekly AI agent audit: "What did AI decide this week? Would we have decided differently?"

**See:** [Governance & Ethics](../DOCS/06-governance-ethics.md)

---

## 🎯 Success Metrics: Are You AI-Native?

**Baseline (Traditional Startup):**
- 80% time on busywork, 20% on high-value work
- 5-10% error rate (manual data entry, follow-ups)
- Linear scalability (2x customers = 2x headcount)

**Target (AI-Native Startup):**
- 20% time on busywork, 80% on high-value work
- <1% error rate (AI-enforced consistency)
- Exponential scalability (10x customers = +2-3 headcount)

**Monthly Dashboard:**

| Category | Metric | Target | Actual |
|----------|--------|--------|--------|
| **Efficiency** | % time on high-value work | >70% | ___ |
| **Leverage** | Revenue per employee | >$200K ARR | ___ |
| **Quality** | Error rate (data, processes) | <1% | ___ |
| **Speed** | Feature shipped → customer feedback | <7 days | ___ |
| **Cost** | AI agent cost / human salary | <10% | ___ |
| **Scale** | Customers per team member | >100 | ___ |

---

## 🚀 Quick Start Checklist

**Week 1-2: Foundation**
- [ ] Define Purpose Layer (mission, values, North Star, guardrails)
- [ ] Hire 5 essential AI agents (CustomerInsights, LeadQualifier, ContentGenerator, FinanceOps, DevAssist)
- [ ] Set up Data Spine (CRM, project mgmt, finance, analytics)
- [ ] Create observability dashboard (track AI agent performance)

**Week 3-12: Product-Market Fit Sprint**
- [ ] Run weekly Build-Measure-Learn cycles
- [ ] Add 3 growth AI agents (SocialMedia, EmailNurture, CustomerSuccess)
- [ ] Iterate to 100 customers
- [ ] Establish weekly operating rhythm (Monday planning, Friday retro)

**Month 4-12: Scale**
- [ ] Upgrade to Intermediate-level AI agents (GrowthStrategist, RevenueOps)
- [ ] Scale to 1,000 customers
- [ ] Hire 1-2 humans (only for high-touch roles)
- [ ] Validate AI-Native metrics (>70% time on high-value work, <1% error rate, >$200K revenue/employee)

---

## 💡 Real-World Example: AI-Native SaaS Startup

**Company:** TaskFlow (fictional example)  
**Product:** Project management tool for remote teams  
**Team:** 2 founders (CEO, CTO) + 3 contract engineers  

**Year 1 Results:**
- **Customers:** 0 → 800 paying customers
- **MRR:** $0 → $80K ($1M ARR run-rate)
- **Headcount:** 5 humans + 12 AI agents
- **Burn Rate:** $60K/month (vs. $150K for traditional startup)
- **Funding:** Bootstrapped (no VC)

**AI Agents Deployed:**
1. CustomerInsights-Agent (analyzes 2,000+ customer messages/month)
2. LeadQualifier-Agent (qualifies 400 leads/month, books 80 demos)
3. ContentGenerator-Agent (writes 12 blog posts, 60 social posts/month)
4. FinanceOps-Agent (closes books in 3 days, tracks runway)
5. DevAssist-Agent (generates 40% of codebase, writes 85% of tests)
6. SocialMedia-Agent (responds to 200+ mentions/month)
7. EmailNurture-Agent (sends 10,000 personalized emails/month)
8. CustomerSuccess-Agent (monitors 800 accounts, flags 20 at-risk/month)
9. GrowthStrategist-Agent (runs 3 experiments/month, 35% win rate)
10. RevenueOps-Agent (forecasts MRR with 12% accuracy)
11. Documentation-Agent (maintains knowledge base, 95% self-service support)
12. Recruiter-Agent (screens 100 applicants, shortlists top 10)

**Founder Time Allocation:**
- 60% on product strategy, customer interviews, vision
- 20% on high-value sales (enterprise deals >$10K ARR)
- 10% on fundraising/investor relations
- 10% on AI agent management (weekly reviews, tuning)

**Key Insight:** "We operate like a 40-person company with 5 people. AI handles everything repeatable. Humans focus on everything creative, strategic, and relationship-driven."

---

## 📚 Next Steps

**Master the Fundamentals:**
- [SOLID.AI Overview](../DOCS/00-overview.md) — Framework introduction
- [Principles](../DOCS/01-principles.md) — Foundational principles
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md) — Where humans lead

**Build Your AI Team:**
- [AI Agents Guide](../DOCS/05-ai-agents.md) — How to define agents
- [Role Hierarchy](../DOCS/10-role-hierarchy-human-ai.md) — Levels and autonomy

**Implement:**
- [Adoption Pack](../ADOPTION/) — Templates, checklists, prompts
- [AI-Native Agile](../DOCS/11-ai-native-agile.md) — Weekly operating rhythm

**Get Inspired:**
- [Whole-Organization Transformation](../DOCS/09-whole-organization-transformation.md) — Economics of AI-as-workforce

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
