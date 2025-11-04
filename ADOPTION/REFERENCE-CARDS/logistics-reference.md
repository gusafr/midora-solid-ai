# Logistics & Supply Chain AI Reference Card

**Quick-start AI prompts for logistics managers, warehouse operators, and supply chain professionals**

---

## 10 Essential AI Prompts for Logistics

### 1. Dynamic Route Optimization for Delivery

**Prompt:**
```
Optimize delivery routes for today's shipments:
- Delivery list:
  * [Address 1] - Package ID, Weight, Dimensions, Time window (if any)
  * [Address 2] - Package ID, Weight, Dimensions, Time window
  * ... [Continue for all deliveries]
- Fleet available:
  * Driver 1: Vehicle capacity, starting location, hours available, current location
  * Driver 2: Vehicle capacity, starting location, hours available, current location
  * ... [Continue for all drivers]
- Constraints:
  * Hours of service limits (DOT regulations: 11-hour driving limit, 14-hour on-duty)
  * Delivery time windows (customer requested specific times)
  * Vehicle capacities (weight, volume)
  * Traffic conditions (current traffic, expected rush hours)
  * Weather (avoid flooded roads, icy conditions)

Generate optimal routes:
- Assign deliveries to drivers (balanced workload)
- Sequence stops to minimize total miles, time
- Respect time windows and hours-of-service limits
- Provide turn-by-turn navigation, estimated arrival times

Real-time re-routing:
- If traffic jam, road closure, or driver ahead of/behind schedule, update route dynamically
```

**Pro Tip:** Set 15-min buffer between stops (unexpected delays, customer not ready); achieve 95%+ on-time delivery.

---

### 2. Inventory Demand Forecasting

**Prompt:**
```
Forecast inventory demand for next 30/60/90 days:
- SKU: [Product identifier]
- Historical sales: [Past 12-24 months of daily/weekly sales data]
- Seasonality: [Holiday spikes, summer/winter patterns]
- Promotions: [Upcoming sales, discounts that will drive demand]
- External factors:
  * Weather (sunscreen in summer, ice melt in winter)
  * Local events (sports championships, concerts increase demand in region)
  * Competitor actions (if competitor stockout, customers come to us)
- Current inventory: [Units on hand, in-transit, on order]
- Lead time: [Days from order to receipt from supplier]

Predict:
- Daily/weekly demand by SKU and location (warehouse, store)
- Stockout risk (will we run out before replenishment arrives?)
- Overstock risk (will we have excess inventory tying up cash?)

Recommend replenishment:
- Order quantity (balance carrying cost vs. stockout risk)
- Order timing (when to place order to arrive just-in-time)
- Safety stock level (buffer for demand variability)
```

**Pro Tip:** Forecast accuracy improves with more data; aim for <15% MAPE (Mean Absolute Percentage Error).

---

### 3. Warehouse Pick Path Optimization

**Prompt:**
```
Optimize pick path for order fulfillment:
- Order: [List of SKUs to pick with quantities]
- Warehouse layout:
  * Aisle map (A1, A2, B1, B2...)
  * SKU locations (Bin addresses: A1-05-03 = Aisle A1, Bay 05, Shelf 03)
  * Zone assignments (if using zone picking)
- Picker location: [Current position, starting position for new pick]
- Picking strategy:
  * Single-order picking (one order at a time)
  * Batch picking (multiple orders in one pass)
  * Wave picking (all orders for a shipping wave)

Generate optimal pick path:
- Sequence of bin locations minimizing walking distance
- Estimated pick time
- Avoid congestion (don't route multiple pickers to same aisle simultaneously)

For batch picking:
- Group orders with overlapping SKUs (pick 20 units of Item X for 5 orders in one stop)
- Provide sorting instructions (at packing station, split batch into individual orders)
```

**Pro Tip:** Re-slot fast-movers closer to packing stations; reduces walk time 20-30%.

---

### 4. Predictive Maintenance for Fleet & Equipment

