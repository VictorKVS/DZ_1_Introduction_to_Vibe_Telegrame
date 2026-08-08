# Architecture Decision & Design Framework v0.1

Status: DRAFT
Owner: Chief / Solution Architecture
Applies to: Stage 04 Solution Architecture and all architecture reviews

## 1. Why architecture exists

Architecture exists to convert approved system requirements into a feasible, secure, supportable and economically justified design under explicit constraints. Architecture is not a drawing exercise and not a technology-selection ceremony.

The architect must answer:

- what system qualities matter most;
- what options exist;
- why one option is preferred;
- what will it cost to build, run, secure, change and replace;
- what competencies and capacity are required;
- what risks and trade-offs are accepted;
- what evidence proves the architecture is fit for purpose;
- what conditions trigger architecture review or replacement.

## 2. Architecture inputs

The architect consumes the complete System Analysis Package and shall not silently invent missing requirements.

Minimum inputs:

- business goals and target KPI;
- SRS / functional requirements;
- NFR and quality attribute scenarios;
- data/domain models;
- integration and interface requirements;
- capacity/performance assumptions;
- availability, backup and DR requirements;
- security/privacy requirements;
- legal/regulatory constraints;
- economic constraints and cost drivers;
- accepted risks and unresolved questions;
- current enterprise landscape and reusable capabilities;
- available people, competencies, infrastructure and technology standards.

Missing critical information becomes an explicit Architecture Blocker or Assumption.

## 3. Architecture work products

Mandatory architecture package:

- ARC-001 Architecture Drivers
- ARC-002 Context / Landscape View
- ARC-003 Architecture Options A/B/C where material
- ARC-004 Trade-off Matrix
- ARC-005 Target Architecture
- ARC-006 Component / Service Decomposition
- ARC-007 Data Architecture
- ARC-008 Integration / API Architecture
- ARC-009 Infrastructure / Deployment Architecture
- ARC-010 Security Architecture / Trust Boundaries
- ARC-011 Identity & Access Architecture
- ARC-012 Availability / Resilience / Backup / DR Design
- ARC-013 Capacity / Performance Model
- ARC-014 Observability / Audit Architecture
- ARC-015 Technology Portfolio / Reuse / Buy-Build Decision
- ARC-016 TCO / Cost Model
- ARC-017 Risk & Threat-Loss Register
- ARC-018 Migration / Transition Architecture
- ARC-019 Architecture Fitness Functions
- ARC-020 ADR Set
- ARC-021 Architecture Resource & Competency Plan
- ARC-022 Architecture Handover Package

## 4. How architecture is designed

Architecture methods are selected by problem class, not habit. Candidate methods include:

- quality attribute scenarios;
- ATAM / lightweight trade-off analysis;
- ADR;
- C4 views;
- DDD / bounded contexts where domain complexity justifies it;
- event storming;
- threat modeling;
- data-flow and trust-boundary modeling;
- capacity modeling;
- failure-mode analysis;
- workload characterization;
- build/buy/reuse analysis;
- technology radar review;
- proof of concept / spike;
- benchmark / load test;
- migration rehearsal;
- economic scenario analysis;
- architecture fitness functions.

For each material method, record: purpose, why selected, required competence, evidence expected, effort/cost, limitations and later outcome quality.

## 5. Architecture option model

For every material architecture decision, compare at least two plausible alternatives unless there is a documented constraint that makes alternatives meaningless.

Each option records:

- description;
- requirements satisfied;
- quality attribute impact;
- implementation effort;
- operational effort;
- TCO;
- expected security loss / residual risk;
- legal/compliance impact;
- infrastructure demand;
- people/competency demand;
- vendor lock-in;
- migration/exit cost;
- strategic asset impact;
- knowledge/reuse value;
- uncertainty/confidence;
- evidence and assumptions.

## 6. Decision criteria

No universal score is mandatory. Weighted scoring may be used only if weights are explicit and sensitivity is understood.

Typical criteria:

- business value support;
- functional fit;
- performance / capacity;
- availability / resilience;
- security;
- privacy / legal;
- maintainability;
- operability;
- time to market;
- implementation cost;
- TCO;
- cost of delay;
- migration cost;
- technology maturity;
- vendor dependency;
- competency availability;
- reuse potential;
- strategic differentiation.

