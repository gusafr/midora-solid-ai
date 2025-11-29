# Generate All PDF Versions
# PowerShell script to generate all SOLID.AI PDF documentation

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  SOLID.AI PDF Generation Suite" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$ErrorActionPreference = "Continue"
$outputDir = "output"

# Ensure output directory exists
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

# Track success/failure
$generated = @()
$failed = @()

# 1. Whitepaper (A4)
Write-Host "1. Generating Whitepaper (A4)..." -ForegroundColor Green
try {
    python scripts/generate_whitepaper_pdf.py --output "$outputDir/solid-ai-whitepaper-a4.pdf"
    if ($LASTEXITCODE -eq 0) {
        $generated += "Whitepaper (A4)"
    } else {
        $failed += "Whitepaper (A4)"
    }
} catch {
    Write-Host "   Failed" -ForegroundColor Red
    $failed += "Whitepaper (A4)"
}

# 2. Whitepaper (Letter)
Write-Host "`n2. Generating Whitepaper (Letter)..." -ForegroundColor Green
try {
    python scripts/generate_whitepaper_pdf.py --page-size Letter --output "$outputDir/solid-ai-whitepaper-letter.pdf"
    if ($LASTEXITCODE -eq 0) {
        $generated += "Whitepaper (Letter)"
    } else {
        $failed += "Whitepaper (Letter)"
    }
} catch {
    Write-Host "   Failed" -ForegroundColor Red
    $failed += "Whitepaper (Letter)"
}

# 3. Core Framework
Write-Host "`n3. Generating Core Framework..." -ForegroundColor Green
try {
    python scripts/generate_pdf_book_reportlab.py --output "$outputDir/solid-ai-core.pdf"
    if ($LASTEXITCODE -eq 0) {
        $generated += "Core Framework"
    } else {
        $failed += "Core Framework"
    }
} catch {
    Write-Host "   Failed" -ForegroundColor Red
    $failed += "Core Framework"
}

# 4. Framework with Playbooks
Write-Host "`n4. Generating Framework + Playbooks..." -ForegroundColor Green
try {
    python scripts/generate_pdf_book_reportlab.py --include-playbooks --output "$outputDir/solid-ai-with-playbooks.pdf"
    if ($LASTEXITCODE -eq 0) {
        $generated += "Framework + Playbooks"
    } else {
        $failed += "Framework + Playbooks"
    }
} catch {
    Write-Host "   Failed" -ForegroundColor Red
    $failed += "Framework + Playbooks"
}

# 5. Complete Documentation
Write-Host "`n5. Generating Complete Documentation..." -ForegroundColor Green
try {
    python scripts/generate_pdf_book_reportlab.py --include-playbooks --include-adoption --output "$outputDir/solid-ai-complete.pdf"
    if ($LASTEXITCODE -eq 0) {
        $generated += "Complete Documentation"
    } else {
        $failed += "Complete Documentation"
    }
} catch {
    Write-Host "   Failed" -ForegroundColor Red
    $failed += "Complete Documentation"
}

# 6. Grayscale Print Version
Write-Host "`n6. Generating Grayscale Print Version..." -ForegroundColor Green
try {
    python scripts/generate_pdf_book_reportlab.py --color-scheme grayscale --output "$outputDir/solid-ai-print-bw.pdf"
    if ($LASTEXITCODE -eq 0) {
        $generated += "Grayscale Print Version"
    } else {
        $failed += "Grayscale Print Version"
    }
} catch {
    Write-Host "   Failed" -ForegroundColor Red
    $failed += "Grayscale Print Version"
}

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Generation Summary" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

if ($generated.Count -gt 0) {
    Write-Host "`nSuccessfully Generated:" -ForegroundColor Green
    foreach ($doc in $generated) {
        Write-Host "   $doc" -ForegroundColor Green
    }
}

if ($failed.Count -gt 0) {
    Write-Host "`nFailed:" -ForegroundColor Red
    foreach ($doc in $failed) {
        Write-Host "   $doc" -ForegroundColor Red
    }
}

# List generated files
Write-Host "`nOutput Directory:" -ForegroundColor Cyan
Get-ChildItem -Path $outputDir -Filter "*.pdf" | ForEach-Object {
    $sizeKB = [math]::Round($_.Length / 1KB, 1)
    Write-Host "   $($_.Name) - $sizeKB KB" -ForegroundColor White
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Generation complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
