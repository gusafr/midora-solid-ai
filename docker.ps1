#!/usr/bin/env pwsh
# Docker Helper Script for solid.ai Documentation
# This script provides convenient commands for Docker operations

param(
    [Parameter(Position=0)]
    [ValidateSet('dev', 'build', 'prod', 'stop', 'clean', 'logs', 'test', 'help')]
    [string]$Command = 'help',
    
    [Parameter(Position=1)]
    [string]$Tag = 'latest'
)

function Show-Help {
    Write-Host "solid.ai Docker Helper Script" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Usage: .\docker.ps1 <command> [tag]" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Commands:" -ForegroundColor Green
    Write-Host "  dev        - Run development server with live reload (port 8000)"
    Write-Host "  build      - Build production Docker image"
    Write-Host "  prod       - Run production container (port 8080)"
    Write-Host "  stop       - Stop all running containers"
    Write-Host "  clean      - Remove all containers and images"
    Write-Host "  logs       - Show container logs"
    Write-Host "  test       - Build and test the production image"
    Write-Host "  help       - Show this help message"
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Yellow
    Write-Host "  .\docker.ps1 dev              # Start development server"
    Write-Host "  .\docker.ps1 build v1.0.0     # Build with specific tag"
    Write-Host "  .\docker.ps1 prod             # Run production container"
    Write-Host "  .\docker.ps1 logs             # View logs"
    Write-Host ""
}

function Start-Dev {
    Write-Host "Starting development server with live reload..." -ForegroundColor Green
    docker-compose --profile dev up
}

function Build-Image {
    Write-Host "Building production Docker image: solid-ai:$Tag" -ForegroundColor Green
    docker build -t "solid-ai:$Tag" .
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Build successful!" -ForegroundColor Green
        Write-Host "Image: solid-ai:$Tag" -ForegroundColor Cyan
        
        # Show image size
        $imageInfo = docker images solid-ai:$Tag --format "{{.Size}}"
        Write-Host "Size: $imageInfo" -ForegroundColor Cyan
    } else {
        Write-Host "❌ Build failed!" -ForegroundColor Red
        exit 1
    }
}

function Start-Prod {
    Write-Host "Starting production container..." -ForegroundColor Green
    
    # Check if container already exists
    $existing = docker ps -a --filter "name=solid-ai-prod" --format "{{.Names}}"
    if ($existing) {
        Write-Host "Removing existing container..." -ForegroundColor Yellow
        docker rm -f solid-ai-prod
    }
    
    docker run -d -p 8080:80 --name solid-ai-prod --restart unless-stopped "solid-ai:$Tag"
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Container started successfully!" -ForegroundColor Green
        Write-Host "Access at: http://localhost:8080" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Waiting for health check..." -ForegroundColor Yellow
        Start-Sleep -Seconds 3
        
        try {
            $response = Invoke-WebRequest -Uri "http://localhost:8080/health" -UseBasicParsing -TimeoutSec 5
            if ($response.StatusCode -eq 200) {
                Write-Host "✅ Health check passed!" -ForegroundColor Green
            }
        } catch {
            Write-Host "⚠️  Health check failed. Check logs with: .\docker.ps1 logs" -ForegroundColor Yellow
        }
    } else {
        Write-Host "❌ Failed to start container!" -ForegroundColor Red
        exit 1
    }
}

function Stop-Containers {
    Write-Host "Stopping all solid.ai containers..." -ForegroundColor Yellow
    docker-compose down
    docker stop solid-ai-prod 2>$null
    docker rm solid-ai-prod 2>$null
    Write-Host "✅ All containers stopped" -ForegroundColor Green
}

function Clean-All {
    Write-Host "Cleaning up Docker resources..." -ForegroundColor Yellow
    
    Write-Host "Stopping containers..." -ForegroundColor Cyan
    Stop-Containers
    
    Write-Host "Removing images..." -ForegroundColor Cyan
    docker rmi solid-ai:latest 2>$null
    docker rmi solid-ai:dev 2>$null
    
    Write-Host "Pruning unused resources..." -ForegroundColor Cyan
    docker system prune -f
    
    Write-Host "✅ Cleanup complete!" -ForegroundColor Green
}

function Show-Logs {
    $container = docker ps --filter "name=solid-ai" --format "{{.Names}}" | Select-Object -First 1
    
    if ($container) {
        Write-Host "Showing logs for: $container" -ForegroundColor Cyan
        Write-Host "Press Ctrl+C to exit" -ForegroundColor Yellow
        docker logs -f $container
    } else {
        Write-Host "❌ No running solid.ai containers found" -ForegroundColor Red
        Write-Host "Available containers:" -ForegroundColor Yellow
        docker ps -a --filter "name=solid-ai"
    }
}

function Test-Image {
    Write-Host "Building and testing production image..." -ForegroundColor Green
    
    # Build
    Write-Host "Step 1: Building image..." -ForegroundColor Cyan
    docker build -t solid-ai:test .
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Build failed!" -ForegroundColor Red
        exit 1
    }
    
    # Start test container
    Write-Host "Step 2: Starting test container..." -ForegroundColor Cyan
    docker run -d --name solid-ai-test -p 8081:80 solid-ai:test
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to start container!" -ForegroundColor Red
        exit 1
    }
    
    Start-Sleep -Seconds 5
    
    # Test health endpoint
    Write-Host "Step 3: Testing health endpoint..." -ForegroundColor Cyan
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:8081/health" -UseBasicParsing -TimeoutSec 10
        if ($response.StatusCode -eq 200) {
            Write-Host "✅ Health check passed!" -ForegroundColor Green
        }
    } catch {
        Write-Host "❌ Health check failed!" -ForegroundColor Red
        docker logs solid-ai-test
        docker rm -f solid-ai-test
        exit 1
    }
    
    # Test main page
    Write-Host "Step 4: Testing main page..." -ForegroundColor Cyan
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:8081/" -UseBasicParsing -TimeoutSec 10
        if ($response.StatusCode -eq 200) {
            Write-Host "✅ Main page accessible!" -ForegroundColor Green
        }
    } catch {
        Write-Host "❌ Main page failed!" -ForegroundColor Red
        docker logs solid-ai-test
        docker rm -f solid-ai-test
        exit 1
    }
    
    # Cleanup
    Write-Host "Step 5: Cleaning up..." -ForegroundColor Cyan
    docker rm -f solid-ai-test
    
    Write-Host ""
    Write-Host "✅ All tests passed!" -ForegroundColor Green
    Write-Host "Image is ready for deployment: solid-ai:test" -ForegroundColor Cyan
}

# Main script execution
switch ($Command) {
    'dev'   { Start-Dev }
    'build' { Build-Image }
    'prod'  { Start-Prod }
    'stop'  { Stop-Containers }
    'clean' { Clean-All }
    'logs'  { Show-Logs }
    'test'  { Test-Image }
    'help'  { Show-Help }
    default { Show-Help }
}
