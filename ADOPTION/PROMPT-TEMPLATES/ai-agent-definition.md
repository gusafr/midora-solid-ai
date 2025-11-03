# AI Agent Definition Prompt

**Category:** AI Design | **Framework:** SOLID.AI | **Use Case:** Creating new AI capabilities

---

## When to Use This Prompt

Use this prompt when **introducing any new AI capability** to ensure responsible design with clear boundaries and oversight.

**Ideal for:**
- Defining AI agents or automation
- Scoping AI responsibilities
- Establishing guardrails and ethics
- Planning human-AI collaboration

---

## The Prompt

```
I need to define an AI agent for: [TASK OR CAPABILITY]

Help me create a comprehensive agent definition following SOLID.AI principles:

1. **Agent Identity**
   - Name: [Suggest a meaningful name]
   - Role: [What is this agent's function?]
   - Persona: [How should it behave/communicate?]

2. **Purpose Statement**
   - Why does this agent exist?
   - What human need or organizational goal does it serve?
   - How does it align with our mission and values?

3. **Capabilities (What it CAN do)**
   - List specific tasks or decisions the agent handles
   - Define inputs, outputs, and data sources
   - Specify performance targets (latency, accuracy, etc.)

4. **Guardrails (What it CANNOT or MUST NOT do)**
   - Prohibited actions (ethical, legal, safety)
   - Boundaries (scope limits, escalation triggers)
   - Failure modes and safe defaults

5. **Human Oversight**
   - When does the agent defer to humans?
   - Who monitors its actions and how often?
   - What level of autonomy: co-pilot, supervised, autonomous?
   - Escalation paths for edge cases or errors

6. **Success Metrics**
   - How do we measure if this agent creates value?
   - What signals indicate degradation or failure?
   - How do we track ethical compliance (bias, fairness, etc.)?

7. **Observability Requirements**
   - What telemetry is logged (decisions, confidence, errors)?
   - What dashboards or alerts are needed?
   - How do we audit this agent's behavior?

8. **Learning & Iteration**
   - How does the agent improve over time?
   - What feedback loops capture performance and issues?
   - When do we review and update the agent definition?

9. **Data & Privacy**
   - What data does the agent access?
   - How is privacy protected?
   - What are retention and security requirements?

10. **Failure & Rollback Plan**
    - What happens if the agent fails or behaves unexpectedly?
    - How do we safely disable or rollback the agent?
    - What manual processes serve as backup?

Generate the definition in YAML format compatible with an agent registry.
```

---

## Example Usage

### Input

```
I need to define an AI agent for: Automatically triaging customer support tickets and suggesting responses

Help me create a comprehensive agent definition following SOLID.AI principles:
[... paste full prompt above ...]
```

### Expected Output (YAML format)

