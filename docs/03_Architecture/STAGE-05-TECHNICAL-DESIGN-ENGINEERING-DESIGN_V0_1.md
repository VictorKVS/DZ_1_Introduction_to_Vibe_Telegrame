# Stage 05 — Technical Design / Engineering Design v0.1

Status: DRAFT / PROVISIONAL — subject to OTUS review
Conforms to: FATHER Stage Operating Model v0.1
Owner: Engineering Architecture / Technical Design

## WHY

Translate the approved Solution Architecture into implementation-ready engineering specifications that are precise enough for development, infrastructure, security, QA and DevSecOps teams to estimate, build, test and operate the system without repeatedly guessing what the architecture meant.

The stage closes the gap between architecture and code.

## INPUT

Architecture Package from Stage 04, including approved ADRs, architecture views, requirements/NFR traceability, security/legal/economic constraints, infrastructure assumptions, capacity model, technology decisions, risks, capability gaps, TCO, evidence pack and unresolved questions.

## WHAT — mandatory engineering outputs

The exact artifact set is project-class dependent. Required information SHALL exist even when several artifacts are merged.

- TD-001 Component Technical Specifications
- TD-002 Module / Service Boundary Specifications
- TD-003 Detailed API / Interface Contracts
- TD-004 Data Model / Database Physical Design
- TD-005 Data Migration / Transformation Design where applicable
- TD-006 Algorithm / Processing Design for material logic
- TD-007 Event / Message / Queue Contracts where applicable
- TD-008 State / Workflow / Transaction Design
- TD-009 Error Handling / Retry / Idempotency Design
- TD-010 Concurrency / Consistency / Transaction Design
- TD-011 Caching / Indexing / Search Design where applicable
- TD-012 Security Control Implementation Design
- TD-013 IAM / Authorization Implementation Model
- TD-014 Secrets / Key / Certificate Handling Design
- TD-015 Logging / Audit / Metrics / Tracing Design
- TD-016 Performance / Capacity Implementation Plan
- TD-017 Resilience / Backup / DR Technical Design
- TD-018 Infrastructure / Deployment Specification
- TD-019 IaC / Environment Specification
- TD-020 CI/CD / Build / Release Pipeline Design
- TD-021 Dependency / Package / License Baseline
- TD-022 SBOM Strategy and Supply-Chain Controls
- TD-023 Test Design Inputs / Testability Hooks
- TD-024 Feature Flags / Rollback / Migration Strategy
- TD-025 Operations / Runbook Design Inputs
- TD-026 Detailed WBS / Bottom-Up Estimate
- TD-027 Resource / Competency / Capacity Plan
- TD-028 Technical Design Decision Log
- TD-029 Engineering Handover Package

## HOW — design methods

Methods are selected according to problem type and must be linked to WHY when material. Candidate methods include:

- API-first / contract-first design;
- schema-first design;
- domain-driven decomposition;
- sequence/state/workflow modeling;
- event modeling;
- data modeling and normalization/denormalization analysis;
- algorithm complexity analysis;
- concurrency/transaction analysis;
- capacity modeling;
- threat modeling and abuse-case refinement;
- secure-by-design patterns;
- failure-mode analysis;
- design reviews / peer reviews;
- spike / PoC / benchmark where uncertainty remains;
- test-driven specification and fitness functions.

FATHER SHALL store method, context, expected outcome, effort/cost, competence requirement and later effectiveness.

## ALGORITHMS AND IMPLEMENTATION CHOICES

At this stage detailed algorithmic decisions become explicit when they affect correctness, latency, memory, throughput, cost, security, determinism, explainability, maintainability or scaling.

For material algorithm choices record:

Problem → Candidate algorithms/approaches → Complexity/constraints → Benchmark or evidence → Data assumptions → Failure modes → Cost/resource impact → Security/privacy impact → Selected approach → Validation test.

Do not over-document trivial implementation choices. Escalate only when the choice materially affects architecture drivers or Survival Rules.

## WITH WHAT

Record required and available engineering resources:

- repositories and branching model;
- source/build environments;
- frameworks/libraries/SDKs;
- databases and brokers;
- API gateways/integration platforms;
- cloud/on-prem services;
- compute/GPU/CPU/RAM/storage/network quotas;
- development/test/staging environments;
- secrets/IAM systems;
- observability stack;
- CI/CD systems;
- SAST/SCA/secrets/container/IaC/DAST capabilities;
- test data and synthetic data;
- licenses and external services;
- documentation/modeling tools;
- knowledge/evidence sources.

