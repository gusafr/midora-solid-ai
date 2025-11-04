# Sales Playbook

**Applying SOLID.AI principles to sales operations, customer engagement, and revenue growth**

---

## Overview

This playbook shows how sales teams can use SOLID.AI to build intelligent, ethical, and adaptive sales operations. Whether you're in B2B, B2C, enterprise, or SMB sales, SOLID.AI principles help you leverage AI while maintaining human relationships and ethical practices.

> **🤝 The Human Touch in Sales**  
> Sales is fundamentally a **relationship business**. While AI can automate lead scoring, email drafts, and data analysis, the **trust required to close complex deals is built human-to-human**. Enterprise sales, strategic partnerships, and high-value negotiations require in-person meetings, active listening, empathy, and creative problem-solving—capabilities AI cannot replicate.  
>   
> **SOLID.AI Principle**: AI finds opportunities and handles routine tasks; humans build trust and win relationships.  
>   
> See [**Human-AI Collaboration Guide**](../DOCS/08-human-ai-collaboration.md) for where to preserve the irreplaceable human element.

---

## Sales Through the SOLID.AI Lens

### Purpose Layer: Revenue with Values
- **Mission Alignment**: Sales goals serve customer success, not just quotas
- **Value Creation**: Focus on solving customer problems, not just closing deals
- **Ethical Selling**: Transparent pricing, honest claims, respectful persistence

### Data Spine: Customer Intelligence
- **CRM as Single Source of Truth**: Unified customer data across touchpoints
- **Lead Scoring Transparency**: Clear criteria for qualification
- **Activity Tracking**: Observable pipeline health and rep performance

### Cognitive Layer: AI Sales Assistants
- **Lead Scoring Agents**: Prioritize high-potential prospects
- **Outreach Automation**: Personalized at scale with human oversight
- **Forecasting Models**: Predict pipeline with confidence intervals
- **Conversation Intelligence**: Extract insights from calls/emails

### Automation Mesh: Sales Workflows
- **Lead Routing**: Automatic assignment based on territory, skill, capacity
- **Follow-up Sequences**: Trigger nurture campaigns at right moments
- **Deal Alerts**: Notify reps of high-value activities or risks
- **Quote Generation**: Accelerate proposal creation

### Organizational Layer: Sales Squads & Pools
- **Territory Squads**: Autonomous teams owning regions or segments
- **Solution Engineers Pool**: Shared technical pre-sales support
- **Sales Ops Pool**: Centralized enablement, analytics, tools
- **Customer Success Handoff**: Smooth transition post-sale

### Governance & Ethics: Trust-Based Selling
- **Privacy Compliance**: GDPR, CCPA in prospecting and outreach
- **Anti-Spam Practices**: Respectful, consent-based communication
- **Pricing Integrity**: No hidden fees or bait-and-switch
- **Diversity in Pipeline**: Avoid bias in targeting or scoring

---

## AI Use Cases for Sales Teams

### 1. Intelligent Lead Scoring

**Purpose**: Help reps focus on highest-potential opportunities

**Agent Definition**:
```yaml
agent:
  identity:
    name: "LeadScore-Agent"
    role: "Prioritize leads by conversion probability"
    persona: "Data-driven advisor, transparent about criteria"
  
  capabilities:
    - task: "Score inbound leads 0-100 based on fit and intent"
      input: "Company data, website behavior, form responses"
      output: "Score + reasoning (e.g., 'High score: 500+ employees, visited pricing 3x')"
      performance: "85% accuracy predicting closed-won within 90 days"
  
  guardrails:
    prohibited:
      - "Do not score based on protected characteristics (race, gender, etc.)"
      - "Do not auto-disqualify without human review of high-intent signals"
    boundaries:
      - "Escalate to rep if score conflicts with qualitative signals (e.g., warm intro)"
  
  human_oversight:
    autonomy_level: "co-pilot"
    review: "Reps can override scores with justification"
    escalation: "Sales ops reviews scoring model monthly for bias and accuracy"
  
  success_metrics:
    value:
      - "Reps spend 70% of time on high-score leads (up from 50%)"
      - "Conversion rate increases 20% due to better prioritization"
    ethical:
      - "No demographic bias in scoring (quarterly audit)"
      - "Transparent scoring criteria visible to reps"
```

