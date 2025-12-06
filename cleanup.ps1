#!/usr/bin/env pwsh
# Cleanup Script for Local Development
# Removes build artifacts, caches, and temporary files

param(
    [Parameter()]
    [ValidateSet('all', 'build', 'docker', 'python', 'cache', 'logs')]
    [string]$Target = 'all',
    
    [Parameter()]
    [switch]$DryRun
)

function Write-Header {
    param([string]$Message)
    Write-Host ""
    Write-Host "=" * 60 -ForegroundColor Cyan
    Write-Host $Message -ForegroundColor Yellow
    Write-Host "=" * 60 -ForegroundColor Cyan
}

function Remove-ItemSafely {
    param(
        [string]$Path,
        [string]$Description
    )
    
    if (Test-Path $Path) {
        $size = if (Test-Path $Path -PathType Container) {
            (Get-ChildItem -Path $Path -Recurse -File | Measure-Object -Property Length -Sum).Sum
        } else {
            (Get-Item $Path).Length
        }
        
        $sizeFormatted = if ($size -gt 1GB) {
            "{0:N2} GB" -f ($size / 1GB)
        } elseif ($size -gt 1MB) {
            "{0:N2} MB" -f ($size / 1MB)
        } elseif ($size -gt 1KB) {
            "{0:N2} KB" -f ($size / 1KB)
        } else {
            "$size bytes"
        }
        
        if ($DryRun) {
            Write-Host "  [DRY RUN] Would remove: $Description ($sizeFormatted)" -ForegroundColor Yellow
        } else {
            Write-Host "  Removing: $Description ($sizeFormatted)" -ForegroundColor Green
            Remove-Item -Path $Path -Recurse -Force -ErrorAction SilentlyContinue
        }
        return $size
    }
    return 0
}

function Cleanup-Build {
    Write-Header "Cleaning Build Artifacts"
    $total = 0
    
    $total += Remove-ItemSafely -Path "./site" -Description "MkDocs build output"
    $total += Remove-ItemSafely -Path "./docs_site/.cache" -Description "MkDocs cache"
    $total += Remove-ItemSafely -Path "./.cache" -Description "General cache"
    
    return $total
}

function Cleanup-Docker {
    Write-Header "Cleaning Docker Resources"
    
    if ($DryRun) {
        Write-Host "  [DRY RUN] Would stop solid-ai containers" -ForegroundColor Yellow
        Write-Host "  [DRY RUN] Would remove solid-ai images" -ForegroundColor Yellow
        Write-Host "  [DRY RUN] Would prune Docker system" -ForegroundColor Yellow
    } else {
        Write-Host "  Stopping solid-ai containers..." -ForegroundColor Green
        docker ps -a --filter "name=solid-ai" --format "{{.Names}}" | ForEach-Object {
            docker rm -f $_ 2>$null
        }
        
        Write-Host "  Removing solid-ai images..." -ForegroundColor Green
        docker images "solid-ai*" --format "{{.ID}}" | ForEach-Object {
            docker rmi -f $_ 2>$null
        }
        
        Write-Host "  Pruning unused Docker resources..." -ForegroundColor Green
        docker system prune -f --volumes
    }
}

function Cleanup-Python {
    Write-Header "Cleaning Python Artifacts"
    $total = 0
    
    $total += Remove-ItemSafely -Path "./__pycache__" -Description "Python cache"
    $total += Remove-ItemSafely -Path "./.pytest_cache" -Description "Pytest cache"
    $total += Remove-ItemSafely -Path "./htmlcov" -Description "Coverage reports"
    $total += Remove-ItemSafely -Path "./.coverage" -Description "Coverage data"
    
    # Find and remove all __pycache__ directories
    Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" -ErrorAction SilentlyContinue | ForEach-Object {
        $total += Remove-ItemSafely -Path $_.FullName -Description "Python cache ($($_.FullName))"
    }
    
    # Find and remove all .pyc files
    Get-ChildItem -Path . -Recurse -File -Filter "*.pyc" -ErrorAction SilentlyContinue | ForEach-Object {
        $total += Remove-ItemSafely -Path $_.FullName -Description "Compiled Python ($($_.Name))"
    }
    
    return $total
}

function Cleanup-Cache {
    Write-Header "Cleaning Cache Files"
    $total = 0
    
    $total += Remove-ItemSafely -Path "./.cache" -Description "General cache"
    $total += Remove-ItemSafely -Path "./node_modules/.cache" -Description "Node modules cache"
    
    return $total
}

function Cleanup-Logs {
    Write-Header "Cleaning Log Files"
    $total = 0
    
    Get-ChildItem -Path . -Recurse -File -Filter "*.log" -ErrorAction SilentlyContinue | ForEach-Object {
        $total += Remove-ItemSafely -Path $_.FullName -Description "Log file ($($_.Name))"
    }
    
    # Remove temporary files
    Get-ChildItem -Path . -Recurse -File -Filter "*.tmp" -ErrorAction SilentlyContinue | ForEach-Object {
        $total += Remove-ItemSafely -Path $_.FullName -Description "Temp file ($($_.Name))"
    }
    
    return $total
}

# Main execution
$totalSize = 0

Write-Host ""
Write-Host "solid.ai Cleanup Script" -ForegroundColor Cyan
Write-Host "======================" -ForegroundColor Cyan
if ($DryRun) {
    Write-Host "MODE: DRY RUN (no files will be deleted)" -ForegroundColor Yellow
} else {
    Write-Host "MODE: ACTIVE (files will be deleted)" -ForegroundColor Red
}

switch ($Target) {
    'all' {
        $totalSize += Cleanup-Build
        $totalSize += Cleanup-Python
        $totalSize += Cleanup-Cache
        $totalSize += Cleanup-Logs
        Cleanup-Docker
    }
    'build' {
        $totalSize += Cleanup-Build
    }
    'docker' {
        Cleanup-Docker
    }
    'python' {
        $totalSize += Cleanup-Python
    }
    'cache' {
        $totalSize += Cleanup-Cache
    }
    'logs' {
        $totalSize += Cleanup-Logs
    }
}

# Summary
Write-Header "Cleanup Summary"

if ($totalSize -gt 0) {
    $sizeFormatted = if ($totalSize -gt 1GB) {
        "{0:N2} GB" -f ($totalSize / 1GB)
    } elseif ($totalSize -gt 1MB) {
        "{0:N2} MB" -f ($totalSize / 1MB)
    } elseif ($totalSize -gt 1KB) {
        "{0:N2} KB" -f ($totalSize / 1KB)
    } else {
        "$totalSize bytes"
    }
    
    if ($DryRun) {
        Write-Host "Would free: $sizeFormatted" -ForegroundColor Yellow
    } else {
        Write-Host "Freed: $sizeFormatted" -ForegroundColor Green
    }
} else {
    Write-Host "No files to clean up" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "Done!" -ForegroundColor Green
Write-Host ""
