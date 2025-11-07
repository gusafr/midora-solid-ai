# Kanban Setup Checklist

**For:** Teams implementing AI-Native Kanban from scratch

**Timeline:** 2 weeks (basic setup → team training → first iteration)

**Outcome:** Operational Kanban board with clear policies, WIP limits, and team buy-in

---

## Pre-Setup (1-2 hours)

### **Assess Team Fit**

- [ ] **Team size:** _____ people (Kanban works best for 3-15 people)

- [ ] **Work type:** (Check all that apply)
  - [ ] Unpredictable arrival (support tickets, bugs, ops requests)
  - [ ] Continuous delivery (ship multiple times per day/week)
  - [ ] Mix of planned + unplanned work
  - [ ] Reactive work (infrastructure, platform, incident response)

- [ ] **Is Kanban the right fit?**
  - ✅ Yes → Continue with this checklist
  - ⚠️ Maybe → Consider hybrid Scrumban (Kanban + 2-week sprints)
  - ❌ No → Use AI-Native Scrum instead (time-boxed sprints)

**See:** [AI-Native Agile (Scrum)](../../DOCS/11-ai-native-agile.md) if Kanban isn't the right fit

---

## Week 1: Board Design & Policy Definition

### Day 1: Design Board Structure (2 hours)

- [ ] **Choose board layout:**
  - [ ] Option A: Simple Flow (Backlog → Todo → Doing → Done) — 3-5 person team
  - [ ] Option B: Standard Software Team (Backlog → Ready → Dev → QA → Deploy → Done) — 5-10 people
  - [ ] Option C: Complex Flow (8+ columns) — 10+ people, multiple review stages

**Selected layout:** _______________

**See:** [Kanban Board Template](../../ADOPTION/TEMPLATES/kanban-board-template.md) for full layouts

---

- [ ] **Define columns:**

| Column Name | Purpose | Entrance Criteria | Exit Criteria |
|-------------|---------|-------------------|---------------|
| 1. _________ | _______ | _________________ | _____________ |
| 2. _________ | _______ | _________________ | _____________ |
| 3. _________ | _______ | _________________ | _____________ |
| 4. _________ | _______ | _________________ | _____________ |
| 5. _________ | _______ | _________________ | _____________ |
| 6. _________ | _______ | _________________ | _____________ |

**Example (Standard Software Team):**

| Column | Purpose | Entrance Criteria | Exit Criteria |
|--------|---------|-------------------|---------------|
| Backlog | Future work | Product Owner prioritizes | Meets Definition of Ready |
| Ready | Work ready to start | Requirements clear, designs approved | Developer pulls into Dev |
| Dev | Coding + unit testing | Developer has capacity | Code reviewed + tests passing |
| QA | Testing | All tests passing in Dev | QA approved |
| Deploy | Production deployment | QA approved | Live in production |
| Done | Shipped | Deployed to production | N/A (complete) |

---

### Day 2: Set WIP Limits (1 hour)

- [ ] **Calculate WIP limits using formula:**

```
WIP Limit per Column = (Team Size × 0.5) + 1
```

**Team size:** _____ people  
**Calculated WIP limit:** _____ items per column

---

- [ ] **Set column-specific WIP limits:**

| Column | WIP Limit | Rationale |
|--------|-----------|-----------|
| Backlog | None (unlimited) | Future work, not started |
| _______ | _____ | _________________________________ |
| _______ | _____ | _________________________________ |
| _______ | _____ | _________________________________ |
| _______ | _____ | _________________________________ |
| Done | None (unlimited) | Completed work |

**Example:**

| Column | WIP Limit | Rationale |
|--------|-----------|-----------|
| Ready | 5 | ~1 week of work buffered |
| Dev | 3 | ~1 item per 2 developers (allows pairing) |
| QA | 2 | 1 QA person, allows 1 active + 1 waiting |
| Deploy | 1 | Only 1 deployment at a time (reduces risk) |

**Total WIP Limit:** _____ items (sum of all columns except Backlog + Done)

**Remember:** Start conservative (easier to increase WIP limits later than decrease)

---

### Day 3: Define Policies (2 hours)

#### **Definition of Ready (DoR)**

**What must be true before item enters "Ready" column?**

- [ ] Requirements documented (user story, acceptance criteria)
- [ ] Designs approved (if applicable — UI mockups, API contracts)
- [ ] Dependencies resolved (no blockers from external teams)
- [ ] Estimated (story points or t-shirt sizing)
- [ ] Prioritized by Product Owner
- [ ] Technical feasibility confirmed (no major unknowns)

**Additional criteria (team-specific):**