**Implementation Checklist**:
- [ ] Define scoring criteria collaboratively with sales team
- [ ] Audit training data for historical bias (e.g., did we ignore valid leads from certain industries?)
- [ ] Make scoring transparent: reps see WHY a lead scored high/low
- [ ] Track override patterns: if reps consistently override, model needs tuning
- [ ] Review closed-lost deals: did we mis-score and lose winnable opportunities?

---

### 2. AI-Powered Outreach Sequences

**Purpose**: Personalize communication at scale while staying human

**Agent Definition**:
```yaml
agent:
  identity:
    name: "OutreachPersonalizer-Agent"
    role: "Generate personalized email/message drafts"
    persona: "Helpful ghostwriter, never spammy"
  
  capabilities:
    - task: "Draft personalized outreach emails"
      input: "Prospect info, previous interactions, value prop"
      output: "Email draft referencing prospect's industry, pain points, recent news"
      performance: "60% open rate, 15% reply rate (vs. 30%/5% for generic)"
  
  guardrails:
    prohibited:
      - "Never send emails directly; always require rep approval"
      - "No deceptive subject lines (e.g., 'Re:' when no prior thread)"
      - "No high-pressure or manipulative language"
    boundaries:
      - "Respect unsubscribe and do-not-contact lists immediately"
      - "Limit outreach frequency: max 1 email/week per prospect"
  
  human_oversight:
    autonomy_level: "supervised"
    review: "Rep reviews and edits every draft before sending"
    escalation: "If prospect replies negatively, pause sequence and alert rep"
  
  success_metrics:
    value:
      - "Reps save 10 hours/week on email composition"
      - "Reply rates improve 2-3x vs. generic templates"
    ethical:
      - "Unsubscribe rate < 2% (indicates respectful messaging)"
      - "Zero spam complaints"
```

**Best Practices**:
- **Personalization Depth**: Reference specific company news, not just mail-merge
- **Transparency**: If AI-generated, consider disclosing (builds trust in some contexts)
- **Human Touch**: Always add a personal line or custom P.S.
- **Consent First**: Use opt-in lists, respect preferences
- **Learn from Replies**: Feed positive/negative responses back to improve agent

---

### 3. Deal Risk & Forecasting

**Purpose**: Predict pipeline health and intervene on at-risk deals

**Agent Definition**:
```yaml
agent:
  identity:
    name: "DealHealthMonitor-Agent"
    role: "Flag at-risk deals and forecast accuracy"
    persona: "Early warning system, not a critic"
  
  capabilities:
    - task: "Assess deal risk based on activity, stakeholder engagement, timeline"
      input: "CRM activity, email/call patterns, deal age, competitive intel"
      output: "Risk level (low/medium/high) + recommended actions"
      performance: "Identifies 80% of deals that will slip or close-lost 30 days early"
  
  guardrails:
    prohibited:
      - "Do not penalize reps for flagged deals (this is a coaching tool, not punishment)"
      - "Do not auto-adjust forecasts without rep input"
    boundaries:
      - "Escalate high-value at-risk deals (>$100K) to manager immediately"
  
  human_oversight:
    autonomy_level: "co-pilot"
    review: "Reps and managers review risk flags in weekly pipeline reviews"
    escalation: "Sales ops validates model accuracy monthly"
  
  success_metrics:
    value:
      - "Forecast accuracy improves from 60% to 85%"
      - "Win rate increases 10% due to proactive intervention on at-risk deals"
    ethical:
      - "Risk scoring does not create unhealthy pressure or gaming"
```

**Intervention Playbook** (when deal flagged as high-risk):
1. **Rep reviews**: Is the risk real or model noise?
2. **Manager 1:1**: Strategize on how to de-risk (e.g., engage executive sponsor)
3. **Update CRM**: Log intervention and outcome
4. **Feedback loop**: Did intervention work? Feed back to model

---

### 4. Conversation Intelligence

**Purpose**: Extract insights from sales calls and emails to coach reps and improve messaging

**Use Cases**:
- **Objection Patterns**: What objections come up most? How do top reps handle them?
- **Talk Time Ratio**: Are reps listening enough (ideal: 60% prospect, 40% rep)?
- **Competitor Mentions**: Track competitive threats and winning responses
- **Next Steps**: Did the call end with clear next steps?

**Ethical Guardrails**:
- **Consent**: Notify prospects "This call may be recorded for quality purposes"
- **Privacy**: Transcripts stored securely, deleted after retention period
- **No Surveillance**: Use for coaching, not punitive tracking
- **Rep Access**: Reps see their own insights, not ranked against peers publicly

