"""
SOLID.AI PDF Generator
Generates professional PDFs with SOLID.AI branding for framework documents

Usage:
    python generate_pdf.py --input DOCS/00-overview.md --output output/pdfs/overview.pdf
    python generate_pdf.py --all  # Generate PDFs for all core documents
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import cm, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Image, Table, TableStyle, KeepTogether
)
from reportlab.pdfgen import canvas
import markdown
import argparse

# SOLID.AI Brand Colors
BRAND_COLORS = {
    'primary_blue_dark': colors.HexColor('#2B5797'),
    'primary_blue_light': colors.HexColor('#7B94C4'),
    'accent_teal': colors.HexColor('#14B8A6'),
    'deep_purple': colors.HexColor('#673AB7'),
    'neutral_dark': colors.HexColor('#2E3A47'),
    'neutral_light': colors.HexColor('#F5F5F0'),
}


class SOLIDAIDocTemplate(SimpleDocTemplate):
    """Custom document template with SOLID.AI branding"""
    
    def __init__(self, filename, **kwargs):
        self.logo_path = kwargs.pop('logo_path', 'assets/images/solid-ai-logo.png')
        super().__init__(filename, **kwargs)
        
    def handle_pageBegin(self):
        """Add header/footer to each page"""
        self._handle_pageBegin()
        
        # Add header (logo + title)
        if self.page > 1:  # Skip cover page
            self.canv.saveState()
            
            # Header logo (small)
            if os.path.exists(self.logo_path):
                self.canv.drawImage(
                    self.logo_path,
                    1*cm, self.height - 1.5*cm,
                    width=2*cm, height=2*cm,
                    preserveAspectRatio=True,
                    mask='auto'
                )
            
            # Header line
            self.canv.setStrokeColor(BRAND_COLORS['primary_blue_light'])
            self.canv.setLineWidth(0.5)
            self.canv.line(1*cm, self.height - 2*cm, self.width + 1*cm, self.height - 2*cm)
            
            # Footer
            self.canv.setFont('Helvetica', 9)
            self.canv.setFillColor(BRAND_COLORS['neutral_dark'])
            
            # Page number (right)
            self.canv.drawRightString(
                self.width + 1*cm, 1*cm,
                f"Page {self.page - 1}"
            )
            
            # Framework name (center)
            self.canv.drawCentredString(
                self.width / 2 + 1*cm, 1*cm,
                "SOLID.AI Framework v1.0 | github.com/gusafr/midora-solid-ai"
            )
            
            self.canv.restoreState()


def create_styles():
    """Create custom paragraph styles for SOLID.AI branding"""
    styles = getSampleStyleSheet()
    
    # Cover page title
    styles.add(ParagraphStyle(
        name='CoverTitle',
        parent=styles['Heading1'],
        fontSize=32,
        textColor=BRAND_COLORS['primary_blue_dark'],
        alignment=TA_CENTER,
        spaceAfter=30,
        fontName='Helvetica-Bold'
    ))
    
    # Cover page subtitle
    styles.add(ParagraphStyle(
        name='CoverSubtitle',
        parent=styles['Normal'],
        fontSize=18,
        textColor=BRAND_COLORS['neutral_dark'],
        alignment=TA_CENTER,
        spaceAfter=50
    ))
    
    # Cover page metadata
    styles.add(ParagraphStyle(
        name='CoverMeta',
        parent=styles['Normal'],
        fontSize=12,
        textColor=BRAND_COLORS['neutral_dark'],
        alignment=TA_CENTER,
        spaceAfter=10
    ))
    
    # Document headings
    styles.add(ParagraphStyle(
        name='Heading1Custom',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=BRAND_COLORS['primary_blue_dark'],
        spaceAfter=20,
        spaceBefore=30,
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        name='Heading2Custom',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=BRAND_COLORS['primary_blue_dark'],
        spaceAfter=15,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    ))
    
    # Body text
    styles.add(ParagraphStyle(
        name='BodyCustom',
        parent=styles['Normal'],
        fontSize=11,
        textColor=BRAND_COLORS['neutral_dark'],
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        leading=16
    ))
    
    return styles


def create_cover_page(title, subtitle, version="1.0", date=None, logo_path='assets/images/solid-ai-logo.png'):
    """Generate cover page with SOLID.AI logo"""
    
    elements = []
    styles = create_styles()
    
    if date is None:
        date = datetime.now().strftime("%B %Y")
    
    # Vertical space
    elements.append(Spacer(1, 3*cm))
    
    # Logo (centered, large)
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=10*cm, height=10*cm)
        logo.hAlign = 'CENTER'
        elements.append(logo)
        elements.append(Spacer(1, 2*cm))
    
    # Title
    elements.append(Paragraph(title, styles['CoverTitle']))
    
    # Subtitle
    elements.append(Paragraph(subtitle, styles['CoverSubtitle']))
    
    # Metadata
    elements.append(Paragraph(f"<b>Version {version}</b>", styles['CoverMeta']))
    elements.append(Paragraph(date, styles['CoverMeta']))
    elements.append(Spacer(1, 1*cm))
    elements.append(Paragraph(
        "SOLID.AI Framework",
        styles['CoverMeta']
    ))
    elements.append(Paragraph(
        "github.com/gusafr/midora-solid-ai",
        styles['CoverMeta']
    ))
    
    elements.append(PageBreak())
    return elements


def markdown_to_pdf_elements(md_content, styles):
    """Convert Markdown content to ReportLab elements"""
    
    elements = []
    
    # Simple parser (for demo - you'd want a proper MD parser in production)
    lines = md_content.split('\n')
    
    for line in lines:
        line = line.strip()
        
        if not line:
            elements.append(Spacer(1, 0.3*cm))
            continue
        
        # Headings
        if line.startswith('# '):
            text = line[2:]
            elements.append(Paragraph(text, styles['Heading1Custom']))
        elif line.startswith('## '):
            text = line[3:]
            elements.append(Paragraph(text, styles['Heading2Custom']))
        elif line.startswith('### '):
            text = line[4:]
            elements.append(Paragraph(text, styles['Heading2']))
        # Lists
        elif line.startswith('- ') or line.startswith('* '):
            text = '• ' + line[2:]
            elements.append(Paragraph(text, styles['BodyCustom']))
        # Normal paragraph
        else:
            elements.append(Paragraph(line, styles['BodyCustom']))
    
    return elements


def generate_pdf(input_file, output_file, logo_path='assets/images/solid-ai-logo.png'):
    """Generate PDF from Markdown file with SOLID.AI branding"""
    
    # Read markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Extract title from first line
    first_line = md_content.split('\n')[0]
    if first_line.startswith('# '):
        title = first_line[2:]
        md_content = '\n'.join(md_content.split('\n')[1:])
    else:
        title = Path(input_file).stem.replace('-', ' ').title()
    
    # Create PDF
    doc = SOLIDAIDocTemplate(
        output_file,
        pagesize=A4,
        title=f"SOLID.AI - {title}",
        author="SOLID.AI Contributors",
        subject="SOLID.AI Framework Documentation",
        logo_path=logo_path,
        topMargin=3*cm,
        bottomMargin=2*cm,
        leftMargin=2*cm,
        rightMargin=2*cm
    )
    
    # Build content
    elements = []
    styles = create_styles()
    
    # Cover page
    elements.extend(create_cover_page(
        title=title,
        subtitle="SOLID.AI Framework Documentation",
        version="1.0",
        logo_path=logo_path
    ))
    
    # Document content
    elements.extend(markdown_to_pdf_elements(md_content, styles))
    
    # Generate PDF
    doc.build(elements)
    print(f"✅ PDF generated: {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Generate SOLID.AI branded PDFs')
    parser.add_argument('--input', help='Input Markdown file')
    parser.add_argument('--output', help='Output PDF file')
    parser.add_argument('--all', action='store_true', help='Generate PDFs for all core documents')
    parser.add_argument('--logo', default='assets/images/solid-ai-logo.png', help='Path to logo file')
    
    args = parser.parse_args()
    
    if args.all:
        # Generate PDFs for all core documents
        docs_dir = Path('DOCS')
        output_dir = Path('output/pdfs')
        output_dir.mkdir(parents=True, exist_ok=True)
        
        core_docs = [
            '00-overview.md',
            '01-principles.md',
            '02-architecture.md',
            '03-organizational-model.md',
            '04-automation-sipoc.md',
            '05-ai-agents.md',
            '06-governance-ethics.md',
            '07-observability.md',
            '08-human-ai-collaboration.md',
            '09-whole-organization-transformation.md',
            '10-role-hierarchy-human-ai.md',
            '11-ai-native-agile.md',
            'glossary.md'
        ]
        
        for doc in core_docs:
            input_file = docs_dir / doc
            if input_file.exists():
                output_file = output_dir / doc.replace('.md', '.pdf')
                print(f"Generating {output_file}...")
                generate_pdf(str(input_file), str(output_file), args.logo)
        
        print(f"\n✅ All PDFs generated in {output_dir}")
    
    elif args.input and args.output:
        generate_pdf(args.input, args.output, args.logo)
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
