# FATHER Factory Modes — FAST / STANDARD / CRITICAL v0.1

Status: DRAFT / PROVISIONAL
Owner: Product Engineering Governance

## Purpose

Use one underlying model and traceability system with different depths of research, documentation, review and human participation. The mode changes process intensity, not the requirement to preserve WHAT, WHY, key evidence, tests and outcomes.

Default for early solo use: FAST.

## 1. FAST — Startup / Solo Founder Mode

Goal: maximum speed with minimum human overhead while preserving enough traceability to avoid uncontrolled improvisation.

Typical use:
- prototype, MVP, internal tool, Telegram bot, small SaaS experiment;
- low/moderate financial exposure;
- reversible technology choices;
- one founder or very small team;
- short feedback cycle.

Human interaction target:
- answer only critical clarification questions;
- approve product direction and material trade-offs;
- review exceptional security/legal/financial risks;
- approve release when needed.

AI/agents should automatically prepare:
- compact Product Brief;
- requirements and open-question register;
- architecture options and recommendation;
- evidence/source links;
- lightweight risk/TCO note;
- core diagrams;
- Test Design Before Code;
- implementation work packages;
- DevSecOps checks;
- release notes and outcome review.

FAST may merge documents, but SHALL retain stable IDs and structured traceability in the model.

Minimum FAST gate before coding:
Problem/value understood → critical requirements/NFRs explicit → architecture selected with WHY → core scenario diagram exists → essential positive/negative/security tests defined → cost/risk not materially unknown → DoR passes.

Minimum FAST diagrams:
- one context/container view;
- scenario/sequence view for critical flows;
- data model when persistent data exists;
- trust/security boundary view when external/sensitive access exists;
- deployment view when non-trivial infrastructure exists.

Default decision levels: L1/L2. L3/L4 triggers override FAST simplification.

## 2. STANDARD — Product / Team Mode

Goal: balanced governance, quality and repeatability for production systems with a team, customers and meaningful operational responsibility.

Typical use:
- commercial product;
- multiple services/integrations;
- meaningful SLA/data/security requirements;
- several engineering roles;
- expected long-term maintenance.

Requires fuller Stage Operating Model, structured Architecture Package, Technical Design, Test Design, DevSecOps, economics, capability/capacity plan and scheduled Architecture Outcome Reviews.

Human review is targeted and mostly asynchronous. L2 is common; L3 used for material decisions.

## 3. CRITICAL — High-Impact / Regulated / Strategic Mode

Goal: reduce the probability and consequence of high-impact failure where loss, legal exposure, security impact, safety, strategic lock-in or irreversibility justifies greater analysis.

Typical use:
- high-value commitments;
- critical infrastructure/business process;
- regulated or highly sensitive data;
- major vendor/cloud/platform lock-in;
- severe availability/safety/security consequences;
- difficult or expensive rollback/migration.

Adds stronger evidence triangulation, independent review where justified, deeper threat/risk analysis, explicit residual-risk acceptance, PoC/benchmark requirements, scenario/sensitivity analysis, robust recovery/exit planning and more frequent outcome validation.

L3/L4 decisions are common.

## 4. Mode does not hide risk

A project may start in FAST but individual decisions automatically escalate when Decision Escalation Matrix or Survival Rules require it.

Example:
FAST project + trivial UI library → FAST/L1.
FAST project + storing sensitive customer data → security controls may require L2/L3 review.
FAST project + 5-year irreversible vendor contract → L3/L4 regardless of project mode.

## 5. Mode switching

Mode may change during the project.

FAST → STANDARD triggers may include:
- paying external customers;
- growing team;
- SLA/support obligations;
- persistent sensitive data;
- significant recurring revenue/cost;
- architecture complexity or operational incidents.

STANDARD → CRITICAL triggers may include:
- regulatory classification;
- major financial exposure;
- severe security/safety impact;
- strategic dependency/lock-in;
- high irreversibility;
- repeated serious incidents.

Mode changes are recorded with WHY and effective baseline version.

## 6. Human Effort Ratio

Primary usability metric:
Human Effort Ratio = human active decision/review time / total production effort.

Track alongside:
- clarification questions per project;
- approval actions per stage;
- time spent filling forms manually;
- agent-generated artifact acceptance rate;
- rework due to missing human context;
- defects/risks prevented;
- lead time to working release.

The goal is not zero human involvement. The goal is to reserve human attention for decisions where judgment adds material value.

## 7. FAST UX rule

For solo/startup use, the normal screen should not expose the whole enterprise model by default. Show a concise action queue such as:

- 3 questions need your answer;
- 1 architecture choice needs approval;
- 1 cost/risk exception needs review;
- release candidate is ready.

The detailed graph, evidence, diagrams, tests and documents remain available on demand.

## 8. Core invariant across all modes

FAST simplifies presentation and review depth, not causality.

Always preserve, proportionate to risk:
WHAT → WHY → DECISION → TEST → IMPLEMENTATION → RESULT → LESSON.

This allows a solo founder to begin in FAST without creating an undocumented prototype that later cannot mature into STANDARD or CRITICAL governance.
