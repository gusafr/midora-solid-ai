# solid.ai Framework Diagrams

This directory contains **Mermaid diagram source files** that visualize the solid.ai framework architecture, organizational patterns, and implementation examples.

## Core Framework Diagrams

### 1. **solid-ai-architecture.mmd**
**Purpose:** Complete six-layer architecture showing the central role of the Data Spine

**Key Elements:**
- Purpose Layer (mission, values, outcomes)
- Data Spine (contracts, products, lineage, observability)
- Cognitive Layer (AI agents, orchestration, learning)
- Automation Mesh (workflows, SIPOC, RPA)
- Organizational Layer (squads, pools, roles)
- Governance & Ethics Layer (policies, compliance, circle)
- Feedback loops showing bidirectional learning

**Use Cases:** Architecture overviews, technical presentations, onboarding

---

### 2. **data-spine-architecture.mmd**
**Purpose:** Detailed breakdown of the Data Spine as the organizational nervous system

**Key Elements:**
- Data sources and ingestion patterns
- Lakehouse storage (Bronze/Silver/Gold)
- Data contracts and SLAs
- Data products and feature stores
- Catalog with lineage and governance
- Observability (quality, monitoring, usage)
- Consumer access patterns (BI, AI agents, apps, analytics)

**Use Cases:** Data platform design, data engineering teams, data governance discussions

---

### 3. **organizational-flow.mmd**
**Purpose:** How squads, pools, AI agents, and governance interact in practice

**Key Elements:**
- Product Triad squad structure (PO + System Architect + PM) with role levels
- Six capability pools with specializations and role level ranges
- Role hierarchy annotations (Executive/High/Intermediate/Low levels)
- AI agent layer supporting humans
- Governance Circle oversight
- Data Spine as integration backbone
- Engagement flows and feedback loops

**Use Cases:** Organizational design workshops, team formation, role clarity

**Updated:** 2025-11-04 (Added role hierarchy levels to squads and pools)

---

### 4. **role-hierarchy-framework.mmd** ✨ NEW
**Purpose:** Visual framework for 4-level role hierarchy with decision authority, AI delegation, and career paths

**Key Elements:**
- Four levels: Executive (🎯), High (🏆), Intermediate (⚙️), Low (🌱)
- Decision authority per level (budget ranges, strategic impact)
- AI delegation patterns (what AI handles vs. what humans decide)
- Compensation ranges (market-competitive transparency)
- Career progression paths (promotion criteria, timelines)
- Role examples per level (CTO, Principal Engineer, Software Engineer II, Junior Developer)
- Transition criteria between levels

**Use Cases:** Role definition, career laddering, compensation planning, hiring, performance reviews

---

### 5. **ai-native-safe-model.mmd**
**Purpose:** Sequence diagram showing ethical AI governance in action

**Key Elements:**
- Purpose Council → Data Spine → AI Agent → Automation Mesh → Governance Circle
- Policy constraints flowing from purpose
- Curated data products with contracts
- Decision orchestration with confidence levels
- Telemetry and audit logs
- Feedback loops for continuous improvement

**Use Cases:** AI safety discussions, governance design, ethical AI implementation

---

## Operational Pattern Diagrams

### 6. **sipoc-automation-pattern.mmd**
**Purpose:** How to automate any operational process using SIPOC methodology

**Key Elements:**
- SIPOC stages (Supplier, Input, Process, Output, Customer)
- Automation implementation (ingestion, validation, execution, generation, delivery)
- Observability layer (metrics, logs, exceptions)
- Human curatorship model (monitor, review exceptions, refine policies)
- Continuous learning feedback loops

**Use Cases:** Process automation design, operational excellence, back-office automation

---

### 7. **pool-engagement-patterns.mmd**
**Purpose:** Three engagement models for pool-squad collaboration

**Key Elements:**
- Squad need identification and intake
- AI-powered capacity assessment and skill matching
- Embedded engagement (2-4 weeks, dedicated resource)
- On-demand engagement (hours/days, consultation)
- Self-service engagement (instant, assets/templates)
- Feedback loops and learning

**Use Cases:** Resource allocation, pool design, capacity planning

---

### 8. **squad-lifecycle.mmd**
**Purpose:** State diagram showing squad formation, active delivery, and transition

**Key Elements:**
- Formation (outcome definition → triad selection → governance approval)
- Active delivery (sprints, retrospectives, checkpoints)
- Blocked state (blocker resolution or strategic pivot)
- Transition options (dissolve, pivot, sustain)
- Knowledge capture and handoff processes

**Use Cases:** Squad management, outcome planning, knowledge management

---

### 9. **cognitive-decision-flow.mmd**
**Purpose:** Detailed sequence of how AI agents make decisions with human oversight

**Key Elements:**
- Event triggers and orchestration
- Data Spine context retrieval
- Agent decision generation
- Policy engine guardrails
- Confidence-based escalation (high/medium/low)
- Human review for edge cases
- Observability and continuous learning

**Use Cases:** AI agent design, decision automation, human-in-the-loop patterns

---

### 10. **ai-native-sprint-flow.mmd** ✨ NEW
**Purpose:** Week-long AI-Native Agile sprint showing daily ceremonies with AI agent participation

**Key Elements:**
- **Monday (Planning):** SprintPlanner-Agent pre-generates sprint options, team finalizes
- **Tuesday-Thursday (Build):** StandupFacilitator-Agent runs daily standups, CIAgent automates testing
- **Wednesday (Refinement):** BacklogRefiner-Agent analyzes upcoming stories, estimates effort
- **Friday (Review & Retro):** DemoCoordinator-Agent prepares demo, RetroAnalyzer-Agent finds patterns
- Human-AI collaboration throughout (squad makes decisions, AI provides insights)
- Data Spine integration for metrics, backlog, deployment
- Governance policy checks

