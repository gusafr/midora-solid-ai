# Squad Organization Quick Reference

## ✅ DO: Organize by Business Services

```
🛒 Order Fulfillment Squad
   └─ Cross-functional team (PO, Dev, QA, Ops)
   └─ Owns: Purchase → Payment → Inventory → Shipping
   └─ Output: OrderCompleted Event

👤 Customer Onboarding Squad  
   └─ Cross-functional team (PO, UX, Dev, QA)
   └─ Owns: Signup → Verification → Activation
   └─ Output: CustomerActivated Event

🛡️ Fraud Detection Squad
   └─ Cross-functional team (PO, Data Scientist, ML Eng)
   └─ Owns: Analysis → Risk Scoring → Alerts
   └─ Output: FraudAssessment Event
```

**Result:** ✅ Clear ownership | ✅ No duplication | ✅ Autonomous delivery

---

## ❌ DON'T: Organize by Technical Layers

```
Frontend Squad → Backend Squad → Database Squad → QA Squad
     ↓               ↓               ↓              ↓
  Handoff         Handoff         Handoff      Handoff
```

**Result:** ❌ Coordination overhead | ❌ Unclear ownership | ❌ Duplicate efforts

---

## 6 Validation Questions

Before forming a squad, answer:

1. ❓ **What business capability** does this serve?
2. ❓ **Who are the end users/stakeholders?**
3. ❓ **What value does it deliver independently?**
4. ❓ **What are the clear input/output contracts?**
5. ❓ **Can this squad succeed without constant coordination?**
6. ❓ **Is the scope sustainable (not too broad/narrow)?**

If you can't answer all 6 clearly → **Boundary needs refinement**

---

## Examples by Domain

**E-Commerce:**
- Product Catalog Management
- Shopping Cart & Checkout
- Order Fulfillment
- Returns & Refunds
- Customer Support

**SaaS:**
- User Onboarding & Activation
- Subscription Management
- Usage Analytics & Billing
- Integration Marketplace
- Customer Success Operations

**Finance:**
- Payment Processing
- Fraud Detection & Prevention
- Reconciliation & Settlement
- Regulatory Reporting
- Credit Risk Assessment

**Healthcare:**
- Patient Registration
- Appointment Scheduling
- Clinical Documentation
- Claims Processing
- Care Coordination

---

## See Full Documentation

- **Diagram:** `DIAGRAMS/squad-business-service-organization.mmd`
- **Playbook:** `PLAYBOOKS/organizational/squads.md`
- **Checklist:** `ADOPTION/CHECKLISTS/squad-formation.md`
- **Template:** `ADOPTION/TEMPLATES/squad-charter-template.md`
- **Summary:** `BUSINESS-SERVICE-ORGANIZATION-UPDATE.md`

---

**Framework:** SOLID.AI | **Updated:** 2025-11-05 | **Version:** 1.1
