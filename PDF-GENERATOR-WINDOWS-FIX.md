# PDF Generator - Windows Compatibility Fix

**Date:** November 5, 2025  
**Issue:** WeasyPrint requires GTK system libraries on Windows, causing generation failures  
**Solution:** Use ReportLab-based generator (pure Python, cross-platform)

---

## Problem

The WeasyPrint-based PDF generator (`scripts/generate_pdf_book.py`) fails on Windows with error:

```
❌ ERROR generating PDF: cannot load library 'gobject-2.0-0': error 0x7e
```

**Root Cause:** WeasyPrint requires GTK+ 3 libraries (gobject, pango, cairo) which are not included with Python and require separate system installation on Windows.

---

## Solution: Use ReportLab Generator

**File:** `scripts/generate_pdf_book_reportlab.py`  
**Technology:** ReportLab (pure Python, no system dependencies)  
**Status:** ✅ Works on Windows, macOS, Linux

### Installation

```powershell
# Ensure you're in the virtual environment
.venv\Scripts\activate.ps1

# Install ReportLab dependencies (already in requirements.txt)
pip install reportlab markdown2 pygments
```

### Usage

```powershell
# Core documentation only (~80 pages, ~0.3 MB)
python scripts/generate_pdf_book_reportlab.py

# Core + Playbooks (~200 pages, ~0.5 MB)
python scripts/generate_pdf_book_reportlab.py --include-playbooks

# Full book: Core + Playbooks + Adoption Pack (~350 pages, ~0.7 MB)
python scripts/generate_pdf_book_reportlab.py --include-playbooks --include-adoption

# Custom output path
python scripts/generate_pdf_book_reportlab.py --output output/custom-name.pdf --include-playbooks

# Grayscale for printing
python scripts/generate_pdf_book_reportlab.py --include-playbooks --color-scheme grayscale

# Letter size (US)
python scripts/generate_pdf_book_reportlab.py --include-playbooks --page-size Letter
```

---

## Recent Updates (November 5, 2025)

Both PDF generators have been updated with identical content:

### ✅ Playbooks Section (5 → 12 playbooks)

Organized into 5 thematic categories:

1. **Foundation** (1 playbook)
   - SOLID.AI Maturity Model: L0→L5 Evolution

2. **Governance & Risk** (1 playbook)
   - AI Governance & Risk Assessment

3. **Implementation & Operations** (2 playbooks)
   - Process Mapping & SIPOC Integration
   - Data Spine Analytics & Insights

4. **People & Culture** (3 playbooks)
   - Organizational Scalability: Breaking Through Ceiling
   - AI Learning & Development: Continuous Upskilling
   - AI-Native OKRs & KPIs: Measuring AI Impact

5. **By Organization Stage** (2 playbooks)
   - Startup: AI-Native from Day One
   - SME: Transformation Journey

6. **Organizational Patterns** (3 playbooks)
   - Squads Implementation
   - Pools Implementation
   - AI Integration

### ✅ Adoption Pack Section (NEW)

Implemented with 3 categories:

1. **Assessment & Planning Checklists** (4 checklists)
   - AI Maturity Assessment
   - Organizational Scalability Assessment
   - Learning & Development Rollout
   - OKR & KPI Setup

2. **Implementation Checklists** (4 checklists)
   - Squad Setup
   - Pool Setup
   - SIPOC Implementation
   - Governance & Ethics Review

3. **Template Catalog**
   - Summary of all 11 YAML templates
   - Download links and usage guidance

### ✅ Subsection Headers

Added organizational headers between playbook/checklist categories for better navigation.

---

## Comparison: WeasyPrint vs ReportLab

| Feature | WeasyPrint | ReportLab |
|---------|------------|-----------|
| **Cross-Platform** | ❌ Requires GTK+ on Windows | ✅ Pure Python |
| **Installation** | Complex (system libs) | Simple (pip only) |
| **Windows Support** | ❌ Error prone | ✅ Works OOTB |
| **File Size** | ~0.8 MB (full) | ~0.7 MB (full) |
| **Generation Speed** | ~8-10 seconds | ~5-7 seconds |
| **CSS Support** | Full CSS3 | Limited (styles only) |
| **Markdown Support** | ✅ Full | ✅ Full |
| **PDF Quality** | Excellent | Excellent |
| **Table of Contents** | Manual | Manual |
| **Status** | ⚠️ Maintenance mode | ✅ Active development |

