# Kanban Board Template

**For:** Teams setting up AI-Native Kanban in Jira, Linear, Trello, or custom tools

**Purpose:** Standard board configuration with WIP limits, column definitions, and AI agent integration points

---

## Board Structure Options

### Option A: Simple Flow (3-5 Person Team)

**Use Case:** Small teams, simple workflow, no separate QA/review stages

```
┌──────────┬──────────┬──────────┬──────────┐
│ Backlog  │   Todo   │  Doing   │   Done   │
│          │          │          │          │
│ (No WIP) │ WIP: 5   │ WIP: 3   │ (No WIP) │
└──────────┴──────────┴──────────┴──────────┘
```

**Column Definitions:**

| Column | Purpose | WIP Limit | Avg Time | AI Monitoring |
|--------|---------|-----------|----------|---------------|
| **Backlog** | All future work, not yet started | None | N/A | None (human-curated) |
| **Todo** | Ready to start (requirements clear) | 5 | 1-2 days | FlowAnalyzer (age >3 days → alert) |
| **Doing** | Active work in progress | 3 | 2-4 days | FlowAnalyzer (age >5 days → alert) |
| **Done** | Completed and shipped | None | N/A | FlowAnalyzer (calculate cycle time) |

**Total WIP Limit:** 8 items (Todo + Doing)

---

### Option B: Standard Software Team (5-10 People)

**Use Case:** Dev + QA separation, code review, deployment stage

```
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Backlog  │  Ready   │   Dev    │   QA     │ Deploy   │   Done   │
│          │          │          │          │          │          │
│ (No WIP) │ WIP: 5   │ WIP: 3   │ WIP: 2   │ WIP: 1   │ (No WIP) │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

**Column Definitions:**

| Column | Purpose | WIP Limit | Avg Time | AI Monitoring |
|--------|---------|-----------|----------|---------------|
| **Backlog** | All future work (not started) | None | N/A | None |
| **Ready** | Requirements clear, designs approved, no blockers | 5 | 1-3 days | FlowAnalyzer (age >5 days → deprioritize?) |
| **Dev** | Coding, unit testing, code review | 3 | 2-4 days | FlowAnalyzer (age >5 days → complexity flag?) |
| **QA** | Testing, bug verification | 2 | 1-3 days | BottleneckDetector (age >4 days → bottleneck alert) |
| **Deploy** | Production deployment | 1 | <1 day | FlowAnalyzer (age >2 days → CI/CD issue?) |
| **Done** | Shipped to production | None | N/A | FlowAnalyzer (cycle time calculation) |

**Total WIP Limit:** 11 items (Ready + Dev + QA + Deploy)

---

### Option C: Complex Flow (10+ People, Multiple Review Stages)

**Use Case:** Large teams, architecture review, staging environment, multiple QA stages

```
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Backlog  │  Ready   │Dev:Coding│Dev:Review│   QA     │ Staging  │ Deploy   │   Done   │
│          │          │          │          │          │          │          │          │
│ (No WIP) │ WIP: 8   │ WIP: 4   │ WIP: 3   │ WIP: 3   │ WIP: 2   │ WIP: 1   │ (No WIP) │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

**Column Definitions:**

| Column | Purpose | WIP Limit | Avg Time | AI Monitoring |
|--------|---------|-----------|----------|---------------|
| **Backlog** | Future work | None | N/A | None |
| **Ready** | Fully specified, ready to start | 8 | 1-3 days | FlowAnalyzer (age >5 days) |
| **Dev: Coding** | Active coding, unit tests | 4 | 2-3 days | FlowAnalyzer (age >4 days) |
| **Dev: Review** | Code review, architecture review | 3 | 1-2 days | BottleneckDetector (age >3 days → reviewer assignment issue?) |
| **QA** | Manual + automated testing | 3 | 2-4 days | BottleneckDetector (age >5 days) |
| **Staging** | Deployed to staging, stakeholder validation | 2 | 1-2 days | FlowAnalyzer (age >3 days) |
| **Deploy** | Production deployment | 1 | <1 day | FlowAnalyzer (age >2 days) |
| **Done** | Live in production | None | N/A | FlowAnalyzer (cycle time) |

**Total WIP Limit:** 21 items

---

## WIP Limit Calculation

### Formula

```
WIP Limit per Column = (Team Size × 0.5) + 1

Example: 8-person team → WIP = (8 × 0.5) + 1 = 5 items per column
```

### Adjustments

**If team is highly specialized (e.g., only 1 QA person):**

```
WIP Limit = (# People in that role × 0.5) + 1

Example: 1 QA person → WIP = (1 × 0.5) + 1 = 1.5 → round to 2
```

**If team is highly collaborative (pairing, mobbing):**

