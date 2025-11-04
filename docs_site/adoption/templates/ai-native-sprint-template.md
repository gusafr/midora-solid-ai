# AI-Native Sprint Template

**Sprint Number:** ___  
**Sprint Dates:** Monday {DATE} → Friday {DATE}  
**Team:** ___________  
**Product Owner:** ___________  
**Tech Lead:** ___________  

---

## Sprint Goal

**What must ship for this sprint to be successful?**

{1-2 sentence sprint goal}

Example: "Ship OAuth login (Google + GitHub) + fix critical checkout bug to unblock enterprise customers."

---

## Team Composition (Humans + AI Agents)

| Role | Name | Level | Availability | Focus This Sprint |
|------|------|-------|--------------|-------------------|
| **Product Owner** | {Name} | High-Level | 100% (40 hours) | Define priorities, accept stories |
| **Tech Lead** | {Name} | High-Level | 100% (40 hours) | Architecture, code review, unblock team |
| **Engineer 1** | {Name} | Intermediate-Level | 100% (40 hours) | Implement features, write tests |
| **Engineer 2** | {Name} | Intermediate-Level | 75% (30 hours, 1 day PTO) | Implement features, write tests |
| **Engineer 3 (AI)** | DevAssist-Agent | Low-Level | 100% (AI agent) | Generate code, write tests, create docs |
| **QA** | {Name or QA-Agent} | Low-Level | 100% | Run tests, log bugs, validate fixes |
| **Sprint Planner (AI)** | SprintPlanner-Agent | Intermediate-Level | Automated (Sunday) | Backlog analysis, recommend priorities |
| **Standup Facilitator (AI)** | StandupFacilitator-Agent | Low-Level | Automated (daily 9am) | Collect updates, surface blockers |
| **Retro Analyzer (AI)** | RetroAnalyzer-Agent | Intermediate-Level | Automated (Friday 1pm) | Analyze metrics, generate insights |

**Total Capacity:** {___} story points (based on last 3 sprints: {___}, {___}, {___})

---

## Pre-Sprint Planning (AI-Generated, Sunday Evening)

### **SprintPlanner-Agent Recommendation**

**Recommended Capacity:** {___} story points

**Top Priorities (Business Value × Readiness):**

1. **[STORY-___] {Title}** ({___} points) — ✅/⚠️/🔗
   - Why top priority: {Rationale}
   - Readiness: {Requirements clear? Designs approved? Dependencies resolved?}

2. **[STORY-___] {Title}** ({___} points) — ✅/⚠️/🔗
   - Why: {Rationale}
   - Readiness: {Status}

3. **[STORY-___] {Title}** ({___} points) — ✅/⚠️/🔗
   - Why: {Rationale}
   - Readiness: {Status}

4. **[STORY-___] {Title}** ({___} points) — ✅/⚠️/🔗
   - Why: {Rationale}
   - Readiness: {Status}

5. **[STORY-___] {Title}** ({___} points) — ✅/⚠️/🔗
   - Why: {Rationale}
   - Readiness: {Status}

**Total:** {___} points

---

**⚠️ Risk Flags:**

- {Risk 1}
  - Example: "STORY-92 depends on DevOps (ETA: Wednesday) — if delayed, de-scope to next sprint"
- {Risk 2}
  - Example: "STORY-105 depends on design approval (ETA: Tuesday) — monitor closely"

---

