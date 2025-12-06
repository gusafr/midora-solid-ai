# Human Resources AI Reference Card

**Quick-start AI prompts for HR professionals, recruiters, and people operations teams**

⚠️ **CRITICAL DISCLAIMER**: AI in HR must comply with employment laws (EEOC, GDPR, labor regulations). All AI-driven hiring, promotion, and termination decisions require human review and must be free from bias. Regularly test for adverse impact on protected classes. Consult legal/compliance before deployment.

---

## 10 Essential AI Prompts for Human Resources

### 1. Resume Screening & Candidate Matching

**Prompt:**
```
Screen resume for job fit:
- Job description:
  * Title: [e.g., "Senior Software Engineer"]
  * Required skills: [Python, AWS, Microservices, 5+ years experience]
  * Nice-to-have skills: [Kubernetes, Machine Learning, team lead experience]
  * Education: [Bachelor's in Computer Science or equivalent]
  * Location: [Remote, NYC, Hybrid]
- Resume: [Upload PDF/DOCX or paste text]

Extract and analyze:
- Skills (technical, soft skills, certifications)
- Experience (years in role, company names, achievements)
- Education (degrees, institutions, graduation year)
- Career trajectory (progression, gaps, job-hopping pattern)

Generate:
- Match score (0-100) based on job requirements
- Gap analysis (What's missing? What exceeds requirements?)
- Red flags (frequent job changes <1 year, unexplained 2+ year gaps, title inconsistencies)
- Green flags (promotions, relevant certifications, top company experience)

Recommend: Interview | Maybe (need clarification) | Pass

⚠️ BIAS CHECK: Ensure scoring doesn't penalize:
- Career gaps (may be parental leave, caregiving, medical)
- Non-traditional education (bootcamps, self-taught)
- International experience (different job titles, school names)
```

**Pro Tip:** Review top 20 candidates manually; AI narrows 500→20, human picks final 5 to interview.

---

### 2. Interview Question Generation & Scoring

**Prompt:**
```
Generate structured interview questions for role:
- Position: [Job title]
- Key competencies to assess:
  * Technical skills: [Specific technologies, domain knowledge]
  * Soft skills: [Communication, teamwork, problem-solving, leadership]
  * Culture fit: [Company values, work style preferences]
- Interview format: [Phone screen, technical interview, behavioral, panel]

Generate 10 questions:
- 5 behavioral (STAR format: Situation, Task, Action, Result)
  * Example: "Tell me about a time you disagreed with your manager. How did you handle it?"
- 3 technical (assess depth of knowledge)
  * Example: "Explain the difference between SQL and NoSQL databases. When would you use each?"
- 2 situational ("What would you do if...")
  * Example: "Your project is behind schedule. Stakeholders demanding delivery. What do you do?"

For each question, provide:
- What we're assessing (competency)
- Good answer indicators (look for...)
- Red flags (avoid candidates who...)
- Scoring rubric (1-5 scale)

Post-interview:
- Transcribe interview (with candidate consent)
- Extract candidate responses to each question
- Score against rubric
- Generate summary: Strengths, Concerns, Hire/No Hire recommendation
```

**⚠️ CRITICAL:** All interviewers ask same questions (reduces bias, enables comparison); AI assists scoring, humans decide.

---

### 3. Onboarding Plan Generation

**Prompt:**
```
Create personalized onboarding plan for new hire:
- New hire profile:
  * Name: [First Last]
  * Role: [Job title]
  * Department: [Team, manager name]
  * Start date: [Date]
  * Location: [Office, Remote, Hybrid]
  * Prior experience: [Senior, Mid-level, Entry-level]
- Company info:
  * Size: [Number of employees]
  * Tools: [Slack, G Suite, JIRA, Salesforce, etc.]
  * Onboarding standard: [30-60-90 day framework]

Generate 30-60-90 day plan:

**Week 1 (Orientation)**:
- Pre-start: [Send welcome email, ship laptop/equipment, create accounts]
- Day 1: [Welcome meeting, IT setup, office tour, benefits enrollment]
- Week 1 tasks: [Complete HR paperwork, security training, meet team, review company handbook]

**Month 1 (Learning)**:
- Training: [Product overview, system access, role-specific training]
- Meetings: [1-on-1s with manager, peers, cross-functional partners]
- Goals: [Small first project, shadow experienced team member]
- Check-in: [Week 2 and Week 4 manager check-ins]

**Month 2 (Contributing)**:
- Goals: [Own first project end-to-end, present work to team]
- Development: [Identify skill gaps, create learning plan]
- Feedback: [30-day survey: How's onboarding going? What can we improve?]

**Month 3 (Thriving)**:
- Goals: [Full project ownership, contribute to team goals]
- Evaluation: [90-day performance review, adjust goals for next quarter]
- Milestone: [Celebrate successful onboarding, transition to normal workflow]

Assign tasks to:
- IT (provision accounts, equipment)
- Manager (check-ins, project assignments, feedback)
- HR (benefits, compliance training, surveys)
- Buddy/Mentor (answer questions, cultural integration)
```

