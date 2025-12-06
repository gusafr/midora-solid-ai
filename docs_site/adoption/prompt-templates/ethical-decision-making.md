# Ethical Decision-Making Prompt

**Category:** Governance & Ethics | **Framework:** SOLID.AI | **Use Case:** Navigating ethical dilemmas

---

## When to Use This Prompt

Use this prompt when **facing ethical questions or dilemmas** related to AI, data, or technology decisions.

**Ideal for:**
- Evaluating risky features or AI capabilities
- Reviewing data usage or privacy questions
- Responding to ethical concerns raised by team
- Preparing for governance review or audit

---

## The Prompt

```
I'm facing an ethical decision about: [DESCRIBE SITUATION/DILEMMA]

Context:
- Stakeholders: [Who's affected?]
- Pressure/Constraints: [Time, budget, competitive pressure, etc.]
- Current thinking: [What we're leaning toward]

Help me analyze this through the SOLID.AI ethical framework:

1. **Stakeholder Impact Analysis**
   Who is affected by this decision, and how?
   
   - **Users/Customers:**
     - Benefits: [What do they gain?]
     - Harms: [What risks do they face?]
     - Consent: [Have they agreed to this?]
   
   - **Employees/Team:**
     - Benefits: [How does this help the team?]
     - Harms: [Does this create burden or ethical discomfort?]
   
   - **Broader Society:**
     - Benefits: [Positive externalities?]
     - Harms: [Negative externalities? Vulnerable populations?]
   
   - **Environment:**
     - Impact: [Resource consumption, sustainability?]

2. **Values Alignment Check**
   - How does this decision align with our stated mission and values?
   - If our users/public knew how we made this decision, would they trust us more or less?
   - Would we be proud to defend this decision publicly?
   - Does this decision treat people as ends in themselves, or as means to our ends?

3. **Transparency & Explainability**
   - Can we clearly explain how this decision/system works?
   - Are we hiding complexity intentionally or unavoidably?
   - What would full transparency look like? What prevents it?
   - How would we respond if this decision/system were exposed in media?

4. **Fairness & Bias Assessment**
   - Could this decision/system treat different groups unfairly?
   - What biases might be encoded (historical, sampling, algorithmic)?
   - How do we test for and mitigate bias?
   - Who's excluded or harmed by this decision, even unintentionally?

5. **Privacy & Consent**
   - What data is collected, used, or shared?
   - Do individuals have meaningful consent and control?
   - Is data collection necessary and proportionate?
   - What are the re-identification or surveillance risks?

6. **Accountability & Oversight**
   - Who is accountable if this goes wrong?
   - What human oversight exists?
   - How do we detect and correct errors or harms?
   - What remediation is available to those harmed?

7. **Long-Term Consequences**
   - What precedent does this set for future decisions?
   - How might this be misused or abused, now or later?
   - What second-order effects might emerge at scale?
   - Are we creating dependencies or lock-in that reduces autonomy?

8. **Alternatives Analysis**
   - What alternative approaches exist?
   - For each alternative:
     - Ethical trade-offs: [What improves/worsens?]
     - Feasibility: [Can we actually do this?]
     - Cost: [Resources, time, opportunity cost]

9. **Decision Framework**
   Based on the above, recommend:
   
   **Option A: Proceed as planned**
   - Justification: [Why this is ethical]
   - Safeguards required: [What mitigations are non-negotiable]
   
   **Option B: Proceed with modifications**
   - Changes needed: [What must be different]
   - Why this is better: [Ethical improvements]
   
   **Option C: Do not proceed**
   - Reasons: [Why risks outweigh benefits]
   - Alternative path: [What to do instead]

10. **Governance & Documentation**
    - Who should approve this decision? (Level of oversight needed)
    - What should be documented for audit/transparency?
    - What ongoing monitoring or review is required?
    - How do we communicate this decision to stakeholders?

Provide a recommendation with clear ethical reasoning.
```

---

## Example Usage

### Input

```
I'm facing an ethical decision about: Using student essay data to train an AI writing assistant

Context:
- Stakeholders: Students (data subjects), teachers (potential users), company (revenue)
- Pressure/Constraints: Competitors are doing this; could significantly improve our product
- Current thinking: We want to do it but anonymize student data first

Help me analyze this through the SOLID.AI ethical framework:
[... paste full prompt above ...]
```

