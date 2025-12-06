# SOLID.AI Brand Assets & Logo Usage

**Version:** 1.0  
**Last Updated:** November 6, 2025

---

## Logo Files

### Primary Logo
**File:** `assets/images/solid-ai-logo.png`

**Description:** SOLID.AI logo featuring molecular/network structure representing interconnected intelligence

**Specifications:**
- Format: PNG (transparent background)
- Colors: Deep blue gradient (#2B5797 → #7B94C4)
- Typography: Custom "solid.ai" wordmark
- Symbol: Hexagonal molecular network structure (6 nodes + center)

---

## Usage Guidelines

### ✅ Approved Uses

**Digital Media:**
- Website header/footer
- GitHub repository
- Social media profiles (LinkedIn, Twitter, GitHub)
- Email signatures
- Presentation slides
- Documentation (PDF, Markdown, HTML)

**Print Media:**
- Business cards
- Conference posters
- White papers
- Case studies
- Training materials

**Required Attribution:**
When using SOLID.AI logo in derivative works, include:
> "SOLID.AI is an open-source framework available at github.com/gusafr/midora-solid-ai"

---

### ❌ Prohibited Uses

- Modifying logo colors, proportions, or elements
- Using logo to imply endorsement without permission
- Incorporating logo into other product logos
- Using logo for commercial products without attribution
- Distorting, rotating, or altering logo in any way

---

## Size Recommendations

### Website
- **Header/Navigation:** 150-200px width
- **Homepage Hero:** 300-400px width
- **Footer:** 100-150px width
- **Favicon:** 32×32px or 64×64px

### PDF Documents
- **Cover Page (A4/Letter):** 400-600px width (centered)
- **Header:** 100-150px width (left-aligned)
- **Footer:** 80-120px width (centered)

### Presentations
- **Title Slide:** 400-500px width
- **Section Dividers:** 250-350px width
- **Footer (recurring):** 100-150px width

---

## Integration Examples

### Markdown (GitHub, Documentation)

```markdown
<div align="center">
  <img src="assets/images/solid-ai-logo.png" alt="SOLID.AI Logo" width="300"/>
</div>
```

### HTML (Website)

```html
<img src="/assets/images/solid-ai-logo.png" 
     alt="SOLID.AI - Organizational Nervous System for AI-Native Companies" 
     width="300" 
     height="auto" />
```

### MkDocs (Material Theme)

In `mkdocs.yml`:
```yaml
theme:
  name: material
  logo: assets/images/solid-ai-logo.png
  favicon: assets/images/solid-ai-logo.png
```

### LaTeX/PDF (ReportLab)

```python
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image

# Cover page logo (centered)
logo = Image('assets/images/solid-ai-logo.png', width=400, height=400)
logo.hAlign = 'CENTER'

# Header logo (smaller, left-aligned)
header_logo = Image('assets/images/solid-ai-logo.png', width=120, height=120)
```

---

## PDF Generation Integration

### Cover Page Template

**Recommended Layout (A4/Letter):**

```
┌─────────────────────────────────────┐
│                                     │
│         [SOLID.AI LOGO]             │  ← 400-500px width, centered
│                                     │
│                                     │
│    DOCUMENT TITLE (28pt bold)       │
│    Subtitle (18pt)                  │
│                                     │
│    Version X.X                      │
│    Date: Month Year                 │
│                                     │
│                                     │
│    [Organization Name]              │
│    [Author(s)]                      │
│                                     │
└─────────────────────────────────────┘
```

### Header/Footer Template

**Header (recurring pages):**
```
[Logo 100px] | Document Title                    Page X
─────────────────────────────────────────────────────────
```

**Footer (recurring pages):**
```
─────────────────────────────────────────────────────────
        [Logo 80px] | SOLID.AI Framework v1.0
        github.com/gusafr/midora-solid-ai
```

---

## PDF Script Integration

### Using ReportLab (Python)

Create `scripts/generate_pdf.py`:

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Image, Paragraph, Spacer, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def create_cover_page(doc_title, subtitle, version, date, author):
    """Generate PDF cover page with SOLID.AI logo"""
    
    elements = []
    styles = getSampleStyleSheet()
    
    # Add vertical space
    elements.append(Spacer(1, 3*cm))
    
    # Add logo (centered)
    logo = Image('assets/images/solid-ai-logo.png', width=12*cm, height=12*cm)
    logo.hAlign = 'CENTER'
    elements.append(logo)
    elements.append(Spacer(1, 2*cm))
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor='#2B5797',
        alignment=TA_CENTER,
        spaceAfter=30
    )
    elements.append(Paragraph(doc_title, title_style))
    
    # Subtitle
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=18,
        alignment=TA_CENTER,
        spaceAfter=50
    )
    elements.append(Paragraph(subtitle, subtitle_style))
    
    # Metadata
    meta_style = ParagraphStyle(
        'Metadata',
        parent=styles['Normal'],
        fontSize=12,
        alignment=TA_CENTER,
        spaceAfter=10
    )
    elements.append(Paragraph(f"Version {version}", meta_style))
    elements.append(Paragraph(f"Date: {date}", meta_style))
    elements.append(Spacer(1, 1*cm))
    elements.append(Paragraph(author, meta_style))
    
    elements.append(PageBreak())
    return elements

