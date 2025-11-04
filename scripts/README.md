# PDF Book Generator

**Generate a professionally-styled PDF book from the SOLID.AI framework documentation.**

## Overview

The PDF book generator (`generate_pdf_book.py`) creates a modern, minimalist PDF document from all framework documentation, suitable for:

- 📖 **Offline reading** (flights, commutes, no internet)
- 🖨️ **Printing** (executive briefings, workshops, training)
- 📧 **Sharing** (email to stakeholders, partners, prospects)
- 💼 **Professional presentations** (sales, consulting engagements)
- 📚 **Reference manual** (onboarding, desk reference)

---

## Features

### ✨ Content Aggregation

- **Core Documentation** (13 files):
  - 00-11: All strategic and operational docs
  - Glossary
- **Manifesto** (optional)
- **Playbooks** (optional, 17 playbooks)
- **Adoption Pack** (optional, templates/checklists)

### 🎨 Modern Minimalist Design

- **Cover page** with gradient background
- **Table of contents** with clickable links
- **Professional typography** (Inter font family)
- **Clean chapter separators**
- **Syntax-highlighted code blocks**
- **Responsive tables** (auto-sized)
- **Headers/footers** with page numbers

### 📐 Customization Options

- **Page sizes**: A4, Letter
- **Color schemes**: Full color, Grayscale (print-friendly)
- **Content selection**: Core docs only, with playbooks, full pack
- **Output path**: Custom file location

---

## Installation

### 1. Install Dependencies

```bash
# Install PDF generation libraries
pip install -r requirements.txt
```

**Dependencies:**
- `weasyprint` - HTML to PDF rendering
- `markdown` - Markdown to HTML conversion
- `pygments` - Code syntax highlighting
- `pillow` - Image processing

### 2. System Requirements

**WeasyPrint** requires system libraries:

**Windows:**
- Install [GTK+ for Windows](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)
- Or use WSL2 with Linux dependencies

**macOS:**
```bash
brew install cairo pango gdk-pixbuf libffi
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

---

## Usage

### Basic Usage (Core Docs Only)

```bash
python scripts/generate_pdf_book.py
```

**Output:** `output/solid-ai-framework.pdf` (~80-100 pages)

---

### Include Playbooks

```bash
python scripts/generate_pdf_book.py --include-playbooks
```

**Output:** `output/solid-ai-framework.pdf` (~150-180 pages)

---

### Full Book (All Content)

```bash
python scripts/generate_pdf_book.py --include-playbooks --include-adoption
```

**Output:** `output/solid-ai-framework.pdf` (~200-250 pages)

---

### Custom Output Path

```bash
python scripts/generate_pdf_book.py --output ~/Desktop/solid-ai.pdf
```

---

### Print-Friendly Version (Grayscale)

```bash
python scripts/generate_pdf_book.py --color-scheme grayscale
```

**Use case:** Print on black-and-white printers, reduce ink consumption

---

### Letter Size (US Standard)

```bash
python scripts/generate_pdf_book.py --page-size Letter
```

**Default:** A4 (international standard)

---

### Combined Example

```bash
python scripts/generate_pdf_book.py \
  --include-playbooks \
  --page-size Letter \
  --color-scheme grayscale \
  --output output/solid-ai-print-edition.pdf
```

---

## Command-Line Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--output PATH` | Any path | `output/solid-ai-framework.pdf` | Output PDF file path |
| `--include-playbooks` | Flag | Off | Include 17 implementation playbooks |
| `--include-adoption` | Flag | Off | Include adoption pack materials |
| `--page-size SIZE` | `A4`, `Letter` | `A4` | Page size format |
| `--color-scheme SCHEME` | `color`, `grayscale` | `color` | Color scheme |

---

## Output Structure

### Cover Page

- **Title:** SOLID.AI Framework
- **Subtitle:** The Organizational Nervous System for AI-Native Companies
- **Version:** v1.0
- **Date:** Current month/year
- **Footer:** License and repository link

### Table of Contents

- Automatically generated from all chapters
- Numbered chapters (01, 02, 03...)
- Clickable links (in digital version)

### Core Documentation (Chapters 1-13)

1. Overview
2. Principles
3. Architecture
4. Organizational Model
5. Automation & SIPOC
6. AI Agents
7. Governance & Ethics
8. Observability
9. Human-AI Collaboration
10. Whole-Organization Transformation
11. Role Hierarchy
12. AI-Native Agile
13. Glossary

### Manifesto

- SOLID.AI Manifesto v1.0

### Playbooks (If `--include-playbooks`)

**Section Divider:** Implementation Playbooks

- Startup: AI-Native from Day One
- SME: Transformation Journey
- Squads Implementation
- Pools Implementation
- AI Integration

### Adoption Pack (If `--include-adoption`)

**Section Divider:** Adoption Pack

- Selected templates
- Checklists
- Reference cards

---

## Design Specifications

### Typography

- **Body Font:** Inter (sans-serif, modern, readable)
- **Code Font:** Fira Code (monospace, ligatures)
- **Body Size:** 10.5pt
- **Line Height:** 1.7 (excellent readability)
- **Alignment:** Justified (professional look)

### Color Palette (Color Scheme)

