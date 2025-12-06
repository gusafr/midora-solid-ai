# PDF Generation Guide

This directory contains scripts for generating professional PDF documentation from the SOLID.AI framework.

## Two PDF Versions

### 1. Whitepaper PDF (Academic/Research Style)
**File:** `generate_whitepaper_pdf.py`

Generates a publication-quality whitepaper with Google Research aesthetics:
- **Typography:** Times Roman body text, Helvetica headings
- **Content:** 7 whitepaper sections only (Abstract, Architecture, Specification, Specification v1, Governance, Diagrams, Architecture Overview)
- **Style:** Academic paper layout with generous whitespace
- **Use Cases:** Conference submissions, academic citations, executive distribution, research publications

```bash
# Generate whitepaper PDF
python scripts/generate_whitepaper_pdf.py

# Custom output path
python scripts/generate_whitepaper_pdf.py --output output/whitepaper-v1.0.pdf

# Letter size (for US printing)
python scripts/generate_whitepaper_pdf.py --page-size Letter
```

**Output:** ~50-80 pages, optimized for printing and digital distribution

---

### 2. Complete Framework PDF (Comprehensive Documentation)
**File:** `generate_pdf_book_reportlab.py`

Generates a complete framework book with all documentation:
- **Typography:** Helvetica sans-serif throughout
- **Content:** All docs, playbooks, adoption guides, ADRs (configurable)
- **Style:** Professional technical documentation with color coding
- **Use Cases:** Implementation teams, internal training, complete reference

```bash
# Generate core documentation only
python scripts/generate_pdf_book_reportlab.py

# Include all playbooks
python scripts/generate_pdf_book_reportlab.py --include-playbooks

# Include adoption pack
python scripts/generate_pdf_book_reportlab.py --include-adoption

# Complete book (everything)
python scripts/generate_pdf_book_reportlab.py --include-playbooks --include-adoption

# Grayscale version (for printing)
python scripts/generate_pdf_book_reportlab.py --color-scheme grayscale

# Custom output
python scripts/generate_pdf_book_reportlab.py --output output/solid-ai-complete.pdf
```

**Output:** 100-300+ pages depending on options

---

## Installation

### Install Dependencies

```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install PDF generation packages
pip install reportlab markdown2 pygments

# Optional: SVG diagram support
pip install svglib
```

---

## Features

### Whitepaper PDF Features

✅ **Google Research Aesthetic**
- Clean typography (Times Roman + Helvetica)
- Generous whitespace and margins
- Academic citation-ready format
- Professional figure numbering

✅ **Academic Elements**
- Title page with metadata
- Status badges (Stable v1.0)
- Formal section headers
- Figure captions
- Page numbers with document title

✅ **Content Optimization**
- Syntax highlighting for code blocks
- Proper list formatting
- Block quotes styling
- Table formatting
- Cross-references preserved

### Complete Framework PDF Features

✅ **Professional Documentation**
- Color-coded sections (or grayscale)
- Table of contents
- Chapter markers
- Syntax-highlighted code
- Embedded diagrams (with svglib)

✅ **Modular Content**
- Core docs only (default)
- Optional playbooks
- Optional adoption materials
- Configurable page size

✅ **Production Ready**
- Cross-platform (Windows, macOS, Linux)
- No system dependencies
- Pure Python implementation
- Batch generation support

---

## Typography Details

### Whitepaper PDF Typography

```
Title Page:
- Title: Helvetica Bold 36pt
- Subtitle: Helvetica 14pt
- Metadata: Helvetica 11pt

Body Content:
- Headings: Helvetica Bold (24pt, 16pt, 13pt, 11pt)
- Body: Times Roman 10.5pt, leading 16pt
- Lists: Times Roman 10.5pt
- Code: Courier 9pt on gray background
- Captions: Helvetica 9pt

Margins:
- All sides: 25mm
- Line spacing: 1.52 (academic standard)
```

### Complete Framework PDF Typography

```
Cover:
- Title: Helvetica Bold 36pt on gradient
- Subtitle: Helvetica 14pt

Content:
- Chapter titles: Helvetica Bold 24pt (indigo border)
- Headings: Helvetica Bold 16pt, 13pt, 11pt
- Body: Helvetica 10pt
- Code: Courier 9pt
- Tables: Helvetica 9pt

Margins:
- Left/Right: 20mm
- Top/Bottom: 25mm
```

---

## Color Schemes

### Whitepaper (Academic)
```
Primary: #1a1a1a (near black)
Accent: #2563eb (blue)
Text: #1a1a1a
Light text: #6b7280
Border: #e5e7eb
Code background: #f3f4f6
```

### Complete Framework (Professional)
```
Color mode:
- Primary: #6366f1 (indigo)
- Secondary: #8b5cf6 (purple)
- Accent: #06b6d4 (cyan)
- Text: #1f2937

Grayscale mode:
- Primary: #374151
- Secondary: #4b5563
- Accent: #6b7280
- Text: #111827
```

---

## File Structure

```
scripts/
├── generate_whitepaper_pdf.py      # Academic whitepaper generator (NEW)
├── generate_pdf_book_reportlab.py  # Complete framework generator
├── svg_helper.py                   # SVG diagram support (optional)
└── PDF-GENERATION-README.md        # This file

output/
├── solid-ai-whitepaper.pdf         # Whitepaper output
└── solid-ai-framework.pdf          # Complete framework output
```

---

## Usage Examples

### Academic Publication Workflow

