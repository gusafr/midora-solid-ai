# Commerce & Retail AI Reference Card

**Quick-start AI prompts for retailers, e-commerce operators, and merchandising teams**

---

## 10 Essential AI Prompts for Commerce

### 1. Demand Forecasting

**Prompt:**
```
Analyze historical sales data for [Product Category] over the past [Time Period]. 
Account for:
- Seasonality (holidays, weather, back-to-school)
- Promotions and discounts
- Market trends and competitor activity

Forecast demand for the next [30/60/90] days by SKU and location.
Highlight products at risk of stockout and those likely to be overstocked.
```

**Pro Tip:** Include external factors like local events, weather forecasts, and social media trends for more accurate predictions.

---

### 2. Personalized Product Recommendations

**Prompt:**
```
Based on this customer's profile:
- Purchase history: [List recent purchases]
- Browsing behavior: [Products viewed, time on page, cart additions]
- Preferences: [Size, color, brand, price range]

Recommend 5 products they're most likely to purchase next.
For each recommendation, explain the reasoning and suggest messaging 
(e.g., "Complete your look," "Customers like you also bought").
```

**Pro Tip:** Test recommendations with A/B testing; measure click-through rate and conversion to optimize algorithm.

---

### 3. Dynamic Pricing Optimization

**Prompt:**
```
Analyze pricing strategy for [Product/Category]:
- Current price: [Amount]
- Cost: [Amount]
- Competitor prices: [List competitors and their prices]
- Inventory level: [Units on hand]
- Sales velocity: [Units sold per day]
- Customer price sensitivity: [Elastic/Inelastic]

Recommend optimal price to maximize [Revenue/Profit/Market Share].
If suggesting price change, estimate impact on sales volume and total revenue.
```

**Pro Tip:** Set guardrails: minimum margin %, maximum price change per day, blackout periods (no surge pricing during emergencies).

---

### 4. Fraud Detection for E-Commerce

**Prompt:**
```
Evaluate this transaction for fraud risk:
- Order value: [Amount]
- Customer: [New/Returning, Account age, Purchase history]
- Shipping address: [Matches billing? Previously used?]
- Payment method: [Credit card, PayPal, BNPL]
- Device/IP: [Known device? VPN? High-risk country?]
- Order details: [High-risk items like electronics, gift cards?]

Provide fraud risk score (0-100) and recommend: 
Approve | Manual Review | Decline
```

**Pro Tip:** Balance fraud prevention with customer experience; don't block legitimate customers with overly aggressive filters.

---

### 5. Customer Segmentation for Targeted Marketing

**Prompt:**
```
Segment our customer base using these dimensions:
- Recency: Last purchase date
- Frequency: Number of purchases in past year
- Monetary: Total spend
- Product affinity: Categories purchased
- Channel preference: Online, in-store, mobile app

Create 5-7 actionable segments (e.g., "High-value loyalists," "At-risk churners," 
"Bargain hunters") and recommend marketing strategies for each.
```

**Pro Tip:** Automate segment updates weekly; trigger campaigns when customers move between segments (e.g., win-back when VIP becomes at-risk).

---

### 6. Inventory Allocation Across Channels

**Prompt:**
```
We have [X units] of [Product] and sell through:
- E-commerce website
- Mobile app
- Retail stores (List locations)
- Marketplace (Amazon, eBay)

Based on:
- Sales velocity by channel
- Profit margin by channel (after fees, shipping)
- Stock transfer costs
- Fulfillment speed requirements

Recommend how to allocate inventory to maximize profit while meeting 
customer expectations (e.g., 2-day shipping for online, in-stock for stores).
```

**Pro Tip:** Reserve safety stock for high-margin channels; dynamically reallocate as demand shifts.

---

### 7. Visual Search & Product Matching

**Prompt:**
```
Customer uploaded this image: [Image or description].

Search our catalog for:
1. Exact matches (same product)
2. Similar items (style, color, pattern)
3. Complementary products ("Complete the look")

Rank results by visual similarity and availability.
If out of stock, suggest alternatives with comparable attributes.
```

**Pro Tip:** Train visual search on your product images + lifestyle photos; tag products with detailed attributes (collar type, hem length, etc.).

---

### 8. Customer Churn Prediction

**Prompt:**
```
Analyze customer behavior to predict churn risk:
- Days since last purchase
- Purchase frequency declining
- Email engagement (open rate, click rate)
- Customer service interactions (complaints, returns)
- Cart abandonment rate

Score customers 0-100 for churn risk.
For high-risk customers, recommend retention tactics:
- Personalized discount
- Product recommendations
- Win-back email campaign
- Loyalty program incentive
```

