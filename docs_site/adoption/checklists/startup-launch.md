# Startup Launch Checklist — AI-Native from Day One

**For:** Founders building from square one (0-10 people, limited resources, clear purpose)

**Goal:** Launch an AI-Native organization that operates like a 20-person company with 5-10 humans

**Time:** 2-3 weeks for foundation, 90 days to first customers

---

## Week 1-2: Foundation

### 📋 **Define Your Purpose Layer**

- [ ] **Mission Statement** — 1-2 sentences defining why you exist
- [ ] **Core Values** — 3-5 principles that guide decisions
- [ ] **North Star Metric** — The ONE metric that defines success (e.g., "Active users", "Revenue", "Customer satisfaction")
- [ ] **Ethical Guardrails** — 3-5 non-negotiables (e.g., "Never sell customer data", "Human oversight for high-stakes decisions")
- [ ] **Human Oversight Boundaries** — Where AI must defer to humans (e.g., "Pricing decisions", "Hiring/firing", "Strategic pivots")

**Output:** `PURPOSE.md` file in your repository

**See:** [Principles — Purpose-Led Decisions](../DOCS/01-principles.md)

---

### 🛠️ **Choose Your Initial Tech Stack**

- [ ] **CRM:** HubSpot (free tier), Pipedrive, or Airtable
- [ ] **Project Management:** Linear, Notion, or ClickUp
- [ ] **Finance/Accounting:** QuickBooks, Xero, or Wave (free)
- [ ] **Communication:** Slack + email
- [ ] **Analytics:** Mixpanel, Amplitude (free tier), or Google Analytics
- [ ] **AI Tools:** ChatGPT/Claude/Gemini, Zapier/Make.com, GitHub Copilot

**Budget:** $50-$200/month for all tools

---

### 🤖 **Hire Your First 5 AI Agents**

- [ ] **CustomerInsights-Agent** (Low-Level Analyst)
  - Role: Analyze customer conversations, surface insights
  - Tools: ChatGPT/Claude with customer transcripts
  - Metrics: Time to insights <24h, insight quality >80% actionable

- [ ] **LeadQualifier-Agent** (Low-Level Assistant)
  - Role: Respond to inbound leads, qualify, book meetings
  - Tools: Zapier + HubSpot + AI
  - Metrics: Response time <5min, qualification accuracy >85%

- [ ] **ContentGenerator-Agent** (Low-Level Assistant)
  - Role: Draft blog posts, social media, email campaigns
  - Tools: ChatGPT/Jasper/Copy.ai
  - Metrics: Draft time <2h/piece, human editing time <30min

- [ ] **FinanceOps-Agent** (Low-Level Assistant)
  - Role: Categorize expenses, generate P&L, track runway
  - Tools: QuickBooks AI/Xero
  - Metrics: Books closed <5 days after month-end, categorization >95% accurate

- [ ] **DevAssist-Agent** (Low-Level Assistant)
  - Role: Generate code, write tests, create documentation
  - Tools: GitHub Copilot/Cursor/Tabnine
  - Metrics: Code generation 70% faster, test coverage >80%

**See:** [Agent Definition Template](../ADOPTION/TEMPLATES/agent-definition-template.yaml), [AI Agents Guide](../DOCS/05-ai-agents.md)

---

### 📊 **Set Up Your Data Spine**

- [ ] **Define Data Contracts:**
  - Customer data (fields, sources, access rules)
  - Financial data (categories, reports, who can access)
  - Product data (features, releases, metrics)
  - AI agent telemetry (what each agent logs, where stored)

- [ ] **Create Single Source of Truth:**
  - All customer data flows to CRM
  - All financial data flows to accounting system
  - All product/usage data flows to analytics

- [ ] **Set Access Controls:**
  - Define who (human + AI) can read/write each data type
  - Set up API keys/integrations

**Output:** `DATA-CONTRACTS.md` file

**See:** [Data Contract Template](../ADOPTION/TEMPLATES/data-contract-template.yaml), [Architecture — Data Spine](../DOCS/02-architecture.md)

---

### 📈 **Create Observability Dashboard**

- [ ] **Set Up Metrics Tracking** (use Notion, Airtable, or Google Sheets)

| Agent | Success Metric | Target | Actual |
|-------|----------------|--------|--------|
| CustomerInsights-Agent | Time to insights | <24h | ___ |
| LeadQualifier-Agent | Response time | <5min | ___ |
| LeadQualifier-Agent | Qualification accuracy | >85% | ___ |
| ContentGenerator-Agent | Draft quality | 90% | ___ |
| FinanceOps-Agent | Categorization accuracy | >95% | ___ |
| DevAssist-Agent | Test coverage | >80% | ___ |

- [ ] **Set Up Weekly Review** (30 minutes every Friday)
  - What did AI agents do well this week?
  - What did humans have to fix/override?
  - Where should we increase AI autonomy?
  - Where should we add human oversight?

**See:** [Observability](../DOCS/07-observability.md)

---

### 🗓️ **Establish Weekly Operating Rhythm**

- [ ] **Monday (2 hours):** Planning
  - Review metrics dashboard
  - Prioritize week's goals
  - Assign work (humans + AI agents)

- [ ] **Tuesday-Thursday:** Execution
  - AI agents handle 70-80% of work
  - Humans focus on high-value work (strategy, customer relationships, creative work)

- [ ] **Friday (1 hour):** Learning & Planning
  - Weekly retro: What did we learn?
  - Update metrics dashboard
  - Plan next week

**See:** [AI-Native Agile](../DOCS/11-ai-native-agile.md)

---

## Week 3-12: Product-Market Fit Sprint