```bash
# 1. Generate whitepaper for conference submission
python scripts/generate_whitepaper_pdf.py --page-size Letter

# 2. Print review copies (grayscale)
python scripts/generate_pdf_book_reportlab.py \
    --color-scheme grayscale \
    --output output/review-copy.pdf

# 3. Final publication version
python scripts/generate_whitepaper_pdf.py \
    --output output/solid-ai-whitepaper-v1.0-final.pdf
```

### Implementation Team Workflow

```bash
# 1. Core docs for architects
python scripts/generate_pdf_book_reportlab.py

# 2. Complete reference with playbooks
python scripts/generate_pdf_book_reportlab.py \
    --include-playbooks \
    --output output/implementation-guide.pdf

# 3. Adoption pack for change managers
python scripts/generate_pdf_book_reportlab.py \
    --include-adoption \
    --output output/adoption-guide.pdf

# 4. Everything (training manual)
python scripts/generate_pdf_book_reportlab.py \
    --include-playbooks \
    --include-adoption \
    --output output/complete-manual.pdf
```

### Batch Generation

```bash
# Generate all versions at once
python scripts/generate_whitepaper_pdf.py
python scripts/generate_pdf_book_reportlab.py --include-playbooks
```

Or create a batch script (`generate_all_pdfs.ps1` for Windows):

```powershell
# generate_all_pdfs.ps1
Write-Host "Generating all PDF versions..." -ForegroundColor Cyan

# Whitepaper
Write-Host "`n1. Whitepaper (A4)..." -ForegroundColor Green
python scripts/generate_whitepaper_pdf.py --output output/solid-ai-whitepaper-a4.pdf

Write-Host "`n2. Whitepaper (Letter)..." -ForegroundColor Green
python scripts/generate_whitepaper_pdf.py --page-size Letter --output output/solid-ai-whitepaper-letter.pdf

# Complete framework
Write-Host "`n3. Core framework..." -ForegroundColor Green
python scripts/generate_pdf_book_reportlab.py --output output/solid-ai-core.pdf

Write-Host "`n4. Framework with playbooks..." -ForegroundColor Green
python scripts/generate_pdf_book_reportlab.py --include-playbooks --output output/solid-ai-playbooks.pdf

Write-Host "`n5. Complete documentation..." -ForegroundColor Green
python scripts/generate_pdf_book_reportlab.py --include-playbooks --include-adoption --output output/solid-ai-complete.pdf

Write-Host "`n✅ All PDFs generated!" -ForegroundColor Cyan
```

---

## Troubleshooting

### Missing Dependencies

**Error:** `ModuleNotFoundError: No module named 'reportlab'`

**Solution:**
```bash
pip install reportlab markdown2 pygments
```

### SVG Diagrams Not Rendering

**Error:** `Info: SVG support not available`

**Solution (optional):**
```bash
pip install svglib
```

### Memory Issues (Large PDFs)

If generating complete documentation with all options causes memory issues:

1. Generate in smaller chunks:
```bash
# Core docs only
python scripts/generate_pdf_book_reportlab.py

# Playbooks separately
python scripts/generate_pdf_book_reportlab.py --include-playbooks --output output/playbooks.pdf
```

2. Increase Python memory limit (advanced):
```bash
python -Xmx4g scripts/generate_pdf_book_reportlab.py --include-playbooks --include-adoption
```

### Windows Path Issues

Use raw strings or forward slashes:
```bash
python scripts/generate_whitepaper_pdf.py --output "output/whitepaper.pdf"
```

---

## Customization

### Modify Typography

Edit the `_setup_styles()` method in either generator:

```python
# Example: Change body font size
self.styles.add(ParagraphStyle(
    name='AcademicBody',
    fontSize=11,  # Changed from 10.5
    # ... other properties
))
```

### Add Custom Sections

Edit the `WHITEPAPER_SECTIONS` list in `generate_whitepaper_pdf.py`:

```python
WHITEPAPER_SECTIONS = [
    ('whitepaper/abstract.md', 'Abstract'),
    ('custom/section.md', 'Custom Section'),  # Add here
    # ... other sections
]
```

### Change Color Scheme

Modify color definitions in `__init__()`:

```python
# Example: Use custom brand colors
self.primary_color = colors.HexColor('#your-color')
self.secondary_color = colors.HexColor('#your-accent')
```

---

## Best Practices

### For Whitepaper Distribution

1. **Always use A4** for international distribution
2. **Use Letter** for US-specific publications
3. **Include version number** in filename: `solid-ai-whitepaper-v1.0.pdf`
4. **Test print quality** before mass printing
5. **Embed fonts** (automatically handled by ReportLab)

### For Complete Documentation

1. **Start with core docs** to verify layout
2. **Add playbooks incrementally** to check page count
3. **Use grayscale** for internal printing to save costs
4. **Generate quarterly** or after major updates
5. **Archive versions** with date stamps

---

## Version History

| Version | Date | Generator | Changes |
|---------|------|-----------|---------|
| 1.0 | 2025-11-29 | `generate_whitepaper_pdf.py` | Initial whitepaper generator with Google Research styling |
| 1.0 | 2024-11 | `generate_pdf_book_reportlab.py` | Complete framework generator (existing) |

---

## License

Both PDF generators and generated PDFs are released under the MIT License.

---

## Support

For issues or questions:
- **GitHub Issues:** https://github.com/gusafr/midora-solid-ai/issues
- **Documentation:** https://gusafr.github.io/midora-solid-ai/
- **PDF Samples:** Check `output/` directory for examples

---

**Quick Start:**

```bash
# Generate whitepaper (recommended first)
python scripts/generate_whitepaper_pdf.py

# Generate complete framework
python scripts/generate_pdf_book_reportlab.py --include-playbooks
```

Both PDFs will be in the `output/` directory!