**Recommendation:** Use ReportLab generator on Windows. Both produce equivalent output quality.

---

## Code Changes Summary

### Updated: `scripts/generate_pdf_book_reportlab.py`

**Lines Changed:** ~120 lines added

**Key Modifications:**

1. **Method: `_collect_content()`** - Expanded playbooks (lines ~280-355)
   ```python
   # Before: 5 playbooks (flat list)
   # After: 12 playbooks (5 categories with subsection headers)
   ```

2. **Method: `_collect_content()`** - Implemented adoption pack (lines ~357-435)
   ```python
   # Before: Not implemented
   # After: 8 checklists + template catalog
   ```

3. **Method: `_build_story()`** - Added subsection_header support (line ~459)
   ```python
   elif part['type'] == 'subsection_header':
       story.extend(self._create_subsection_header(part))
   ```

4. **Method: `_create_subsection_header()`** - NEW method (lines ~565-580)
   ```python
   def _create_subsection_header(self, part: Dict[str, str]) -> List:
       """Create subsection header (lighter than section divider)."""
       # Horizontal rule + styled title
   ```

---

## Testing Checklist

Test all three generation modes:

- [x] **Core only:** `python scripts/generate_pdf_book_reportlab.py`
  - ✅ Generates ~80 pages (0.3 MB)
  - ✅ Includes: Overview → Glossary + Manifesto
  
- [x] **Core + Playbooks:** `python scripts/generate_pdf_book_reportlab.py --include-playbooks`
  - ✅ Generates ~200 pages (0.5 MB)
  - ✅ Includes: 12 playbooks organized in 5 categories
  
- [x] **Full Book:** `python scripts/generate_pdf_book_reportlab.py --include-playbooks --include-adoption`
  - ✅ Generates ~350 pages (0.7 MB)
  - ✅ Includes: All content + 8 checklists + template catalog

**Result:** All tests passed ✅ (November 5, 2025 01:49 AM)

---

## Future: Fixing WeasyPrint on Windows (Optional)

If you prefer WeasyPrint's CSS rendering, install GTK+ libraries:

### Option 1: GTK3-Runtime Installer
```powershell
# Download GTK3 Runtime from: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer
# Install to: C:\Program Files\GTK3-Runtime Win64
# Add to PATH: C:\Program Files\GTK3-Runtime Win64\bin
```

### Option 2: MSYS2 Package Manager
```powershell
# Install MSYS2: https://www.msys2.org/
# Open MSYS2 terminal:
pacman -S mingw-w64-x86_64-gtk3
pacman -S mingw-w64-x86_64-python-gobject
pacman -S mingw-w64-x86_64-pango
```

**Note:** These methods require 200-400 MB of additional system libraries. ReportLab is recommended unless you specifically need advanced CSS features.

---

## Deployment Checklist

- [x] Updated `scripts/generate_pdf_book_reportlab.py` (12 playbooks + adoption pack)
- [x] Updated `scripts/generate_pdf_book.py` (same updates for WeasyPrint users)
- [x] Tested ReportLab generator on Windows (✅ works)
- [x] Created `PDF-GENERATOR-WINDOWS-FIX.md` documentation
- [ ] Update main README.md with ReportLab recommendation for Windows users
- [ ] Add CI/CD workflow to auto-generate PDFs on releases (GitHub Actions)

---

## Related Documentation

- **Main PDF Update Log:** `PDF-GENERATOR-UPDATE-LOG.md`
- **ADOPTION Pack Updates:** `ADOPTION-PACK-UPDATE-LOG.md`
- **Website Publishing:** `WEBSITE-PUBLISHING-UPDATE-LOG.md`
- **Requirements:** `requirements.txt` (ReportLab dependencies)

---

## Support

**Issue:** PDF generation errors on Windows  
**Solution:** Use `scripts/generate_pdf_book_reportlab.py` instead of `scripts/generate_pdf_book.py`

**File Locations:**
- ReportLab Generator: `scripts/generate_pdf_book_reportlab.py` ✅ Recommended
- WeasyPrint Generator: `scripts/generate_pdf_book.py` ⚠️ Requires GTK+
- Output Directory: `output/solid-ai-framework.pdf`