```
WIP Limit = (Team Size × 0.3) + 1

Example: 6-person team, frequent pairing → WIP = (6 × 0.3) + 1 = 2.8 → round to 3
```

### Starting Recommendations

| Team Size | Ready WIP | Dev WIP | QA WIP | Total WIP |
|-----------|-----------|---------|--------|-----------|
| 3-5 people | 5 | 3 | 2 | 10 |
| 5-8 people | 5 | 4 | 2 | 11 |
| 8-12 people | 8 | 5 | 3 | 16 |
| 12-15 people | 10 | 6 | 4 | 20 |

**Start conservative** (easier to increase WIP than decrease)

---

## Policies

### Definition of Ready (DoR)

**Checklist for item to enter "Ready" column:**

- [ ] **Requirements documented** (user story, acceptance criteria)
- [ ] **Designs approved** (if UI/UX change — mockups, wireframes)
- [ ] **API contracts defined** (if backend work — endpoint specs, request/response schemas)
- [ ] **Dependencies resolved** (no blockers from external teams)
- [ ] **Estimated** (story points or t-shirt sizing)
- [ ] **Prioritized** by Product Owner (rank in backlog)
- [ ] **Technical feasibility confirmed** (no major unknowns, architecture approved)

**If item missing any of above → stays in Backlog until complete**

---

### Definition of Done (DoD)

**Checklist for item to move to "Done" column:**

- [ ] **Code implemented** and committed to version control (Git)
- [ ] **Code reviewed** by peer (at least 1 approval in GitHub/GitLab)
- [ ] **Automated tests written** (unit tests + integration tests where applicable)
- [ ] **All tests passing** (CI/CD pipeline green)
- [ ] **Deployed to production** (or staging if deployment is separate process)
- [ ] **Product Owner accepted** (meets acceptance criteria)
- [ ] **Documentation updated** (README, API docs, user guide if public-facing)
- [ ] **Monitoring configured** (if feature requires observability — logs, metrics, alerts)

**If item missing any of above → cannot move to Done (return to appropriate column)**

---

### Blocked Item Policy

**If item cannot progress (waiting on external dependency, blocker):**

1. Add "🚫 Blocked" label/tag
2. Add comment: 
   - What's the blocker?
   - Who can unblock?
   - ETA for resolution?
3. (Optional) Move to "Blocked" swim lane (horizontal section on board)
4. Daily check-in: Scrum Master/Team Lead follows up on blocked items
5. If blocker not resolved in 3 days → escalate to Product Owner/Tech Lead

