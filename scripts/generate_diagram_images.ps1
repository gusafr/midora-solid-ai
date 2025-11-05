# =========================================================================
# Generate Diagram Images from Mermaid Files
# =========================================================================
# 
# This script converts all .mmd (Mermaid) files to SVG images for:
# - PDF integration (ReportLab can embed SVG)
# - Presentations and reports
# - Archive/backup of visual diagrams
#
# Prerequisites:
#   - Node.js installed
#   - Mermaid CLI: npm install -g @mermaid-js/mermaid-cli
#   - Or use npx (no install): npx -p @mermaid-js/mermaid-cli mmdc
#
# Usage:
#   .\scripts\generate_diagram_images.ps1
#   .\scripts\generate_diagram_images.ps1 -Format png -Width 2400
#   .\scripts\generate_diagram_images.ps1 -DiagramsDir "C:\path\to\diagrams"
#
# =========================================================================

param(
    [string]$DiagramsDir = "DIAGRAMS",
    [string]$OutputDir = "DIAGRAMS/images",
    [ValidateSet("svg", "png", "pdf")]
    [string]$Format = "svg",
    [int]$Width = 1920,
    [int]$Height = 0,  # 0 = auto-calculate based on content
    [string]$BackgroundColor = "white",
    [string]$Theme = "default",
    [switch]$SkipExisting,
    [switch]$Quiet
)

# =========================================================================
# Configuration
# =========================================================================

$ErrorActionPreference = "Stop"
$script:TotalConverted = 0
$script:TotalSkipped = 0
$script:TotalFailed = 0

# =========================================================================
# Helper Functions
# =========================================================================

function Write-Status {
    param([string]$Message, [string]$Type = "Info")
    
    if ($Quiet) { return }
    
    $timestamp = Get-Date -Format "HH:mm:ss"
    switch ($Type) {
        "Success" { Write-Host "[$timestamp] ✅ $Message" -ForegroundColor Green }
        "Warning" { Write-Host "[$timestamp] ⚠️  $Message" -ForegroundColor Yellow }
        "Error"   { Write-Host "[$timestamp] ❌ $Message" -ForegroundColor Red }
        "Info"    { Write-Host "[$timestamp] ℹ️  $Message" -ForegroundColor Cyan }
        default   { Write-Host "[$timestamp] $Message" }
    }
}

function Test-MermaidCLI {
    Write-Status "Checking for Mermaid CLI..." "Info"
    
    # Check if mmdc is available globally
    $mmdc = Get-Command mmdc -ErrorAction SilentlyContinue
    if ($mmdc) {
        $version = & mmdc --version 2>&1
        Write-Status "Found Mermaid CLI: $version" "Success"
        return "mmdc"
    }
    
    # Check if npx is available
    $npx = Get-Command npx -ErrorAction SilentlyContinue
    if ($npx) {
        Write-Status "Mermaid CLI not installed globally, will use npx" "Warning"
        return "npx"
    }
    
    # Neither available
    Write-Status "Mermaid CLI not found!" "Error"
    Write-Host ""
    Write-Host "Please install Mermaid CLI using one of these methods:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  Option 1: Install globally (recommended)" -ForegroundColor White
    Write-Host "    npm install -g @mermaid-js/mermaid-cli" -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Option 2: Install Node.js to use npx" -ForegroundColor White
    Write-Host "    Download from: https://nodejs.org/" -ForegroundColor Gray
    Write-Host ""
    exit 1
}

function Get-MermaidCommand {
    param([string]$CliType)
    
    if ($CliType -eq "mmdc") {
        return "mmdc"
    } else {
        return "npx -y -p @mermaid-js/mermaid-cli mmdc"
    }
}

