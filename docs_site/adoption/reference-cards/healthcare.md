# Healthcare AI Reference Card

**Quick-start AI prompts for clinicians, hospital administrators, and healthcare IT teams**

⚠️ **CRITICAL DISCLAIMER**: AI in healthcare is advisory only. All clinical decisions must be made by licensed healthcare professionals. AI assists, humans decide. This reference card is for educational purposes and does not constitute medical advice.

---

## 10 Essential AI Prompts for Healthcare

### 1. Clinical Decision Support for Diagnosis

**Prompt:**
```
Patient presentation:
- Chief complaint: [Symptoms described by patient]
- Vital signs: [BP, HR, Temp, RR, SpO2]
- Medical history: [Chronic conditions, past diagnoses]
- Medications: [Current prescriptions]
- Lab results: [Recent tests with values and reference ranges]
- Physical exam findings: [Key observations]

Generate differential diagnosis (ranked by likelihood):
1. [Most likely diagnosis] - Supporting evidence: [...]
2. [Alternative diagnosis] - Supporting evidence: [...]
3. [Less likely but serious diagnosis to rule out] - Why consider: [...]

Suggest additional tests or imaging to confirm/rule out diagnoses.
Flag red flags requiring urgent intervention.
```

**⚠️ CRITICAL:** Physician reviews ALL AI suggestions, applies clinical judgment, considers patient context. AI assists, doctor decides.

---

### 2. Medical Imaging Analysis (Radiology)

**Prompt:**
```
Analyze this [X-ray/CT/MRI] image:
- Body region: [Chest, Brain, Abdomen, Musculoskeletal]
- Clinical indication: [Why imaging ordered, suspected condition]
- Patient context: [Age, symptoms, relevant history]

Identify:
- Normal anatomy (confirm expected structures present)
- Abnormalities (masses, fractures, inflammation, hemorrhage)
- Location, size, characteristics of findings
- Comparison to prior imaging (if available): Stable | Improved | Worsened

Provide preliminary interpretation and recommend:
- Additional imaging views or modalities
- Urgent findings requiring immediate notification
- Confidence level in findings (low/medium/high)
```

**⚠️ CRITICAL:** Board-certified radiologist reviews all AI interpretations. AI flags suspicious findings; radiologist makes final diagnosis.

---

### 3. Patient Risk Stratification

**Prompt:**
```
Assess patient risk for [Sepsis/Readmission/Deterioration/Mortality]:
- Current condition: [Diagnosis, vital signs, lab values]
- Risk factors: [Age, comorbidities, frailty, social determinants]
- Recent trends: [Vital signs getting worse? Labs deteriorating?]
- Early warning scores: [NEWS, MEWS, qSOFA]

Calculate risk score (0-100) and categorize:
- Low risk: Continue current care
- Medium risk: Increase monitoring frequency, consider intervention
- High risk: Escalate to ICU, initiate protocol (e.g., sepsis bundle)

Recommend preventive interventions to reduce risk.
```

**Pro Tip:** Integrate risk scores into EHR alerts; notify clinical team when patient moves from low→high risk (early intervention saves lives).

---

### 4. Medication Interaction & Allergy Check

**Prompt:**
```
Patient being prescribed: [New medication, dose, route, frequency]

Current medications: [List all prescriptions, OTC, supplements]
Allergies: [Drug allergies, severity of reaction]
Conditions: [Renal function, liver function, pregnancy status]
Age: [Pediatric dosing differs, elderly more sensitive]

Check for:
- Drug-drug interactions (severity: Minor | Moderate | Severe | Contraindicated)
- Drug-allergy conflicts (cross-reactivity with allergens)
- Dose appropriateness (adjust for renal/hepatic impairment, age, weight)
- Duplicate therapy (already taking same drug class)

Recommend: Proceed | Adjust dose | Choose alternative medication | Contraindicated
```

**⚠️ CRITICAL:** Pharmacist or physician reviews all high-severity alerts. Never override contraindication alerts without expert consultation.

---

### 5. Automated Medical Coding (ICD-10, CPT)

**Prompt:**
```
Clinical documentation:
- Chief complaint: [Patient's reason for visit]
- History of present illness: [Detailed symptom narrative]
- Physical exam: [Findings]
- Assessment: [Diagnosis]
- Plan: [Treatments, procedures, tests ordered]

Generate appropriate medical codes:
- ICD-10 diagnosis codes (primary + secondary diagnoses)
- CPT procedure codes (office visit level, procedures performed)
- Modifiers (if applicable)

Ensure codes support medical necessity (test/treatment justified by diagnosis).
Flag potential coding errors:
- Undercoding (missed billable services)
- Overcoding (upcoding risk, compliance issue)
- Unbundling (billing separately what should be bundled)
```

