# Multi-stage build for solid.ai documentation site
# Stage 1: Build the documentation
FROM python:3.11-slim AS builder

WORKDIR /docs

# Install build dependencies for pycairo (required by svglib)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libcairo2-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source files
COPY mkdocs.yml .
COPY *.md ./
COPY DOCS/ ./DOCS/
COPY DIAGRAMS/ ./DIAGRAMS/
COPY RFC/ ./RFC/
COPY ADR/ ./ADR/
COPY MANIFESTO/ ./MANIFESTO/
COPY PLAYBOOKS/ ./PLAYBOOKS/
COPY ADOPTION/ ./ADOPTION/
COPY docs_site/ ./docs_site/
COPY LICENSE .

# Build the static site
RUN mkdocs build

# Stage 2: Serve with lightweight nginx
FROM nginx:alpine

# Copy built site from builder stage
COPY --from=builder /docs/site /usr/share/nginx/html

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost/health || exit 1

# Run nginx
CMD ["nginx", "-g", "daemon off;"]