**Pro Tip:** Onboarding buddy (peer mentor) increases new hire retention 25%; human connection matters.

---

### 4. Employee Retention & Flight Risk Prediction

**Prompt:**
```
Identify employees at risk of leaving:
- Employee profile:
  * Tenure: [Months/years with company]
  * Role: [Title, level]
  * Performance: [Last review rating, trend]
  * Compensation: [Salary percentile vs. market, last raise]
  * Manager: [Manager tenure, team turnover rate]
  * Engagement: [Survey scores, trend over time]
- Churn signals:
  * Engagement declining (survey scores down)
  * Manager change (new manager, relationship reset)
  * Missed promotion (passed over, peer promoted)
  * Compensation lag (below market, no raise in 18+ months)
  * LinkedIn activity (profile updated, connections to recruiters)
  * PTO spike (using all vacation suddenly, interview time off?)
  * Low participation (skipping team events, voluntary projects)

Calculate flight risk score (0-100):
- 0-30: Low risk (engaged, growing, compensated fairly)
- 31-70: Medium risk (watch, proactive check-in)
- 71-100: High risk (likely exploring options, intervene now)

For high-risk employees, recommend retention tactics:
- Compensation adjustment (raise, bonus, equity refresh)
- Career development (promotion, stretch assignment, training)
- Manager coaching (improve relationship, address concerns)
- Flexibility (remote work, schedule adjustment)
- Recognition (public appreciation, awards, responsibility)

Prioritize retention by:
- Impact of loss (high performer, critical skill, culture carrier)
- Feasibility (can we address their concern? or beyond our control?)
```

**⚠️ CRITICAL:** Flight risk scores confidential (HR + manager only); don't create self-fulfilling prophecy ("flagged as flight risk, so I'm leaving").

---

### 5. Performance Review Summarization

**Prompt:**
```
Summarize performance review feedback for employee:
- Employee: [Name, role, tenure]
- Review period: [Past 6/12 months]
- Feedback sources:
  * Manager assessment: [Strengths, areas for improvement, goals met/missed]
  * Peer feedback (360 review): [Collaboration, communication, impact]
  * Self-assessment: [Employee's view of achievements, challenges]
  * Objective data: [Projects delivered, KPIs achieved, customer NPS]

Synthesize feedback into:
1. **Key Strengths** (Top 3-5)
   - Example: "Consistently delivers high-quality work ahead of deadlines"
   - Supporting evidence: [Manager + peer feedback aligned, 5 projects shipped on time]

2. **Areas for Development** (Top 2-3)
   - Example: "Could improve cross-team communication"
   - Supporting evidence: [Peer feedback: 'Sometimes misses us on important updates']
   - Actionable plan: [Attend communication workshop, weekly check-ins with cross-functional partners]

3. **Performance Rating** (Exceeds / Meets / Needs Improvement)
   - Rationale: [Why this rating? Calibrated against peers?]

4. **Goals for Next Period** (3-5 SMART goals)
   - Example: "Lead launch of Product X, achieving 10K users in Q1"

5. **Career Development Discussion**
   - What are employee's aspirations? (IC growth, management, lateral move?)
   - Development plan: [Training, mentorship, stretch assignments]

6. **Compensation & Promotion Recommendation**
   - Raise %: [Market adjustment, merit, equity]
   - Promotion: [If ready, timeline and criteria]
```

**Pro Tip:** Calibration sessions (managers compare ratings across teams) ensure fairness; prevent manager bias (lenient vs. harsh rater).