**Prompt:**
```
Predict maintenance needs for [Truck/Forklift/Conveyor]:
- Equipment ID: [Vehicle number, equipment identifier]
- Telemetry data:
  * Odometer/hours: [Current mileage or operating hours]
  * Engine diagnostics: [Oil pressure, coolant temp, error codes]
  * Vibration sensors: [Bearing wear, belt tension]
  * Tire pressure/tread depth
  * Brake wear indicators
  * Battery health (for electric vehicles/forklifts)
- Maintenance history: [Last service date, repairs performed, parts replaced]
- Manufacturer guidelines: [Recommended service intervals]

Predict:
- Probability of failure in next 30/60/90 days
- Component at risk (engine, transmission, brakes, hydraulics)
- Recommended action:
  * Continue operation (low risk)
  * Schedule maintenance within X days (medium risk)
  * Immediate inspection/repair (high risk, safety concern)

Optimize maintenance scheduling:
- Combine multiple services (oil change + brake inspection during same downtime)
- Schedule during low-utilization periods (nights, weekends)
- Balance fleet availability (don't ground all trucks for maintenance simultaneously)
```

**Pro Tip:** Predictive maintenance reduces unplanned downtime 50%; schedule repairs before catastrophic failure.

---

### 5. Last-Mile Delivery Time Prediction

**Prompt:**
```
Predict accurate delivery time for customer:
- Package: [Tracking number, current location]
- Destination: [Customer address]
- Delivery method: [Standard, Express, Same-day]
- Route data:
  * Current driver location
  * Remaining stops before this delivery
  * Estimated time per stop (average 5-10 min)
  * Distance to destination
- Real-time factors:
  * Traffic conditions (accidents, congestion)
  * Weather (rain, snow slows deliveries)
  * Driver pace (running ahead or behind schedule?)

Provide customer with:
- Estimated delivery window (e.g., "2:00 PM - 4:00 PM")
- Real-time tracking link (see driver approaching on map)
- Proactive delay notifications (if driver delayed, inform customer immediately)

For failed delivery prevention:
- Detect if customer unlikely to be home (residential, weekday delivery)
- Suggest alternative: Reschedule, deliver to neighbor, hold at facility for pickup
```

**Pro Tip:** Customers tolerate delays if informed; 90% satisfaction with communication, even if late.

---

### 6. Load Optimization for Trucks

**Prompt:**
```
Optimize truck loading for shipment:
- Truck capacity:
  * Weight limit: [e.g., 40,000 lbs for semi-truck]
  * Volume limit: [e.g., 3,000 cubic feet]
  * Axle weight limits (can't overload front or rear axle)
- Packages to load:
  * [Package 1] - Weight, Dimensions (L×W×H), Fragility, Destination
  * [Package 2] - Weight, Dimensions, Fragility, Destination
  * ... [Continue for all packages]
- Constraints:
  * Heavy items on bottom (crush risk)
  * Fragile items protected (no heavy items on top)
  * LIFO loading (last packages in = first out for multi-stop routes)
  * Hazmat separation (flammable, corrosive separated)

Generate load plan:
- 3D visualization of package placement in truck
- Load sequence (which packages load first, last)
- Weight distribution (balanced, avoid tipping)
- Estimated space utilization (aim for >85%)

If all packages don't fit:
- Suggest splitting across multiple trucks
- Prioritize high-value, urgent shipments
```

**Pro Tip:** Optimized loading increases truck utilization 10-15%; fewer trips = lower fuel cost, emissions.

---

### 7. Freight Rate Negotiation & Carrier Selection

