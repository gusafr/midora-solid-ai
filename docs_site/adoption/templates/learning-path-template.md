# Learning Path Template

**Purpose:** Copy-paste YAML template for designing 4-level AI learning & development paths by function.

---

## How to Use This Template

1. **Copy the YAML below** into your L&D planning documentation
2. **Customize for your function** (Sales, Engineering, Finance, Marketing, CS, HR, etc.)
3. **Define modules per level** (Level 1: Awareness → Level 4: Specialist)
4. **Set target completion rates** (Level 1: 100%, Level 2: 60-80%, etc.)
5. **Plan rollout strategy** (Pilot → Company-wide → Function-specific)
6. **Track metrics** (adoption, effectiveness, quality, business impact)

---

## Template Contents

This template includes:
- ✅ **4-Level Learning Structure** - From Awareness (4h) to Specialist (100h+)
- ✅ **Target Completion Rates** - Realistic goals per level (100% → 5-10%)
- ✅ **Module Breakdown** - Topics, duration, delivery format, prerequisites
- ✅ **Rollout Plan** - Phased approach (Pilot → Scale)
- ✅ **Metrics Framework** - Adoption, effectiveness, quality, business impact
- ✅ **Complete Example** - Sales function learning path

---

## Download Template

**File:** [`learning-path-template.yaml`](learning-path-template.yaml)

---

## Template Preview

