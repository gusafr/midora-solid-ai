# AI-Native Sprint Checklist

**For:** Teams adopting AI-Native Agile ceremonies (Monday→Friday sprint rhythm with AI agents as participants)

**Goal:** Run productive weekly sprints where humans + AI agents collaborate, with AI handling coordination, insights, retrospectives

**Time:** 1 week per sprint (Monday planning → Friday retro), 4-6 weeks to establish rhythm

---

## Why AI-Native Sprint?

**Traditional Agile Problem:**
- **Meetings dominated by status updates** (not strategy/problem-solving)
- **Retrospectives are subjective** (no data, just opinions)
- **Sprint planning takes 2-4 hours** (manual story sizing, dependency mapping)
- **Daily standups feel like theatre** (people say "I'm working on X" without insights)

**AI-Native Agile Solution:**
- **AI Agents Participate:** SprintPlanner-Agent, StandupFacilitator-Agent, RetroAnalyzer-Agent
- **Data-Driven:** All ceremonies use real metrics (velocity, cycle time, blocker duration)
- **Time-Efficient:** Sprint planning <1 hour (AI pre-analyzes backlog), standups <15min (AI surfaces blockers)
- **Continuous Improvement:** Retro insights tracked sprint-over-sprint, AI flags recurring patterns

**See:** [AI-Native Agile Documentation](../DOCS/11-ai-native-agile.md)

---

## Pre-Sprint Setup (One-Time)

### **Deploy 3 AI Agents**

- [ ] **SprintPlanner-Agent** (Intermediate-Level Coordinator)
  - Role: Analyze backlog, recommend story prioritization, flag dependencies
  - Tools: Jira/Linear + AI (ChatGPT/Claude API)
  - Cost: ~$1K-$2K/month (Intermediate-Level)

- [ ] **StandupFacilitator-Agent** (Low-Level Assistant)
  - Role: Collect daily updates asynchronously, surface blockers, prepare standup agenda
  - Tools: Slack + Jira/Linear
  - Cost: ~$200-$500/month (Low-Level)

- [ ] **RetroAnalyzer-Agent** (Intermediate-Level Analyst)
  - Role: Analyze sprint metrics (velocity, cycle time, bug rate), generate retro insights
  - Tools: Jira/Linear + BI (Tableau/Looker) + AI
  - Cost: ~$1K-$2K/month (Intermediate-Level)

**See:** [Agent Definition Template](../ADOPTION/TEMPLATES/agent-definition-template.yaml), [AI Agents Guide](../DOCS/05-ai-agents.md)

---

### **Configure Sprint Metrics Dashboard**

- [ ] **Set up real-time dashboard** (use Jira dashboard, Linear insights, or custom BI)

| Metric | What It Measures | Target | Sprint 1 | Sprint 2 | Sprint 3 |
|--------|------------------|--------|----------|----------|----------|
| **Velocity** | Story points completed per sprint | 20-30 | ___ | ___ | ___ |
| **Cycle Time** | Days from "In Progress" → "Done" | <5 days | ___ | ___ | ___ |
| **WIP (Work in Progress)** | # stories in progress simultaneously | <5 | ___ | ___ | ___ |
| **Blocker Duration** | Hours spent on blocked stories | <8h/sprint | ___ | ___ | ___ |
| **Bug Rate** | Bugs introduced per 10 stories shipped | <2 | ___ | ___ | ___ |
| **Deployment Frequency** | Deploys per sprint | >3 | ___ | ___ | ___ |

- [ ] **Grant AI agents read access** to project management tool (Jira/Linear API keys)

---

### **Define Team Composition**

Map your team (humans + AI agents) to roles:

| Role | Name | Level | Responsibilities |
|------|------|-------|-----------------|
| **Product Owner** | [Human Name] | High-Level | Define priorities, accept stories |
| **Tech Lead** | [Human Name] | High-Level | Architecture, code review, technical decisions |
| **Engineer 1** | [Human Name] | Intermediate-Level | Implement features, write tests |
| **Engineer 2** | [Human Name] | Intermediate-Level | Implement features, write tests |
| **Engineer 3** | [AI Agent: DevAssist-Agent] | Low-Level | Generate code, write tests, create docs |
| **QA** | [Human or AI: QA-Agent] | Low-Level | Run tests, log bugs |
| **Sprint Planner** | [AI: SprintPlanner-Agent] | Intermediate-Level | Backlog analysis, dependency mapping |
| **Standup Facilitator** | [AI: StandupFacilitator-Agent] | Low-Level | Collect updates, surface blockers |
| **Retro Analyzer** | [AI: RetroAnalyzer-Agent] | Intermediate-Level | Analyze metrics, generate insights |

