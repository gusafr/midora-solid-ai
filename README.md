# solid.ai — Organizational Nervous System for AI-Native Companies

solid.ai is the open framework for designing intelligent, ethical, and adaptive organizations where humans and AI co-create value. The repository captures the reference model, governance patterns, and playbooks required to connect purpose, data, intelligence, automation, and organizational design into one cohesive operating system.

## Why solid.ai

### The Competitive Imperative
**You cannot be "agile" or "AI-Native" when only IT operates in this paradigm.** Most organizations are **bipolar**—one side digital, adaptive, and iterative; the other side analog, hierarchical, and slow. The slowest process sets the tempo for the entire organization.

**SOLID.AI is the blueprint for whole-organization transformation:**

- ⚡ **Eliminate Overhead**: AI handles 80% of repetitive tasks (data entry, approvals, manual reconciliation), freeing humans for high-value work
- 🎯 **Increase Reliability**: Reduce error rates from 5-10% (human) to <1% (AI-enforced consistency)
- 📈 **Exponential Scalability**: Double revenue without doubling headcount—AI scales at marginal cost
- 🏃 **10x Speed**: When ALL functions (Sales, Finance, HR, Marketing, Ops) operate at AI speed, time-to-market collapses from months to weeks
- 🤝 **Human-AI Symbiosis**: Augment human creativity, judgment, and empathy with AI automation—not replacement
- 📊 **Clear Role Progression**: 4-level hierarchy (Assistant/Analyst → Consultant/Coordinator → Specialist/Manager → Director) applies to both humans and AI agents
- 🌍 **Universal**: Applicable across ALL industries (tech, healthcare, finance, manufacturing, retail, consulting, logistics, HR)
- 🛡️ **Ethical & Accountable**: Treat AI agents as transparent, observable teammates with human oversight

> **The Only Sustainable Path:** Organizations that transform **coherently across all functions** will outpace those that remain organizationally schizophrenic. See [Whole-Organization Transformation](DOCS/09-whole-organization-transformation.md).

> **🤝 Where Humans Lead**  
> SOLID.AI is designed for **human-AI collaboration**, not human replacement. While AI excels at data processing, pattern recognition, and automation, certain roles require uniquely human capabilities:
> - **Empathy & Trust**: In-person sales, client relationships, bedside manner, employee mentoring
> - **Creative Vision**: Strategic planning, product innovation, brand strategy
> - **Ethical Judgment**: High-stakes decisions, conflict resolution, fairness in edge cases
> - **Physical Presence**: Surgery, hands-on manufacturing, emergency response
> 
> See [**Human-AI Collaboration Guide**](DOCS/08-human-ai-collaboration.md) for detailed guidance on where to preserve the irreplaceable human element.

## Core Layers
| Layer | Focus | Outcomes |
| --- | --- | --- |
| Purpose Layer | Strategic intent, ethics, human oversight | Coherent direction and alignment |
| Data Spine | Shared data contracts, interoperability, observability | Trusted information flow |
| Cognitive Layer | AI agents, orchestration (e.g., MAGI), learning loops | Responsible intelligence |
| Automation Mesh | Event-driven execution, SIPOC automation patterns | Reliable, adaptive operations |
| Organizational Layer | Squads, pools, adaptive topology | Symbiotic human–AI collaboration |
| Governance & Ethics Layer | Accountability, transparency, auditability | Trustworthy scale |