**Pro Tip:** Act early; customers who haven't purchased in 60 days are easier to win back than those dormant for 180 days.

---

### 9. Omnichannel Fulfillment Optimization

**Prompt:**
```
Customer ordered:
- [Item 1] - In stock at: Store A, Warehouse B
- [Item 2] - In stock at: Store C, Warehouse D
- [Item 3] - In stock at: Warehouse B

Customer location: [ZIP code]
Delivery expectation: [Standard/Express/Next-Day]

Recommend fulfillment strategy:
- Which facility ships each item (minimize cost, meet delivery promise)
- Ship separately or consolidate (balance speed vs. shipping cost)
- Offer in-store pickup as alternative?
```

**Pro Tip:** Expose inventory availability to customers ("Available at your local store for pickup today!") to reduce shipping costs.

---

### 10. Return Fraud Detection & Prevention

**Prompt:**
```
Evaluate this return request for fraud risk:
- Customer: [Return history, Account age]
- Item: [Category, Condition reported, Original price]
- Reason: [Doesn't fit, Defective, Changed mind]
- Purchase date: [X days ago]
- Tags/packaging: [Intact? Worn? Missing?]

Assess likelihood of:
- Wardrobing (wore item, returning)
- Counterfeit swap (returning fake, keeping real)
- Serial returner abuse

Recommend: Approve | Inspect | Decline | Ban customer (if serial abuser)
```

**Pro Tip:** Track return rate by customer; those exceeding 30% should be flagged for review (possible abuse).

---

## Advanced Techniques

### Cross-Sell & Upsell Optimization
**Prompt Pattern:**
```
Customer added [Item] to cart at [Price].
What complementary items should we recommend (cross-sell)?
What higher-value alternatives should we suggest (upsell)?
Provide reasoning and expected revenue lift for each recommendation.
```

### Sentiment Analysis on Product Reviews
**Prompt Pattern:**
```
Analyze reviews for [Product]:
- Overall sentiment (positive/negative/neutral)
- Common themes (quality, fit, color accuracy, shipping)
- Specific complaints to address
- Opportunities to highlight in marketing ("Customers love the soft fabric!")
```

### Markdown Optimization for Clearance
**Prompt Pattern:**
```
We have [X units] of [Product] that must clear in [Y weeks].
Current price: [Amount], Cost: [Amount]
Recommend markdown schedule:
- Week 1: [% off]
- Week 2: [% off]
- Week 3: [% off]
Goal: Maximize revenue, minimize dead stock.
```

---

## Metrics to Track

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| **Conversion Rate** | 2-5% (e-commerce) | How many visitors become buyers |
| **Average Order Value (AOV)** | Increasing | Revenue per transaction |
| **Cart Abandonment Rate** | <70% | Reduce friction in checkout |
| **Customer Lifetime Value (CLV)** | 3x acquisition cost | Long-term profitability |
| **Inventory Turnover** | 8-12x/year | Efficient capital use |
| **Stockout Rate** | <2% | Avoid lost sales |
| **Return Rate** | <10% | Product quality, accurate descriptions |
| **Net Promoter Score (NPS)** | >50 | Customer satisfaction, loyalty |

---

## Related Resources

- **Full Playbook**: [Commerce & Retail Playbook](../../PLAYBOOKS/playbook-commerce.md)
- **AI Integration**: [AI Integration Playbook](../../PLAYBOOKS/playbook-ai-integration.md)
- **Data Contracts**: [Example: Product Recommendation Event](../../PLAYBOOKS/playbook-commerce.md#data-contracts)
- **Ethical AI**: [Fair Pricing, Privacy-Respecting Personalization](../../PLAYBOOKS/playbook-commerce.md#ethical-commerce)

---

## Tips for Success

1. **Start Small**: Pilot AI with one use case (e.g., demand forecasting for top 20% SKUs by revenue)
2. **Measure Everything**: Track metrics before/after AI (prove ROI)
3. **Human Oversight**: Merchandisers review AI recommendations (don't blindly auto-price)
4. **Privacy First**: Personalization requires data, but respect opt-outs and minimize collection
5. **Test Continuously**: A/B test recommendations, pricing, messaging (AI improves with feedback)
6. **Balance Automation**: Automate repetitive tasks (inventory alerts), keep humans for strategy (category planning)
7. **Customer Experience**: AI should enhance CX (faster checkout, better recommendations), not frustrate (intrusive tracking)

---

**Questions?** Join the SOLID.AI community or open an issue on [GitHub](https://github.com/gusafr/midora-solid-ai/issues)!

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
