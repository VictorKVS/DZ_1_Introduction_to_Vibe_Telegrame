# Role Expert Knowledge & Decision Model v0.1

Status: DRAFT / PROVISIONAL
Owner: Enterprise Governance / FATHER Core

## 1. Principle

Every material participant in the product factory — Product, Business Analysis, System Analysis, Architecture, Engineering, QA, Security, Legal, Economics/FinOps, DevOps/Platform, Operations and other domain roles — SHALL work from an explicit role knowledge model rather than from undocumented personal habit alone.

The depth of expert work is proportional to project processing depth, decision criticality, uncertainty, reversibility, order/value exposure and potential loss.

Core chain:

Task → Role Objective → Context/Constraints → Role Knowledge Base → Candidate Methods/Decisions → Evidence → Weighted/Risk-Based Evaluation → Decision/Artifact → Verification → Actual Outcome → Role Knowledge Update.

## 2. Role Knowledge Base

Each role maintains a governed RoleKB containing, as applicable:

- problem/task classes;
- approved methods/practices;
- applicability conditions and exclusions;
- standards/regulations/policies;
- books, papers, official documentation and authoritative references;
- internal templates and patterns;
- successful and failed external cases;
- internal lessons, incidents and near misses;
- decision heuristics and warning signals;
- objective functions / weighted criteria;
- hard constraints and Survival Rules;
- expected effort/cost ranges;
- competency requirements;
- validation methods and Definition of Done;
- source provenance, freshness and confidence;
- measured historical outcomes.

LLM-generated text is not primary evidence. It may search, summarize, compare and propose, but material claims must preserve underlying sources or be explicitly marked as inference/hypothesis.

## 3. Role Decision Profile

For every material task or decision, FATHER creates a RoleDecisionProfile:

- role;
- task/problem class;
- business/project objective;
- required outcome;
- project type;
- FATHER Depth: MIN / FAST / STANDARD / FULL;
- Decision Level: L1 / L2 / L3 / L4;
- order/project value exposure;
- potential direct loss;
- potential lost revenue/opportunity cost;
- security/legal/operational impact;
- reversibility;
- uncertainty;
- time available;
- required evidence depth;
- required expert competency;
- need for independent/human review;
- research/analysis budget;
- Value of Information.

## 4. Risk-based expert depth

### LOW / L1
Use existing validated patterns, concise evidence and automated checks. Minimal human attention.

### MODERATE / L2
Compare alternatives, use multiple relevant evidence sources, peer review where useful, and explicit validation criteria.

### HIGH / L3
Use deeper role-specific analysis, independent/contradictory evidence, failure cases, scenarios/sensitivity where applicable, expert review and explicit residual risks.

### STRATEGIC / L4
Use strongest economically justified evidence, senior/domain experts, independent challenge, scenario modelling, explicit uncertainty, accountable approval and scheduled outcome review.

Project monetary value alone does not determine depth. A low-cost change may have catastrophic security/legal consequences; a high-price but reversible standard procurement may require less technical investigation.

## 5. Role-specific examples

### Product / Product Manager KB
Methods: JTBD, customer/problem discovery, product metrics, experiment design, pricing/value hypotheses, prioritization, market/competitor evidence.
Decision weights may include customer value, revenue potential, time-to-market, adoption probability, strategic fit, cost and reversibility.

### Business Analyst KB
Methods: stakeholder analysis, interviews, BPMN, process analysis/mining, business rules, AS-IS/TO-BE, acceptance criteria, traceability.
Weights: ambiguity reduction, business coverage, evidence quality, stakeholder cost, time, downstream rework risk.

### System Analyst KB
Methods: functional decomposition, use cases, UML/SysML where justified, state/event/data models, interface analysis, measurable NFR scenarios.
Weights: completeness, consistency, testability, solution neutrality, integration/data risk, downstream architecture rework.

### Architect KB
Methods/patterns: C4, ADR, DDD, event-driven/distributed patterns, ATAM/CBAM-style reviews, build/buy/reuse, capacity/resilience/security architecture.
Weights: NFR fit, TCO, risk, capability, portability, maintainability, security, lifecycle and switching cost.

