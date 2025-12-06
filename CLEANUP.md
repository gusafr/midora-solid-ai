# Resource Optimization & Cleanup Strategy

This document outlines the cleanup and resource optimization strategies for the solid.ai documentation repository.

## Overview

The repository implements **automated and manual cleanup** to optimize:
- 💾 **Storage usage** - Remove old artifacts, caches, and build outputs
- 🚀 **Build performance** - Keep only recent caches for faster builds
- 🔒 **Security** - Remove old container images that may have vulnerabilities
- 💰 **Cost** - Reduce storage costs in GitHub and container registries

---

## Automated Cleanup (GitHub Actions)

### Weekly Cleanup Workflow
**File:** `.github/workflows/cleanup.yml`

**Schedule:** Runs every Sunday at 2 AM UTC (configurable)

**What It Cleans:**

#### 1. Workflow Runs
- **Retention:** 30 days
- **Minimum:** Keep last 5 runs
- **Purpose:** Remove old workflow execution logs

#### 2. Artifacts
- **Retention:** 30 days
- **Minimum:** Keep last 5 artifacts
- **Purpose:** Remove old build artifacts (MkDocs site builds, test results)

#### 3. Docker Images (GitHub Container Registry)
- **Untagged:** Deleted (keep last 5)
- **Tagged:** Keep last 10 versions
- **Protected tags:** Never delete `latest`, `main`, or semantic versions (`v1.2.3`)
- **Purpose:** Remove old container images to save registry space

#### 4. Build Caches
- **Retention:** 7 days
- **Purpose:** Remove old Docker build caches
- **Note:** GitHub automatically limits cache to 10 GB per repository

### Manual Trigger

You can manually trigger the cleanup workflow:
1. Go to **Actions** → **Cleanup Old Artifacts and Caches**
2. Click **Run workflow**
3. Select branch and confirm

---

## Local Cleanup (Development)

### Cleanup Script
**File:** `cleanup.ps1`

A PowerShell script for cleaning local development resources.

### Usage

```powershell
# Clean everything (recommended)
.\cleanup.ps1 all

# Preview what would be deleted (dry run)
.\cleanup.ps1 all -DryRun

# Clean specific targets
.\cleanup.ps1 build         # MkDocs build output only
.\cleanup.ps1 docker        # Docker containers and images
.\cleanup.ps1 python        # Python cache files
.\cleanup.ps1 cache         # General cache files
.\cleanup.ps1 logs          # Log and temp files
```

### What Gets Cleaned

#### Build Target (`build`)
- `./site/` - MkDocs build output
- `./docs_site/.cache/` - MkDocs cache
- `./.cache/` - General cache

**Typical savings:** 50-100 MB

#### Docker Target (`docker`)
- All `solid-ai-*` containers (running and stopped)
- All `solid-ai*` images
- Unused Docker resources (via `docker system prune`)

**Typical savings:** 500 MB - 2 GB

#### Python Target (`python`)
- All `__pycache__/` directories
- All `.pyc` files
- `.pytest_cache/`
- `htmlcov/` - Coverage reports
- `.coverage` - Coverage data

**Typical savings:** 5-20 MB

#### Cache Target (`cache`)
- `./.cache/`
- `./node_modules/.cache/`

**Typical savings:** 10-50 MB

#### Logs Target (`logs`)
- All `*.log` files
- All `*.tmp` files

**Typical savings:** 1-10 MB

### Example Output

```powershell
PS> .\cleanup.ps1 all

solid.ai Cleanup Script
======================
MODE: ACTIVE (files will be deleted)

============================================================
Cleaning Build Artifacts
============================================================
  Removing: MkDocs build output (45.23 MB)
  Removing: MkDocs cache (12.45 MB)

============================================================
Cleaning Python Artifacts
============================================================
  Removing: Python cache (3.21 MB)
  Removing: Pytest cache (1.05 MB)

============================================================
Cleanup Summary
============================================================
Freed: 62.94 MB

Done!
```

---

## Retention Policies

### GitHub Actions Artifacts
| Type | Retention | Minimum Kept | Rationale |
|------|-----------|--------------|-----------|
| Workflow runs | 30 days | 5 | Debugging recent issues |
| Build artifacts | 30 days | 5 | Re-deployment needs |
| Pages artifacts | 7 days | 1 | Only latest deployment needed |

### Docker Images
| Type | Retention | Minimum Kept | Rationale |
|------|-----------|--------------|-----------|
| Untagged | N/A | 5 | Intermediate build layers |
| Tagged (dev) | Rolling | 10 | Development versions |
| Semantic versions | Forever | All | Official releases |
| `latest` tag | Forever | 1 | Current production |

