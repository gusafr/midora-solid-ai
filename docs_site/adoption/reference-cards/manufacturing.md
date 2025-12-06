# Manufacturing & Industrial AI Reference Card

**Quick-start AI prompts for plant managers, production engineers, and operations teams**

---

## 10 Essential AI Prompts for Manufacturing

### 1. Predictive Maintenance for Equipment

**Prompt:**
```
Analyze telemetry data for [Equipment Name/ID]:
- Vibration levels: [Current readings vs. baseline]
- Temperature: [Bearing, motor, hydraulic fluid]
- Oil quality: [Viscosity, contamination, metal particles]
- Operating hours since last maintenance: [Hours]
- Historical failure patterns: [Past breakdowns for this equipment type]

Predict probability of failure in next [30/60/90] days.
Recommend: Continue operation | Schedule inspection | Immediate shutdown
Suggest root cause if anomaly detected.
```

**Pro Tip:** Set up real-time alerts for critical equipment (production bottlenecks); prioritize maintenance to minimize downtime impact.

---

### 2. Automated Quality Inspection (Computer Vision)

**Prompt:**
```
Inspect this [Part/Product] image for defects:
- Expected specifications: [Dimensions, color, surface finish]
- Common defects: [Scratches, dents, misalignment, color variation, contamination]

Analyze image and report:
- Pass/Fail decision
- Defect type and location (if any)
- Confidence score
- Recommended action (Scrap | Rework | Pass with note)
```

**Pro Tip:** Train vision models on your specific products/defects; label 500-1,000 images per defect type for high accuracy.

---

### 3. Production Schedule Optimization

**Prompt:**
```
Optimize production schedule for next [Week/Month]:
- Orders: [List with due dates, quantities, priorities]
- Equipment: [List machines, capacities, current status]
- Materials: [Inventory levels, lead times, incoming shipments]
- Labor: [Shifts, skills, availability]
- Changeover times: [Time to switch between products]

Generate schedule that:
- Meets due dates (prioritize urgent orders)
- Minimizes changeovers (batch similar products)
- Maximizes equipment utilization (target >85% OEE)
- Balances workload across shifts
```

**Pro Tip:** Include buffer time for unexpected issues (equipment breakdown, material delays); aim for 90% schedule adherence.

---

### 4. Root Cause Analysis for Downtime

**Prompt:**
```
Production line stopped unexpectedly:
- Equipment: [Line/Machine name]
- Duration: [Minutes/Hours]
- Symptoms: [Error codes, operator observations, sensor readings]
- Recent changes: [Maintenance, product changeover, new material batch]
- Historical data: [Similar incidents in past 90 days]

Perform root cause analysis:
1. Identify most likely cause (5 Whys, Fishbone diagram)
2. Suggest immediate fix to resume production
3. Recommend long-term prevention measures
```

**Pro Tip:** Build a knowledge base of past downtime incidents; AI learns from history to diagnose faster.

---

### 5. Overall Equipment Effectiveness (OEE) Analysis

**Prompt:**
```
Calculate OEE for [Equipment/Line] over [Time Period]:
- Availability: [Actual run time / Planned run time]
  Account for: Breakdowns, changeovers, planned maintenance
- Performance: [Actual output / Theoretical max output]
  Account for: Slowdowns, minor stops, reduced speed
- Quality: [Good units / Total units produced]
  Account for: Defects, rework, scrap

Report OEE and identify primary loss:
- Is it availability (too much downtime)?
- Performance (running too slow)?
- Quality (too many defects)?

Recommend improvement initiatives to increase OEE from [Current]% to [Target]%.
```

**Pro Tip:** World-class OEE is 85%+; if below 65%, focus on biggest loss category first (availability, performance, or quality).

---

### 6. Energy Consumption Optimization

**Prompt:**
```
Analyze energy usage for [Facility/Production Line]:
- Current consumption: [kWh per unit produced, peak demand charges]
- Energy-intensive equipment: [List with power ratings]
- Production schedule: [Shift patterns, idle time]
- Utility rates: [Time-of-use pricing, demand charges]

Recommend strategies to reduce energy costs:
- Shift production to off-peak hours
- Optimize equipment startup/shutdown sequences
- Identify energy waste (idle equipment, compressed air leaks)
- Suggest equipment upgrades (high-efficiency motors, LED lighting)

Estimate annual savings.
```

**Pro Tip:** Target 10-20% energy reduction through operational changes (before capital investments); monitor kWh per unit produced.

---

### 7. Supply Chain Disruption Mitigation

**Prompt:**
```
Supplier [Name] delayed shipment of [Critical Material]:
- Original delivery: [Date]
- New estimated delivery: [Date + X days delay]
- Impact: [Products affected, production at risk]
- Current inventory: [Units on hand, days of supply]
- Alternative suppliers: [List with lead times, pricing, quality]

Recommend mitigation strategy:
- Can we expedite from current supplier (air freight, premium cost)?
- Should we source from alternative supplier (risk: quality, cost)?
- Adjust production schedule (build other products first)?
- Communicate delay to customers (manage expectations)?
```

**Pro Tip:** Maintain 2+ qualified suppliers for critical materials; build safety stock for long-lead-time items.

---

### 8. Worker Safety & Ergonomics Analysis