---

## Sales Squad Model

### Territory-Based Squads

**Squad Charter Example**:

**Squad Name**: Northeast Enterprise Sales  
**Mission**: Drive $5M ARR in Northeast region by solving customers' [specific problem]  
**Scope**: Companies >500 employees in NY, NJ, PA, MA  
**Team**: 4 AEs, 1 SE (from pool), 1 SDR, 1 CSM (post-sale handoff)

**AI Agents Supporting Squad**:
- LeadScore-Agent (prioritize inbound from region)
- OutreachPersonalizer-Agent (draft prospecting emails)
- DealHealthMonitor-Agent (flag at-risk deals)

**Success Metrics**:
- Revenue: $5M ARR (outcome)
- Pipeline: 3x coverage (leading indicator)
- Win Rate: >30% (efficiency)
- Customer Satisfaction: NPS >50 (quality)

**Rituals**:
- Daily: 15-min stand-up on hot deals
- Weekly: Pipeline review with manager
- Monthly: Squad retro (what's working, what's not)
- Quarterly: Territory planning and goal reset

---

## Data Contracts for Sales

### Example: Opportunity Created Event

```yaml
contract:
  identity:
    name: "opportunity-created-event"
    version: "1.0.0"
    type: "event"
  
  schema:
    fields:
      - name: "opportunity_id"
        type: "string (UUID)"
        required: true
      - name: "account_name"
        type: "string"
        required: true
      - name: "estimated_value"
        type: "number"
        required: true
      - name: "close_date"
        type: "date"
        required: true
      - name: "stage"
        type: "enum"
        values: ["Discovery", "Demo", "Proposal", "Negotiation", "Closed-Won", "Closed-Lost"]
        required: true
      - name: "lead_source"
        type: "string"
        required: false
      - name: "assigned_rep"
        type: "string"
        required: true
  
  consumers:
    - name: "Forecasting Model"
      use_case: "Predict quarterly revenue"
    - name: "Sales Ops Dashboard"
      use_case: "Track pipeline health"
    - name: "Marketing Attribution"
      use_case: "Measure campaign ROI"
  
  quality_expectations:
    completeness: "All required fields present within 24h of deal creation"
    accuracy: "Estimated value within 20% of final contract (validated at close)"
    freshness: "Stage updates within same business day"
```

---

## Ethical Sales with AI

### Privacy & Consent
- **GDPR/CCPA Compliance**: Track consent for marketing communications
- **Data Minimization**: Collect only what's needed for sales process
- **Right to Delete**: Honor requests to remove prospect/customer data

### Fairness & Bias
- **Lead Scoring Audits**: Ensure no demographic bias (e.g., ignoring certain geographies or company sizes unfairly)
- **Territory Assignment**: Equitable distribution of opportunities
- **Commission Transparency**: Clear, fair compensation tied to value created

