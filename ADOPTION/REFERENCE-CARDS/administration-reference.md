# Administration & Finance AI Reference Card

**Quick AI prompting patterns for HR, finance, procurement, and operations professionals**

---

## 🎯 Purpose

This reference card provides ready-to-use AI prompts to help administration and finance teams leverage AI assistants (ChatGPT, Claude, Copilot, etc.) for process automation, compliance, reporting, and operational efficiency.

---

## 🚀 10 Essential AI Prompts for Administration & Finance

### 1. **Invoice Data Extraction & Validation**

**Use when:** Processing invoices manually is slow and error-prone

**Prompt:**
```
I have an invoice from [Vendor Name] for [description of goods/services].

Invoice details:
- Amount: $[amount]
- Date: [date]
- Line items: [list if available]
- PO number: [if referenced]

Tasks:
1. Extract structured data: Vendor, invoice number, date, amount, line items, tax
2. Validate against our PO [PO-####] (expected amount: $X, items: Y)
3. Flag discrepancies: price mismatches >5%, missing PO, duplicate invoice
4. Recommend action: Auto-approve, escalate to manager, or reject with reason

If data is incomplete, list what's missing.
```

**Why it works:** Structured extraction reduces manual data entry; validation catches errors before payment.

---

### 2. **Expense Policy Compliance Check**

**Use when:** Reviewing employee expense reports for policy violations

**Prompt:**
```
Employee submitted expense report:
- Total: $[amount]
- Expenses:
  - [Category 1]: $X (e.g., "Dinner with client: $150")
  - [Category 2]: $Y (e.g., "Uber to airport: $45")
  - [Category 3]: $Z (e.g., "Software subscription: $99")

Our expense policy:
- Meals: Max $75/person, requires business purpose and attendees
- Travel: Economy class only, ride-share allowed
- Software: Requires manager pre-approval

For each expense:
1. Check policy compliance (✅ compliant | ⚠️ needs clarification | ❌ violation)
2. Explain issue if non-compliant
3. Suggest corrective action (e.g., "Request attendee names", "Reduce to policy limit")

Be helpful, not punitive. If borderline, give benefit of the doubt but ask for clarification.
```

**Why it works:** Catches policy violations early; educates employees in real-time.

---

### 3. **HR Onboarding Checklist Generator**

**Use when:** Ensuring new hire has seamless first-day experience

**Prompt:**
```
New hire details:
- Name: [Full Name]
- Start date: [Date]
- Role: [Job Title]
- Department: [e.g., Engineering, Sales, Marketing]
- Manager: [Name]
- Location: [Office/Remote]

Generate a comprehensive onboarding checklist with:
1. **Pre-Day 1** (7 days before): Offer letter, background check, IT equipment order, desk/badge request
2. **Day 1**: Welcome email, system access (email, Slack, HRIS, tools), team intro, manager 1:1
3. **Week 1**: Benefits enrollment, training modules, project assignments, team lunch
4. **Week 4**: 30-day check-in, performance goal setting, feedback survey

For each task:
- Owner (HR, IT, Manager, Facilities)
- Due date
- Status tracking (Not Started/In Progress/Complete)

Make it actionable and specific to [Department].
```

**Why it works:** Nothing falls through cracks; new hires productive from day 1.

---

### 4. **Monthly Financial Close Report**

**Use when:** Summarizing monthly financials for leadership

**Prompt:**
```
Month: [Month, Year]

Financial data:
- Revenue: $[amount] (vs. budget: $[amount], last month: $[amount])
- Expenses: $[amount] (breakdown by category)
- Net income: $[amount]
- Cash balance: $[amount]
- AR/AP aging: [summary]

Generate an executive summary (max 300 words) covering:
1. **Highlights**: Key wins (e.g., "Revenue up 15% MoM")
2. **Concerns**: Variances or risks (e.g., "Expenses 10% over budget due to...")
3. **Trends**: 3-month trend analysis (improving/stable/declining)
4. **Actions**: Recommendations (e.g., "Accelerate collections", "Review vendor contracts")

Tone: Clear, concise, focused on insights not just data.
```

**Why it works:** Transforms raw numbers into actionable narrative; saves CFO hours of report writing.

---

### 5. **Compliance Risk Assessment**

**Use when:** Proactively identifying regulatory or policy risks

