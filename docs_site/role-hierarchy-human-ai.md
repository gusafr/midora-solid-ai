# Role Hierarchy: Human & AI Agent Progression

**Defining specialization, autonomy, and strategic impact across organizational levels**

---

## Overview

SOLID.AI recognizes that both **humans and AI agents** operate at different levels of specialization, autonomy, and strategic impact. This document defines a **4-level hierarchy** that applies to both human collaborators and AI agents, establishing clear expectations for capabilities, decision-making authority, and organizational relevance at each tier.

**Key Principle:** As roles progress from **Low → Intermediate → High → Executive**, they transition from:
- **Task execution** → **Coordination** → **Strategic decision-making** → **Organizational leadership**
- **Narrow scope** → **Broader context** → **Domain expertise** → **Cross-domain vision**
- **Supervised** → **Semi-autonomous** → **Autonomous** → **Governing**

---

## Visual Framework

The following diagram illustrates the complete 4-level hierarchy with decision authority, AI delegation patterns, compensation ranges, and career progression paths:

```mermaid
--8<-- "../DIAGRAMS/role-hierarchy-framework.mmd"
```

💡 **Tip:** This visual shows how each level differs in strategic impact, decision authority, and AI collaboration patterns. Use it for role definitions, career planning, and organizational design.

---

## The 4-Level Role Hierarchy

### Level 1: Low Level — Assistant & Analyst

**Purpose:** Execute well-defined tasks, provide data-driven insights, support higher-level roles

**Scope:** Narrow, single-domain, task-oriented

**Autonomy:** Supervised (human review required)

#### Human Roles

**Assistant (Low Level — Human)**

**Responsibilities:**
- Execute routine, repetitive tasks following established procedures
- Provide administrative support (scheduling, documentation, data entry)
- Escalate exceptions or ambiguities to higher levels
- Learn organizational processes and tools

**Examples:**
- Sales Development Rep (SDR): Qualify inbound leads, book meetings for Account Executives
- Finance Assistant: Process expense reports, reconcile invoices
- HR Coordinator: Schedule interviews, manage candidate communication
- Marketing Coordinator: Schedule social posts, update website content

**Success Metrics:**
- Task completion rate (95%+)
- Accuracy (98%+)
- Response time (SLA compliance)
- Volume throughput (e.g., 50 leads qualified/week)

**Decision Authority:**
- **Can decide:** How to execute assigned task within guidelines
- **Cannot decide:** Strategic priorities, exceptions to policy, budget allocation

---

**Analyst (Low Level — Human)**

**Responsibilities:**
- Gather, clean, and analyze data to surface insights
- Create reports and dashboards for decision-makers
- Identify patterns, trends, and anomalies
- Support strategic decisions with data-driven recommendations

**Examples:**
- Data Analyst: Build SQL queries, create dashboards, analyze A/B tests
- Business Analyst: Map business processes, identify optimization opportunities
- Financial Analyst: Prepare budget variance reports, forecast models
- Market Research Analyst: Survey analysis, competitive intelligence

**Success Metrics:**
- Report accuracy (99%+)
- Insight quality (actionable, clear, timely)
- Data timeliness (real-time vs. batch)
- Stakeholder satisfaction with analysis

**Decision Authority:**
- **Can decide:** Which data sources to use, how to visualize insights
- **Cannot decide:** Which initiatives to prioritize, how to respond to findings

---

#### AI Agent Roles

**Assistant-Agent (Low Level — AI)**

**Responsibilities:**
- Automate repetitive, high-volume tasks (data entry, email responses, document generation)
- Provide instant answers to FAQs (chatbots, knowledge base queries)
- Trigger workflows based on predefined rules (if X, then Y)
- Flag exceptions for human review

**Examples:**
- **InvoiceProcessor-Agent**: Extract data from invoices, match to POs, route for approval
- **LeadQualifier-Agent**: Score inbound leads, enrich with firmographic data, assign to SDRs
- **OnboardingAssistant-Agent**: Send welcome emails, provision accounts, assign training modules
- **ChatbotSupport-Agent**: Answer tier-1 customer questions, escalate complex issues to humans

**Agent Definition Template:**
```yaml
agent:
  identity:
    name: "InvoiceProcessor-Agent"
    level: "Low (Assistant)"
    role: "Automate invoice data extraction and validation"
    persona: "Meticulous accountant, never skips a step"
  
  capabilities:
    - task: "Extract invoice data from PDFs"
      input: "Invoice document (PDF, image, email)"
      output: "Structured data (vendor, amount, date, line items)"
      performance: "98% accuracy, 5-second processing"
  
  guardrails:
    prohibited:
      - "Do not auto-approve invoices >$5K without human review"
      - "Do not pay invoices from unknown vendors"
    boundaries:
      - "Escalate mismatches >10% to human immediately"
  
  human_oversight:
    autonomy_level: "supervised"
    review: "Finance team reviews all processed invoices before payment"
    escalation: "Accountant handles complex cases (foreign currency, partial shipments)"
  
  success_metrics:
    value:
      - "Processing time: 5 seconds/invoice (vs. 10 minutes manual)"
      - "Accuracy: 98%"
    ethical:
      - "Zero fraudulent payments due to AI error"
      - "100% audit trail compliance"
```

