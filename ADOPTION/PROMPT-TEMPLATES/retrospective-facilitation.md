# Retrospective Facilitation Prompt

**Category:** Team Learning | **Framework:** SOLID.AI | **Use Case:** Continuous improvement

---

## When to Use This Prompt

Use this prompt to **facilitate effective retrospectives** that drive continuous learning and improvement aligned with SOLID.AI principles.

**Ideal for:**
- Sprint or iteration retrospectives
- Post-incident reviews
- Project post-mortems
- Quarterly team health checks

---

## The Prompt

```
Facilitate a retrospective for: [TEAM/PROJECT/SPRINT/INCIDENT]

Context:
- Timeframe: [What period are we reviewing?]
- Participants: [Who's in the retro?]
- Key events: [Major milestones, challenges, or incidents]

Guide us through a SOLID.AI retrospective focusing on continuous learning:

1. **Set the Stage (Psychological Safety)**
   - Remind participants: We focus on systems, not individuals
   - Goal: Learn and improve, not blame
   - Suggested opening: [Propose an icebreaker or framing]

2. **Gather Data (What Happened)**
   - Timeline of events (objective facts only)
   - Metrics and outcomes (quantitative)
   - Sentiment and experience (qualitative)
   - Human-AI interactions (where relevant)

3. **Generate Insights (Why It Happened)**
   Analyze through SOLID.AI lenses:
   
   **Purpose Alignment:**
   - Did we stay true to our mission and values?
   - Where did we optimize for wrong metrics?
   
   **Human-AI Symbiosis:**
   - How did AI augment or hinder our work?
   - Where did humans and AI collaborate well or poorly?
   
   **Organizational Design:**
   - Did our squad/pool structure support the work?
   - Were decision rights clear?
   
   **Data & Observability:**
   - Did we have the information we needed, when needed?
   - What visibility gaps slowed us down?
   
   **Ethics & Governance:**
   - Were ethical considerations surfaced early?
   - Did our guardrails work as intended?

4. **Decide What to Do (Action Items)**
   - **Continue:** What's working that we should keep doing?
   - **Stop:** What's not working that we should eliminate?
   - **Start:** What new practices should we experiment with?
   - **Learn:** What questions do we still have? What experiments to run?
   
   For each action:
   - Owner: [Who's responsible?]
   - Timeline: [By when?]
   - Success criteria: [How do we know it worked?]

5. **Close (Commit to Learning)**
   - Summary of key insights
   - Appreciation for team contributions
   - Commitment to action items
   - Date for follow-up check-in

Format output as:
- Facilitation guide (for the facilitator)
- Action items (trackable todos)
- Insights summary (shareable learning)
```

---

## Example Usage

### Input

```
Facilitate a retrospective for: Product Squad's Q3 Sprint Retrospective

Context:
- Timeframe: Last 2-week sprint
- Participants: 6 developers, 1 product manager, 1 designer
- Key events: Launched AI-powered course recommendation feature, had one production incident, missed velocity target

Guide us through a SOLID.AI retrospective focusing on continuous learning:
[... paste full prompt above ...]
```

### Expected Output

