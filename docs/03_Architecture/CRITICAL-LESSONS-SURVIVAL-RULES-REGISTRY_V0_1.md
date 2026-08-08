# Critical Lessons & Survival Rules Registry v0.1

Status: DRAFT / PROVISIONAL
Owner: Enterprise Governance

## Purpose

Maintain a compact registry of high-impact rules whose violation can create disproportionate financial, legal, security, operational or strategic loss. Rules may originate from external failure cases, standards, expert experience, internal incidents, near misses, scenario analysis or preventive reasoning. We do not need to suffer a catastrophe before adopting a well-supported preventive rule.

## Core principle

A Survival Rule is not folklore and not an absolute slogan. Every rule must preserve WHY: risk addressed, applicability, evidence, expected loss, exceptions, owner, review date and conditions for retirement.

Rule lifecycle:
PROPOSED → REVIEWED → ACTIVE → EXCEPTION_GRANTED / REVIEW_DUE → SUPERSEDED / RETIRED.

## Rule record

Each rule SHALL contain:
- Rule ID and short imperative statement;
- domain;
- protected objective/asset;
- failure scenario;
- rationale / WHY;
- applicability and exclusions;
- supporting and contradicting evidence;
- external failure/success cases;
- internal incidents/near misses if any;
- probability/range and impact/range where estimable;
- Expected Loss / worst credible loss;
- mandatory controls;
- required evidence of compliance;
- exception authority and compensating controls;
- owner;
- review trigger and review date;
- links to policies, contracts, ADRs, tests and metrics;
- observed outcomes after adoption.

## Initial preventive rules — candidates for Legal/Economic/Security review

These are starting hypotheses, not universal legal advice. Their thresholds and wording must be adapted to jurisdiction, project type and risk.

### SR-FIN-001 — No material unsecured credit exposure without approved protection
Do not extend material credit/deferred payment or incur material unrecoverable expenditure for a counterparty without an executed agreement and a reviewed protection model appropriate to the exposure.

WHY: non-payment, dispute, delay and counterparty failure can convert delivered work and committed costs into direct loss and lost cash flow.

Possible controls: signed contract/order, payment schedule, advance/milestones, credit limit, security/guarantee where justified, suspension rights, acceptance procedure, late-payment/remedy clauses where lawful, termination rights, counterparty check and exposure monitoring.

Important: a penalty alone is not assumed to cover all loss or to be collectible. Legal and financial review determines enforceability, recoverability and whether the protection is economically sufficient.

### SR-FIN-002 — No irreversible commitment without downside calculation
Before a material irreversible or expensive-to-reverse commitment, record downside scenarios, switching/exit cost, Expected Loss, funding requirement and decision authority.

### SR-CON-001 — No material work outside an agreed scope and change mechanism
Material work must be traceable to an approved scope, acceptance criteria and change process. Emergency exceptions must be documented retrospectively within the defined SLA.

### SR-CON-002 — No dependency on an undocumented verbal promise for a critical obligation
Critical commercial, delivery, access, SLA, data, IP, support and acceptance obligations require durable evidence appropriate to the jurisdiction and contract model.

### SR-ARC-001 — No high-impact architecture decision without alternatives and WHY
Material architectural decisions require alternatives, decision criteria, evidence, rejected-option rationale, cost/TCO, risk, capability feasibility, validation plan and review trigger.

### SR-ARC-002 — No strategic lock-in without an exit strategy
For material vendor/platform lock-in, document data portability, replacement candidates, migration path, estimated switching cost, contractual exit conditions and triggers for reconsideration.

### SR-ARC-003 — No capacity-critical design without measured assumptions
Critical capacity/performance decisions require explicit workload assumptions and a validation method such as benchmark, load test, PoC or production fitness function proportionate to risk.

### SR-SEC-001 — No production secret in source code or ordinary documentation
Secrets require approved secret storage, controlled access, rotation/revocation and auditability appropriate to the environment.

### SR-SEC-002 — No unreviewed external dependency with privileged or sensitive access
A third party, service, package or integration receiving material privileged/sensitive access requires risk-based security, legal, data and lifecycle review.

### SR-DATA-001 — No critical data store without ownership, backup/recovery and restore evidence
Critical data requires owner, classification, retention, backup/recovery requirements and periodic restore verification proportionate to business impact.

### SR-OPS-001 — No critical service without observability and accountable ownership
Critical production services require an owner, service objectives where applicable, logging/metrics/alerts, incident route and sufficient operational evidence to detect and diagnose material failure.

### SR-REL-001 — No high-impact release without rollback/recovery strategy
Where rollback is impossible, the release requires an explicitly approved alternative recovery/forward-fix strategy and higher decision level.

### SR-KNOW-001 — No critical single-person knowledge dependency without mitigation
Critical knowledge concentrated in one person/agent requires documentation, handover, second-person review, automation, training or another justified continuity control.

### SR-AI-001 — No high-impact autonomous AI decision without bounded authority and evidence
AI/agents may recommend or execute only within explicit authority. High-impact financial, legal, security, safety or irreversible actions require risk-based controls, traceability and accountable human approval unless a separately governed automation case has been approved.

## Exception process

A rule is strong precisely because exceptions are visible. An exception record must contain: business reason, duration, exposure, compensating controls, Expected Loss, approver, monitoring, expiry and closure evidence. Permanent silent exceptions are prohibited.

## Proactive rule discovery

Rules may be proposed before internal failure by mining:
- public postmortems and incident reports;
- court/regulatory cases and standards where applicable;
- engineering and management books/research;
- vendor and independent advisories;
- competitor/industry failures;
- internal near misses;
- threat modeling, premortem and scenario analysis;
- repeated review findings;
- insurance/audit/control requirements;
- architecture outcome data.

## Metrics

Track: violations, exceptions, near misses, losses despite compliance, losses linked to violation, prevented/avoided loss estimates, false-positive burden, cost of controls, rule age/freshness, exception frequency, time-to-close exceptions, and whether a rule remains economically justified.

## Governance rule

Never preserve a rule merely because it is old. Never remove a rule merely because no recent incident occurred. Review the causal WHY, current evidence, changed conditions, control cost and expected downside.
