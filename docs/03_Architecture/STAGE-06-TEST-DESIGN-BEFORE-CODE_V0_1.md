# Stage 06 — Test Design Before Code v0.1

Status: DRAFT / PROVISIONAL — subject to OTUS review
Conforms to: FATHER Stage Operating Model v0.1
Owner: QA/Test Architecture + Engineering Architecture

## WHY

Define how the approved architecture and technical design will be verified before implementation begins. Tests are not an afterthought and not merely unit-test code. They are executable and documentary specifications of expected system behavior, quality attributes, security properties and failure handling.

The stage creates an independent verification contract between Architecture/Analysis and Development.

Core principle:

Requirement/NFR → Architecture Decision → Technical Design → Test Model → Expected Result → Code.

Development begins only when the implementation work package has sufficient test intent, acceptance criteria and testability inputs for its risk level.

## INPUT

- Business and system requirements;
- acceptance criteria;
- architecture drivers and ADRs;
- Architecture Views;
- detailed technical design;
- API/data/event contracts;
- threat model and security controls;
- capacity/resilience assumptions;
- legal/compliance constraints;
- Survival Rules;
- known failure cases and historical defects;
- production-like workload assumptions;
- WBS and implementation packages.

## WHAT — mandatory test-design outputs

Artifact depth is risk-based, but mandatory information must not disappear.

- TEST-001 Test Strategy / Verification Plan
- TEST-002 Requirement-to-Test Traceability Matrix
- TEST-003 Test Scope / In-Scope / Out-of-Scope
- TEST-004 Test Architecture & Environment Model
- TEST-005 Test Data Model and Data Preparation Rules
- TEST-006 Functional Test Scenarios
- TEST-007 API / Contract Test Specification
- TEST-008 Integration Test Specification
- TEST-009 Component / Service Test Specification
- TEST-010 Data / Database / Migration Test Specification
- TEST-011 State / Workflow / Transaction Test Specification
- TEST-012 Error / Retry / Idempotency / Recovery Test Specification
- TEST-013 Performance / Capacity / Load Test Specification
- TEST-014 Resilience / Failover / Backup / Restore / DR Test Specification
- TEST-015 Security Verification Specification
- TEST-016 IAM / Authorization / Privilege Test Specification
- TEST-017 Secrets / Keys / Certificate Test Specification
- TEST-018 Logging / Audit / Observability Test Specification
- TEST-019 CI/CD / Supply-Chain / SBOM Test Specification
- TEST-020 Infrastructure / IaC / Configuration Test Specification
- TEST-021 Compatibility / Portability / Migration Test Specification where applicable
- TEST-022 Legal / Compliance Verification Cases where technically testable
- TEST-023 Architecture Fitness Functions
- TEST-024 Regression Test Baseline
- TEST-025 Test Automation Plan
- TEST-026 Test Execution Cost / Environment Capacity Estimate
- TEST-027 Defect Classification & Failure Evidence Model
- TEST-028 Test Review / Approval Record
- TEST-029 Development Handover Test Package

## TEST CASE CONTRACT

Every material test case SHALL define:

- Test ID;
- WHY: requirement, NFR, ADR, control, failure case or Survival Rule being verified;
- test objective;
- preconditions;
- system state;
- actors/components involved;
- input data;
- test steps or machine-readable scenario;
- expected result;
- expected state changes;
- expected API/event/database effects;
- expected logs/metrics/audit events where relevant;
- pass/fail criteria;
- tolerance/range where exact equality is inappropriate;
- negative/error behavior;
- cleanup/reset conditions;
- test environment and required capacity;
- automation level;
- owner;
- evidence produced;
- related diagrams/notations;
- source/evidence references where the expected result relies on a standard, protocol or architectural claim.

## DIAGRAMS AND NOTATIONS

Tests SHALL use diagrams when sequence, state, topology, trust boundaries, data movement or failure propagation are material to understanding.

