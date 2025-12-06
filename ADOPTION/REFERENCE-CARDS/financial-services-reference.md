# Financial Services AI Reference Card

**Quick-start AI prompts for bankers, risk analysts, compliance officers, and fintech teams**

⚠️ **CRITICAL DISCLAIMER**: AI in financial services must comply with regulations (Basel III, Dodd-Frank, ECOA, fair lending laws). All AI-driven decisions with material impact (credit, lending, account closure) require human review and must be explainable. Consult legal/compliance before deployment.

---

## 10 Essential AI Prompts for Financial Services

### 1. Fraud Detection for Transactions

**Prompt:**
```
Evaluate this transaction for fraud risk:
- Transaction details:
  * Amount: [USD amount]
  * Merchant: [Name, category, location]
  * Time: [Timestamp, unusual hour?]
  * Channel: [Card present, online, mobile, ATM]
- Customer profile:
  * Location: [Where customer normally transacts]
  * Spending patterns: [Typical transaction size, frequency, categories]
  * Account age: [New account = higher risk]
  * Recent activity: [Unusual pattern? Multiple transactions in short time?]
- Device/IP:
  * Device ID: [Known device or new?]
  * IP geolocation: [Matches customer location?]
  * VPN/proxy detected: [Yes/No]

Provide fraud score (0-100) and categorize:
- Low risk (<20): Auto-approve
- Medium risk (20-70): Step-up authentication (SMS code, push notification)
- High risk (>70): Decline or manual review

Explain reasoning (for compliance, customer inquiry).
```

**Pro Tip:** Balance fraud prevention with customer experience; false positives anger customers (legitimate transaction declined).

---

### 2. Credit Risk Assessment & Underwriting

**Prompt:**
```
Applicant requesting [Mortgage/Auto Loan/Personal Loan/Credit Card]:
- Loan amount: [USD amount]
- Purpose: [Home purchase, debt consolidation, etc.]
- Applicant profile:
  * Credit score: [FICO, VantageScore]
  * Income: [Annual, verified employment]
  * Debt-to-income ratio: [%]
  * Credit history: [Length, payment history, utilization]
  * Assets/collateral: [Down payment, savings, home equity]
  * Derogatory marks: [Bankruptcies, foreclosures, collections]

Assess credit risk:
- Probability of default (PD): [%]
- Loss given default (LGD): [%]
- Expected loss: [USD amount]

Recommend decision:
- Approve at [Interest rate %]
- Approve with conditions (higher rate, lower amount, co-signer)
- Counter-offer (smaller loan, different product)
- Decline (with adverse action notice, reason for denial per ECOA)

Ensure compliance:
- ECOA: No discrimination based on race, gender, age, marital status, religion
- Disparate impact: Check if approval rate differs by protected class
- Explainability: Provide reasons for denial (not just "algorithm said no")
```

**⚠️ CRITICAL:** Regularly test credit model for disparate impact (e.g., approval rate for Black applicants ≥80% of White applicants). Document testing for regulatory exams.

---

### 3. Anti-Money Laundering (AML) & Suspicious Activity Detection

**Prompt:**
```
Monitor customer account for suspicious activity (AML/BSA compliance):
- Customer: [Individual, business]
- Account activity:
  * Large deposits: [>$10K, structured to avoid CTR reporting?]
  * Wire transfers: [To/from high-risk countries, shell companies?]
  * Cash transactions: [Frequent, just below reporting threshold?]
  * Rapid movement of funds: [In and out quickly, layering?]
- Customer profile:
  * Expected activity: [Salary deposits, normal bills]
  * Risk rating: [Low, Medium, High based on occupation, geography, product]
- Red flags:
  * Inconsistent with stated business purpose
  * Politically Exposed Person (PEP) involvement
  * Sanctions list match (OFAC, UN, EU)

Assess AML risk (0-100):
- Low risk: No action
- Medium risk: Enhanced monitoring
- High risk: File Suspicious Activity Report (SAR), freeze account if necessary

Generate SAR narrative (who, what, when, where, why suspicious).
```

