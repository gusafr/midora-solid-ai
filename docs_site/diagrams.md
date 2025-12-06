# 📊 Framework Diagrams Gallery

**Visual representations of the SOLID.AI framework architecture, organizational patterns, and implementation examples.**

All diagrams are created using [Mermaid](https://mermaid.js.org/) and can be embedded in documentation, presentations, or exported as images.

---

## Core Framework Diagrams

### 1. SOLID.AI Architecture (6 Layers)

Complete architecture showing the central role of the Data Spine as the organizational nervous system.

```mermaid
--8<-- "DIAGRAMS/solid-ai-architecture.mmd"
```

**Use Cases:** Architecture overviews, technical presentations, onboarding

---

### 2. Data Spine Architecture

Detailed breakdown of the Data Spine components: contracts, products, lineage, observability.

```mermaid
--8<-- "DIAGRAMS/data-spine-architecture.mmd"
```

**Use Cases:** Data platform design, data engineering, governance discussions

---

### 3. Organizational Flow

How squads, pools, AI agents, and governance interact in practice, with role hierarchy levels.

```mermaid
--8<-- "DIAGRAMS/organizational-flow.mmd"
```

**Use Cases:** Organizational design workshops, team formation, role clarity

---

### 4. Role Hierarchy Framework ✨ NEW

4-level role hierarchy (Executive/High/Intermediate/Low) with decision authority, AI delegation, compensation, and career paths.

```mermaid
--8<-- "DIAGRAMS/role-hierarchy-framework.mmd"
```

**Use Cases:** Role definition, career laddering, compensation planning, hiring, performance reviews

**Related Documentation:** [Role Hierarchy (Human & AI)](role-hierarchy-human-ai.md)

---

### 5. AI-Native Safe Model

Sequence diagram showing ethical AI governance with policy constraints and human oversight.

```mermaid
--8<-- "DIAGRAMS/ai-native-safe-model.mmd"
```

**Use Cases:** AI safety discussions, governance design, ethical AI implementation

---

## Operational Pattern Diagrams

### 6. SIPOC Automation Pattern

How to automate any operational process using SIPOC methodology with human curatorship.

```mermaid
--8<-- "DIAGRAMS/sipoc-automation-pattern.mmd"
```

**Use Cases:** Process automation design, operational excellence, back-office automation

---

### 7. Pool Engagement Patterns

Three engagement models for pool-squad collaboration: Embedded, On-Demand, Self-Service.

```mermaid
--8<-- "DIAGRAMS/pool-engagement-patterns.mmd"
```

**Use Cases:** Resource allocation, pool design, capacity planning

---

### 8. Squad Lifecycle

State diagram showing squad formation, active delivery, blocked state, and transition options.

```mermaid
--8<-- "DIAGRAMS/squad-lifecycle.mmd"
```

**Use Cases:** Squad management, outcome planning, knowledge management

---

### 9. Cognitive Decision Flow

How AI agents make decisions with confidence-based escalation and human oversight.

```mermaid
--8<-- "DIAGRAMS/cognitive-decision-flow.mmd"
```

**Use Cases:** AI agent design, decision automation, human-in-the-loop patterns

---

### 10. AI-Native Sprint Flow ✨ NEW

Week-long AI-Native Agile sprint showing daily ceremonies with 6 AI agents participating.

```mermaid
--8<-- "DIAGRAMS/ai-native-sprint-flow.mmd"
```

**Use Cases:** AI-Native Agile implementation, sprint planning, team coaching

**Related Documentation:** [AI-Native Agile & SAFe](ai-native-agile.md)

---

### 11. Human-AI Collaboration Models ✨ NEW

Comprehensive visualization of 5 collaboration models with task examples and decision tree.

```mermaid
--8<-- "DIAGRAMS/collaboration-models-matrix.mmd"
```

**Use Cases:** Collaboration model design, task allocation, AI adoption planning, workforce planning

**Related Documentation:** [Human-AI Collaboration](human-ai-collaboration.md)

---

### 12. Human-AI Evolution Timeline

Gantt chart showing evolution of human-AI role allocation mapped to collaboration models (2025→2027+).

```mermaid
--8<-- "DIAGRAMS/human-ai-evolution.mmd"
```

**Use Cases:** Transformation roadmaps, workforce planning, change management

---

## Implementation Examples

### 13. Midora Implementation

Concrete implementation showing Midora's 4 systems, 10+ repositories, 6 pools, and product triad squads.

```mermaid
--8<-- "DIAGRAMS/midora-implementation.mmd"
```

**Use Cases:** Reference implementation, case studies, real-world examples

---

## Additional Visual Resources

### Bipolar Organization vs. AI-Native Organization

Text-based visual comparison showing the competitive disadvantage of "bipolar organizations" (IT fast, business slow) vs. AI-Native organizations (entire org fast).

📄 **[View Bipolar vs. AI-Native Comparison](DIAGRAMS/bipolar-vs-ai-native.md)**

Includes:
- Side-by-side ASCII diagrams
- Economics comparison (cost structure, scalability)
- 5-year competitive outcomes projection
- Leadership choice framework

**Related Documentation:** [Whole-Organization Transformation](whole-organization-transformation.md)

---

## Using These Diagrams

### Embedding in Your Documentation

All diagrams are available in the [`DIAGRAMS/`](https://github.com/gusafr/midora-solid-ai/tree/main/DIAGRAMS) directory as `.mmd` files.

**To embed in Markdown:**

```markdown
​```mermaid
--8<-- "DIAGRAMS/solid-ai-architecture.mmd"
​```
```

Or copy the diagram source directly from the `.mmd` file.

### Viewing & Editing

- **VS Code:** Install [Mermaid Preview extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)
- **GitHub:** Diagrams render automatically in `.md` files
- **Online Editor:** [Mermaid Live Editor](https://mermaid.live) for testing/editing
- **Export:** Use Mermaid Live Editor to export as SVG, PNG, or PDF

### Color Scheme

Diagrams use consistent colors per layer/concept:

- **Purpose Layer:** Orange (#ff9800)
- **Data Spine:** Blue (#0066cc) - Always emphasized with thick border
- **Cognitive Layer:** Purple (#9c27b0)
- **Automation Mesh:** Green (#4caf50)
- **Organizational Layer:** Yellow (#fbc02d)
- **Governance & Ethics:** Red (#d32f2f)

---

## Diagram Maintenance

**Responsibility:** Solutions Architecture Pool + Documentation maintainers

**Source Files:** [`DIAGRAMS/`](https://github.com/gusafr/midora-solid-ai/tree/main/DIAGRAMS) directory

**Last Updated:** November 4, 2025

**Diagram Count:** 13 Mermaid diagrams + 1 markdown visual

---

## Contributing

Have ideas for new diagrams or improvements? See [CONTRIBUTING.md](https://github.com/gusafr/midora-solid-ai/blob/main/CONTRIBUTING.md) for guidelines.

---

**Next Steps:**
- Explore [Reading Paths](README.md) for guided framework tours
- Review [Adoption Pack](adoption/index.md) for implementation templates
- Check [Playbooks](playbooks/README.md) for sector-specific guidance