Recommended notations depend on the problem:

- C4 context/container/component references for tested boundaries;
- UML sequence diagrams for interaction tests;
- UML/state-machine or equivalent state diagrams for stateful behavior;
- BPMN/workflow diagrams for business/process scenarios;
- data-flow diagrams for data movement and trust boundaries;
- deployment/network diagrams for infrastructure and failover tests;
- ER/data models for database and migration tests;
- timing/load profiles for performance tests;
- attack-flow/abuse-case diagrams for security verification.

A diagram must identify its notation/legend, version/date, source architecture view and exact test cases that depend on it. Decorative diagrams without verification value are optional.

## TESTS BEFORE IMPLEMENTATION

The expected behavior must be defined before the implementation is written. This may result in different executable forms:

- acceptance-test skeletons;
- API contract tests;
- schema validation tests;
- BDD/Gherkin scenarios where useful;
- unit-test interfaces/stubs for deterministic logic;
- property-based test properties;
- architecture fitness functions;
- security test cases;
- load-test models;
- infrastructure policy tests;
- migration validation scripts.

Not every test must be fully executable before coding. The minimum before development is a reviewed test specification and, for critical behavior, an executable failing/skeleton test where economically justified.

## FUNCTIONAL TEST TEMPLATE

Test Scenario:

Given [initial state / preconditions]
When [action/event/input]
Then [observable expected result]
And [state/data/event/log effects]
And [quality/security constraints]

Each scenario links back to the requirement and forward to implementation artifacts.

## NFR TESTING

NFRs SHALL be translated into measurable verification where possible.

Examples:

Latency requirement → workload profile + percentile + duration + environment + threshold.

Availability/resilience requirement → failure injection + expected degradation/failover + RTO/RPO evidence.

Security requirement → actor/permission/data state + prohibited/allowed action + audit evidence.

Maintainability/architecture rule → automated fitness function/lint/static rule where measurable.

Cost constraint → workload + infrastructure configuration + measured usage + price profile.

## ARCHITECTURE FITNESS FUNCTIONS

Architecture decisions that can be continuously verified should become automated fitness functions.

Examples include:

- forbidden dependency checks;
- layering/module-boundary checks;
- API backward-compatibility checks;
- schema compatibility checks;
- latency/throughput thresholds;
- security configuration rules;
- IaC policy checks;
- dependency/license restrictions;
- resilience/health checks;
- observability coverage expectations.

Fitness functions preserve architecture after the original architect is no longer involved.

## SECURITY TEST DESIGN

Security verification begins before code and is derived from threat model, abuse cases, trust boundaries and controls.

Plan at least where applicable:

- authentication/authorization positive and negative cases;
- privilege escalation and access-boundary tests;
- input validation and abuse cases;
- secrets/configuration checks;
- dependency/SBOM/SCA expectations;
- SAST rules and secure coding controls;
- API security tests;
- logging/audit evidence;
- cryptography/key/certificate handling validation;
- container/IaC/configuration checks;
- DAST/pentest scope for later stages.

## TEST DATA

Test data must define source, classification, privacy constraints, synthetic/masked strategy, representativeness, edge cases, lifecycle, retention and cleanup.

Production personal/confidential data must not be copied into test environments merely for convenience.

## WITH WHAT

Record required and available test capability:

- environments;
- compute/storage/network capacity;
- service virtualization/mocks/stubs;
- datasets and generators;
- test frameworks;
- API testing tools;
- performance/load tools;
- security testing capabilities;
- observability stack;
- CI execution capacity;
- licenses/cloud/API cost;
- required access and secrets.

Unknown cost/capacity remains NOT_ESTIMATED / NOT_VALIDATED.

## BY WHOM

Primary roles: QA/Test Architect, QA Automation Engineer, System Analyst, Technical Architect/Lead Engineer.

