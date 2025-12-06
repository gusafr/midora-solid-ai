# Squad Formation Checklist

**Purpose:** Establish purpose-driven, autonomous squads aligned with SOLID.AI organizational principles

**Framework:** SOLID.AI | **Version:** 1.0

---

## Pre-Formation (Discovery & Planning)

### Business Service Definition (CRITICAL FIRST STEP)
- [ ] **Business service identified** - squad owns a self-contained capability (e.g., "Order Fulfillment" NOT "Backend Team")
- [ ] **Service boundary validation** - clear start/end, inputs/outputs, no overlap with other squads
- [ ] **Domain experts consulted** - verified this is a genuine bounded context in Domain-Driven Design sense
- [ ] **Duplication check** - confirmed no other squad already owns this service
- [ ] **Value independence** - service can deliver business value without constant coordination
- [ ] **Scalability verified** - service scope sustainable (not too broad to split, not too narrow to combine)

**Examples of Good Business Services:**
- ✅ Customer Onboarding (signup → activation)
- ✅ Subscription Management (plans → billing → cancellation)
- ✅ Fraud Detection (real-time risk scoring)
- ❌ "Frontend Team" (technical layer, not business service)
- ❌ "Feature X Squad" (temporary, not sustainable service)

### Squad Category & Purpose
- [ ] **Squad category** selected - Tech Core | Business Core | Operations Core | Innovation & Intelligence
  - **Tech Core:** Platform/infrastructure enabling other squads (e.g., Data Platform, MLOps, DevOps)
  - **Business Core:** Direct customer value or revenue (e.g., Order Fulfillment, Customer Onboarding)
  - **Operations Core:** Internal operations (e.g., Finance AP/AR, HR Payroll, Compliance)
  - **Innovation & Intelligence:** R&D, experimentation, strategic initiatives
- [ ] **Category alignment** validated - category matches squad's primary function and stakeholder focus
- [ ] **Squad mission** defined - clear statement of why this squad exists
- [ ] **Organizational alignment** verified - connects to company strategy and values
- [ ] **Outcome focus** articulated - what success looks like, not just tasks
- [ ] **Scope boundaries** set - what's in and out of squad's domain (aligned with business service)
- [ ] **Stakeholder needs** understood - who depends on this squad's work

### Composition & Roles
- [ ] **Squad size** determined - ideally 5-9 people (small enough to collaborate, large enough for skills)
- [ ] **Cross-functional skills** identified - roles needed to deliver end-to-end
- [ ] **Squad members** selected - people with right skills and alignment to mission
- [ ] **Squad lead** appointed - clear ownership and accountability
- [ ] **Pool relationships** defined - which pools (design, data, platform, etc.) support this squad
- [ ] **AI agent assignments** planned - which AI agents will support squad's work

### Charter Development
- [ ] **Squad charter** drafted - using template ([TEMPLATES/squad-charter-template.md](../TEMPLATES/squad-charter-template.md))
- [ ] **Vision statement** written - inspiring future state squad is working toward
- [ ] **Key results** defined - measurable outcomes (OKRs or similar)
- [ ] **Success metrics** identified - how squad measures impact and health
- [ ] **Constraints and guardrails** documented - what squad cannot do or must comply with
- [ ] **Decision rights** clarified - what squad can decide autonomously vs. escalate

### Data Spine Integration (CRITICAL)
- [ ] **Input data contracts** defined - what data/events service consumes (schema, SLA, source)
- [ ] **Output data contracts** defined - what data/events service produces (schema, SLA, consumers)
- [ ] **Business events** cataloged - all domain events service publishes (with ownership)
- [ ] **Event stakeholders** identified - which other services will consume your events
- [ ] **Schema registry** configured - contracts registered with versioning
- [ ] **Data quality SLAs** defined - accuracy, completeness, timeliness guarantees
- [ ] **Observability plan** created - dashboards for service health, data lineage, quality monitoring

### Automation Mesh Integration (CRITICAL)
- [ ] **SIPOC workflow** documented - Suppliers → Inputs → Process → Outputs → Customers
- [ ] **Automation opportunities** identified - which steps are AI-automated vs. human-in-loop
- [ ] **Event subscriptions** configured - what events service consumes from other services
- [ ] **Event publications** registered - what events service produces for other services
- [ ] **Workflow orchestration** defined - how service triggers/responds to events
- [ ] **Error handling** designed - retry policies, dead letter queues, escalation paths
- [ ] **Circuit breakers** configured - graceful degradation when dependencies fail