**Autonomy:** **Supervised** (always requires human review before final action)

**Decision Authority:**
- **Can decide:** How to categorize data, which template to use, when to escalate
- **Cannot decide:** Whether to approve payment, override policy, handle exceptions

---

**Analyst-Agent (Low Level — AI)**

**Responsibilities:**
- Analyze large datasets to identify patterns, trends, anomalies
- Generate reports and visualizations automatically
- Predict outcomes based on historical data (forecasting, risk scoring)
- Surface insights for human decision-makers

**Examples:**
- **SalesForecasting-Agent**: Predict quarterly revenue based on pipeline, win rates, seasonality
- **ChurnPrediction-Agent**: Identify customers at risk of cancellation (behavior patterns, engagement drop)
- **SentimentAnalysis-Agent**: Monitor brand mentions, detect PR risks early
- **FraudDetection-Agent**: Flag suspicious transactions for fraud team review

**Agent Definition Template:**
```yaml
agent:
  identity:
    name: "ChurnPrediction-Agent"
    level: "Low (Analyst)"
    role: "Identify customers at risk of cancellation"
    persona: "Data-driven early warning system"
  
  capabilities:
    - task: "Score customer churn risk"
      input: "Customer usage data, support tickets, payment history, engagement metrics"
      output: "Churn risk score (0-100) + reasoning (e.g., 'Usage down 50% last 30 days')"
      performance: "Predicts 70% of churn 3+ months early"
  
  guardrails:
    prohibited:
      - "Do not auto-cancel accounts based on churn score"
      - "Do not contact customers directly without human approval"
    boundaries:
      - "Escalate VIP/high-value customers (>$100K ARR) to Account Manager immediately"
  
  human_oversight:
    autonomy_level: "automated (insights only)"
    review: "Customer Success reviews weekly churn report, prioritizes outreach"
    escalation: "GM reviews monthly for model accuracy, bias"
  
  success_metrics:
    value:
      - "Churn prediction accuracy: 70% at 3+ months early warning"
      - "False positive rate: <20% (don't cry wolf)"
    ethical:
      - "No demographic bias in churn scoring"
      - "Transparent scoring criteria (explainable AI)"
```

**Autonomy:** **Automated (insights only)** (provides analysis, humans decide action)

**Decision Authority:**
- **Can decide:** Which data to analyze, how to model patterns
- **Cannot decide:** How to respond to insights (e.g., offer discount, contact customer)

---

### Level 2: Intermediate Level — Consultant & Coordinator

**Purpose:** Coordinate workflows, provide expert advice, manage cross-functional processes

**Scope:** Multi-domain, process-oriented, stakeholder management

**Autonomy:** Semi-autonomous (human approval for significant decisions)

#### Human Roles

**Consultant (Intermediate Level — Human)**

**Responsibilities:**
- Provide expert advice in specialized domain (technology, strategy, finance, HR)
- Design solutions to complex problems (not just analysis, but recommendations)
- Guide clients/stakeholders through decision-making processes
- Transfer knowledge (training, documentation, mentoring)

**Examples:**
- Management Consultant: Advise clients on business model, operations, digital transformation
- Solutions Architect: Design technical systems, advise on technology stack
- Financial Advisor: Recommend investment strategies, tax optimization
- HR Business Partner: Advise managers on talent strategy, org design, compensation

**Success Metrics:**
- Client satisfaction (NPS >70)
- Recommendation adoption rate (60%+)
- Problem resolution time
- Knowledge transfer effectiveness (clients can self-serve after engagement)

**Decision Authority:**
- **Can decide:** Recommended approach, solution design, priorities within engagement
- **Cannot decide:** Client's final decision (advisory, not prescriptive), budget sign-off

---

**Coordinator (Intermediate Level — Human)**

**Responsibilities:**
- Orchestrate workflows across teams, departments, or functions
- Manage schedules, resources, dependencies
- Ensure communication flows smoothly (no dropped handoffs)
- Resolve bottlenecks and escalate blockers

**Examples:**
- Program Manager: Coordinate multi-team initiatives, track dependencies, remove roadblocks
- Supply Chain Coordinator: Manage logistics across suppliers, warehouses, transportation
- Event Coordinator: Orchestrate conferences, trade shows (vendors, speakers, logistics)
- Scrum Master: Facilitate agile ceremonies, remove impediments, coach teams

**Success Metrics:**
- On-time delivery rate (90%+)
- Stakeholder satisfaction
- Bottleneck resolution time
- Resource utilization (minimize idle time, over-allocation)

**Decision Authority:**
- **Can decide:** How to sequence tasks, resource allocation within budget
- **Cannot decide:** Strategic priorities, scope changes, budget increases

---

#### AI Agent Roles

**Consultant-Agent (Intermediate Level — AI)**

**Responsibilities:**
- Provide expert recommendations based on deep domain knowledge
- Design solutions by combining multiple data sources, models, constraints
- Personalize advice based on context (customer segment, use case, constraints)
- Explain reasoning transparently (not black-box)