**Pro Tip:** Certified coder reviews AI-suggested codes before claim submission; accurate coding = proper reimbursement + compliance.

---

### 6. Patient Admission Prediction

**Prompt:**
```
Emergency Department patient:
- Chief complaint: [Presenting problem]
- Vital signs: [BP, HR, Temp, RR, SpO2, Pain level]
- Lab results: [Key values]
- Imaging: [If performed, findings]
- Triage level: [ESI 1-5]
- Disposition uncertainty: [Can we safely discharge, or admit?]

Predict probability of admission (0-100%).
If admission likely, recommend:
- Admission service (Medicine, Surgery, ICU, Observation)
- Expedite bed request (reduce ED boarding time)

If discharge likely, recommend:
- Outpatient follow-up (PCP, specialist)
- Discharge instructions, red flags to return
```

**Pro Tip:** Helps hospital flow (early bed requests reduce ED overcrowding); but physician makes final admit/discharge decision.

---

### 7. Clinical Trial Matching

**Prompt:**
```
Patient profile:
- Diagnosis: [Cancer type/stage, rare disease, chronic condition]
- Demographics: [Age, gender, location]
- Prior treatments: [What's been tried, response, toxicities]
- Biomarkers: [Genetic mutations, receptor status, lab values]
- Performance status: [ECOG 0-4, can patient tolerate trial?]

Search active clinical trials matching patient:
- Inclusion criteria met
- Exclusion criteria NOT violated
- Geographic accessibility (trial sites within [X miles])
- Trial phase (1, 2, 3) and risk/benefit

Rank top 3 trials by fit.
Provide trial details: NCT number, contact, enrollment status.
```

**Pro Tip:** Especially valuable for rare diseases, refractory cancers where standard treatments exhausted; gives patients hope and access to cutting-edge therapies.

---

### 8. Discharge Planning & Readmission Prevention

**Prompt:**
```
Patient being discharged:
- Diagnosis: [Reason for admission, treatments received]
- Discharge destination: [Home, SNF, rehab, home health]
- Readmission risk factors: [Heart failure, COPD, complex medication regimen, social isolation]
- Support system: [Caregiver availability, health literacy]
- Barriers: [Transportation, medication affordability, language]

Assess 30-day readmission risk (0-100%).
If high risk, recommend interventions:
- Medication reconciliation (clear discharge med list, teach-back)
- Follow-up appointment scheduled within 7 days
- Home health referral (nursing visits, therapy)
- Durable medical equipment (walker, oxygen, hospital bed)
- Social work consult (address food insecurity, housing, transportation)

Generate patient-friendly discharge instructions (6th-grade reading level).
```

**Pro Tip:** Hospitals penalized for excessive readmissions (CMS); proactive planning saves money and improves patient outcomes.

---

### 9. Staffing & Capacity Planning

**Prompt:**
```
Hospital census and forecast:
- Current census: [Inpatients by unit: Med-Surg, ICU, Peds, OB]
- Scheduled admissions: [Elective surgeries, planned births]
- ED volume trend: [Patients in ED, admission rate %]
- Seasonal factors: [Flu season, holiday weekend]
- Historical patterns: [Average daily admissions for this time of year]

Predict bed demand for next [24/48/72 hours] by unit.
Recommend staffing levels:
- Nurse-to-patient ratios by acuity
- Flex up (call in additional staff) or flex down (cancel on-call)?
- Transfer patients between units to balance capacity
- Divert ambulances if at capacity (last resort)

Alert if capacity crisis predicted (>95% occupancy, no ICU beds).
```

**Pro Tip:** Accurate forecasting prevents understaffing (burnout, safety risk) and overstaffing (wasted cost).

---

### 10. Population Health & Chronic Disease Management

**Prompt:**
```
Patient population: [Diabetics, CHF patients, Hypertensives, etc.]
Size: [Number of patients in cohort]

Identify high-risk patients:
- Uncontrolled disease (HbA1c >9%, BP >160/100)
- Non-adherent to medications (refill gaps)
- Overdue for preventive care (retinal exam, foot exam, flu shot)
- Frequent ED visits or hospitalizations (care coordination opportunity)

Stratify into risk tiers:
- Tier 1 (Lowest risk): Routine outreach, annual visits
- Tier 2 (Moderate risk): Care manager check-ins, quarterly visits
- Tier 3 (High risk): Intensive case management, monthly touchpoints

For each tier, recommend interventions:
- Patient outreach (calls, secure messages, home visits)
- Medication optimization, adherence support
- Lifestyle coaching (nutrition, exercise, smoking cessation)
- Close the gaps in care (schedule overdue screenings)
```