---

### 6. Compensation Equity Analysis

**Prompt:**
```
Analyze pay equity across organization:
- Employee data:
  * Compensation (base, bonus, equity)
  * Role (title, level, department)
  * Performance (recent review ratings)
  * Tenure (years with company)
  * Location (adjust for cost of living)
  * Demographics (optional self-identification: gender, race, age)
- Market data:
  * Salary benchmarks by role, location, experience (Radford, Mercer, Pave)

Perform equity analysis:
1. **Internal Equity**: Are employees in same role/level paid similarly?
   - Identify outliers (overpaid, underpaid by >10%)
   - Explain variance (performance, tenure, location, or unexplained?)

2. **External Equity**: Are we competitive with market?
   - Compare to market 50th percentile (P50), 75th percentile (P75)
   - Flag roles where we're <10% below market (retention risk)

3. **Pay Gap Analysis** (if demographic data available):
   - Compare compensation by gender, race, age (controlling for role, performance, tenure)
   - Calculate: "Women in Engineering paid X% less than men for same role/performance"
   - Statistical significance: Is gap due to chance, or systemic issue?
   - Recommend adjustments to close unexplained gaps

Generate report:
- Employees to adjust (increase compensation to close gaps)
- Budget required (total cost of equity adjustments)
- Timeline (implement in next compensation cycle)

⚠️ CRITICAL: Document analysis (legal protection if audited by EEOC); close gaps proactively (avoid lawsuits, build trust).
```

**Pro Tip:** Publish salary ranges by role (transparency reduces pay negotiation gaps, builds trust).

---

### 7. Diversity Hiring Pipeline Analysis

**Prompt:**
```
Analyze diversity in hiring funnel:
- Job opening: [Role title]
- Hiring stages:
  1. Applications received
  2. Resume screened (passed AI/recruiter review)
  3. Phone screen
  4. Technical interview
  5. On-site interview
  6. Offer extended
  7. Offer accepted

Track candidates by demographic (if self-identified):
- Gender (Male, Female, Non-binary, Prefer not to say)
- Race/Ethnicity (White, Black/African American, Hispanic/Latino, Asian, Multi-racial, Other)
- Veteran status, Disability status

Calculate conversion rates by stage:
- Example: 100 applicants → 30 screened → 10 phone screens → 5 on-sites → 2 offers → 1 accepted

Identify drop-off:
- Where do underrepresented candidates drop out disproportionately?
  * If women 50% of applicants, but only 20% of hires → investigate bias in interview process
  * If Black candidates 30% of resumes screened, but only 10% of phone screens → resume screening bias?

Recommend interventions:
- Bias in resume screening: Blind resume reviews (remove names, schools)
- Interview bias: Structured interviews (same questions for all), diverse interview panels
- Offer conversion: Understand why candidates decline (competing offers, concerns about culture?)

⚠️ EEOC COMPLIANCE: Document hiring data, analyze for adverse impact (if one group hired at <80% rate of another, investigate).
```

**Pro Tip:** Diversity sourcing (partner with HBCUs, women-in-tech groups, veteran programs) increases pipeline before screening.

---

### 8. Learning & Development Recommendations

**Prompt:**
```
Recommend personalized learning for employee:
- Employee profile:
  * Role: [Current title, level]
  * Skills: [Current competencies from resume, assessments]
  * Career goals: [IC expert, manager, lateral move to different function]
  * Learning style: [Self-paced online, instructor-led, hands-on projects]
  * Time availability: [1 hour/week, immersive bootcamp, on-the-job]
- Company goals:
  * Strategic priorities (we're investing in AI, cloud migration, etc.)
  * Skill gaps (organization lacks X skill, high demand for Y role)

Recommend learning paths:
1. **Skill Development** (close gaps for current role)
   - Example: "Improve data analysis skills: Complete SQL course, Tableau certification"
   - Timeline: [3 months], Resources: [Coursera, Udemy, internal training]

2. **Career Advancement** (prepare for next role)
   - Example: "Preparing for engineering manager role: Leadership training, mentor junior engineers"
   - Timeline: [6 months], Resources: [Manager training program, exec coaching]

3. **Strategic Alignment** (company priority skills)
   - Example: "AI/ML skills (company priority): Deep Learning Specialization, work on AI project"
   - Timeline: [12 months], Resources: [Stanford online, internal AI squad]

Track progress:
- Completion rates (courses started, finished)
- Application (did they use new skill on the job?)
- Impact (promoted? Higher performance rating? Project success?)

Incentivize learning:
- Professional development budget ($1-2K/year per employee)
- Recognition (certificates, LinkedIn endorsements)
- Career impact (learning tied to promotions, raises)
```

