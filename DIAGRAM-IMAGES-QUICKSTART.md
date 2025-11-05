# Diagram Image Generation - Quick Start Guide

This guide explains how to generate SVG/PNG images from Mermaid diagrams and integrate them into PDFs.

---

## Overview

**Problem:** Mermaid diagrams (`.mmd` files) need to be converted to images for:
- PDF embedding (ReportLab can't render Mermaid directly)
- Presentations and reports
- Archival and backup

**Solution:** Use Mermaid CLI to convert `.mmd` → `.svg` (scalable vector graphics)

---

## Prerequisites

### Option 1: Install Mermaid CLI Globally (Recommended)

```powershell
# Install globally (requires Node.js)
npm install -g @mermaid-js/mermaid-cli

# Verify installation
mmdc --version
```

### Option 2: Use npx (No Global Install)

If you have Node.js installed, you can use `npx` without installing Mermaid CLI globally. The script will automatically use `npx` if `mmdc` is not found.

---

## Quick Start

### Step 1: Generate SVG Diagrams

```powershell
# Generate all diagrams as SVG (default, recommended)
.\scripts\generate_diagram_images.ps1

# Output: DIAGRAMS/images/svg/*.svg (24 files)
```

### Step 2: Install SVG Support for PDF (Optional)

```powershell
# Install svglib for PDF embedding
pip install svglib

# Or install all requirements
pip install -r requirements.txt
```

### Step 3: Generate PDF with Embedded Diagrams

```powershell
# Generate PDF with all content
python scripts/generate_pdf_book_reportlab.py --include-playbooks --include-adoption

# Output: output/solid-ai-framework.pdf
# - Core docs: ~350 pages
# - Embedded diagrams: 24 SVG images
# - File size: ~2-3 MB
```

---

## Directory Structure

After running the diagram generation script:

```
DIAGRAMS/
├── images/                        ⭐ NEW
│   ├── svg/                       ⭐ Scalable vector graphics
│   │   ├── ai-native-safe-model.svg
│   │   ├── ai-native-sprint-flow.svg
│   │   └── ... (24 total)
│   ├── png/                       (Optional, high-res raster)
│   │   └── ... (if generated)
│   └── README.md                  ⭐ Index with usage examples
├── ai-native-safe-model.mmd       (Source files)
├── ai-native-sprint-flow.mmd
└── ... (24 .mmd files)
```

---

## Usage Examples

### Generate SVG Diagrams (Default)

```powershell
.\scripts\generate_diagram_images.ps1
```

**Output:**
```
=========================================
  Mermaid Diagram Image Generator
=========================================

✅ Found Mermaid CLI: 11.x.x
ℹ️  Scanning for .mmd files in DIAGRAMS...
✅ Found 24 diagram(s)

ℹ️  Converting diagrams to svg format...
ℹ️  Output directory: DIAGRAMS/images/svg
ℹ️  Image size: 1920px width (auto height)
ℹ️  Theme: default | Background: white

ℹ️  Converting ai-native-safe-model.mmd...
✅ ✓ ai-native-safe-model.mmd → 45.3 KB

... (repeat for all 24 diagrams)

=========================================
  Conversion Complete
=========================================

✅ Converted:  24
⏭️  Skipped:    0
❌ Failed:     0
⏱️  Duration:   38.5 seconds

Output: DIAGRAMS/images/svg
Total size: 1.2 MB
```

### Generate PNG Diagrams (High-Resolution)

```powershell
# Generate PNG at 2400px width (300 DPI for printing)
.\scripts\generate_diagram_images.ps1 -Format png -Width 2400

# Output: DIAGRAMS/images/png/*.png
```

### Generate Both Formats

```powershell
# Generate SVG (for web/PDF)
.\scripts\generate_diagram_images.ps1 -Format svg

# Generate PNG (for compatibility)
.\scripts\generate_diagram_images.ps1 -Format png -Width 2400
```

### Skip Existing Files (Faster)

```powershell
# Only convert new/modified diagrams
.\scripts\generate_diagram_images.ps1 -SkipExisting
```

---

## Script Options

| Parameter | Default | Description |
|-----------|---------|-------------|
| `-DiagramsDir` | `DIAGRAMS` | Source directory with .mmd files |
| `-OutputDir` | `DIAGRAMS/images` | Output directory for images |
| `-Format` | `svg` | Output format: svg, png, pdf |
| `-Width` | `1920` | Image width in pixels |
| `-Height` | `0` | Image height (0 = auto-calculate) |
| `-BackgroundColor` | `white` | Background color |
| `-Theme` | `default` | Mermaid theme (default, dark, forest, neutral) |
| `-SkipExisting` | `false` | Skip files that already exist |
| `-Quiet` | `false` | Suppress progress messages |

---

## PDF Integration

### How It Works

1. **Script detects diagrams:** Looks for `--8<--` markers in markdown
2. **Finds SVG file:** Checks `DIAGRAMS/images/svg/{name}.svg`
3. **Embeds in PDF:** Uses `svglib` to convert SVG → ReportLab Drawing
4. **Fallback:** If SVG not found, shows placeholder with web link

### Example Output

**With SVG Support (✅ svglib installed):**
```
✅ SVG diagram support enabled

Processing: DOCS/02-architecture.md
  📊 Embedding diagram: AI-Native SAFE Model
  ✓ SVG loaded: 45.3 KB
  
... (repeat for all diagrams)

PDF generated: output/solid-ai-framework.pdf
  Pages: 385
  Size: 2.4 MB
  Diagrams: 24 embedded
```

**Without SVG Support (⚠️ svglib not installed):**
```
⚠️  SVG diagram support disabled (install svglib: pip install svglib)

Processing: DOCS/02-architecture.md
  📊 Placeholder: AI-Native SAFE Model
  ℹ️  View online: https://gusafr.github.io/...
  
... (repeat for all diagrams)

PDF generated: output/solid-ai-framework.pdf
  Pages: 375
  Size: 0.8 MB
  Diagrams: 24 placeholders
```

---

## Workflow

### Initial Setup (One-Time)

```powershell
# 1. Install Node.js (if not already installed)
#    Download from: https://nodejs.org/

# 2. Install Mermaid CLI
npm install -g @mermaid-js/mermaid-cli

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Generate all diagram images
.\scripts\generate_diagram_images.ps1
```

### Regular Updates (When Diagrams Change)

```powershell
# 1. Edit .mmd files in DIAGRAMS/

# 2. Regenerate images
.\scripts\generate_diagram_images.ps1 -SkipExisting

# 3. Generate PDF
python scripts/generate_pdf_book_reportlab.py --include-playbooks --include-adoption
```

---

## Troubleshooting

### Error: "Mermaid CLI not found"

**Solution:**
```powershell
# Install Mermaid CLI globally
npm install -g @mermaid-js/mermaid-cli

# Or verify Node.js is installed
node --version
npm --version
```

### Warning: "SVG diagram support disabled"

**Solution:**
```powershell
# Install svglib
pip install svglib

# Or reinstall all requirements
pip install -r requirements.txt
```

### Diagrams Not Embedded in PDF

**Check:**
1. SVG files exist: `DIAGRAMS/images/svg/*.svg`
2. Filenames match: `ai-native-safe-model.mmd` → `ai-native-safe-model.svg`
3. svglib installed: `pip show svglib`

**Solution:**
```powershell
# Regenerate diagrams
.\scripts\generate_diagram_images.ps1

# Verify SVG files created
dir DIAGRAMS\images\svg\*.svg

# Regenerate PDF
python scripts/generate_pdf_book_reportlab.py --include-playbooks --include-adoption
```

### Low-Quality Diagrams in PDF

**Solution: Increase PNG resolution**
```powershell
# Generate high-res PNG (2400px = 300 DPI)
.\scripts\generate_diagram_images.ps1 -Format png -Width 2400

# Or use SVG (always high quality)
.\scripts\generate_diagram_images.ps1 -Format svg
```

---

## Best Practices

### 1. Use SVG for Production
- ✅ Scalable (looks good at any zoom level)
- ✅ Small file size (~40-60 KB per diagram)
- ✅ Perfect for web and PDF
- ✅ Editable with vector tools

### 2. Keep PNG as Fallback
- ✅ Universal compatibility
- ✅ Works without svglib
- ⚠️ Larger file size (~200-400 KB per diagram)
- ⚠️ Fixed resolution

### 3. Commit Generated Images to Git
```powershell
# Add to version control
git add DIAGRAMS/images/svg/*.svg
git commit -m "docs: Regenerate diagram images"
```

**Why?**
- Contributors don't need Node.js
- CI/CD pipelines can generate PDFs without Mermaid CLI
- Faster PDF generation (no conversion step)

### 4. Update Images When Diagrams Change
```powershell
# After editing .mmd files
.\scripts\generate_diagram_images.ps1 -SkipExisting
git add DIAGRAMS/images/svg/*.svg
git commit -m "docs: Update diagram images"
```

---

## Performance

### Diagram Generation
- **SVG:** ~1-2 seconds per diagram
- **PNG:** ~1.5-3 seconds per diagram (larger size)
- **Total (24 diagrams):** ~30-60 seconds

### PDF Generation (with diagrams)
- **With svglib:** ~22-28 seconds (385 pages, 2.4 MB)
- **Without svglib:** ~18-22 seconds (375 pages, 0.8 MB)

### File Sizes
- **SVG:** ~40-60 KB per diagram → ~1.2 MB total
- **PNG (1920px):** ~150-250 KB per diagram → ~4 MB total
- **PNG (2400px):** ~250-400 KB per diagram → ~7 MB total

---

## Next Steps

1. ✅ **Generate diagrams:** `.\scripts\generate_diagram_images.ps1`
2. ✅ **Install svglib:** `pip install svglib`
3. ✅ **Generate PDF:** `python scripts/generate_pdf_book_reportlab.py --include-playbooks --include-adoption`
4. ✅ **Review output:** `output/solid-ai-framework.pdf`
5. ✅ **Commit images:** `git add DIAGRAMS/images/svg/*.svg`

---

**Last Updated:** November 5, 2025  
**Scripts:**
- `scripts/generate_diagram_images.ps1` - Mermaid → SVG/PNG conversion
- `scripts/svg_helper.py` - SVG → ReportLab integration
- `scripts/generate_pdf_book_reportlab.py` - PDF generation with diagrams
