# SOLID.AI PDF Book Generators - Quick Reference

## ⚡ Quick Start (Recommended)

```powershell
# Install dependencies (30 seconds)
pip install reportlab markdown2 pygments

# Generate PDF (works immediately)
python scripts/generate_pdf_book_reportlab.py --include-playbooks

# Find your PDF
start output/solid-ai-framework.pdf
```

---

## 📊 Version Comparison

| | ReportLab ⭐ | WeasyPrint |
|---|-------------|------------|
| **Script** | `generate_pdf_book_reportlab.py` | `generate_pdf_book.py` |
| **Installation** | `pip install` (30 sec) | `pip install` + GTK setup (10-30 min) |
| **Windows** | ✅ Works natively | ❌ Requires GTK runtime |
| **macOS** | ✅ Works natively | ⚠️ Requires Homebrew + deps |
| **Linux** | ✅ Works natively | ✅ Works natively |
| **Quality** | ⭐⭐⭐⭐ Professional | ⭐⭐⭐⭐⭐ Premium |
| **File Size** | ~0.18-0.35 MB | ~0.15-0.30 MB (more optimized) |
| **Generation** | ⚡ Fast (5-15s) | Medium (10-30s) |
| **Styling** | ReportLab API | Full CSS support |
| **Status** | ✅ **Ready to use** | ⚠️ Requires setup |

---

## ⭐ Option 1: ReportLab (RECOMMENDED)

**When to use:** Immediate needs, distribution, team collaboration, Windows users

### Pros
- ✅ **Zero setup** - Just `pip install`
- ✅ **Cross-platform** - Works everywhere immediately
- ✅ **Professional output** - Clean, modern design
- ✅ **Fast generation** - 5-15 seconds
- ✅ **Battle-tested** - 20+ years in production

### Cons
- ⚠️ Less CSS flexibility than WeasyPrint
- ⚠️ Simpler styling (but still professional)

### Installation
```powershell
pip install reportlab markdown2 pygments
```

### Usage Examples

```powershell
# Basic (core docs only, ~80 pages)
python scripts/generate_pdf_book_reportlab.py

# With playbooks (~150 pages)
python scripts/generate_pdf_book_reportlab.py --include-playbooks

# Grayscale for printing
python scripts/generate_pdf_book_reportlab.py --color-scheme grayscale

# US Letter size
python scripts/generate_pdf_book_reportlab.py --page-size Letter

# Custom output
python scripts/generate_pdf_book_reportlab.py --output my-custom.pdf
```

### Output
- **File:** `output/solid-ai-framework.pdf`
- **Size:** 0.18 MB (core) → 0.25 MB (with playbooks)
- **Pages:** ~80-150 pages
- **Time:** 5-15 seconds

---

## 🎨 Option 2: WeasyPrint (PREMIUM QUALITY)

**When to use:** Marketing materials, client presentations, perfect design needed

### Pros
- ✅ **Premium quality** - Best HTML/CSS rendering
- ✅ **Beautiful typography** - Web fonts, gradients
- ✅ **Flexible design** - Full CSS control
- ✅ **Smaller files** - Better optimization

### Cons
- ❌ **Complex setup** - Requires GTK on Windows
- ❌ **Platform-specific** - Different install per OS
- ⚠️ **Slower generation** - 10-30 seconds

### Installation

#### Windows (Complex)
1. Download GTK3 Runtime: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer
2. Run installer (use default options)
3. Add GTK `bin` directory to PATH
4. Install Python packages:
   ```powershell
   pip install weasyprint markdown pygments pillow
   ```

#### macOS
```bash
brew install python3 cairo pango gdk-pixbuf libffi
pip install weasyprint markdown pygments pillow
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install python3-pip python3-cffi python3-brotli \
  libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0
pip install weasyprint markdown pygments pillow
```

### Usage Examples

```powershell
# Basic (core docs only)
python scripts/generate_pdf_book.py

# With playbooks
python scripts/generate_pdf_book.py --include-playbooks

# With adoption pack
python scripts/generate_pdf_book.py --include-playbooks --include-adoption

# Grayscale
python scripts/generate_pdf_book.py --color-scheme grayscale

# Letter size
python scripts/generate_pdf_book.py --page-size Letter
```

