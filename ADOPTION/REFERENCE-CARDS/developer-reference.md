# Developer Quick Reference Card

**Role:** Software Developer | **Framework:** SOLID.AI | **Version:** 1.0

---

## Core AI Prompting Patterns for Developers

### 1. Purpose-Driven Feature Development

```
I need to implement [FEATURE]. Before writing code:

1. What is the human-centered purpose of this feature?
2. How does it align with our product's core values?
3. What are potential ethical concerns or unintended consequences?
4. What success metrics beyond "shipped" should we track?

After answering, suggest an implementation approach.
```

**Use when:** Starting any new feature or significant code change

---

### 2. Architecture Decision with AI Context

```
I'm deciding between [OPTION A] and [OPTION B] for [PROBLEM].

Consider:
- Scalability with AI agents in the loop
- Observability and debuggability
- Data contract implications
- Human oversight requirements
- Cognitive load on the team

Provide a structured comparison and recommendation.
```

**Use when:** Making architectural or design choices

---

### 3. Code Review with Ethical Lens

```
Review this code for:
1. Functional correctness and edge cases
2. Observability (logging, metrics, tracing)
3. Ethical implications (bias, privacy, transparency)
4. AI agent interaction patterns
5. Data contract compliance

[PASTE CODE]

Provide feedback in priority order.
```

**Use when:** Reviewing your own code or others'

---

### 4. Data Contract Design

```
I need to design a data contract for [ENTITY/EVENT].

Include:
- Schema with semantic meaning
- Ownership and lifecycle
- Quality expectations (freshness, accuracy)
- Privacy and security requirements
- Consuming systems and SLAs

Generate a contract template aligned with SOLID.AI Data Spine principles.
```

**Use when:** Creating new APIs, events, or data models

---

### 5. AI Agent Definition

```
Define an AI agent for [TASK/CAPABILITY]:

Agent Persona: [Name and role]
Purpose: [Why this agent exists]
Capabilities: [What it can do]
Guardrails: [What it cannot or must not do]
Human Oversight: [When/how humans intervene]
Success Metrics: [How we measure value]
Failure Modes: [What could go wrong and recovery plans]

Format as YAML compatible with our agent registry.
```

**Use when:** Introducing new AI capabilities

---

### 6. Debugging with Observability

```
I'm debugging [ISSUE]. Current symptoms: [DESCRIBE].

Help me:
1. Identify what telemetry data I should examine
2. Formulate queries for logs/metrics/traces
3. Determine if this is a code, data, or AI agent issue
4. Plan systematic isolation steps
5. Document findings for future learning

What's the first thing I should check?
```

**Use when:** Troubleshooting production issues

---

### 7. Refactoring for Clarity

```
This code works but is hard to understand/maintain:

[PASTE CODE]

Refactor it following these principles:
- Scalable Simplicity (reduce cognitive load)
- Clear data flow and contracts
- Explicit error handling
- Observable execution paths
- Self-documenting intent

Explain each change.
```

**Use when:** Improving code quality

---

### 8. Test Strategy with AI Components

```
I need a test strategy for [COMPONENT] which includes AI agents.

Design tests for:
1. Deterministic logic (unit tests)
2. AI agent behavior (property-based, golden sets)
3. Data contract compliance (schema validation)
4. Human-AI handoff points (integration tests)
5. Ethical guardrails (adversarial testing)
6. Observability (trace validation)

Suggest specific test scenarios.
```

**Use when:** Planning testing approaches

---

### 9. Performance Optimization

```
[COMPONENT] is too slow. Current metrics: [DATA].

Analyze for:
- Algorithmic complexity
- I/O bottlenecks (DB, API, AI inference)
- Unnecessary work or redundancy
- Caching opportunities
- Data pipeline inefficiencies

Recommend optimizations prioritized by impact/effort ratio.
```

**Use when:** Addressing performance issues

---

### 10. Documentation Generation

```
Generate documentation for this code:

[PASTE CODE]

Include:
- Purpose and context (the "why")
- Public interface and usage examples
- Dependencies and data contracts
- AI agent interactions (if any)
- Observability hooks
- Known limitations and edge cases

Format in Markdown suitable for our docs site.
```

**Use when:** Documenting code or APIs

---

## SOLID.AI Developer Mindset

✅ **Do:**
- Start with purpose before jumping to implementation
- Design for observability from day one
- Document AI agent roles and responsibilities explicitly
- Build in feedback loops for continuous learning
- Consider ethical implications early
- Keep complexity at the edges, simplicity at the core

❌ **Avoid:**
- "Move fast and break things" without guardrails
- Black-box AI implementations
- Ignoring data lineage and contracts
- Optimizing for efficiency over values
- Skipping human oversight mechanisms

---

## Key Resources

- **Full Playbooks:** [PLAYBOOKS/](../../PLAYBOOKS/)
- **Architecture Docs:** [DOCS/02-architecture.md](../../DOCS/02-architecture.md)
- **Data Spine:** [RFC-0002](../../RFC/rfc-0002-data-layer.md)
- **AI Agents:** [DOCS/05-ai-agents.md](../../DOCS/05-ai-agents.md)
- **Glossary:** [DOCS/glossary.md](../../DOCS/glossary.md)

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Feedback:** [GitHub Issues](https://github.com/gusafr/midora-solid-ai/issues)