**Examples:**
- **FinancialAdvisor-Agent**: Recommend investment allocations based on risk tolerance, goals, tax situation
- **TechStackAdvisor-Agent**: Suggest technology stack (languages, frameworks, infrastructure) based on team skills, scale, budget
- **HiringStrategy-Agent**: Advise on recruiting channels, job descriptions, interview process for specific roles
- **MarketingMix-Agent**: Recommend channel allocation (SEO, paid ads, content, events) based on product, audience, budget

**Agent Definition Template:**
```yaml
agent:
  identity:
    name: "TechStackAdvisor-Agent"
    level: "Intermediate (Consultant)"
    role: "Recommend optimal technology stack for projects"
    persona: "Experienced architect, pragmatic, balances trade-offs"
  
  capabilities:
    - task: "Recommend tech stack"
      input: "Project requirements (scale, team skills, budget, timeline, compliance)"
      output: "Recommended stack (languages, frameworks, databases, infrastructure) + trade-off analysis"
      performance: "85% of recommendations accepted by engineering teams"
  
  guardrails:
    prohibited:
      - "Do not recommend technologies team has no expertise in (high risk)"
      - "Do not ignore compliance requirements (e.g., HIPAA, PCI-DSS)"
      - "Do not recommend vendor lock-in without explicit justification"
    boundaries:
      - "Escalate to CTO if recommendation conflicts with architectural standards"
  
  human_oversight:
    autonomy_level: "co-pilot"
    review: "Engineering lead reviews recommendation, makes final decision"
    escalation: "CTO approves major platform decisions (e.g., migrate to new cloud provider)"
  
  success_metrics:
    value:
      - "Recommendation quality: 85% acceptance rate"
      - "Time saved: 10 hours/project (vs. manual research)"
    ethical:
      - "Transparent trade-offs (cost, complexity, risk)"
      - "No vendor bias (recommend best fit, not highest commission)"
```

**Autonomy:** **Co-pilot** (provides expert recommendation, human makes final call)

**Decision Authority:**
- **Can decide:** Recommended approach, trade-off analysis
- **Cannot decide:** Final technology choice (human decides, AI advises)

---

**Coordinator-Agent (Intermediate Level — AI)**

**Responsibilities:**
- Orchestrate multi-step workflows across systems and teams
- Manage dependencies (trigger task B when task A completes)
- Route work to appropriate teams/agents based on context
- Monitor progress, detect delays, escalate blockers

**Examples:**
- **OrderOrchestrator-Agent**: Coordinate order fulfillment (payment → inventory → shipping → delivery → customer notification)
- **HiringWorkflow-Agent**: Orchestrate recruiting (job posting → resume screening → interview scheduling → offer generation)
- **IncidentResponse-Agent**: Coordinate incident resolution (alert → triage → assign → communicate → resolve → post-mortem)
- **CampaignLaunch-Agent**: Orchestrate marketing campaign (creative → legal review → ad setup → email send → analytics)

**Agent Definition Template:**
```yaml
agent:
  identity:
    name: "OrderOrchestrator-Agent"
    level: "Intermediate (Coordinator)"
    role: "Coordinate end-to-end order fulfillment"
    persona: "Air traffic controller, keeps everything moving smoothly"
  
  capabilities:
    - task: "Orchestrate order fulfillment workflow"
      input: "Order placed event (customer, items, shipping address, payment method)"
      output: "Triggered workflows (payment processing, inventory reservation, shipping label, delivery tracking, customer notifications)"
      performance: "95% of orders fulfilled within SLA (24-48 hours)"
  
  guardrails:
    prohibited:
      - "Do not ship orders with failed payment"
      - "Do not auto-substitute items without customer approval"
      - "Do not exceed promised delivery date without notification"
    boundaries:
      - "Escalate to operations manager if inventory insufficient (stockout)"
      - "Escalate to customer service if delivery delayed >24 hours"
  
  human_oversight:
    autonomy_level: "automated"
    review: "Operations team monitors dashboard, handles exceptions"
    escalation: "Manager intervenes for VIP customers, high-value orders (>$10K)"
  
  success_metrics:
    value:
      - "On-time fulfillment: 95%"
      - "Order accuracy: 99%"
      - "Customer satisfaction: NPS >70"
    ethical:
      - "Transparent delivery estimates (no overpromising)"
      - "Fair treatment (no preferential fulfillment unless explicitly tiered service)"
```

**Autonomy:** **Automated** (orchestrates routine workflows independently, escalates exceptions)

**Decision Authority:**
- **Can decide:** Which team/agent to route tasks to, when to trigger next step
- **Cannot decide:** How to handle exceptions (stockouts, payment failures, delivery delays)

---

### Level 3: High Level — Specialist & Manager

**Purpose:** Deep domain expertise, team leadership, strategic decision-making within function

**Scope:** Cross-functional, strategic, long-term impact

**Autonomy:** Autonomous (makes decisions, accountable for outcomes)

#### Human Roles

**Specialist (High Level — Human)**

