# Operations Quick Reference Card

**Role:** Operations / SRE / DevOps | **Framework:** SOLID.AI | **Version:** 1.0

---

## Core AI Prompting Patterns for Operations

### 1. Incident Response with AI Context

```
We have an incident: [DESCRIPTION].

Current status:
- Symptoms: [WHAT'S HAPPENING]
- Affected systems: [COMPONENTS]
- AI agents involved: [IF ANY]
- User impact: [SEVERITY]

Help me:
1. Triage severity and establish incident command
2. Identify likely root causes (code, data, AI, infrastructure)
3. Determine safe rollback or mitigation steps
4. Plan communication to stakeholders
5. Set up post-incident review structure

What's the first action I should take?
```

**Use when:** Responding to production incidents

---

### 2. Observability Design

```
Design observability for [SYSTEM/FEATURE]:

Include:
1. **Metrics:** What KPIs and health signals to track
2. **Logs:** What events to capture and retention policies
3. **Traces:** End-to-end request flows, especially human-AI handoffs
4. **Dashboards:** What views operators need
5. **Alerts:** Conditions, thresholds, and escalation paths
6. **AI Behavior:** How to monitor agent decisions and performance
7. **Ethical Signals:** Bias, fairness, consent violations

Generate an observability plan.
```

**Use when:** Instrumenting new systems or improving existing ones

---

### 3. Capacity Planning with AI Workloads

```
Plan capacity for [SERVICE] considering AI workloads:

Current state:
- Traffic patterns: [DATA]
- AI inference load: [MODELS, REQUESTS]
- Data processing: [VOLUMES]
- Growth projections: [ESTIMATES]

Analyze:
1. Compute requirements (CPU, GPU, memory)
2. Storage and data pipeline capacity
3. Network bandwidth and latency
4. AI model serving costs
5. Scaling triggers and thresholds
6. Cost optimization opportunities

Provide a capacity plan with 6-month outlook.
```

**Use when:** Planning infrastructure and costs

---

### 4. Runbook Creation

```
Create a runbook for [SCENARIO/SYSTEM]:

Include:
- **Purpose:** What this runbook handles
- **Detection:** How we know this is happening
- **Triage:** Initial assessment steps
- **Response:** Step-by-step mitigation
- **AI Agent Actions:** What automation can/should do
- **Human Decisions:** When human judgment is required
- **Rollback:** How to safely undo changes
- **Communication:** Who to notify and when
- **Post-Action:** Follow-up and learning capture

Format in Markdown with clear sections.
```

**Use when:** Documenting operational procedures

---

### 5. Performance Optimization

```
Optimize performance for [SYSTEM]:

Current metrics:
- Latency: [P50, P95, P99]
- Throughput: [REQUESTS/SEC]
- Error rate: [PERCENTAGE]
- Resource utilization: [CPU, MEMORY, etc.]
- AI inference time: [IF APPLICABLE]

Identify:
1. Bottlenecks in the critical path
2. Optimization opportunities (caching, batching, etc.)
3. Infrastructure tuning options
4. AI model optimization (quantization, batching)
5. Cost-performance tradeoffs
6. Monitoring to validate improvements

Prioritize by impact/effort.
```

**Use when:** Improving system performance

---

### 6. Deployment Strategy

```
Design a deployment strategy for [CHANGE]:

Consider:
- **Risk Level:** [LOW/MEDIUM/HIGH]
- **AI Components:** [YES/NO - which ones]
- **Data Migrations:** [YES/NO - describe]
- **Traffic Patterns:** [EXPECTED LOAD]

Recommend:
1. Deployment method (blue/green, canary, rolling, etc.)
2. Rollout phases and gates
3. Health checks and success criteria
4. Rollback triggers and procedures
5. Observability during deployment
6. Communication and coordination plan

Include a deployment checklist.
```

**Use when:** Planning releases and changes

---

### 7. Cost Analysis and Optimization

```
Analyze costs for [SERVICE/SYSTEM]:

Current spend breakdown:
- Compute: [AMOUNT]
- Storage: [AMOUNT]
- AI/ML inference: [AMOUNT]
- Data transfer: [AMOUNT]
- Third-party services: [AMOUNT]

Identify:
1. Cost drivers and trends
2. Waste and inefficiency
3. Right-sizing opportunities
4. Reserved vs. on-demand tradeoffs
5. AI model cost optimization (smaller models, caching, etc.)
6. Business value vs. cost ratio

Provide optimization recommendations.
```

