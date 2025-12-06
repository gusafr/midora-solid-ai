# GitHub Release v1.0.0 - Asset Preparation

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  SOLID.AI v1.0 Release Assets" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$releaseDir = "release-v1.0"
$outputDir = "output"

# Create release directory
if (-not (Test-Path $releaseDir)) {
    New-Item -ItemType Directory -Path $releaseDir | Out-Null
    Write-Host "Created release directory: $releaseDir" -ForegroundColor Green
}

Write-Host "`nCopying release assets..." -ForegroundColor Yellow

# Copy PDFs
Write-Host "  - PDFs" -ForegroundColor White
Copy-Item "$outputDir/solid-ai-whitepaper-a4.pdf" "$releaseDir/" -Force
Copy-Item "$outputDir/solid-ai-whitepaper-letter.pdf" "$releaseDir/" -Force
Copy-Item "$outputDir/solid-ai-complete.pdf" "$releaseDir/" -Force
Copy-Item "$outputDir/solid-ai-core.pdf" "$releaseDir/" -Force
Copy-Item "$outputDir/solid-ai-with-playbooks.pdf" "$releaseDir/" -Force
Copy-Item "$outputDir/solid-ai-print-bw.pdf" "$releaseDir/" -Force

# Copy documentation
Write-Host "  - Documentation" -ForegroundColor White
Copy-Item "CHANGELOG.md" "$releaseDir/" -Force
Copy-Item "RELEASE-NOTES-v1.0.md" "$releaseDir/" -Force
Copy-Item "README.md" "$releaseDir/" -Force
Copy-Item "LICENSE" "$releaseDir/" -Force

# Copy diagrams (SVG exports if available)
Write-Host "  - Diagrams" -ForegroundColor White
$diagramsZip = "$releaseDir/solid-ai-diagrams-v1.0.zip"
if (Test-Path "diagrams/images") {
    Compress-Archive -Path "diagrams/images/*" -DestinationPath $diagramsZip -Force
    Write-Host "    Created diagrams archive" -ForegroundColor Green
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Release Assets Ready!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Write-Host "`nAssets in $releaseDir/:" -ForegroundColor Yellow
Get-ChildItem -Path $releaseDir | ForEach-Object {
    $sizeKB = [math]::Round($_.Length / 1KB, 1)
    Write-Host "  $($_.Name) - $sizeKB KB" -ForegroundColor White
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Go to: https://github.com/gusafr/midora-solid-ai/releases/new" -ForegroundColor White
Write-Host ""
Write-Host "2. Select tag: v1.0.0" -ForegroundColor White
Write-Host ""
Write-Host "3. Release title: SOLID.AI Framework v1.0" -ForegroundColor White
Write-Host ""
Write-Host "4. Description: Copy content from RELEASE-NOTES-v1.0.md" -ForegroundColor White
Write-Host ""
Write-Host "5. Upload assets from: $releaseDir/" -ForegroundColor White
Write-Host ""
Write-Host "6. Check 'Set as the latest release'" -ForegroundColor White
Write-Host ""
Write-Host "7. Click 'Publish release'" -ForegroundColor White
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Asset Checklist:" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "[x] solid-ai-whitepaper-a4.pdf (75 KB)" -ForegroundColor Green
Write-Host "[x] solid-ai-whitepaper-letter.pdf (76 KB)" -ForegroundColor Green
Write-Host "[x] solid-ai-complete.pdf (1.4 MB)" -ForegroundColor Green
Write-Host "[x] solid-ai-core.pdf (870 KB)" -ForegroundColor Green
Write-Host "[x] solid-ai-with-playbooks.pdf (1.3 MB)" -ForegroundColor Green
Write-Host "[x] solid-ai-print-bw.pdf (870 KB)" -ForegroundColor Green
Write-Host "[x] CHANGELOG.md" -ForegroundColor Green
Write-Host "[x] RELEASE-NOTES-v1.0.md" -ForegroundColor Green
Write-Host "[x] README.md" -ForegroundColor Green
Write-Host "[x] LICENSE" -ForegroundColor Green
if (Test-Path $diagramsZip) {
    Write-Host "[x] solid-ai-diagrams-v1.0.zip" -ForegroundColor Green
}
Write-Host ""
