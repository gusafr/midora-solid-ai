# Impact Analysis Template

**Initiative Name:** _______________________________

**Proposed by:** _______________  
**Date:** _______________  
**Stakeholders:** _______________  

---

## 1. Initiative Description

### Problem Statement
[What problem are we solving? Why now?]

### Proposed Solution
[High-level approach — what will we build/change?]

### Business Value

- [ ] **Revenue impact:** $ _______________ (increase/protect)
- [ ] **Cost savings:** $ _______________ (reduced manual work, infrastructure)
- [ ] **Customer satisfaction:** _______________ (CSAT improvement, NPS)
- [ ] **Risk mitigation:** _______________ (security, compliance, reliability)

---

## 2. Technical Impact Assessment

| Criteria | Score (PP/P/M/G/GG) | Rationale |
|----------|---------------------|-----------|
| **Services Affected** | ___ | [List services] |
| **Code Complexity** | ___ | [Single module? Refactor? Rewrite?] |
| **Data Model Changes** | ___ | [Schema migration? Breaking changes?] |
| **API Changes** | ___ | [New endpoints? Breaking changes?] |
| **Performance Impact** | ___ | [Caching? Scaling? Optimization?] |

**Technical Complexity:** ___ (highest score above)

### Key Technical Risks
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

## 3. Organizational Impact Assessment

| Criteria | Score (PP/P/M/G/GG) | Rationale |
|----------|---------------------|-----------|
| **Teams Involved** | ___ | [List teams] |
| **Cross-Functional Coordination** | ___ | [How many functions?] |
| **Skills Gap** | ___ | [New skills needed? Training? Hiring?] |
| **Change Management** | ___ | [User impact? Communication plan?] |
| **Stakeholder Alignment** | ___ | [How many decision-makers?] |

**Organizational Complexity:** ___ (highest score above)

### Key Organizational Risks
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

## 4. Operational Impact Assessment

| Criteria | Score (PP/P/M/G/GG) | Rationale |
|----------|---------------------|-----------|
| **Deployment Complexity** | ___ | [CI/CD? Blue-green? Canary?] |
| **Downtime Required** | ___ | [Zero downtime? Maintenance window?] |
| **Rollback Plan** | ___ | [Instant? Hours? Days? Irreversible?] |
| **Monitoring & Alerting** | ___ | [Existing metrics? New dashboards?] |
| **Security/Compliance** | ___ | [Review required? Audit?] |

**Operational Complexity:** ___ (highest score above)

### Key Operational Risks
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

## 5. Architectural Impact Assessment

| Criteria | Score (PP/P/M/G/GG) | Rationale |
|----------|---------------------|-----------|
| **Architectural Pattern** | ___ | [Fits existing? New pattern?] |
| **Technical Debt** | ___ | [Introduces debt? Removes debt?] |
| **Scalability** | ___ | [Horizontal scaling? New infrastructure?] |
| **Integration Complexity** | ___ | [Internal? External? How many?] |
| **Long-Term Maintainability** | ___ | [Standard stack? Specialized?] |

**Architectural Complexity:** ___ (highest score above)

### Key Architectural Risks
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

## 6. Overall T-Shirt Size

### Dimension Scores

| Dimension | Score |
|-----------|-------|
| Technical | ___ |
| Organizational | ___ |
| Operational | ___ |
| Architectural | ___ |

**Overall T-Shirt Size:** ___ (maximum score across all dimensions)

### Escalation Rule Applied?
- [ ] Yes — 2+ dimensions are G/GG, escalate by 1 level
- [ ] No — use maximum score as-is

**Final T-Shirt Size:** ___

---

## 7. Resource Estimate

### Effort

| Role | Estimated Days | Justification |
|------|----------------|---------------|
| Backend Engineer | ___ days | [Work involved] |
| Frontend Engineer | ___ days | [Work involved] |
| DevOps Engineer | ___ days | [Work involved] |
| QA Engineer | ___ days | [Work involved] |
| Product Manager | ___ days | [Work involved] |
| Designer | ___ days | [Work involved] |
| Data Engineer | ___ days | [Work involved] |
| **Total** | **___ days** | **___ person-months** |

### Timeline