Domain review as applicable: Security Engineer, Performance Engineer, Data Engineer/DBA, DevOps/Platform/SRE, Product/BA for acceptance, Legal/Compliance for regulated testable obligations.

Developers participate in testability review before implementation and later own relevant lower-level automated tests.

## WORK PACKAGES / ESTIMATION

Typical WBS:

- WP-06.01 Traceability and test-scope design
- WP-06.02 Functional/acceptance scenarios
- WP-06.03 API/integration/contract tests
- WP-06.04 Data/state/migration tests
- WP-06.05 Performance/capacity tests
- WP-06.06 Resilience/DR tests
- WP-06.07 Security tests
- WP-06.08 Infrastructure/CI/CD/supply-chain tests
- WP-06.09 Fitness functions and automation skeletons
- WP-06.10 Test environment/data design
- WP-06.11 Review and Development handover

Each WP uses O/M/P → PERT and Bottom-Up where feasible. Store test-environment/API/cloud cost separately from labor cost.

## TEST DESIGN GATES

### Traceability Gate
Every critical requirement/NFR/ADR/control has at least one verification path or an explicit NOT_TESTABLE justification.

### Testability Gate
The technical design exposes sufficient hooks, interfaces, logs, metrics, IDs, health endpoints and controllable states to verify behavior.

### Architecture Gate
Test scenarios accurately reflect approved architecture and do not silently redefine system behavior.

### Security Gate
Threats/controls have appropriate verification and negative test coverage.

### Economic Gate
Test depth is proportionate to price of failure. High-cost tests must be justified by Expected Loss/Value of Information; catastrophic/high-loss cases cannot be omitted merely to save test cost without explicit risk acceptance.

## DEFINITION OF READY FOR CODE

An implementation work package is READY FOR CODE when:

- linked requirements and design are baselined;
- expected behavior is explicit;
- acceptance/pass-fail criteria exist;
- material positive, negative and failure scenarios are defined;
- test data needs are known;
- required environment/capacity is known or explicitly unresolved;
- testability hooks are designed;
- security tests are identified where applicable;
- traceability exists;
- critical executable test skeletons/contract tests exist where justified;
- remaining uncertainty has an owner;
- Test Design Gate is PASS/CONDITIONAL with accepted risk.

## OUTPUT — TEST-FIRST ENGINEERING PACKAGE

Development receives:

Technical Design + test strategy + test cases + diagrams/notations + expected results + test data requirements + environment requirements + automation skeletons/contracts + security verification + fitness functions + traceability + DoR + unresolved questions.

The developer therefore implements toward a visible verification target rather than writing code first and discovering expected behavior later.

## METRICS

Track:

- percentage of requirements with tests defined before code;
- critical requirements with executable pre-code test/contract skeletons;
- defects found before coding due to test-design review;
- defects found during development/testing/production by origin;
- requirement ambiguity exposed by test design;
- architecture defects exposed by test design;
- test case rework after code begins;
- escaped defects;
- mutation/property/fault-injection effectiveness where used;
- automation ratio;
- test execution lead time and cost;
- flaky test rate;
- coverage by risk, not only code-line percentage;
- security/control verification coverage;
- production incidents that lacked a pre-release test scenario;
- avoided rework/loss due to test-first design.

## LEARNING LOOP

After implementation and production, compare predicted tests with actual defects/incidents. Ask:

- Which planned tests prevented defects?
- Which tests were useless or too expensive?
- Which production failures had no corresponding scenario?
- Which architecture assumptions were difficult/impossible to test?
- Which requirements were not testable and why?
- Which methods and competencies improved defect prevention?

Lessons update test patterns, architecture methods, technical-design templates, Failure KB, Survival Rules and estimation coefficients.

Core traceability:

Business Goal → Requirement/NFR → ADR → Technical Design → Test Specification → Executable Test → Code/Config/IaC → Test Evidence → Production Metric/Incident → Lesson.