## 7. Economic architecture model

Architecture must calculate not only build cost but lifecycle economics:

Build Cost + Migration Cost + Infrastructure + Cloud + LLM/API + Licenses + Labor + Security + Legal + Support + Monitoring + Backup/DR + Training + Taxes/Overhead + Risk Reserve + Expected Loss + Cost of Delay + Exit/Replacement Cost.

Unknown items remain present as 0 + NOT_ESTIMATED.

For significant options maintain P50/P80 or comparable uncertainty ranges where enough information exists.

## 8. Capability and capacity model

Architecture shall specify required implementation and operational capabilities:

- role;
- competency;
- level;
- estimated hours;
- availability window;
- tooling;
- environment;
- infrastructure quota;
- reviewer/supervision requirement.

Compare to available capability and identify gaps. A design that cannot be built or operated by the available organization is not considered feasible without a gap-resolution plan.

## 9. Security embedded in architecture

Architecture Security Gate includes:

- assets and criticality;
- data classification;
- trust boundaries;
- identity/authentication/authorization;
- secrets/key management;
- network segmentation;
- secure communication;
- threat model / abuse cases;
- logging/audit;
- backup/recovery;
- supply-chain assumptions;
- residual risk and expected monetary loss;
- required security tests and controls.

Security requirements become architecture constraints and later test obligations.

## 10. Legal and jurisdiction embedded in architecture

Architecture records jurisdiction profile, data location, processor/controller roles where applicable, retention, cross-border flows, contractual restrictions, sector obligations and mandatory human decisions.

A technical option that violates a mandatory legal constraint is not merely lower-scored; it is infeasible unless an approved legal exception exists.

## 11. Technology lifecycle and exit design

For each significant technology record:

- lifecycle state: ASSESS / TRIAL / ADOPT / STANDARD / LEGACY / RETIRE;
- maturity;
- support status;
- license;
- community/vendor health;
- critical dependencies;
- data portability;
- interface abstraction strategy;
- replacement candidates;
- migration complexity;
- estimated replacement cost;
- review date;
- review triggers.

Review triggers include end-of-support, major price change, severe security event, material performance gap, regulatory change, vendor lock-in escalation, loss of internal competence or emergence of a clearly superior strategic option.

## 12. Architecture Definition of Done

Architecture is DONE only when:

- architecture drivers are explicit;
- material alternatives were considered;
- selected option has documented rationale;
- all critical NFRs are addressed;
- capacity assumptions are explicit;
- security/legal/economic gates are passed or formally waived;
- implementation and operation competencies are available or gap plan approved;
- key risks have owners and responses;
- TCO and unknown-cost placeholders exist;
- migration/exit is considered for critical technologies;
- architecture fitness functions / verification criteria exist;
- ADRs are linked to requirements and tests;
- downstream engineering accepts the handover package.

## 13. Architecture metrics

### Outcome metrics
- percentage of architecture decisions meeting expected outcomes;
- production SLO attainment attributable to architecture;
- realized TCO vs predicted TCO;
- realized risk/loss vs expected risk/loss;
- business KPI support.

### Process metrics
- architecture lead time;
- architecture touch/wait time;
- number of decision iterations;
- decision latency;
- architecture review cycle time;
- effort and cost plan/fact.

### Quality metrics
- architecture-related defects;
- late NFR discovery;
- downstream rework caused by architecture;
- number of emergency architecture changes;
- handover rejection rate;
- fitness-function failures.

### Competency metrics
- estimate accuracy by architect/team;
- review findings by competency domain;
- method effectiveness by project class;
- dependency on scarce experts;
- reusable pattern usage;
- AI-assisted vs human effort and outcome.

### Evolution metrics
- average replacement/migration cost;
- technology obsolescence events detected early;
- percentage of technologies with exit plan;
- technical debt growth/retirement;
- architecture reuse rate.

## 14. Architecture learning loop

Architecture Decision → Implementation → Test → Production → Cost → Incident / Change → Business Outcome → Architecture Review → Pattern / Anti-pattern / Standard update.

FATHER shall learn which architecture decisions work under which contexts, rather than declaring any architecture pattern universally best.