**Use when:** Managing infrastructure costs

---

### 8. Security and Compliance Check

```
Review [SYSTEM/CHANGE] for security and compliance:

Check:
1. **Authentication & Authorization:** Who can access what
2. **Data Privacy:** PII handling, encryption, retention
3. **AI Ethics:** Bias monitoring, transparency, consent
4. **Audit Logging:** What's tracked for compliance
5. **Secrets Management:** Credentials, keys, certificates
6. **Network Security:** Firewalls, segmentation, TLS
7. **Compliance Requirements:** GDPR, SOC2, etc.

Generate a security checklist and risk assessment.
```

**Use when:** Security reviews and compliance audits

---

### 9. Chaos Engineering with AI

```
Design a chaos experiment for [SYSTEM]:

Test resilience when:
- [FAILURE SCENARIO: e.g., AI service degraded, data pipeline delayed]

Experiment design:
1. **Hypothesis:** What we expect to happen
2. **Blast Radius:** Scope and limits of experiment
3. **Injection Method:** How we introduce failure
4. **Observability:** What we monitor during experiment
5. **Success Criteria:** What "graceful degradation" looks like
6. **Abort Conditions:** When to stop the experiment
7. **AI Behavior:** How agents should respond to failure
8. **Learning Capture:** What we document afterward

Generate an experiment plan.
```

**Use when:** Testing system resilience

---

### 10. Post-Incident Review (Blameless)

```
Facilitate a post-incident review for [INCIDENT]:

Timeline: [WHEN IT HAPPENED]
Duration: [HOW LONG]
Impact: [USER/BUSINESS IMPACT]

Guide discussion on:
1. **What Happened:** Objective timeline of events
2. **Why It Happened:** Root causes (technical, process, human)
3. **What Went Well:** Effective responses and mitigations
4. **What We Learned:** Insights about system, AI, or organization
5. **Action Items:** Concrete improvements (not blame)
6. **AI Agent Behavior:** How automation helped or hindered
7. **Knowledge Sharing:** How we disseminate learnings

Generate a PIR document template.
```

**Use when:** Learning from incidents

---

## SOLID.AI Operations Mindset

✅ **Do:**
- Design for observability from day one
- Treat AI agents as teammates with specific roles
- Build automated responses with human oversight hooks
- Create blameless learning cultures
- Monitor ethical signals alongside technical metrics
- Optimize for resilience, not just efficiency
- Document runbooks and share knowledge

❌ **Avoid:**
- Black-box AI without visibility into decisions
- Alert fatigue from noisy, unactionable signals
- Heroic firefighting instead of systematic improvement
- Optimizing costs at the expense of reliability
- Deploying without rollback plans
- Skipping post-incident learning

---

## AI-Specific Operations Considerations

### Monitoring AI Agents
- **Decision Logging:** Track all autonomous actions
- **Confidence Scores:** Monitor when AI is uncertain
- **Fallback Triggers:** Detect when agents defer to humans
- **Drift Detection:** Watch for model performance degradation
- **Ethical Violations:** Alert on bias, privacy, or safety issues

### Data Pipeline Health
- **Freshness:** Is data arriving on time?
- **Quality:** Are contracts being met?
- **Lineage:** Can we trace data flow?
- **Volume Anomalies:** Unexpected spikes or drops?

### Human-AI Handoffs
- **Latency:** How long until human sees escalation?
- **Context Preservation:** Does human get full picture?
- **Override Tracking:** When do humans correct AI?

---

## Key Resources

- **Observability:** [DOCS/07-observability.md](../../DOCS/07-observability.md)
- **Operations Playbook:** [PLAYBOOKS/playbook-operations.md](../../PLAYBOOKS/playbook-operations.md)
- **Automation SIPOC:** [DOCS/04-automation-sipoc.md](../../DOCS/04-automation-sipoc.md)
- **Architecture:** [DOCS/02-architecture.md](../../DOCS/02-architecture.md)
- **Glossary:** [DOCS/glossary.md](../../DOCS/glossary.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Feedback:** [GitHub Issues](https://github.com/gusafr/midora-solid-ai/issues)