```markdown
# Q3 Sprint Retrospective Facilitation Guide

## Set the Stage (5 minutes)

**Opening:**
"Welcome everyone. This retrospective is about learning and improving our systems, not placing blame. We're here to understand what happened, why, and how we can do better together."

**Icebreaker:**
"In one word, how are you feeling about this sprint?" (Go around the room)

**Ground Rules:**
- Focus on systems and processes, not individuals
- Everyone's voice matters - speak up and listen actively
- Commit to actionable outcomes

---

## Gather Data (10 minutes)

### Timeline of Events
1. **Day 1:** Sprint kickoff, AI recommendation feature planning
2. **Day 5:** Feature merged to main, deployed to staging
3. **Day 7:** Production deploy (80% rollout)
4. **Day 8:** Incident - recommendation engine returned stale data for 2 hours
5. **Day 9:** Incident resolved, rollback to 50%
6. **Day 10:** Root cause: cache invalidation bug
7. **Day 12:** Full deploy with fix
8. **Day 14:** Sprint close, velocity 32 points (target was 40)

### Metrics
- **Velocity:** 32/40 points (80% of target)
- **Incident duration:** 2 hours
- **User impact:** ~15% of users saw stale recommendations
- **Feature adoption:** 45% of eligible users engaged (exceeded 30% target)
- **AI performance:** 78% recommendation accuracy (target 75%)

### Sentiment & Experience
(Facilitator: Ask team to share on sticky notes or digital board)
- What went well?
- What was frustrating?
- What surprised us?

---

## Generate Insights (20 minutes)

### Purpose Alignment
**Q: Did we stay true to our mission of empowering students with personalized learning?**

Insights:
- ✅ Feature adoption exceeded expectations - users finding value
- ⚠️ Incident compromised trust temporarily (stale recommendations)
- ✅ We prioritized getting AI accuracy right before pushing volume

**Q: Where did we optimize for wrong metrics?**
- ⚠️ We focused on velocity (40 points) but quality/stability mattered more
- ✅ Good call to rollback rather than push through incident

---

### Human-AI Symbiosis
**Q: How did AI augment or hinder our work?**

Insights:
- ✅ AI recommendations working well once deployed correctly
- ⚠️ Cache complexity added cognitive load - took time to debug
- ✅ AI agent (recommendation engine) has clear ownership and monitoring now

**Q: Where did humans and AI collaborate well or poorly?**
- ✅ Product team provided great test cases for AI validation
- ⚠️ We didn't have human-reviewable logs during incident (debugging was hard)

---

### Organizational Design
**Q: Did our squad structure support the work?**

Insights:
- ✅ Cross-functional squad worked well for feature development
- ⚠️ Incident response lacked clear ownership (overlapping with platform team)
- ⚠️ Designer felt underutilized mid-sprint

**Q: Were decision rights clear?**
- ✅ Product manager made clear trade-off decisions on scope
- ⚠️ Unclear who could decide to rollback during incident (escalated unnecessarily)

---

### Data & Observability
**Q: Did we have the information we needed, when needed?**

Insights:
- ⚠️ Cache invalidation wasn't instrumented - incident detection was slow
- ⚠️ No alerting on recommendation staleness
- ✅ Once incident started, logs helped us root cause quickly

**Q: What visibility gaps slowed us down?**
- Cache layer is a black box
- No end-to-end trace from user request → recommendation → display

---

### Ethics & Governance
**Q: Were ethical considerations surfaced early?**

Insights:
- ✅ We discussed bias in recommendations during planning
- ✅ Validated recommendations against diverse student cohorts
- ⚠️ Didn't fully consider impact of stale recommendations on trust

**Q: Did our guardrails work as intended?**
- ✅ Rollback plan worked (we fell back to rule-based recommendations)
- ⚠️ No automated rollback triggered - relied on manual detection

---

## Decide What to Do (15 minutes)

### CONTINUE (Keep Doing)
1. ✅ **Cross-functional sprint planning**
   - Owner: Product Manager
   - Why: Kept team aligned and avoided siloes

2. ✅ **AI accuracy validation before launch**
   - Owner: Dev Lead
   - Why: Ensured we met user value targets

3. ✅ **Rollback readiness**
   - Owner: Everyone
   - Why: Saved us during incident

---

### STOP (Eliminate)
1. ❌ **Velocity-driven commitments**
   - Owner: Product Manager + Team
   - Why: Created pressure that led to missed observability
   - Replace with: Outcome-based goals

2. ❌ **Deploying without cache monitoring**
   - Owner: Dev Lead
   - Why: Blind spot that caused incident

---

### START (New Practices)
1. ✨ **Instrument cache layer with staleness alerts**
   - Owner: DevOps Engineer (Jane)
   - Timeline: By next sprint planning
   - Success: Alert fires if cache >10 min stale

2. ✨ **Incident command clarity**
   - Owner: Engineering Manager
   - Timeline: This week
   - Success: Runbook with roles (IC, communicator, resolver)

3. ✨ **End-to-end tracing for AI features**
   - Owner: Dev Lead (Carlos)
   - Timeline: Add to backlog, prioritize next sprint
   - Success: Can trace user request → AI decision → response

4. ✨ **Designer involvement checklist**
   - Owner: Product Manager + Designer (Aisha)
   - Timeline: Before next sprint
   - Success: Clear touchpoints for design through sprint

---

### LEARN (Experiments & Questions)
1. 🔬 **Experiment: Automated rollback triggers**
   - Question: Can we auto-rollback on error rate spike?
   - Owner: DevOps Engineer (Jane)
   - Timeline: Spike this sprint, decide next retro

2. ❓ **Open Question: Velocity vs. Quality balance**
   - Question: What's the right balance? How do we measure quality?
   - Owner: Team discussion next sprint planning

---

## Close (5 minutes)

### Key Insights Summary
- We delivered user value (45% adoption 🎉) but had an avoidable incident
- Observability gaps (cache layer) slowed us down
- Velocity pressure may have contributed to missed instrumentation
- Team collaboration strong, but incident roles need clarity
- AI-human collaboration working well in feature development

### Appreciation
"Shout-outs: Carlos for debugging the cache issue under pressure, Aisha for user testing scenarios, Jane for getting rollback working quickly."

### Commitment
"We're committing to 4 START actions and 2 STOP actions. Let's revisit these in next retro."

### Follow-Up
Next retro: [Date in 2 weeks]
Interim check-in: [Date in 1 week] - review progress on action items

---

## Action Items Tracker

| Action | Type | Owner | Timeline | Success Criteria |
|--------|------|-------|----------|------------------|
| Instrument cache staleness | START | Jane | Next sprint planning | Alert fires if cache >10 min stale |
| Incident command runbook | START | Eng Manager | This week | Runbook published with clear roles |
| End-to-end tracing | START | Carlos | Next sprint (backlog) | Can trace request → AI → response |
| Designer touchpoints checklist | START | PM + Aisha | Before next sprint | Clear design involvement plan |
| Shift from velocity to outcomes | STOP | PM + Team | Next sprint planning | Goals framed as outcomes not points |
| Don't deploy without cache monitoring | STOP | Dev Lead | Ongoing | No cache changes without instrumentation |
| Spike: Auto-rollback triggers | LEARN | Jane | This sprint | Decision on feasibility by next retro |
| Discuss: Velocity vs. Quality | LEARN | Team | Next sprint planning | Team alignment on balance |

---

## Shareable Learning

**For broader team/company:**
- ✅ **Win:** AI recommendation feature exceeded adoption targets
- ⚠️ **Learning:** Cache layers need observability before production
- 🔧 **Action:** Establishing incident command roles for clearer response
- 📚 **Pattern:** Balance velocity pressure with quality instrumentation

(Share in: #eng-learning Slack channel, next All-Hands, RFC if systemic)
```

