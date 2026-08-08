# FATHER Project Processing Profiles v0.2

Status: DRAFT / PROVISIONAL
Owner: Product Engineering Governance

## Purpose

Separate four concepts that must not be mixed:

1. Project Type — what kind of project this is: startup, learning task, internal tool, commercial product, regulated system, etc.
2. FATHER Depth — how deeply FATHER processes the project: MIN / FAST / STANDARD / FULL.
3. Decision Criticality — how risky a specific decision is: L1 / L2 / L3 / L4.
4. Learning Override — a temporary per-stage depth increase used to study/practice a discipline even when the project itself is small.

The same underlying model, stable IDs and traceability are used at all depths.

Core invariant:
WHAT → WHY → DECISION → TEST → IMPLEMENTATION → RESULT → LESSON.

## 1. Project Type

Project Type describes context, not governance depth.

Initial types:
- LEARNING_TASK
- STARTUP / MVP
- INTERNAL_TOOL
- PRODUCT
- ENTERPRISE
- REGULATED / CRITICAL
- RESEARCH / R&D

A STARTUP may run at MIN, FAST, STANDARD or FULL. A LEARNING_TASK may also run at any depth.

## 2. FATHER Depth

### MIN

Purpose: preserve the production chain with the smallest practical overhead.

Use for small homework, spikes, tiny utilities and low-risk experiments.

FATHER should automatically keep:
- short problem/goal;
- core requirements;
- one selected solution with WHY;
- minimal diagram where useful;
- expected result / essential tests before code;
- implementation trace;
- result and lesson.

Most enterprise artifacts are merged into structured records and hidden from the normal UI.

### FAST

Purpose: startup/solo-founder speed while keeping enough architecture/test/security discipline to avoid uncontrolled improvisation.

Adds as appropriate:
- Product Brief;
- requirements/open questions;
- architecture alternatives;
- evidence/source links;
- compact risk/TCO note;
- core graphical views;
- Test Design Before Code;
- work packages and estimates;
- DevSecOps checks;
- outcome review.

Default recommendation for early FATHER projects and most learning projects.

### STANDARD

Purpose: balanced production governance for long-lived products and teams.

Uses the full Stage Operating Model proportionately, with fuller Architecture Package, Technical Design, test strategy, economics, capability/capacity model, change management and scheduled outcome reviews.

### FULL

Purpose: activate the complete FATHER factory model for deep engineering, auditability, organizational learning or high-complexity work.

May include full business/system analysis, evidence/OSINT research, failure cases, architecture methods, C4/BPMN/UML/DFD/ER views, threat modeling, economic scenarios, infrastructure/capacity planning, detailed Technical Design, Test Design Before Code, supply-chain controls, operations, outcome validation, knowledge updates and governance evidence.

FULL means maximum justified depth, not maximum paperwork. Artifacts may still be generated automatically from the structured model.

## 3. Per-stage depth

A project has a default FATHER Depth, but every stage may override it.

Example:

Project Type: LEARNING_TASK
Project Depth: FAST

Product              MIN
Business Analysis     MIN
System Analysis       FAST
Architecture          FULL
OSINT / Evidence      FAST
Security              FULL
Economics             MIN
Technical Design      FAST
Test Design           FULL
Development           FAST
DevSecOps             FULL
Operations            MIN
Outcome Review        FAST

This permits a small project to become a focused training exercise without forcing full bureaucracy everywhere.

## 4. Learning Override

Learning Override temporarily raises selected stage(s) to a requested depth.

Examples:
- studying architecture → Architecture = FULL;
- studying DevSecOps → DevSecOps = FULL;
- studying security → Security/Threat Modeling = FULL;
- studying testing → Test Design + Test Execution = FULL.

Learning Override records:
- learning objective;
- selected stage/domain;
- requested depth;
- competencies being practiced;
- expected learning evidence;
- time/cost spent;
- actual lesson/competency update.

Learning Override must never reduce mandatory controls required by decision criticality or Survival Rules.

## 5. Decision Criticality is independent

Every material decision uses the Architecture Decision Escalation Matrix:

L1 — local/reversible
L2 — peer review
L3 — targeted mini-board / strong evidence
L4 — strategic/high-impact human risk acceptance

A MIN project can contain an L4 decision. A FULL project can contain many L1 decisions.

Decision Criticality overrides simplification when risk requires it.

Example:

Project Type = STARTUP
FATHER Depth = FAST

UI library choice                 → L1
Database choice                   → L2
Sensitive personal-data handling  → L3
Irreversible 5-year vendor lock-in → L4

The project remains FAST; only the dangerous decisions become deeper.

## 6. Learning Factory concept

All course exercises, homework and experiments should be created as projects of type LEARNING_TASK or STARTUP-LAB and processed through FATHER.

This produces not merely completed homework but structured production history:

Learning Task
→ Goal/Requirement
→ Analysis
→ Architecture
→ Diagram
→ Test Before Code
→ Code
→ Security/DevSecOps
→ Test Result
→ Outcome
→ Lesson
→ Competency Update.

After many tasks FATHER accumulates training data about:
- requirement quality;
- architecture decisions;
- methods used;
- estimation accuracy;
- test quality;
- coding/rework time;
- security findings;
- recurring mistakes;
- competency growth;
- which automation actually saves human effort.

## 7. Human Effort Ratio

Primary usability metric:
Human Effort Ratio = human active decision/review time / total production effort.

Track:
- human minutes per project;
- clarification questions;
- approval actions;
- manual form/document time;
- AI-generated artifact acceptance/rework;
- lead time;
- missed gaps;
- avoided rework/loss.

A depth profile that creates more governance cost than value should be simplified.

## 8. UX

Project creation should expose a small configuration panel:

Project Type: [Learning Task / Startup / Product / ...]
FATHER Depth: [MIN / FAST / STANDARD / FULL]
Learning Override: [none / select stages]
Decision Criticality: automatic per decision, with human override/escalation and recorded WHY.

Normal user view shows only actions requiring attention. The full model remains available graphically and in generated documents.

## 9. Core rule

Project Type tells FATHER what kind of work is being done.
FATHER Depth tells FATHER how much process/detail to apply.
Decision Criticality tells FATHER how much risk governance a specific decision needs.
Learning Override tells FATHER where to intentionally go deeper for training.

These are independent axes and must remain independently configurable.