# Usage example
doc = SimpleDocTemplate(
    "output/SOLID-AI-Framework-v1.0.pdf",
    pagesize=A4,
    title="SOLID.AI Framework v1.0",
    author="SOLID.AI Contributors"
)

content = []
content.extend(create_cover_page(
    doc_title="SOLID.AI Framework",
    subtitle="Organizational Nervous System for AI-Native Companies",
    version="1.0",
    date="November 2025",
    author="github.com/gusafr/midora-solid-ai"
))

# Add document content here...

doc.build(content)
```

---

## Color Palette (for consistent branding)

| Color | Hex Code | Usage |
|-------|----------|-------|
| **Primary Blue (Dark)** | `#2B5797` | Logo nodes, headings, primary CTAs |
| **Secondary Blue (Light)** | `#7B94C4` | Logo gradient, backgrounds, borders |
| **Accent Teal** | `#14B8A6` | Highlights, success states, interactive elements |
| **Deep Purple** | `#673AB7` | Secondary accents (MkDocs theme) |
| **Neutral Dark** | `#2E3A47` | Body text, dark mode backgrounds |
| **Neutral Light** | `#F5F5F0` | Page backgrounds, light mode |

---

## Typography Recommendations

### Primary Font (Body Text)
- **Web:** Inter (Google Fonts)
- **PDF:** Helvetica or Arial
- **Fallback:** Sans-serif system fonts

### Monospace Font (Code)
- **Web:** Fira Code (Google Fonts)
- **PDF:** Courier New or Monaco
- **Fallback:** Monospace system fonts

### Font Sizes
- **H1 (Main Titles):** 28-32pt
- **H2 (Section Headings):** 22-24pt
- **H3 (Subsections):** 18-20pt
- **Body Text:** 11-12pt
- **Code/Technical:** 10-11pt
- **Captions/Footnotes:** 9-10pt

---

## File Storage

### Repository Structure

```
midora-solid-ai/
├── assets/
│   └── images/
│       ├── solid-ai-logo.png          ← Primary logo
│       ├── solid-ai-logo-square.png   ← Square variant (future)
│       └── solid-ai-logo-white.png    ← White variant (future)
├── docs_site/
│   └── assets/
│       └── images/
│           └── solid-ai-logo.png      ← Copy for website
└── output/
    └── pdfs/                          ← Generated PDFs with logo
```

---

## Attribution & License

**Logo:** © 2025 SOLID.AI Contributors  
**Framework:** MIT License (see LICENSE file)

**Attribution Required:**
When using SOLID.AI branding in derivative works, include:

```
SOLID.AI Framework v1.0
Open-source organizational framework for AI-Native companies
https://github.com/gusafr/midora-solid-ai
```

---

## Future Enhancements

**Planned Variants (v1.1+):**
- [ ] Square logo variant (for social media avatars)
- [ ] White/inverted logo (for dark backgrounds)
- [ ] Icon-only version (for small spaces)
- [ ] Animated SVG version (for web)
- [ ] Favicon (.ico format)

**Planned Integrations:**
- [ ] PDF generation script with logo templates
- [ ] PowerPoint/Keynote templates
- [ ] Email signature HTML template
- [ ] LinkedIn banner template
- [ ] Conference poster template

---

## Contact & Support

**Questions about logo usage?**
- GitHub Issues: [github.com/gusafr/midora-solid-ai/issues](https://github.com/gusafr/midora-solid-ai/issues)
- Email: (contact information to be added)

**Submit new logo variants or templates:**
- Pull Requests welcome at: [github.com/gusafr/midora-solid-ai](https://github.com/gusafr/midora-solid-ai)

---

**Version:** 1.0 | **Last Updated:** November 6, 2025 | **Framework:** SOLID.AI