---

## Customization Tips

**For post-incident reviews (blameless):**
Add: "Focus on system resilience and learning, not individual actions"

**For project post-mortems:**
Add: "What would we do differently if starting this project today?"

**For quarterly health checks:**
Add: "How is team morale and sustainability? What's causing burnout?"

**For AI-heavy teams:**
Add: "Analyze AI agent performance, ethical compliance, and human oversight effectiveness"

---

## Follow-Up Prompts

After the retrospective:

```
Convert these action items into concrete tasks we can add to our sprint backlog.
```

```
Draft a brief summary of this retrospective's learnings to share with leadership.
```

```
Suggest experiments we could run to test our "START" hypotheses.
```

```
Create a template for our next retrospective based on what worked well this time.
```

---

## SOLID.AI Principles Applied

- ✅ **Continuous Learning** - Core purpose of retrospectives
- ✅ **Purpose-Led Decisions** - Evaluates alignment with mission
- ✅ **Human-Machine Symbiosis** - Reviews AI collaboration
- ✅ **Intelligent Decentralization** - Examines squad effectiveness
- ✅ **Ethical Automation** - Checks governance and ethics

---

## Related Resources

- **Operations Playbook:** [PLAYBOOKS/playbook-operations.md](../../PLAYBOOKS/playbook-operations.md)
- **Squad Playbook:** [PLAYBOOKS/playbook-squads.md](../../PLAYBOOKS/playbook-squads.md)
- **Principles:** [DOCS/01-principles.md](../../DOCS/01-principles.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Share Your Results:** [GitHub Discussions](https://github.com/gusafr/midora-solid-ai/discussions)