**Pro Tip:** Manager check-ins on learning goals (quarterly); employees with development plans 40% more likely to stay.

---

### 9. Exit Interview Analysis & Insights

**Prompt:**
```
Analyze exit interview data to reduce turnover:
- Exit interviews (past 6-12 months):
  * Employee: [Role, tenure, department, manager, performance rating]
  * Resignation reason: [Better pay, career growth, manager conflict, burnout, relocation, personal]
  * Feedback: [What did we do well? What should we improve?]
  * Regrettable loss? (Would we rehire? High performer leaving = problem)

Aggregate insights:
1. **Primary Turnover Drivers** (rank by frequency)
   - Example: 40% cite "lack of career growth," 25% cite "compensation," 20% cite "manager relationship"

2. **Department/Manager Hot Spots**
   - Example: "Engineering turnover 2x company average, concentrated in Team X under Manager Y"
   - Action: Manager coaching, team restructure, investigate culture issues

3. **Tenure Patterns**
   - Example: "50% of departures occur at 18-month mark (outgrow role, no clear next step)"
   - Action: Create career paths, 12-month career conversations

4. **Competitive Intel**
   - Where are people going? (Competitors, startups, different industries?)
   - Why? (Better pay, equity, remote work, cutting-edge tech?)
   - Action: Adjust comp, benefits, tech stack to compete

Generate action plan:
- Short-term fixes (raise comp for underpaid roles, address toxic manager)
- Long-term strategy (career frameworks, manager training, culture investment)

⚠️ CONFIDENTIALITY: Exit feedback anonymized in aggregate reports (individual comments only shared if critical safety/legal issue).
```

**Pro Tip:** Conduct "stay interviews" with current employees (why do you stay? what would make you leave?); proactive retention.

---

### 10. Workforce Planning & Headcount Forecasting

**Prompt:**
```
Forecast hiring needs for next 12 months:
- Business plan:
  * Growth targets (revenue, customers, products)
  * Strategic initiatives (launch new product, expand to new market)
  * Expected attrition (historical: 10-15% annual turnover)
- Current headcount:
  * By department (Engineering, Sales, Marketing, Ops, etc.)
  * By role (breakdown of individual contributors, managers, execs)
  * Open positions (time to fill, offer acceptance rate)
- Productivity assumptions:
  * Revenue per employee (benchmark for efficiency)
  * Team ratios (manager:IC, engineer:PM, sales:sales ops)

Forecast headcount needs:
1. **Backfill for Attrition** (assume 12% turnover)
   - Example: 100 employees × 12% = 12 backfills needed

2. **Growth Hiring** (to hit business goals)
   - Example: Increase sales 50% → need 20 more sales reps (if current team 40 reps)

3. **Strategic Hires** (new capabilities)
   - Example: Launch AI product → hire 5 ML engineers, 1 AI PM

Total hiring plan: [X new hires] across departments

Resource plan:
- Recruiting team capacity (how many recruiters to hire per month?)
- Budget (salaries, recruiting costs, tools)
- Timeline (when to start hiring for Q3 goal? account for 60-day time-to-hire)

Risk mitigation:
- If hiring slower than plan (market tight, losing candidates), what's fallback? (Contractors, outsourcing, scope reduction?)
```

**Pro Tip:** Hiring takes longer than expected; start recruiting 3-6 months before you need role filled (sourcing, interviewing, ramp-up time).

---

## Advanced Techniques

### AI-Powered Candidate Sourcing
**Prompt Pattern:**
```
Find passive candidates for hard-to-fill role:
- Search LinkedIn, GitHub, Kaggle for profiles matching:
  * Skills: [Python, ML, NLP]
  * Experience: [5+ years, worked at top AI companies]
  * Location: [Open to remote, or specific city]
- Generate personalized outreach message highlighting why role fits their background
- Track response rates, optimize messaging
```

