# Organizational Scalability Assessment

**Purpose:** Diagnose scalability ceilings and create a plan to scale both humans and culture

**Framework:** SOLID.AI | **Version:** 1.0  
**Reference:** [Organizational Scalability Playbook](../../PLAYBOOKS/people-culture/organizational-scalability.md)

---

## Quick Assessment (20 minutes)

### Dimension 1: Technical Scalability (____/100)

**Score Your Organization (0-100):**

- **0-20 (Manual Chaos):** Most processes manual, no APIs, siloed tools, scaling = hiring more people
- **21-40 (Basic Automation):** Some scripts/tools, but not integrated, automation islands
- **41-60 (API-First):** APIs exist, some integration, event-driven architecture emerging
- **61-80 (Automation Mesh):** 60%+ processes automated, agents coordinate, data spine operational
- **81-100 (Autonomous):** AI agents handle most routine work, self-healing systems, humans focus on strategy/innovation

**Your Score:** ____/100

**Key Questions:**

1. **What % of your processes are fully automated end-to-end?**
   - [ ] <10% (Manual)
   - [ ] 10-30% (Some automation)
   - [ ] 30-60% (Majority manual with automation islands)
   - [ ] 60-80% (Majority automated)
   - [ ] >80% (Mostly autonomous)

2. **How many systems do you have that DON'T talk to each other?**
   - [ ] >20 (Data swamps, integration hell)
   - [ ] 10-20 (Some silos)
   - [ ] 5-10 (Mostly integrated)
   - [ ] <5 (Unified data spine)
   - [ ] 0 (Everything flows through event mesh)

3. **If you doubled headcount tomorrow, would your systems handle it?**
   - [ ] No, systems would break
   - [ ] Maybe, but lots of manual workarounds needed
   - [ ] Yes, but would need some reconfiguration
   - [ ] Yes, systems scale automatically

---

### Dimension 2: Human Scalability (____/100)

**Score Your Organization (0-100):**

- **0-20 (Hero Culture):** Knowledge in individuals' heads, single points of failure, training takes 6+ months
- **21-40 (Documented Processes):** Some documentation, but not used, still rely on "ask Jane"
- **41-60 (Playbooks & Training):** Playbooks exist and used, new hires productive in 3 months
- **61-80 (Self-Service Knowledge):** AI assistants answer questions, new hires productive in 1 month
- **81-100 (AI-Augmented Experts):** Every person has AI co-pilot, cross-functional fluency, <2 weeks to productivity

**Your Score:** ____/100

**Key Questions:**

1. **What happens if your top performer in [critical function] quits tomorrow?**
   - [ ] We're screwed, 6+ months to recover
   - [ ] Big impact, 3-6 months to replace
   - [ ] Manageable, 1-3 months to replace
   - [ ] Minimal impact, <1 month to replace (knowledge documented)
   - [ ] No impact, AI agents + playbooks cover it

2. **How long does it take a new hire to be fully productive?**
   - [ ] >6 months (Hero culture)
   - [ ] 3-6 months (Some documentation)
   - [ ] 1-3 months (Good playbooks)
   - [ ] <1 month (Self-service learning + AI assistants)
   - [ ] <2 weeks (AI co-pilots do onboarding)

3. **What % of your employees can explain the end-to-end customer journey?**
   - [ ] <10% (Deep silos)
   - [ ] 10-30% (Some cross-functional awareness)
   - [ ] 30-60% (T-shaped people emerging)
   - [ ] 60-80% (Most people have broad context)
   - [ ] >80% (Everyone understands the whole system)

---

### Dimension 3: Cultural Scalability (____/100)

**Score Your Organization (0-100):**

- **0-20 (Founder Dependency):** All decisions go through founder(s), no delegation, culture = "what founder wants"
- **21-40 (Informal Culture):** Unwritten rules, "you had to be there," culture weakens with each hire
- **41-60 (Written Values):** Values documented but not lived, culture feels diluted
- **61-80 (Values-Driven):** Values embedded in decisions, culture propagates through onboarding/rituals
- **81-100 (Self-Reinforcing Culture):** Culture is codified, AI agents enforce values, new hires assimilate quickly

**Your Score:** ____/100

