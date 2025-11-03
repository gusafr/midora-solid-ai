# Backstage IDP Integration

**Status:** ✅ Ready for import into Backstage

The solid.ai framework provides comprehensive Backstage catalog definitions for seamless integration with your Internal Developer Portal (IDP).

## Quick Import

```yaml
# In Backstage, register:
https://github.com/gusafr/midora-solid-ai/blob/main/catalog-info.yaml
```

Or add to `app-config.yaml`:

```yaml
catalog:
  locations:
    - type: url
      target: https://github.com/gusafr/midora-solid-ai/blob/main/catalog-info.yaml
```

## What Gets Imported

- 📦 **Component:** Documentation site with TechDocs
- 🏗️ **System:** Complete framework system
- 🌐 **Domain:** Organizational design domain  
- 👥 **Team:** Framework maintainers
- 🔌 **API:** Conceptual framework model
- 📚 **Resources:** Playbooks and diagrams (10+ diagrams)
- 🎨 **Template:** Product Triad squad creation

## For Midora

If you're using `midora-idp-backstage`, this catalog integrates seamlessly with your existing components (midora-core, midora-intelligence, etc.).

See [complete Backstage integration guide](https://gusafr.github.io/midora-solid-ai/backstage/) for detailed setup and customization.

---

**Catalog File:** [`catalog-info.yaml`](https://github.com/gusafr/midora-solid-ai/blob/main/catalog-info.yaml)  
**Documentation:** [BACKSTAGE.md](https://github.com/gusafr/midora-solid-ai/blob/main/BACKSTAGE.md)