**See:** [Role Hierarchy](../DOCS/10-role-hierarchy.md)

---

## Monday: Sprint Planning (1 hour)

### **Pre-Planning (AI Agent Work — Sunday Evening)**

- [ ] **SprintPlanner-Agent runs pre-analysis** (automated, no human involvement)
  - Analyze backlog: Which stories are ready? (clear requirements, designs attached, dependencies resolved)
  - Estimate velocity: Based on last 3 sprints, how many points can team complete?
  - Flag dependencies: Which stories depend on external teams? (highlight risk)
  - Recommend prioritization: Using business value + technical risk scoring

**Output:** `SPRINT-PLAN-DRAFT.md` posted to Slack #sprint-planning channel Sunday night

**Example:**

> **SprintPlanner-Agent — Sprint 15 Draft Plan**
>
> **Recommended Capacity:** 25 story points (based on last 3 sprints: 22, 26, 24)
>
> **Top Priorities (Business Value × Readiness):**
> 1. [STORY-101] Add OAuth login (8 points) — High value, low risk, all dependencies resolved ✅
> 2. [STORY-87] Fix checkout bug (3 points) — Blocks revenue, quick win ⚠️
> 3. [STORY-92] API rate limiting (5 points) — Medium value, requires DevOps sync 🔗
> 4. [STORY-110] Export to CSV (5 points) — High customer demand, clear requirements ✅
> 5. [STORY-105] Notification preferences (5 points) — Low risk, designs approved ✅
>
> **⚠️ Risks:**
> - [STORY-92] depends on DevOps (ETA: Wednesday) — risk of delay
> - [STORY-87] is critical path for revenue — prioritize
>
> **📊 Velocity Trend:** Increasing (+8% over 3 sprints) — team is improving
>
> **💡 Recommendation:** Commit to 25 points, backlog STORY-92 if DevOps delayed

---

### **Sprint Planning Meeting (60 minutes, Monday 9am)**

- [ ] **Review SprintPlanner-Agent Recommendations** (10 minutes)
  - Product Owner: "Do these priorities align with business goals?"
  - Tech Lead: "Are technical risks accurately flagged?"