- [ ] _____________________________________________
- [ ] _____________________________________________
- [ ] _____________________________________________

---

#### **Definition of Done (DoD)**

**What must be true before item moves to "Done" column?**

- [ ] Code implemented and committed to version control
- [ ] Code reviewed by peer (at least 1 approval)
- [ ] Automated tests written and passing (unit + integration)
- [ ] Deployed to production (or staging if deployment is separate)
- [ ] Product Owner accepted (meets acceptance criteria)
- [ ] Documentation updated (if public API or user-facing feature)

**Additional criteria (team-specific):**

- [ ] _____________________________________________
- [ ] _____________________________________________
- [ ] _____________________________________________

---

#### **Blocked Item Policy**

- [ ] **How to mark blocked items:**
  - [ ] Add "🚫 Blocked" label/tag
  - [ ] Add comment: What's the blocker? Who can unblock? ETA?
  - [ ] (Optional) Move to "Blocked" swim lane

- [ ] **Who follows up on blocked items?**
  - [ ] Scrum Master / Team Lead: ___________________ (name)

- [ ] **Escalation rule:**
  - [ ] If blocker not resolved in _____ days → escalate to Product Owner/Tech Lead

---

#### **Expedite Policy (Urgent Work)**

- [ ] **How to mark expedite items:**
  - [ ] Add "🔥 Expedite" label/tag
  - [ ] Expedite items bypass WIP limits (temporarily)

- [ ] **Limit:** Max _____ expedite item(s) in flow at a time (recommend: 1)

- [ ] **Who approves expedite items?**
  - [ ] Product Owner / Tech Lead: ___________________ (name)

---

### Day 4: Create Board in Tool (2 hours)

**Tool choice:**

- [ ] Jira
- [ ] Linear
- [ ] Trello
- [ ] Azure DevOps
- [ ] GitHub Projects
- [ ] Custom tool: _______________

**See:** [Kanban Board Template](../../ADOPTION/TEMPLATES/kanban-board-template.md) for tool-specific setup instructions

---

#### **Board Setup Steps:**

- [ ] Create new board (name: "Team Kanban Board" or team-specific name)

- [ ] Add columns (from Day 1 design)

- [ ] Set WIP limits for each column (from Day 2)

- [ ] Configure card layout:
  - [ ] Show fields: Story points, Assignee, Priority, Labels
  - [ ] Show colors: Priority (High = Red, Medium = Yellow, Low = Blue)