**Prompt:**
```
Select optimal carrier for shipment:
- Shipment details:
  * Origin: [ZIP code]
  * Destination: [ZIP code]
  * Weight: [lbs or kg]
  * Dimensions: [L×W×H]
  * Service level: [Ground, Air, Expedited]
  * Delivery deadline: [Date/time]
- Available carriers: [FedEx, UPS, USPS, regional carriers, LTL]
- Carrier data:
  * Rates (base rate, fuel surcharge, accessorials)
  * Transit time (how long to deliver?)
  * On-time performance (historical delivery success rate)
  * Claims rate (damage/loss frequency)
  * Coverage area (do they serve destination?)

Recommend best carrier:
- Lowest cost (if time not critical)
- Fastest transit (if urgent)
- Best reliability (if high-value shipment)
- Balance cost vs. service (Pareto optimal)

For freight negotiation:
- Benchmark rates against market (are we paying too much?)
- Leverage volume discounts (if shipping 1,000 packages/month, negotiate better rates)
```

**Pro Tip:** Don't always choose cheapest; late deliveries cost more in customer dissatisfaction than premium shipping.

---

### 8. Returns Processing Automation

**Prompt:**
```
Process product return efficiently:
- Return request:
  * Customer: [Name, order number]
  * Item: [SKU, quantity, original price]
  * Reason: [Doesn't fit, defective, changed mind, wrong item shipped]
  * Condition: [Tags on, unopened, used, damaged]
- Return policy:
  * Time limit (30/60/90 days from purchase?)
  * Restocking fee (if applicable)
  * Refund method (original payment, store credit)
- Return fraud check:
  * Customer return rate (serial returner? >30% of purchases returned)
  * Item condition (wardrobing: worn and returned?)
  * Refund history (excessive refund requests)

Recommend action:
- Approve return (full refund, arrange pickup/drop-off)
- Approve with restocking fee (if outside policy window)
- Deny return (policy violation, abuse detected)
- Inspect before refund (if high-value, suspected counterfeit swap)

Disposition decision:
- Restock (if new, saleable condition)
- Liquidate (if opened, sell as "open-box" at discount)
- Dispose/recycle (if damaged, unsaleable)
```

**Pro Tip:** Generous return policy increases sales (confidence to buy); but monitor abuse, set thresholds.

---

### 9. Supply Chain Disruption Response

**Prompt:**
```
Respond to supply chain disruption:
- Disruption type:
  * Supplier delay (factory shutdown, material shortage)
  * Transportation disruption (port congestion, trucking capacity shortage)
  * Natural disaster (hurricane, earthquake blocking routes)
  * Geopolitical (tariffs, trade restrictions, sanctions)
- Impact:
  * Products affected (which SKUs impacted?)
  * Severity (days of delay, stockout risk)
  * Customer impact (which orders at risk of missing delivery commitments?)

Mitigation options:
1. Expedite from current supplier (air freight instead of ocean, premium cost)
2. Source from alternative supplier (secondary supplier, different geography)
3. Substitute product (offer similar item if exact SKU unavailable)
4. Adjust production schedule (build other products first, delay affected items)
5. Communicate with customers (proactive notification, manage expectations)

Recommend:
- Immediate actions (next 24-48 hours)
- Short-term tactics (next 2 weeks)
- Long-term resilience (diversify suppliers, increase safety stock, nearshoring)

Estimate cost vs. impact (is $50K air freight worth avoiding $500K in lost sales?).
```

