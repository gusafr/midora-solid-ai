# solid.ai — Organizational Nervous System for AI-Native Companies

solid.ai is the open framework for designing intelligent, ethical, and adaptive organizations where humans and AI co-create value. The repository captures the reference model, governance patterns, and playbooks required to connect purpose, data, intelligence, automation, and organizational design into one cohesive operating system.

## Why solid.ai
- Align strategic intent with automated execution through a purpose-first architecture.
- Treat AI agents as accountable teammates inside transparent, observable systems.
- Grow organizations as living ecosystems that continuously learn and improve.

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
| `LICENSE` | MIT License granting open-source usage |
| `CODE_OF_CONDUCT.md` | Community expectations and escalation paths |
| `CONTRIBUTING.md` | Workflow for RFCs, ADRs, and documentation updates |
| `DOCKER.md` | Docker containerization guide for development and deployment |
| `CLEANUP.md` | Resource optimization and cleanup strategies |
| `MANIFESTO/solid-ai-manifesto-v1.md` | Foundational manifesto outlining philosophy and roadmap |
| `DOCS/` | Modular documentation covering principles, architecture, governance, and glossary |
| `DIAGRAMS/` | Mermaid source files for architecture, organizational flows, and implementation patterns (10 diagrams) |
| `RFC/` | Request for Comments governing strategic evolutions |
| `ADR/` | Architecture Decision Records tracking technical choices |
| `PLAYBOOKS/` | Operational guides for squads, pools, operations, and AI integration |
| `mkdocs.yml` | MkDocs Material configuration for publishing the site |

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

See [DOCKER.md](DOCKER.md) for production builds, deployment options, and CI/CD integration.

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