Unknown cost or capacity items remain explicit placeholders with status NOT_ESTIMATED / NOT_VALIDATED.

## BY WHOM

Primary roles may include Technical/Software Architect, Lead Engineer, Backend/Frontend/Mobile Engineers, Data Engineer/DBA, Integration Engineer, DevOps/Platform Engineer, Security Engineer, QA/Test Architect, SRE/Operations and Technical Writer.

Supporting review: Solution Architect, System Analyst, Legal/Compliance where implementation affects regulated constraints, Economics/FinOps where design materially changes TCO.

Each work package records required competency level, actual assigned competency, available hours, review/supervision requirement and capability gap.

## WORK PACKAGES / ESTIMATION

Typical WBS:

- WP-05.01 Component/service detailed design
- WP-05.02 API/integration contracts
- WP-05.03 Data/storage design
- WP-05.04 Algorithms/workflows/state design
- WP-05.05 Security/IAM implementation design
- WP-05.06 Infrastructure/deployment/IaC design
- WP-05.07 CI/CD and supply-chain design
- WP-05.08 Observability/operations/resilience design
- WP-05.09 Testability and acceptance hooks
- WP-05.10 Design review / handover

Each WP uses O/M/P → PERT plus Bottom-Up decomposition where enough information exists. Store estimate, confidence, assigned role/capacity, rate placeholder, labor cost, infrastructure/tool cost, risk reserve, baseline and actual.

## GATES

### Quality Gate
Checks implementation readiness, internal consistency, traceability, interface completeness, ambiguity, testability and unresolved design gaps.

### Security Gate
Checks secure design controls, IAM, secrets, trust boundaries, dependency/supply-chain controls, logging/audit requirements, abuse cases and security test hooks.

### Legal / Compliance Gate
Checks implementation-level obligations such as data location/retention, auditability, licensing, IP, consent/records, contractual technical requirements and regulated interfaces.

### Economic Gate
Checks Bottom-Up implementation estimate, infrastructure/API/license cost, expected operational cost, cost-driving design decisions, migration/rollback cost and risk reserve.

### Technology Strategy Gate
Checks whether selected libraries/services/frameworks remain aligned with approved technology lifecycle, evidence, licensing, support horizon, skill availability, lock-in and exit strategy.

### Survival Rules Gate
Checks active Critical Lessons & Survival Rules. Exceptions escalate through the Decision Escalation Matrix.

## DEFINITION OF DONE

Stage 05 is complete when:

- developers can implement without inventing material requirements or architecture;
- interfaces/contracts are explicit enough for parallel work and testing;
- data and state behavior are sufficiently specified;
- material algorithms and performance assumptions have validation plans;
- security controls are implementation-ready;
- infrastructure/deployment/CI/CD expectations are explicit;
- testability hooks and acceptance mappings exist;
- operational/observability/resilience needs are designed;
- detailed WBS/PERT/Bottom-Up estimate exists at appropriate confidence;
- required competencies/capacity are assigned or gaps have mitigation;
- unknowns have owners and due dates;
- relevant gates pass or formal exceptions exist;
- Engineering/Development accepts the handover package.

## OUTPUT — ENGINEERING IMPLEMENTATION PACKAGE

The development organization receives:

Requirements/NFR traceability + approved architecture + detailed component/API/data/algorithm specs + security controls + infrastructure/IaC design + CI/CD design + test inputs + operational requirements + WBS + estimates + capability plan + risks + open questions + evidence links + decision log.

## METRICS

Track:

- design lead/touch/wait time;
- person-hours and cost plan/fact;
- estimate error;
- implementation questions caused by missing/ambiguous design;
- design rejections/rework;
- defects attributable to technical design;
- interface contract changes after coding starts;
- schema/data migration defects;
- performance regressions linked to wrong design assumptions;
- security findings attributable to technical design;
- CI/CD/infrastructure rework;
- automation/reuse ratio;
- competency gaps;
- method effectiveness;
- downstream incidents/rework;
- avoided loss/value created by early design findings.

## LEARNING LOOP

Technical Design is revisited after development, testing and production. FATHER compares predicted implementation complexity, effort, performance, cost and failure modes with actual results. Lessons update design patterns, failure cases, estimation coefficients, competency profiles, Technology Intelligence and Survival Rules.

Core traceability:

Business Goal → Requirement/NFR → Architecture Decision → Technical Design Element → Code/Config/IaC/Test → Production Metric → Outcome → Lesson.