function Convert-MermaidToImage {
    param(
        [string]$InputFile,
        [string]$OutputFile,
        [string]$MermaidCmd
    )
    
    $inputFileName = Split-Path $InputFile -Leaf
    
    # Check if output already exists and skip if requested
    if ($SkipExisting -and (Test-Path $OutputFile)) {
        Write-Status "Skipping $inputFileName (already exists)" "Info"
        $script:TotalSkipped++
        return $true
    }
    
    Write-Status "Converting $inputFileName..." "Info"
    
    try {
        # Read and clean the mmd file (remove ```mermaid fences if present)
        $content = Get-Content -Path $InputFile -Raw
        $cleanedContent = $content
        
        # Remove code fences if present
        if ($content -match '```mermaid\s*([\s\S]*?)\s*```') {
            $cleanedContent = $matches[1].Trim()
        } elseif ($content -match '````plaintext\s*```mermaid\s*([\s\S]*?)\s*```\s*````') {
            $cleanedContent = $matches[1].Trim()
        }
        
        # Create temporary file with cleaned content
        $tempFile = [System.IO.Path]::GetTempFileName() + ".mmd"
        Set-Content -Path $tempFile -Value $cleanedContent -Encoding UTF8
        
        # Build mmdc command
        $mmArgs = "-i `"$tempFile`" -o `"$OutputFile`" -t $Theme -b $BackgroundColor"
        
        if ($Width -gt 0) {
            $mmArgs += " -w $Width"
        }
        
        if ($Height -gt 0) {
            $mmArgs += " -H $Height"
        }
        
        # Execute conversion
        $fullCmd = "$MermaidCmd $mmArgs"
        $output = Invoke-Expression $fullCmd 2>&1
        
        # Clean up temp file
        Remove-Item -Path $tempFile -ErrorAction SilentlyContinue
        
        if ($LASTEXITCODE -eq 0) {
            # Check if file was created
            if (Test-Path $OutputFile) {
                $fileSize = (Get-Item $OutputFile).Length
                $fileSizeKB = [math]::Round($fileSize / 1KB, 1)
                Write-Status "✓ $inputFileName → $fileSizeKB KB" "Success"
                $script:TotalConverted++
                return $true
            } else {
                Write-Status "Failed to create output file: $OutputFile" "Error"
                $script:TotalFailed++
                return $false
            }
        } else {
            Write-Status "Conversion failed: $output" "Error"
            $script:TotalFailed++
            return $false
        }
    }
    catch {
        Write-Status "Error converting $inputFileName : $_" "Error"
        $script:TotalFailed++
        return $false
    }
}

# =========================================================================
# Main Script
# =========================================================================

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  Mermaid Diagram Image Generator" -ForegroundColor White
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Validate prerequisites
$cliType = Test-MermaidCLI
$mermaidCmd = Get-MermaidCommand -CliType $cliType

# Step 2: Validate input directory
if (-not (Test-Path $DiagramsDir)) {
    Write-Status "Diagrams directory not found: $DiagramsDir" "Error"
    exit 1
}

# Step 3: Find all .mmd files
Write-Status "Scanning for .mmd files in $DiagramsDir..." "Info"
$mmdFiles = Get-ChildItem -Path $DiagramsDir -Filter "*.mmd" -File | Sort-Object Name

if ($mmdFiles.Count -eq 0) {
    Write-Status "No .mmd files found in $DiagramsDir" "Warning"
    exit 0
}

Write-Status "Found $($mmdFiles.Count) diagram(s)" "Success"
Write-Host ""

# Step 4: Create output directory
$outputSubDir = Join-Path $OutputDir $Format
if (-not (Test-Path $outputSubDir)) {
    Write-Status "Creating output directory: $outputSubDir" "Info"
    New-Item -ItemType Directory -Path $outputSubDir -Force | Out-Null
}

# Step 5: Convert each diagram
Write-Status "Converting diagrams to $Format format..." "Info"
Write-Status "Output directory: $outputSubDir" "Info"
Write-Status "Image size: ${Width}px width $(if ($Height -gt 0) { "x ${Height}px height" } else { "(auto height)" })" "Info"
Write-Status "Theme: $Theme | Background: $BackgroundColor" "Info"
Write-Host ""

$startTime = Get-Date

foreach ($mmdFile in $mmdFiles) {
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($mmdFile.Name)
    $outputFileName = "$baseName.$Format"
    $outputFilePath = Join-Path $outputSubDir $outputFileName
    
    Convert-MermaidToImage -InputFile $mmdFile.FullName -OutputFile $outputFilePath -MermaidCmd $mermaidCmd
}

$endTime = Get-Date
$duration = $endTime - $startTime

# Step 6: Generate summary report
Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  Conversion Complete" -ForegroundColor White
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Statistics:" -ForegroundColor White
Write-Host "  ✅ Converted:  $script:TotalConverted" -ForegroundColor Green
Write-Host "  ⏭️  Skipped:    $script:TotalSkipped" -ForegroundColor Yellow
Write-Host "  ❌ Failed:     $script:TotalFailed" -ForegroundColor Red
Write-Host "  ⏱️  Duration:   $($duration.TotalSeconds) seconds" -ForegroundColor Cyan
Write-Host ""

