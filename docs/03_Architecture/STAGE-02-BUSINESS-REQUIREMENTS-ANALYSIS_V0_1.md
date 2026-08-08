# Stage 02 — Business Requirements & Business Analysis v0.1

Status: DRAFT
Owner: FATHER Architecture Governance

## 1. Purpose

Transform an approved project opportunity into a measurable, traceable and economically justified business baseline before system design begins.

The stage must answer: what business problem is being solved, for whom, why now, what value is expected, what is in/out of scope, what constraints apply, who owns decisions, how success will be measured, and what uncertainty remains.

## 2. Entry criteria

- Stage 01 Presale / Project Intake completed.
- GO or NEED DISCOVERY decision recorded.
- Initial scope, risks and ROM estimate available.
- Business sponsor / decision owner identified or explicitly marked UNKNOWN.

## 3. Mandatory artifacts

| ID | Artifact | Purpose | Primary owner |
|---|---|---|---|
| BA-001 | Business Requirements Document / PRD baseline | Defines business need and target result | Business Analyst / Product |
| BA-002 | Stakeholder & Decision Rights Map | Identifies stakeholders, owners and approval rights | BA / PM |
| BA-003 | AS-IS Model | Establishes current process and baseline | BA |
| BA-004 | TO-BE Model | Describes desired operating model | BA + Product |
| BA-005 | Business Rules Register | Captures rules that constrain behavior | BA + Domain Expert |
| BA-006 | Scope & Boundary Baseline | Defines IN / OUT / assumptions | BA + PM |
| BA-007 | Business Value & KPI Model | Defines measurable expected value | Product + Economist |
| BA-008 | Constraints & Dependencies Register | Captures external/internal dependencies | BA + Architect |
| BA-009 | Data & Information Needs | Defines required business information and sensitivity candidates | BA + Data/Security |
| BA-010 | Acceptance & Success Criteria | Defines measurable business acceptance | Product + BA + QA |
| BA-011 | Requirements Traceability Seed | Links Goal → Problem → Requirement → KPI | BA |
| BA-012 | Analysis Decision Record | Records approval / rejection / unresolved issues | Responsible decision owner |

Optional artifacts are allowed only when their value is explicit: customer journey, BPMN, service blueprint, domain glossary, prototypes, research report, market analysis, regulatory mapping, data-flow sketch.

## 4. Work Breakdown Structure and resource model

Every work package SHALL have O/M/P estimates, PERT expected effort, role, competency requirement, rate placeholder, direct cost, non-labor cost, risk reserve, dependencies and confidence.

PERT expected effort: E = (O + 4M + P) / 6.

| WP | Work package | Typical roles | Cost status initially |
|---|---|---|---|
| WP-02.01 | Stakeholder discovery | BA, PM | NOT_ESTIMATED |
| WP-02.02 | Problem and goal validation | BA, Product, Sponsor | NOT_ESTIMATED |
| WP-02.03 | AS-IS analysis | BA, Domain Expert | NOT_ESTIMATED |
| WP-02.04 | TO-BE design | BA, Product, Architect | NOT_ESTIMATED |
| WP-02.05 | Rules and constraints | BA, Legal, Security, Domain Expert | NOT_ESTIMATED |
| WP-02.06 | Value/KPI economics | Economist, Product, BA | NOT_ESTIMATED |
| WP-02.07 | Data needs and classification screening | BA, Data, Security | NOT_ESTIMATED |
| WP-02.08 | Acceptance criteria | BA, QA, Product | NOT_ESTIMATED |
| WP-02.09 | Traceability and baseline review | BA, PM, Architect | NOT_ESTIMATED |
| WP-02.10 | Gate review and approval | Quality, Security, Legal, Economics, Technology | NOT_ESTIMATED |

Unknown monetary values SHALL be represented as amount=0 with status=NOT_ESTIMATED, never as FREE.

## 5. Roles and competencies

Minimum role model:

- Business Sponsor — owns business outcome and funding decision.
- Product Owner / Product Manager — owns product value and priority.
- Business Analyst — owns analysis quality and business requirements baseline.
- Project Manager — owns coordination, dependencies, estimate baseline and change process.
- Solution/System Architect — checks feasibility and future architectural implications without prematurely designing the solution.
- Security specialist — identifies security/privacy obligations and unacceptable assumptions early.
- Legal/Compliance specialist — identifies jurisdiction, contractual and regulatory constraints.
- Economist/Financial analyst — validates value, cost-of-delay, expected benefits and economic assumptions.
- QA/Test representative — ensures success and acceptance criteria are testable.
- Domain Expert — validates business semantics and rules.

