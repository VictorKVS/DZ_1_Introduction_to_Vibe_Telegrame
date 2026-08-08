# Architecture Decision Escalation Matrix v0.1

Status: DRAFT / PROVISIONAL
Owner: Architecture Governance

## Purpose

Determine the governance depth of a material decision from its possible loss, irreversibility, uncertainty, security/legal impact, scope and capability gap. The level controls who participates, how much evidence is required, whether PoC/benchmark is mandatory, and who may accept residual risk.

## Dimensions

Assess at least: implementation exposure, worst credible loss, expected loss, reversibility/switching cost, blast radius, security/privacy impact, legal/compliance impact, data criticality, availability/safety impact, vendor lock-in, uncertainty/evidence quality, novelty/R&D, capability gap, operational complexity and strategic lifetime.

Do not collapse all dimensions into a single opaque score. Preserve individual drivers and WHY for escalation.

## Levels

### L1 — Local / Reversible
Low exposure, narrow blast radius, easily reversible, established pattern, strong evidence.
Approval: Architect/Tech Lead within delegated authority.
Minimum: short ADR, requirement traceability, alternatives appropriate to impact, cost note, evidence references, rollback/review trigger.

### L2 — Architecture Review
Meaningful cross-component impact, moderate cost/risk or non-trivial uncertainty.
Approval: Architect + relevant Engineering/System Analysis/Product reviewers.
Minimum: A/B alternatives, trade-off analysis, evidence pack, effort/TCO range, operational impact, validation plan.

### L3 — Architecture Board
High cost, major data/security/availability impact, significant lock-in, material capability gap, difficult reversal or potential loss in the organization's high-impact range.
Participants as applicable: Architecture, Product, Engineering, Security, Legal/Compliance, Economics/FinOps, Infrastructure/Operations, QA, Domain Expert.
Minimum: A/B/C where meaningful, independent/contradicting evidence, failure cases, TCO, Expected Loss, capability/capacity plan, migration/exit strategy, scenario/sensitivity analysis and PoC/benchmark when uncertainty is material.

### L4 — Strategic / Survival-Critical
Enterprise-wide or strategic commitment, extreme or existential downside, highly irreversible decision, regulated/safety-critical impact, or explicit Survival Rule exception with major exposure.
Approval: accountable executive/sponsor plus Architecture Board; independent expert/review where justified.
Minimum: full L3 package, strategic scenarios, P50/P80 or equivalent uncertainty ranges where appropriate, deep OSINT/market/competitor evidence, independent validation, explicit residual-risk acceptance, exit/continuity plan and scheduled outcome reviews.

## Survival Rule integration

A proposed violation or exception to an ACTIVE Survival Rule cannot remain at L1. Default escalation:
- low/materially bounded exception → at least L2;
- material financial/security/legal/operational exposure → at least L3;
- exception with high or strategic downside, irreversible consequences, or exposure beyond delegated risk appetite → L4.

The rule owner and applicable control owners participate. Exceptions require duration, exposure, compensating controls, Expected Loss, approver, monitoring and expiry.

## Evidence depth by level

L1: concise evidence, normally authoritative primary documentation/internal standard where sufficient.
L2: multiple relevant sources or internal evidence; contradictions documented when material.
L3: triangulation, failure cases, independent evidence where available, internal PoC/benchmark when justified.
L4: strongest economically reasonable evidence set, independent challenge, scenarios and explicit uncertainty.

LLM output alone is never evidence.

## Economic proportionality

Research and governance cost should be proportional to Value of Information and potential downside. Do not spend weeks proving a reversible low-cost choice; do not make a multi-million-loss decision from intuition and one vendor presentation.

## Outcome feedback

Decision level itself is validated after implementation. Track whether L1/L2 decisions repeatedly cause high-impact rework/incidents and whether L3/L4 review creates measurable avoided loss. Governance thresholds and mandatory methods may then be proposed for adjustment with provenance and approval.

## Decision Gate output

Every material decision records: level, escalation drivers, approvers, required reviewers, evidence depth, required methods/tests, residual risk owner, Survival Rules touched, decision expiry/review triggers and Architecture Outcome Review schedule.