if ($script:TotalConverted -gt 0) {
    Write-Host "Output: $outputSubDir" -ForegroundColor White
    Write-Host ""
    
    # Calculate total size
    $totalSize = (Get-ChildItem -Path $outputSubDir -File | Measure-Object -Property Length -Sum).Sum
    $totalSizeMB = [math]::Round($totalSize / 1MB, 2)
    Write-Host "Total size: $totalSizeMB MB" -ForegroundColor Cyan
    Write-Host ""
}

# Step 7: Create index file
$indexFile = Join-Path $OutputDir "README.md"
Write-Status "Generating image index: $indexFile" "Info"

$indexContent = @"
# Diagram Images

**Generated:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")  
**Format:** $Format  
**Source:** $DiagramsDir  
**Total Diagrams:** $script:TotalConverted

---

## Available Formats

- **SVG** - Scalable vector graphics (best for web, PDF, presentations)
- **PNG** - High-resolution raster images (universal compatibility)
- **PDF** - Portable Document Format (for archival)

---

## Diagrams

| # | Diagram | SVG | PNG | Source |
|---|---------|-----|-----|--------|
"@

$counter = 1
foreach ($mmdFile in $mmdFiles | Sort-Object Name) {
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($mmdFile.Name)
    $title = ($baseName -replace '-', ' ' -replace '_', ' ').Split(' ') | ForEach-Object { 
        (Get-Culture).TextInfo.ToTitleCase($_) 
    }
    $title = $title -join ' '
    
    $svgPath = "svg/$baseName.svg"
    $pngPath = "png/$baseName.png"
    $sourcePath = "../$($mmdFile.Name)"
    
    $svgExists = Test-Path (Join-Path $OutputDir $svgPath)
    $pngExists = Test-Path (Join-Path $OutputDir $pngPath)
    
    $svgLink = if ($svgExists) { "✅ [SVG]($svgPath)" } else { "❌" }
    $pngLink = if ($pngExists) { "✅ [PNG]($pngPath)" } else { "❌" }
    
    $indexContent += "`n| $counter | **$title** | $svgLink | $pngLink | [.mmd]($sourcePath) |"
    $counter++
}

$indexContent += @"


---

## Usage

### In PDF Generation
``````python
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

# Load SVG diagram
drawing = svg2rlg('DIAGRAMS/images/svg/ai-native-safe-model.svg')

# Add to PDF
renderPDF.draw(drawing, canvas, x, y)
``````

### In Markdown Documentation
``````markdown
![AI-Native SAFE Model](../DIAGRAMS/images/svg/ai-native-safe-model.svg)
``````

### In Presentations
- Drag and drop SVG/PNG files into PowerPoint, Google Slides, etc.
- SVG files maintain quality at any zoom level
- PNG files work universally (fallback)

---

## Regeneration

To regenerate all diagrams:

``````powershell
# Generate SVG (default)
.\scripts\generate_diagram_images.ps1

# Generate PNG (high-res)
.\scripts\generate_diagram_images.ps1 -Format png -Width 2400

# Generate both formats
.\scripts\generate_diagram_images.ps1 -Format svg
.\scripts\generate_diagram_images.ps1 -Format png -Width 2400

# Skip existing files (faster)
.\scripts\generate_diagram_images.ps1 -SkipExisting
``````

---

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `-DiagramsDir` | `DIAGRAMS` | Source directory with .mmd files |
| `-OutputDir` | `DIAGRAMS/images` | Output directory for images |
| `-Format` | `svg` | Output format (svg, png, pdf) |
| `-Width` | `1920` | Image width in pixels |
| `-Height` | `0` | Image height (0 = auto) |
| `-BackgroundColor` | `white` | Background color |
| `-Theme` | `default` | Mermaid theme |
| `-SkipExisting` | `false` | Skip files that already exist |
| `-Quiet` | `false` | Suppress progress messages |

---

**Last Updated:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
"@

Set-Content -Path $indexFile -Value $indexContent -Encoding UTF8
Write-Status "Index file created: $indexFile" "Success"

Write-Host ""
Write-Host "Next Steps:" -ForegroundColor White
Write-Host "  1. Review generated images in: $outputSubDir" -ForegroundColor Gray
Write-Host "  2. Integrate with PDF generator (see README.md)" -ForegroundColor Gray
Write-Host "  3. Optionally generate PNG for fallback compatibility" -ForegroundColor Gray
Write-Host ""

exit 0