- [ ] (Optional) Add swim lanes:
  - [ ] By Priority (High, Medium, Low)
  - [ ] By Assignee (each person's work)
  - [ ] By Type (Feature, Bug, Tech Debt)

- [ ] Test board:
  - [ ] Create 3 test items
  - [ ] Move items through columns (Backlog → Ready → Dev → Done)
  - [ ] Verify WIP limits enforced (can't exceed limit)

---

### Day 5: Populate Backlog (1 hour)

- [ ] **Add 20-30 items to Backlog:**
  - [ ] Mix of features, bugs, tech debt, improvements
  - [ ] Each item has: Title, Description, Acceptance criteria, Priority

- [ ] **Prioritize top 10 items** (Product Owner ranks in order)

- [ ] **Ensure top 5 items meet Definition of Ready:**
  - [ ] Item 1: ✅/❌ Ready?
  - [ ] Item 2: ✅/❌ Ready?
  - [ ] Item 3: ✅/❌ Ready?
  - [ ] Item 4: ✅/❌ Ready?
  - [ ] Item 5: ✅/❌ Ready?

**If ❌ → add comments on what's missing (requirements? designs? dependency?)**

---

## Week 2: Team Training & First Iteration

### Day 6: Team Training Workshop (2 hours)

#### **Part 1: Kanban Principles (30 min)**

- [ ] **Principle 1: Visualize Work**
  - Show team the board, explain columns
  - Walk through example item flow (Backlog → Done)

- [ ] **Principle 2: Limit WIP**
  - Explain why WIP limits matter (focus, prevent overload, faster flow)
  - Demo: What happens when WIP limit hit? (can't pull new work until something completes)

- [ ] **Principle 3: Manage Flow**
  - Goal: Move items smoothly through board (not start as much work as possible)
  - Metric: Cycle time (days from Ready → Done)

- [ ] **Principle 4: Make Policies Explicit**
  - Review Definition of Ready, Definition of Done
  - Review Blocked/Expedite policies

- [ ] **Principle 5: Feedback Loops**
  - Weekly retrospectives to improve board, policies

- [ ] **Principle 6: Improve Collaboratively**
  - Team owns board design — can change columns, WIP limits, policies

---

#### **Part 2: Hands-On Walkthrough (1 hour)**

- [ ] **Pull items from Backlog → Ready** (top 5 prioritized items)

- [ ] **Simulate item flow:**
  - [ ] Developer pulls item from Ready → Dev
  - [ ] Developer completes coding → moves to QA
  - [ ] QA tests → moves to Deploy
  - [ ] Item deployed → moves to Done

- [ ] **Practice WIP limit enforcement:**
  - [ ] What if Dev column at WIP limit (3/3)?
    - Answer: Can't pull new work from Ready until Dev item completes
    - Action: Help teammate finish Dev work vs. starting new work

- [ ] **Practice blocked item handling:**
  - [ ] Simulate: Item blocked in Dev (waiting on external API team)
  - [ ] Action: Add "🚫 Blocked" label, comment with details, notify Scrum Master

---

#### **Part 3: Q&A (30 min)**

Common questions to address:

- [ ] **Q:** "What if I have capacity but WIP limit is hit?"
  - **A:** Help teammates finish work vs. starting new work (pair programming, code review, testing)

- [ ] **Q:** "What if urgent bug comes in?"
  - **A:** Use Expedite policy (add "🔥 Expedite" label, bypass WIP limit temporarily, limit 1 at a time)

- [ ] **Q:** "How do we decide what to work on next?"
  - **A:** Pull from top of Ready column (Product Owner prioritizes)

- [ ] **Q:** "What if item doesn't meet Definition of Done?"
  - **A:** Cannot move to Done — return to appropriate column (e.g., QA finds bug → return to Dev)

---

### Day 7-10: Run First Iteration (Manual, No AI Yet) — 4 days

#### **Daily Routine:**

- [ ] **9am Daily Standup (15 min):**
  - Each person: What am I working on? Any blockers?
  - Team: Check WIP limits (any columns over limit?)
  - Scrum Master: Follow up on blocked items

- [ ] **Throughout Day:**
  - Move items through board (update status in Jira/Linear)
  - Add comments when item blocked or needs help
  - Respect WIP limits (don't pull new work if column at limit)

- [ ] **End of Day:**
  - Team reviews board (any aging items? bottlenecks?)

---

#### **Track Daily Metrics:**

| Day | Items in Flow (WIP) | Items Completed (Throughput) | Blocked Items | Notes |
|-----|---------------------|------------------------------|---------------|-------|
| Mon | _____ | _____ | _____ | ______________________________ |
| Tue | _____ | _____ | _____ | ______________________________ |
| Wed | _____ | _____ | _____ | ______________________________ |
| Thu | _____ | _____ | _____ | ______________________________ |

**Example:**

| Day | WIP | Throughput | Blocked | Notes |
|-----|-----|------------|---------|-------|
| Mon | 7 | 0 | 0 | First day — team pulling work |
| Tue | 8 | 2 | 0 | 2 items shipped to Done |
| Wed | 7 | 3 | 1 | 1 item blocked (external API delay) |
| Thu | 6 | 4 | 1 | QA bottleneck (items piling up) |

---

### Day 11: First Retrospective (1 hour) — Friday

#### **Retrospective Agenda:**

- [ ] **Review Metrics (15 min):**
  - [ ] Total throughput this week: _____ items completed
  - [ ] Average cycle time: _____ days (Ready → Done)
  - [ ] WIP limit adherence: ___% (% of time within limits)
  - [ ] Bottleneck column: _________ (column with longest avg age)

---

- [ ] **What Went Well? (15 min):**
  - What did the team do well this week?
  - Examples: "We shipped 8 items!", "WIP limits helped us focus", "Blocked item resolved in 1 day"

**Wins to celebrate:**

1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

- [ ] **What Didn't Go Well? (20 min):**
  - What challenges did we face?
  - Examples: "QA was bottleneck 3 days", "2 items blocked for 2+ days", "WIP limit breached twice"

**Challenges to address:**

1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

- [ ] **What to Change Next Week? (10 min):**
  - What actions will improve flow?
  - Examples: "Increase QA WIP limit 2→3", "Add Definition of Ready checklist", "Daily check-in on blocked items"

**Action items:**

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| ______ | _____ | ________ | Not Started / In Progress / Done |
| ______ | _____ | ________ | Not Started / In Progress / Done |
| ______ | _____ | ________ | Not Started / In Progress / Done |

---

### Day 12: Measure Baseline Metrics (End of Week 2)

- [ ] **Calculate baseline metrics** (save as baseline for AI optimization later):

| Metric | Week 2 Result | Calculation Method |
|--------|---------------|--------------------|
| **Throughput** | _____ items/week | Count items completed (moved to Done) |
| **Avg Cycle Time** | _____ days | Sum (Done date - Ready date) ÷ # items |
| **Avg WIP** | _____ items | Count items in flow (Ready+Dev+QA+Deploy) daily, average |
| **Bottleneck Column** | _________ | Column with highest avg age |
| **WIP Limit Adherence** | ____% | (# days within limit ÷ 5 days) × 100 |
| **Rework Rate** | ____% | (# items returned to earlier column ÷ total items) × 100 |

**Example:**

| Metric | Week 2 Result |
|--------|---------------|
| Throughput | 8 items/week |
| Avg Cycle Time | 5.2 days |
| Avg WIP | 7 items |
| Bottleneck Column | QA (avg 4.5 days) |
| WIP Limit Adherence | 90% |
| Rework Rate | 12% |

**Save these metrics** — will compare to Week 4 (after AI deployment) and Week 8 (after optimization)

---

## ✅ Week 2 Completion Checklist

- [ ] Board operational (all team members using it daily)
- [ ] WIP limits enforced (team respects limits)
- [ ] Policies defined and documented (Definition of Ready, Definition of Done)
- [ ] Team trained on Kanban principles
- [ ] First retrospective completed (action items assigned)
- [ ] Baseline metrics measured (throughput, cycle time, WIP, bottleneck)
- [ ] Team satisfaction: ___/5 (survey team: 1-5 scale, how's Kanban working?)

**If any ❌ → address before moving to AI deployment (Week 3-4)**

---

## Next Steps

### **Week 3-4: AI Agent Deployment**

Once basic Kanban operational (Week 2 complete), deploy AI agents:

- [ ] FlowAnalyzer-Agent (daily flow reports, aging item alerts)
- [ ] BottleneckDetector-Agent (real-time bottleneck detection, WIP limit monitoring)

**See:** [AI-Native Kanban Playbook — Week 3-4](../../PLAYBOOKS/implementation/ai-native-kanban.md#week-3-4-ai-deployment--flowanalyzer--bottleneckdetector)

---

### **Week 5-6: Optimization**

Deploy KanbanOptimizer-Agent for WIP limit tuning, column redesign recommendations

**See:** [AI-Native Kanban Playbook — Week 5-6](../../PLAYBOOKS/implementation/ai-native-kanban.md#week-5-6-optimization--kanbanoptimizer-deployment)

---

## Common Pitfalls (Week 1-2)

### **Pitfall #1: Team Ignores WIP Limits**

**Problem:** Team pulls new work even when column at WIP limit

**Solutions:**

- [ ] Visualize WIP limits clearly (highlight red when over limit)
- [ ] Daily standup reminder: "Are we within WIP limits?"
- [ ] Retrospective discussion: Why are we breaching? (WIP limits too low? Team not bought in?)

---

### **Pitfall #2: Definition of Ready Not Enforced**

**Problem:** Items moving to Ready without clear requirements → rework later

**Solutions:**

- [ ] Product Owner reviews every item before moving to Ready
- [ ] Add automation: Jira/Linear rule blocks item if "Requirements" field empty
- [ ] Weekly backlog refinement: Ensure top 10 items meet Definition of Ready

---

### **Pitfall #3: No One Tracks Metrics**

**Problem:** Team doesn't measure throughput, cycle time → can't optimize

**Solutions:**

- [ ] Assign owner: Scrum Master tracks metrics weekly
- [ ] Use tool automation: Jira dashboard, Linear insights, or custom BI
- [ ] Review metrics in retrospective (data-driven discussions)

---

### **Pitfall #4: Board Becomes Stale**

**Problem:** Team stops updating board, items stuck in columns

**Solutions:**

- [ ] Daily standup: "Everyone, update your items before standup"
- [ ] End of day reminder: "Update board status before logging off"
- [ ] Retrospective: Discuss barriers to board updates (tool too slow? unclear how to update?)

---

## Resources

**Framework Documentation:**
- [AI-Native Kanban](../../DOCS/12-ai-native-kanban.md) — Conceptual overview
- [AI Agents](../../DOCS/05-ai-agents.md) — Agent architecture

**Playbooks:**
- [AI-Native Kanban Implementation](../../PLAYBOOKS/implementation/ai-native-kanban.md) — Full 8-week plan

**Templates:**
- [Kanban Board Template](../../ADOPTION/TEMPLATES/kanban-board-template.md) — Jira/Linear/Trello setup
- [Agent Definition Template](../../ADOPTION/TEMPLATES/agent-definition-template.yaml) — Configure AI agents

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