**Pro Tip:** Value-based care rewards keeping populations healthy (not just treating sick patients); AI helps prioritize limited resources.

---

## Advanced Techniques

### Natural Language Processing for Clinical Notes
**Prompt Pattern:**
```
Extract structured data from this clinical note:
- Problems: [Active diagnoses]
- Medications: [Current prescriptions with doses]
- Allergies: [Drug, food, environmental]
- Social history: [Smoking, alcohol, substance use]
- Family history: [Genetic risk factors]

Enable downstream analytics (quality reporting, research) without manual chart review.
```

### Predictive Modeling for Length of Stay
**Prompt Pattern:**
```
Predict hospital length of stay for admitted patient:
- Diagnosis: [Primary and secondary]
- Age, comorbidities, severity of illness
- Procedures planned (surgery, etc.)
- Historical LOS for similar patients

Estimate discharge date.
Use for: Discharge planning, bed turnover, family communication.
```

### AI-Assisted Physician Documentation
**Prompt Pattern:**
```
Transcribe patient encounter (audio from clinic visit).
Generate SOAP note:
- Subjective: Patient's description of symptoms
- Objective: Vitals, exam findings, test results
- Assessment: Diagnosis
- Plan: Treatment, follow-up

Physician reviews, edits, signs note (saves 10-15 min per patient).
```

---

## Metrics to Track

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| **Clinical Accuracy** | >95% (AI suggestions concordant with expert review) | Patient safety, trust in AI |
| **Time Saved** | 30% reduction in documentation time | Reduce physician burnout, more patient face time |
| **Diagnostic Accuracy** | Sensitivity >90%, Specificity >95% | Catch diseases early (sensitivity), avoid false alarms (specificity) |
| **Readmission Rate** | <15% (30-day) | Quality of care, cost (CMS penalties for excess readmissions) |
| **Early Sepsis Detection** | Alert 6+ hours before clinical recognition | Sepsis mortality drops 7% per hour delay in treatment |
| **Medication Error Rate** | <1 per 1,000 orders | Patient safety (ADEs cause 1.3M ED visits/year in US) |
| **Patient Safety Events** | Zero harm from AI errors | Non-negotiable; AI must fail safe (alert human, don't auto-treat) |

---

## Related Resources

- **Full Playbook**: [Healthcare Playbook](../../PLAYBOOKS/playbook-healthcare.md)
- **AI Integration**: [AI Integration Playbook](../../PLAYBOOKS/playbook-ai-integration.md)
- **Data Contracts**: [Example: Lab Result Event](../../PLAYBOOKS/playbook-healthcare.md#data-contracts)
- **Ethical AI**: [HIPAA Compliance, Patient Safety, FDA Regulation](../../PLAYBOOKS/playbook-healthcare.md#ethical-healthcare)

---

## Tips for Success

1. **Human-in-the-Loop**: AI advises, clinician decides (regulatory requirement + patient safety)
2. **Regulatory Compliance**: Know FDA Medical Device classification (is your AI a Class II device requiring 510k?)
3. **HIPAA Security**: Encrypt PHI, access controls, audit logs, BAAs with AI vendors
4. **Clinical Validation**: Validate AI on YOUR patient population (algorithms trained on academic centers may not generalize to community hospitals)
5. **Transparency**: Tell patients if AI used in care (informed consent, trust)
6. **Bias Testing**: Ensure AI performs equitably across race, gender, age, socioeconomic status (health equity)
7. **Fail-Safe Design**: If AI fails/offline, clinical workflows must continue (don't create dependency)
8. **Physician Buy-In**: Include clinicians in AI selection, training, feedback (not imposed from IT)

---

## Ethical & Legal Considerations

⚠️ **PATIENT SAFETY PARAMOUNT**: 
- AI is ADVISORY ONLY (never autonomous treatment)
- Physician liability not transferred to AI (doctor remains responsible)
- Document when AI recommendations overridden (clinical judgment)
- Report AI errors to vendor, FDA (if medical device), institutional safety committee

⚠️ **PRIVACY & SECURITY**:
- De-identify data before training AI (HIPAA requirement)
- Secure AI systems to HIPAA standards (encryption, access controls, audit trails)
- Patient consent for AI use in care (transparency)

⚠️ **EQUITY & BIAS**:
- Test AI across demographics (ensure no disparate performance by race, gender)
- Don't let AI perpetuate healthcare disparities (algorithms trained on biased data can discriminate)

---

**Questions?** Join the SOLID.AI community or open an issue on [GitHub](https://github.com/gusafr/midora-solid-ai/issues)!

⚠️ **CRITICAL REMINDER**: This is educational content. Consult legal, regulatory, and clinical experts before deploying AI in healthcare. Patient safety above all else.

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
