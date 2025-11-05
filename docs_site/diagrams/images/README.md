# Diagram Images

**Generated:** 2025-11-05 13:27:52  
**Format:** png  
**Source:** DIAGRAMS  
**Total Diagrams:** 21

---

## Available Formats

- **SVG** - Scalable vector graphics (best for web, PDF, presentations)
- **PNG** - High-resolution raster images (universal compatibility)

---

## Diagrams

| # | Diagram | SVG | PNG | Source |
|---|---------|-----|-----|--------|
| 1 | **Ai Maturity Model Progression** | ✅ [SVG](svg/ai-maturity-model-progression.svg) | ✅ [PNG](png/ai-maturity-model-progression.png) | [.mmd](../ai-maturity-model-progression.mmd) |
| 2 | **Ai Native Safe Model** | ✅ [SVG](svg/ai-native-safe-model.svg) | ✅ [PNG](png/ai-native-safe-model.png) | [.mmd](../ai-native-safe-model.mmd) |
| 3 | **Ai Native Sprint Flow** | ✅ [SVG](svg/ai-native-sprint-flow.svg) | ✅ [PNG](png/ai-native-sprint-flow.png) | [.mmd](../ai-native-sprint-flow.mmd) |
| 4 | **Augmentation Factor Calculation** | ✅ [SVG](svg/augmentation-factor-calculation.svg) | ✅ [PNG](png/augmentation-factor-calculation.png) | [.mmd](../augmentation-factor-calculation.mmd) |
| 5 | **Business Service Full Integration** | ✅ [SVG](svg/business-service-full-integration.svg) | ✅ [PNG](png/business-service-full-integration.png) | [.mmd](../business-service-full-integration.mmd) |
| 6 | **Cognitive Decision Flow** | ✅ [SVG](svg/cognitive-decision-flow.svg) | ✅ [PNG](png/cognitive-decision-flow.png) | [.mmd](../cognitive-decision-flow.mmd) |
| 7 | **Collaboration Models Matrix** | ✅ [SVG](svg/collaboration-models-matrix.svg) | ✅ [PNG](png/collaboration-models-matrix.png) | [.mmd](../collaboration-models-matrix.mmd) |
| 8 | **Data Analytics Patterns** | ✅ [SVG](svg/data-analytics-patterns.svg) | ✅ [PNG](png/data-analytics-patterns.png) | [.mmd](../data-analytics-patterns.mmd) |
| 9 | **Data Spine Architecture** | ✅ [SVG](svg/data-spine-architecture.svg) | ✅ [PNG](png/data-spine-architecture.png) | [.mmd](../data-spine-architecture.mmd) |
| 10 | **Human Ai Evolution** | ✅ [SVG](svg/human-ai-evolution.svg) | ✅ [PNG](png/human-ai-evolution.png) | [.mmd](../human-ai-evolution.mmd) |
| 11 | **Learning Path Structure** | ✅ [SVG](svg/learning-path-structure.svg) | ✅ [PNG](png/learning-path-structure.png) | [.mmd](../learning-path-structure.mmd) |
| 12 | **Midora Implementation** | ❌ | ❌ | [.mmd](../midora-implementation.mmd) |
| 13 | **Organizational Flow** | ✅ [SVG](svg/organizational-flow.svg) | ✅ [PNG](png/organizational-flow.png) | [.mmd](../organizational-flow.mmd) |
| 14 | **Organizational Scalability Ceilings** | ✅ [SVG](svg/organizational-scalability-ceilings.svg) | ✅ [PNG](png/organizational-scalability-ceilings.png) | [.mmd](../organizational-scalability-ceilings.mmd) |
| 15 | **Pool Engagement Patterns** | ✅ [SVG](svg/pool-engagement-patterns.svg) | ✅ [PNG](png/pool-engagement-patterns.png) | [.mmd](../pool-engagement-patterns.mmd) |
| 16 | **Process Sipoc Example** | ✅ [SVG](svg/process-sipoc-example.svg) | ✅ [PNG](png/process-sipoc-example.png) | [.mmd](../process-sipoc-example.mmd) |
| 17 | **Risk Scoring Framework** | ✅ [SVG](svg/risk-scoring-framework.svg) | ✅ [PNG](png/risk-scoring-framework.png) | [.mmd](../risk-scoring-framework.mmd) |
| 18 | **Role Hierarchy Framework** | ✅ [SVG](svg/role-hierarchy-framework.svg) | ✅ [PNG](png/role-hierarchy-framework.png) | [.mmd](../role-hierarchy-framework.mmd) |
| 19 | **Sipoc Automation Pattern** | ✅ [SVG](svg/sipoc-automation-pattern.svg) | ✅ [PNG](png/sipoc-automation-pattern.png) | [.mmd](../sipoc-automation-pattern.mmd) |
| 20 | **Solid Ai Architecture** | ✅ [SVG](svg/solid-ai-architecture.svg) | ✅ [PNG](png/solid-ai-architecture.png) | [.mmd](../solid-ai-architecture.mmd) |
| 21 | **Squad Business Service Organization** | ✅ [SVG](svg/squad-business-service-organization.svg) | ✅ [PNG](png/squad-business-service-organization.png) | [.mmd](../squad-business-service-organization.mmd) |
| 22 | **Squad Lifecycle** | ✅ [SVG](svg/squad-lifecycle.svg) | ✅ [PNG](png/squad-lifecycle.png) | [.mmd](../squad-lifecycle.mmd) |


---

## Usage

### In PDF Generation (Python)
```python
from svg_helper import create_diagram_flowable

# Create flowable for diagram
flowable, name = create_diagram_flowable(
    'DIAGRAMS/ai-native-safe-model.mmd',
    diagrams_dir=Path('DIAGRAMS'),
    width=15*cm
)

# Add to PDF story
story.append(flowable)
```

### In Markdown Documentation
```markdown
![AI-Native SAFE Model](../DIAGRAMS/images/svg/ai-native-safe-model.svg)
```

### In Presentations
- Drag and drop SVG/PNG files into PowerPoint, Google Slides, etc.
- SVG files maintain quality at any zoom level
- PNG files work universally (fallback)

---

## Regeneration

```bash
# Generate SVG (default)
python scripts/generate_diagram_images.py

# Generate PNG (high-res)
python scripts/generate_diagram_images.py --format png --width 2400

# Skip existing files
python scripts/generate_diagram_images.py --skip-existing
```

---

**Last Updated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