**Prompt:**
```
We're a [industry] company with [# employees] in [locations].

Regulatory landscape:
- [Regulation 1, e.g., "SOX (financial controls)"]
- [Regulation 2, e.g., "GDPR (data privacy)"]
- [Regulation 3, e.g., "Labor law (overtime, classification)"]

Recent audit findings or known gaps:
- [e.g., "Weak segregation of duties in AP", "Missing consent for marketing emails"]

Generate a compliance risk assessment:
1. **High-priority risks**: What could result in fines, legal action, or material audit findings?
2. **Medium-priority risks**: What could cause operational disruption or reputational damage?
3. **Mitigation actions**: Specific steps to close gaps (e.g., "Implement dual approval for journal entries >$10K")
4. **Owner and timeline**: Who fixes it, by when

Prioritize by impact and likelihood.
```

**Why it works:** Proactive risk management prevents surprises; builds culture of compliance.

---

### 6. **Vendor Contract Review**

**Use when:** Evaluating or renewing vendor contracts

**Prompt:**
```
Vendor: [Name]
Service: [e.g., "Cloud hosting", "Payroll processing"]
Contract value: $[annual spend]
Term: [length, e.g., "3 years"]

Key terms:
- Pricing: [e.g., "$X/month + $Y per user"]
- SLA: [e.g., "99.9% uptime"]
- Termination: [e.g., "90-day notice, early termination fee $Z"]
- Auto-renewal: [Yes/No, notice period]

Review for:
1. **Pricing competitiveness**: Is this market rate? Any hidden fees?
2. **Risk factors**: Long lock-in, auto-renewal traps, weak SLA penalties
3. **Negotiation opportunities**: Volume discounts, flexible terms, better SLAs
4. **Compliance**: Does contract meet our data privacy, security requirements?

Provide 3-5 specific recommendations (e.g., "Negotiate multi-year discount", "Add termination clause after year 1").
```

**Why it works:** Avoids bad deals; strengthens vendor relationships through smart negotiation.

---

### 7. **Budget Variance Analysis**

**Use when:** Understanding why actuals differ from budget

**Prompt:**
```
Department: [e.g., "Marketing"]
Period: [Month/Quarter]

Budget vs. Actual:
- Category 1 (e.g., "Advertising"): Budget $50K, Actual $65K (+30%)
- Category 2 (e.g., "Events"): Budget $20K, Actual $15K (-25%)
- Category 3 (e.g., "Salaries"): Budget $100K, Actual $100K (0%)

Known context:
- [e.g., "Ran unplanned campaign for product launch"]
- [e.g., "Conference canceled due to low attendance"]

For each variance >10%:
1. **Root cause**: Why did this happen? (planned change, one-time event, ongoing trend)
2. **Materiality**: Does this impact annual forecast?
3. **Action**: Continue, adjust budget, or reduce spend going forward?

Distinguish between timing differences (will even out) vs. true over/underspend.
```

**Why it works:** Focuses leadership on meaningful variances; prevents budget surprises.

---

### 8. **Payroll Audit & Error Detection**

**Use when:** Ensuring payroll accuracy before processing

**Prompt:**
```
Payroll period: [Dates]
Employees: [Count]

Potential issues to check:
- Duplicate payments (same employee paid twice)
- Mismatched hours (timesheet vs. payroll system)
- Tax withholding errors (wrong filing status, exemptions)
- Overtime miscalculations (non-exempt employees)
- New hires missing from payroll
- Terminated employees still on payroll

Review checklist:
1. Cross-reference employee list with HRIS (any adds/deletes?)
2. Validate hours worked against timesheets
3. Spot-check tax withholding for 10% of employees
4. Flag anomalies (e.g., "Employee X: 80 hours OT, usually 0")
5. Verify direct deposit details updated

Generate audit report with flagged items for review before payroll run.
```

**Why it works:** Prevents costly payroll errors; ensures compliance with labor laws.

---

### 9. **Employee Offboarding Workflow**

**Use when:** Ensuring departing employees are properly offboarded

