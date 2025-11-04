# PDF Book Generation Guide

## Problem: WeasyPrint System Dependencies

The original `generate_pdf_book.py` uses **WeasyPrint**, which requires system-level libraries (GTK, cairo, etc.) that can be challenging to install on Windows.

**Error encountered:**
```
❌ ERROR: cannot load library 'gobject-2.0-0'
```

## Solution: Two Options Available

### Option 1: WeasyPrint (Premium Quality, Complex Setup)

**Script:** `generate_pdf_book.py`

**Pros:**
- ✅ Best HTML/CSS rendering
- ✅ Beautiful typography
- ✅ Professional design quality
- ✅ Supports complex layouts

**Cons:**
- ❌ Requires system libraries (GTK)
- ❌ Complex Windows installation
- ❌ Platform-specific setup

**Installation (Windows):**
1. Download GTK3 from: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer
2. Run installer (use default options)
3. Add GTK bin directory to PATH
4. Install Python packages:
   ```powershell
   pip install weasyprint markdown pygments pillow
   ```

**Usage:**
```powershell
python scripts/generate_pdf_book.py --include-playbooks --include-adoption
```

---

### Option 2: ReportLab (Works Everywhere, Good Quality) ⭐ RECOMMENDED

**Script:** `generate_pdf_book_reportlab.py`

**Pros:**
- ✅ **Pure Python** (no system dependencies)
- ✅ **Works on Windows, macOS, Linux** immediately
- ✅ Fast installation (`pip install`)
- ✅ Professional quality output
- ✅ Battle-tested library (20+ years)

**Cons:**
- ⚠️ Less flexible than WeasyPrint for complex CSS
- ⚠️ Simpler styling (still professional)

**Installation:**
```powershell
pip install reportlab markdown2 pygments
```

**Usage:**
```powershell
# Basic (core docs only)
python scripts/generate_pdf_book_reportlab.py

# With playbooks
python scripts/generate_pdf_book_reportlab.py --include-playbooks

# Full book
python scripts/generate_pdf_book_reportlab.py --include-playbooks --include-adoption

# Grayscale for printing
python scripts/generate_pdf_book_reportlab.py --color-scheme grayscale

# US Letter size
python scripts/generate_pdf_book_reportlab.py --page-size Letter
```

---

## Quick Start (Recommended Path)

**For immediate results on any platform:**

```powershell
# 1. Install dependencies (already done if you see this)
pip install reportlab markdown2 pygments

# 2. Generate PDF
python scripts/generate_pdf_book_reportlab.py --include-playbooks

# 3. Find your PDF
# Location: output/solid-ai-framework.pdf
```

---

## Comparison Table

| Feature | WeasyPrint | ReportLab |
|---------|------------|-----------|
| **Installation** | Complex (system deps) | Simple (`pip install`) |
| **Windows Support** | ❌ Difficult | ✅ Native |
| **macOS Support** | ⚠️ Requires brew | ✅ Native |
| **Linux Support** | ✅ Good | ✅ Good |
| **Styling Quality** | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐ Very Good |
| **Rendering Speed** | Medium | Fast |
| **File Size** | Smaller (optimized) | Slightly larger |
| **Maintenance** | Active | Very Active |
| **Use Cases** | Perfect designs | Professional docs |

---

## Output Comparison

Both scripts produce professional PDFs with:
- ✅ Cover page with SOLID.AI branding
- ✅ Table of contents
- ✅ 13 core documentation chapters
- ✅ SOLID.AI Manifesto
- ✅ Optional playbooks
- ✅ Optional adoption materials
- ✅ Headers and footers
- ✅ Page numbers
- ✅ Professional typography

**WeasyPrint advantages:**
- More flexible CSS
- Better web font support
- Smoother gradients
- Potential diagram rendering (Mermaid)

**ReportLab advantages:**
- Faster generation
- More control over page elements
- Better table handling
- No external dependencies

---

## Recommendation by Use Case

### For Distribution (External Stakeholders)
→ **Use ReportLab** (`generate_pdf_book_reportlab.py`)
- Guaranteed to work on any computer
- Professional appearance
- Fast generation

### For Marketing/Sales Materials
→ **Use WeasyPrint** (`generate_pdf_book.py`) *if you can install GTK*
- Premium design quality
- Best visual presentation
- Worth the setup effort for client-facing materials

### For Internal Documentation
→ **Use ReportLab** (`generate_pdf_book_reportlab.py`)
- Quick to regenerate
- Easy for team members to run
- No technical barriers

### For Printing
→ **Both work well**
- Use `--color-scheme grayscale` for black & white printing
- Use `--page-size Letter` for US standard
- Use `--page-size A4` for international

---

## Troubleshooting

### WeasyPrint Issues

**Problem:** `cannot load library 'gobject-2.0-0'`
- **Solution:** Install GTK runtime (see Option 1 installation)

**Problem:** `cairo library not found`
- **Solution:** Ensure GTK bin directory is in PATH

**Problem:** Slow generation
- **Solution:** This is normal for WeasyPrint, be patient

### ReportLab Issues

**Problem:** `ImportError: No module named 'reportlab'`
- **Solution:** `pip install reportlab markdown2 pygments`

**Problem:** Text encoding errors
- **Solution:** Ensure markdown files are UTF-8 encoded

**Problem:** Missing content
- **Solution:** Check that DOCS/ and PLAYBOOKS/ directories exist

---

## Diagram Handling

### Current Approach: Interactive Placeholders

The PDF generator handles Mermaid diagrams by creating **interactive placeholders** that direct readers to the online documentation:

**What appears in the PDF:**
```
📊 Diagram: Solid AI Architecture
View this interactive diagram online at:
https://gusafr.github.io/midora-solid-ai/diagrams/
```

**Benefits:**
- ✅ PDFs generate successfully without errors
- ✅ Readers are informed about diagram availability
- ✅ Links direct to interactive, zoomable versions
- ✅ No additional dependencies required
- ✅ Smaller PDF file sizes

**Alternatives (if needed in the future):**
1. **Pre-render to PNG**: Install Mermaid CLI and convert diagrams to images
2. **Mermaid Live API**: Auto-render diagrams via web service during generation
3. **Manual export**: Save diagrams as images and embed them

For most use cases, the current placeholder approach is **recommended** because:
- Users can interact with diagrams online (zoom, pan, click)
- Diagrams remain up-to-date with the website
- Simpler build process without Node.js dependency

---

## Next Steps

1. **Try ReportLab first** (easiest):
   ```powershell
   python scripts/generate_pdf_book_reportlab.py --include-playbooks
   ```

2. **If you need premium quality**, install GTK and try WeasyPrint:
   ```powershell
   # After installing GTK
   python scripts/generate_pdf_book.py --include-playbooks
   ```

3. **Customize the output:**
   - Edit CSS in the script files
   - Adjust colors, fonts, spacing
   - Add custom sections

---

## Support

- **ReportLab Documentation:** https://www.reportlab.com/docs/reportlab-userguide.pdf
- **WeasyPrint Documentation:** https://doc.courtbouillon.org/weasyprint/stable/
- **SOLID.AI Framework:** https://github.com/gusafr/midora-solid-ai

---

**Last Updated:** November 4, 2025  
**Version:** 1.1  
**Status:** Production Ready ✅