**Responsibilities:**
- Serve as subject matter expert (SME) in specialized domain
- Solve complex, novel problems requiring deep expertise
- Advise leadership on strategic decisions in domain
- Develop best practices, standards, frameworks

**Examples:**
- Principal Engineer: Architect complex systems, define technical standards, mentor engineers
- Tax Specialist (CPA): Navigate complex tax regulations, optimize tax strategy, advise CFO
- Clinical Specialist (MD): Handle rare/complex medical cases, develop treatment protocols, train residents
- Cybersecurity Specialist (CISO): Design security architecture, respond to breaches, advise CEO on risk

**Success Metrics:**
- Problem resolution success rate (complex cases)
- Strategic impact (influence on company direction)
- Knowledge dissemination (documentation, training, mentorship)
- Peer recognition (thought leadership, publications, speaking)

**Decision Authority:**
- **Can decide:** Technical/domain strategy within function, hiring in domain, budget for domain initiatives
- **Cannot decide:** Cross-functional priorities, company-wide strategic direction

---

**Manager (High Level — Human)**

**Responsibilities:**
- Lead team of 5-20 people (assistants, analysts, consultants, coordinators)
- Set goals, allocate resources, manage performance
- Remove blockers, resolve conflicts, develop talent
- Translate strategic objectives into tactical execution

**Examples:**
- Engineering Manager: Lead 8-12 engineers, deliver product roadmap, grow team capabilities
- Sales Manager: Lead 6-10 Account Executives, hit revenue targets, coach reps
- Finance Manager: Lead accounting team, ensure accurate reporting, optimize processes
- HR Manager: Lead recruiting + employee relations, reduce time-to-hire, improve retention

**Success Metrics:**
- Team performance (delivery, quality, velocity)
- Employee engagement (retention, satisfaction, growth)
- Operational excellence (SLA compliance, process efficiency)
- Strategic goal attainment (OKRs, KPIs)

**Decision Authority:**
- **Can decide:** Team structure, hiring, performance management, budget allocation within function
- **Cannot decide:** Company strategy, cross-functional priorities (requires exec alignment)

---

#### AI Agent Roles

**Specialist-Agent (High Level — AI)**

**Responsibilities:**
- Apply deep domain expertise to complex, novel problems
- Reason across multiple constraints, data sources, scenarios
- Provide strategic recommendations (not just tactical)
- Continuously learn from outcomes (improve over time)

**Examples:**
- **LegalContractAnalyzer-Agent**: Review complex contracts (M&A, partnerships), flag risks, suggest negotiation points
- **DrugInteractionSpecialist-Agent**: Analyze complex medication regimens (10+ drugs), recommend adjustments for patient safety
- **SupplyChainOptimizer-Agent**: Design multi-tier supply chain networks (cost, resilience, sustainability trade-offs)
- **CyberThreatHunter-Agent**: Detect advanced persistent threats (APTs), correlate signals across logs, recommend remediation

**Agent Definition Template:**
```yaml
agent:
  identity:
    name: "LegalContractAnalyzer-Agent"
    level: "High (Specialist)"
    role: "Review complex legal contracts, identify risks, suggest mitigations"
    persona: "Experienced corporate attorney, detail-oriented, strategic thinker"
  
  capabilities:
    - task: "Analyze M&A contract"
      input: "250-page purchase agreement + due diligence data"
      output: "Risk report (red flags, liabilities, negotiation leverage points) + suggested edits"
      performance: "Identifies 95% of risks flagged by human legal review, 10x faster"
  
  guardrails:
    prohibited:
      - "Do not auto-sign contracts (human attorney must review and approve)"
      - "Do not miss material risks (e.g., indemnification clauses, IP transfers)"
      - "Do not recommend illegal or unethical terms"
    boundaries:
      - "Escalate to General Counsel if contract involves >$50M value, litigation risk, or novel legal issues"
  
  human_oversight:
    autonomy_level: "co-pilot"
    review: "Corporate attorney reviews AI analysis, makes final legal judgment"
    escalation: "General Counsel approves high-stakes contracts"
  
  success_metrics:
    value:
      - "Risk identification accuracy: 95%"
      - "Review time: 2 hours (vs. 20 hours human)"
      - "Cost savings: $200K/year (external counsel fees)"
    ethical:
      - "No legal malpractice due to AI error"
      - "100% explainability (AI shows which clauses triggered risk flags)"
```

**Autonomy:** **Co-pilot** (provides expert analysis, human specialist makes final judgment)

**Decision Authority:**
- **Can decide:** Risk assessment, recommended mitigations
- **Cannot decide:** Whether to sign contract, final legal judgment

---

**Manager-Agent (High Level — AI)**

**Responsibilities:**
- Coordinate team of AI agents (orchestrate multi-agent workflows)
- Allocate resources (compute, data, API calls) dynamically
- Monitor agent performance, retrain underperforming agents
- Escalate systemic issues to human leadership