### OKRs & KPIs (CRITICAL)
- [ ] **Service-level OKRs** defined - quarterly objectives aligned with business strategy
- [ ] **KPI dashboard** configured - real-time metrics (business impact, efficiency, quality, speed)
- [ ] **AI augmentation metrics** tracked - automation rate, human-AI collaboration effectiveness
- [ ] **Business value metrics** defined - revenue, cost savings, customer satisfaction
- [ ] **Quarterly review cadence** established - OKR check-ins with stakeholders

### Data Governance Compliance
- [ ] **Event ownership** documented - squad is authoritative source for domain events
- [ ] **Breaking change policy** communicated - RFC process for schema changes affecting consumers
- [ ] **Data classification** applied - PII, sensitive, public data properly tagged
- [ ] **Retention policies** defined - how long data is kept (GDPR, SOX, etc.)
- [ ] **Access controls** configured - role-based permissions for service data
- [ ] **Audit logging** enabled - all data access logged for compliance

---

## Formation (Launch & Onboarding)

### Team Onboarding
- [ ] **Kickoff meeting** held - squad meets, reviews charter, builds connections
- [ ] **Roles and responsibilities** clarified - everyone knows their contribution
- [ ] **Working agreements** established - how squad collaborates, communicates, resolves conflict
- [ ] **Rituals designed** - stand-ups, planning, reviews, retros, etc.
- [ ] **Communication channels** set up - Slack, Teams, email lists, etc.
- [ ] **Documentation space** created - wiki, repo, or shared drive for squad knowledge

### Operating Model
- [ ] **Cadence defined** - sprint/iteration length, planning frequency, review cycles
- [ ] **Planning process** designed - how squad prioritizes, estimates, and commits
- [ ] **Review rituals** scheduled - demos, retrospectives, stakeholder check-ins
- [ ] **Escalation paths** clear - when and how squad raises blockers or asks for help
- [ ] **Stakeholder touchpoints** planned - regular updates to those depending on squad

### AI & Data Integration
- [ ] **AI agents onboarded** - squad knows which agents support them and how to use
- [ ] **Data access** configured - squad can access data needed for their mission
- [ ] **Data contracts** reviewed - squad understands data they produce/consume
- [ ] **Observability dashboards** set up - squad can monitor their systems and AI agents
- [ ] **Automation playbooks** shared - squad trained on SIPOC automation patterns

### Empowerment & Autonomy
- [ ] **Budget/resources** allocated - squad has what they need to deliver
- [ ] **Autonomy boundaries** communicated - what squad owns vs. coordinates
- [ ] **Decision-making authority** granted - squad can act without constant approval
- [ ] **Failure tolerance** established - psychological safety to experiment and learn
- [ ] **Support network** identified - pools, mentors, or leadership for guidance

---

## Operation (Execute & Iterate)

### Daily Execution
- [ ] **Daily rituals** running - stand-ups, check-ins, or async updates
- [ ] **Work visible** - kanban board, task tracker, or similar for transparency
- [ ] **Blockers surfaced** quickly - team flags and resolves impediments
- [ ] **Human-AI collaboration** effective - squad using AI agents productively
- [ ] **Stakeholder communication** flowing - regular updates and feedback

### Iteration & Learning
- [ ] **Sprint/iteration planning** - squad reviews progress, sets next priorities
- [ ] **Retrospectives** held regularly - squad reflects, learns, improves
- [ ] **Feedback loops** active - user, stakeholder, and operational data informs decisions
- [ ] **Metrics tracked** - squad monitors success metrics and health indicators
- [ ] **Experiments run** - squad tests hypotheses, learns from failures
- [ ] **Knowledge shared** - learnings documented (RFCs, ADRs, playbooks)

### Squad Health Monitoring
- [ ] **Team morale** checked - regular pulse on engagement, burnout, psychological safety
- [ ] **Cognitive load** managed - squad not overwhelmed, complexity sustainable
- [ ] **Skill development** happening - team members growing capabilities
- [ ] **Collaboration quality** assessed - healthy conflict, trust, shared ownership
- [ ] **Work-life balance** maintained - sustainable pace, no chronic overwork

---

## Governance & Alignment (Ongoing)

### Purpose Alignment
- [ ] **Quarterly mission review** - squad reassesses charter, adjusts if needed
- [ ] **Strategic alignment** verified - squad work still serves company priorities
- [ ] **Value delivery** measured - squad creating expected impact
- [ ] **Scope drift** monitored - squad staying focused or thoughtfully expanding