### Expected Output (Condensed)

```markdown
# Ethical Analysis: Student Essay Data for AI Training

## 1. Stakeholder Impact Analysis

**Students (Data Subjects):**
- **Benefits:** Better AI writing feedback (if they use the product)
- **Harms:**
  - Privacy: Essays may contain personal, sensitive information
  - Consent: Students likely didn't consent to commercial AI training
  - Future risk: De-anonymization possible; essays could be reconstructed
  - Trust: May feel betrayed if discovered without clear consent

**Teachers:**
- **Benefits:** Improved AI tool for feedback
- **Harms:** Ethical discomfort if students weren't fully informed

**Company:**
- **Benefits:** Competitive AI model, potential revenue
- **Harms:** Reputational risk if this becomes public scandal

**Society:**
- **Benefits:** Better educational AI tools (if shared broadly)
- **Harms:** Normalizes data extraction from vulnerable populations (students)

## 2. Values Alignment Check

❌ **Mission Alignment:** If your mission is "empowering learners," using their data without clear consent contradicts this.

❌ **Public Defensibility:** "We used student essays to build our AI" would likely cause backlash.

❌ **Treating as Ends:** Students become means to your commercial AI, not ends in themselves.

## 3. Transparency & Explainability

⚠️ **Current State:** Students likely unaware their essays could be used this way.

❌ **Full Transparency:** Would require: "Your essays will train our commercial AI, which may be used by others."

⚠️ **Media Risk:** HIGH - "EdTech Company Uses Student Essays to Train AI" is a bad headline.

## 4. Fairness & Bias

⚠️ **Bias Risk:** Student essays reflect demographic, linguistic, and educational privilege. Training on this data may:
- Favor certain writing styles or dialects
- Disadvantage non-native speakers or neurodiverse writers
- Encode existing educational inequalities

## 5. Privacy & Consent

❌ **Consent:** Likely missing or insufficient. Students consented to submit essays for grading, not AI training.

⚠️ **Anonymization Limits:** Even anonymized text can be re-identified through writing style, topic, or metadata.

❌ **Proportionality:** Using student data for commercial AI training is disproportionate to original purpose (education).

## 6. Accountability & Oversight

❓ **Who's Accountable:** If student is harmed (e.g., essay leaked, bias perpetuated), who takes responsibility?

⚠️ **Human Oversight:** Who ensures data use remains ethical over time?

## 7. Long-Term Consequences

❌ **Precedent:** Sets expectation that student data is extractable for profit.

⚠️ **Misuse:** Trained model could be sold or licensed in ways students didn't anticipate.

⚠️ **Scale Effects:** Normalizes surveillance capitalism in education.

## 8. Alternatives Analysis

| Alternative | Ethical Trade-offs | Feasibility | Cost |
|-------------|-------------------|-------------|------|
| **A: Proceed as planned (anonymized)** | ❌ Still lacks true consent; privacy risk remains | ✅ Easy | Low |
| **B: Obtain explicit opt-in consent** | ✅ Respects autonomy; ⚠️ Low participation may limit AI quality | ⚠️ Requires new consent flow | Medium |
| **C: Use synthetic or public domain data** | ✅ No privacy/consent issues; ⚠️ May reduce AI accuracy | ✅ Feasible | Medium |
| **D: Partner with students as co-creators** | ✅ Empowers students; ✅ Builds trust | ⚠️ Complex; requires incentives | High |
| **E: Don't use student data** | ✅ Avoids all ethical risks; ❌ Competitive disadvantage | ✅ Easy | Opportunity cost |

## 9. Recommended Decision

### **Option B: Proceed with explicit opt-in consent + safeguards**

**Justification:**
- Respects student autonomy
- Aligns with mission of empowering learners
- Reduces reputational and legal risk
- Can still build competitive AI (if enough students opt in)

**Non-Negotiable Safeguards:**

1. **Informed Consent:**
   - Clear, jargon-free explanation: "We want to use your essays to train an AI writing assistant."
   - Specify: Who benefits, how data is used, how long it's retained
   - Opt-in only (not opt-out or buried in ToS)
   - No penalty for declining

2. **Student Benefit:**
   - Students who opt in get early/free access to improved AI tool
   - Consider revenue sharing or scholarships funded by AI product

3. **Data Minimization:**
   - Only use essays explicitly opted in
   - Retain only as long as necessary
   - Delete upon request

4. **Bias Mitigation:**
   - Audit AI for demographic bias before launch
   - Diversify training data beyond opted-in essays if needed

5. **Transparency:**
   - Publish data usage policy publicly
   - Annual report on how student data is used

6. **Oversight:**
   - Ethics review board approves data usage
   - Student representatives on board

**If opt-in rate too low:** Fall back to **Option C (synthetic data)** or **Option E (don't proceed)**.

---

### **Why NOT Option A (anonymized without consent)?**

❌ Anonymization alone doesn't address consent violation.
❌ Students submitted essays for education, not commercial AI.
❌ High risk of public backlash and trust erosion.

---

## 10. Governance & Documentation

**Approval Required:**
- ✅ Ethics Review Board
- ✅ Legal (privacy/FERPA compliance)
- ✅ Student Advisory Council (if exists)
- ✅ Executive leadership

**Documentation:**
- Ethical risk assessment (this document)
- Consent flow design and copy
- Bias audit plan and results
- Data retention and deletion policy

**Ongoing Monitoring:**
- Quarterly review of opt-in rates and student feedback
- Annual bias audit of trained AI
- Incident response plan for data breaches or misuse

**Communication:**
- To students: Transparent invitation to participate with clear value
- To teachers: Partnership in ethical AI development
- To public (if asked): "We use only consensually provided student data, with safeguards"

---

## Summary

| Criterion | Score | Notes |
|-----------|-------|-------|
| **Stakeholder Benefit** | ⚠️ Mixed | Benefits company more than students without consent |
| **Values Alignment** | ❌ Poor | Conflicts with "empowering learners" mission |
| **Transparency** | ❌ Poor | Current plan hides usage from students |
| **Fairness** | ⚠️ Risk | Bias in training data likely |
| **Privacy** | ❌ High Risk | Anonymization insufficient; consent missing |
| **Accountability** | ⚠️ Unclear | Who's responsible for harms? |

**Recommendation: Proceed ONLY with explicit opt-in consent and safeguards (Option B).**

**Do NOT proceed with anonymization alone (Option A) - it's ethically insufficient and legally/reputationally risky.**
```

