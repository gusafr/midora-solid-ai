# AI-Native Kanban Implementation Playbook

**For:** Teams adopting continuous flow methodology with AI optimization

**Timeline:** 8 weeks (basic setup → AI agent deployment → optimization)

**Outcome:** 15-25% throughput increase, 10-20% cycle time reduction, real-time bottleneck detection

---

## Who Should Use This Playbook?

### ✅ Good Fit for Kanban

- **Support/operations teams** (unpredictable work arrival)
- **Maintenance teams** (mix of planned + unplanned work)
- **Platform/infrastructure teams** (reactive work like deploy requests, incident response)
- **Early-stage startups** (priorities change weekly, sprints feel too rigid)
- **Continuous delivery teams** (ship multiple times per day)

### ⚠️ Consider Scrum Instead

- **New product development** with predictable scope (use Scrum for time-boxed iterations)
- **Teams requiring strict sprint commitments** (regulatory compliance, contract deliverables)
- **Teams new to Agile** (Scrum's structure easier to learn first)

### 🎯 Hybrid (Scrumban)

- **Product teams with support duties** (planned features + urgent bugs)
- **Teams transitioning from Scrum to Kanban** (gradual change)

**See:** [AI-Native Agile (Scrum)](../../DOCS/11-ai-native-agile.md) for sprint-based approach

---

## Overview: 8-Week Implementation

| Week | Phase | Focus | Key Deliverable |
|------|-------|-------|-----------------|
| 1-2 | **Foundation** | Design board, define policies, train team | Basic Kanban board operational |
| 3-4 | **AI Deployment** | Deploy FlowAnalyzer + BottleneckDetector agents | Daily AI-powered flow reports |
| 5-6 | **Optimization** | Deploy KanbanOptimizer, adjust WIP limits | First round of optimizations |
| 7-8 | **Refinement** | Measure improvements, iterate on policies | Sustainable continuous flow |

**Expected Outcomes:**
- Throughput: +15-25% (e.g., 10 items/week → 12-13 items/week)
- Cycle time: -10-20% (e.g., 5 days → 4-4.5 days)
- Bottleneck detection: Real-time alerts (vs. discovering in retrospectives)
- Team satisfaction: Improved (less manual tracking, more time for meaningful work)

---

## Week 1-2: Foundation — Basic Kanban Setup

### Goal: Operational Kanban board with clear policies

### Step 1: Design Your Kanban Board (2 hours)

**Choose Column Structure:**

**Option A: Simple Flow (3-5 person team, single-function)**

```
┌──────────┬──────────┬──────────┬──────────┐
│ Backlog  │   Todo   │  Doing   │   Done   │
│ (No WIP) │ WIP: 5   │ WIP: 3   │ (No WIP) │
└──────────┴──────────┴──────────┴──────────┘
```

**Option B: Standard Software Team (5-10 people, Dev + QA)**

```
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Backlog  │  Ready   │   Dev    │   QA     │ Deploy   │   Done   │
│ (No WIP) │ WIP: 5   │ WIP: 3   │ WIP: 2   │ WIP: 1   │ (No WIP) │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

**Option C: Complex Flow (10+ people, multiple review stages)**

```
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Backlog  │  Ready   │Dev:Coding│Dev:Review│   QA     │Staging   │ Deploy   │   Done   │
│ (No WIP) │ WIP: 8   │ WIP: 4   │ WIP: 3   │ WIP: 3   │ WIP: 2   │ WIP: 1   │ (No WIP) │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

**Decision Criteria:**

- **Simple Flow:** Use if team <5 people OR work is simple (no review/QA stages)
- **Standard:** Use if team 5-10 people with Dev + QA separation
- **Complex:** Use if team >10 people OR work has multiple handoffs (design → dev → review → QA → deploy)

**Recommended Starting Point:** Option B (Standard Software Team)

---

### Step 2: Set WIP Limits (1 hour)

**Formula for WIP Limits:**

```
WIP Limit per Column = (Team Size × 0.5) + 1

Example: 6-person team → WIP limit = (6 × 0.5) + 1 = 4 items per column
```

**Why Start Conservative?**

- Easier to increase WIP limits later (if team consistently hitting limits)
- Harder to decrease (team feels restricted after higher limits)
- Low WIP forces focus on finishing work vs. starting new work

**Recommended Starting WIP Limits (Standard Board):**

| Column | WIP Limit | Rationale |
|--------|-----------|-----------|
| Backlog | None | Future work, not started |
| Ready | 5 | ~1 week of work buffered |
| Dev | 3 | ~1 item per 2 developers (allows pairing) |
| QA | 2 | Typically 1 QA person, allows 1 in progress + 1 waiting |
| Deploy | 1 | Only 1 deployment at a time (reduces risk) |
| Done | None | Completed work, unlimited |

---

### Step 3: Define Policies (2 hours)

**Definition of Ready (What must be true before item enters "Ready"?):**

- [ ] Requirements clearly documented (user story, acceptance criteria)
- [ ] Designs approved (if applicable — UI mockups, API contracts, architecture diagrams)
- [ ] Dependencies resolved (no blockers from external teams)
- [ ] Estimated (story points or t-shirt sizing)
- [ ] Prioritized by Product Owner

**Definition of Done (What must be true before item moves to "Done"?):**

- [ ] Code implemented and committed to version control
- [ ] Code reviewed by peer (at least 1 approval)
- [ ] Automated tests written and passing (unit + integration)
- [ ] Deployed to production (or staging if deployment is separate step)
- [ ] Product Owner accepted (meets acceptance criteria)
- [ ] Documentation updated (if public API or user-facing feature)

**Blocked Item Policy:**

- [ ] Mark item with "🚫 Blocked" label
- [ ] Add comment: What's the blocker? Who can unblock? ETA?
- [ ] Move to "Blocked" swim lane (optional — some boards add a horizontal "Blocked" section)
- [ ] Daily check-in: Scrum Master follows up on blocked items

**Expedite Policy (Urgent work like P0 bugs):**

- [ ] Mark item with "🔥 Expedite" label
- [ ] Expedite items bypass WIP limits (can exceed limit temporarily)
- [ ] Team prioritizes expedite items above all other work
- [ ] Limit: Max 1 expedite item at a time (prevents everything becoming "urgent")

---

### Step 4: Populate Backlog (1 hour)

**Add 20-30 items to Backlog:**

- Mix of features, bugs, tech debt, improvements
- Ensure each item has clear title, description, acceptance criteria
- Prioritize top 10 items (Product Owner)

**Example Backlog Items:**

| ID | Title | Type | Priority | Story Points | Status |
|----|-------|------|----------|--------------|--------|
| ITEM-101 | Add OAuth login (Google) | Feature | High | 8 | Backlog |
| ITEM-102 | Fix checkout bug (payment failing) | Bug | High | 3 | Backlog |
| ITEM-103 | Export data to CSV | Feature | Medium | 5 | Backlog |
| ITEM-104 | Refactor authentication logic | Tech Debt | Low | 8 | Backlog |
| ITEM-105 | Add notification preferences | Feature | Medium | 5 | Backlog |

---

### Step 5: Team Training (2 hours)

**Kanban Principles Workshop (1 hour):**

- **Principle 1: Visualize Work** — Show team the board, explain columns
- **Principle 2: Limit WIP** — Explain why WIP limits matter (focus, flow, bottleneck prevention)
- **Principle 3: Manage Flow** — Goal is to move items smoothly through board (not start as much work as possible)
- **Principle 4: Make Policies Explicit** — Review Definition of Ready, Definition of Done
- **Principle 5: Feedback Loops** — Weekly retrospectives to improve
- **Principle 6: Improve Collaboratively** — Team owns board design, can change it

**Board Walkthrough (30 minutes):**

- Pull 5 items from Backlog → Ready
- Team pulls 1 item from Ready → Dev (whoever has capacity)
- Simulate item moving through Dev → QA → Deploy → Done
- Practice: What happens when WIP limit hit? (Cannot pull new work until something completes)

**Q&A (30 minutes):**

- Answer team questions
- Common questions:
  - "What if I have capacity but WIP limit is hit?" → Help teammates finish work vs. starting new work
  - "What if urgent bug comes in?" → Use Expedite policy (bypass WIP limit temporarily)
  - "How do we decide what to work on next?" → Pull from top of Ready column (Product Owner prioritizes)

---

### Step 6: Run 1-Week Trial (Manual, No AI Yet)

**Daily Routine (Week 1):**

- **9am Daily Standup (15 min):**
  - Each person: What am I working on? Any blockers?
  - Team: Check WIP limits (any columns over limit?)
  - Scrum Master: Follow up on blocked items

- **Throughout Day:**
  - Move items through board (update status in Jira/Linear)
  - Add comments when item blocked or needs help

- **Friday Retrospective (30 min):**
  - What went well? (e.g., "We shipped 8 items this week!")
  - What didn't go well? (e.g., "QA was bottleneck 3 days — items piled up")
  - What to change next week? (e.g., "Increase QA WIP limit from 2→3?")

**Measure Baseline Metrics (Week 1 End):**

| Metric | Week 1 Result | Notes |
|--------|---------------|-------|
| Throughput | ___ items completed | Example: 8 items |
| Average Cycle Time | ___ days | Example: 5.2 days |
| WIP (avg items in flow) | ___ items | Example: 7 items |
| Bottleneck column | ___ | Example: QA (items aged 4+ days) |

**Save these metrics as baseline for AI optimization later**

---

## Week 3-4: AI Deployment — FlowAnalyzer + BottleneckDetector

### Goal: AI agents monitoring flow, alerting on bottlenecks

### Step 1: Deploy FlowAnalyzer-Agent (4 hours)

**Pre-requisites:**

- [ ] Jira or Linear API access (read-only, for board state)
- [ ] Slack workspace (for posting daily reports)
- [ ] AI provider account (ChatGPT API, Claude API, or self-hosted LLM)

**Agent Configuration:**

```yaml
agent:
  name: FlowAnalyzer-Agent
  level: Intermediate (Analyst)
  
  inputs:
    - source: Jira API
      endpoint: /rest/agile/1.0/board/{boardId}/issue
      fields: [id, summary, status, created, updated, story_points]
  
  schedule:
    daily_report: Every day at 9am
    weekly_summary: Every Friday at 5pm
  
  outputs:
    - destination: Slack #kanban-flow channel
      format: Markdown
  
  thresholds:
    aging_item_alert: Item age > 1.5x average for column
    cycle_time_target: 5 days
    wip_target: 10 items
```

**Implementation Options:**

**Option A: Low-Code (Zapier/Make.com) — $50-100/month**

1. Create Zap: "Every day at 9am"
2. Step 1: Fetch board data (Jira API)
3. Step 2: Send to ChatGPT API (prompt: "Analyze this Kanban data, generate flow report")
4. Step 3: Post to Slack #kanban-flow

**Option B: Custom Script (Python) — $20-50/month (AI API costs only)**

```python
# flow_analyzer.py (simplified example)
import requests
from openai import OpenAI

def fetch_board_data():
    response = requests.get(
        f"{JIRA_URL}/rest/agile/1.0/board/{BOARD_ID}/issue",
        auth=(JIRA_EMAIL, JIRA_API_TOKEN)
    )
    return response.json()

def analyze_flow(board_data):
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = f"""
    Analyze this Kanban board data and generate a daily flow report:
    {board_data}
    
    Include:
    - Total items in flow
    - Average cycle time
    - Aging items (>1.5x average age for column)
    - Throughput this week
    - Trend vs. last week
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def post_to_slack(report):
    requests.post(
        SLACK_WEBHOOK_URL,
        json={"text": report}
    )

if __name__ == "__main__":
    board_data = fetch_board_data()
    report = analyze_flow(board_data)
    post_to_slack(report)
```

**Deploy:** Run as cron job (every day at 9am) on AWS Lambda, Google Cloud Functions, or local server

---

**Example Output (Daily Flow Report):**

```
🤖 FlowAnalyzer-Agent — Daily Flow Report (Nov 6, 2025)

📊 Current Flow Metrics:
- Total items in flow: 9 items (within WIP target of 10 ✅)
- Average cycle time: 4.8 days (target: <5 days ✅)
- Throughput this week: 11 items completed (up from 8 last week 📈 +38%)

⚠️ Aging Items (Need Attention):
- [ITEM-112] in QA for 6 days (expected 3 days) — ⚠️ Bottleneck
  - Assignee: @QA-Engineer
  - Prediction: Will complete in 1 more day (7 days total)
  - Recommendation: Escalate to QA Lead if not done by EOD

✅ On-Track Items:
- [ITEM-115] in Dev for 2 days (expected 3 days) — On track
- [ITEM-118] in Ready for 1 day (expected <5 days) — On track

📈 Trend Analysis:
- Throughput: +38% vs. last week (8 → 11 items)
- Cycle time: Stable (4.9 days last week → 4.8 days this week)
- Bottleneck column: QA (40% of items aged >3 days in QA)

💡 Recommendation: Monitor QA column closely — may need WIP limit increase if bottleneck persists
```

---

### Step 2: Deploy BottleneckDetector-Agent (4 hours)

**Agent Configuration:**

```yaml
agent:
  name: BottleneckDetector-Agent
  level: Intermediate (Coordinator)
  
  monitoring:
    frequency: Every 1 hour (check WIP limits, bottlenecks)
  
  alerts:
    - condition: Column WIP exceeds limit
      action: Post to Slack (immediate alert)
    - condition: Column avg age > 2x target
      action: Post to Slack (bottleneck alert)
    - condition: Bottleneck persists >3 days
      action: Escalate to Team Lead (DM in Slack)
  
  recommendations:
    enable: true (AI suggests solutions to bottlenecks)
```

**Implementation:** Similar to FlowAnalyzer (Zapier or Python script)

**Example Output (Bottleneck Alert):**

```
⚠️ BottleneckDetector-Agent — Bottleneck Alert (Nov 6, 2025)

🚨 BOTTLENECK DETECTED
- Column: QA
- Current WIP: 3/2 (150% of limit — over by 1 item)
- Average age: 5.8 days (target: 3 days, 193% over)
- Severity: 4/5 (High — intervention needed within 24 hours)

📊 Root Cause:
- QA throughput: 2 items/week (down from 4 items/week last month)
- Dev throughput: 5 items/week (stable)
- Gap: Dev shipping 2.5x faster than QA can test → pileup

💡 Recommended Solutions:
1. **Increase QA WIP limit from 2→3** (allows parallel testing)
   - Impact: +50% QA capacity
   - Effort: 5 minutes (update board)
   
2. **Automate regression tests** (reduce manual QA time)
   - Impact: +30% QA throughput
   - Effort: 2 weeks to implement
   
3. **Hire QA contractor (part-time)**
   - Impact: +100% QA throughput
   - Effort: 2 weeks to hire, $3K/month

🎯 Recommended Action: Implement Solution 1 TODAY (increase WIP limit), evaluate if bottleneck persists after 3 days

📅 Escalation: If bottleneck not resolved in 3 days, auto-escalating to @TeamLead
```

---

### Step 3: Team Adoption (Week 3-4)

**Daily Routine (Now AI-Powered):**

- **9am: Review AI Report (10 min):**
  - Team reads FlowAnalyzer daily report in Slack
  - Focus on: Aging items, bottlenecks (not status updates — AI already provided)
  - Action: Address blockers flagged by AI

- **Live Standup (Optional, only if blockers):**
  - If FlowAnalyzer flags 0 blockers → skip standup, keep working
  - If blockers flagged → 10-minute discussion to unblock

- **Throughout Day:**
  - Continue moving items through board
  - BottleneckDetector monitors in background (alerts if WIP limit breached)

- **Friday Retrospective (30 min):**
  - Review AI's weekly summary
  - Discuss: Did AI recommendations make sense? Did we act on them?
  - Decide: Any board changes needed? (WIP limits, column structure, policies)

**Measure Improvement (Week 4 End vs. Week 1 Baseline):**

| Metric | Week 1 (Baseline) | Week 4 (AI-Powered) | Change |
|--------|-------------------|---------------------|--------|
| Throughput | 8 items/week | ___ items/week | ___% |
| Avg Cycle Time | 5.2 days | ___ days | ___% |
| Bottleneck Detection Time | 3-5 days (found in retro) | Real-time (<1 hour) | 95% faster |
| Team Meeting Time | 90 min/week (standup + retro) | ___ min/week | ___% |

**Expected:** Throughput +10-15%, cycle time -10-15%, bottleneck detection 95% faster

---

## Week 5-6: Optimization — KanbanOptimizer Deployment

### Goal: AI-driven board optimization, WIP limit tuning

### Step 1: Deploy KanbanOptimizer-Agent (4 hours)

**Agent Configuration:**

```yaml
agent:
  name: KanbanOptimizer-Agent
  level: High (Specialist)
  
  analysis_period: Last 30 days
  
  capabilities:
    - Recommend WIP limit adjustments (based on throughput, bottleneck data)
    - Suggest column redesigns (if handoffs causing delays)
    - Identify policy gaps (if rework rate high)
  
  schedule:
    monthly_report: First Friday of each month
  
  outputs:
    - destination: Slack #kanban-optimization
      format: Detailed Markdown report with recommendations
```

**Implementation:** Python script (more complex than FlowAnalyzer — needs historical data analysis)

---

### Step 2: Review First Optimization Report (1 hour team meeting)

**Example Monthly Report (Generated by KanbanOptimizer-Agent):**

```
💡 KanbanOptimizer-Agent — Monthly Optimization Report (November 2025)

📊 System Performance (Last 30 Days):
- Throughput: 48 items/month (avg 12 items/week)
- Cycle time: 4.6 days (target: <5 days ✅)
- WIP limit adherence: 92% (8% of time over limit)
- Bottleneck frequency: QA bottlenecked 35% of days

📈 Trends (Last 3 Months):
- Throughput: 40 → 44 → 48 items/month (+20% improvement)
- Cycle time: 5.8 → 5.1 → 4.6 days (-21% improvement)
- Bottleneck: Was Dev (Sept) → now QA (Nov)

---

🎯 Recommended Optimizations:

**1. Increase QA WIP Limit from 2→3** ⭐ HIGH IMPACT
- Rationale: QA bottlenecked 35% of November (10 days) — capacity insufficient
- Impact: +33% QA throughput (allows parallel testing)
- Risk: May increase context switching for QA engineer
- **Vote:** Implement? (Team decides in retrospective)

**2. Split "Dev" Column into "Dev: Coding" + "Dev: Code Review"** ⭐ MEDIUM IMPACT
- Rationale: 30% of Dev cycle time spent in code review (invisible on current board)
- Impact: Better visibility into code review delays → faster interventions
- Effort: 1 hour to restructure board
- **Vote:** Implement? (Team decides)

**3. Add "Definition of Ready" Policy for Dev Column** ⭐ HIGH IMPACT
- Rationale: 20% of items returned from Dev to Ready due to incomplete requirements
- Proposed policy: "Item cannot enter Dev unless acceptance criteria documented + designs approved"
- Impact: -20% rework rate, -10% cycle time
- **Vote:** Implement? (Product Owner approves)

**4. Automate Regression Tests** ⭐ HIGH IMPACT (Long-term)
- Rationale: QA spends 60% of time on manual regression testing
- Impact: -60% manual QA time → +60% capacity for new feature testing
- Effort: 2-3 weeks to implement (Engineer time)
- **Vote:** Prioritize in backlog? (Product Owner decides)

---

📅 Implementation Plan (if all approved):
- **Week 1 (Nov 4-8):** Implement Optimization 1 (QA WIP limit) + Optimization 3 (Definition of Ready)
- **Week 2 (Nov 11-15):** Monitor impact, measure QA throughput
- **Week 3 (Nov 18-22):** Implement Optimization 2 (split Dev column) in retrospective
- **Week 4 (Nov 25-29):** Start Optimization 4 (automate regression tests)

🎯 Expected Outcome (After 4 weeks):
- Throughput: 48 → 56 items/month (+17%)
- Cycle time: 4.6 → 4.0 days (-13%)
- Bottleneck frequency: 35% → <10% of days
```

---

### Step 3: Implement Optimizations (Week 5-6)

**Team Retrospective (Friday Week 5, 1 hour):**

- [ ] Review KanbanOptimizer report
- [ ] Vote on each recommendation:
  - ✅ Approve: Implement immediately
  - ⏸️ Defer: Good idea, but not now (prioritize later)
  - ❌ Reject: Not applicable to our team

**Example Voting:**

| Optimization | Vote | Action |
|--------------|------|--------|
| Increase QA WIP 2→3 | ✅ Approve (5/5 votes) | Implement Monday Week 6 |
| Split Dev column | ✅ Approve (4/5 votes, 1 abstain) | Implement Monday Week 6 |
| Add Definition of Ready | ✅ Approve (5/5 votes) | Product Owner updates policy |
| Automate regression tests | ⏸️ Defer (3/5 votes) | Add to backlog, prioritize next month |

**Implement Changes (Week 6):**

- [ ] Update board structure (WIP limits, columns)
- [ ] Update policies (Definition of Ready, Definition of Done)
- [ ] Communicate changes to team (Slack announcement + standup discussion)
- [ ] Monitor for 2 weeks, measure impact

---

## Week 7-8: Refinement — Measure & Iterate

### Goal: Validate optimizations, establish sustainable rhythm

### Step 1: Measure Optimization Impact (Week 8 End)

**Compare Week 8 vs. Week 1 (Baseline):**

| Metric | Week 1 (Baseline) | Week 8 (Optimized) | Change | Status |
|--------|-------------------|--------------------|---------| -------|
| Throughput | 8 items/week | ___ items/week | ___% | ✅ Target: +15% |
| Avg Cycle Time | 5.2 days | ___ days | ___% | ✅ Target: -15% |
| Bottleneck Detection | 3-5 days (manual) | <1 hour (AI) | 95% faster | ✅ |
| WIP Limit Adherence | ___% | ___% | ___% | ✅ Target: >90% |
| Rework Rate | ___% | ___% | ___% | ✅ Target: <10% |

**Expected Results:**

- ✅ Throughput: +15-25% (e.g., 8 → 10-11 items/week)
- ✅ Cycle time: -10-20% (e.g., 5.2 → 4.2-4.7 days)
- ✅ Bottleneck detection: Real-time (vs. 3-5 days manual)

---

### Step 2: Team Retrospective (Week 8, 1 hour)

**Discussion Questions:**

1. **What's working well with AI-Native Kanban?**
   - Example answers: "AI alerts saved us 2 days on bottleneck detection", "Daily reports reduce standup time 50%"

2. **What's not working?**
   - Example answers: "AI over-alerts (too many notifications)", "Predictions sometimes inaccurate"

3. **How to improve AI agents?**
   - Example actions: "Tune FlowAnalyzer thresholds (reduce alerts)", "Train KanbanOptimizer on our team's data (improve accuracy)"

4. **Next optimizations?**
   - Example: "Automate regression tests (from deferred list)", "Add DeploymentOptimizer-Agent to speed up deploy column"

---

### Step 3: Establish Sustainable Rhythm (Ongoing)

**Daily:**
- [ ] 9am: AI posts FlowAnalyzer daily report
- [ ] Team reviews report (5-10 minutes)
- [ ] Address blockers/aging items

**Weekly:**
- [ ] Friday: FlowAnalyzer posts weekly summary
- [ ] (Optional) Friday retrospective (30 min every 2 weeks)

**Monthly:**
- [ ] First Friday: KanbanOptimizer posts monthly optimization report
- [ ] Team retrospective: Vote on optimizations, implement approved changes

**Quarterly:**
- [ ] Review long-term trends (throughput, cycle time, team satisfaction)
- [ ] Upgrade AI agents (if accuracy >90% → consider High-Level agents)
- [ ] Adjust board structure (if team grows/shrinks or work changes)

---

## Success Criteria

### ✅ Week 8 Success Indicators

- [ ] Throughput increased 15-25% (vs. Week 1 baseline)
- [ ] Cycle time decreased 10-20% (vs. Week 1 baseline)
- [ ] Bottleneck detection is real-time (<1 hour vs. 3-5 days)
- [ ] Team satisfaction improved (survey: 4+/5 rating)
- [ ] AI agents operating autonomously (minimal manual intervention)
- [ ] WIP limit adherence >90% (team respects limits)
- [ ] Rework rate <10% (Definition of Ready/Done effective)

### ⚠️ Yellow Flags (Need Attention)

- [ ] Throughput increased <10% (optimizations not effective)
- [ ] Cycle time unchanged or increased (process issues)
- [ ] Team ignoring AI alerts (alert fatigue)
- [ ] WIP limit adherence <80% (limits set wrong or team not bought in)

### 🚨 Red Flags (Intervention Needed)

- [ ] Throughput decreased (AI agents adding overhead, not value)
- [ ] Cycle time increased >10% (board design wrong for team)
- [ ] Team actively disabling AI agents (not seeing value)
- [ ] Bottlenecks persisting >5 days despite AI alerts (structural issues)

**If Red Flags → Escalate to Tech Lead + Product Owner for root cause analysis**

---

## Common Pitfalls & Solutions

### Pitfall #1: Team Ignores AI Alerts (Alert Fatigue)

**Problem:** FlowAnalyzer posts daily reports, but team stops reading after Week 2

**Solutions:**

- [ ] Reduce alert frequency (daily → 3x/week)
- [ ] Tune thresholds (only alert on high-severity issues)
- [ ] Change format (move from Slack to dashboard, check on-demand)
- [ ] Add human review (Scrum Master highlights top 2-3 insights in standup)

---

### Pitfall #2: AI Recommendations Not Implemented

**Problem:** KanbanOptimizer suggests WIP limit changes, but team votes "defer" every month

**Solutions:**

- [ ] Make recommendations more actionable (provide step-by-step implementation)
- [ ] Start small (trial 1 optimization for 2 weeks, measure impact)
- [ ] Get Product Owner buy-in (if team lacks decision authority)
- [ ] Review in retrospective: Why are we deferring? (lack of time? fear of change?)

---

### Pitfall #3: WIP Limits Constantly Breached

**Problem:** Team pulls new work even when column at WIP limit

**Solutions:**

- [ ] Automated enforcement (BottleneckDetector blocks new work if WIP limit hit)
- [ ] Visualize WIP limits clearly (highlight red when over limit)
- [ ] Retrospective discussion: Why are we breaching? (WIP limits too low? Team not respecting limits?)
- [ ] Adjust WIP limits if team consistently at capacity (e.g., increase Dev WIP 3→4)

---

### Pitfall #4: Bottlenecks Persist Despite AI Alerts

**Problem:** BottleneckDetector flags QA bottleneck for 3 weeks, but nothing changes

**Solutions:**

- [ ] Escalation policy: If bottleneck >5 days → auto-escalate to Team Lead
- [ ] Action required: Product Owner must approve one of AI's recommendations (increase WIP, hire, automate)
- [ ] Root cause analysis: Is bottleneck structural? (e.g., QA capacity 50% of Dev → need to hire)

---

## Next Steps After Week 8

### Option 1: Scale AI-Native Kanban (Team Growing)

**If team grows from 5→10 people:**

- [ ] Add more specialized AI agents:
  - DeploymentOptimizer-Agent (optimize deploy frequency, reduce deploy time)
  - CodeReviewOptimizer-Agent (reduce code review cycle time)
  - CustomerSupportPrioritizer-Agent (auto-triage support tickets)

- [ ] Split board into swim lanes (by team, product area, or priority)

---

### Option 2: Adopt Hybrid Scrumban (Need Sprint Commitments)

**If stakeholders require predictable delivery (e.g., quarterly roadmap):**

- [ ] Add 2-week sprint rhythm (sprint planning + retrospective)
- [ ] Keep Kanban board (continuous flow within sprint)
- [ ] Deploy SprintPlanner-Agent (from AI-Native Scrum playbook)

**See:** [Scrumban Implementation Guide](scrumban.md)

---

### Option 3: Expand to Multiple Teams (Scaled Kanban)

**If organization has 3+ teams using Kanban:**

- [ ] Add portfolio-level Kanban board (track epics across teams)
- [ ] Deploy PortfolioOptimizer-Agent (identify cross-team dependencies, optimize resource allocation)
- [ ] Standardize metrics (all teams report throughput, cycle time, bottlenecks)

**See:** [Scaled AI-Native Kanban](scaled-ai-native-kanban.md) (future playbook)

---

## Resources

**Framework Documentation:**
- [AI-Native Kanban](../../DOCS/12-ai-native-kanban.md) — Conceptual overview
- [AI-Native Agile (Scrum)](../../DOCS/11-ai-native-agile.md) — Sprint-based alternative
- [AI Agents](../../DOCS/05-ai-agents.md) — Agent architecture

**Templates:**
- [Kanban Board Template](../../ADOPTION/TEMPLATES/kanban-board-template.md) — Jira/Linear setup
- [Agent Definition Template](../../ADOPTION/TEMPLATES/agent-definition-template.yaml) — Configure AI agents
- [Kanban Metrics Dashboard](../../ADOPTION/TEMPLATES/kanban-metrics-dashboard.md) — Track cycle time, throughput

**Checklists:**
- [Kanban Setup Checklist](../../ADOPTION/CHECKLISTS/kanban-setup.md) — Step-by-step implementation
- [AI Agent Integration](../../ADOPTION/CHECKLISTS/ai-agent-integration.md) — Deploy FlowAnalyzer, BottleneckDetector

**Other Playbooks:**
- [Scrumban Implementation](scrumban.md) — Hybrid Scrum + Kanban
- [Startup AI-Native (Kanban)](../by-stage/startup-ai-native-kanban.md) — Kanban for early-stage startups

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
