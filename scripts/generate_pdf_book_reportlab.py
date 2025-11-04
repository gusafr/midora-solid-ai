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
        Preformatted, Image, KeepTogether, ListFlowable, ListItem
    )
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
    from reportlab.pdfgen import canvas
    import markdown2
except ImportError as e:
    print(f"❌ ERROR: Missing dependency - {e}")
    print("\nInstall required packages:")
    print("  pip install reportlab markdown2 pygments")
    sys.exit(1)


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
            
            playbook_paths = [
                ('by-stage/startup-ai-native.md', 'Startup: AI-Native from Day One'),
                ('by-stage/sme-transformation.md', 'SME: Transformation Journey'),
                ('organizational/squads.md', 'Squads Implementation'),
                ('organizational/pools.md', 'Pools Implementation'),
                ('organizational/ai-integration.md', 'AI Integration'),
            ]
            
            for path, title in playbook_paths:
                file_path = self.playbooks_dir / path
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        parts.append({
                            'type': 'chapter',
                            'title': title,
                            'content': f.read(),
                            'filename': path
                        })
        
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
    
    def _create_chapter(self, part: Dict[str, str]) -> List:
        """Create chapter from markdown content."""
        elements = []
        
        # Chapter break
        elements.append(PageBreak())
        
        # Chapter title
        elements.append(Paragraph(f"<b>{part['title']}</b>", self.styles['ChapterTitle']))
        elements.append(Spacer(1, 0.5*cm))
        
        # Process markdown content
        # Simple processing - convert to paragraphs
        lines = part['content'].split('\n')
        
        in_code_block = False
        code_lines = []
        
        for line in lines:
            # Code blocks
            if line.strip().startswith('```'):
                if in_code_block:
                    # End code block
                    code_text = '\n'.join(code_lines)
                    elements.append(Preformatted(code_text, self.styles['CustomCode']))
                    elements.append(Spacer(1, 0.3*cm))
                    code_lines = []
                in_code_block = not in_code_block
                continue
            
            if in_code_block:
                code_lines.append(line)
                continue
            
            # Skip diagram placeholders
            if '--8<--' in line or 'mermaid' in line:
                continue
            
            # Headers
            if line.startswith('# '):
                continue  # Skip H1 (already have chapter title)
            elif line.startswith('## '):
                text = line[3:].strip()
                elements.append(Spacer(1, 0.5*cm))
                elements.append(Paragraph(f"<b>{text}</b>", self.styles['CustomHeading2']))
            elif line.startswith('### '):
                text = line[4:].strip()
                elements.append(Spacer(1, 0.3*cm))
                elements.append(Paragraph(f"<b>{text}</b>", self.styles['CustomHeading3']))
            elif line.startswith('---'):
                elements.append(Spacer(1, 0.5*cm))
            elif line.strip():
                # Regular paragraph
                text = line.strip()
                # Clean up markdown
                text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
                text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
                text = re.sub(r'`(.+?)`', r'<font name="Courier" color="#8b5cf6">\1</font>', text)
                
                if text:
                    elements.append(Paragraph(text, self.styles['CustomBody']))
        
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