**Blocked items DO count toward WIP limits** (can't pull new work while blocked items exist)

---

### Expedite Policy (Urgent Work)

**For P0 bugs, critical security fixes, emergency customer requests:**

1. Add "🔥 Expedite" label/tag
2. Expedite items **bypass WIP limits** (can exceed limit temporarily)
3. Team prioritizes expedite items above all other work
4. **Limit:** Max 1 expedite item in flow at a time (prevents "everything is urgent")
5. After expedite shipped, return to normal WIP limits

---

### Rework Policy

**If item returned to earlier column (e.g., QA finds bug, returns to Dev):**

1. Add "🔄 Rework" label
2. Track rework rate: % of items that return to earlier columns
3. If rework rate >15% → root cause analysis in retrospective
4. Common causes:
   - Incomplete Definition of Ready (requirements unclear)
   - Incomplete Definition of Done (QA standards not met)
   - Skill gap (developer needs training)

---

## Jira Configuration

### Board Setup

**1. Create Board:**
- Go to "Boards" → "Create board" → "Kanban board"
- Name: "Team Kanban Board" (or specific team name)
- Filter: (select project or custom JQL)

**2. Add Columns:**
- Click "Board settings" → "Columns"
- Add columns: Backlog, Ready, Dev, QA, Deploy, Done
- Map Jira statuses to columns:
  - Backlog → "To Do"
  - Ready → "Ready for Dev"
  - Dev → "In Progress"
  - QA → "In QA"
  - Deploy → "Ready for Deploy"
  - Done → "Done"

**3. Set WIP Limits:**
- Click "Board settings" → "Columns"
- For each column, set "Column limit" (e.g., Ready: 5, Dev: 3, QA: 2)
- Enable "Column constraint": "Issue count" (limits number of issues)

**4. Configure Card Layout:**
- Click "Board settings" → "Card layout"
- Show fields: Story points, Assignee, Priority, Labels
- Show colors: Priority (High = Red, Medium = Yellow, Low = Blue)

**5. Add Swimlanes (Optional):**
- Click "Board settings" → "Swimlanes"
- Options:
  - By Priority (High, Medium, Low)
  - By Assignee (each person's work)
  - By Expedite status (Expedite items on top)

---

### Automation Rules (Jira Automation)

**Rule 1: Alert on WIP Limit Breach**

```yaml
Trigger: Issue transitioned to any status
Condition: Column count > WIP limit
Action: 
  - Post to Slack: "⚠️ {{column_name}} column at {{count}}/{{limit}} WIP — over limit!"
  - Notify Team Lead via email
```

**Rule 2: Auto-Tag Aging Items**

```yaml
Trigger: Scheduled (runs daily at 9am)
Condition: Issue in column for >5 days (configurable per column)
Action:
  - Add label: "Aging Item"
  - Post comment: "⚠️ This item has been in {{column_name}} for {{days}} days (target: 3 days)"
  - Notify assignee via email
```

**Rule 3: Block Item Entry if Definition of Ready Not Met**

```yaml
Trigger: Issue transitioned to "Ready for Dev"
Condition: 
  - "Requirements" field is empty OR
  - "Designs Approved" checkbox not checked
Action:
  - Transition back to "To Do"
  - Post comment: "❌ Cannot move to Ready — Definition of Ready not met (missing requirements or designs)"
  - Notify reporter
```

---

### JQL Queries for Reporting

**Aging Items Report:**

```jql
project = "PROJECT_KEY" AND 
status in ("Ready for Dev", "In Progress", "In QA") AND 
created < -5d 
ORDER BY created ASC
```

**WIP Report:**

```jql
project = "PROJECT_KEY" AND 
status not in ("To Do", "Done") 
ORDER BY status, priority DESC
```

**Throughput Report (This Week):**

```jql
project = "PROJECT_KEY" AND 
status = "Done" AND 
resolved >= startOfWeek() 
ORDER BY resolved DESC
```

**Blocked Items Report:**

```jql
project = "PROJECT_KEY" AND 
labels = "Blocked" AND 
status != "Done" 
ORDER BY updated ASC
```

---

## Linear Configuration

### View Setup

**1. Create Kanban View:**
- Click "+" next to "Views" → "Board view"
- Name: "Kanban Board"
- Group by: "Status"

**2. Add Columns:**
- Click "..." on view → "Customize view" → "Statuses"
- Add statuses: Backlog, Ready, Dev, QA, Deploy, Done
- (Linear auto-creates columns for each status)

**3. Set WIP Limits:**
- (Note: Linear doesn't have built-in WIP limits — use external automation)
- Option 1: Use Linear API + custom script to monitor WIP
- Option 2: Manual monitoring (team checks board daily)

**4. Configure Filters:**
- Click "Filter" → Add filters:
  - "Project = [Your Project]"
  - "Assignee = [Team members]"
  - "Priority != None" (hide unprioritized items)

---

### Automation (Linear Webhooks + Zapier)

**Rule 1: Alert on Aging Items**

- Linear Webhook: "Issue Updated" → Zapier
- Zapier Filter: Issue in status for >5 days (use Linear API to calculate age)
- Zapier Action: Post to Slack #kanban-flow channel

**Rule 2: Tag Blocked Items**

- Linear Webhook: "Issue Comment Added" → Zapier
- Zapier Filter: Comment contains "blocked" keyword
- Zapier Action: 
  - Add label "Blocked" to issue
  - Post to Slack with mention: "@TeamLead — Item blocked, needs attention"

---

## Trello Configuration

### Board Setup

**1. Create Board:**
- Click "Create new board"
- Name: "Team Kanban"
- Visibility: Team (or Workspace)

**2. Add Lists (Columns):**
- Create lists: Backlog, Ready, Dev, QA, Deploy, Done
- Click "..." on each list → "Set list limit" (Trello Power-Up required)
  - Ready: 5
  - Dev: 3
  - QA: 2
  - Deploy: 1

**3. Enable Power-Ups:**
- Click "Power-Ups" → Enable:
  - "List Limits" (for WIP limits)
  - "Card Aging" (highlight old cards)
  - "Custom Fields" (add story points, priority)

**4. Card Template:**
- Create card: "TEMPLATE — User Story"
- Add checklist:
  - [ ] Requirements documented
  - [ ] Designs approved
  - [ ] Acceptance criteria defined
  - [ ] Estimated (story points)
- Team copies template for new items

---

### Automation (Butler for Trello)

**Rule 1: Alert on WIP Limit**

```
When a card is added to list "Dev"
and the number of cards in "Dev" is more than 3
post comment "@team — Dev column at WIP limit, complete work before adding more"
```

**Rule 2: Auto-Tag Aging Cards**

```
Every day at 9am
for each card in list "Dev"
if the card is older than 5 days
add label "Aging" to the card
and post comment "⚠️ This card has aged >5 days in Dev"
```

---

## AI Agent Integration Points

### FlowAnalyzer-Agent

**Data Source:** Jira/Linear/Trello API

**Queries:**

```
GET /rest/agile/1.0/board/{boardId}/issue
  → Fetch all items on board

For each item:
  - item.id
  - item.summary
  - item.status (maps to column)
  - item.created (age calculation: today - created)
  - item.updated (last activity)
  - item.assignee
  - item.story_points
```

**Output:** Slack #kanban-flow daily report

**Trigger:** Cron job (9am daily)

---

### BottleneckDetector-Agent

**Data Source:** Jira/Linear API + board configuration (WIP limits)

**Logic:**

```python
for column in ["Ready", "Dev", "QA", "Deploy"]:
    current_wip = count_items_in_column(column)
    wip_limit = get_wip_limit(column)
    avg_age = calculate_avg_age(column)
    target_age = get_target_age(column)  # e.g., Dev target = 3 days
    
    if current_wip > wip_limit:
        alert("⚠️ WIP limit breached", column, current_wip, wip_limit)
    
    if avg_age > (target_age * 2):
        alert("🚨 Bottleneck detected", column, avg_age, target_age)
```

**Output:** Slack #kanban-flow alerts (real-time)

**Trigger:** Cron job (every 1 hour)

---

### KanbanOptimizer-Agent

**Data Source:** 30 days of historical board data

**Analysis:**

```python
# Calculate optimal WIP limits
for column in ["Ready", "Dev", "QA"]:
    avg_throughput = calculate_throughput(column, last_30_days)
    bottleneck_frequency = calculate_bottleneck_days(column, last_30_days)
    
    if bottleneck_frequency > 30%:  # Bottleneck >30% of days
        recommend_increase_wip(column, current_limit + 1)
    
    if avg_throughput < 80% of capacity:
        recommend_decrease_wip(column, current_limit - 1)
```

**Output:** Monthly optimization report (Slack #kanban-optimization)

**Trigger:** First Friday of each month

---

## Metrics Dashboard Template

### Key Metrics to Track

| Metric | Calculation | Target | Display |
|--------|-------------|--------|---------|
| **Throughput** | # items completed per week | 10-15 items/week | Line chart (weekly trend) |
| **Cycle Time** | Days from Ready → Done (avg) | <5 days | Histogram (distribution) |
| **Lead Time** | Days from Backlog → Done (avg) | <7 days | Line chart (weekly trend) |
| **WIP** | # items in flow (Ready+Dev+QA+Deploy) | 10 items | Gauge (current vs. limit) |
| **Bottleneck Frequency** | % of days column bottlenecked | <10% | Bar chart (by column) |
| **Rework Rate** | % items returned to earlier column | <10% | Pie chart (rework vs. clean flow) |
| **Blocked Time** | % of cycle time spent blocked | <5% | Stacked bar chart |

---

### Example Dashboard (Grafana, Tableau, or Google Data Studio)

```
┌─────────────────────────────────────────────────────────────┐
│  KANBAN METRICS DASHBOARD                   Week: Nov 4-8   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📊 Throughput: 12 items/week  (+20% vs. last week) ✅       │
│  ⏱️  Cycle Time: 4.2 days      (-15% vs. last week) ✅       │
│  🚧 WIP: 9/10 items            (90% of limit) ✅             │
│  ⚠️  Bottleneck: QA (35% of week) → Needs attention          │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  Throughput Trend (Last 4 Weeks)                            │
│  ┌─────────────────────────────────────────┐               │
│  │ 10 ████                                 │               │
│  │ 11 █████                                │               │
│  │ 10 ████                                 │               │
│  │ 12 ██████  ← This week                  │               │
│  └─────────────────────────────────────────┘               │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  Cycle Time Distribution (This Week)                        │
│  ┌─────────────────────────────────────────┐               │
│  │ 2 days: ██ (2 items)                    │               │
│  │ 3 days: ████ (4 items)                  │               │
│  │ 4 days: ███ (3 items)                   │               │
│  │ 5 days: ██ (2 items)                    │               │
│  │ 6+ days: █ (1 item) ⚠️                   │               │
│  └─────────────────────────────────────────┘               │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  Bottleneck Analysis (This Week)                            │
│  ┌─────────────────────────────────────────┐               │
│  │ Ready:  10% █                           │               │
│  │ Dev:    15% ██                          │               │
│  │ QA:     35% ████████ ⚠️                  │               │
│  │ Deploy:  5% █                           │               │
│  └─────────────────────────────────────────┘               │
│  💡 Recommendation: Increase QA WIP limit 2→3               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Resources

**Framework Documentation:**
- [AI-Native Kanban](../../DOCS/12-ai-native-kanban.md)
- [AI Agents](../../DOCS/05-ai-agents.md)

**Playbooks:**
- [AI-Native Kanban Implementation](../../PLAYBOOKS/implementation/ai-native-kanban.md)

**Other Templates:**
- [Agent Definition Template](agent-definition-template.yaml)
- [Kanban Metrics Dashboard](kanban-metrics-dashboard.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