**Pro Tip:** File SARs within 30 days of detection (FinCEN requirement); maintain confidentiality (don't tip off customer).

---

### 4. Know Your Customer (KYC) & Onboarding

**Prompt:**
```
Verify new customer identity (KYC compliance):
- Customer information:
  * Name: [Full legal name]
  * Date of birth: [DOB]
  * Address: [Residential address]
  * Government ID: [Passport, driver's license number]
  * Tax ID: [SSN for US, equivalent for other countries]
- Verification steps:
  1. Identity verification (check ID against databases, liveness detection for remote onboarding)
  2. Address verification (utility bill, bank statement)
  3. Sanctions screening (OFAC, UN, EU watchlists)
  4. PEP check (Politically Exposed Person, higher AML risk)
  5. Adverse media screening (negative news, criminal activity)

Risk assessment:
- Low risk: Expedite onboarding (standard monitoring)
- Medium risk: Additional documentation required
- High risk: Enhanced due diligence (source of wealth, business purpose)
- Prohibit: Sanctions match, identity cannot be verified

Generate CIP (Customer Identification Program) record for regulatory compliance.
```

**Pro Tip:** Use AI for faster, more accurate ID verification (OCR + biometric liveness detection); reduces onboarding friction, improves conversion.

---

### 5. Robo-Advisor Investment Recommendations

**Prompt:**
```
Client seeking investment advice:
- Investment goals:
  * Goal: [Retirement, college savings, wealth accumulation]
  * Time horizon: [Years until goal]
  * Target amount: [USD amount needed]
- Risk profile:
  * Risk tolerance: [Conservative, Moderate, Aggressive]
  * Age: [Younger = can take more risk]
  * Income/liquidity needs: [Need cash flow from portfolio?]
  * Experience: [Sophisticated investor or beginner?]
- Current portfolio:
  * Assets: [Stocks, bonds, cash, real estate, alternatives]
  * Allocation: [% in each asset class]
  * Tax situation: [Taxable, IRA, 401k]

Recommend portfolio allocation:
- Asset mix (stocks/bonds/cash/alternatives %)
- Specific funds/ETFs (low-cost index funds)
- Tax optimization (tax-loss harvesting, municipal bonds for high earners)
- Rebalancing strategy (quarterly, threshold-based)

Provide expected return, volatility, probability of reaching goal.

Disclosures (SEC compliance):
- Fiduciary duty (advice in client's best interest, not highest commission)
- Conflicts of interest (if any)
- Fee structure (% AUM, flat fee, transparent)
```

**Pro Tip:** Robo-advisors democratize wealth management (low minimums, low fees); but humans still needed for complex situations (estate planning, tax strategies, behavioral coaching).

---

### 6. Market Risk (VaR) & Portfolio Analytics

**Prompt:**
```
Calculate Value at Risk (VaR) for portfolio:
- Portfolio holdings: [List securities, quantities, market values]
- Time horizon: [1 day, 10 day, 1 month]
- Confidence level: [95%, 99%]
- Historical data: [Returns, volatility, correlations]
- Risk factors: [Equity risk, interest rate risk, FX risk, credit spread risk]

Report:
- VaR: "95% confidence that portfolio will not lose more than $X in 1 day"
- Stress testing: Impact of scenarios (2008 crisis, COVID crash, interest rate shock)
- Concentration risk: Over-exposed to single sector/security?
- Tail risk: Potential for extreme losses (>99th percentile)

Recommend risk mitigation:
- Diversification (reduce concentration)
- Hedging (options, futures)
- Position limits (max % in any single security)
```

**Pro Tip:** VaR is backward-looking (based on history); stress testing forward-looking (what if unprecedented event?). Use both.

---

### 7. Customer Churn Prediction & Retention

**Prompt:**
```
Identify customers at risk of leaving (closing accounts, switching to competitor):
- Customer profile:
  * Tenure: [Years with bank]
  * Products held: [Checking, savings, credit card, mortgage, investment]
  * Profitability: [Revenue from fees, interest, cross-sell]
  * Engagement: [Last login, transaction frequency, app usage]
- Churn signals:
  * Balance declining (transferring money out)
  * Product closures (closed credit card, moved investments)
  * Customer service complaints (unresolved issues)
  * Competitor research (clicked on competitor ads, searched "switch banks")

Score churn risk (0-100):
- Low risk: Continue standard relationship management
- Medium risk: Proactive outreach (offer fee waiver, higher interest rate, personalized advice)
- High risk: Executive retention call, special retention offer

For high-value customers at risk, recommend personalized retention strategy.
```

**Pro Tip:** Retaining existing customers cheaper than acquiring new (5-25x cost difference); proactive retention saves revenue.

---

### 8. Regulatory Reporting & Compliance Automation

**Prompt:**
```
Generate regulatory report [Type: Call Report, CCAR, Liquidity Coverage Ratio]:
- Data sources: [Core banking, loan systems, investment portfolios, Treasury]
- Reporting period: [Quarter-end, month-end]
- Regulatory requirements:
  * Basel III: Capital adequacy ratios (CET1, Tier 1, Total Capital)
  * CCAR: Stress test results, capital plan
  * LCR: High-quality liquid assets / Net cash outflows over 30 days
  * CECL: Current Expected Credit Loss provisioning

Automate data aggregation:
- Reconcile data across systems (ensure consistency)
- Calculate required metrics/ratios
- Flag anomalies (ratio suddenly changed, likely data error)

Generate report in required format (FR Y-9C, FR 2052a, etc.).
Perform pre-submission validation (common errors, missing data).
```

**Pro Tip:** Regulatory reporting errors = enforcement actions, fines; AI reduces manual errors, speeds up quarterly/monthly cycles.

---

### 9. Algorithmic Trading & Execution Optimization

**Prompt:**
```
Execute large order [BUY/SELL X shares of Security Y]:
- Order size: [Large relative to average daily volume?]
- Urgency: [Execute immediately, or can work over hours/days?]
- Market conditions: [Volatile, liquid, market impact]

Recommend execution strategy:
- VWAP (Volume-Weighted Average Price): Spread order throughout day to match volume profile
- TWAP (Time-Weighted Average Price): Even distribution over time window
- Implementation Shortfall: Minimize difference between decision price and execution price
- Liquidity-seeking: Access dark pools, hidden orders to minimize market impact

Predict:
- Execution cost (slippage, market impact, opportunity cost)
- Optimal order splitting (size, timing)

Monitor execution:
- Real-time deviation from benchmark (VWAP, arrival price)
- Adjust strategy if market conditions change (volatility spike, news event)
```

**Pro Tip:** Best execution obligation (MiFID II, Reg NMS); document why execution strategy chosen (fiduciary duty).

---

### 10. Insurance Underwriting & Claims Fraud

**Prompt:**
```
Evaluate insurance application [Life/Auto/Home/Commercial]:
- Applicant profile:
  * Age, health, occupation (life insurance)
  * Driving record, vehicle (auto insurance)
  * Property location, construction, claims history (home insurance)
- Risk factors:
  * Pre-existing conditions, family history (life)
  * Accident history, DUI (auto)
  * Flood zone, wildfire risk, prior claims (home)

Recommend underwriting decision:
- Approve at [Premium amount, coverage limits]
- Approve with exclusions (pre-existing condition not covered)
- Decline (uninsurable risk)

Claims fraud detection:
- Claim details: [Loss description, amount, timing]
- Red flags: [Claim shortly after policy inception, exaggerated loss, inconsistent statements, history of claims]
- Fraud score (0-100): Low | Medium (investigate) | High (deny, refer to SIU)

Ensure fairness:
- No discrimination based on protected classes (race, gender, religion)
- Actuarially justified (premiums reflect risk, not bias)
```

**Pro Tip:** Insurance fraud costs industry $80B/year (US); AI detects patterns humans miss (organized fraud rings).

---

## Advanced Techniques

### Natural Language Processing for Earnings Call Sentiment
**Prompt Pattern:**
```
Analyze earnings call transcript for [Company]:
- Sentiment: Positive/Negative/Neutral
- Key themes: Revenue growth, margin pressure, forward guidance
- Executive tone: Confident, defensive, evasive
- Q&A dynamics: Tough questions from analysts, vague answers

Use for: Investment decision, risk assessment, portfolio management.
```

### Explainable AI for Credit Decisions
**Prompt Pattern:**
```
Generate adverse action notice for declined credit applicant:
- Primary reasons for denial (ECOA requires top 4 reasons):
  1. Credit score too low (below X)
  2. Debt-to-income ratio too high (above Y%)
  3. Insufficient credit history (only Z months)
  4. Recent derogatory marks (collection account)

Provide in plain language, inform of right to free credit report, dispute process.
```

### Behavioral Analytics for Insider Trading Detection
**Prompt Pattern:**
```
Monitor employee trading activity (insider trading surveillance):
- Employee: [Name, role, access to material non-public information (MNPI)]
- Trade: [Buy/Sell, security, amount, date]
- Context: [Upcoming earnings, M&A rumors, product launch]

Red flags:
- Trade before material news (advance knowledge?)
- Out of pattern (suddenly large position)
- Coordinated trading (multiple insiders trading same direction)

Escalate to compliance for investigation, potential SAR filing.
```

---

## Metrics to Track

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| **Fraud Detection Rate** | >90% (catch 90% of fraud) | Prevent losses, protect customers |
| **False Positive Rate** | <5% (don't block legitimate transactions) | Customer experience, operational cost |
| **Credit Loss Rate** | <2% of portfolio | Profitability, soundness (too high = bad underwriting) |
| **Disparate Impact Ratio** | >0.80 (4/5ths rule) | Fair lending compliance (ECOA, CFPB) |
| **AML Detection (SARs Filed)** | Appropriate level | Compliance (too few = missing activity, too many = inefficient) |
| **Customer Churn Rate** | <10% annually | Retention = profitability |
| **Regulatory Exam Findings** | Zero (or low severity) | Avoid fines, consent orders, reputation damage |

---

## Related Resources

- **Full Playbook**: [Financial Services Playbook](../../PLAYBOOKS/playbook-financial-services.md)
- **AI Integration**: [AI Integration Playbook](../../PLAYBOOKS/playbook-ai-integration.md)
- **Data Contracts**: [Example: Transaction Event](../../PLAYBOOKS/playbook-financial-services.md#data-contracts)
- **Ethical AI**: [Fair Lending, Regulatory Compliance, Explainability](../../PLAYBOOKS/playbook-financial-services.md#ethical-financial-services)

---

## Tips for Success

1. **Explainability is Non-Negotiable**: Credit denials, account closures require explanations (ECOA, FCRA); use interpretable models
2. **Test for Bias**: Regularly test AI for disparate impact (approval rates by race, gender, age); document testing for regulators
3. **Human-in-the-Loop**: High-stakes decisions (large credit approvals, SAR filing, account closure) require human review
4. **Model Risk Management**: Validate models, document assumptions, governance (SR 11-7 for banks)
5. **Regulatory Engagement**: Inform regulators of AI use (OCC, Fed, CFPB); some require pre-approval for novel uses
6. **Data Privacy**: Financial data highly sensitive (GLBA, GDPR); encryption, access controls, consent
7. **Fail-Safe**: If AI fails, revert to manual processes (don't halt critical operations)

---

## Ethical & Legal Considerations

⚠️ **FAIR LENDING**:
- Never use race, gender, age, marital status, religion, national origin as factors (prohibited by ECOA)
- Avoid proxy variables (ZIP code correlates with race, name with ethnicity)
- Test for disparate impact (if protected group rejected at >4/5ths rate, rebuttable presumption of discrimination)

⚠️ **TRANSPARENCY**:
- Provide explanations for adverse actions (credit denial, lower limit)
- Disclose AI use in customer-facing materials (building trust, regulatory expectation)
- Right to human review (GDPR, some US states require human decision for automated decisions)

⚠️ **COMPLIANCE**:
- Basel III: Capital adequacy for credit risk models
- Dodd-Frank: Stress testing, living wills for large banks
- GLBA: Privacy, data security
- BSA/AML: Suspicious activity monitoring, reporting
- FCRA: Accuracy of credit reporting, dispute resolution

---

**Questions?** Join the SOLID.AI community or open an issue on [GitHub](https://github.com/gusafr/midora-solid-ai/issues)!

⚠️ **CRITICAL REMINDER**: Consult legal, compliance, and risk management before deploying AI in financial services. Regulatory landscape complex and evolving.

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
