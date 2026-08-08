# Stage 03 — System Analysis v0.1

Status: DRAFT
Conforms to: FATHER Stage Operating Model v0.1

## WHY

Convert the approved business baseline into a sufficiently complete, measurable and testable system specification from which architecture can be designed and estimated without silently inventing business requirements.

## INPUT

Business/Analysis Package from Stage 02: goals, PRD/business requirements, AS-IS/TO-BE, rules, scope, KPI/value model, constraints, data needs, acceptance criteria, traceability seed, risks, estimates, decisions and open questions.

## WHAT — mandatory output artifacts

- SA-001 System Context & Boundary Model
- SA-002 SRS / System Requirements Baseline
- SA-003 Functional Requirements & Use Cases / Scenarios
- SA-004 NFR Specification
- SA-005 Domain / Information Model
- SA-006 Data Requirements & Lifecycle Model
- SA-007 Integration & Interface Requirements
- SA-008 API Contract Candidates / Interaction Contracts
- SA-009 State / Event / Workflow Models where applicable
- SA-010 Error, Exception & Recovery Requirements
- SA-011 Observability / Audit / Logging Requirements
- SA-012 Capacity & Performance Requirements
- SA-013 Availability / Resilience / Backup / DR Requirements
- SA-014 Security & Privacy Requirements
- SA-015 Regulatory / Jurisdiction Requirement Mapping
- SA-016 System Acceptance Criteria & Testability Map
- SA-017 Requirements Traceability Matrix
- SA-018 Assumption / Constraint / Open Question Register
- SA-019 System Analysis Estimate & Resource Plan
- SA-020 System Analysis Decision Record / Handover Package

Artifacts may be merged for small projects, but mandatory information may not disappear.

## HOW — methods

Method selection depends on problem class. Candidate methods include requirements decomposition, use cases, user stories with acceptance criteria, BPMN, UML/SysML where useful, Event Storming, domain modeling, state machines, sequence diagrams, context/data-flow diagrams, interface analysis, CRUD/event matrices, NFR quality-attribute scenarios, prototyping, data profiling and requirements reviews.

For each material method record why selected, prerequisites, expected output, required competence, time/cost and later effectiveness.

NFRs SHALL be measurable where reasonably possible: performance, capacity, latency, throughput, availability, RTO/RPO, scalability, security, privacy, observability, maintainability, portability, compatibility and other project-specific quality attributes.

## WITH WHAT

Record required and available: source systems, databases, datasets, schemas, APIs, documentation, logs, knowledge bases, modeling tools, test/prototype environments, LLM/API assistance, compute/storage/network resources and access permissions.

Missing or poor-quality source information becomes a DATA_GAP or KNOWLEDGE_GAP with owner, impact and resolution plan.

## BY WHOM

Primary: System Analyst.

Supporting roles: Business Analyst, Product, Solution Architect, Data Architect/Engineer, Security, Legal/Compliance, QA/Test Architect, DevOps/Platform/Infrastructure, Domain Expert, Economist/Estimator, API/Integration specialist.

Each role assignment records required level, actual level, available hours, historical estimate accuracy/quality when known and supervision/review requirements.

## WORK PACKAGES / ESTIMATION

- WP-03.01 Context/boundary analysis
- WP-03.02 Functional decomposition
- WP-03.03 NFR formalization
- WP-03.04 Data/domain analysis
- WP-03.05 Integration/interface analysis
- WP-03.06 Security/privacy/system controls requirements
- WP-03.07 Capacity/resilience/operations requirements
- WP-03.08 Acceptance/testability mapping
- WP-03.09 Traceability and consistency review
- WP-03.10 Architecture handover review

Each WP stores O/M/P, PERT expected effort, confidence, assigned capacity, dependencies, labor and non-labor cost placeholders, risk reserve, baseline and actual.

## CAPABILITY & CAPACITY

Compare Required Capability vs Available Capability for system analysis, domain knowledge, integrations, data, NFR/performance, security, testing and infrastructure. Material gaps trigger alternative analysis: train/hire/contract/AI assist/reuse/change method/reschedule/scope adjustment.

## GATES

Quality: completeness, consistency, ambiguity, traceability, testability and measurable NFRs.

Security: security/privacy requirements, assets, trust assumptions, auditability, access-control needs and threat-model inputs.

Legal: jurisdiction/regulatory constraints translated into system requirements with source/evidence.

Economics: cost-driving requirements identified; expensive NFRs and alternatives visible; Cost of Delay/Value of Information considered for unresolved questions.

Technology Strategy: requirements remain solution-neutral unless a technology constraint is justified; reuse/buy/build candidates and lock-in constraints are identified for architecture.

## DONE

Stage is complete when system boundary is explicit; functional behavior is sufficiently specified; material NFRs are measurable; data/integration requirements are known to the required confidence; acceptance is testable; security/legal/operational requirements are mapped; unknowns are explicit; traceability exists from business goals to system requirements; estimate/resource/capability model exists; gates pass or formal waivers exist; and the architect accepts the handover package.

## OUTPUT — ARCHITECTURE INPUT PACKAGE

The architect receives the full SRS baseline plus context, models, data/integration contracts, NFR quality scenarios, capacity assumptions, security/legal requirements, acceptance/testability map, traceability, cost-driving requirements, capability gaps, assumptions, open questions, evidence and estimate confidence.

## METRICS & LEARNING

Track lead/touch/wait time, effort/cost plan-fact, estimate error, requirement volatility, ambiguity findings, missing NFRs discovered downstream, architecture rejections caused by analysis, defects traced to requirements, handover rejection, rework, method effectiveness, automation ratio, competency gaps and realized production/business outcome.

Learning loop: method + analyst/team profile + project class + estimate + actual + downstream defects/rework + outcome → update method recommendations, competency model, templates and estimation coefficients.