**Examples:**
- **CustomerServiceManager-Agent**: Coordinate chatbot, email-agent, voice-agent; route tickets based on complexity, language, urgency
- **MarketingCampaignManager-Agent**: Coordinate content-writer-agent, ad-optimizer-agent, analytics-agent for campaign execution
- **DataPipelineManager-Agent**: Coordinate ETL-agents, validate data quality, retry failures, alert on anomalies
- **IncidentCommandCenter-Agent**: Coordinate detection-agent, triage-agent, remediation-agent during outages

**Agent Definition Template:**
```yaml
agent:
  identity:
    name: "CustomerServiceManager-Agent"
    level: "High (Manager)"
    role: "Coordinate AI agents handling customer support, optimize resolution"
    persona: "Service operations leader, data-driven, customer-obsessed"
  
  capabilities:
    - task: "Route customer tickets to appropriate agent"
      input: "Incoming ticket (channel, language, sentiment, complexity)"
      output: "Assignment to chatbot (tier 1), email-agent (tier 2), or human (tier 3)"
      performance: "95% of tier-1 tickets resolved by chatbot, <5 min response time"
    
    - task: "Monitor agent performance, retrain underperformers"
      input: "Agent metrics (resolution rate, customer satisfaction, handle time)"
      output: "Retraining jobs triggered for agents below 80% CSAT"
      performance: "Agent performance improves 10% per quarter"
  
  guardrails:
    prohibited:
      - "Do not route VIP customers to chatbot (human-first for high-value)"
      - "Do not ignore escalations (if tier-1 agent fails 3x, escalate to human)"
    boundaries:
      - "Escalate to human manager if ticket volume spikes >50% (potential incident)"
  
  human_oversight:
    autonomy_level: "automated"
    review: "Customer service manager reviews dashboard weekly, adjusts routing rules"
    escalation: "VP Customer Success intervenes for systemic issues (agent failures, customer complaints)"
  
  success_metrics:
    value:
      - "Tier-1 resolution rate: 80% (chatbot handles 8 of 10 tickets)"
      - "Customer satisfaction: NPS >60"
      - "Cost per ticket: 50% reduction vs. all-human support"
    ethical:
      - "No customer trapped in bot loop (always option to escalate to human)"
      - "Fair treatment (no demographic bias in routing)"
```

**Autonomy:** **Automated** (manages agent team independently, escalates systemic issues)

**Decision Authority:**
- **Can decide:** Agent routing logic, resource allocation, retraining triggers
- **Cannot decide:** Strategic changes to support model (SLAs, staffing, pricing)

---

### Level 4: Executive Level — Director

**Purpose:** Set strategic vision, allocate resources across organization, lead transformational change

**Scope:** Organizational, cross-functional, long-term (3-5 year horizon)

**Autonomy:** Governing (sets direction, accountable to CEO/Board)

#### Human Roles

**Director (Executive Level — Human)**

**Responsibilities:**
- Set strategic vision and priorities for function or business unit
- Allocate budget, headcount, and resources across teams
- Lead organizational transformation (process redesign, cultural change, M&A integration)
- Represent function in executive leadership team (peer to VP, CXO)
- Develop talent pipeline (hire, promote, retain leaders)

**Examples:**
- VP Engineering: Set product roadmap, allocate engineering resources, build technical culture
- CFO: Set financial strategy, capital allocation, investor relations
- Chief Medical Officer (CMO): Set clinical standards, quality protocols, physician training
- Chief Human Resources Officer (CHRO): Set talent strategy, compensation philosophy, culture

**Success Metrics:**
- Strategic goal attainment (3-5 year OKRs)
- Financial performance (revenue, profit, ROI)
- Organizational health (engagement, retention, diversity)
- Market position (competitive advantage, innovation, reputation)

**Decision Authority:**
- **Can decide:** Functional strategy, budget allocation, major hires, org structure
- **Cannot decide:** Company-wide strategy (requires CEO/Board), M&A (requires Board)

---

#### AI Agent Roles

**Director-Agent (Executive Level — AI)**

**Responsibilities:**
- Synthesize data across entire organization to inform strategic decisions
- Model long-term scenarios (3-5 year forecasts, sensitivity analysis)
- Recommend resource allocation (budget, headcount, technology investment)
- Monitor organizational health metrics, flag strategic risks early
- Advise CEO/Board on data-driven strategic decisions

**Examples:**
- **StrategicPlanning-Agent**: Model 5-year revenue scenarios based on market trends, competitive moves, investment options
- **CapitalAllocation-Agent**: Recommend budget allocation across departments, products, geographies (ROI optimization)
- **TalentStrategy-Agent**: Forecast hiring needs, skill gaps, retention risks; recommend talent investments
- **RiskManagement-Agent**: Monitor enterprise risks (financial, operational, reputational), recommend mitigations

