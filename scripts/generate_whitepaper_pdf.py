#!/usr/bin/env python3
"""
SOLID.AI Whitepaper PDF Generator

Generates an academic-style whitepaper PDF with Google Research aesthetics.
Uses Inter for headings and IBM Plex Sans for body text.

Usage:
    python scripts/generate_whitepaper_pdf.py [options]

Options:
    --output PATH    Output PDF path (default: output/solid-ai-whitepaper.pdf)
    --page-size SIZE Page size: A4, Letter (default: A4)

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
    from reportlab.lib.units import cm, mm, inch
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
        Preformatted, Image, KeepTogether, ListFlowable, ListItem, HRFlowable
    )
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    import markdown2
except ImportError as e:
    print(f"❌ ERROR: Missing dependency - {e}")
    print("\nInstall required packages:")
    print("  pip install reportlab markdown2 pygments")
    sys.exit(1)


class WhitepaperPDFGenerator:
    """Generate academic whitepaper PDF with Google Research style."""
    
    # Whitepaper sections in order
    WHITEPAPER_SECTIONS = [
        ('whitepaper/index.md', 'Title Page'),
        ('whitepaper/abstract.md', 'Abstract'),
        ('whitepaper/architecture.md', 'Architecture'),
        ('whitepaper/specification.md', 'Specification'),
        ('whitepaper/implementation.md', 'Implementation Guide'),
        ('whitepaper/governance.md', 'Governance & Implementation'),
        ('whitepaper/diagrams.md', 'Diagrams'),
        ('whitepaper/figures.md', 'Architecture Overview'),
    ]
    
    def __init__(self, output_path: str = "output/solid-ai-whitepaper.pdf",
                 page_size: str = "A4"):
        self.output_path = Path(output_path)
        self.page_size = A4 if page_size == "A4" else letter
        self.root_dir = Path(__file__).parent.parent
        self.docs_site_dir = self.root_dir / "docs_site"
        
        # Ensure output directory exists
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Google Research color palette
        self.primary_color = colors.HexColor('#1a1a1a')      # Near black
        self.secondary_color = colors.HexColor('#2563eb')    # Blue accent
        self.text_color = colors.HexColor('#1a1a1a')
        self.text_light = colors.HexColor('#6b7280')
        self.border_color = colors.HexColor('#e5e7eb')
        self.code_bg = colors.HexColor('#f3f4f6')
        
        # Setup styles
        self._setup_styles()
        
    def _setup_styles(self):
        """Setup paragraph styles with academic typography."""
        self.styles = getSampleStyleSheet()
        
        # Title page
        self.styles.add(ParagraphStyle(
            name='WhitepaperTitle',
            fontSize=36,
            textColor=self.primary_color,
            spaceAfter=12*mm,
            spaceBefore=60*mm,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold',
            leading=40
        ))
        
        self.styles.add(ParagraphStyle(
            name='WhitepaperSubtitle',
            fontSize=14,
            textColor=self.text_light,
            spaceAfter=6*mm,
            alignment=TA_CENTER,
            fontName='Helvetica',
            leading=18
        ))
        
        self.styles.add(ParagraphStyle(
            name='WhitepaperMetadata',
            fontSize=11,
            textColor=self.text_light,
            spaceAfter=3*mm,
            alignment=TA_CENTER,
            fontName='Helvetica',
            leading=14
        ))
        
        # Section titles (chapter-level)
        self.styles.add(ParagraphStyle(
            name='SectionTitle',
            fontSize=24,
            textColor=self.primary_color,
            spaceAfter=10*mm,
            spaceBefore=15*mm,
            fontName='Helvetica-Bold',
            leading=28,
            keepWithNext=True
        ))
        
        # Body text (academic serif style)
        self.styles.add(ParagraphStyle(
            name='AcademicBody',
            fontSize=10.5,
            textColor=self.text_color,
            spaceAfter=4*mm,
            alignment=TA_JUSTIFY,
            fontName='Times-Roman',
            leading=16,
            firstLineIndent=0
        ))
        
        # Headings (sans-serif)
        self.styles.add(ParagraphStyle(
            name='AcademicH2',
            fontSize=16,
            textColor=self.primary_color,
            spaceAfter=4*mm,
            spaceBefore=8*mm,
            fontName='Helvetica-Bold',
            leading=20,
            keepWithNext=True
        ))
        
        self.styles.add(ParagraphStyle(
            name='AcademicH3',
            fontSize=13,
            textColor=self.primary_color,
            spaceAfter=3*mm,
            spaceBefore=6*mm,
            fontName='Helvetica-Bold',
            leading=16,
            keepWithNext=True
        ))
        
        self.styles.add(ParagraphStyle(
            name='AcademicH4',
            fontSize=11,
            textColor=self.text_color,
            spaceAfter=2*mm,
            spaceBefore=4*mm,
            fontName='Helvetica-Bold',
            leading=14,
            keepWithNext=True
        ))
        
        # Code blocks
        self.styles.add(ParagraphStyle(
            name='AcademicCode',
            fontSize=9,
            textColor=self.text_color,
            spaceAfter=4*mm,
            spaceBefore=2*mm,
            fontName='Courier',
            leading=11,
            leftIndent=10*mm,
            rightIndent=10*mm,
            backColor=self.code_bg,
            borderWidth=0.5,
            borderColor=self.border_color,
            borderPadding=5
        ))
        
        # Block quotes
        self.styles.add(ParagraphStyle(
            name='AcademicBlockquote',
            fontSize=10,
            textColor=self.text_light,
            spaceAfter=4*mm,
            spaceBefore=2*mm,
            fontName='Times-Italic',
            leading=15,
            leftIndent=15*mm,
            rightIndent=10*mm,
            borderWidth=0,
            borderColor=self.secondary_color,
            borderPadding=5
        ))
        
        # List items
        self.styles.add(ParagraphStyle(
            name='AcademicListItem',
            fontSize=10.5,
            textColor=self.text_color,
            spaceAfter=2*mm,
            fontName='Times-Roman',
            leading=16,
            leftIndent=0,
            bulletIndent=5*mm
        ))
        
        # Figure captions
        self.styles.add(ParagraphStyle(
            name='FigureCaption',
            fontSize=9,
            textColor=self.text_light,
            spaceAfter=6*mm,
            spaceBefore=2*mm,
            alignment=TA_CENTER,
            fontName='Helvetica',
            leading=12
        ))
        
        # Table text
        self.styles.add(ParagraphStyle(
            name='TableText',
            fontSize=9,
            textColor=self.text_color,
            fontName='Helvetica',
            leading=11
        ))
        
    def _create_header_footer(self, canvas, doc):
        """Create header and footer with page numbers."""
        canvas.saveState()
        
        # Footer with page number
        page_num = canvas.getPageNumber()
        if page_num > 1:  # Skip first page
            text = f"SOLID.AI Framework Whitepaper v1.0 — Page {page_num}"
            canvas.setFont('Helvetica', 8)
            canvas.setFillColor(self.text_light)
            canvas.drawCentredString(self.page_size[0] / 2, 15*mm, text)
            
            # Decorative line
            canvas.setStrokeColor(self.border_color)
            canvas.setLineWidth(0.5)
            canvas.line(40*mm, 12*mm, self.page_size[0] - 40*mm, 12*mm)
        
        canvas.restoreState()
        
    def _parse_markdown(self, content: str) -> List:
        """Convert markdown to ReportLab flowables."""
        story = []
        
        # Remove YAML frontmatter and badges
        content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL | re.MULTILINE)
        content = re.sub(r'!\[.*?\]\(https://img\.shields\.io/.*?\)', '', content)
        
        lines = content.split('\n')
        i = 0
        in_code_block = False
        code_block = []
        code_lang = ''
        in_list = False
        list_items = []
        
        while i < len(lines):
            line = lines[i]
            
            # Code blocks
            if line.strip().startswith('```'):
                if not in_code_block:
                    in_code_block = True
                    code_lang = line.strip()[3:].strip()
                    code_block = []
                else:
                    # End code block
                    code_text = '\n'.join(code_block)
                    story.append(Preformatted(code_text, self.styles['AcademicCode']))
                    in_code_block = False
                    code_block = []
                i += 1
                continue
            
            if in_code_block:
                code_block.append(line)
                i += 1
                continue
            
            # Skip horizontal rules
            if line.strip() in ['---', '***', '___']:
                story.append(HRFlowable(width="100%", thickness=0.5, color=self.border_color, spaceAfter=4*mm, spaceBefore=4*mm))
                i += 1
                continue
            
            # Headings
            if line.startswith('# '):
                text = line[2:].strip()
                story.append(Paragraph(text, self.styles['SectionTitle']))
                i += 1
                continue
            elif line.startswith('## '):
                text = line[3:].strip()
                story.append(Paragraph(text, self.styles['AcademicH2']))
                i += 1
                continue
            elif line.startswith('### '):
                text = line[4:].strip()
                story.append(Paragraph(text, self.styles['AcademicH3']))
                i += 1
                continue
            elif line.startswith('#### '):
                text = line[5:].strip()
                story.append(Paragraph(text, self.styles['AcademicH4']))
                i += 1
                continue
            
            # Lists
            if line.strip().startswith(('- ', '* ', '+ ')) or re.match(r'^\d+\.\s', line.strip()):
                if not in_list:
                    in_list = True
                    list_items = []
                
                # Extract list item text
                text = re.sub(r'^[-*+]\s+', '', line.strip())
                text = re.sub(r'^\d+\.\s+', '', text)
                
                # Process markdown in list item
                text = self._process_inline_markdown(text)
                list_items.append(ListItem(Paragraph(text, self.styles['AcademicListItem'])))
                i += 1
                
                # Check if next line continues list
                if i >= len(lines) or not (lines[i].strip().startswith(('- ', '* ', '+ ')) or re.match(r'^\d+\.\s', lines[i].strip())):
                    # End of list
                    story.append(ListFlowable(list_items, bulletType='bullet', start=None))
                    in_list = False
                    list_items = []
                continue
            
            # Block quotes
            if line.strip().startswith('>'):
                text = line.strip()[1:].strip()
                text = self._process_inline_markdown(text)
                story.append(Paragraph(text, self.styles['AcademicBlockquote']))
                i += 1
                continue
            
            # Empty lines
            if not line.strip():
                if story and not isinstance(story[-1], Spacer):
                    story.append(Spacer(1, 2*mm))
                i += 1
                continue
            
            # Regular paragraphs
            text = self._process_inline_markdown(line)
            if text.strip():
                story.append(Paragraph(text, self.styles['AcademicBody']))
            
            i += 1
        
        return story
    
    def _process_inline_markdown(self, text: str) -> str:
        """Process inline markdown (bold, italic, code, links)."""
        # Escape XML characters FIRST
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        
        # Process inline code FIRST to protect from other formatting
        # Use a placeholder without markdown special chars
        code_blocks = []
        def save_code(match):
            code_blocks.append(match.group(1))
            return f"XCODEX{len(code_blocks)-1}XCODEX"
        text = re.sub(r'`([^`]+)`', save_code, text)
        
        # Now process bold and italic (they won't affect code blocks)
        text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
        text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
        text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
        text = re.sub(r'_(.+?)_', r'<i>\1</i>', text)
        
        # Links - simplified to just underline the text
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<u>\1</u>', text)
        
        # Restore inline code blocks
        for i, code in enumerate(code_blocks):
            text = text.replace(f"XCODEX{i}XCODEX", f'<font name="Courier" size="9">{code}</font>')
        
        return text
    
    def _create_title_page(self) -> List:
        """Create title page."""
        story = []
        
        # Title
        story.append(Paragraph("SOLID.AI Framework", self.styles['WhitepaperTitle']))
        
        # Subtitle
        story.append(Paragraph(
            "A Formal Specification for Strategic, Organized, Layered, Intelligent, Data-Driven Artificial Intelligence",
            self.styles['WhitepaperSubtitle']
        ))
        
        story.append(Spacer(1, 15*mm))
        
        # Metadata
        story.append(Paragraph("Whitepaper v1.0 — Stable", self.styles['WhitepaperMetadata']))
        story.append(Paragraph(f"Published: {datetime.now().strftime('%B %Y')}", self.styles['WhitepaperMetadata']))
        story.append(Paragraph("License: MIT", self.styles['WhitepaperMetadata']))
        
        story.append(Spacer(1, 20*mm))
        
        # Abstract teaser
        abstract_text = (
            "A comprehensive architectural specification for building AI-native organizations "
            "that scale human intelligence through structured collaboration between people and "
            "artificial intelligence. This whitepaper provides the complete technical specification, "
            "architectural patterns, and governance principles required to implement production-ready "
            "AI-native systems."
        )
        story.append(Paragraph(abstract_text, self.styles['AcademicBody']))
        
        story.append(PageBreak())
        
        return story
    
    def generate(self):
        """Generate the whitepaper PDF."""
        print(f"📄 Generating SOLID.AI Whitepaper PDF...")
        print(f"   Output: {self.output_path}")
        
        # Create PDF document
        doc = SimpleDocTemplate(
            str(self.output_path),
            pagesize=self.page_size,
            leftMargin=25*mm,
            rightMargin=25*mm,
            topMargin=25*mm,
            bottomMargin=25*mm,
            title="SOLID.AI Framework Whitepaper v1.0",
            author="SOLID.AI Framework Contributors",
            subject="AI-Native Organization Architecture"
        )
        
        story = []
        
        # Title page
        story.extend(self._create_title_page())
        
        # Process each whitepaper section
        for file_path, section_name in self.WHITEPAPER_SECTIONS:
            full_path = self.docs_site_dir / file_path
            
            if not full_path.exists():
                print(f"   ⚠️  Skipping missing file: {file_path}")
                continue
            
            print(f"   ✓ Processing: {section_name}")
            
            # Skip index (we have custom title page)
            if 'index.md' in file_path:
                continue
            
            # Read markdown content
            content = full_path.read_text(encoding='utf-8')
            
            # Parse and add to story
            section_content = self._parse_markdown(content)
            story.extend(section_content)
            
            # Page break after each section (except last)
            if file_path != self.WHITEPAPER_SECTIONS[-1][0]:
                story.append(PageBreak())
        
        # Build PDF
        doc.build(story, onFirstPage=self._create_header_footer, onLaterPages=self._create_header_footer)
        
        print(f"\n✅ Whitepaper PDF generated successfully!")
        print(f"   📁 {self.output_path.absolute()}")
        print(f"   📊 Size: {self.output_path.stat().st_size / 1024:.1f} KB")


def main():
    parser = argparse.ArgumentParser(description="Generate SOLID.AI Whitepaper PDF")
    parser.add_argument('--output', default='output/solid-ai-whitepaper.pdf',
                        help='Output PDF path')
    parser.add_argument('--page-size', choices=['A4', 'Letter'], default='A4',
                        help='Page size')
    
    args = parser.parse_args()
    
    generator = WhitepaperPDFGenerator(
        output_path=args.output,
        page_size=args.page_size
    )
    
    generator.generate()


if __name__ == '__main__':
    main()