### Cross-Squad Coordination
- [ ] **Dependencies managed** - handoffs with other squads clear and smooth
- [ ] **Pool collaboration** healthy - squads getting support from pools (design, data, etc.)
- [ ] **Conflicts resolved** - disputes with other squads or teams addressed constructively
- [ ] **Shared learnings** - squad contributing to organizational knowledge

### Ethical & Governance Compliance
- [ ] **Ethical practices** upheld - squad following governance and ethics guidelines
- [ ] **Data privacy** maintained - squad handling data responsibly
- [ ] **AI accountability** ensured - AI agents used transparently and safely
- [ ] **Audit readiness** - squad can explain decisions and show compliance
- [ ] **Category-specific governance** met:
  - **Tech Core:** High security/compliance standards (platform vulnerabilities = org-wide impact)
  - **Business Core:** Medium oversight (product quality, customer data privacy)
  - **Operations Core:** High regulatory compliance (SOX, GDPR, labor laws, audit trails)
  - **Innovation:** Low governance (fast iteration, controlled risk, experimental approval)

---

## Evolution (Adapt or Sunset)

### Scaling & Adaptation
- [ ] **Growth plan** if needed - how squad expands if mission grows
- [ ] **Split strategy** if too large - spawning new squads from existing one
- [ ] **Skill gaps** addressed - hiring, training, or pool support to fill needs
- [ ] **Charter updates** - mission, scope, or structure adjusted based on learning

### Sunset or Pivot
- [ ] **Mission complete** recognized - if squad achieved goal, celebrate and reassign
- [ ] **Pivot decision** made - if mission no longer viable, squad redirected or dissolved
- [ ] **Knowledge transfer** - learnings and artifacts preserved for organization
- [ ] **Team transition** - members moved to new squads or roles thoughtfully

---

## Governance Checkpoints

| Checkpoint | Timing | Participants | Purpose |
|------------|--------|--------------|---------|
| **Kickoff Review** | Before formation | Leadership + Squad Lead | Validate charter, mission, and resourcing |
| **30-Day Check-in** | 1 month after launch | Squad + Stakeholders | Early health check, address teething issues |
| **Quarterly Review** | Every 3 months | Squad + Leadership | Assess impact, alignment, and health |
| **Annual Strategy** | Yearly | All Squads + Leadership | Realign missions with company strategy |
| **Sunset Decision** | As needed | Leadership + Squad | Thoughtfully end or pivot squad |

---

## Red Flags (Intervention Needed)

⛔ **ACT if any of these occur:**

- [ ] **Mission drift** - squad losing focus or taking on unrelated work
- [ ] **Burnout signals** - team overworked, morale low, turnover increasing
- [ ] **Value stagnation** - squad not delivering expected impact
- [ ] **Dependency hell** - squad constantly blocked by other teams
- [ ] **Conflict escalation** - unresolved tensions within or across squads
- [ ] **Ethical concerns** - squad cutting corners on ethics or governance
- [ ] **Lack of autonomy** - squad needs constant approvals, can't make decisions

**Action:** Leadership intervention - coaching, resources, restructuring, or mission reset.

---

## Success Indicators

✅ **Healthy squad shows:**

- [ ] **Clear purpose** - everyone can articulate the squad's mission
- [ ] **Autonomy** - squad makes most decisions without escalation
- [ ] **Velocity** - consistent delivery of value to users/stakeholders
- [ ] **Learning** - squad experiments, retrospects, and improves
- [ ] **Collaboration** - trust, psychological safety, healthy conflict
- [ ] **Impact** - metrics show squad is achieving outcomes
- [ ] **Sustainability** - team energized, not burned out
- [ ] **Alignment** - squad work connects to company strategy

---

## Tools & Templates

- **Squad Charter Template:** [TEMPLATES/squad-charter-template.md](../TEMPLATES/squad-charter-template.md)
- **Squad Playbook:** [PLAYBOOKS/playbook-squads.md](../../PLAYBOOKS/playbook-squads.md)
- **Organizational Model:** [DOCS/03-organizational-model.md](../../DOCS/03-organizational-model.md)
- **Organizational Topology RFC:** [RFC/rfc-0003-midora-organizational-topology.md](../../RFC/rfc-0003-midora-organizational-topology.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Feedback:** [GitHub Issues](https://github.com/gusafr/midora-solid-ai/issues)