**Pro Tip:** Build supply chain visibility (track suppliers' suppliers); early warning = more response options.

---

### 10. Warehouse Space Utilization & Slotting

**Prompt:**
```
Optimize warehouse space and slotting:
- Warehouse layout:
  * Total square footage
  * Racking configuration (pallet racks, shelving, floor stack)
  * Zones (receiving, reserve storage, picking, packing, shipping)
- Current inventory:
  * SKUs stored (quantity, dimensions per unit)
  * Turnover velocity (A items: fast-movers, C items: slow-movers)
  * Seasonal patterns (Halloween costumes spike in Sept-Oct)
- Storage constraints:
  * Temperature-controlled zones (refrigerated, frozen)
  * Hazmat storage (flammable, corrosive require special areas)
  * Security (high-value items in caged area)

Analyze space utilization:
- Current utilization % (occupied space / total capacity)
- Wasted space (aisles too wide, low-density storage)
- Slotting efficiency (are fast-movers in golden zone? or buried in back?)

Recommend slotting strategy:
- A items (80% of picks): Closest to packing (golden zone, chest-height shelves)
- B items (15% of picks): Mid-distance
- C items (5% of picks): Furthest, highest shelves (seldom accessed, okay to walk far)

If out of space:
- Vertical expansion (add mezzanine, taller racks)
- Offsite overflow storage (satellite warehouse)
- SKU rationalization (discontinue slow-moving items, free up space)
```

**Pro Tip:** Re-slot quarterly; fast-movers change seasonally (Christmas items are A in Nov-Dec, C rest of year).

---

## Advanced Techniques

### Digital Twin for Warehouse Simulation
**Prompt Pattern:**
```
Simulate warehouse operations with proposed changes:
- Change: [Add 10 pickers, automate packing line, reorganize layout]
- Simulate: Order volume, pick times, throughput
- Predict: Impact on orders per day, labor cost, space utilization
- Decide: Implement change if ROI positive (payback <2 years)
```

### Carbon Footprint Optimization
**Prompt Pattern:**
```
Calculate carbon emissions for delivery:
- Route miles, vehicle type (diesel, electric, hybrid)
- Load factor (full truck vs. half-empty)
- Recommend: Consolidate shipments, switch to EVs, offset emissions
- Report: CO₂ per package delivered (sustainability metric)
```

### Network Optimization for Facility Location
**Prompt Pattern:**
```
Optimize warehouse/distribution center network:
- Customer demand heatmap (where are customers located?)
- Current facilities (locations, capacities, costs)
- Evaluate: Should we add facility? Close facility? Relocate?
- Objective: Minimize total cost (facilities + transportation) while meeting service level (2-day delivery)
```

---

## Metrics to Track

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| **On-Time Delivery** | >95% | Customer satisfaction, contract compliance |
| **Cost per Delivery** | Minimize | Profitability (last-mile is 50% of total logistics cost) |
| **Order Accuracy** | >99% | Wrong item shipped = returns, customer dissatisfaction |
| **Warehouse Pick Rate** | 40+ orders/hour | Labor productivity |
| **Inventory Turnover** | 8-12x/year | Capital efficiency (cash tied up in inventory) |
| **Stockout Rate** | <2% | Avoid lost sales |
| **Fleet Utilization** | >85% | Asset efficiency (trucks, forklifts) |
| **Damage/Loss Rate** | <0.5% | Quality, customer trust |

---

## Related Resources

- **Full Playbook**: [Logistics & Supply Chain Playbook](../../PLAYBOOKS/playbook-logistics.md)
- **AI Integration**: [AI Integration Playbook](../../PLAYBOOKS/playbook-ai-integration.md)
- **Data Contracts**: [Example: Shipment Tracking Event](../../PLAYBOOKS/playbook-logistics.md#data-contracts)
- **Ethical AI**: [Worker Safety, Environmental Sustainability](../../PLAYBOOKS/playbook-logistics.md#ethical-logistics)

---

## Tips for Success

1. **Real-Time Data**: Install GPS on trucks, scanners in warehouse (can't optimize without visibility)
2. **Start Simple**: Pilot route optimization on 10 drivers, prove value, then scale to 100
3. **Driver Input**: Drivers know local roads, customer quirks (AI suggests, driver validates)
4. **Safety First**: Never sacrifice worker safety for efficiency (ergonomic pick paths, safe driving speeds)
5. **Customer Communication**: Proactive notifications (out for delivery, delays) reduce "where's my order?" calls 80%
6. **Continuous Improvement**: Review metrics weekly, iterate on AI models (retrain with latest data)
7. **Sustainability**: Route optimization reduces emissions 15%; market to eco-conscious customers

---

**Questions?** Join the SOLID.AI community or open an issue on [GitHub](https://github.com/gusafr/midora-solid-ai/issues)!

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