---

## Customization Tips

**For high-stakes decisions (healthcare, finance, safety):**
Add: "What regulatory or legal compliance requirements apply?"

**For competitive pressure:**
Add: "Does being second-to-market ethically justify cutting corners?"

**For resource constraints:**
Add: "If we can't do this ethically, should we do it at all?"

**For existing systems:**
Add: "What's the ethical obligation to fix deployed systems causing harm?"

---

## Follow-Up Prompts

After the analysis:

```
Draft a communication to students explaining this decision and inviting opt-in participation.
```

```
Create a checklist to ensure all ethical safeguards are implemented before launch.
```

```
Design a bias audit process for the AI trained on student essays.
```

```
What metrics should we track to ensure this decision remains ethical over time?
```

---

## SOLID.AI Principles Applied

- ✅ **Purpose-Led Decisions** - Anchors in mission and values
- ✅ **Ethical Automation** - Prioritizes transparency and accountability
- ✅ **Human-Machine Symbiosis** - Ensures humans remain in control
- ✅ **Continuous Learning** - Includes monitoring and iteration

---

## Related Resources

- **Governance & Ethics:** [DOCS/06-governance-ethics.md](../../DOCS/06-governance-ethics.md)
- **Manifesto:** [MANIFESTO/solid-ai-manifesto-v1.md](../../MANIFESTO/solid-ai-manifesto-v1.md)
- **AI Integration Playbook:** [PLAYBOOKS/playbook-ai-integration.md](../../PLAYBOOKS/playbook-ai-integration.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Share Your Results:** [GitHub Discussions](https://github.com/gusafr/midora-solid-ai/discussions)