### Sentiment Analysis on Employee Surveys
**Prompt Pattern:**
```
Analyze open-ended survey responses:
- Question: "What can we do to improve company culture?"
- 500 text responses

Extract themes:
- Positive sentiment: [Appreciation for flexibility, strong team bonds]
- Negative sentiment: [Lack of career growth, communication gaps]
- Actionable suggestions: ["More transparent exec updates," "Better DEI training"]

Prioritize by frequency and sentiment intensity.
```

### Skills Gap Analysis
**Prompt Pattern:**
```
Compare current workforce skills to future needs:
- Current skills (from resumes, self-assessments, certifications)
- Future needs (strategic plan: AI, cloud, cybersecurity)
- Gap: [Need 20 ML engineers, have 5 → 15 hires or 50 upskilled]

Recommend: Hire vs. Train vs. Partner (contractors, consultants)
```

---

## Metrics to Track

| Metric | Target | Why It Matters |
|--------|--------|----------------|
| **Time to Hire** | <30 days | Speed of talent acquisition (lose candidates if too slow) |
| **Quality of Hire** | 90-day retention >95% | Right candidate-role match |
| **Diversity (Hiring)** | Match labor market demographics | Inclusive workplace, legal compliance |
| **Employee Engagement** | >80% favorable | Retention, productivity, culture |
| **Voluntary Turnover** | <10% annually | Retention (high turnover = cost, disruption) |
| **Internal Mobility** | 20-30% of roles filled internally | Career growth, retention |
| **Pay Equity** | Zero unexplained gaps | Fairness, legal compliance, trust |

---

## Related Resources

- **Full Playbook**: [Human Resources Playbook](../../PLAYBOOKS/playbook-human-resources.md)
- **AI Integration**: [AI Integration Playbook](../../PLAYBOOKS/playbook-ai-integration.md)
- **Data Contracts**: [Example: Employee Lifecycle Event](../../PLAYBOOKS/playbook-human-resources.md#data-contracts)
- **Ethical AI**: [Algorithmic Fairness, Privacy, Transparency](../../PLAYBOOKS/playbook-human-resources.md#ethical-hr)

---

## Tips for Success

1. **Bias Testing**: Quarterly adverse impact analysis (hiring, promotions, comp by demographics); document for EEOC compliance
2. **Human-in-the-Loop**: AI assists, humans decide (hiring, performance, terminations); legal requirement, ethical imperative
3. **Transparency**: Tell candidates/employees how AI used (resume screening, interview analysis, flight risk); build trust
4. **Privacy**: Employee data highly confidential (GDPR, state laws); strict access controls, encryption, consent
5. **Explainability**: Provide reasons for AI decisions (rejected resume, denied promotion); candidates/employees deserve explanations
6. **Continuous Improvement**: Gather feedback (was AI-screened candidate good? was retention prediction accurate?); retrain models
7. **Employee Agency**: Employees can challenge AI decisions (appeals process, human review); not powerless against algorithm

---

## Ethical & Legal Considerations

⚠️ **ANTI-DISCRIMINATION**:
- Never use race, gender, age, religion, disability, national origin as factors (illegal under Title VII, ADA, ADEA)
- Avoid proxy variables (ZIP code → race, name → ethnicity, school → socioeconomic status)
- Test for disparate impact (EEOC 4/5ths rule: protected group hired at ≥80% rate of majority group)

⚠️ **PRIVACY & CONSENT**:
- Minimize data collection (only what's needed for HR decisions)
- Inform employees how AI used (handbook, onboarding, job postings)
- Secure data (encryption, access controls, GDPR/CCPA compliance)
- Consent for recording interviews, monitoring (legal requirement in some jurisdictions)

⚠️ **TRANSPARENCY & FAIRNESS**:
- Explain AI decisions (rejected candidate, compensation determination)
- Human review for high-stakes decisions (hire, fire, promote, compensate)
- Appeals process (employees can challenge AI outcomes)
- Regular audits (bias testing, accuracy validation, ethical review)

---

**Questions?** Join the SOLID.AI community or open an issue on [GitHub](https://github.com/gusafr/midora-solid-ai/issues)!

⚠️ **CRITICAL REMINDER**: Consult employment attorneys and compliance experts before deploying AI in HR. Laws vary by country, state, and evolve rapidly.

---

**Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI
