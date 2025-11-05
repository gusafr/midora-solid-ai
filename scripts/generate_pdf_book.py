#!/usr/bin/env python3
"""
SOLID.AI Framework - PDF Book Generator

Generates a professionally-styled PDF book from all framework documentation.
Modern, minimalist design with clean typography and embedded diagrams.

Usage:
    python scripts/generate_pdf_book.py [options]

Options:
    --output PATH          Output PDF path (default: output/solid-ai-framework.pdf)
    --include-playbooks    Include all playbooks (default: core docs only)
    --include-adoption     Include adoption pack materials
    --page-size SIZE       Page size: A4, Letter (default: A4)
    --color-scheme SCHEME  Scheme: color, grayscale (default: color)

Requirements:
    pip install weasyprint markdown pygments pillow
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import argparse
import re
import subprocess
from typing import List, Dict, Optional
import markdown
from markdown.extensions import codehilite, tables, toc, fenced_code, attr_list


class PDFBookGenerator:
    """Generate SOLID.AI framework PDF book with modern, minimalist styling."""
    
    def __init__(self, output_path: str = "output/solid-ai-framework.pdf",
                 include_playbooks: bool = False,
                 include_adoption: bool = False,
                 page_size: str = "A4",
                 color_scheme: str = "color"):
        self.output_path = Path(output_path)
        self.include_playbooks = include_playbooks
        self.include_adoption = include_adoption
        self.page_size = page_size
        self.color_scheme = color_scheme
        self.root_dir = Path(__file__).parent.parent
        self.docs_dir = self.root_dir / "DOCS"
        self.diagrams_dir = self.root_dir / "DIAGRAMS"
        self.playbooks_dir = self.root_dir / "PLAYBOOKS"
        self.adoption_dir = self.root_dir / "ADOPTION"
        
        # Ensure output directory exists
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        
    def generate(self):
        """Generate the complete PDF book."""
        print("🚀 SOLID.AI PDF Book Generator")
        print("=" * 60)
        print(f"Output: {self.output_path}")
        print(f"Page Size: {self.page_size}")
        print(f"Color Scheme: {self.color_scheme}")
        print(f"Include Playbooks: {self.include_playbooks}")
        print(f"Include Adoption: {self.include_adoption}")
        print()
        
        # Step 1: Collect all content
        print("📚 Step 1/5: Collecting content...")
        content_parts = self._collect_content()
        print(f"   ✓ Collected {len(content_parts)} sections")
        
        # Step 2: Convert Markdown to HTML
        print("📝 Step 2/5: Converting Markdown to HTML...")
        html_content = self._convert_to_html(content_parts)
        print(f"   ✓ Generated HTML ({len(html_content)} characters)")
        
        # Step 3: Apply CSS styling
        print("🎨 Step 3/5: Applying modern minimalist styling...")
        styled_html = self._apply_styling(html_content)
        print("   ✓ Applied CSS styling")
        
        # Step 4: Render Mermaid diagrams (if available)
        print("📊 Step 4/5: Processing diagrams...")
        final_html = self._process_diagrams(styled_html)
        print("   ✓ Processed diagrams")
        
        # Step 5: Generate PDF
        print("📄 Step 5/5: Generating PDF...")
        self._generate_pdf(final_html)
        print(f"   ✓ PDF saved to {self.output_path}")
        
        # Display summary
        file_size = self.output_path.stat().st_size / (1024 * 1024)  # MB
        print()
        print("=" * 60)
        print(f"✅ SUCCESS! PDF book generated")
        print(f"📦 File: {self.output_path}")
        print(f"💾 Size: {file_size:.2f} MB")
        print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
    def _collect_content(self) -> List[Dict[str, str]]:
        """Collect all markdown content in order."""
        parts = []
        
        # Cover page
        parts.append({
            'type': 'cover',
            'title': 'SOLID.AI Framework',
            'subtitle': 'The Organizational Nervous System for AI-Native Companies',
            'version': 'v1.0',
            'date': datetime.now().strftime('%B %Y'),
            'content': ''
        })
        
        # Table of contents placeholder
        parts.append({
            'type': 'toc',
            'title': 'Table of Contents',
            'content': ''  # Will be generated from parts
        })
        
        # Core documentation (DOCS 00-11 + glossary)
        print("   → Reading core documentation...")
        doc_files = [
            ('00-overview.md', 'Overview'),
            ('01-principles.md', 'Principles'),
            ('02-architecture.md', 'Architecture'),
            ('03-organizational-model.md', 'Organizational Model'),
            ('04-automation-sipoc.md', 'Automation & SIPOC'),
            ('05-ai-agents.md', 'AI Agents'),
            ('06-governance-ethics.md', 'Governance & Ethics'),
            ('07-observability.md', 'Observability'),
            ('08-human-ai-collaboration.md', 'Human-AI Collaboration'),
            ('09-whole-organization-transformation.md', 'Whole-Organization Transformation'),
            ('10-role-hierarchy-human-ai.md', 'Role Hierarchy'),
            ('11-ai-native-agile.md', 'AI-Native Agile'),
            ('glossary.md', 'Glossary'),
        ]
        
        for filename, title in doc_files:
            file_path = self.docs_dir / filename
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    parts.append({
                        'type': 'chapter',
                        'title': title,
                        'content': content,
                        'filename': filename
                    })
        
        # Manifesto
        manifesto_path = self.root_dir / "MANIFESTO" / "solid-ai-manifesto-v1.md"
        if manifesto_path.exists():
            print("   → Reading manifesto...")
            with open(manifesto_path, 'r', encoding='utf-8') as f:
                parts.append({
                    'type': 'chapter',
                    'title': 'SOLID.AI Manifesto',
                    'content': f.read(),
                    'filename': 'manifesto'
                })
        
        # Playbooks (if requested)
        if self.include_playbooks:
            print("   → Reading playbooks...")
            parts.append({
                'type': 'section_divider',
                'title': 'Implementation Playbooks',
                'content': ''
            })
            
            # Foundation Playbooks
            parts.append({
                'type': 'subsection_header',
                'title': 'Foundation',
                'content': ''
            })
            foundation_playbooks = [
                ('foundation/solid-ai-maturity-model.md', 'SOLID.AI Maturity Model: L0→L5 Evolution'),
            ]
            for path, title in foundation_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({
                            'type': 'chapter',
                            'title': title,
                            'content': f.read(),
                            'filename': path
                        })
            
            # Governance Playbooks
            parts.append({
                'type': 'subsection_header',
                'title': 'Governance',
                'content': ''
            })
            governance_playbooks = [
                ('governance/ai-governance-risk-assessment.md', 'AI Governance & Risk Assessment'),
            ]
            for path, title in governance_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({
                            'type': 'chapter',
                            'title': title,
                            'content': f.read(),
                            'filename': path
                        })
            
            # Implementation Playbooks
            parts.append({
                'type': 'subsection_header',
                'title': 'Implementation',
                'content': ''
            })
            implementation_playbooks = [
                ('implementation/process-mapping-sipoc-integration.md', 'Process Mapping & SIPOC Integration'),
                ('implementation/data-spine-analytics-insights.md', 'Data Spine Analytics & Insights'),
            ]
            for path, title in implementation_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({
                            'type': 'chapter',
                            'title': title,
                            'content': f.read(),
                            'filename': path
                        })
            
            # People & Culture Playbooks
            parts.append({
                'type': 'subsection_header',
                'title': 'People & Culture',
                'content': ''
            })
            people_culture_playbooks = [
                ('people-culture/organizational-scalability.md', 'Organizational Scalability'),
                ('people-culture/ai-learning-development.md', 'AI Learning & Development'),
                ('people-culture/ai-native-okrs-kpis.md', 'AI-Native OKRs & KPIs'),
            ]
            for path, title in people_culture_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({
                            'type': 'chapter',
                            'title': title,
                            'content': f.read(),
                            'filename': path
                        })
            
            # By Stage Playbooks
            parts.append({
                'type': 'subsection_header',
                'title': 'By Company Stage',
                'content': ''
            })
            stage_playbooks = [
                ('by-stage/startup-ai-native.md', 'Startup: AI-Native from Day One'),
                ('by-stage/sme-transformation.md', 'SME: Transformation Journey'),
            ]
            for path, title in stage_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({
                            'type': 'chapter',
                            'title': title,
                            'content': f.read(),
                            'filename': path
                        })
            
            # Organizational Patterns
            parts.append({
                'type': 'subsection_header',
                'title': 'Organizational Patterns',
                'content': ''
            })
            organizational_playbooks = [
                ('organizational/squads.md', 'Squads Implementation'),
                ('organizational/pools.md', 'Pools Implementation'),
                ('organizational/ai-integration.md', 'AI Integration'),
            ]
            for path, title in organizational_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({
                            'type': 'chapter',
                            'title': title,
                            'content': f.read(),
                            'filename': path
                        })
        
        # Adoption pack (if requested)
        if self.include_adoption:
            print("   → Reading adoption pack...")
            parts.append({
                'type': 'section_divider',
                'title': 'Adoption Pack',
                'content': ''
            })
            
            # Checklists - By Assessment & Planning
            parts.append({
                'type': 'subsection_header',
                'title': 'Checklists: Assessment & Planning',
                'content': ''
            })
            assessment_checklists = [
                ('CHECKLISTS/ai-maturity-assessment.md', 'AI Maturity Assessment'),
                ('CHECKLISTS/organizational-scalability-assessment.md', 'Organizational Scalability Assessment'),
                ('CHECKLISTS/learning-development-rollout.md', 'Learning & Development Rollout'),
                ('CHECKLISTS/okr-kpi-setup.md', 'OKR & KPI Setup'),
            ]
            for path, title in assessment_checklists:
                file_path = self.adoption_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({
                            'type': 'chapter',
                            'title': title,
                            'content': f.read(),
                            'filename': path
                        })
            
            # Checklists - By Implementation
            parts.append({
                'type': 'subsection_header',
                'title': 'Checklists: Implementation',
                'content': ''
            })
            implementation_checklists = [
                ('CHECKLISTS/ai-agent-integration.md', 'AI Agent Integration'),
                ('CHECKLISTS/squad-formation.md', 'Squad Formation'),
                ('CHECKLISTS/data-spine-implementation.md', 'Data Spine Implementation'),
                ('CHECKLISTS/governance-ethics-review.md', 'Governance & Ethics Review'),
            ]
            for path, title in implementation_checklists:
                file_path = self.adoption_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({
                            'type': 'chapter',
                            'title': title,
                            'content': f.read(),
                            'filename': path
                        })
            
            # Templates - Planning & Metrics
            parts.append({
                'type': 'subsection_header',
                'title': 'Templates: Planning & Metrics',
                'content': ''
            })
            
            # For templates, we'll include the markdown wrappers which contain
            # the YAML templates embedded with instructions
            template_note = '''
# About Templates

The following templates are provided in YAML format for easy copy-paste into your documentation and planning tools.

Each template includes:
- **Complete structure** ready to copy
- **Instructions** on how to fill it out
- **Examples** from real implementations
- **Related resources** for additional guidance

**Note:** These templates are shown in embedded format. For the raw YAML files, 
visit: `github.com/gusafr/midora-solid-ai/ADOPTION/TEMPLATES/`

---
            '''
            parts.append({
                'type': 'chapter',
                'title': 'Template Guide',
                'content': template_note,
                'filename': 'templates-intro'
            })
            
            # Note: We don't include the full YAML templates in PDF as they're very long
            # Instead, we include a reference/summary
            template_summary = '''
# Available Templates

The SOLID.AI Adoption Pack includes the following ready-to-use templates:

## 1. Risk Assessment Template (`risk-assessment-template.yaml`)

**Purpose:** AI governance risk assessment using Impact × Likelihood × Autonomy framework

**Includes:**
- Risk scoring framework (5 dimensions of impact)
- Automated tier calculation (maps 1-125 risk score to 5 tiers)
- Alert configuration (5 alert types)
- Mitigation planning
- Bias assessment
- Accountability assignment
- Complete example: Invoice processing automation

**Size:** ~500 lines  
**Format:** YAML

---

## 2. Learning Path Template (`learning-path-template.yaml`)

**Purpose:** Design 4-level AI learning & development paths by function

**Includes:**
- Level 1 Awareness (4h, 100% target)
- Level 2 Practitioner (20h, 60-80%, function-specific)
- Level 3 Power User (40h, 20-30%)
- Level 4 Specialist (100h+, 5-10%)
- Rollout plan (Pilot → Scale)
- Metrics framework
- Complete example: Sales function learning path

**Size:** ~700 lines  
**Format:** YAML

---

## 3. OKR Template (`okr-template.yaml`)

**Purpose:** AI-native OKRs with augmentation factors

**Includes:**
- Objective + 3-4 Key Results
- Augmentation factor calculation ((Human+AI) / Human-Only)
- 8 Universal AI Agent KPIs
- Weekly check-ins
- End-of-quarter review
- Complete examples: Sales and Engineering OKRs

**Size:** ~650 lines  
**Format:** YAML

---

## 4. Additional Templates

The Adoption Pack also includes:

- **Agent Definition Template** - Define AI agents with capabilities, data contracts, governance
- **Squad Charter Template** - Squad mission, composition, ways of working
- **Data Contract Template** - Schema, SLAs, lineage, observability
- **90-Day Transformation Plan** - Phased transformation roadmap
- **Role Hierarchy Matrix** - 4-level progression (Assistant → Specialist) for humans & AI
- **RFC Template** - Request for Comments for strategic changes
- **ADR Template** - Architecture Decision Records
- **AI-Native Sprint Template** - Sprint planning with AI integration

---

**To access these templates:**

1. **Online:** Visit `github.com/gusafr/midora-solid-ai/ADOPTION/TEMPLATES/`
2. **Command Line:** Clone the repo and navigate to `ADOPTION/TEMPLATES/`
3. **Website:** Visit the SOLID.AI documentation site

All templates are licensed under MIT and free to use, modify, and distribute.
            '''
            parts.append({
                'type': 'chapter',
                'title': 'Template Catalog',
                'content': template_summary,
                'filename': 'templates-catalog'
            })
        
        return parts
    
    def _convert_to_html(self, parts: List[Dict[str, str]]) -> str:
        """Convert all markdown parts to HTML."""
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.tables',
            'markdown.extensions.toc',
            'markdown.extensions.fenced_code',
            'markdown.extensions.attr_list',
            'markdown.extensions.sane_lists',
        ])
        
        html_parts = []
        
        for i, part in enumerate(parts):
            if part['type'] == 'cover':
                # Cover page HTML
                html_parts.append(self._generate_cover_html(part))
            elif part['type'] == 'toc':
                # TOC will be generated by CSS
                html_parts.append(self._generate_toc_html(parts))
            elif part['type'] == 'section_divider':
                # Section divider
                html_parts.append(f'<div class="section-divider"><h1>{part["title"]}</h1></div>')
            elif part['type'] == 'subsection_header':
                # Subsection header (within a section)
                html_parts.append(f'<div class="subsection-header"><h2>{part["title"]}</h2></div>')
            elif part['type'] == 'chapter':
                # Convert markdown to HTML
                chapter_html = md.convert(part['content'])
                html_parts.append(f'<div class="chapter" id="chapter-{i}">{chapter_html}</div>')
                md.reset()  # Reset for next chapter
        
        return '\n'.join(html_parts)
    
    def _generate_cover_html(self, part: Dict[str, str]) -> str:
        """Generate cover page HTML."""
        return f'''
        <div class="cover-page">
            <div class="cover-content">
                <div class="logo">SOLID.AI</div>
                <h1>{part['title']}</h1>
                <p class="subtitle">{part['subtitle']}</p>
                <div class="version-info">
                    <p class="version">{part['version']}</p>
                    <p class="date">{part['date']}</p>
                </div>
            </div>
            <div class="cover-footer">
                <p>Open Source Framework</p>
                <p>MIT License • github.com/gusafr/midora-solid-ai</p>
            </div>
        </div>
        '''
    
    def _generate_toc_html(self, parts: List[Dict[str, str]]) -> str:
        """Generate table of contents HTML."""
        toc_items = []
        chapter_num = 0
        
        for i, part in enumerate(parts):
            if part['type'] == 'chapter':
                chapter_num += 1
                toc_items.append(
                    f'<li><a href="#chapter-{i}">'
                    f'<span class="toc-number">{chapter_num}</span>'
                    f'<span class="toc-title">{part["title"]}</span>'
                    f'</a></li>'
                )
            elif part['type'] == 'section_divider':
                toc_items.append(
                    f'<li class="toc-section">{part["title"]}</li>'
                )
        
        return f'''
        <div class="toc-page">
            <h1>Table of Contents</h1>
            <ol class="toc-list">
                {''.join(toc_items)}
            </ol>
        </div>
        '''
    
    def _apply_styling(self, html_content: str) -> str:
        """Apply modern minimalist CSS styling."""
        css = self._get_modern_minimalist_css()
        
        full_html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SOLID.AI Framework</title>
    <style>
        {css}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
        '''
        
        return full_html
    
    def _get_modern_minimalist_css(self) -> str:
        """Generate modern minimalist CSS."""
        # Color palette
        if self.color_scheme == 'color':
            primary = '#6366f1'      # Indigo
            secondary = '#8b5cf6'    # Purple
            accent = '#06b6d4'       # Cyan
            text = '#1f2937'         # Dark gray
            text_light = '#6b7280'   # Medium gray
            bg = '#ffffff'
            bg_alt = '#f9fafb'
        else:  # grayscale
            primary = '#374151'
            secondary = '#4b5563'
            accent = '#6b7280'
            text = '#111827'
            text_light = '#6b7280'
            bg = '#ffffff'
            bg_alt = '#f9fafb'
        
        return f'''
        /* ===== Modern Minimalist Theme ===== */
        
        @page {{
            size: {self.page_size};
            margin: 2.5cm 2cm 2cm 2cm;
            
            @top-center {{
                content: "SOLID.AI Framework";
                font-family: 'Inter', -apple-system, sans-serif;
                font-size: 9pt;
                color: {text_light};
                border-bottom: 1px solid #e5e7eb;
                padding-bottom: 0.5cm;
            }}
            
            @bottom-right {{
                content: counter(page);
                font-family: 'Inter', -apple-system, sans-serif;
                font-size: 9pt;
                color: {text_light};
            }}
        }}
        
        @page :first {{
            margin: 0;
            @top-center {{ content: none; }}
            @bottom-right {{ content: none; }}
        }}
        
        @page toc {{
            @top-center {{ content: "Table of Contents"; }}
        }}
        
        /* ===== Typography ===== */
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            font-size: 10.5pt;
            line-height: 1.7;
            color: {text};
            background: {bg};
        }}
        
        /* ===== Cover Page ===== */
        
        .cover-page {{
            page: :first;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background: linear-gradient(135deg, {primary} 0%, {secondary} 100%);
            color: white;
            padding: 4cm 3cm;
            page-break-after: always;
        }}
        
        .cover-content {{
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}
        
        .logo {{
            font-size: 24pt;
            font-weight: 900;
            letter-spacing: -0.02em;
            margin-bottom: 4cm;
        }}
        
        .cover-page h1 {{
            font-size: 42pt;
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 1cm;
            letter-spacing: -0.03em;
        }}
        
        .subtitle {{
            font-size: 16pt;
            font-weight: 300;
            opacity: 0.9;
            max-width: 80%;
            line-height: 1.5;
        }}
        
        .version-info {{
            margin-top: 2cm;
            font-size: 12pt;
            opacity: 0.8;
        }}
        
        .version {{
            font-weight: 600;
        }}
        
        .cover-footer {{
            border-top: 1px solid rgba(255,255,255,0.2);
            padding-top: 1cm;
            font-size: 9pt;
            opacity: 0.7;
        }}
        
        /* ===== Table of Contents ===== */
        
        .toc-page {{
            page: toc;
            page-break-after: always;
            padding: 2cm 0;
        }}
        
        .toc-page h1 {{
            font-size: 28pt;
            font-weight: 700;
            color: {primary};
            margin-bottom: 1.5cm;
            letter-spacing: -0.02em;
        }}
        
        .toc-list {{
            list-style: none;
            counter-reset: toc-counter;
        }}
        
        .toc-list li {{
            margin-bottom: 0.8cm;
            counter-increment: toc-counter;
        }}
        
        .toc-list li a {{
            display: flex;
            text-decoration: none;
            color: {text};
            align-items: baseline;
        }}
        
        .toc-number {{
            font-weight: 600;
            color: {primary};
            min-width: 2cm;
            font-size: 11pt;
        }}
        
        .toc-number::before {{
            content: counter(toc-counter, decimal-leading-zero);
        }}
        
        .toc-title {{
            flex: 1;
            font-size: 12pt;
        }}
        
        .toc-section {{
            font-weight: 700;
            color: {primary};
            font-size: 14pt;
            margin-top: 1.5cm;
            margin-bottom: 0.5cm;
            border-bottom: 2px solid {primary};
            padding-bottom: 0.3cm;
        }}
        
        /* ===== Section Divider ===== */
        
        .section-divider {{
            page-break-before: always;
            page-break-after: always;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: {bg_alt};
        }}
        
        .section-divider h1 {{
            font-size: 36pt;
            font-weight: 800;
            color: {primary};
            text-align: center;
            letter-spacing: -0.02em;
        }}
        
        /* ===== Subsection Header ===== */
        
        .subsection-header {{
            page-break-before: always;
            padding: 1.5cm 0 1cm 0;
            border-bottom: 3px solid {primary};
            margin-bottom: 1cm;
        }}
        
        .subsection-header h2 {{
            font-size: 20pt;
            font-weight: 700;
            color: {primary};
            letter-spacing: -0.02em;
            margin: 0;
        }}
        
        /* ===== Chapters ===== */
        
        .chapter {{
            page-break-before: always;
            padding-top: 1cm;
        }}
        
        .chapter h1 {{
            font-size: 24pt;
            font-weight: 700;
            color: {primary};
            margin-bottom: 0.8cm;
            margin-top: 1cm;
            letter-spacing: -0.02em;
            border-bottom: 3px solid {primary};
            padding-bottom: 0.4cm;
        }}
        
        .chapter h2 {{
            font-size: 18pt;
            font-weight: 600;
            color: {text};
            margin-top: 1.2cm;
            margin-bottom: 0.6cm;
            letter-spacing: -0.01em;
        }}
        
        .chapter h3 {{
            font-size: 14pt;
            font-weight: 600;
            color: {text};
            margin-top: 1cm;
            margin-bottom: 0.5cm;
        }}
        
        .chapter h4 {{
            font-size: 12pt;
            font-weight: 600;
            color: {text_light};
            margin-top: 0.8cm;
            margin-bottom: 0.4cm;
        }}
        
        .chapter p {{
            margin-bottom: 0.6cm;
            text-align: justify;
        }}
        
        .chapter ul, .chapter ol {{
            margin-left: 1cm;
            margin-bottom: 0.6cm;
        }}
        
        .chapter li {{
            margin-bottom: 0.3cm;
        }}
        
        /* ===== Code Blocks ===== */
        
        pre {{
            background: {bg_alt};
            border-left: 4px solid {primary};
            padding: 0.6cm;
            margin: 0.6cm 0;
            border-radius: 0.2cm;
            overflow-x: auto;
            font-family: 'Fira Code', 'Courier New', monospace;
            font-size: 9pt;
            line-height: 1.5;
        }}
        
        code {{
            background: {bg_alt};
            padding: 0.1cm 0.2cm;
            border-radius: 0.1cm;
            font-family: 'Fira Code', 'Courier New', monospace;
            font-size: 9pt;
            color: {secondary};
        }}
        
        pre code {{
            background: none;
            padding: 0;
        }}
        
        /* ===== Tables ===== */
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 0.8cm 0;
            font-size: 9.5pt;
        }}
        
        th {{
            background: {primary};
            color: white;
            padding: 0.4cm;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 0.4cm;
            border-bottom: 1px solid #e5e7eb;
        }}
        
        tr:nth-child(even) {{
            background: {bg_alt};
        }}
        
        /* ===== Blockquotes ===== */
        
        blockquote {{
            border-left: 4px solid {accent};
            padding-left: 0.8cm;
            margin: 0.8cm 0;
            color: {text_light};
            font-style: italic;
        }}
        
        /* ===== Links ===== */
        
        a {{
            color: {primary};
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        /* ===== Utility Classes ===== */
        
        .page-break {{
            page-break-after: always;
        }}
        
        .no-break {{
            page-break-inside: avoid;
        }}
        
        hr {{
            border: none;
            border-top: 1px solid #e5e7eb;
            margin: 1cm 0;
        }}
        
        strong {{
            font-weight: 600;
            color: {text};
        }}
        
        em {{
            font-style: italic;
            color: {text_light};
        }}
        '''
    
    def _process_diagrams(self, html: str) -> str:
        """Process Mermaid diagrams (placeholder for diagram rendering)."""
        # For now, replace mermaid blocks with placeholder
        # In production, you'd render diagrams to images using mermaid-cli
        
        diagram_placeholder = '''
        <div class="diagram-placeholder" style="
            background: #f9fafb;
            border: 2px dashed #d1d5db;
            padding: 2cm;
            text-align: center;
            margin: 1cm 0;
            border-radius: 0.2cm;
        ">
            <p style="color: #6b7280; font-style: italic;">
                📊 Diagram rendered in online version
            </p>
            <p style="color: #9ca3af; font-size: 9pt; margin-top: 0.3cm;">
                View full diagrams at: github.com/gusafr/midora-solid-ai/DIAGRAMS
            </p>
        </div>
        '''
        
        # Replace mermaid code blocks
        html = re.sub(
            r'<code class="language-mermaid">.*?</code>',
            diagram_placeholder,
            html,
            flags=re.DOTALL
        )
        
        return html
    
    def _generate_pdf(self, html: str):
        """Generate PDF from HTML using WeasyPrint."""
        try:
            from weasyprint import HTML, CSS
            
            # Create temporary HTML file
            temp_html = self.output_path.parent / "temp_book.html"
            with open(temp_html, 'w', encoding='utf-8') as f:
                f.write(html)
            
            # Generate PDF
            HTML(filename=str(temp_html)).write_pdf(str(self.output_path))
            
            # Clean up temp file
            temp_html.unlink()
            
        except ImportError:
            print("❌ ERROR: WeasyPrint not installed")
            print("   Install with: pip install weasyprint")
            sys.exit(1)
        except Exception as e:
            print(f"❌ ERROR generating PDF: {e}")
            sys.exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate SOLID.AI Framework PDF Book',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Generate core documentation only
  python scripts/generate_pdf_book.py
  
  # Include playbooks
  python scripts/generate_pdf_book.py --include-playbooks
  
  # Full book with adoption pack
  python scripts/generate_pdf_book.py --include-playbooks --include-adoption
  
  # Grayscale for printing
  python scripts/generate_pdf_book.py --color-scheme grayscale
        '''
    )
    
    parser.add_argument(
        '--output',
        default='output/solid-ai-framework.pdf',
        help='Output PDF path (default: output/solid-ai-framework.pdf)'
    )
    parser.add_argument(
        '--include-playbooks',
        action='store_true',
        help='Include playbooks in the book'
    )
    parser.add_argument(
        '--include-adoption',
        action='store_true',
        help='Include adoption pack materials'
    )
    parser.add_argument(
        '--page-size',
        choices=['A4', 'Letter'],
        default='A4',
        help='Page size (default: A4)'
    )
    parser.add_argument(
        '--color-scheme',
        choices=['color', 'grayscale'],
        default='color',
        help='Color scheme (default: color)'
    )
    
    args = parser.parse_args()
    
    # Generate PDF
    generator = PDFBookGenerator(
        output_path=args.output,
        include_playbooks=args.include_playbooks,
        include_adoption=args.include_adoption,
        page_size=args.page_size,
        color_scheme=args.color_scheme
    )
    
    generator.generate()


if __name__ == '__main__':
    main()
