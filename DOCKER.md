# Docker Setup for solid.ai Documentation

This guide explains how to build, run, and deploy the solid.ai documentation site using Docker.

## Prerequisites

- Docker Desktop installed ([download here](https://www.docker.com/products/docker-desktop))
- Docker Compose (included with Docker Desktop)

## Quick Start

### Option 1: Development Mode (Live Reload)

Run the documentation with **live reload** for active development:

```powershell
# Using docker-compose
docker-compose --profile dev up

# Or using Docker directly
docker build -f Dockerfile.dev -t solid-ai:dev .
docker run -p 8000:8000 -v ${PWD}:/docs solid-ai:dev
```

Access the site at: **http://localhost:8000**

Changes to markdown files will automatically reload the browser.

### Option 2: Production Build

Build and run the **production-optimized** site with nginx:

```powershell
# Build the Docker image
docker build -t solid-ai:latest .

# Run the container
docker run -d -p 8080:80 --name solid-ai-docs solid-ai:latest

# Or use docker-compose
docker-compose --profile prod up -d
```

Access the site at: **http://localhost:8080**

### Option 3: Local Production Test

Build the site locally and serve with nginx:

```powershell
# Build the site
.venv\Scripts\python.exe -m mkdocs build

# Serve with nginx using docker-compose
docker-compose --profile local-prod up
```

Access the site at: **http://localhost:8080**

## Docker Commands

### Build Commands

```powershell
# Build development image
docker build -f Dockerfile.dev -t solid-ai:dev .

# Build production image
docker build -t solid-ai:prod .

# Build with specific tag (version)
docker build -t solid-ai:v1.0.0 .

# Build without cache (force rebuild)
docker build --no-cache -t solid-ai:latest .
```

### Run Commands

```powershell
# Run development container (interactive)
docker run -it --rm -p 8000:8000 -v ${PWD}:/docs solid-ai:dev

# Run production container (detached)
docker run -d -p 8080:80 --name solid-ai-prod solid-ai:prod

# Run with custom name and restart policy
docker run -d -p 8080:80 --name solid-ai --restart unless-stopped solid-ai:latest
```

### Container Management

```powershell
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# View container logs
docker logs solid-ai-prod
docker logs -f solid-ai-prod  # Follow logs

# Stop container
docker stop solid-ai-prod

# Start stopped container
docker start solid-ai-prod

# Remove container
docker rm solid-ai-prod

# Remove container forcefully
docker rm -f solid-ai-prod
```

### Image Management

```powershell
# List images
docker images

# Remove image
docker rmi solid-ai:latest

# Remove all unused images
docker image prune

# Tag image for registry
docker tag solid-ai:latest ghcr.io/gusafr/solid-ai:latest

# Push to registry
docker push ghcr.io/gusafr/solid-ai:latest
```

### Docker Compose Commands

```powershell
# Start development environment
docker-compose --profile dev up

# Start production environment (detached)
docker-compose --profile prod up -d

# Stop all services
docker-compose down

# Rebuild and start
docker-compose --profile prod up -d --build

# View logs
docker-compose logs -f

# Remove all containers and volumes
docker-compose down -v
```

## Deployment Scenarios

### 1. Deploy to Cloud Run (Google Cloud)

```powershell
# Build and push to Google Container Registry
docker build -t gcr.io/PROJECT_ID/solid-ai:latest .
docker push gcr.io/PROJECT_ID/solid-ai:latest

# Deploy to Cloud Run
gcloud run deploy solid-ai \
  --image gcr.io/PROJECT_ID/solid-ai:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### 2. Deploy to AWS ECS/Fargate

```powershell
# Build and push to Amazon ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
docker build -t solid-ai:latest .
docker tag solid-ai:latest ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/solid-ai:latest
docker push ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/solid-ai:latest

# Create ECS task definition and service (use AWS Console or CLI)
```

### 3. Deploy to Azure Container Instances

```powershell
# Build and push to Azure Container Registry
az acr login --name myregistry
docker build -t solid-ai:latest .
docker tag solid-ai:latest myregistry.azurecr.io/solid-ai:latest
docker push myregistry.azurecr.io/solid-ai:latest

# Deploy to Azure Container Instances
az container create \
  --resource-group myResourceGroup \
  --name solid-ai-docs \
  --image myregistry.azurecr.io/solid-ai:latest \
  --dns-name-label solid-ai-docs \
  --ports 80
```

### 4. Deploy to Kubernetes

Create `k8s-deployment.yml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: solid-ai-docs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: solid-ai-docs
  template:
    metadata:
      labels:
        app: solid-ai-docs
    spec:
      containers:
      - name: solid-ai
        image: solid-ai:latest
        ports:
        - containerPort: 80
        livenessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: solid-ai-service
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: solid-ai-docs
```

Deploy:

```powershell
kubectl apply -f k8s-deployment.yml
```

## CI/CD Integration

### GitHub Actions Example

Create `.github/workflows/docker-publish.yml`:

```yaml
name: Build and Push Docker Image

on:
  push:
    branches: [ main ]
    tags: [ 'v*' ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      
      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v4
        with:
          images: ghcr.io/${{ github.repository }}
      
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

## Troubleshooting

### Container won't start

```powershell
# Check container logs
docker logs solid-ai-prod

# Inspect container
docker inspect solid-ai-prod

# Run interactively to debug
docker run -it --rm solid-ai:latest sh
```

### Port already in use

```powershell
# Find process using port 8080
netstat -ano | findstr :8080

# Use different port
docker run -p 8081:80 solid-ai:latest
```

### Build fails

```powershell
# Clean build without cache
docker build --no-cache -t solid-ai:latest .

# Check build context size
docker build --progress=plain -t solid-ai:latest .
```

### Health check failing

```powershell
# Test health endpoint
docker exec solid-ai-prod wget -O- http://localhost/health

# Check nginx logs
docker exec solid-ai-prod cat /var/log/nginx/error.log
```

## Best Practices

1. **Use multi-stage builds** (already implemented) - Reduces final image size
2. **Tag images with versions** - Use semantic versioning for releases
3. **Don't run as root** - Consider adding a non-root user in production
4. **Use .dockerignore** - Exclude unnecessary files from build context
5. **Set resource limits** - Prevent container from consuming all host resources
6. **Enable health checks** - Ensure container is actually serving traffic
7. **Use environment variables** - For configurable settings
8. **Scan for vulnerabilities** - Use `docker scan solid-ai:latest`

## Performance Optimization

### Image Size Comparison

- **Development image:** ~500 MB (includes Python, MkDocs, all dependencies)
- **Production image:** ~25 MB (nginx:alpine + static site)

### Build Time Optimization

```powershell
# Use BuildKit for faster builds
$env:DOCKER_BUILDKIT=1
docker build -t solid-ai:latest .

# Enable build cache
docker build --cache-from solid-ai:latest -t solid-ai:latest .
```

## Security Considerations

1. **Scan images regularly:**
   ```powershell
   docker scan solid-ai:latest
   ```

2. **Use official base images** (already implemented: `python:3.11-slim`, `nginx:alpine`)

3. **Keep base images updated:**
   ```powershell
   docker pull python:3.11-slim
   docker pull nginx:alpine
   docker build --pull -t solid-ai:latest .
   ```

4. **Run as non-root user** (add to Dockerfile if needed)

5. **Enable Content Security Policy** (add to nginx.conf if needed)

---

## Support

For issues related to Docker setup, please open an issue on the [GitHub repository](https://github.com/gusafr/midora-solid-ai).

**Last Updated:** 2025-11-02  
**Maintained by:** solid.ai Framework Team  
**License:** MIT
