# Architecture Review Board Lite v0.1

Status: DRAFT / PROVISIONAL
Owner: Architecture Governance

## Principle

Governance must reduce expensive mistakes without turning delivery into a committee process. Most decisions should be handled asynchronously by the smallest competent set of reviewers. Meetings are an exception, not the default.

## Default model

There is one Decision Owner, normally the responsible architect. FATHER prepares the decision pack, searches evidence/failure cases, checks Survival Rules and proposes the decision level. Human reviewers are requested only when their domain is materially affected.

### L1 — architect decides
Architect/Tech Lead records a short ADR and may proceed within delegated authority. No board meeting.

### L2 — one peer review
Decision Owner + one competent peer/reviewer. Review is asynchronous by default. If no material objection exists within the agreed review window, the decision may proceed according to project rules.

### L3 — targeted mini-board
Decision Owner + 2–4 relevant reviewers selected by impact. Examples: Security only when security exposure is material; Legal only for legal/regulatory/contractual impact; Economics/FinOps for material cost/TCO; Operations for material production impact; Product for material business/scope impact. Avoid inviting roles merely for ceremony.

### L4 — accountable sponsor review
Decision Owner + relevant L3 reviewers + one accountable sponsor/executive who accepts strategic residual risk. Independent review is added only when justified by uncertainty or downside.

## One-page Decision Pack

Normal review should fit on one page or structured screen:

1. Decision required.
2. WHY / architecture drivers.
3. A/B/C alternatives where meaningful.
4. Recommended option.
5. Key evidence and failure cases.
6. Cost/TCO and worst credible/expected loss.
7. Security/legal/operational impacts where applicable.
8. Capability/capacity gaps.
9. Survival Rules touched.
10. Validation/rollback/exit plan.
11. Confidence and unresolved questions.
12. Who must approve and by when.

Detailed evidence remains linked rather than copied into the meeting document.

## Objections and dissent

A reviewer should not merely write REJECT. A material objection records: claim/decision disputed, WHY, evidence or missing evidence, expected consequence, and proposed alternative/condition.

Dissenting opinion is preserved. The Decision Owner may accept a non-blocking objection with rationale. Blocking authority exists only for explicitly delegated domains/risk thresholds; otherwise disagreement escalates one level rather than creating endless discussion.

## Timeboxes

Review windows are defined by project class and urgency. Missing a review SLA must not silently become permanent approval for L3/L4 high-impact decisions. Emergency decisions may proceed only with named accountable owner, temporary validity, compensating controls and mandatory retrospective review.

## Automation / AI assistance

FATHER may automatically:
- classify likely decision level;
- identify required reviewers;
- detect missing ADR fields;
- search Evidence KB, Failure KB and Survival Rules;
- summarize contradictions;
- calculate PERT/TCO/Expected Loss scenarios;
- prepare the one-page pack;
- track review deadlines and decisions;
- schedule outcome validation;
- update knowledge after approved review.

FATHER does not invent approval. Human approval remains explicit where the matrix requires it.

## Minimal RACI

Decision Owner: Responsible + prepares recommendation.
Accountable Approver: only where L3/L4 or policy requires.
Domain Reviewer: Consulted only for material domain impact.
FATHER/agents: analysis, evidence, checks, traceability and administration.
Others: informed through the decision log, not invited by default.

## Metrics

Track review lead time, human hours spent in governance, decisions by level, rework prevented, late objections, unnecessary escalations, exceptions, decision reversals, downstream incidents/rework attributable to decisions and avoided loss.

A governance process that costs more than the risk it reduces must itself be reviewed and simplified.

## Core rule

Minimum bureaucracy, maximum traceability: the smallest competent human decision group, supported by the largest useful body of machine-prepared evidence.