- [ ] **Refine & Commit** (30 minutes)
  - Team discusses each story
  - Adjust estimates if needed (AI's estimate is a starting point)
  - Commit to sprint goal (e.g., "Ship OAuth login + fix critical bugs")

- [ ] **Assign Work** (15 minutes)
  - Product Owner assigns stories to humans/AI agents
  - Example: STORY-101 (OAuth) → Engineer 1 (human) + DevAssist-Agent (AI generates boilerplate code)
  - Example: STORY-87 (bug fix) → Engineer 2 (human) + QA-Agent (AI runs regression tests)

- [ ] **Set Sprint Success Criteria** (5 minutes)
  - Product Owner: "What must ship for this sprint to be successful?"
  - Example: "OAuth working in production + checkout bug fixed = success"

**Output:** Sprint backlog committed in Jira/Linear, all stories assigned

---

## Tuesday-Thursday: Daily Standup (15 minutes, async-first)

### **Async Standup (AI-Driven, 9am Daily)**

- [ ] **StandupFacilitator-Agent collects updates** (automated, no manual input)
  - Pulls data from Jira/Linear, GitHub, Slack
  - Generates standup summary

**Example Slack Post (Tuesday 9am):**

> **StandupFacilitator-Agent — Sprint 15, Day 2**
>
> **✅ Progress:**
> - [STORY-101] OAuth login: 60% complete (Engineer 1 + DevAssist-Agent shipped Google provider, working on GitHub)
> - [STORY-87] Checkout bug: Fixed, in QA (Engineer 2, QA-Agent running tests)
>
> **🚧 Blockers:**
> - [STORY-92] API rate limiting: Waiting on DevOps (ETA: Wednesday) — **⚠️ At risk**
>
> **📊 Metrics:**
> - Velocity: 12/25 points complete (48% of sprint, on track)
> - Cycle time: 3.2 days (target: <5 days) ✅
> - WIP: 4 stories in progress (target: <5) ✅
>
> **💬 Human Input Needed:**
> - @Engineer1: Do you need help with GitHub OAuth?
> - @ProductOwner: Should we de-scope STORY-92 if DevOps delayed?

---

### **Live Standup (Optional, 15 minutes, 9:15am)**

- [ ] **Only if blockers flagged by AI** (otherwise skip meeting)
  - Focus on: How to unblock STORY-92? (call DevOps, pivot to different story, etc.)
  - Do NOT do status updates (AI already posted those)

**Rule:** If StandupFacilitator-Agent flags zero blockers → skip live standup, keep working

---

### **Human Engineers Update Jira/Linear Throughout Day**

- [ ] **Move stories through workflow:**
  - "To Do" → "In Progress" → "Code Review" → "QA" → "Done"
  - StandupFacilitator-Agent auto-detects state changes, updates tomorrow's standup

- [ ] **AI Agents Also Update Status:**
  - Example: DevAssist-Agent comments on STORY-101: "Generated OAuth callback handler, 120 lines of code, 15 tests, ready for review"

---

## Friday: Sprint Review + Retrospective (1.5 hours)

### **Sprint Review (45 minutes, Friday 2pm)**

- [ ] **Demo Completed Work** (30 minutes)
  - Engineers demo STORY-101 (OAuth login working), STORY-87 (checkout bug fixed)
  - Product Owner accepts/rejects stories (acceptance criteria met?)

- [ ] **Metrics Review** (10 minutes)
  - SprintPlanner-Agent presents:
    - Velocity: 24/25 points (96% completion) ✅
    - Deployment frequency: 5 deploys this sprint (target: >3) ✅
    - Bug rate: 1 bug per 10 stories (target: <2) ✅

- [ ] **Stakeholder Feedback** (5 minutes)
  - Product Owner: "What should we prioritize next sprint?"
  - Team: Any questions from stakeholders?

---

### **Retrospective (45 minutes, Friday 3pm)**

#### **Pre-Retro (AI Analysis — Friday 1pm)**

- [ ] **RetroAnalyzer-Agent generates insights** (automated)

**Example Output:**

> **RetroAnalyzer-Agent — Sprint 15 Retrospective**
>
> **📊 Sprint Metrics:**
> - Velocity: 24/25 points (96%) — **On track** ✅
> - Cycle time: 4.1 days (target: <5 days) — **Improved from 5.2 last sprint** 📈
> - Blocker duration: 12 hours (target: <8h) — **⚠️ Above target**
> - Bug rate: 1 bug/10 stories — **Below target** ✅
>
> **🎯 What Went Well:**
> 1. **Velocity improved +8%** — Team is shipping faster (last 3 sprints: 22 → 26 → 24)
> 2. **Cycle time decreased 21%** — Stories moving faster through pipeline (5.2 days → 4.1 days)
> 3. **DevAssist-Agent contributed 40% of code** — Freed engineers for complex logic
>
> **⚠️ What Didn't Go Well:**
> 1. **STORY-92 blocked 12 hours** — DevOps dependency caused delay (Wed ETA missed, delivered Thurs)
> 2. **3 stories carried over to next sprint** — Scope creep mid-sprint (requirements changed)
>
> **💡 Recommended Actions:**
> 1. **Reduce external dependencies:** Schedule DevOps sync BEFORE sprint planning (not during sprint)
> 2. **Freeze scope mid-sprint:** Product Owner + Tech Lead agree: No requirement changes Tue-Fri
> 3. **Increase DevAssist-Agent autonomy:** Currently generates code but requires heavy review — train on team's style guide to reduce review time
>
> **📈 Trend Analysis (Last 3 Sprints):**
> - Velocity: 22 → 26 → 24 (stable, +9% average)
> - Blocker duration: 18h → 15h → 12h (improving -33%)
> - Bug rate: 3 → 2 → 1 (improving -67%)
>
> **🏆 MVP (Most Valuable Participant):**
> - Human: Engineer 2 (shipped 3 stories, mentored junior, fixed critical bug)
> - AI Agent: DevAssist-Agent (40% code contribution, 0 bugs introduced)

---

#### **Live Retro Discussion (45 minutes)**

- [ ] **Review RetroAnalyzer-Agent Insights** (10 minutes)
  - Team reads AI-generated retro report
  - Discuss: "Do we agree with AI's assessment?"

- [ ] **What Went Well?** (10 minutes)
  - Celebrate wins: Velocity up, cycle time down, bug rate low
  - Recognize humans + AI contributions

- [ ] **What Didn't Go Well?** (15 minutes)
  - Focus on: External dependencies (DevOps delay), scope creep
  - Root cause: Why did STORY-92 get blocked? (DevOps not consulted early enough)

- [ ] **Action Items for Next Sprint** (10 minutes)
  - Action 1: Product Owner schedules DevOps sync before Monday planning
  - Action 2: No requirement changes Tuesday-Friday (freeze scope)
  - Action 3: Tech Lead creates style guide for DevAssist-Agent (reduce review time)
  - **Assign owner + due date for each action**

**Output:** Action items logged in Jira/Linear, tracked next sprint

---

## Sprint-over-Sprint: Continuous Improvement

### **Track Action Items**

- [ ] **Every sprint, review last sprint's action items:**
  - Did we complete them? (Y/N)
  - Did they improve metrics? (e.g., blocker duration decreased after DevOps sync?)

| Sprint | Action Item | Owner | Status | Impact |
|--------|-------------|-------|--------|--------|
| Sprint 14 | Reduce code review time | Tech Lead | ✅ Done | Cycle time -1.2 days |
| Sprint 15 | DevOps sync before planning | Product Owner | ✅ Done | Blocker duration -6h |
| Sprint 15 | Freeze scope mid-sprint | Product Owner | 🔄 In progress | TBD |

---

### **Quarterly Retro (Every 12 Sprints)**

- [ ] **Review long-term trends:**
  - Velocity trend: Are we shipping more over time?
  - Quality trend: Bug rate, deployment frequency improving?
  - Team satisfaction: Survey every quarter (1-5 scale)

- [ ] **Upgrade AI Agents:**
  - If SprintPlanner-Agent accuracy >90% for 3 months → consider upgrading to High-Level Strategic Planner (if available)
  - If DevAssist-Agent generating 60% of code → reduce team size? Or expand scope?

---

## 🛡️ Common Pitfalls

### **Pitfall #1: AI Generates Retro, Team Ignores It**
- **Problem:** RetroAnalyzer-Agent creates detailed report, but team doesn't act on insights
- **Solution:** Product Owner owns action items — assign owners, track in backlog, review next sprint

### **Pitfall #2: Standup Becomes Status Theatre Again**
- **Problem:** Team reads StandupFacilitator-Agent report aloud (wastes time)
- **Solution:** Rule — If no blockers flagged, skip live standup. Only meet if AI surfaces issues.

### **Pitfall #3: AI Over-Optimizes for Velocity**
- **Problem:** SprintPlanner-Agent recommends 40 points, team burns out
- **Solution:** Human Product Owner sets sustainable pace — AI recommends, human decides

### **Pitfall #4: No Human Accountability**
- **Problem:** "AI said to do X, so we did it" (humans defer all decisions to AI)
- **Solution:** AI agents are Assistants/Coordinators (Low/Intermediate-Level) — High-Level humans (Product Owner, Tech Lead) make final calls

---

## 📊 Success Metrics (After 6 Sprints)

| Category | Metric | Baseline | Target | Actual (Sprint 6) |
|----------|--------|----------|--------|-------------------|
| **Efficiency** | Sprint planning time | 2-4 hours | <1 hour | ___ |
| **Efficiency** | Daily standup time | 30 min | <15 min (or skip if no blockers) | ___ |
| **Velocity** | Story points per sprint | ___ | +20% (vs. baseline) | ___ |
| **Quality** | Bug rate | ___ bugs/sprint | <2 bugs/10 stories | ___ |
| **Speed** | Cycle time | ___ days | <5 days | ___ |
| **Blocker Resolution** | Blocker duration | ___ hours/sprint | <8 hours | ___ |
| **Team Satisfaction** | Retro satisfaction survey | ___/5 | >4/5 | ___ |

---

## 📚 Resources

**Documentation:**
- [AI-Native Agile](../DOCS/11-ai-native-agile.md)
- [AI Agents](../DOCS/05-ai-agents.md)
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)

**Templates:**
- [AI-Native Sprint Template](../ADOPTION/TEMPLATES/ai-native-sprint-template.md)
- [Agent Definition Template](../ADOPTION/TEMPLATES/agent-definition-template.yaml)

**Prompts:**
- [Sprint Planning Prompt](../ADOPTION/PROMPT-TEMPLATES/ai-native-sprint-planning.md)

**Playbooks:**
- [Startup AI-Native Playbook — Operating Rhythm](../PLAYBOOKS/by-stage/startup-ai-native.md#establish-weekly-operating-rhythm)
- [SME Transformation — Agile Adoption](../PLAYBOOKS/by-stage/sme-transformation.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