### Honest Communication
- **No Bait-and-Switch**: Pricing and features match what's promised
- **Competitor Comparisons**: Honest, not defamatory
- **Pressure Tactics**: Avoid manipulative urgency ("Deal expires tonight!" when it doesn't)

### Sustainability
- **Long-Term Relationships**: Optimize for customer success, not one-time sale
- **Churn Prevention**: Post-sale handoff to customer success ensures value delivery
- **Referrals**: Happy customers are best source of new business

---

## Metrics for AI-Augmented Sales

### Sales Performance Metrics
| Metric | Target | AI Impact |
|--------|--------|-----------|
| **Pipeline Coverage** | 3-5x quota | AI lead scoring focuses effort on high-potential |
| **Win Rate** | 25-35% | AI deal risk flags enable proactive coaching |
| **Sales Cycle Length** | 60-90 days | AI automates admin, reps spend more time selling |
| **Average Deal Size** | Trend up | AI identifies upsell/cross-sell opportunities |

### AI Agent Metrics
| Metric | Target | Why It Matters |
|--------|--------|----------------|
| **Lead Score Accuracy** | >80% | Poor scoring wastes rep time |
| **Outreach Reply Rate** | 2-3x baseline | Measures personalization quality |
| **Forecast Accuracy** | >85% | Inaccurate forecasts hurt planning |
| **Agent Override Rate** | <20% | High overrides = model needs tuning |

### Ethical Metrics
| Metric | Target | Why It Matters |
|--------|--------|----------------|
| **Spam Complaint Rate** | <0.1% | Indicates respectful outreach |
| **Unsubscribe Rate** | <2% | Measures message relevance |
| **Bias in Scoring** | Zero demographic disparity | Ensures fairness |
| **Customer Satisfaction (NPS)** | >50 | Did we sell what we promised? |

---

## Common Pitfalls & Solutions

| Pitfall | Solution |
|---------|----------|
| **AI spams prospects** | Require human approval for all outreach; monitor reply/unsubscribe rates |
| **Reps don't trust lead scores** | Make scoring transparent; train reps on criteria; allow overrides with feedback |
| **Gaming the forecast** | Use AI to detect sandbagging; focus on pipeline health, not just forecast number |
| **Data quality degrades** | Enforce data contracts; automate CRM hygiene (e.g., deduplication) |
| **AI replaces human relationships** | Use AI for admin/research; reps own relationships and strategy |
| **Pressure to hit quotas overrides ethics** | Leadership models ethical selling; celebrate customer success, not just revenue |

---

## Getting Started: Sales AI Roadmap

### Month 1: Foundation
- [ ] Define sales data contracts (leads, opportunities, activities)
- [ ] Audit CRM data quality
- [ ] Identify one high-impact AI use case (e.g., lead scoring)
- [ ] Form sales ops + AI cross-functional squad

### Month 2-3: Pilot
- [ ] Build or buy lead scoring model
- [ ] Train sales team on AI tool usage
- [ ] Pilot with 2-3 reps or one territory
- [ ] Gather feedback, iterate

### Month 4-6: Scale
- [ ] Roll out to full sales team
- [ ] Add second AI use case (e.g., outreach personalization)
- [ ] Establish ongoing governance (bias audits, accuracy reviews)
- [ ] Capture learnings, update playbook

### Month 7-12: Optimize
- [ ] Expand to deal risk monitoring, forecasting
- [ ] Integrate AI across full sales workflow
- [ ] Share best practices across squads
- [ ] Contribute learnings back to SOLID.AI community

---

## Real-World Example: B2B SaaS Sales Squad

**Context**: Mid-market B2B SaaS company selling to HR teams

**Before SOLID.AI**:
- Reps waste 60% of time on unqualified leads
- Generic email templates get 5% reply rate
- Forecast accuracy 60% (causes planning chaos)
- Sales and marketing blame each other for bad leads

**After SOLID.AI Implementation**:

1. **Lead Scoring Agent** prioritizes inbound based on company size, budget signals, tech stack
2. **Outreach Agent** drafts personalized emails referencing prospect's HR challenges
3. **Deal Risk Agent** flags stalled deals 30 days before quarter end
4. **Data Contracts** ensure marketing and sales agree on "qualified lead" definition

**Results** (after 6 months):
- Reps spend 75% of time on high-score leads
- Reply rate improves to 15%
- Forecast accuracy reaches 88%
- Win rate increases from 22% to 31%
- Sales-marketing alignment improves (shared data spine)

**Key Success Factors**:
- Sales leadership championed ethical AI use
- Reps involved in defining scoring criteria (not black box)
- Weekly retrospectives to tune AI and process
- Celebrated human relationship-building, not just AI efficiency

---

## Conclusion

Sales is fundamentally about **human relationships and trust**. AI should amplify your ability to:

- **Understand customers** (through better data and insights)
- **Personalize at scale** (without losing authenticity)
- **Focus on high-value activities** (by automating admin)
- **Coach and improve** (with conversation intelligence)

But AI should never replace:

- **Empathy** in understanding customer pain
- **Judgment** in navigating complex deals
- **Integrity** in making honest recommendations
- **Creativity** in crafting solutions

Use SOLID.AI to build sales operations that are **intelligent, ethical, and human-centered**.

---

**Next Steps**:
- Review [AI Integration Playbook](../../../organizational/ai-integration.md) for technical implementation
- Use [Sales Reference Card](../ADOPTION/REFERENCE-CARDS/sales-reference.md) for daily AI prompts (coming soon)
- Adapt [Squad Charter Template](../ADOPTION/TEMPLATES/squad-charter-template.md) for your sales teams

**Questions or feedback?** [Open an issue](https://github.com/gusafr/midora-solid-ai/issues) or contribute your sales AI learnings!

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