## Repository Structure
| Path | Description |
| --- | --- |
| `README.md` | Entry point and orientation for contributors and adopters |
| `QUICK-START-GUIDE.md` | **NEW!** 5-minute guide to start using SOLID.AI today |
| `LICENSE` | MIT License granting open-source usage |
| `CODE_OF_CONDUCT.md` | Community expectations and escalation paths |
| `CONTRIBUTING.md` | Workflow for RFCs, ADRs, and documentation updates |
| `DOCKER.md` | Docker containerization guide for development and deployment |
| `CLEANUP.md` | Resource optimization and cleanup strategies |
| `BACKSTAGE.md` | Backstage IDP integration guide |
| `catalog-info.yaml` | Backstage catalog definitions for framework components |
| `MANIFESTO/solid-ai-manifesto-v1.md` | Foundational manifesto outlining philosophy and roadmap |
| `DOCS/` | **Core Framework Documentation:**<br/>• `00-overview.md` — Framework introduction and transformation imperative<br/>• `01-principles.md` — 8 foundational principles (coherence, data contracts, AI-native, etc.)<br/>• `02-architecture.md` — 6-layer architecture (Purpose, Data Spine, Cognitive, Automation, Organizational, Governance)<br/>• `03-organizational-model.md` — Squads, pools, and adaptive topology (MIDORA)<br/>• `04-automation-sipoc.md` — SIPOC automation patterns and workflow design<br/>• `05-ai-agents.md` — Agent definitions, capabilities, and governance<br/>• `06-governance-ethics.md` — Ethics, compliance, accountability, transparency<br/>• `07-observability.md` — Monitoring, metrics, telemetry, and alerting<br/>• `08-human-ai-collaboration.md` — Where humans lead and AI supports<br/>• `09-whole-organization-transformation.md` — Bipolar organization problem and economics of AI-as-workforce<br/>• `10-role-hierarchy-human-ai.md` — 4-level progression (Assistant→Consultant→Specialist→Director) for humans and AI<br/>• `11-ai-native-agile.md` — Agile/Scrum/SAFe integration with AI-Native principles<br/>• `glossary.md` — Comprehensive terminology reference |
| `DIAGRAMS/` | Mermaid source files for architecture, organizational flows, and implementation patterns (10 diagrams) |
| `RFC/` | Request for Comments governing strategic evolutions |
| `ADR/` | Architecture Decision Records tracking technical choices |
| `PLAYBOOKS/` | Operational guides for squads, pools, operations, and AI integration |
| `ADOPTION/` | **NEW!** Ready-to-use adoption pack: prompts, templates, checklists, and reference cards |
| `mkdocs.yml` | MkDocs Material configuration for publishing the site |

## 🚀 New to SOLID.AI? Start Here!

**[Read the Quick Start Guide](QUICK-START-GUIDE.md)** — Learn SOLID.AI in 5 minutes and get 10 essential AI prompts to use today.

**Explore the Adoption Pack:**
- **[Reference Cards](ADOPTION/REFERENCE-CARDS/)** — AI prompting patterns for:
  - **Software Development:** Developers, PMs, Ops, Leadership
  - **Business Functions:** Sales, Administration, Marketing
  - **Production & Commerce:** Retail, Manufacturing
  - **Highly Regulated:** Healthcare, Financial Services
  - **Service Sectors:** Professional Services, Logistics, Human Resources
- **[Prompt Templates](ADOPTION/PROMPT-TEMPLATES/)** — Ready-to-use prompts for feature development, AI agents, data contracts, ethics, and retrospectives
- **[Checklists](ADOPTION/CHECKLISTS/)** — Step-by-step guides for AI integration, squad formation, data spine, and governance
- **[Templates](ADOPTION/TEMPLATES/)** — File templates for agent definitions, squad charters, data contracts, RFCs, and ADRs

## Quick Start

### Option 1: Using Docker (Recommended)
1. Clone the repository:
	```powershell
	git clone https://github.com/gusafr/midora-solid-ai.git
	cd midora-solid-ai
	```
2. Run with Docker Compose:
	```powershell
	docker-compose --profile dev up
	```
3. Open `http://localhost:8000` in your browser to explore the docs.

See [Docker Setup](docker.md) for production builds, deployment options, and CI/CD integration.

### Option 2: Local Python Environment
1. Clone the repository:
	```powershell
	git clone https://github.com/gusafr/midora-solid-ai.git
	cd midora-solid-ai
	```
2. Prepare the documentation site locally:
	```powershell
	python -m venv .venv
	.venv\Scripts\Activate.ps1
	pip install -r requirements.txt
	mkdocs serve
	```
3. Open `http://127.0.0.1:8000` in your browser to explore the docs.

## Contributing
We follow an RFC-first change management process. Please review `CONTRIBUTING.md` before proposing updates. Every change that touches the core architecture or governance must include an RFC or ADR reference.

## License
Distributed under the MIT License. See `LICENSE` for details.

## Stay Connected
- Discussions and RFC debates happen in GitHub Discussions (coming soon).
- Follow tagged releases as the manifesto and documentation evolve (v1.x, v2.x, etc.).