### Developer / Senior Engineer KB
Algorithms, data structures, implementation patterns, performance engineering, concurrency, databases, language/runtime specifics, scientific papers/reference implementations/benchmarks.
Weights are task-dependent: correctness, latency, throughput, energy, memory, cloud cost, accuracy, maintainability, security, implementation time.

### QA / Test Engineer KB
Methods: risk-based testing, equivalence/boundary analysis, state-transition, decision tables, property/model-based testing, contract/performance/reliability/security test design.
Weights: defect impact, probability, coverage value, test cost, automation value, detection stage and reproducibility.

### Security KB
Threat patterns, attack techniques, controls, secure design patterns, advisories, standards, internal incidents and compensating controls.
Weights: expected loss, exploitability, asset criticality, blast radius, control effectiveness, residual risk, operational cost.

### Legal / Compliance KB
Applicable laws/regulations/contract patterns, jurisdiction rules, precedents/official interpretations where appropriate, regulatory obligations, data/IP/retention/localization requirements.
Weights: legal exposure, enforceability, jurisdiction, contractual leverage, compliance cost, business impact and uncertainty. Material legal conclusions require accountable legal review as appropriate.

### Economics / FinOps KB
TCO, CAPEX/OPEX, Cost of Delay, opportunity cost, Expected Loss, unit economics, cloud/API/licensing/tax/rent assumptions, sensitivity/scenario methods.
Weights: cash flow, ROI/value, downside, uncertainty, reversibility and strategic option value.

### DevOps / Platform KB
CI/CD, IaC, deployment, observability, SRE/reliability patterns, capacity, supply-chain controls, platform and cloud economics.
Weights: deployment frequency, recovery, reliability, security, platform cost, operational toil and portability.

### Operations / SRE KB
SLO/SLI, incident response, runbooks, capacity, DR, observability, change management, postmortems.
Weights: availability, MTTR, operational burden, business loss, resilience and maintainability.

## 6. Role Method Record

Each reusable method receives:

Method ID → Role → Problem Class → Preconditions → Procedure → Required Inputs → Outputs → Required Competency → Evidence Sources → Typical Effort/Cost → Known Limitations → Failure Cases → Validation Method → Historical Outcome Metrics → Recommendation Status.

FATHER learns not only which role produced a good outcome, but which method worked under which conditions.

## 7. Weighted criteria are contextual

FATHER SHALL NOT maintain one universal set of weights per role. It may maintain recommended priors/templates by problem class, but final weights/hard constraints come from the actual objective and risk context.

Weights must be explainable and versioned. Material changes to weights preserve WHY.

## 8. Expert escalation

If RoleKB evidence is weak, contradictory, stale, outside tested applicability, or the required competence exceeds available capability, FATHER marks EXPERT_GAP and proposes one or more:

- targeted research;
- external/domain expert;
- senior human review;
- PoC/experiment/benchmark;
- additional data collection;
- alternative lower-risk approach;
- scope reduction;
- explicit risk acceptance.

The system must not simulate certainty merely because an answer can be generated.

## 9. Deliverable provenance

Every material deliverable/decision records:

Role → Method → Inputs → Evidence → Assumptions → Alternatives → Decision/Output → Confidence → Reviewer/Approver → Validation → Actual Outcome.

This allows later questions such as:
"Why did Product prioritize this?"
"Why did Legal require this clause?"
"Why did Security select this control?"
"Why did QA use this test strategy?"
"Why did Engineering choose this algorithm?"

## 10. Organizational learning

After project execution, outcomes update role knowledge:

Expected → Actual → Variance → Cause → Role/Method contribution → Lesson → KB update → training/competency update → future recommendation.

Do not reduce evaluation to individual blame. Separate role-method quality from changed inputs, scope, implementation deviation and external events.

## 11. Role maturity

M0 — personal experience and scattered documents.
M1 — documented role standards and source registry.
M2 — structured RoleKB with stable method/pattern records.
M3 — automated retrieval, evidence packs and risk-based depth selection.
M4 — historical outcome-based method recommendations and competency calibration.
M5 — calibrated expert assistance that predicts where deeper human/domain expertise is economically justified.

## 12. Core rule

The factory does not replace expertise by making every agent sound senior. It industrializes expertise by preserving methods, evidence, boundary conditions, outcomes and escalation paths — and spends the most expert attention where the price of being wrong is highest.