**Use Cases:** AI-Native Agile implementation, sprint planning, team coaching, transformation roadmaps

---

### 11. **collaboration-models-matrix.mmd** ✨ NEW
**Purpose:** Comprehensive visualization of 5 Human-AI collaboration models with task examples

**Key Elements:**
- **Model 1 - Reserved for Humans:** Ethics, vision, culture, relationships (100% human)
- **Model 2 - Human-Led with AI Support:** Strategic planning, architecture (70-85% AI confidence)
- **Model 3 - Human-AI Partnership:** Software dev, content creation (85-92% AI confidence, 50/50 collaboration)
- **Model 4 - AI-Led with Human Oversight:** Testing, monitoring, L1 support (92-97% AI confidence)
- **Model 5 - AI-Autonomous with Human Curation:** CI/CD, data entry, scheduling (97%+ AI confidence)
- Decision tree for choosing the right model
- Evolution timeline (2025 → 2027+)
- Role examples per model

**Use Cases:** Collaboration model design, task allocation, AI adoption planning, workforce planning

---

### 12. **human-ai-evolution.mmd**
**Purpose:** Gantt chart showing the evolution of human-AI role allocation mapped to collaboration models

**Key Elements:**
- Phase 1 (2025): Mostly human with AI copilots (Reserved, Human-Led, Partnership models)
- Phase 2 (2026): Balanced human-AI collaboration (Partnership, AI-Led models)
- Phase 3 (2027+): AI-majority with human curation (AI-Led, Autonomous models)
- Role-by-role breakdown (PO, Architect, PM, Developers, QA, PMO, Operations)
- Explicit mapping to 5 collaboration models (not just percentages)

**Use Cases:** Transformation roadmaps, workforce planning, change management

**Updated:** 2025-11-04 (Mapped timeline to 5 collaboration models for clarity)

---

## Implementation Examples

### 13. **midora-implementation.mmd**
**Purpose:** Concrete implementation showing Midora's 4 systems, 10+ repositories, pools, and squads

**Key Elements:**
- **midora-core** (Platform): back-end-py, api-openapi, idp-backstage
- **midora-intelligence** (AI/ML): ml-service, magi-py
- **learning-apps** (Student Experience): front-end-fl-v2, front-end-ts, portal-ph
- **content-pipeline**: course-generator-py
- Six capability pools (Developers, Architecture, QA, PMO, Coaching, Portfolio)
- Product Triad squads working across systems
- 100% automated operations layer

**Use Cases:** Reference implementation, case studies, real-world examples

---

## Additional Resources

### 14. **bipolar-vs-ai-native.md**
**Purpose:** Text-based visual comparison of traditional "bipolar organization" vs. AI-Native organization

**Key Elements:**
- Side-by-side ASCII diagrams (IT department fast, rest of company slow vs. entire org AI-native)
- Economics comparison (cost structure, scalability, profit margins)
- Competitive outcomes (5-year projection table)
- Leadership choice framework (status quo, partial, whole-org transformation)
- Getting started roadmap (Week 1 → Month 24)

**Use Cases:** Executive presentations, transformation case, competitive strategy

---

## Usage Guidelines

### Embedding in Documentation

To embed a diagram in a Markdown file:

```markdown
```mermaid
--8<-- "DIAGRAMS/solid-ai-architecture.mmd"
\```
```

Or copy the content directly from the `.mmd` file.

### Viewing Diagrams

- **VS Code:** Install the [Mermaid Preview extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)
- **GitHub:** Diagrams render automatically in `.md` files
- **MkDocs:** Use the `mermaid2` plugin (already configured in `mkdocs.yml`)
- **Online:** [Mermaid Live Editor](https://mermaid.live)

### Updating Diagrams

When updating diagrams:
1. Edit the `.mmd` source file
2. Validate syntax using Mermaid Live Editor or VS Code preview
3. Update documentation that references the diagram
4. Test rendering in MkDocs with `mkdocs serve`
5. Commit changes with descriptive message

### Diagram Style Guidelines

- **Colors:** Use consistent color schemes per layer/concept
  - Purpose Layer: Orange (#ff9800)
  - Data Spine: Blue (#0066cc) - Always emphasized with thick border
  - Cognitive Layer: Purple (#9c27b0)
  - Automation Mesh: Green (#4caf50)
  - Organizational Layer: Yellow (#fbc02d)
  - Governance & Ethics: Red (#d32f2f)

- **Emojis:** Use sparingly for visual clarity (🎯 squads, 🏊 pools, 🧬 data spine, etc.)

- **Layout:** Prefer TB (top-bottom) for hierarchies, LR (left-right) for flows

- **Complexity:** Keep diagrams focused - split complex topics across multiple diagrams

---

## Diagram Maintenance

**Responsibility:** Solutions Architecture Pool + Documentation maintainers

**Cadence:** Review quarterly or when significant framework changes occur

**Versioning:** Track major changes in git history; consider version tags for breaking changes

**Diagram Count:** 13 Mermaid diagrams (.mmd) + 1 markdown visual (bipolar-vs-ai-native.md)

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines on proposing new diagrams or improving existing ones.

---

**Last Updated:** 2025-11-04  
**Maintained by:** solid.ai Framework Team  
**License:** MIT