**Agent Definition Template:**
```yaml
agent:
  identity:
    name: "StrategicPlanning-Agent"
    level: "Executive (Director)"
    role: "Model long-term strategic scenarios, advise CEO on strategic decisions"
    persona: "Chief Strategy Officer, visionary, data-driven, pragmatic"
  
  capabilities:
    - task: "Model 5-year revenue scenarios"
      input: "Market data, competitive intelligence, product roadmap, investment options"
      output: "3 scenarios (conservative, base, aggressive) with probability-weighted outcomes, key assumptions, risks"
      performance: "Forecasts within 15% accuracy at 3-year horizon"
    
    - task: "Recommend strategic resource allocation"
      input: "Budget constraints, strategic priorities, ROI models"
      output: "Recommended allocation (by department, product, geography) + trade-off analysis"
      performance: "Recommendations increase ROI 20% vs. status quo"
  
  guardrails:
    prohibited:
      - "Do not make strategic decisions autonomously (advisory only to CEO)"
      - "Do not recommend unethical strategies (e.g., deceive customers, exploit labor)"
      - "Do not ignore long-term risks for short-term gains"
    boundaries:
      - "Escalate to Board if recommendation involves >$100M investment, M&A, or existential risk"
  
  human_oversight:
    autonomy_level: "advisory-only"
    review: "CEO reviews strategic recommendations, makes final decisions"
    escalation: "Board approves major strategic pivots, M&A, capital raises"
  
  success_metrics:
    value:
      - "Strategic forecast accuracy: ±15% at 3 years"
      - "Resource allocation ROI: +20% vs. baseline"
      - "Decision quality: CEO satisfaction >90%"
    ethical:
      - "No strategic recommendations violate company values or ethics"
      - "Transparent assumptions (CEO understands model logic)"
      - "Long-term thinking (5-year horizon, not quarterly earnings focus)"
```

**Autonomy:** **Advisory-only** (provides strategic analysis and recommendations, CEO/Board makes final decisions)

**Decision Authority:**
- **Can decide:** Scenario modeling approach, data sources, assumptions
- **Cannot decide:** Strategic direction (CEO decides), capital allocation (Board approves)

---

## Role Progression Pathways

### Human Career Progression

**Individual Contributor (IC) Track:**
```
Low Level:        Assistant → Analyst
                       ↓
Intermediate:     Consultant (Domain Expert)
                       ↓
High Level:       Specialist (SME, Thought Leader)
                       ↓
Executive:        Principal/Fellow (Strategic Advisor to CEO)
```

**Management Track:**
```
Low Level:        Assistant → Analyst
                       ↓
Intermediate:     Coordinator (Team Lead, 2-3 people)
                       ↓
High Level:       Manager (Team of 5-20)
                       ↓
Executive:        Director/VP (Function of 50-200)
                       ↓
C-Suite:          CXO (Organization of 500+)
```

---

### AI Agent Progression

**Agent Evolution Path:**
```
Low Level:        Assistant-Agent → Analyst-Agent
                  (Task automation)   (Insight generation)
                       ↓
Intermediate:     Consultant-Agent → Coordinator-Agent
                  (Expert advice)     (Multi-agent orchestration)
                       ↓
High Level:       Specialist-Agent → Manager-Agent
                  (Complex reasoning) (Agent team leadership)
                       ↓
Executive:        Director-Agent
                  (Strategic planning, organizational-level recommendations)
```

**Evolution Triggers:**
- **Performance:** Agent consistently exceeds metrics (95%+ accuracy, 90%+ user satisfaction)
- **Complexity:** Agent handles increasingly complex tasks (multi-step reasoning, cross-domain synthesis)
- **Autonomy:** Agent requires less human oversight (supervised → co-pilot → automated)
- **Impact:** Agent's decisions drive measurable business outcomes (cost savings, revenue growth, risk reduction)

---

## Autonomy Levels by Role Level

| Role Level | Human Autonomy | AI Agent Autonomy | Human Oversight Required |
|------------|----------------|-------------------|--------------------------|
| **Low (Assistant/Analyst)** | Supervised (manager reviews all work) | **Supervised** (human approves before action) | 100% (every decision reviewed) |
| **Intermediate (Consultant/Coordinator)** | Semi-autonomous (manager spot-checks) | **Co-pilot** (human makes final call, AI advises) | 20-50% (significant decisions reviewed) |
| **High (Specialist/Manager)** | Autonomous (accountable for outcomes) | **Automated** (AI acts, human reviews exceptions) | 5-10% (exception handling, quality assurance) |
| **Executive (Director)** | Governing (sets strategy, accountable to Board) | **Advisory-only** (AI recommends, human decides) | 100% (all strategic decisions human-led) |

---

## Decision Authority Matrix

| Decision Type | Assistant/Analyst | Consultant/Coordinator | Specialist/Manager | Director (Executive) |
|---------------|-------------------|------------------------|--------------------|-----------------------|
| **Task Execution** | ✅ Can decide | ✅ Can decide | ✅ Can decide | ❌ Delegates |
| **Process Design** | ❌ Cannot decide | ✅ Can recommend | ✅ Can decide | ✅ Can decide |
| **Resource Allocation** | ❌ Cannot decide | ⚠️ Within budget | ✅ Can decide (dept) | ✅ Can decide (org) |
| **Hiring** | ❌ Cannot decide | ❌ Cannot decide | ✅ Can decide (team) | ✅ Can decide (function) |
| **Strategic Priorities** | ❌ Cannot decide | ❌ Cannot decide | ⚠️ Functional only | ✅ Can decide |
| **Budget Sign-off** | ❌ Cannot decide | ⚠️ Small (<$10K) | ⚠️ Department | ✅ Function/Org |