**Prompt:**
```
Evaluate workstation [ID/Name] for safety and ergonomic risks:
- Task: [Description of work performed]
- Repetition rate: [Actions per minute/hour]
- Force required: [Lifting weight, tool operation]
- Posture: [Standing, sitting, bending, reaching overhead]
- Environmental hazards: [Noise, heat, chemical exposure]
- Incident history: [Past injuries at this workstation]

Identify risks:
- Musculoskeletal disorders (repetitive strain, back injury)
- Acute injury (pinch points, caught in machinery)
- Long-term health (hearing loss, respiratory)

Recommend controls:
- Engineering controls (automation, lift assists, guards)
- Administrative controls (job rotation, breaks)
- PPE (hearing protection, gloves, respirators)
```

**Pro Tip:** Aim for zero lost-time accidents; invest in ergonomic improvements (ROI from reduced workers' comp claims, turnover).

---

### 9. Yield Optimization for Process Manufacturing

**Prompt:**
```
Analyze production process for [Product]:
- Input materials: [Quantities, costs]
- Process parameters: [Temperature, pressure, time, mixing speed]
- Output: [Actual yield %, quality metrics]
- Scrap/waste: [%, reasons]
- Target yield: [%]

Identify factors impacting yield:
- Material quality variations (incoming inspection data)
- Process deviations (sensor readings, operator adjustments)
- Equipment condition (wear, calibration drift)

Recommend process adjustments to improve yield from [Current]% to [Target]%.
Estimate annual savings from yield improvement.
```

**Pro Tip:** In process industries (chemicals, food, pharma), 1% yield improvement can save millions; monitor in real-time.

---

### 10. Demand-Driven Production Planning

**Prompt:**
```
Align production with demand forecast:
- Forecasted demand: [Units by product, by month]
- Current inventory: [Finished goods, work-in-progress, raw materials]
- Production capacity: [Units per day by line/machine]
- Lead times: [Raw material procurement, production, shipping]
- Inventory carrying cost: [% per year]
- Stockout cost: [Lost sales, customer dissatisfaction]

Recommend production plan:
- Build-to-stock (produce ahead based on forecast) vs. 
  Build-to-order (produce only when orders received)?
- How much safety stock to hold?
- When to ramp up production for seasonal peaks?

Balance inventory costs vs. service level (target 95% on-time delivery).
```

**Pro Tip:** Use Sales & Operations Planning (S&OP) process; align sales forecasts with production capacity monthly.

---

## Advanced Techniques

### Digital Twin for Process Simulation
**Prompt Pattern:**
```
Simulate production of [Product] with these parameter changes:
- Temperature: [Current] → [Proposed]
- Pressure: [Current] → [Proposed]
- Cycle time: [Current] → [Proposed]

Predict impact on:
- Yield, quality, energy consumption, throughput
- Equipment stress (will changes shorten equipment life?)

Recommend whether to implement changes.
```

### Anomaly Detection in Sensor Data
**Prompt Pattern:**
```
Monitor real-time sensor data from [Equipment]:
- Temperature, pressure, vibration, current draw, flow rate

Establish normal operating range (baseline from past 90 days).
Alert if readings deviate >2 standard deviations (potential issue developing).
Suggest probable cause and recommended action.
```

### Supplier Quality Management
**Prompt Pattern:**
```
Analyze incoming material quality from [Supplier]:
- Defect rate: [% of batches rejected]
- On-time delivery: [%]
- Cost competitiveness: [vs. alternatives]
- Responsiveness: [Issue resolution time]

Score supplier performance (0-100).
Recommend: Continue | Improve | Replace
If replace, suggest alternative suppliers.
```

---

## Metrics to Track

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| **OEE (Overall Equipment Effectiveness)** | >85% | World-class manufacturing benchmark |
| **Cycle Time** | Minimize | Time from raw material → finished product |
| **First Pass Yield** | >95% | % of units passing quality without rework |
| **Scrap Rate** | <3% | Waste, cost of quality issues |
| **On-Time Delivery** | >95% | Customer satisfaction, contract compliance |
| **Unplanned Downtime** | <2% | Equipment reliability, maintenance effectiveness |
| **Safety (TRIR)** | <1.0 | Total Recordable Incident Rate (per 100 workers) |
| **Energy Intensity** | Decrease | kWh per unit produced (sustainability, cost) |

---

## Related Resources

- **Full Playbook**: [Manufacturing & Industrial Playbook](../../PLAYBOOKS/playbook-manufacturing.md)
- **AI Integration**: [AI Integration Playbook](../../PLAYBOOKS/playbook-ai-integration.md)
- **Data Contracts**: [Example: Equipment Telemetry Event](../../PLAYBOOKS/playbook-manufacturing.md#data-contracts)
- **Ethical AI**: [Worker Safety, Environmental Compliance](../../PLAYBOOKS/playbook-manufacturing.md#ethical-manufacturing)

---

## Tips for Success

1. **Start with Pain Points**: Focus AI on biggest losses (downtime, scrap, safety incidents)
2. **IoT Foundation**: Install sensors on critical equipment (can't predict failures without data)
3. **Pilot Before Scaling**: Test predictive maintenance on one production line, prove ROI, then expand
4. **Operator Buy-In**: Train operators to trust AI insights (not replace them, augment them)
5. **Closed-Loop**: Act on AI recommendations (if AI predicts failure, actually schedule maintenance)
6. **Continuous Improvement**: Use DMAIC (Define, Measure, Analyze, Improve, Control) with AI insights
7. **Safety First**: AI should never compromise worker safety for efficiency gains

---

**Questions?** Join the SOLID.AI community or open an issue on [GitHub](https://github.com/gusafr/midora-solid-ai/issues)!

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