```yaml
---
# AI LEARNING & DEVELOPMENT: LEARNING PATH TEMPLATE
# Purpose: Design 4-level certification program for AI literacy
# Framework: SOLID.AI
# Version: 1.0
# Last Updated: November 2025

# ========================================
# LEARNING PATH OVERVIEW
# ========================================
learning_path:
  function: "[Sales | Engineering | Finance | Marketing | CS | HR | Operations | Executive]"
  owner: "[L&D Lead or Function Head]"
  last_updated: "YYYY-MM-DD"
  version: "1.0"

# ========================================
# LEVEL 1: AI AWARENESS (Universal, All Employees)
# ========================================
level_1_awareness:
  description: "Foundation AI literacy for all employees"
  target_audience: "100% of employees"
  duration: "4 hours (2h self-paced + 2h workshop)"
  delivery_format: "Self-paced online + live workshop"
  prerequisites: "None"
  
  modules:
    - module_1:
        title: "What is AI? (And What It's Not)"
        topics:
          - "AI vs. automation vs. rules-based systems"
          - "How LLMs work (simplified)"
          - "What AI can/cannot do (realistic expectations)"
        duration: "30 minutes"
        format: "Video + quiz"
        
    - module_2:
        title: "Prompt Engineering Basics"
        topics:
          - "6 principles: Role, Context, Task, Format, Tone, Examples"
          - "Chain-of-thought prompting"
          - "Iterative refinement"
        duration: "1 hour"
        format: "Interactive tutorial + hands-on practice"
        
    - module_3:
        title: "AI Ethics & Governance"
        topics:
          - "Bias and fairness"
          - "Data privacy (what NOT to share with AI)"
          - "When to escalate (high-risk decisions)"
        duration: "30 minutes"
        format: "Case studies + discussion"
        
    - module_4:
        title: "AI Tools for Your Role"
        topics:
          - "Approved AI tools (ChatGPT, Copilot, [internal tools])"
          - "How to access and use them"
          - "Your first AI prompt (live demo)"
        duration: "2 hours"
        format: "Live workshop + hands-on practice"
        
  assessment:
    type: "Quiz (10 questions, 70% pass)"
    retake_allowed: true
    
  certification:
    title: "AI Awareness Certified"
    badge: "Level 1 - AI Aware"
    incentive: "Required for Level 2 enrollment"

# ========================================
# LEVEL 2: AI PRACTITIONER (Function-Specific, 60-80% of Function)
# ========================================
level_2_practitioner:
  description: "Apply AI daily in your function"
  target_audience: "60-80% of [Function] employees"
  duration: "20 hours (10h self-paced + 10h applied project)"
  delivery_format: "Self-paced + cohort-based + project"
  prerequisites: "Level 1 Awareness Certified"
  
  modules:
    # Customize these modules for each function (Sales, Engineering, Finance, etc.)
    - module_1:
        title: "[Function]-Specific AI Use Cases"
        topics:
          - "[Use Case 1: e.g., Sales - Lead qualification with AI]"
          - "[Use Case 2: e.g., Sales - Personalized outreach at scale]"
          - "[Use Case 3: e.g., Sales - Forecasting with AI insights]"
        duration: "2 hours"
        format: "Video + real examples from your team"
        
    - module_2:
        title: "Advanced Prompt Engineering for [Function]"
        topics:
          - "[Function]-specific prompt templates"
          - "Multi-step workflows (e.g., research → draft → refine)"
          - "Error handling and validation"
        duration: "3 hours"
        format: "Interactive exercises + prompt library"
        
    - module_3:
        title: "AI-Powered Workflows"
        topics:
          - "Integrating AI into your daily routine"
          - "Automation with AI (e.g., Zapier + ChatGPT)"
          - "Measuring productivity gains"
        duration: "2 hours"
        format: "Workflow mapping + implementation guide"
        
    - module_4:
        title: "Data Literacy for AI"
        topics:
          - "Understanding Data Spine (where your data lives)"
          - "Data contracts (what data AI can access)"
          - "Quality inputs = quality outputs"
        duration: "2 hours"
        format: "Data architecture overview + hands-on query"
        
    - module_5:
        title: "Capstone Project: Implement AI in Your Role"
        topics:
          - "Identify 1 process to AI-augment"
          - "Build AI workflow (with mentor support)"
          - "Measure impact (time saved, quality improved)"
        duration: "10 hours"
        format: "Self-directed + weekly cohort check-ins"
        
  assessment:
    type: "Project submission + peer review"
    criteria:
      - "Clear problem statement"
      - "AI solution implemented"
      - "Measured impact (quantitative)"
      - "Reflection on learnings"
    pass_threshold: "3/4 criteria met"
    
  certification:
    title: "AI Practitioner ([Function])"
    badge: "Level 2 - AI Practitioner"
    incentive: "$2,000 bonus + title upgrade (e.g., 'Senior Sales Rep, AI-Augmented')"

# ========================================
# LEVEL 3: AI POWER USER (Advanced, 20-30% of Function)
# ========================================
level_3_power_user:
  description: "Build custom AI solutions, train others"
  target_audience: "20-30% of [Function] (top performers)"
  duration: "40 hours (20h learning + 20h project)"
  delivery_format: "Self-paced + mentorship + major project"
  prerequisites: "Level 2 Practitioner Certified + Manager nomination"
  
  modules:
    - module_1:
        title: "AI Strategy for [Function]"
        topics:
          - "Identifying high-impact AI opportunities"
          - "ROI analysis (cost/benefit of AI initiatives)"
          - "Change management (getting team buy-in)"
        duration: "4 hours"
        format: "Case studies + strategy workshop"
        
    - module_2:
        title: "Building Custom AI Agents"
        topics:
          - "No-code AI agent builders (e.g., Bubble, Retool + OpenAI API)"
          - "Agent design patterns (e.g., research assistant, content generator)"
          - "Testing and iteration"
        duration: "8 hours"
        format: "Hands-on labs + real agent builds"
        
    - module_3:
        title: "AI-Powered Integration & APIs"
        topics:
          - "Connecting AI to internal systems (CRM, ERP, Data Spine)"
          - "Event-driven AI (triggers, webhooks)"
          - "Error handling and monitoring"
        duration: "6 hours"
        format: "Technical workshop + sandbox environment"
        
    - module_4:
        title: "Training Others on AI"
        topics:
          - "Facilitation skills (how to teach AI effectively)"
          - "Creating learning materials (prompts, templates)"
          - "Mentoring Level 2 practitioners"
        duration: "2 hours"
        format: "Train-the-trainer session"
        
    - module_5:
        title: "Capstone: Build + Deploy a Custom AI Solution"
        topics:
          - "Solve a team/function-wide problem with AI"
          - "Deploy solution (min 10 users)"
          - "Train team on usage"
          - "Measure impact (productivity, quality, cost savings)"
        duration: "20 hours"
        format: "Self-directed + mentor support + demo day"
        
  assessment:
    type: "Major project + demo + peer feedback"
    criteria:
      - "Novel AI solution (not copy-paste)"
      - "Deployed to production (min 10 users)"
      - "Quantified impact (>20% efficiency gain)"
      - "Documented and transferable"
    pass_threshold: "4/4 criteria met"
    
  certification:
    title: "AI Power User ([Function])"
    badge: "Level 3 - AI Power User"
    incentive: "$5,000 bonus + title upgrade (e.g., '[Function] AI Lead') + conference budget"

# ========================================
# LEVEL 4: AI SPECIALIST (Expert, 5-10% of Function)
# ========================================
level_4_specialist:
  description: "AI expertise, innovation, and thought leadership"
  target_audience: "5-10% of [Function] (AI champions)"
  duration: "100+ hours (50h learning + 50h research/innovation)"
  delivery_format: "Advanced courses + research project + mentorship"
  prerequisites: "Level 3 Power User + 2+ custom AI solutions deployed"
  
  modules:
    - module_1:
        title: "Advanced AI & MLOps"
        topics:
          - "Fine-tuning models (when and how)"
          - "Monitoring AI in production (performance, drift)"
          - "A/B testing AI solutions"
        duration: "16 hours"
        format: "Advanced technical course + lab"
        
    - module_2:
        title: "AI Governance & Ethics (Deep Dive)"
        topics:
          - "Risk scoring frameworks (Impact × Likelihood × Autonomy)"
          - "Bias detection and mitigation"
          - "Regulatory compliance (GDPR, HIPAA, etc.)"
        duration: "8 hours"
        format: "Case studies + policy design workshop"
        
    - module_3:
        title: "AI Research & Innovation"
        topics:
          - "Staying current (papers, conferences, community)"
          - "Experimenting with cutting-edge AI (GPT-5, multimodal, agents)"
          - "Prototyping new use cases"
        duration: "16 hours"
        format: "Research sprint + innovation lab"
        
    - module_4:
        title: "Thought Leadership & Community"
        topics:
          - "Publishing AI learnings (internal/external)"
          - "Speaking at conferences/meetups"
          - "Building the AI Guild (community of practice)"
        duration: "10 hours"
        format: "Content creation + speaking practice"
        
  assessment:
    type: "Research project + public presentation"
    criteria:
      - "Novel AI research or innovation"
      - "Significant business impact (>$100K value)"
      - "Knowledge shared (blog, talk, training)"
      - "Mentored 3+ Level 2/3 learners"
    pass_threshold: "3/4 criteria met"
    
  certification:
    title: "AI Specialist ([Function])"
    badge: "Level 4 - AI Specialist"
    incentive: "$10,000 bonus + title upgrade (e.g., 'Principal [Function] Engineer - AI') + conference speaking + R&D time"

# ========================================
# ROLLOUT PLAN
# ========================================
rollout:
  phase_1_pilot:
    description: "Test with 20-30 volunteers (mix of Level 1 & 2)"
    duration: "8 weeks"
    goals:
      - "Validate content quality"
      - "Test delivery formats (self-paced vs. live)"
      - "Gather feedback (surveys, NPS)"
    success_criteria:
      - "90%+ completion rate"
      - "4.0+ satisfaction score (out of 5)"
      - "Measurable productivity gains (survey self-report)"
      
  phase_2_level_1_all:
    description: "Roll out Level 1 Awareness to all employees"
    duration: "12 weeks"
    delivery:
      - "Self-paced online (weeks 1-8)"
      - "Live workshops (weeks 9-12, 50 people per session)"
    goals:
      - "100% of employees complete Level 1"
      - "AI tools enabled for all (ChatGPT, Copilot, etc.)"
    success_criteria:
      - "95%+ completion within 12 weeks"
      - "80%+ quiz pass rate (first attempt)"
      
  phase_3_level_2_function:
    description: "Roll out Level 2 Practitioner by function (start with high-ROI functions)"
    duration: "24 weeks (6 months)"
    priority_order:
      - "Function 1: Sales (highest ROI, customer-facing)"
      - "Function 2: Engineering (tech-savvy, fast adopters)"
      - "Function 3: Finance (process automation, measurable gains)"
      - "Function 4: Marketing (content generation, high demand)"
      - "Function 5: Customer Success (efficiency gains)"
      - "Function 6: HR (admin automation)"
    delivery:
      - "Cohorts of 20-30 per function"
      - "Monthly cohort starts (continuous enrollment)"
    goals:
      - "60-80% of each function completes Level 2"
      - "Each function has 3+ custom AI solutions deployed"
    success_criteria:
      - "70%+ completion within 6 months"
      - "Avg 25% productivity gain (measured via OKRs)"
      
  phase_4_level_3_ongoing:
    description: "Continuous Level 3 Power User track (by nomination)"
    duration: "Ongoing (quarterly cohorts)"
    delivery:
      - "Quarterly cohorts (10-15 people)"
      - "Manager nominations + self-nominations"
    goals:
      - "20-30% of each function achieves Level 3 by Year 2"
      - "Each function has AI Power Users leading initiatives"
    success_criteria:
      - "80%+ completion (highly motivated learners)"
      - "Each graduate deploys 1+ production AI solution"
      
  phase_5_level_4_specialist:
    description: "Level 4 Specialist track (invitation-only, top 5-10%)"
    duration: "Ongoing (annual cohorts)"
    delivery:
      - "Annual cohort (5-10 people across all functions)"
      - "Invitation-only (based on Level 3 performance + innovation)"
    goals:
      - "5-10% of company achieves Level 4 by Year 3"
      - "AI Specialists drive innovation, research, governance"
    success_criteria:
      - "100%+ completion (elite learners)"
      - "Each graduate publishes 1+ thought leadership piece"

# ========================================
# METRICS & SUCCESS TRACKING
# ========================================
metrics:
  # Metric 1: Adoption (How many people are learning?)
  adoption:
    - metric: "Level 1 completion rate"
      target: "95% within 12 weeks"
      measurement: "LMS dashboard"
      
    - metric: "Level 2 enrollment rate"
      target: "70% of employees enroll within 6 months"
      measurement: "LMS + manager reports"
      
    - metric: "Level 3 completion rate"
      target: "20-30% of each function by Year 2"
      measurement: "LMS + certification records"
      
  # Metric 2: Effectiveness (Are people actually using AI?)
  effectiveness:
    - metric: "AI tool usage (active users)"
      target: "80% of employees use AI weekly"
      measurement: "Tool analytics (ChatGPT, Copilot, etc.)"
      
    - metric: "Prompts per user per week"
      target: "10+ prompts/week (Level 2+)"
      measurement: "Tool analytics"
      
    - metric: "Custom AI solutions deployed"
      target: "10+ solutions per function by Year 1"
      measurement: "Project tracker + demos"
      
  # Metric 3: Quality (Is AI being used well?)
  quality:
    - metric: "Learner satisfaction (NPS)"
      target: "50+ NPS"
      measurement: "Post-training survey"
      
    - metric: "Manager satisfaction (AI impact on team)"
      target: "80% of managers report positive impact"
      measurement: "Quarterly manager survey"
      
    - metric: "Governance incidents (AI misuse)"
      target: "<5 incidents per quarter"
      measurement: "Governance Circle reports"
      
  # Metric 4: Business Impact (Is AI delivering value?)
  business_impact:
    - metric: "Productivity gain (self-reported)"
      target: "25% time savings (Level 2+)"
      measurement: "Monthly survey (time saved, tasks automated)"
      
    - metric: "Revenue per employee"
      target: "+20% YoY (company-wide)"
      measurement: "Finance reports"
      
    - metric: "Employee engagement (AI satisfaction)"
      target: "80%+ employees feel AI makes work better"
      measurement: "Annual engagement survey"

# ========================================
# EXAMPLE: SALES FUNCTION LEARNING PATH
# ========================================
# Below is a complete example for the Sales function

example_sales:
  learning_path:
    function: "Sales"
    owner: "VP of Sales + L&D Lead"
    last_updated: "2025-11-01"
    version: "1.0"
    
  level_2_practitioner:
    description: "AI-powered sales workflows"
    target_audience: "70% of Sales team (all AEs, SDRs)"
    duration: "20 hours"
    
    modules:
      - module_1:
          title: "AI for Lead Qualification & Research"
          topics:
            - "Use ChatGPT to research companies (tech stack, pain points)"
            - "AI-powered lead scoring (predict likelihood to buy)"
            - "Personalized outreach at scale (1:1 emails, not templates)"
          duration: "2 hours"
          
      - module_2:
          title: "AI-Assisted Sales Calls"
          topics:
            - "Real-time call transcription (Gong, Chorus)"
            - "AI-generated follow-up emails (summarize call, next steps)"
            - "Objection handling (AI suggests responses)"
          duration: "3 hours"
          
      - module_3:
          title: "AI-Powered Forecasting"
          topics:
            - "Data Spine: Where sales data lives (CRM, calls, emails)"
            - "AI forecasting models (predict close rate, deal size)"
            - "Identifying at-risk deals (AI flags red flags)"
          duration: "2 hours"
          
      - module_4:
          title: "Data Contracts for Sales"
          topics:
            - "What data AI can access (CRM fields, call transcripts)"
            - "Data quality (clean data = better AI)"
            - "Privacy (what NOT to share with AI)"
          duration: "2 hours"
          
      - module_5:
          title: "Capstone: Automate Your Sales Workflow"
          topics:
            - "Choose 1 manual task to automate (e.g., prospect research)"
            - "Build AI workflow (prompts + tools)"
            - "Measure impact (time saved, deals closed faster)"
          duration: "10 hours"
          
    assessment:
      type: "Project: Automate 1 sales task + demo to team"
      criteria:
        - "Clear before/after comparison"
        - "Time savings >20%"
        - "Replicable by other AEs"
        
    certification:
      title: "AI Practitioner (Sales)"
      incentive: "$2K bonus + 'AI-Augmented AE' title"

---

# Related Resources

**Playbooks:**
- [AI Learning & Development](../../playbooks/people-culture/ai-learning-development.md)

**Checklists:**
- [Learning & Development Rollout](../checklists/learning-development-rollout.md)

**Diagrams:**
- [Learning Path Structure](../../diagrams.md#learning-path-structure) - 4-level certification ladder

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Framework:** SOLID.AI  
**License:** MIT
```

---

## Next Steps

1. **Download the template** (YAML file above)
2. **Customize for your function** (Sales, Engineering, Finance, etc.)
3. **Define modules and projects** for each level
4. **Set rollout timeline** (pilot → scale)
5. **Track metrics** and iterate

For detailed guidance, see the [AI Learning & Development Playbook](../../playbooks/people-culture/ai-learning-development.md).