**Key Questions:**

1. **How often do decisions get escalated to the founder/CEO?**
   - [ ] Daily, for almost everything
   - [ ] Multiple times per week
   - [ ] Weekly or less, only for major decisions
   - [ ] Rarely, only strategic pivots
   - [ ] Never, culture and playbooks guide decisions

2. **If you 10x your team, would your culture stay intact?**
   - [ ] No, would completely dilute
   - [ ] Probably not, hard to maintain
   - [ ] Maybe, if we're intentional
   - [ ] Yes, culture is well-documented
   - [ ] Yes, culture self-propagates (rituals, AI reinforcement)

3. **What % of your values are operationalized (not just posters on wall)?**
   - [ ] 0% (Values are aspirational)
   - [ ] 25% (Some values show up in decisions)
   - [ ] 50% (Half are real, half are lip service)
   - [ ] 75% (Most values are lived)
   - [ ] 100% (All values measurable and embedded in processes)

---

## Calculate Overall Scalability Score

**Total:** (_____ + _____ + _____) / 3 = ____/100

**Interpretation:**
- **0-40:** High risk of hitting scalability ceiling soon
- **41-60:** Moderate scalability, targeted improvements needed
- **61-80:** Good scalability, ready for 2-3x growth
- **81-100:** Excellent scalability, ready for 10x+ growth

---

## Identify Your Scalability Ceiling

**Which ceiling pattern are you hitting? (Check all that apply)**

### Ceiling 1: Founder Bottleneck
- [ ] CEO/founder approves all hires, major decisions, customer deals
- [ ] Team waits for founder's input before acting
- [ ] Founder works 70+ hours/week, constantly firefighting
- [ ] Culture = "What would [founder name] do?"

**Symptoms:**
- Decision velocity slows as team grows
- Founder burning out
- Team feels disempowered

**Your Reality:**
- Founder approval required for: ______________________________
- Decisions waiting for founder: _____ per week
- Founder working hours per week: _____

**Root Cause:** Founder hasn't delegated decision-making authority or codified decision frameworks.

---

### Ceiling 2: Communication Overhead
- [ ] Meetings multiply with each new hire
- [ ] Information silos between teams
- [ ] Context constantly re-explained
- [ ] "Wait, who's working on this?" happens frequently

**Symptoms:**
- Meeting hours increase quadratically (n² problem)
- Duplicate work across teams
- Decisions made without full context

**Your Reality:**
- Average meeting hours per person per week: _____
- How often duplicate work discovered: ☐ Daily ☐ Weekly ☐ Monthly ☐ Rarely
- How often critical info missed: ☐ Daily ☐ Weekly ☐ Monthly ☐ Rarely

**Root Cause:** No shared context layer (data spine, knowledge graphs, AI assistants).

---

### Ceiling 3: Knowledge Silos
- [ ] Critical knowledge trapped in individuals' heads
- [ ] "Bus factor" = 1 for key systems/processes
- [ ] New hires take 6+ months to be productive
- [ ] Documentation exists but outdated/not used

**Symptoms:**
- Single points of failure (people)
- Long ramp times
- Reliance on "Ask [person name]"

**Your Reality:**
- Processes with bus factor = 1: _____
- Time to productivity for new hires: _____ months
- % of documentation up-to-date: _____%

**Root Cause:** Knowledge not externalized, playbooks don't exist or aren't maintained.

---

### Ceiling 4: Process Rigidity
- [ ] Processes designed for current size, break when scaled
- [ ] Manual approval chains with 5+ steps
- [ ] Exception handling requires heroics
- [ ] "That's how we've always done it"

**Symptoms:**
- Processes slow down as volume increases
- Bottlenecks at manual approval steps
- Can't handle edge cases

**Your Reality:**
- Manual approval steps in critical processes: _____
- Time from request to approval: _____ days (goal: <1 day)
- % of requests that are "exceptions": _____%

**Root Cause:** Processes not designed for scale, no automation or self-service.

---

## Create Your Scalability Action Plan

### Priority 1: Biggest Ceiling (Choose One Above)

**Ceiling:** ______________________________

**Current Impact:**
- Preventing growth of: ☐ Revenue ☐ Team size ☐ Product complexity ☐ Customer base
- Costing us: $_____ per month (opportunity cost)
- Causing: _____ hours of wasted time per week

**Target State (6 months):**
- _____________________________________________________
- _____________________________________________________

**Actions (Next 90 Days):**

1. **Action:** _____________________________________________________
   - **Owner (DRI):** _____________________________
   - **Due Date:** _____________________________
   - **Success Metric:** _____________________________

2. **Action:** _____________________________________________________
   - **Owner (DRI):** _____________________________
   - **Due Date:** _____________________________
   - **Success Metric:** _____________________________

3. **Action:** _____________________________________________________
   - **Owner (DRI):** _____________________________
   - **Due Date:** _____________________________
   - **Success Metric:** _____________________________

---

### Priority 2: Technical Scalability (if score <60)

**Current Score:** ____/100  
**Target Score (6 months):** ____/100

**Specific Actions:**

- [ ] **Build API-first architecture**
  - Identify top 5 manual processes: _____________________________
  - Expose APIs for each: Due date _____________________________
  - Owner: _____________________________

- [ ] **Implement event-driven data spine**
  - Define 10 core events: _____________________________
  - Set up event streaming (Kafka/Pulsar): Due date _____________________________
  - Owner: _____________________________

- [ ] **Deploy first 3 AI agents**
  - Agent 1: _____________________________ (automates _____% of _____ process)
  - Agent 2: _____________________________ (automates _____% of _____ process)
  - Agent 3: _____________________________ (automates _____% of _____ process)
  - Owner: _____________________________

**Resources Needed:**
- Budget: $_____
- Headcount: _____ (engineers, data, etc.)
- Timeline: _____ months

**Success Metrics:**
- Automation rate: Current _____% → Target _____%
- API coverage: Current _____% → Target _____%
- Agent-handled tasks: 0 → Target _____/month

---

### Priority 3: Human Scalability (if score <60)

**Current Score:** ____/100  
**Target Score (6 months):** ____/100

**Specific Actions:**

- [ ] **Externalize critical knowledge**
  - Identify top 5 "hero" dependencies: _____________________________
  - Create playbooks for each: Due date _____________________________
  - Owner: _____________________________

- [ ] **Build self-service knowledge base**
  - Deploy AI assistant (ChatGPT, internal LLM): Due date _____________________________
  - Ingest all documentation: Due date _____________________________
  - Usage target: _____% of team using daily
  - Owner: _____________________________

- [ ] **Cross-train for T-shaped skills**
  - Run "Day in the Life" swaps: _____ pairs per month
  - Job rotation program: _____ people rotate per quarter
  - All-hands "How [X] Works" sessions: _____ per month
  - Owner: _____________________________

**Resources Needed:**
- Budget: $_____
- Headcount: _____ (knowledge management, training)
- Timeline: _____ months

**Success Metrics:**
- Bus factor: Current _____ → Target _____ (>3 for all critical processes)
- Time to productivity: Current _____ months → Target _____ months (<1 month)
- Cross-functional fluency: Current _____% → Target _____% (70%+)

---

### Priority 4: Cultural Scalability (if score <60)

**Current Score:** ____/100  
**Target Score (6 months):** ____/100

**Specific Actions:**

- [ ] **Codify decision-making frameworks**
  - Define decision types: Strategic (CEO), Operational (Managers), Tactical (Teams)
  - Create "Type 1 vs Type 2" decision guide (Amazon model)
  - Document: "Who decides what?" matrix
  - Due date: _____________________________
  - Owner: _____________________________

- [ ] **Operationalize values**
  - For each value, define 3 observable behaviors: Due date _____________________________
  - Add values to interview scorecards: Due date _____________________________
  - Add values to performance reviews: Due date _____________________________
  - Track: % of decisions citing values: Current _____% → Target _____%
  - Owner: _____________________________

- [ ] **Create cultural rituals**
  - Weekly "wins" sharing: Start date _____________________________
  - Monthly all-hands with Q&A: Start date _____________________________
  - Quarterly culture surveys: Start date _____________________________
  - AI agent to reinforce culture (e.g., Slackbot with values prompts): Deploy date _____________________________
  - Owner: _____________________________

**Resources Needed:**
- Budget: $_____
- Headcount: _____ (culture/HR lead)
- Timeline: _____ months

**Success Metrics:**
- Founder approval rate: Current _____/week → Target _____/week (<5)
- Values mentioned in decisions: Current _____% → Target _____% (80%+)
- Employee NPS: Current _____ → Target _____ (50+)

---

## Avoid Common Anti-Patterns

**Check if you're doing any of these (and stop immediately):**

### Anti-Pattern 1: Premature Scaling
- [ ] Hiring aggressively before product-market fit
- [ ] Building for 10x scale when at 1x
- [ ] Over-engineering infrastructure

**Fix:** Focus on product-market fit first. Scale when demand exceeds capacity.

---

### Anti-Pattern 2: Process Bureaucracy
- [ ] Adding approval layers "for control"
- [ ] Requiring sign-offs from 5+ people
- [ ] "Best practices" from 10,000-person companies applied to 50-person startup

**Fix:** Default to autonomy. Use AI agents for compliance checks, not human approval chains.

---

### Anti-Pattern 3: Hero Worship
- [ ] Celebrating "saving the day" heroics
- [ ] Tolerating knowledge hoarding
- [ ] Rewarding individual brilliance over team capability

**Fix:** Reward externalizing knowledge, teaching others, building systems. Make heroes obsolete.

---

### Anti-Pattern 4: Culture Neglect
- [ ] "We'll worry about culture later"
- [ ] Values as posters, not practices
- [ ] Hiring for skills only, ignoring values fit

**Fix:** Culture compounds. Define and embed values from Day 1.

---

### Anti-Pattern 5: Scaling Dysfunction
- [ ] Hiring more people to solve broken processes
- [ ] Adding layers of management instead of fixing systems
- [ ] "We'll clean up technical debt after we scale"

**Fix:** Fix the process FIRST, then scale. Scaling dysfunction = faster failure.

---

## Monthly Scalability Check-Ins

**Track progress monthly:**

| Month | Technical Score | Human Score | Cultural Score | Overall Score | Ceiling Hit? |
|-------|----------------|-------------|----------------|---------------|--------------|
| Baseline | ____/100 | ____/100 | ____/100 | ____/100 | ____________ |
| Month 1 | ____/100 | ____/100 | ____/100 | ____/100 | ____________ |
| Month 2 | ____/100 | ____/100 | ____/100 | ____/100 | ____________ |
| Month 3 | ____/100 | ____/100 | ____/100 | ____/100 | ____________ |
| Month 6 | ____/100 | ____/100 | ____/100 | ____/100 | ____________ |

**Re-score dimensions monthly. If any score drops >10 points, investigate why.**

---

## Success Criteria

**After 6 months, you should have:**
- [x] All 3 dimensions scored >60 (ready for 2-3x growth)
- [x] Top ceiling addressed (action plan executed)
- [x] Automation rate >40% (technical scalability improving)
- [x] Time to productivity <2 months (human scalability improving)
- [x] Founder approval rate <5/week (cultural scalability improving)

**After 12 months, you should have:**
- [x] All 3 dimensions scored >80 (ready for 10x growth)
- [x] No active ceilings (can scale without bottlenecks)
- [x] Automation rate >60%
- [x] Time to productivity <1 month
- [x] Self-reinforcing culture (AI agents + rituals)

---

## Resources

**Related Playbooks:**
- [Organizational Scalability](../../PLAYBOOKS/people-culture/organizational-scalability.md) - Full framework
- [Maturity Model](../../PLAYBOOKS/foundation/solid-ai-maturity-model.md) - Maturity progression
- [AI Learning & Development](../../PLAYBOOKS/people-culture/ai-learning-development.md) - Build human capacity

**Checklists:**
- [AI Maturity Assessment](./ai-maturity-assessment.md) - Assess AI maturity
- [Learning Development Rollout](./learning-development-rollout.md) - Scale human capability
- [SME Transformation Roadmap](./sme-transformation-roadmap.md) - Complete transformation plan

**Templates:**
- [90-Day Transformation Plan](../TEMPLATES/90-day-transformation-plan.md) - Execution roadmap

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Framework:** SOLID.AI