**Prompt:**
```
Departing employee:
- Name: [Full Name]
- Last day: [Date]
- Reason: [Resignation/Termination/Retirement]
- Department: [e.g., Engineering]

Generate offboarding checklist:
1. **HR tasks**: Exit interview, final paycheck calculation, benefits termination (COBRA notice), retrieve company property (laptop, badge)
2. **IT tasks**: Revoke system access (email, Slack, VPN, databases), backup files, transfer ownership (docs, projects)
3. **Manager tasks**: Transition knowledge, reassign projects, notify team
4. **Finance tasks**: Final expense report, settle outstanding balances
5. **Legal/Compliance**: Non-disclosure/non-compete reminders, return of confidential data

For each task:
- Owner
- Due date (relative to last day)
- Status

Ensure nothing falls through cracks (especially security/access revocation).
```

**Why it works:** Protects company from security risks; ensures smooth transition.

---

### 10. **Process Improvement Analysis**

**Use when:** Identifying admin bottlenecks and automation opportunities

**Prompt:**
```
Process: [e.g., "Accounts Payable: Invoice to Payment"]

Current state:
- Steps: [list, e.g., "1. Invoice received via email 2. Manual data entry 3. Manager approval 4. Payment"]
- Time: [e.g., "7 days on average"]
- Pain points: [e.g., "Manual data entry error-prone", "Approval delays if manager out of office"]

Analyze:
1. **Bottlenecks**: Where do delays occur most often?
2. **Error-prone steps**: Which steps have highest mistake rate?
3. **Automation opportunities**: What could AI/software automate? (e.g., "OCR for data extraction", "Auto-routing based on amount")
4. **Quick wins**: Low-effort, high-impact improvements (e.g., "Delegate approval authority", "Batch processing")

Provide a roadmap: What to fix first, estimated time/cost savings.
```

**Why it works:** Data-driven process improvement; identifies where AI can help most.

---

## 💡 Pro Tips for AI-Assisted Administration

### DO:
- ✅ **Provide context**: More details = better output (policy rules, historical data, constraints)
- ✅ **Validate compliance**: AI doesn't know your policies; cross-check recommendations
- ✅ **Automate repetitive work**: Invoice extraction, expense flagging, checklist generation
- ✅ **Use structured formats**: Tables, checklists, bullet points for clarity
- ✅ **Iterate and refine**: If output isn't right, adjust prompt and try again

### DON'T:
- ❌ **Trust blindly**: AI can hallucinate; verify numbers, rules, compliance requirements
- ❌ **Share sensitive PII**: Don't paste SSNs, salary, or confidential data into public AI tools
- ❌ **Skip human oversight**: Critical decisions (hiring, firing, payments) need human review
- ❌ **Over-automate**: Some processes benefit from human judgment (employee relations, complex negotiations)
- ❌ **Ignore privacy**: Use enterprise AI tools (not public ChatGPT) for confidential data

---

## 🎓 Advanced Techniques

### **Multi-Step Workflows**
Break complex tasks into steps:
```
"Step 1: Identify all invoices overdue >30 days. Step 2: Categorize by vendor. Step 3: Draft escalation emails. Step 4: Recommend payment priority."
```

### **Scenario Planning**
Explore options:
```
"What if we renegotiate this contract with Vendor X? Compare 3 scenarios: (1) Reduce scope 20% (2) Extend term for discount (3) Switch vendors"
```

### **Compliance Assistant**
Ask AI to explain regulations:
```
"Explain GDPR Article 17 (right to deletion) in plain language. What does HR need to do when employee requests data deletion?"
```

---

## 📊 Measuring AI Impact on Administration

| Metric | Target | How to Track |
|--------|--------|--------------|
| **Invoice processing time** | <2 days | Measure before/after AI automation |
| **Expense report approval time** | <2 days | Track submission to approval cycle |
| **Payroll error rate** | <0.1% | Count errors per pay period |
| **Onboarding completion** | 100% day 1 | Track tasks completed on time |
| **Compliance findings** | Zero material | Count audit findings year-over-year |

---

## 🔗 Related Resources

- **Full Playbook:** [Administration Playbook](../../PLAYBOOKS/playbook-administration.md) - Deep dive on AI admin agents, squad models, compliance
- **AI Integration:** [AI Integration Playbook](../../PLAYBOOKS/playbook-ai-integration.md) - How to implement AI tools in admin workflows
- **Data Contract Template:** [Data Contract](../TEMPLATES/data-contract-template.yaml) - Structure your admin data events

---

## 🤝 Contributing

Found a prompt that works great? Have an admin AI success story? [Open an issue](https://github.com/gusafr/midora-solid-ai/issues) or submit a PR to share with the community!

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