```yaml
agent:
  identity:
    name: "SupportTriage-Agent"
    role: "Customer Support Ticket Triage and Response Suggestion"
    persona: "Helpful, empathetic, and transparent assistant to support team"
  
  purpose:
    statement: "Reduce response time for customers while ensuring high-quality, empathetic support by triaging tickets and suggesting initial responses for human review."
    alignment: "Aligns with our mission to provide accessible, human-centered customer care at scale."
  
  capabilities:
    - task: "Classify ticket urgency (low, medium, high, critical)"
      input: "Ticket text, customer history, product context"
      output: "Urgency level + confidence score"
      performance: "95% accuracy, <2s latency"
    
    - task: "Suggest response draft"
      input: "Ticket content, knowledge base, past resolutions"
      output: "Response text + sources + confidence"
      performance: "80% human approval rate"
  
  guardrails:
    prohibited:
      - "Never send responses directly to customers without human review"
      - "Cannot access payment information or credentials"
      - "Must not make promises about refunds, timelines, or features"
    
    boundaries:
      - "Escalate immediately if: legal threat, safety concern, VIP customer, sentiment < -0.7"
      - "Maximum autonomy: Suggest only, never execute"
    
    safe_defaults:
      - "When uncertain (confidence < 0.7), flag for full human review"
      - "On error, route to general support queue"
  
  human_oversight:
    autonomy_level: "supervised" # co-pilot | supervised | autonomous
    review_frequency: "Every response reviewed before sending"
    reviewers: "Customer Support Specialists"
    escalation: "Low confidence or guardrail violations → Team Lead"
  
  success_metrics:
    value:
      - "Average response time reduced by >30%"
      - "Customer satisfaction maintained or improved (CSAT >= 4.5/5)"
      - "Support team reports reduced cognitive load"
    
    performance:
      - "Classification accuracy >= 95%"
      - "Suggestion acceptance rate >= 80%"
    
    ethical:
      - "No demographic bias in urgency classification (monthly audit)"
      - "Privacy violations: 0 tolerance"
  
  observability:
    logging:
      - "Every classification decision with confidence score"
      - "All suggested responses (pre-edit and post-edit)"
      - "Human override/edit patterns"
      - "Escalation reasons"
    
    dashboards:
      - "Real-time accuracy and latency"
      - "Confidence score distribution"
      - "Escalation rate trends"
      - "Human edit patterns (what gets changed)"
    
    alerts:
      - "Accuracy drops below 90% for 1 hour"
      - "Escalation rate spike (>20% increase)"
      - "Guardrail violation detected"
  
  learning:
    improvement_loop: "Weekly review of misclassifications and low-confidence cases"
    feedback: "Human edits used to fine-tune suggestions"
    review_cadence: "Monthly agent definition review with support team"
  
  data_privacy:
    access: "Ticket text, customer metadata (no PII beyond name/email), past interactions"
    protection: "All data encrypted at rest and in transit; GDPR compliant"
    retention: "Logs retained 90 days, anonymized after"
  
  failure_plan:
    failure_modes:
      - "Model unavailable → Route all tickets to human queue"
      - "High error rate → Disable suggestions, triage only"
      - "Guardrail violation → Immediate escalation + incident review"
    
    rollback: "Kill switch disables agent; manual triage resumes immediately"
    backup: "Support team trained to handle full manual load"
```

---

## Customization Tips

**For high-risk domains (healthcare, finance, legal):**
Add: "What regulatory compliance requirements apply?"

**For customer-facing agents:**
Add: "How does the agent handle frustrated or vulnerable users?"

**For decision-making agents:**
Add: "What explainability do we provide for agent decisions?"

**For autonomous agents:**
Add: "What pre-deployment testing and validation is required?"

---

## Follow-Up Prompts

After generating the definition:

```
Review this agent definition for potential ethical risks or gaps in oversight.
```

```
Create a testing plan to validate this agent's behavior before production.
```

```
Generate a runbook for operating and monitoring this agent.
```

```
Design a dashboard to visualize this agent's performance and health.
```

---

## SOLID.AI Principles Applied

- ✅ **Purpose-Led Decisions** - Anchors agent in clear purpose
- ✅ **Cognitive Workforce** - Defines explicit roles and responsibilities
- ✅ **Ethical Automation** - Bakes in guardrails and transparency
- ✅ **Human-Machine Symbiosis** - Specifies collaboration model
- ✅ **Continuous Learning** - Includes feedback and improvement loops

---

## Related Resources

- **AI Agents Documentation:** [DOCS/05-ai-agents.md](../../DOCS/05-ai-agents.md)
- **AI Integration Playbook:** [PLAYBOOKS/playbook-ai-integration.md](../../PLAYBOOKS/playbook-ai-integration.md)
- **Governance & Ethics:** [DOCS/06-governance-ethics.md](../../DOCS/06-governance-ethics.md)
- **Template:** [TEMPLATES/agent-definition-template.yaml](../TEMPLATES/agent-definition-template.yaml)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Share Your Results:** [GitHub Discussions](https://github.com/gusafr/midora-solid-ai/discussions)
