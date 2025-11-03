# Backstage Integration for solid.ai Framework

This guide explains how to integrate the solid.ai documentation and framework components into Backstage Developer Portal.

## Overview

The solid.ai framework provides Backstage catalog definitions for:
- ✅ **Documentation Component** - Main docs site
- ✅ **System** - Complete framework system
- ✅ **Domain** - Organizational design domain
- ✅ **Team** - Framework maintainers
- ✅ **API** - Conceptual framework model
- ✅ **Resources** - Playbooks and diagrams
- ✅ **Template** - Squad creation template

## Quick Setup

### Option 1: Import from GitHub (Recommended)

1. Open your Backstage instance
2. Go to **Create** → **Register Existing Component**
3. Enter the catalog URL:
   ```
   https://github.com/gusafr/midora-solid-ai/blob/main/catalog-info.yaml
   ```
4. Click **Analyze** → **Import**

### Option 2: Add to Backstage App Configuration

Edit your `app-config.yaml`:

```yaml
catalog:
  locations:
    - type: url
      target: https://github.com/gusafr/midora-solid-ai/blob/main/catalog-info.yaml
      rules:
        - allow: [Component, System, API, Resource, Template, Domain, Group]
```

Restart Backstage to apply changes.

### Option 3: Manual Import (Development)

```bash
# Clone the repository
git clone https://github.com/gusafr/midora-solid-ai.git
cd midora-solid-ai

# Copy catalog file to your Backstage catalog
cp catalog-info.yaml /path/to/backstage/catalog/solid-ai-catalog.yaml

# Register in Backstage app-config.yaml
# catalog:
#   locations:
#     - type: file
#       target: /path/to/backstage/catalog/solid-ai-catalog.yaml
```

---

## Catalog Entities

### 1. Component: solid-ai-docs

**Type:** Documentation  
**Lifecycle:** Production  
**Owner:** solid-ai-team

Main documentation component with TechDocs integration.

**Features:**
- Integrated TechDocs (MkDocs)
- Links to live documentation site
- GitHub source integration
- Tags for discoverability

**Access:**
- Backstage: `/catalog/default/component/solid-ai-docs`
- Docs: https://gusafr.github.io/midora-solid-ai/

### 2. System: solid-ai-framework

**Type:** System  
**Owner:** solid-ai-team  
**Domain:** organizational-design

Complete framework system encompassing all six layers.

**Components:**
- solid-ai-docs (documentation)
- solid-ai-playbooks (resources)
- solid-ai-diagrams (resources)

### 3. Domain: organizational-design

**Owner:** solid-ai-team

Represents the organizational design domain covering:
- Organizational architecture
- Team topology patterns
- Governance frameworks
- AI-human collaboration models

### 4. Group: solid-ai-team

**Type:** Team

Framework maintainers and contributors.

**Customization:**
```yaml
# In catalog-info.yaml, update:
spec:
  profile:
    email: your-team@example.com
  members:
    - user:default/john.doe
    - user:default/jane.smith
```

### 5. API: solid-ai-framework-api

**Type:** Conceptual OpenAPI  
**Lifecycle:** Production

Conceptual model representing the six framework layers.

**Note:** This is not a REST API but a conceptual representation for documentation purposes.

### 6. Resource: solid-ai-playbooks

**Type:** Documentation  
**Owner:** solid-ai-team

Collection of operational playbooks:
- Squads playbook
- Pools playbook
- Operations playbook
- AI integration playbook
- Midora implementation reference

### 7. Resource: solid-ai-diagrams

**Type:** Documentation  
**Owner:** solid-ai-team

Mermaid diagram library (10+ diagrams):
- Architecture diagrams
- Organizational flows
- SIPOC automation patterns
- Cognitive decision flows
- Implementation examples

### 8. Template: solid-ai-squad-template

**Type:** Service Template

Self-service template for creating Product Triad squads.

**Parameters:**
- Squad name and strategic outcome
- Product Triad members (PO, Architect, PM)
- Pool capability requirements

**Usage:**
1. Go to **Create** in Backstage
2. Select **Create solid.ai Product Triad Squad**
3. Fill in squad details
4. Review generated squad charter

---

## TechDocs Integration

### Enable TechDocs for solid.ai

The documentation is already configured for TechDocs with MkDocs.

**Backstage Configuration:**

```yaml
# app-config.yaml
techdocs:
  builder: 'local' # or 'external'
  generator:
    runIn: 'docker'  # or 'local'
  publisher:
    type: 'local'    # or 'googleGcs', 'awsS3', 'azureBlobStorage'
```

**Component Configuration:**

Already set in `catalog-info.yaml`:
```yaml
metadata:
  annotations:
    backstage.io/techdocs-ref: dir:.
```

**Build TechDocs:**

```bash
# From Backstage root directory
yarn techdocs-cli generate --source-dir /path/to/midora-solid-ai --output-dir /path/to/output
```

---

## Customization

### Update Team Information

Edit `catalog-info.yaml`:

```yaml
apiVersion: backstage.io/v1alpha1
kind: Group
metadata:
  name: solid-ai-team
spec:
  profile:
    displayName: Your Team Name
    email: your-team@example.com
    picture: https://example.com/team-avatar.png
  members:
    - user:default/alice
    - user:default/bob
```

### Add Custom Links

```yaml
metadata:
  links:
    - url: https://your-wiki.example.com/solid-ai
      title: Internal Wiki
      icon: wiki
    - url: https://your-slack.slack.com/archives/C123456
      title: Slack Channel
      icon: chat
```

### Add Custom Tags

```yaml
metadata:
  tags:
    - your-organization
    - your-department
    - custom-tag
```

### Configure Ownership

```yaml
spec:
  owner: your-team-name  # Must match a Group entity
```

---

## Advanced: Midora-Specific Integration

If you're Midora Education Labs, integrate with your existing Backstage setup:

### Link to Midora Systems

Edit `catalog-info.yaml` to add dependencies:

```yaml
spec:
  dependsOn:
    - component:default/midora-back-end-py
    - component:default/midora-ml-service
    - component:default/midora-magi-py
  providesApis:
    - solid-ai-framework-api
```

### Add to Midora Domain

```yaml
spec:
  system: solid-ai-framework
  domain: midora-platform  # Link to existing Midora domain
```

### Integrate with IDP

```yaml
metadata:
  annotations:
    backstage.io/techdocs-ref: dir:.
    github.com/project-slug: gusafr/midora-solid-ai
    backstage.io/source-location: url:https://github.com/gusafr/midora-solid-ai
    # Midora-specific annotations
    midora.io/framework-version: '1.0.0'
    midora.io/implementation: 'reference'
```

---

## Catalog Validation

### Validate Catalog File

```bash
# Install Backstage CLI
npm install -g @backstage/cli

# Validate catalog
backstage-cli catalog:validate catalog-info.yaml
```

### Common Issues

**Issue:** "Entity not found"  
**Solution:** Ensure all referenced entities exist (Group, System, Domain)

**Issue:** "Invalid YAML syntax"  
**Solution:** Use YAML linter or online validator

**Issue:** "TechDocs build fails"  
**Solution:** Ensure `mkdocs.yml` is in repository root and valid

---

## Catalog Graph Visualization

Once imported, your catalog graph will show:

```
Domain: organizational-design
  └── System: solid-ai-framework
      ├── Component: solid-ai-docs
      │   ├── Provides: solid-ai-framework-api
      │   └── Owner: solid-ai-team
      ├── Resource: solid-ai-playbooks
      │   └── Owner: solid-ai-team
      └── Resource: solid-ai-diagrams
          └── Owner: solid-ai-team
```

---

## Monitoring & Maintenance

### Update Catalog

Backstage automatically refreshes catalog entities from GitHub. Manual refresh:

1. Go to component page in Backstage
2. Click **...** menu
3. Select **Refresh**

### Health Checks

Monitor in Backstage:
- Component health status
- TechDocs build status
- Link validity
- Ownership assignments

### Versioning

Track framework versions using annotations:

```yaml
metadata:
  annotations:
    solid-ai.io/version: '1.0.0'
    solid-ai.io/release-date: '2025-11-02'
```

---

## Example: Complete Midora Setup

For Midora Education Labs `midora-idp-backstage`:

```yaml
# In your Backstage app-config.yaml
catalog:
  locations:
    # Import solid.ai framework
    - type: url
      target: https://github.com/gusafr/midora-solid-ai/blob/main/catalog-info.yaml
      rules:
        - allow: [Component, System, API, Resource, Template, Domain, Group]
    
    # Import Midora components
    - type: url
      target: https://github.com/midora/midora-back-end-py/blob/main/catalog-info.yaml
    - type: url
      target: https://github.com/midora/midora-ml-service/blob/main/catalog-info.yaml
    # ... other Midora repos

integrations:
  github:
    - host: github.com
      token: ${GITHUB_TOKEN}

techdocs:
  builder: 'external'
  generator:
    runIn: 'docker'
  publisher:
    type: 'awsS3'  # or your preferred storage
    awsS3:
      bucketName: midora-techdocs
      region: us-east-1
```

---

## Benefits

Once integrated, you get:

✅ **Centralized documentation** - All framework docs in Backstage  
✅ **Discoverability** - Easy search and navigation  
✅ **Ownership tracking** - Clear team responsibilities  
✅ **Dependency mapping** - Visual system relationships  
✅ **Self-service** - Squad creation templates  
✅ **Compliance** - Standardized metadata  
✅ **Version control** - Git-based catalog updates  

---

## Support

For Backstage integration issues:
- [Backstage Documentation](https://backstage.io/docs/features/software-catalog/)
- [TechDocs Guide](https://backstage.io/docs/features/techdocs/)
- [Catalog Format](https://backstage.io/docs/features/software-catalog/descriptor-format)

**Last Updated:** 2025-11-02  
**Maintained by:** solid.ai Framework Team  
**License:** MIT
