# GitHub Pages Setup Guide

This guide explains how to enable and configure GitHub Pages for the solid.ai documentation site.

## Current Status

⚠️ **GitHub Pages is currently disabled**

The Pages deployment workflow (`.github/workflows/pages.yml`) is configured but won't run automatically until you enable GitHub Pages in your repository settings.

## Quick Setup

### Step 1: Enable GitHub Pages

1. Go to your repository: https://github.com/gusafr/midora-solid-ai
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar, under "Code and automation")
4. Under **"Build and deployment"**:
   - **Source:** Select **GitHub Actions**
   - (Don't select "Deploy from a branch")
5. Click **Save** (if button appears)

### Step 2: Enable the Workflow

Once Pages is enabled, uncomment the workflow trigger:

Edit `.github/workflows/pages.yml`:

```yaml
on:
  push:
    branches:
      - main
  workflow_dispatch:
```

Remove the comment marks (`#`) from the `push:` section.

### Step 3: Trigger First Deployment

Option A: Push a commit to `main` branch
```powershell
git add .
git commit -m "Enable GitHub Pages deployment"
git push origin main
```

Option B: Manual trigger
1. Go to **Actions** tab
2. Click **Deploy to GitHub Pages**
3. Click **Run workflow**
4. Select `main` branch
5. Click **Run workflow**

### Step 4: Verify Deployment

1. Go to **Settings → Pages**
2. You should see: "Your site is live at https://gusafr.github.io/midora-solid-ai/"
3. Click the URL to view your documentation

---

## Configuration Details

### Custom Domain (Optional)

If you want to use a custom domain:

1. Go to **Settings → Pages**
2. Under **Custom domain**, enter your domain (e.g., `docs.midora.ai`)
3. Click **Save**
4. Add DNS records at your domain provider:
   ```
   Type: CNAME
   Name: docs (or @ for root domain)
   Value: gusafr.github.io
   ```
5. Wait for DNS propagation (can take up to 24 hours)
6. Enable **Enforce HTTPS** (recommended)

### Branch Protection

To prevent accidental deployments:

1. Go to **Settings → Branches**
2. Add rule for `main` branch
3. Enable **Require status checks to pass before merging**
4. Select **Build** (from Pages workflow)

---

## Troubleshooting

### "Not Found" Error in Workflow

**Problem:** Deployment fails with 404 error

**Solution:** Enable GitHub Pages first (see Step 1 above)

### Site Shows 404

**Problem:** Site is deployed but shows 404 page

**Possible causes:**
1. **Wrong base path:** Check `site_url` in `mkdocs.yml`
2. **Missing index.html:** Ensure build completed successfully
3. **Recent deployment:** Wait 1-2 minutes for propagation

**Solution:**
```yaml
# In mkdocs.yml, ensure correct site_url:
site_url: https://gusafr.github.io/midora-solid-ai/
```

### Build Succeeds but Deploy Fails

**Problem:** Build job completes but deploy job fails

**Solution:** Check workflow permissions:
```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

### Old Content Showing

**Problem:** Site doesn't reflect latest changes

**Solution:**
1. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. Clear browser cache
3. Check workflow run completed successfully
4. Check deployment status in **Settings → Pages**

---

## Workflow Details

### Automatic Deployment

Once enabled, the site deploys automatically when:
- ✅ Commits are pushed to `main` branch
- ✅ Pull requests are merged to `main`

### Manual Deployment

You can manually trigger deployment:
1. Go to **Actions** → **Deploy to GitHub Pages**
2. Click **Run workflow**
3. Select branch (usually `main`)
4. Click **Run workflow**

### Build Process

The workflow:
1. ✅ Checks out repository
2. ✅ Sets up Python 3.11
3. ✅ Installs dependencies from `requirements.txt`
4. ✅ Runs `mkdocs build --strict` (fails on warnings)
5. ✅ Uploads build artifact
6. ✅ Deploys to GitHub Pages

### Deployment URL

Your documentation will be available at:
```
https://gusafr.github.io/midora-solid-ai/
```

Or with custom domain:
```
https://docs.midora.ai/  (if configured)
```

---

## Repository Settings Checklist

Before enabling Pages, verify:

- [ ] Repository is public (or GitHub Pro/Team for private repos)
- [ ] `mkdocs.yml` has correct `site_url`
- [ ] `.github/workflows/pages.yml` exists
- [ ] `requirements.txt` includes all dependencies
- [ ] Local build works: `mkdocs build --strict`

---

## Alternative: Manual Deployment

If you prefer not to use GitHub Actions:

### Option 1: Deploy from Local Build

```powershell
# Build the site
mkdocs build

# Install GitHub Pages gem (if not installed)
# gem install github-pages

# Deploy using gh-pages
mkdocs gh-deploy --force
```

### Option 2: Deploy from Branch

1. Build locally: `mkdocs build`
2. Push `site/` contents to `gh-pages` branch
3. In **Settings → Pages**, select:
   - Source: **Deploy from a branch**
   - Branch: **gh-pages** / **/ (root)**

---

## Security Considerations

### Permissions

The Pages workflow uses minimal permissions:
- `contents: read` - Read repository files
- `pages: write` - Deploy to Pages
- `id-token: write` - Authentication token

### Secrets

No secrets are required for basic deployment. Custom domain with DNS verification may require additional configuration.

### Branch Protection

Recommended settings:
- Require pull request reviews
- Require status checks (build must pass)
- Restrict who can push to `main`

---

## Monitoring

### Check Deployment Status

**Via GitHub UI:**
1. Go to **Actions** tab
2. See latest workflow runs
3. Green checkmark = successful deployment

**Via API:**
```powershell
# Check Pages deployment status
gh api repos/gusafr/midora-solid-ai/pages
```

### View Deployment History

1. Go to **Deployments** (right sidebar)
2. Click **github-pages**
3. See all deployment history

---

## Cost & Limits

### Free Tier Limits (Public Repos)

- ✅ **Storage:** 1 GB
- ✅ **Bandwidth:** 100 GB/month
- ✅ **Build time:** 10 minutes max per build
- ✅ **Builds:** Unlimited

Current site size: ~25-50 MB (well within limits)

### Private Repository

Requires GitHub Pro, Team, or Enterprise plan.

---

## Next Steps

1. ✅ Enable GitHub Pages (Settings → Pages → Source: GitHub Actions)
2. ✅ Uncomment workflow trigger in `.github/workflows/pages.yml`
3. ✅ Push to `main` or manually trigger workflow
4. ✅ Verify site at https://gusafr.github.io/midora-solid-ai/
5. ⚙️ (Optional) Configure custom domain
6. ⚙️ (Optional) Enable branch protection

---

## Support

For issues with GitHub Pages deployment:
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [MkDocs Documentation](https://www.mkdocs.org/)

**Last Updated:** 2025-11-02  
**Maintained by:** solid.ai Framework Team  
**License:** MIT
