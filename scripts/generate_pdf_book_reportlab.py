#!/usr/bin/env python3
"""
SOLID.AI Framework - PDF Book Generator (Cross-Platform)

Generates a professionally-styled PDF book using ReportLab (pure Python, no system deps).
Works out-of-the-box on Windows, macOS, and Linux.

Usage:
    python scripts/generate_pdf_book_reportlab.py [options]

Options:
    --output PATH          Output PDF path (default: output/solid-ai-framework.pdf)
    --include-playbooks    Include all playbooks (default: core docs only)
    --include-adoption     Include adoption pack materials
    --page-size SIZE       Page size: A4, Letter (default: A4)
    --color-scheme SCHEME  Scheme: color, grayscale (default: color)

Requirements:
    pip install reportlab markdown2 pygments
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import argparse
import re
from typing import List, Dict, Optional

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm, mm
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
        Preformatted, Image, KeepTogether, ListFlowable, ListItem, HRFlowable
    )
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
    from reportlab.pdfgen import canvas
    import markdown2
except ImportError as e:
    print(f"❌ ERROR: Missing dependency - {e}")
    print("\nInstall required packages:")
    print("  pip install reportlab markdown2 pygments")
    sys.exit(1)

# Import SVG helper (optional dependency)
try:
    from svg_helper import create_diagram_flowable, check_dependencies
    SVG_SUPPORT = check_dependencies()
except ImportError:
    SVG_SUPPORT = False
    print("ℹ️  Info: SVG support not available (install svglib for diagram embedding)")


class PDFBookGenerator:
    """Generate SOLID.AI framework PDF book using ReportLab (cross-platform)."""
    
    def __init__(self, output_path: str = "output/solid-ai-framework.pdf",
                 include_playbooks: bool = False,
                 include_adoption: bool = False,
                 page_size: str = "A4",
                 color_scheme: str = "color"):
        self.output_path = Path(output_path)
        self.include_playbooks = include_playbooks
        self.include_adoption = include_adoption
        self.page_size = A4 if page_size == "A4" else letter
        self.color_scheme = color_scheme
        self.root_dir = Path(__file__).parent.parent
        self.docs_dir = self.root_dir / "DOCS"
        self.diagrams_dir = self.root_dir / "DIAGRAMS"
        self.playbooks_dir = self.root_dir / "PLAYBOOKS"
        self.adoption_dir = self.root_dir / "ADOPTION"
        
        # Ensure output directory exists
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Setup colors
        if color_scheme == 'color':
            self.primary = colors.HexColor('#6366f1')      # Indigo
            self.secondary = colors.HexColor('#8b5cf6')    # Purple
            self.accent = colors.HexColor('#06b6d4')       # Cyan
            self.text = colors.HexColor('#1f2937')
            self.text_light = colors.HexColor('#6b7280')
        else:  # grayscale
            self.primary = colors.HexColor('#374151')
            self.secondary = colors.HexColor('#4b5563')
            self.accent = colors.HexColor('#6b7280')
            self.text = colors.HexColor('#111827')
            self.text_light = colors.HexColor('#6b7280')
        
        # Setup styles
        self._setup_styles()
        
    def _setup_styles(self):
        """Setup paragraph styles."""
        self.styles = getSampleStyleSheet()
        
        # Cover title
        self.styles.add(ParagraphStyle(
            name='CoverTitle',
            parent=self.styles['Heading1'],
            fontSize=36,
            textColor=colors.white,
            spaceAfter=20,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Cover subtitle
        self.styles.add(ParagraphStyle(
            name='CoverSubtitle',
            parent=self.styles['Normal'],
            fontSize=14,
            textColor=colors.white,
            spaceAfter=12,
            alignment=TA_CENTER,
            fontName='Helvetica'
        ))
        
        # Chapter title
        self.styles.add(ParagraphStyle(
            name='ChapterTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=self.primary,
            spaceAfter=20,
            spaceBefore=30,
            fontName='Helvetica-Bold',
            borderWidth=3,
            borderColor=self.primary,
            borderPadding=10,
            borderRadius=0
        ))
        
        # Custom Heading 2
        self.styles.add(ParagraphStyle(
            name='CustomHeading2',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=self.text,
            spaceAfter=12,
            spaceBefore=20,
            fontName='Helvetica-Bold'
        ))
        
        # Custom Heading 3
        self.styles.add(ParagraphStyle(
            name='CustomHeading3',
            parent=self.styles['Heading3'],
            fontSize=13,
            textColor=self.text,
            spaceAfter=10,
            spaceBefore=15,
            fontName='Helvetica-Bold'
        ))
        
        # Custom Body text
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=self.text,
            spaceAfter=12,
            alignment=TA_JUSTIFY,
            fontName='Helvetica',
            leading=14
        ))
        
        # Custom Code
        self.styles.add(ParagraphStyle(
            name='CustomCode',
            parent=self.styles['Code'],
            fontSize=8,
            textColor=self.secondary,
            fontName='Courier',
            leftIndent=20,
            rightIndent=20,
            spaceAfter=12,
            backColor=colors.HexColor('#f9fafb')
        ))
        
    def generate(self):
        """Generate the complete PDF book."""
        print("🚀 SOLID.AI PDF Book Generator (ReportLab)")
        print("=" * 60)
        print(f"Output: {self.output_path}")
        print(f"Page Size: {'A4' if self.page_size == A4 else 'Letter'}")
        print(f"Color Scheme: {self.color_scheme}")
        print(f"Include Playbooks: {self.include_playbooks}")
        print(f"Include Adoption: {self.include_adoption}")
        print()
        
        # Step 1: Collect all content
        print("📚 Step 1/4: Collecting content...")
        content_parts = self._collect_content()
        print(f"   ✓ Collected {len(content_parts)} sections")
        
        # Step 2: Convert to ReportLab flowables
        print("📝 Step 2/4: Converting to PDF elements...")
        story = self._build_story(content_parts)
        print(f"   ✓ Generated {len(story)} PDF elements")
        
        # Step 3: Generate PDF
        print("📄 Step 3/4: Generating PDF...")
        self._generate_pdf(story)
        print(f"   ✓ PDF saved to {self.output_path}")
        
        # Step 4: Display summary
        print("✨ Step 4/4: Finalizing...")
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
            'content': ''
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
            
            # === Foundation ===
            parts.append({'type': 'subsection_header', 'title': 'Foundation'})
            foundation_playbooks = [
                ('foundation/solid-ai-maturity-model.md', 'SOLID.AI Maturity Model: L0→L5 Evolution'),
            ]
            for path, title in foundation_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({'type': 'chapter', 'title': title, 'content': f.read(), 'filename': path})
            
            # === Governance ===
            parts.append({'type': 'subsection_header', 'title': 'Governance & Risk'})
            governance_playbooks = [
                ('governance/ai-governance-risk-assessment.md', 'AI Governance & Risk Assessment'),
            ]
            for path, title in governance_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({'type': 'chapter', 'title': title, 'content': f.read(), 'filename': path})
            
            # === Implementation ===
            parts.append({'type': 'subsection_header', 'title': 'Implementation & Operations'})
            implementation_playbooks = [
                ('implementation/process-mapping-sipoc-integration.md', 'Process Mapping & SIPOC Integration'),
                ('implementation/data-spine-analytics-insights.md', 'Data Spine Analytics & Insights'),
            ]
            for path, title in implementation_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({'type': 'chapter', 'title': title, 'content': f.read(), 'filename': path})
            
            # === People & Culture ===
            parts.append({'type': 'subsection_header', 'title': 'People & Culture'})
            people_culture_playbooks = [
                ('people-culture/organizational-scalability.md', 'Organizational Scalability: Breaking Through Ceiling'),
                ('people-culture/ai-learning-development.md', 'AI Learning & Development: Continuous Upskilling'),
                ('people-culture/ai-native-okrs-kpis.md', 'AI-Native OKRs & KPIs: Measuring AI Impact'),
            ]
            for path, title in people_culture_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({'type': 'chapter', 'title': title, 'content': f.read(), 'filename': path})
            
            # === By Stage ===
            parts.append({'type': 'subsection_header', 'title': 'By Organization Stage'})
            by_stage_playbooks = [
                ('by-stage/startup-ai-native.md', 'Startup: AI-Native from Day One'),
                ('by-stage/sme-transformation.md', 'SME: Transformation Journey'),
            ]
            for path, title in by_stage_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({'type': 'chapter', 'title': title, 'content': f.read(), 'filename': path})
            
            # === Organizational ===
            parts.append({'type': 'subsection_header', 'title': 'Organizational Patterns'})
            organizational_playbooks = [
                ('organizational/squads.md', 'Squads Implementation'),
                ('organizational/pools.md', 'Pools Implementation'),
                ('organizational/ai-integration.md', 'AI Integration'),
            ]
            for path, title in organizational_playbooks:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({'type': 'chapter', 'title': title, 'content': f.read(), 'filename': path})
        
        # Adoption Pack (if requested)
        if self.include_adoption:
            print("   → Reading adoption pack...")
            parts.append({
                'type': 'section_divider',
                'title': 'Adoption Pack',
                'content': ''
            })
            
            # === Assessment & Planning Checklists ===
            parts.append({'type': 'subsection_header', 'title': 'Assessment & Planning Checklists'})
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
                        parts.append({'type': 'chapter', 'title': title, 'content': f.read(), 'filename': path})
            
            # === Implementation Checklists ===
            parts.append({'type': 'subsection_header', 'title': 'Implementation Checklists'})
            implementation_checklists = [
                ('CHECKLISTS/squad-setup.md', 'Squad Setup'),
                ('CHECKLISTS/pool-setup.md', 'Pool Setup'),
                ('CHECKLISTS/sipoc-implementation.md', 'SIPOC Implementation'),
                ('CHECKLISTS/governance-ethics-review.md', 'Governance & Ethics Review'),
            ]
            for path, title in implementation_checklists:
                file_path = self.adoption_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({'type': 'chapter', 'title': title, 'content': f.read(), 'filename': path})
            
            # === Template Catalog ===
            parts.append({'type': 'subsection_header', 'title': 'Template Catalog'})
            template_summary = '''
# Template Catalog

The SOLID.AI Adoption Pack includes 11 ready-to-use YAML templates for implementing key framework components.

## Organizational Structure Templates

### 1. Squad Template
**File:** `ADOPTION/TEMPLATES/squad-template.yaml`
**Purpose:** Configure autonomous cross-functional teams
**Key Sections:** Mission, roles, technologies, OKRs, rituals, dependencies

### 2. Pool Template
**File:** `ADOPTION/TEMPLATES/pool-template.yaml`
**Purpose:** Define specialized capability centers
**Key Sections:** Skills, resource allocation, engagement models, evolution paths

## Planning & Metrics Templates

### 3. Risk Assessment Template
**File:** `ADOPTION/TEMPLATES/risk-assessment-template.yaml`
**Purpose:** Comprehensive AI governance risk framework
**Key Sections:** Risk scoring (5 dimensions), alert levels, mitigation strategies, compliance tracking
**NEW:** Integrated multi-factor risk scoring with impact/likelihood/velocity assessment

### 4. Learning Path Template
**File:** `ADOPTION/TEMPLATES/learning-path-template.yaml`
**Purpose:** Structured AI upskilling curriculum
**Key Sections:** Role-based tracks, competency progression (L0-L5), learning resources, assessments
**NEW:** Aligns with SOLID.AI Maturity Model levels for systematic capability development

### 5. OKR Template
**File:** `ADOPTION/TEMPLATES/okr-template.yaml`
**Purpose:** AI-native objectives and key results tracking
**Key Sections:** AI impact metrics, augmentation factors, human-AI collaboration KPIs, quarterly goals
**NEW:** Includes human-AI collaboration multipliers and augmentation factor calculations

### 6. SIPOC Template
**File:** `ADOPTION/TEMPLATES/sipoc-template.yaml`
**Purpose:** Document process flows for automation opportunities
**Key Sections:** Suppliers, inputs, process steps, outputs, customers, automation potential

## Governance Templates

### 7. Governance Policy Template
**File:** `ADOPTION/TEMPLATES/governance-policy-template.yaml`
**Purpose:** Establish AI governance guardrails
**Key Sections:** Principles, approval workflows, compliance requirements, monitoring

### 8. Ethics Review Template
**File:** `ADOPTION/TEMPLATES/ethics-review-template.yaml`
**Purpose:** Evaluate AI systems for ethical concerns
**Key Sections:** Bias assessment, transparency, accountability, fairness metrics

## Sprint Templates

### 9. Sprint Planning Template
**File:** `ADOPTION/TEMPLATES/sprint-planning-template.yaml`
**Purpose:** AI-native sprint structure
**Key Sections:** Goals, capacity planning, human-AI task distribution, velocity tracking

### 10. Retrospective Template
**File:** `ADOPTION/TEMPLATES/retrospective-template.yaml`
**Purpose:** Continuous improvement for AI-augmented teams
**Key Sections:** What worked, blockers, action items, AI effectiveness review

### 11. Roadmap Template
**File:** `ADOPTION/TEMPLATES/roadmap-template.yaml`
**Purpose:** Strategic planning with AI transformation milestones
**Key Sections:** Quarterly objectives, capability buildout, dependency management

---

**Download Location:** All templates available at `https://github.com/gusafr/midora-solid-ai/tree/main/ADOPTION/TEMPLATES`

**Usage:** Copy YAML templates, customize for your context, track in version control alongside code.
'''
            parts.append({'type': 'chapter', 'title': 'Available Templates', 'content': template_summary, 'filename': 'templates'})
        
        return parts
    
    def _build_story(self, parts: List[Dict[str, str]]) -> List:
        """Build ReportLab story from content parts."""
        story = []
        
        for part in parts:
            if part['type'] == 'cover':
                story.extend(self._create_cover(part))
            elif part['type'] == 'toc':
                story.extend(self._create_toc(parts))
            elif part['type'] == 'section_divider':
                story.extend(self._create_section_divider(part))
            elif part['type'] == 'subsection_header':
                story.extend(self._create_subsection_header(part))
            elif part['type'] == 'chapter':
                story.extend(self._create_chapter(part))
        
        return story
    
    def _create_cover(self, part: Dict[str, str]) -> List:
        """Create cover page."""
        elements = []
        
        # Spacer to center content vertically
        elements.append(Spacer(1, 8*cm))
        
        # Title
        title = Paragraph(f"<b>{part['title']}</b>", self.styles['CoverTitle'])
        elements.append(title)
        elements.append(Spacer(1, 1*cm))
        
        # Subtitle
        subtitle = Paragraph(part['subtitle'], self.styles['CoverSubtitle'])
        elements.append(subtitle)
        elements.append(Spacer(1, 3*cm))
        
        # Version info
        version = Paragraph(f"<b>{part['version']}</b> • {part['date']}", self.styles['CoverSubtitle'])
        elements.append(version)
        
        # Page break
        elements.append(PageBreak())
        
        return elements
    
    def _create_toc(self, parts: List[Dict[str, str]]) -> List:
        """Create table of contents."""
        elements = []
        
        # TOC title
        elements.append(Paragraph("<b>Table of Contents</b>", self.styles['ChapterTitle']))
        elements.append(Spacer(1, 1*cm))
        
        # TOC entries
        chapter_num = 0
        for part in parts:
            if part['type'] == 'chapter':
                chapter_num += 1
                toc_entry = Paragraph(
                    f"<b>{chapter_num:02d}.</b> {part['title']}",
                    self.styles['CustomBody']
                )
                elements.append(toc_entry)
                elements.append(Spacer(1, 0.3*cm))
        
        elements.append(PageBreak())
        
        return elements
    
    def _create_section_divider(self, part: Dict[str, str]) -> List:
        """Create section divider page."""
        elements = []
        
        elements.append(PageBreak())
        elements.append(Spacer(1, 10*cm))
        
        title = Paragraph(
            f"<b>{part['title']}</b>",
            self.styles['ChapterTitle']
        )
        elements.append(title)
        
        elements.append(PageBreak())
        
        return elements
    
    def _create_subsection_header(self, part: Dict[str, str]) -> List:
        """Create subsection header (lighter than section divider, no full page)."""
        elements = []
        
        # Add spacing and horizontal rule
        elements.append(Spacer(1, 1.5*cm))
        elements.append(HRFlowable(width="100%", thickness=2, color=self.primary, spaceAfter=0.5*cm))
        
        # Subsection title
        title = Paragraph(
            f"<b>{part['title']}</b>",
            self.styles['Heading1']
        )
        elements.append(title)
        elements.append(Spacer(1, 0.8*cm))
        
        return elements
    
    def _create_chapter(self, part: Dict[str, str]) -> List:
        """Create chapter from markdown content with full markdown support."""
        elements = []
        
        # Chapter break
        elements.append(PageBreak())
        
        # Chapter title (with numbering if it's a numbered chapter)
        chapter_title = part['title']
        if part.get('filename', '').startswith(('00-', '01-', '02-', '03-', '04-', '05-', '06-', '07-', '08-', '09-', '10-', '11-')):
            chapter_num = part['filename'][:2]
            chapter_title = f"{chapter_num}. {part['title']}"
        
        elements.append(Paragraph(f"<b>{chapter_title}</b>", self.styles['ChapterTitle']))
        elements.append(Spacer(1, 0.5*cm))
        
        # Process markdown content with enhanced parsing
        lines = part['content'].split('\n')
        
        in_code_block = False
        in_table = False
        in_list = False
        in_blockquote = False
        code_lines = []
        table_lines = []
        list_items = []
        blockquote_lines = []
        current_list_type = None  # 'bullet' or 'numbered'
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Code blocks
            if line.strip().startswith('```'):
                if in_code_block:
                    # End code block
                    code_text = '\n'.join(code_lines)
                    elements.append(Preformatted(code_text, self.styles['CustomCode']))
                    elements.append(Spacer(1, 0.3*cm))
                    code_lines = []
                in_code_block = not in_code_block
                i += 1
                continue
            
            if in_code_block:
                code_lines.append(line)
                i += 1
                continue
            
            # Markdown tables (detect | at start or in line)
            if '|' in line and not in_table:
                # Start collecting table
                in_table = True
                table_lines = [line]
                i += 1
                continue
            
            if in_table:
                if '|' in line or line.strip().startswith('|'):
                    table_lines.append(line)
                    i += 1
                    continue
                else:
                    # End of table, render it
                    if table_lines:
                        table_element = self._create_table(table_lines)
                        if table_element:
                            elements.append(table_element)
                            elements.append(Spacer(1, 0.4*cm))
                    table_lines = []
                    in_table = False
                    # Don't increment i, process current line
                    continue
            
            # Bullet lists (-, *, +)
            if re.match(r'^\s*[-*+]\s+', line):
                if not in_list or current_list_type != 'bullet':
                    # Start new bullet list or switch from numbered
                    if in_list and list_items:
                        # Finish previous list
                        elements.extend(self._create_list(list_items, current_list_type))
                        list_items = []
                    in_list = True
                    current_list_type = 'bullet'
                
                # Extract bullet item
                indent = len(line) - len(line.lstrip())
                content = re.sub(r'^\s*[-*+]\s+', '', line)
                list_items.append({'indent': indent, 'content': content})
                i += 1
                continue
            
            # Numbered lists (1. 2. etc.)
            if re.match(r'^\s*\d+\.\s+', line):
                if not in_list or current_list_type != 'numbered':
                    # Start new numbered list or switch from bullet
                    if in_list and list_items:
                        # Finish previous list
                        elements.extend(self._create_list(list_items, current_list_type))
                        list_items = []
                    in_list = True
                    current_list_type = 'numbered'
                
                # Extract numbered item
                indent = len(line) - len(line.lstrip())
                content = re.sub(r'^\s*\d+\.\s+', '', line)
                list_items.append({'indent': indent, 'content': content})
                i += 1
                continue
            
            # If we were in a list and this line doesn't continue it
            if in_list:
                # Empty line within list - allow it
                if not line.strip():
                    i += 1
                    continue
                # Non-list line that's not empty - end the list
                else:
                    # End the list
                    elements.extend(self._create_list(list_items, current_list_type))
                    list_items = []
                    in_list = False
                    current_list_type = None
                    # Continue to process current line (don't increment i)
                    # Fall through to process the line below
            
            # Blockquotes (> )
            if line.strip().startswith('> '):
                if not in_blockquote:
                    in_blockquote = True
                    blockquote_lines = []
                content = line.strip()[2:]  # Remove "> "
                blockquote_lines.append(content)
                i += 1
                continue
            
            if in_blockquote:
                if line.strip().startswith('> '):
                    content = line.strip()[2:]
                    blockquote_lines.append(content)
                    i += 1
                    continue
                else:
                    # End blockquote
                    elements.extend(self._create_blockquote(blockquote_lines))
                    blockquote_lines = []
                    in_blockquote = False
                    # Don't increment i, process current line (fall through)
            
            # Handle diagram placeholders
            if '--8<--' in line:
                # Extract diagram filename
                match = re.search(r'--8<--\s*"?([^"]+\.mmd)"?', line)
                if match:
                    diagram_path = match.group(1)
                    
                    # Try to embed actual SVG/PNG diagram
                    if SVG_SUPPORT:
                        diagram_flowable, diagram_name = create_diagram_flowable(
                            diagram_path, self.diagrams_dir, width=13*cm  # Fit within margins
                        )
                        
                        if diagram_flowable:
                            # Successfully loaded diagram - embed it
                            elements.append(Spacer(1, 0.3*cm))
                            
                            # Diagram title
                            title_text = f"📊 <b>{diagram_name}</b>"
                            elements.append(Paragraph(title_text, self.styles['CustomHeading3']))
                            elements.append(Spacer(1, 0.2*cm))
                            
                            # Add the actual diagram
                            elements.append(diagram_flowable)
                            elements.append(Spacer(1, 0.3*cm))
                            
                            i += 1
                            continue
                    
                    # Fallback: Use placeholder if SVG not available
                    diagram_name = diagram_path.split('/')[-1].replace('.mmd', '').replace('-', ' ').title()
                    
                    # Add visual placeholder box
                    elements.append(Spacer(1, 0.3*cm))
                    
                    # Diagram title with icon
                    placeholder_text = f"📊 <b>Diagram: {diagram_name}</b>"
                    elements.append(Paragraph(placeholder_text, self.styles['CustomHeading3']))
                    
                    # Reference note
                    note_text = (
                        f'<i>View this interactive diagram online at:</i><br/>'
                        f'<font color="#8b5cf6">https://gusafr.github.io/midora-solid-ai/diagrams/</font>'
                    )
                    elements.append(Paragraph(note_text, self.styles['CustomBody']))
                    elements.append(Spacer(1, 0.3*cm))
                i += 1
                continue
            
            # Horizontal rules (---, ***, ___)
            if re.match(r'^\s*(-{3,}|\*{3,}|_{3,})\s*$', line):
                elements.append(Spacer(1, 0.3*cm))
                # Create a horizontal line
                from reportlab.platypus import HRFlowable
                elements.append(HRFlowable(width="80%", thickness=1, color=self.text_light, 
                                          spaceAfter=0.3*cm, spaceBefore=0.3*cm))
                i += 1
                continue
            
            # Headers
            if line.startswith('# '):
                i += 1
                continue  # Skip H1 (already have chapter title)
            elif line.startswith('## '):
                text = line[3:].strip()
                elements.append(Spacer(1, 0.5*cm))
                elements.append(Paragraph(f"<b>{text}</b>", self.styles['CustomHeading2']))
                i += 1
                continue
            elif line.startswith('### '):
                text = line[4:].strip()
                elements.append(Spacer(1, 0.3*cm))
                elements.append(Paragraph(f"<b>{text}</b>", self.styles['CustomHeading3']))
                i += 1
                continue
            
            # Callout boxes (See also:, Next Steps:, See:, etc.)
            if re.match(r'^(See also:|Next Steps:|See:|\*\*See also:\*\*|\*\*Next Steps:\*\*|\*\*See:\*\*)', line, re.IGNORECASE):
                # Collect callout content
                callout_lines = [line]
                i += 1
                while i < len(lines) and lines[i].strip() and not lines[i].startswith('#'):
                    callout_lines.append(lines[i])
                    i += 1
                    if i < len(lines) and not lines[i].strip():
                        break
                
                elements.extend(self._create_callout(callout_lines))
                continue
            
            # Empty lines
            if not line.strip():
                i += 1
                continue
            
            # Regular paragraph
            text = line.strip()
            if text:
                # Clean up markdown formatting
                text = self._format_inline_markdown(text)
                elements.append(Paragraph(text, self.styles['CustomBody']))
            
            i += 1
        
        # Handle any remaining open blocks
        if in_code_block and code_lines:
            code_text = '\n'.join(code_lines)
            elements.append(Preformatted(code_text, self.styles['CustomCode']))
        
        if in_table and table_lines:
            table_element = self._create_table(table_lines)
            if table_element:
                elements.append(table_element)
        
        if in_list and list_items:
            elements.extend(self._create_list(list_items, current_list_type))
        
        if in_blockquote and blockquote_lines:
            elements.extend(self._create_blockquote(blockquote_lines))
        
        return elements
    
    def _format_inline_markdown(self, text: str) -> str:
        """Format inline markdown (bold, italic, code, links)."""
        # Links [text](url) - style as colored underlined text
        text = re.sub(
            r'\[([^\]]+)\]\(([^)]+)\)',
            r'<font color="#06b6d4"><u>\1</u></font>',
            text
        )
        
        # Bold **text**
        text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
        
        # Italic *text*
        text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
        
        # Inline code `text`
        text = re.sub(
            r'`(.+?)`',
            r'<font name="Courier" color="#8b5cf6">\1</font>',
            text
        )
        
        return text
    
    def _create_table(self, table_lines: List[str]) -> Optional[Table]:
        """Create a table from markdown table lines."""
        if not table_lines:
            return None
        
        # Parse table rows
        rows = []
        for line in table_lines:
            # Skip separator lines (|---|---|)
            if re.match(r'^\s*\|[\s\-:|]+\|\s*$', line):
                continue
            
            # Split by | and clean up
            cells = [cell.strip() for cell in line.split('|')]
            # Remove empty first/last elements from leading/trailing |
            if cells and not cells[0]:
                cells = cells[1:]
            if cells and not cells[-1]:
                cells = cells[:-1]
            
            if cells:
                # Format cell content
                formatted_cells = [
                    Paragraph(self._format_inline_markdown(cell), self.styles['CustomBody'])
                    for cell in cells
                ]
                rows.append(formatted_cells)
        
        if not rows:
            return None
        
        # Create table
        table = Table(rows, hAlign='LEFT')
        
        # Style the table
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), self.primary),  # Header background
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),   # Header text
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('TOPPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9fafb')),
            ('GRID', (0, 0), (-1, -1), 0.5, self.text_light),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('TOPPADDING', (0, 1), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ])
        table.setStyle(table_style)
        
        return table
    
    def _create_list(self, items: List[Dict], list_type: str) -> List:
        """Create a formatted list (bullet or numbered)."""
        elements = []
        
        if not items:
            return elements
        
        # Group items by indentation level for nesting
        base_indent = min(item['indent'] for item in items)
        
        for item in items:
            indent_level = (item['indent'] - base_indent) // 2  # Assume 2 spaces per level
            content = self._format_inline_markdown(item['content'])
            
            # Create paragraph with left indent
            left_indent = 15 + (indent_level * 15)
            bullet_style = ParagraphStyle(
                'ListItem',
                parent=self.styles['CustomBody'],
                leftIndent=left_indent,
                bulletIndent=left_indent - 10,
                spaceAfter=6
            )
            
            if list_type == 'bullet':
                bullet_text = '•'
            else:  # numbered
                bullet_text = '•'  # For simplicity, using bullets for all levels
            
            para = Paragraph(f"{bullet_text} {content}", bullet_style)
            elements.append(para)
        
        elements.append(Spacer(1, 0.2*cm))
        return elements
    
    def _create_blockquote(self, lines: List[str]) -> List:
        """Create a styled blockquote."""
        elements = []
        
        if not lines:
            return elements
        
        # Combine lines
        text = ' '.join(lines)
        text = self._format_inline_markdown(text)
        
        # Create blockquote style with side border
        blockquote_style = ParagraphStyle(
            'Blockquote',
            parent=self.styles['CustomBody'],
            leftIndent=20,
            rightIndent=20,
            textColor=self.text_light,
            fontName='Helvetica-Oblique',
            borderWidth=3,
            borderColor=self.accent,
            borderPadding=10,
            backColor=colors.HexColor('#f0f9ff'),
            spaceAfter=12
        )
        
        elements.append(Spacer(1, 0.2*cm))
        elements.append(Paragraph(text, blockquote_style))
        elements.append(Spacer(1, 0.2*cm))
        
        return elements
    
    def _create_callout(self, lines: List[str]) -> List:
        """Create a callout box for cross-references and important notes."""
        elements = []
        
        if not lines:
            return elements
        
        # Format all lines
        formatted_text = '<br/>'.join(
            self._format_inline_markdown(line.strip()) for line in lines
        )
        
        # Create callout style with colored background
        callout_style = ParagraphStyle(
            'Callout',
            parent=self.styles['CustomBody'],
            leftIndent=15,
            rightIndent=15,
            backColor=colors.HexColor('#eff6ff'),
            borderWidth=1,
            borderColor=self.accent,
            borderPadding=12,
            spaceAfter=12,
            fontSize=9
        )
        
        elements.append(Spacer(1, 0.3*cm))
        elements.append(Paragraph(formatted_text, callout_style))
        elements.append(Spacer(1, 0.3*cm))
        
        return elements
    
    def _generate_pdf(self, story: List):
        """Generate PDF from story."""
        doc = SimpleDocTemplate(
            str(self.output_path),
            pagesize=self.page_size,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=2.5*cm,
            bottomMargin=2*cm,
            title="SOLID.AI Framework",
            author="SOLID.AI Framework Team"
        )
        
        # Build PDF
        doc.build(story, onFirstPage=self._draw_cover_background, onLaterPages=self._add_page_number)
    
    def _draw_cover_background(self, canvas_obj, doc):
        """Draw gradient background on cover page."""
        canvas_obj.saveState()
        
        # Simple gradient effect using rectangles
        page_width, page_height = self.page_size
        
        # Fill with primary color
        canvas_obj.setFillColor(self.primary)
        canvas_obj.rect(0, 0, page_width, page_height, fill=1, stroke=0)
        
        # Footer
        canvas_obj.setFillColor(colors.white)
        canvas_obj.setFont('Helvetica', 8)
        footer_text = "Open Source Framework • MIT License • github.com/gusafr/midora-solid-ai"
        canvas_obj.drawCentredString(page_width / 2, 1*cm, footer_text)
        
        canvas_obj.restoreState()
    
    def _add_page_number(self, canvas_obj, doc):
        """Add page number to footer."""
        canvas_obj.saveState()
        
        page_width, page_height = self.page_size
        
        # Header
        canvas_obj.setFillColor(self.text_light)
        canvas_obj.setFont('Helvetica', 9)
        canvas_obj.drawCentredString(page_width / 2, page_height - 1.5*cm, "SOLID.AI Framework")
        
        # Page number
        canvas_obj.setFont('Helvetica', 9)
        canvas_obj.drawRightString(page_width - 2*cm, 1*cm, str(canvas_obj.getPageNumber()))
        
        canvas_obj.restoreState()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate SOLID.AI Framework PDF Book (ReportLab - Cross-Platform)',
        formatter_class=argparse.RawDescriptionHelpFormatter
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
    
    # Show SVG support status
    if SVG_SUPPORT:
        print("✅ SVG diagram support enabled")
    else:
        print("⚠️  SVG diagram support disabled (install svglib: pip install svglib)")
    print()
    
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