**📈 Velocity Trend:** {Improving/Stable/Declining}
- Last 3 sprints: {___}, {___}, {___} points ({___}% avg completion)
- Insight: {What's the trend?}

---

**💡 Recommendations:**

1. {Recommendation 1}
   - Example: "Reduce external dependencies — schedule DevOps sync BEFORE sprint planning"
2. {Recommendation 2}
   - Example: "Have backup story ready if STORY-92 delayed (e.g., STORY-120)"
3. {Recommendation 3}
   - Example: "Freeze scope Tuesday-Friday to prevent mid-sprint requirement changes"

---

## Monday: Sprint Planning (1 Hour)

### **Planning Meeting (Monday 9am, 60 minutes)**

**Attendees:** Product Owner, Tech Lead, Engineers, (AI agents don't attend, but provide input via pre-analysis)

**Agenda:**

1. **Review SprintPlanner-Agent Recommendations** (10 minutes)
   - Product Owner: "Do these priorities align with business goals?"
   - Tech Lead: "Are technical risks accurately flagged?"

2. **Refine & Commit** (30 minutes)
   - Discuss each story
   - Adjust estimates if needed (AI's estimate is starting point, team decides)
   - Commit to sprint goal

3. **Assign Work** (15 minutes)
   - Product Owner assigns stories to humans/AI agents
   - Example: STORY-101 (OAuth) → Engineer 1 (human) + DevAssist-Agent (AI generates boilerplate)

4. **Set Success Criteria** (5 minutes)
   - Product Owner: "What must ship for this sprint to be successful?"

---

### **Sprint Backlog (Committed Stories)**

| Story ID | Title | Points | Assigned To | Status | Notes |
|----------|-------|--------|-------------|--------|-------|
| STORY-___ | {Title} | {___} | {Name or Agent} | To Do | {Dependency? Risk?} |
| STORY-___ | {Title} | {___} | {Name or Agent} | To Do | {Dependency? Risk?} |
| STORY-___ | {Title} | {___} | {Name or Agent} | To Do | {Dependency? Risk?} |
| STORY-___ | {Title} | {___} | {Name or Agent} | To Do | {Dependency? Risk?} |
| STORY-___ | {Title} | {___} | {Name or Agent} | To Do | {Dependency? Risk?} |

**Total Committed:** {___} story points

---

## Tuesday-Thursday: Execution + Daily Standup

### **Daily Standup (Async-First, 9am)**

**StandupFacilitator-Agent posts to Slack #standup channel:**

```
**StandupFacilitator-Agent — Sprint {___}, Day {___}**

**✅ Progress:**
- [STORY-___] {Title}: {___}% complete ({Owner} shipped {What?})
- [STORY-___] {Title}: {Status}

**🚧 Blockers:**
- [STORY-___] {Title}: {Blocker description} — **⚠️ At risk**

**📊 Metrics:**
- Velocity: {___}/{___} points complete ({___}% of sprint, on track ✅/⚠️)
- Cycle time: {___} days (target: <5 days) ✅/⚠️
- WIP: {___} stories in progress (target: <5) ✅/⚠️

**💬 Human Input Needed:**
- @{Name}: {Question or action needed}
- @{Name}: {Question or action needed}
```

**Live Standup (Optional, 15 minutes, 9:15am):**
- Only if blockers flagged by AI
- Focus on: How to unblock? (call external team, pivot to different story, etc.)
- Do NOT do status updates (AI already posted those)

**Rule:** If StandupFacilitator-Agent flags zero blockers → skip live standup

---

### **Work Tracking (Daily)**

| Story ID | Mon | Tue | Wed | Thu | Fri | Status | Notes |
|----------|-----|-----|-----|-----|-----|--------|-------|
| STORY-___ | To Do | In Progress | In Progress | Code Review | Done | ✅ Completed | Shipped Thursday |
| STORY-___ | To Do | To Do | In Progress | In Progress | QA | 🔄 In Progress | QA Friday |
| STORY-___ | To Do | In Progress | Blocked | Blocked | In Progress | ⚠️ At Risk | DevOps delay |

---

## Friday: Sprint Review + Retrospective (1.5 Hours)

### **Sprint Review (45 minutes, Friday 2pm)**

**Attendees:** Product Owner, Tech Lead, Engineers, Stakeholders (optional)

**Agenda:**

1. **Demo Completed Work** (30 minutes)
   - Engineers demo stories marked "Done"
   - Product Owner accepts/rejects (acceptance criteria met?)

2. **Metrics Review** (10 minutes)
   - SprintPlanner-Agent presents:
     - Velocity: {___}/{___} points ({___}% completion)
     - Deployment frequency: {___} deploys this sprint
     - Bug rate: {___} bugs per 10 stories

3. **Stakeholder Feedback** (5 minutes)
   - Product Owner: "What should we prioritize next sprint?"

---

### **Sprint Metrics Summary**

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| **Velocity** | {___} points | {___} points ({___}% completion) | ✅/⚠️ |
| **Cycle Time** | <5 days | {___} days | ✅/⚠️ |
| **Blocker Duration** | <8 hours | {___} hours | ✅/⚠️ |
| **Bug Rate** | <2 bugs/10 stories | {___} | ✅/⚠️ |
| **Deployment Frequency** | >3 deploys | {___} | ✅/⚠️ |

---

### **Retrospective (45 minutes, Friday 3pm)**

**Attendees:** Product Owner, Tech Lead, Engineers (full team)

#### **Pre-Retro (AI Analysis — Friday 1pm)**

**RetroAnalyzer-Agent generates:**

```markdown
**RetroAnalyzer-Agent — Sprint {___} Retrospective**

**📊 Sprint Metrics:**
- Velocity: {___}/{___} points ({___}% completion) — **{On track/Behind/Ahead}** ✅/⚠️
- Cycle time: {___} days (target: <5 days) — **{Improved/Stable/Worse} from last sprint** 📈/📉
- Blocker duration: {___} hours (target: <8h) — **{Above/Below target}** ⚠️/✅
- Bug rate: {___} bugs/10 stories — **{Better/Worse than target}** ✅/⚠️

**🎯 What Went Well:**
1. {Win 1} (example: "Velocity +8% — team shipping faster")
2. {Win 2} (example: "Cycle time decreased 21% — stories moving faster through pipeline")
3. {Win 3} (example: "DevAssist-Agent contributed 40% of code — freed engineers for complex logic")

**⚠️ What Didn't Go Well:**
1. {Challenge 1} (example: "STORY-92 blocked 12 hours — DevOps dependency caused delay")
2. {Challenge 2} (example: "3 stories carried over — scope creep mid-sprint")

**💡 Recommended Actions:**
1. {Action 1} (example: "Schedule DevOps sync BEFORE sprint planning (not during sprint)")
2. {Action 2} (example: "Freeze scope mid-sprint — no requirement changes Tue-Fri")
3. {Action 3} (example: "Increase DevAssist-Agent autonomy — train on team's style guide")

**📈 Trend Analysis (Last 3 Sprints):**
- Velocity: {___} → {___} → {___} ({improving/stable/declining})
- Blocker duration: {___}h → {___}h → {___}h ({improving/worsening})
- Bug rate: {___} → {___} → {___} ({improving/worsening})

**🏆 MVP (Most Valuable Participant):**
- **Human:** {Name} ({Why? e.g., "Shipped 3 stories, mentored junior, fixed critical bug"})
- **AI Agent:** {Agent Name} ({Why? e.g., "40% code contribution, 0 bugs introduced"})
```

---

#### **Live Retro Discussion (45 minutes)**

1. **Review AI Insights** (10 minutes)
   - Team reads RetroAnalyzer-Agent report
   - Discuss: "Do we agree with AI's assessment?"

2. **What Went Well?** (10 minutes)
   - Celebrate wins
   - Recognize humans + AI contributions

3. **What Didn't Go Well?** (15 minutes)
   - Focus on root causes (not blame)
   - Example: "Why did STORY-92 get blocked? → DevOps not consulted early enough"

4. **Action Items for Next Sprint** (10 minutes)
   - Action 1: {___} (example: "Product Owner schedules DevOps sync before Monday planning")
   - Action 2: {___} (example: "No requirement changes Tue-Fri")
   - Action 3: {___} (example: "Tech Lead creates style guide for DevAssist-Agent")
   - **Assign owner + due date for each action**

---

### **Action Items (Track Next Sprint)**

| Action Item | Owner | Due Date | Status |
|-------------|-------|----------|--------|
| {Action 1} | {Name} | Next sprint planning | Not Started / In Progress / Done |
| {Action 2} | {Name} | {Date} | Not Started / In Progress / Done |
| {Action 3} | {Name} | {Date} | Not Started / In Progress / Done |

---

## Sprint Health Check

**Green (Healthy Sprint):**
- ✅ Velocity within 10% of commitment
- ✅ <8 hours total blocker duration
- ✅ <2 bugs per 10 stories shipped
- ✅ Team satisfaction >4/5

**Yellow (Needs Attention):**
- ⚠️ Velocity 10-20% below commitment
- ⚠️ 8-16 hours blocker duration
- ⚠️ 2-4 bugs per 10 stories
- ⚠️ Team satisfaction 3-4/5

**Red (Intervention Needed):**
- 🔴 Velocity >20% below commitment
- 🔴 >16 hours blocker duration
- 🔴 >4 bugs per 10 stories
- 🔴 Team satisfaction <3/5

**This Sprint Status:** {Green/Yellow/Red}

**If Yellow or Red:**
- [ ] Root cause analysis: What caused issues? (scope creep, dependencies, skill gaps, AI agent errors?)
- [ ] Action plan: {What will we change next sprint?}
- [ ] Escalate to leadership if: Blockers structural (e.g., IT won't provide API access, hiring freeze blocks capacity)

---

## Notes & Learnings

**Key Decisions This Sprint:**
- {Decision 1} (example: "Decided to de-scope STORY-92 due to DevOps delay")
- {Decision 2} (example: "Tech Lead approved using new library for OAuth")

**Technical Debt Identified:**
- {Debt 1} (example: "Authentication logic needs refactor — add to backlog")
- {Debt 2} (example: "Test coverage 78% (target: >80%) — prioritize next sprint")

**AI Agent Performance:**

| AI Agent | Tasks Completed | Accuracy | Escalation Rate | Notes |
|----------|-----------------|----------|-----------------|-------|
| DevAssist-Agent | 12 code files generated | 95% (1 bug) | 5% | Excellent — minor bug in error handling |
| StandupFacilitator-Agent | 5 standup reports | 100% | 0% | Accurate blocker flagging |
| SprintPlanner-Agent | 1 sprint plan | 90% | 10% | Over-estimated STORY-105 complexity |

**Improvements for AI Agents:**
- {Improvement 1} (example: "Train DevAssist-Agent on team's error handling patterns")
- {Improvement 2} (example: "Update SprintPlanner-Agent with more accurate complexity heuristics")

---

## Resources

**Documentation:**
- [AI-Native Agile](../DOCS/11-ai-native-agile.md)
- [AI Agents](../DOCS/05-ai-agents.md)
- [Human-AI Collaboration](../DOCS/08-human-ai-collaboration.md)

**Checklists:**
- [AI-Native Sprint Checklist](../ADOPTION/CHECKLISTS/ai-native-sprint.md)

**Prompts:**
- [Sprint Planning Prompt](../ADOPTION/PROMPT-TEMPLATES/ai-native-sprint-planning.md)

**Playbooks:**
- [Startup AI-Native — Operating Rhythm](../PLAYBOOKS/by-stage/startup-ai-native.md)

---

**Sprint:** {___}  
**Version:** 1.0  
**Last Updated:** November 2025  
**Framework:** SOLID.AI
