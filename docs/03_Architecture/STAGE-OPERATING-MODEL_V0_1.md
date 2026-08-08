# FATHER Stage Operating Model v0.1

Status: DRAFT
Owner: Architecture Governance

## Purpose

Defines the mandatory operating model for every production stage. A stage is not only a list of documents. It is a controlled transformation of inputs into an output package using explicit methods, resources, competencies, infrastructure, economics, evidence and gates.

## Universal stage contract

Every stage SHALL define:

1. WHY — business goal, problem, expected value and reason the stage exists.
2. INPUT — upstream package, evidence, assumptions, constraints and unresolved questions.
3. WHAT — work packages, tasks, artifacts and deliverables.
4. HOW — approved methods, practices, standards, algorithms and decision methods; method-selection rationale shall be recorded when material.
5. WITH WHAT — data, knowledge bases, tools, software, APIs, licenses, infrastructure, compute/storage/network capacity and external services.
6. BY WHOM — roles, RACI/decision rights, required competencies, actual competency level, capacity/availability and supervision needs.
7. HOW MUCH — O/M/P and PERT effort, rates, labor, cloud, LLM/API, licenses, rent, taxes, external services, CAPEX/OPEX, reserves and expected risk loss. Unknown monetary values are 0 + NOT_ESTIMATED, never FREE.
8. WHEN — dependencies, critical constraints, schedule, queues, resource conflicts and capacity limits.
9. HOW WELL — outcome, process, quality, security, legal, economic, technology and competency metrics.
10. DONE — Definition of Done, acceptance criteria, required evidence and gate conditions.
11. OUTPUT PACKAGE — exact handover contract to the next role/stage.
12. LEARNING — Estimate → Baseline → Actual → Variance → Cause → Outcome → Lesson → Standard/Method/Competency update.

## Capability and Capacity Profile

Each project/stage SHALL compare Required Capability against Available Capability.

Required Capability includes role, competency, level, required hours, time window, tools and infrastructure capacity.

Available Capability includes assigned person/agent/team, verified competency level, available hours, productivity history, quality history, infrastructure quota and constraints.

Gap states: NONE, SKILL_GAP, CAPACITY_GAP, TOOL_GAP, DATA_GAP, INFRASTRUCTURE_GAP, BUDGET_GAP, COMPLIANCE_GAP.

For a material gap, alternatives SHALL be evaluated where applicable: train, hire, contractor, AI assistance, reuse component, buy service/product, change method, change architecture, reschedule, reduce scope, accept risk.

Each alternative records expected cost, time, quality, risk and strategic/knowledge value.

## Method Profile

Methods are first-class measurable objects. Record method ID/name, applicable problem class, prerequisites, competency requirement, expected outputs, cost/effort range, limitations, evidence quality, historical usage, actual outcomes, rework and recommendation status.

FATHER SHALL learn which methods work best for which project classes and team profiles rather than treating methods as universal doctrine.

## Definition of Done hierarchy

DoD SHALL exist at four levels when applicable:

- Artifact DoD — document/model/code/configuration is complete and evidenced.
- Work Package DoD — all required outputs and checks for the work package are complete.
- Stage DoD — exit criteria and gates are satisfied.
- Product/Release DoD — integrated product meets business, technical, quality, security, legal and economic acceptance.

A status field alone is not evidence of completion.

## Output Package / Handover Contract

Every stage SHALL define exactly what the next stage receives, including artifacts, structured data, evidence, open questions, assumptions, decisions, risks, estimates, capability gaps, unresolved costs and traceability links.

The receiving role may reject an incomplete package with categorized findings. Handover rejection/rework is a quality metric of the producing stage.

## Cross-cutting gates

Every stage evaluates applicability of Quality, Security, Legal/Compliance, Economics and Technology Strategy gates. Additional domain gates may be added. Missing evidence cannot silently PASS.

## Improvement metrics

Track at minimum: lead time, touch time, waiting time, person-hours by role, cost plan/fact, estimate error, rework, downstream defects attributable to the stage, handover rejection, gate findings, automation ratio, reusable asset ratio, competency gaps, method effectiveness and realized downstream/business outcome.

The objective is simultaneous improvement of quality, productivity and capability without optimizing one by hiding losses in another.

## Core production chain

Product Package → Analysis Package → Architecture Package → Security/Legal/Economic/Technology Decisions → Engineering Package → Test/Acceptance Package → Release Package → Operations Package → Outcome/Lessons Package.

Every transformation is traceable to the business goal and eventually to measured production/business outcomes.