- **Primary:** `#6366f1` (Indigo) - Headers, accents
- **Secondary:** `#8b5cf6` (Purple) - Gradients
- **Accent:** `#06b6d4` (Cyan) - Highlights
- **Text:** `#1f2937` (Dark gray)
- **Text Light:** `#6b7280` (Medium gray)
- **Background:** `#ffffff` (White)
- **Background Alt:** `#f9fafb` (Light gray) - Code blocks, tables

### Color Palette (Grayscale Scheme)

- All colors replaced with grayscale equivalents
- Optimized for black-and-white printing
- Reduces ink consumption by ~60%

### Page Layout

- **Margins:** 2.5cm top, 2cm sides, 2cm bottom
- **Headers:** "SOLID.AI Framework" centered
- **Footers:** Page number right-aligned
- **Chapter Breaks:** New page for each chapter
- **Section Breaks:** Full-page divider for major sections

---

## Troubleshooting

### Error: "WeasyPrint not installed"

**Solution:**
```bash
pip install weasyprint
```

### Error: "cairo not found" (Windows)

**Solution:**
1. Download [GTK+ for Windows](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)
2. Install to default location
3. Add GTK+ bin directory to PATH
4. Restart terminal

**Alternative:** Use WSL2 (Windows Subsystem for Linux)

### Error: "Permission denied"

**Solution:** Check output directory permissions
```bash
chmod 755 output/
```

### PDF is blank or missing content

**Solution:** Check source files exist
```bash
ls DOCS/*.md  # Should show 13 files
```

### Diagrams not rendering

**Current:** Diagrams show placeholder text with link to online version

**Future:** Will integrate `mermaid-cli` for diagram rendering

---

## Customization

### Modify CSS Styling

Edit `_get_modern_minimalist_css()` method in `generate_pdf_book.py`:

```python
def _get_modern_minimalist_css(self) -> str:
    # Change colors
    primary = '#your-color-here'
    
    # Change fonts
    font-family: 'YourFont', sans-serif;
    
    # Change spacing
    margin-bottom: 1cm;  # Increase/decrease
```

### Add Custom Content

Edit `_collect_content()` method to include additional files:

```python
# Add custom section
parts.append({
    'type': 'chapter',
    'title': 'Your Custom Chapter',
    'content': Path('path/to/file.md').read_text(),
    'filename': 'custom'
})
```

### Change Page Breaks

Add manual page breaks in markdown:

```markdown
---

<!-- page-break -->
```

Or wrap in `<div>`:

```html
<div class="page-break"></div>
```

---

## Roadmap

### Planned Enhancements

- [ ] **Diagram Rendering:** Integrate `mermaid-cli` to render diagrams as images
- [ ] **Localization:** Multi-language support (ES, PT, FR, DE)
- [ ] **Interactive TOC:** Bookmarks in PDF for navigation
- [ ] **Cover Customization:** Custom logos, backgrounds
- [ ] **Theme Variants:** Dark mode, high contrast
- [ ] **EPUB Export:** Generate EPUB for e-readers
- [ ] **Section Selection:** Generate specific chapters only
- [ ] **Watermarks:** Add custom watermarks (Draft, Confidential)

---

## Examples

### Generate for Executive Briefing

```bash
# Short, print-friendly version for C-suite
python scripts/generate_pdf_book.py \
  --page-size Letter \
  --color-scheme grayscale \
  --output briefing/executive-summary.pdf
```

**Result:** Core docs only, ~80 pages, grayscale, Letter size

---

### Generate Complete Reference Manual

```bash
# Full book with all materials
python scripts/generate_pdf_book.py \
  --include-playbooks \
  --include-adoption \
  --output manuals/solid-ai-complete-v1.0.pdf
```

**Result:** All content, ~250 pages, full color, A4

---

### Generate for Sales Team

```bash
# Core + select playbooks, color for digital sharing
python scripts/generate_pdf_book.py \
  --include-playbooks \
  --color-scheme color \
  --output sales/solid-ai-sales-deck.pdf
```

**Result:** Core + playbooks, ~180 pages, full color

---

## Performance

**Generation Time:**
- Core docs only: ~10-15 seconds
- With playbooks: ~20-30 seconds
- Full content: ~40-60 seconds

**File Sizes:**
- Core docs: ~2-3 MB
- With playbooks: ~4-6 MB
- Full content: ~8-12 MB

**Memory Usage:** ~200-400 MB during generation

---

## Contributing

### Report Issues

Found a bug or have suggestions?

1. Open issue: [GitHub Issues](https://github.com/gusafr/midora-solid-ai/issues)
2. Tag with `pdf-generator` label
3. Include error message and steps to reproduce

### Submit Enhancements

Have improvements?

1. Fork repository
2. Create branch: `feature/pdf-enhancement`
3. Test changes thoroughly
4. Submit pull request

---

## License

MIT License - Same as SOLID.AI framework

Generated PDFs can be shared freely with attribution.

---

## Support

**Documentation:** [Framework Documentation](../README.md)

**Issues:** [GitHub Issues](https://github.com/gusafr/midora-solid-ai/issues)

**Discussions:** [GitHub Discussions](https://github.com/gusafr/midora-solid-ai/discussions)

---

**Last Updated:** November 4, 2025  
**Script Version:** 1.0  
**Framework Version:** SOLID.AI v1.0