### 🚀 **Run Weekly Build-Measure-Learn Cycles**

- [ ] **Monday: Build** (Founders + DevAssist-Agent)
  - Define feature requirements (2 hours)
  - DevAssist-Agent generates code, tests, docs (4 hours)
  - Founders review, refine, ship (2 hours)

- [ ] **Tuesday-Thursday: Measure** (CustomerInsights-Agent)
  - Monitor usage, collect feedback
  - Daily insights report: What's working? What's not?

- [ ] **Friday: Learn** (Full Team)
  - Weekly retro: Review customer insights, update roadmap
  - Decide: Pivot, persevere, or iterate?

---

### 📈 **Scale Customer Acquisition (Add 3 More AI Agents)**

- [ ] **SocialMedia-Agent** (Low-Level Assistant)
  - Role: Monitor brand mentions, respond to questions, identify influencers
  - Metrics: Response time <1h, engagement rate >5%

- [ ] **EmailNurture-Agent** (Low-Level Assistant)
  - Role: Send onboarding sequences, re-engagement campaigns
  - Metrics: Open rate >25%, click rate >5%, conversion >15%

- [ ] **CustomerSuccess-Agent** (Low-Level Assistant)
  - Role: Monitor product usage, identify at-risk customers, send proactive check-ins
  - Metrics: Churn rate <5%/month, CSAT >4.5/5

---

### 🎯 **Set 90-Day Goals**

- [ ] **Customer Metrics:**
  - Target: ___ paying customers (e.g., 10-100)
  - MRR/ARR: $___ (e.g., $5K-$50K MRR)

- [ ] **Product Metrics:**
  - Features shipped: ___ (e.g., 5-10 major features)
  - User feedback: ___ customer interviews completed (e.g., 30-50)

- [ ] **Team Metrics:**
  - AI agents deployed: ___ (target: 8-10)
  - % time on high-value work: >70%
  - Burn rate: $___ /month (target: <$80K)

- [ ] **Quality Metrics:**
  - Error rate: <1% (AI-enforced consistency)
  - Customer satisfaction: >4/5

---

## Month 4-12: Scale to Product-Market Fit

### 🔧 **Upgrade to Intermediate-Level AI Agents**

- [ ] **GrowthStrategist-Agent** (Intermediate-Level Consultant)
  - Role: Analyze acquisition channels, recommend experiments, calculate LTV:CAC
  - Metrics: 2-3 experiments/month, >30% win rate, LTV:CAC >3:1

- [ ] **RevenueOps-Agent** (Intermediate-Level Coordinator)
  - Role: Orchestrate Lead → Demo → Trial → Paid workflow
  - Metrics: Funnel conversion >10%, trial→paid >20%

---

### 👥 **Decide When to Hire Humans (vs. Upgrade AI Agents)**

| Role Needed | Hire Human? | Or Upgrade AI Agent? |
|-------------|-------------|----------------------|
| Sales (SMB) | ❌ No | ✅ Upgrade LeadQualifier to Intermediate |
| Sales (Enterprise) | ✅ Yes (1 human) | AI pre-qualifies, human closes |
| Customer Success | ❌ No (until 500 customers) | ✅ CustomerSuccess-Agent handles proactive outreach |
| Marketing | ❌ No | ✅ ContentGenerator + SocialMedia + EmailNurture |
| Finance/Ops | ❌ No (until Series A) | ✅ FinanceOps-Agent + annual CPA for taxes |
| Product/Eng | ✅ Yes (1-2 engineers) | DevAssist-Agent accelerates them 3x |

**Hiring Rule:** Only hire humans for high-touch relationships, creative vision, or technical depth.

---

### 📊 **Validate AI-Native Metrics (12 months)**

| Category | Metric | Target | Actual |
|----------|--------|--------|--------|
| **Efficiency** | % time on high-value work | >70% | ___ |
| **Leverage** | Revenue per employee | >$200K ARR | ___ |
| **Quality** | Error rate | <1% | ___ |
| **Speed** | Feature shipped → customer feedback | <7 days | ___ |
| **Cost** | AI agent cost / human salary | <10% | ___ |
| **Scale** | Customers per team member | >100 | ___ |

---

## 🛡️ Governance & Ethics

### **AI Transparency**
- [ ] Disclose when customers interact with AI (e.g., "This email drafted by AI, reviewed by our team")
- [ ] Never pretend AI is human in sales/support conversations

### **Data Privacy**
- [ ] Only use customer data for agreed purposes
- [ ] GDPR/CCPA compliance from day one (use tools with built-in compliance)

### **Human Oversight**
- [ ] High-stakes decisions (pricing, enterprise deals, customer churn) always reviewed by humans
- [ ] Weekly AI agent audit: "What did AI decide this week? Would we have decided differently?"

**See:** [Governance & Ethics](../DOCS/06-governance-ethics.md), [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)

---

## 📚 Resources

**Playbook:**
- [🚀 AI-Native Startup](../PLAYBOOKS/by-stage/startup-ai-native.md)

**Templates:**
- [Agent Definition](../ADOPTION/TEMPLATES/agent-definition-template.yaml)
- [Data Contract](../ADOPTION/TEMPLATES/data-contract-template.yaml)
- [Squad Charter](../ADOPTION/TEMPLATES/squad-charter-template.md)

**Checklists:**
- [AI Agent Integration](ai-agent-integration.md)
- [Data Spine Implementation](data-spine-implementation.md)

**Docs:**
- [Overview](../DOCS/00-overview.md)
- [Principles](../DOCS/01-principles.md)
- [AI Agents](../DOCS/05-ai-agents.md)
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