- **Estimated duration:** ___ weeks/months
- **Dependencies:** _______________ (blocked by? blocks?)
- **Milestones:**
  1. _______________ (date: _______)
  2. _______________ (date: _______)
  3. _______________ (date: _______)

---

## 8. Risk Assessment

**Risk Level:** ___ (Low / Medium / High / Very High)

| Risk | Likelihood (1-5) | Impact (1-5) | Score | Mitigation |
|------|------------------|--------------|-------|------------|
| [Risk 1] | ___ | ___ | ___ | [How to mitigate?] |
| [Risk 2] | ___ | ___ | ___ | [How to mitigate?] |
| [Risk 3] | ___ | ___ | ___ | [How to mitigate?] |

**Risk Score Calculation:** Likelihood × Impact (1-25 scale)
- **1-5:** Low risk
- **6-12:** Medium risk
- **13-20:** High risk
- **21-25:** Very high risk

---

## 9. Dependencies & Blockers

### Internal Dependencies

| Dependency | Team | Status | ETA | Blocker? |
|------------|------|--------|-----|----------|
| [Dependency 1] | ___ | Not Started / In Progress / Done | _____ | Yes / No |
| [Dependency 2] | ___ | Not Started / In Progress / Done | _____ | Yes / No |

### External Dependencies

| Dependency | Vendor/Team | Status | ETA | Blocker? |
|------------|-------------|--------|-----|----------|
| [External API] | ___ | Not Started / In Progress / Done | _____ | Yes / No |
| [3rd Party Tool] | ___ | Not Started / In Progress / Done | _____ | Yes / No |

---

## 10. Go/No-Go Recommendation

**Recommendation:** ___ (Go / No-Go / Defer)

### Rationale

- **Business Value:** _______________ (High / Medium / Low)
- **Complexity:** _______________ (T-shirt size: PP/P/M/G/GG)
- **Risk:** _______________ (Low / Medium / High / Very High)
- **Resource Availability:** _______________ (Team has capacity? Need to hire?)
- **Strategic Alignment:** _______________ (Aligns with roadmap? Ad-hoc request?)

### Decision Matrix

| Business Value | Complexity | Risk | Recommendation |
|----------------|------------|------|----------------|
| High | PP/P/M | Low/Medium | **Go** — prioritize high |
| High | G/GG | Medium/High | **Go** — allocate resources, plan carefully |
| Medium | PP/P | Low | **Go** — quick win |
| Medium | M/G | Medium | **Go (conditional)** — if capacity available |
| Medium | GG | High | **Defer** — wait for more capacity |
| Low | PP/P | Low | **Defer** — backlog for future |
| Low | M/G/GG | Any | **No-Go** — not worth investment |

**Final Recommendation:** _______________

### Conditions (if conditional go)
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

## 11. Approval & Sign-Off

### Reviewed by

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | _______________ | _______________ | _____ |
| Tech Lead | _______________ | _______________ | _____ |
| Architect | _______________ | _______________ | _____ |
| Engineering Manager | _______________ | _______________ | _____ |

**Approval Status:** ___ (Approved / Rejected / Needs Revision)

### Next Steps

- [ ] Add to roadmap (if approved)
- [ ] Create epic/feature in Jira/Linear
- [ ] Break down into stories
- [ ] Assign to squad
- [ ] Schedule kickoff meeting

---

## T-Shirt Sizing Quick Reference

| Size | Effort | Duration | Complexity | Examples |
|------|--------|----------|------------|----------|
| **PP** | 1-3 days | <1 week | Trivial | Config change, flag toggle |
| **P** | 3-10 days | 1-2 weeks | Low | Bug fix, UI tweak, add field |
| **M** | 10-30 days | 1-2 months | Medium | New feature (single service), API endpoint |
| **G** | 30-90 days | 2-4 months | High | Multi-service feature, data migration |
| **GG** | 90+ days | 4+ months | Very High | Platform rewrite, system migration |

---

**Template Version:** 1.0 | **Last Updated:** November 2025 | **Framework:** SOLID.AI

**See Also:**
- [Impact Analysis Playbook](../../PLAYBOOKS/governance/impact-analysis.md) — Complete guide with examples
- [RFC Template](rfc-template.md) — For G/GG initiatives requiring architecture review
