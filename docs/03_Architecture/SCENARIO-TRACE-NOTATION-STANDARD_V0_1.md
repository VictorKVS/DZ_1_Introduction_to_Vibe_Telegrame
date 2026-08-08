# Scenario Trace & Notation Standard v0.1

Status: DRAFT / PROVISIONAL — subject to OTUS review
Owner: Architecture Governance + QA/Test Architecture

## Purpose

Create one coherent graphical and traceable representation of system behavior from business process through architecture, technical design, tests and real runtime traces. Diagrams are not isolated pictures; they are linked views of the same scenario/event chain.

## Core principle

Every important business/system scenario receives a stable Scenario ID. All diagrams, requirements, tests, traces, logs and incidents refer to that ID and to stable Event/Step IDs where applicable.

Example chain:

Business Process → System Scenario → Architecture Interaction → Technical Sequence → Test Scenario → Runtime Trace → Defect/Incident → Outcome.

## Canonical notation stack

Use the smallest set of widely understood notations appropriate to each layer.

### 1. Business / process layer
BPMN 2.x — for business processes, actors/lanes, gateways, events, timers, messages and exception paths.

Purpose: show what the business/user is trying to accomplish and where responsibility changes.

### 2. Enterprise / capability context where needed
ArchiMate-style views may be used for enterprise capability, application, technology and business relationships when project scale justifies them.

Purpose: relate business capability, applications and technology without overloading implementation diagrams.

### 3. System structure
C4 Model — Context, Container and Component views.

Purpose: show system boundaries, major applications/services/components and ownership/dependencies.

### 4. Runtime interaction
UML Sequence Diagram — canonical notation for ordered call/event chains.

Purpose: show who calls whom, request/event order, synchronous/asynchronous interactions, retries, branches and expected responses.

### 5. State behavior
UML State Machine where state is material.

Purpose: show legal states, transitions, guards, timeout/error/recovery paths.

### 6. Data
ER / physical data model for persistence; DFD where data flow/trust boundaries are important.

Purpose: show what data is created/read/updated, where it crosses boundaries and what persistence changes are expected.

### 7. Deployment and network
C4 Deployment or UML Deployment plus explicit network/trust-boundary view where needed.

Purpose: map logical interaction to actual runtime nodes, zones, clusters, networks and trust boundaries.

### 8. Security paths
DFD + trust boundaries + abuse/attack-flow overlays where security analysis requires them.

Purpose: connect threat model and security tests to the same scenario chain.

## Scenario model

Each ScenarioRecord should include:

- scenario_id;
- name;
- business_goal / requirement links;
- trigger;
- actors;
- preconditions;
- ordered steps/events;
- alternate/exception paths;
- expected outputs;
- state changes;
- data changes;
- integrations;
- security controls;
- observability expectations;
- linked architecture diagrams;
- linked tests;
- linked runtime traces;
- owner;
- version/status.

Each important step receives Step/Event ID, for example SCN-PAY-017.E04.

## Diagram chaining

A scenario should be navigable vertically:

BPMN Process
  ↓ Scenario ID
C4 Context/Container
  ↓ same Scenario ID
UML Sequence
  ↓ same Step/Event IDs
State/Data/Trust views
  ↓
Test Case / Test Suite
  ↓
OpenTelemetry Trace / Logs / Metrics
  ↓
Actual Outcome

The graphical UI may later display these as consecutive synchronized panels or as drill-down layers.

## Test overlay

Each test must declare which scenario steps it covers and what it injects/observes.

Example:

Test ID: TEST-PAY-017
Scenario: SCN-PAY-017
Covered steps: E03-E08
Input: duplicate request with same idempotency key
Expected interactions: API → Payment Service → DB → Event Bus
Expected DB delta: one payment row
Expected event delta: one PaymentCreated event
Expected observability: two request spans, one business transaction/event publication
Expected result: no duplicate charge

## Runtime trace overlay

Use distributed tracing concepts compatible with OpenTelemetry where applicable:

- trace_id = one end-to-end execution;
- span_id = one operation/component segment;
- parent_span_id = causal parent;
- service/component name;
- operation/event name;
- start/end/duration;
- status/error;
- scenario_id/test_id attributes where safe and feasible;
- business correlation ID where appropriate;
- architecture component ID;
- step/event ID when deterministic mapping is possible.

This enables planned UML Sequence and actual runtime trace to be compared.

## Design vs actual comparison

For each scenario FATHER should eventually display:

PLANNED PATH
Actor → Gateway → Service A → DB → Event Bus → Service B

ACTUAL TRACE
Actor → Gateway → Service A → Cache → Service A retry → DB → Event Bus → Service B

Difference:
- unexpected cache call;
- retry occurred;
- latency added at Service A;
- architecture/test expectation changed or implementation defect detected.

## Debugging mode

During debugging/testing, the graphical interface should allow:

1. choose Scenario ID;
2. show canonical expected sequence;
3. replay one test execution;
4. overlay actual spans/events/logs;
5. highlight missing/unexpected steps;
6. show state/data deltas;
7. show failed assertion/security control;
8. jump to requirement, ADR, code/PR and test;
9. create defect or update design if expected behavior was wrong.

## Diagram source format

Diagrams should be stored as text/source-controlled artifacts where practical so they can be versioned, diffed and generated automatically. Candidate rendering formats include PlantUML/Mermaid/Structurizr DSL or equivalent approved tooling, while the semantic notation remains BPMN/C4/UML/DFD/ER as defined above.

The repository stores source + stable IDs + metadata; rendered SVG/PNG is derived output where possible.

## Naming / ID standard

Examples:

- PROC-ORDER-001 — BPMN business process
- SCN-ORDER-014 — system scenario
- EVT-ORDER-014-05 — event/step
- C4-ORDER-CTX-01 — context view
- SEQ-ORDER-014 — sequence view
- STM-ORDER-01 — state machine
- DATA-ORDER-01 — data view
- TEST-ORDER-014-03 — test
- TRACE-... — runtime execution reference
- DEFECT-... / INC-... — defect/incident

IDs are stable across renderings and versions.

## Quality criteria

A scenario/diagram set is good when:

- the same entities use the same IDs/names across views;
- arrows/interactions have explicit meaning;
- sync vs async is visible;
- happy path and material exception paths are represented;
- state/data side effects are traceable;
- trust boundaries are explicit where relevant;
- every critical interaction is testable/observable;
- runtime evidence can be mapped back to planned steps;
- diagrams are version-controlled and not stale relative to implementation.

## Metrics

Track:

- scenario coverage by sequence diagrams;
- test coverage by scenario steps;
- runtime trace mapping coverage;
- planned-vs-actual path deviations;
- defects found through path comparison;
- stale diagram rate;
- mean time to diagnose with/without scenario trace;
- handover/debugging time saved;
- undocumented runtime interaction count.

## Target UI

FATHER should ultimately provide a Scenario Trace Viewer with synchronized layers:

Business Process | Architecture | Sequence | State/Data | Test | Runtime Trace | Metrics/Errors

Selecting one step highlights the corresponding element in every layer. This creates a visual chain from intent to actual execution and makes architecture, testing and debugging one connected model rather than separate documents.
