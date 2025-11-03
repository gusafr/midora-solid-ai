# Unpublish GitHub Pages

To completely remove the published site at https://gusafr.github.io/midora-solid-ai/, follow these steps:

## Step 1: Disable GitHub Pages

1. Go to: https://github.com/gusafr/midora-solid-ai/settings/pages
2. Under **"Build and deployment"**:
   - Source: Select **"None"** (or "Deploy from a branch" → "None")
3. Click **Save**

This will unpublish the site immediately.

## Step 2: Delete gh-pages Branch (if exists)

If there's a `gh-pages` branch, delete it:

```powershell
# Check if branch exists
git branch -a | grep gh-pages

# If it exists, delete it locally and remotely
git branch -D gh-pages
git push origin --delete gh-pages
```

Or via GitHub UI:
1. Go to: https://github.com/gusafr/midora-solid-ai/branches
2. Find `gh-pages` branch (if exists)
3. Click the trash icon to delete

## Step 3: Remove GitHub Pages Artifact

The deployment artifact may still exist. It will be cleaned up automatically by the cleanup workflow within 7 days, or you can manually remove it:

1. Go to: https://github.com/gusafr/midora-solid-ai/actions
2. Click on the last successful workflow run
3. Delete the artifact manually

## Step 4: Verify Unpublished

After disabling Pages:
- https://gusafr.github.io/midora-solid-ai/ should show 404
- May take a few minutes to propagate

## Alternative: Make Repository Private

If you want to ensure the documentation is not accessible:

1. Go to: https://github.com/gusafr/midora-solid-ai/settings
2. Scroll to **"Danger Zone"**
3. Click **"Change visibility"**
4. Select **"Make private"**

This will immediately make everything inaccessible except to collaborators.

---

**Note:** Since the workflow `.github/workflows/pages.yml` has already been removed, no new deployments will occur.