### Build Caches
| Type | Retention | Rationale |
|------|-----------|-----------|
| Docker build cache | 7 days | Balance speed vs storage |
| MkDocs cache | Per build | Regenerated each build |
| Python pip cache | GitHub managed | Dependency caching |

---

## Best Practices

### For Contributors

1. **Run cleanup regularly**
   ```powershell
   # Before committing large changes
   .\cleanup.ps1 all
   ```

2. **Use dry run first**
   ```powershell
   # Preview before deleting
   .\cleanup.ps1 all -DryRun
   ```

3. **Clean Docker after testing**
   ```powershell
   # After Docker testing sessions
   .\cleanup.ps1 docker
   ```

### For Maintainers

1. **Monitor workflow runs**
   - Check Actions tab weekly
   - Verify cleanup workflow succeeds
   - Review deleted artifact counts

2. **Adjust retention periods**
   - Edit `.github/workflows/cleanup.yml`
   - Update `retain_days` and `min-versions-to-keep`
   - Test with manual trigger

3. **Monitor registry size**
   - Check Packages tab in GitHub
   - Verify old images are being deleted
   - Adjust policies if needed

---

## Storage Savings

### Expected Savings per Week

| Category | Local Dev | GitHub Actions | Registry |
|----------|-----------|----------------|----------|
| Build artifacts | 50-100 MB | 200-500 MB | N/A |
| Docker images | 500 MB - 2 GB | N/A | 1-5 GB |
| Caches | 20-50 MB | 100-500 MB | N/A |
| Logs | 1-10 MB | 10-50 MB | N/A |
| **Total** | **571 MB - 2.16 GB** | **310 MB - 1 GB** | **1-5 GB** |

### Cumulative Savings per Year

Without cleanup: **~50-100 GB** of accumulated artifacts and caches
With cleanup: **~5-10 GB** (95% reduction)

---

## Troubleshooting

### Cleanup Workflow Fails

**Problem:** GitHub Actions cleanup workflow fails with permission error

**Solution:**
```yaml
# Ensure correct permissions in workflow
permissions:
  actions: write
  packages: write
  contents: read
```

### Local Cleanup Script Errors

**Problem:** PowerShell execution policy blocks script

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Problem:** Docker cleanup fails with "permission denied"

**Solution:**
```powershell
# Run as administrator or ensure Docker Desktop is running
```

### Cache Not Being Deleted

**Problem:** GitHub Actions cache persists beyond 7 days

**Solution:**
- GitHub cache limit is 10 GB per repository
- Older caches are automatically evicted when limit is reached
- Manual deletion requires `gh` CLI with authentication

---

## Customization

### Adjust Retention Periods

Edit `.github/workflows/cleanup.yml`:

```yaml
# Keep artifacts for 60 days instead of 30
retain_days: 60

# Keep minimum 10 runs instead of 5
keep_minimum_runs: 10

# Keep 20 Docker versions instead of 10
min-versions-to-keep: 20
```

### Change Cleanup Schedule

Edit `.github/workflows/cleanup.yml`:

```yaml
on:
  schedule:
    # Run daily at 3 AM UTC
    - cron: '0 3 * * *'
    
    # Or run monthly on the 1st at 2 AM UTC
    - cron: '0 2 1 * *'
```

### Exclude Specific Artifacts

Edit `.github/workflows/cleanup.yml`:

```yaml
# Protect specific artifact names
- name: Delete old artifacts
  uses: c-hive/gha-remove-artifacts@v1
  with:
    age: '30 days'
    skip-recent: 5
    skip-tags: 'production-*'  # Don't delete production artifacts
```

---

## Monitoring

### Check Cleanup Effectiveness

```powershell
# View GitHub Actions storage usage
gh api /repos/:owner/:repo/actions/cache/usage

# List current artifacts
gh api /repos/:owner/:repo/actions/artifacts

# List container images
gh api /users/:owner/packages/container/:package/versions
```

### Cleanup Metrics

Track in GitHub repository:
- Actions storage used (should stay under 2 GB)
- Number of artifacts (should stay under 50)
- Container registry size (should stay under 10 GB)

---

## Security Considerations

1. **Image scanning before deletion**
   - Cleanup runs after security scans complete
   - Never delete images with open security issues until resolved

2. **Artifact retention for compliance**
   - Adjust retention to meet compliance requirements
   - Some organizations require 90-day minimum

3. **Automated cleanup permissions**
   - Workflow uses GitHub token with minimal permissions
   - Only `write` access to actions and packages

---

**Last Updated:** 2025-11-02  
**Maintained by:** solid.ai Framework Team  
**License:** MIT