### Output
- **File:** `output/solid-ai-framework.pdf`
- **Size:** 0.15-0.30 MB (better optimization)
- **Pages:** ~80-250 pages
- **Time:** 10-30 seconds

---

## 🎯 Recommendation by Use Case

### Internal Documentation / Team Distribution
→ **Use ReportLab** 
- Quick to setup
- Easy for team to regenerate
- Professional quality

### Client Presentations / Sales Materials
→ **Use WeasyPrint** (if you can install GTK)
- Premium visual quality
- Worth the setup for client-facing docs

### Print Production
→ **Both work well**
- Use `--color-scheme grayscale`
- Use `--page-size Letter` (US) or `A4` (international)

### Offline Distribution
→ **Use ReportLab**
- Guaranteed to work on recipient's computer
- No compatibility issues

---

## 📖 Complete Documentation

- **ReportLab Guide:** See `scripts/generate_pdf_book_reportlab.py` docstring
- **WeasyPrint Guide:** See `scripts/README.md`
- **Comparison:** See `scripts/PDF_GENERATION_GUIDE.md`

---

## 🆘 Troubleshooting

### ReportLab Issues

**Problem:** `No module named 'reportlab'`
```powershell
pip install reportlab markdown2 pygments
```

**Problem:** Empty or corrupt PDF
- Check that DOCS/ directory exists
- Verify markdown files are UTF-8 encoded

### WeasyPrint Issues

**Problem:** `cannot load library 'gobject-2.0-0'` (Windows)
- Install GTK3 Runtime (see installation above)
- Add GTK bin to PATH
- Restart terminal

**Problem:** `cairo library not found` (macOS)
```bash
brew install cairo pango gdk-pixbuf libffi
```

**Problem:** Slow generation
- This is normal for WeasyPrint
- Consider using ReportLab for faster results

---

## 📝 Sample Output Structure

Both generators create PDFs with:

1. **Cover Page**
   - SOLID.AI branding
   - Version and date
   - Framework subtitle

2. **Table of Contents**
   - Clickable chapter links
   - Page numbers

3. **Core Documentation** (13 chapters)
   - 00: Overview
   - 01: Principles  
   - 02: Architecture
   - 03: Organizational Model
   - 04: Automation & SIPOC
   - 05: AI Agents
   - 06: Governance & Ethics
   - 07: Observability
   - 08: Human-AI Collaboration
   - 09: Whole-Organization Transformation
   - 10: Role Hierarchy
   - 11: AI-Native Agile
   - Glossary

4. **Manifesto** (included automatically)

5. **Playbooks** (if `--include-playbooks`)
   - By-stage (2)
   - By-sector (10)
   - Organizational (5)

6. **Adoption Materials** (if `--include-adoption`)
   - Checklists
   - Prompt templates
   - File templates

7. **Diagrams**
   - Interactive placeholders with web links
   - Directs readers to online diagrams
   - Format: "📊 Diagram: [Name] - View at [URL]"

---

## 📊 Diagram Handling

**Current approach:** Interactive placeholders in PDF that link to the website.

**In the PDF, diagrams appear as:**
```
📊 Diagram: Solid AI Architecture
View this interactive diagram online at:
https://gusafr.github.io/midora-solid-ai/diagrams/
```

**Why placeholders?**
- ✅ No additional dependencies (no Node.js needed)
- ✅ Readers get interactive, zoomable diagrams online
- ✅ Diagrams stay up-to-date with the website
- ✅ Faster PDF generation
- ✅ Smaller file sizes

**Need diagrams embedded in PDF?** See `scripts/PDF_GENERATION_GUIDE.md` for alternatives.

---

## ✅ Tested Configurations

### ReportLab (All Working ✅)
- ✅ Windows 10/11
- ✅ Core docs only
- ✅ With playbooks
- ✅ Color scheme
- ✅ Grayscale scheme
- ✅ A4 page size
- ✅ Letter page size

### WeasyPrint (Setup Required)
- ⚠️ Windows (requires GTK)
- ✅ macOS (with Homebrew)
- ✅ Linux (native)

---

**Last Updated:** November 4, 2025  
**Status:** Production Ready ✅  
**Recommendation:** Start with ReportLab, upgrade to WeasyPrint if needed