Each assignment records role, person/agent, competency level, required competency, gap, supervision requirement and actual performance after completion.

## 6. Cross-cutting gates

### Quality Gate
Checks completeness, consistency, testability, ambiguity, stakeholder approval, traceability and explicit unknowns.

### Security Gate
Checks data sensitivity candidates, misuse/abuse scenarios, access assumptions, critical business assets, confidentiality/integrity/availability needs and mandatory security requirements discovered at business level.

### Legal / Compliance Gate
Checks jurisdiction, personal/confidential data, contractual restrictions, sector requirements, retention/localization issues and mandatory human decisions.

### Economic Gate
Checks expected business value, cost categories, cost of delay, opportunity cost, benefit assumptions, budget boundary and whether further analysis is economically justified.

### Technology Strategy Gate
Checks whether requirements accidentally prescribe technology, identifies existing reusable solutions, buy/build/integrate candidates and technology constraints that genuinely come from business needs.

No gate may silently PASS missing evidence. Statuses: PASS, FAIL, CONDITIONAL, WAIVER, NOT_APPLICABLE with justification.

## 7. Metrics

### Outcome metrics
- Business requirements accepted without major re-baseline after architecture.
- Percentage of business goals linked to measurable KPIs.
- Percentage of requirements linked to a business problem/goal.
- Late-discovered business requirements.
- Business-value realization after release.

### Process metrics
- Lead time of Stage 02.
- Person-hours by role.
- PERT estimate vs actual effort.
- Planned vs actual stage cost.
- Number and age of unresolved questions.
- Stakeholder response/wait time.
- Number of analysis iterations.

### Quality metrics
- Ambiguity findings per requirement.
- Duplicate/conflicting requirements.
- Requirements rejected/reworked downstream.
- Acceptance criteria coverage.
- Traceability coverage.
- Defects attributable to requirements.

### Competency metrics
- Estimate accuracy by role/competency level.
- Rework by role/competency level.
- Review findings by competency domain.
- Human vs AI-assisted effort.
- Reusable pattern/template utilization.
- Competency gaps causing delay or defects.

### Economic metrics
- Cost of Stage 02.
- Expected value of the proposed outcome.
- Cost of Delay.
- Expected loss from unresolved assumptions.
- Value of Information for additional discovery.
- Cost avoided by detecting infeasible/low-value requirements before design/code.

## 8. Plan / Baseline / Actual

For effort, schedule, cost and major KPI assumptions store:

Estimate → Approved Baseline → Actual → Variance → Cause → Corrective Action → Lesson.

Variance reasons use controlled categories where possible: scope change, client dependency, estimation error, competency gap, technology uncertainty, legal/security discovery, external dependency, defect/rework, deliberate investment, other.

## 9. Change management

After baseline approval, material changes require a Change Request containing:

- changed requirement and reason;
- requester and decision owner;
- impacted goals/KPIs;
- architecture impact candidate;
- security/legal impact;
- effort and schedule impact;
- economic impact including Cost of Delay/opportunity cost;
- test/acceptance impact;
- decision and evidence.

## 10. Exit criteria

Stage 02 may complete only when:

- business problem and target outcome are explicit;
- stakeholders and decision rights are known or risks accepted;
- AS-IS/TO-BE are sufficient for the project class;
- scope IN/OUT and assumptions are baselined;
- requirements have owners and traceability;
- success criteria are measurable/testable;
- material security/legal/economic constraints are identified;
- WBS/resource/PERT estimate exists at appropriate confidence;
- unknown costs are present as NOT_ESTIMATED placeholders;
- unresolved items have owners and due dates;
- required gates are PASS/CONDITIONAL or formally waived;
- decision owner approves transition to System Analysis.

## 11. Learning loop

After later stages and after production outcome, Stage 02 metrics are revisited. FATHER SHALL learn which requirement patterns, roles, competencies, discovery methods and document depth correlate with lower rework, better estimate accuracy, higher delivery speed and higher realized business value.

Target maturity: DEFINED → MEASURED → BASELINED → CONTROLLED → OPTIMIZED → PREDICTIVE.

## 12. Core traceability

Business Goal → Business Problem → Business Requirement → KPI / Value Metric → Business Rule / Constraint → Acceptance Criterion → System Requirement → Architecture Decision → Test → Code/Process/Infrastructure → Production Metric → Business Outcome → Lesson Learned.