**Legend:**
- ✅ Full authority to decide
- ⚠️ Limited authority (with constraints)
- ❌ No authority (must escalate)

---

## Compensation & Valuation by Level

### Human Compensation Benchmarks (US Tech Industry, 2025)

| Role Level | Example Titles | Typical Compensation (Total) |
|------------|----------------|------------------------------|
| **Low Level** | Assistant, Analyst | $50K - $90K |
| **Intermediate** | Consultant, Coordinator | $90K - $150K |
| **High Level** | Specialist, Manager | $150K - $300K |
| **Executive** | Director, VP | $300K - $1M+ |

---

### AI Agent "Cost" (Cloud Infrastructure + Licensing)

| Agent Level | Compute/Storage | Licensing (if proprietary models) | Total Annual Cost |
|-------------|-----------------|-----------------------------------|-------------------|
| **Low Level** | Minimal (batch processing, simple models) | $5K - $20K | **$5K - $20K** |
| **Intermediate** | Moderate (real-time orchestration, multi-model) | $20K - $50K | **$20K - $50K** |
| **High Level** | High (complex reasoning, large language models) | $50K - $150K | **$50K - $150K** |
| **Executive** | Very High (enterprise-grade models, scenario modeling) | $150K - $500K | **$150K - $500K** |

**ROI Comparison:**
- **Low-Level Agent** ($10K/year) replaces 50% of **Low-Level Human** ($70K/year) → **$25K savings** (250% ROI)
- **Intermediate Agent** ($35K/year) replaces 30% of **Intermediate Human** ($120K/year) → **$1K savings** (3% ROI, but 24/7 availability, instant response)
- **High-Level Agent** ($100K/year) augments **High-Level Human** ($200K/year) → Enables human to be 2x more productive → **$200K value creation** (200% ROI)
- **Executive Agent** ($300K/year) advises **CEO** (priceless) → Improves strategic decision quality by 20% → **Millions in value** (immeasurable ROI)

---

## Implementation Guidance

### How to Assign Role Levels

#### For Humans:
1. **Assess scope of work:** Single task? Multi-step process? Cross-functional coordination? Strategic vision?
2. **Evaluate decision authority:** What can they decide independently vs. require approval?
3. **Measure impact:** Operational (task execution)? Tactical (team performance)? Strategic (organizational outcomes)?
4. **Consider tenure & expertise:** Years of experience, domain knowledge, leadership capability

#### For AI Agents:
1. **Assess task complexity:** Simple automation? Multi-step reasoning? Cross-domain synthesis?
2. **Evaluate autonomy:** Supervised (human approves every action)? Co-pilot (AI suggests, human decides)? Automated (AI acts, human reviews exceptions)?
3. **Measure reliability:** Error rate? User satisfaction? Business impact?
4. **Plan evolution path:** Can this agent be promoted to higher level? What performance triggers promotion?

---

### Example: Sales Function Role Hierarchy

| Role Level | Human Role | AI Agent Role |
|------------|------------|---------------|
| **Low** | **Sales Development Rep (SDR):** Qualify inbound leads, book meetings | **LeadQualifier-Agent:** Score leads, enrich data, route to SDRs |
| **Intermediate** | **Sales Engineer:** Provide technical demos, answer product questions | **DemoPersonalizer-Agent:** Customize demo environment, suggest talking points based on prospect |
| **High** | **Sales Manager:** Lead 8 AEs, coach on deals, forecast revenue | **DealRisk-Agent:** Analyze pipeline, flag at-risk deals, recommend coaching focus |
| **Executive** | **VP Sales:** Set sales strategy, allocate territories, hire sales leaders | **SalesStrategy-Agent:** Model revenue scenarios, recommend quota distribution, forecast hiring needs |

---

### Example: Finance Function Role Hierarchy

| Role Level | Human Role | AI Agent Role |
|------------|------------|---------------|
| **Low** | **Accounts Payable Clerk:** Process invoices, reconcile vendor statements | **InvoiceProcessor-Agent:** Extract invoice data, validate against POs, route for approval |
| **Intermediate** | **Financial Analyst:** Build budget models, variance reports | **BudgetAnalyst-Agent:** Generate variance reports, flag anomalies, suggest corrective actions |
| **High** | **Finance Manager:** Lead accounting team, ensure accurate reporting | **MonthEndClose-Agent:** Orchestrate month-end close workflow, monitor completion, escalate delays |
| **Executive** | **CFO:** Set financial strategy, capital allocation, investor relations | **CapitalAllocation-Agent:** Model investment scenarios, recommend allocation, forecast cash flow |

---

## Cultural Implications

### Mindset Shifts Required

**From:**
- "AI will replace me" (fear, resistance)
- "I need to protect my job by hoarding knowledge"
- "AI is only for repetitive tasks"

**To:**
- "AI is my teammate that handles busywork, so I can focus on high-value work"
- "I get promoted by leveraging AI to multiply my impact"
- "AI can reach Manager/Director level (with human oversight), freeing executives for strategic leadership"

