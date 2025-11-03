# Purpose-Driven Feature Development Prompt

**Category:** Development | **Framework:** SOLID.AI | **Use Case:** Starting new features

---

## When to Use This Prompt

Use this prompt at the **start of any new feature development** to ensure alignment with SOLID.AI principles before writing code.

**Ideal for:**
- Feature kickoff meetings
- Technical design discussions
- Clarifying requirements with product managers
- Preventing misaligned implementations

---

## The Prompt

```
I need to implement [FEATURE DESCRIPTION].

Before writing code, help me think through:

1. **Human-Centered Purpose**
   - What real human need does this feature serve?
   - How does it improve lives, not just metrics?
   - What does "success" look like from a user perspective?

2. **Mission Alignment**
   - How does this feature connect to our company's core mission?
   - Does it reinforce or dilute our values?
   - What would we lose if we didn't build this?

3. **Ethical Considerations**
   - Who might be harmed by this feature, even unintentionally?
   - What biases could be introduced or amplified?
   - How do we protect privacy, consent, and autonomy?
   - What are potential misuse scenarios?

4. **AI Collaboration Opportunity**
   - Could AI augment this feature (co-pilot model)?
   - Could AI automate parts safely (with human oversight)?
   - Where must human judgment remain non-negotiable?

5. **Success Metrics Beyond "Shipped"**
   - How will we measure actual user value?
   - What leading indicators show we're on track?
   - What would cause us to rollback or pivot?
   - How do we capture learnings for iteration?

After answering these questions, suggest:
- A purpose statement (1-2 sentences)
- An implementation approach aligned with the above
- Key risks and mitigation strategies
- Observability and learning hooks to build in
```

---

## Example Usage

### Input

```
I need to implement an AI-powered resume screening feature for our hiring platform.

Before writing code, help me think through:
[... paste full prompt above ...]
```

### Expected Output

The AI will provide:
- **Purpose analysis** - e.g., "This feature serves recruiters overwhelmed by volume, but must not discriminate or reduce human connection in hiring"
- **Ethical risks** - e.g., "Risk of encoding historical hiring biases; need demographic blind review and bias auditing"
- **AI opportunities** - e.g., "AI can surface candidates, but final decisions must remain with humans"
- **Implementation approach** - e.g., "Build as a ranking assistant with explainable scoring and human override"
- **Success metrics** - e.g., "Track time-to-hire, candidate diversity, and recruiter satisfaction—not just throughput"

---

## Customization Tips

**For AI-heavy features:**
Add: "How do we make AI decisions explainable and auditable?"

**For data-intensive features:**
Add: "What data contracts and quality requirements exist?"

**For user-facing features:**
Add: "How do we gather continuous feedback from real users?"

**For internal tools:**
Add: "How does this reduce cognitive load vs. create new complexity?"

---

## Follow-Up Prompts

After getting initial answers, drill deeper:

```
Based on the purpose we identified, what would a minimal viable version look like that still delivers core value?
```

```
What specific observability do we need to detect if this feature is causing unintended harm?
```

```
How do we design the feature to evolve based on learning, not just ship-and-forget?
```

---

## SOLID.AI Principles Applied

- ✅ **Purpose-Led Decisions** - Starts with "why" before "how"
- ✅ **Ethical Automation** - Proactively addresses potential harms
- ✅ **Human-Machine Symbiosis** - Identifies right balance of AI and human
- ✅ **Continuous Learning** - Builds in feedback and iteration mechanisms

---

## Related Resources

- **Developer Reference Card:** [REFERENCE-CARDS/developer-reference.md](../REFERENCE-CARDS/developer-reference.md)
- **AI Integration Playbook:** [PLAYBOOKS/playbook-ai-integration.md](../../PLAYBOOKS/playbook-ai-integration.md)
- **Principles:** [DOCS/01-principles.md](../../DOCS/01-principles.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Share Your Results:** [GitHub Discussions](https://github.com/gusafr/midora-solid-ai/discussions)