---

### Career Development in AI-Native Organization

**Low-Level Humans:**
- **Without AI:** Stuck in repetitive tasks forever (burnout, turnover)
- **With AI:** AI handles repetitive tasks, humans upskill to Intermediate level (Consultant/Coordinator roles)
- **Result:** Faster career progression, higher job satisfaction

**Intermediate Humans:**
- **Without AI:** Bogged down in coordination, firefighting (meetings, emails, status updates)
- **With AI:** Coordinator-Agents handle workflow orchestration, humans focus on strategic problem-solving
- **Result:** Promotion to High-Level (Specialist/Manager) roles

**High-Level Humans:**
- **Without AI:** Limited by time (can only solve 10 complex problems/year)
- **With AI:** Specialist-Agents pre-analyze problems, surface insights, humans make final calls on 100 problems/year
- **Result:** 10x productivity, outsized impact, Executive promotions

**Executives:**
- **Without AI:** Make strategic decisions based on intuition + quarterly reports (lag time, incomplete data)
- **With AI:** Director-Agents provide real-time scenario modeling, predictive analytics, early warning systems
- **Result:** Better strategic decisions, faster adaptation to market changes, competitive advantage

---

## Success Metrics by Role Level

### Low Level (Assistant/Analyst)

**Human:**
- Task completion rate: 95%+
- Accuracy: 98%+
- Response time: SLA compliance
- Manager satisfaction: 80%+

**AI Agent:**
- Automation rate: 80%+ (of eligible tasks)
- Error rate: <2%
- Processing speed: 10-100x faster than human
- User satisfaction: 80%+

---

### Intermediate Level (Consultant/Coordinator)

**Human:**
- Recommendation adoption rate: 60%+
- Stakeholder satisfaction: NPS >70
- Project on-time delivery: 90%+
- Knowledge transfer effectiveness: 80%+ (stakeholders can self-serve after engagement)

**AI Agent:**
- Recommendation quality: 70%+ acceptance rate
- Workflow completion rate: 90%+ (within SLA)
- Coordination overhead reduction: 50%+ (fewer human handoffs, meetings)
- User satisfaction: 75%+

---

### High Level (Specialist/Manager)

**Human:**
- Strategic goal attainment: 85%+ (OKRs, KPIs)
- Team performance: Top quartile (vs. peers)
- Employee engagement: 80%+ (team retention, satisfaction)
- Thought leadership: Published insights, speaking engagements, mentorship

**AI Agent:**
- Complex problem resolution: 80%+ success rate
- Agent team performance: 90%+ (if managing other agents)
- Business impact: Measurable ROI (cost savings, revenue growth, risk reduction)
- User trust: 85%+ (stakeholders rely on AI recommendations)

---

### Executive Level (Director)

**Human:**
- Strategic goal attainment: 3-5 year OKRs met
- Financial performance: Revenue/profit targets exceeded
- Organizational health: Engagement, retention, diversity benchmarks met
- Market position: Competitive advantage sustained, innovation recognized

**AI Agent:**
- Strategic forecast accuracy: ±15% at 3 years
- Resource allocation ROI: +20% vs. baseline
- Risk mitigation: Early detection of 80%+ of strategic risks
- Executive satisfaction: CEO/Board confidence in AI recommendations

---

## Conclusion: A Unified Framework for Human & AI Progression

**SOLID.AI's 4-Level Role Hierarchy enables:**

1. **Clarity:** Everyone (human and AI) understands their role, scope, authority, and expectations
2. **Career Progression:** Humans see clear path from Assistant → Analyst → Consultant → Specialist → Manager → Director
3. **AI Evolution:** Agents can be "promoted" from Low → Intermediate → High → Executive as capabilities improve
4. **Complementarity:** Humans and AI agents collaborate at each level (AI handles scale, humans handle judgment)
5. **Accountability:** Decision authority clearly defined (who can decide what, who must review/approve)
6. **Economic Transparency:** ROI quantified at each level (cost of human vs. AI, productivity multiplier)

**The AI-Native Organization is one where:**
- **Assistants (human + AI)** automate repetitive tasks with 100% oversight
- **Analysts (human + AI)** surface insights from data, advise decision-makers
- **Consultants (human + AI)** provide expert recommendations, design solutions
- **Coordinators (human + AI)** orchestrate workflows, remove bottlenecks
- **Specialists (human + AI)** solve complex problems, set domain standards
- **Managers (human + AI)** lead teams, allocate resources, drive execution
- **Directors (human + AI)** set strategy, govern the organization, ensure long-term success

**Humans and AI agents are teammates, not competitors. Together, they create an organization that is faster, smarter, more reliable, and more humane than either could achieve alone.**

---

**Next Steps:**
- [Review Sector Playbooks](../PLAYBOOKS/) - See role hierarchies applied to Sales, Finance, HR, Marketing, etc.
- [Explore Adoption Pack](../ADOPTION/) - Ready-to-use agent definitions for each level
- [Read Whole-Organization Transformation](09-whole-organization-transformation.md) - How to implement role hierarchies org-wide

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
