# Architecture Outcome Validation & Learning Loop v0.1

Status: DRAFT / PROVISIONAL — subject to OTUS review
Owner: Architecture Governance

## Principle

An architecture decision is not complete when an ADR is approved or when a system is released. It is complete only when predicted outcomes are compared with measured outcomes and the result updates organizational knowledge.

Core loop:

Architecture Driver → Alternatives → Evidence → Prediction → ADR → Implementation → Verification → Production Observation → Expected vs Actual → Causal Review → Knowledge Update → Standard/Method/Competency Update.

## 1. Prediction Baseline

Every material architecture decision SHALL record measurable predictions where applicable:

- delivery effort and schedule;
- CAPEX/OPEX/TCO;
- cloud/API/LLM/licensing cost;
- latency/throughput/capacity;
- availability/reliability/RTO/RPO;
- security and privacy risk;
- operational/support effort;
- maintainability and expected change cost;
- migration/switching cost;
- competency/capacity demand;
- expected business effect;
- assumptions, confidence intervals and uncertainty.

Predictions must be tied to evidence and the conditions under which they are expected to hold.

## 2. Validation checkpoints

Recommended checkpoints are risk-based and may include:

- implementation/design verification;
- pre-release acceptance;
- release;
- 1 month;
- 3 months;
- 6 months;
- 12 months;
- major incident;
- major scale/load change;
- technology/version migration;
- retirement/replacement.

High-impact decisions may require more frequent review. Low-impact decisions may use fewer checkpoints.

## 3. Expected vs Actual Record

For each predicted metric store:

Metric → Predicted value/range → Actual value → Variance → Confidence → Context change → Cause category → Decision impact → Corrective action.

Do not label the architect wrong when the input conditions materially changed. Separate at least:

- architecture/model error;
- estimation error;
- invalid assumption;
- requirement/scope change;
- workload/data change;
- implementation deviation;
- competency/capacity gap;
- vendor/technology change;
- external/legal/market change;
- measurement error;
- unknown cause.

## 4. Architecture Outcome Review

The review answers:

1. What did we predict?
2. What happened?
3. Which assumptions held?
4. Which assumptions failed?
5. Which evidence was strong/weak?
6. Were alternatives evaluated correctly?
7. Was the selected method appropriate?
8. Did implementation conform to the architecture?
9. What was the economic consequence of variance?
10. What should change in the ADR, pattern, standard, method, source reputation, competency model or technology status?

## 5. Decision Quality Metrics

Track separately rather than using a single simplistic score:

- performance forecast error;
- capacity forecast error;
- cost/TCO forecast error;
- schedule/effort forecast error;
- reliability forecast error;
- operational effort forecast error;
- security risk forecast quality;
- migration/switching estimate error;
- technology lifecycle forecast calibration;
- business outcome forecast error;
- rework attributable to architecture;
- incidents attributable to architecture;
- avoided loss / value created by architecture.

Metrics may be aggregated by architect, agent, team, project class, method, technology, evidence source and decision type, with safeguards against misleading comparisons.

## 6. Method effectiveness

Methods are evaluated using their downstream outcomes.

Example comparison dimensions:

Method + Project Class + Team Competency → Analysis Cost → Decision Confidence → Rework → Defects/Incidents → Forecast Accuracy → TCO/Business Outcome.

The objective is to learn when extra analysis, PoC, benchmark, ATAM/CBAM-style review, threat modeling or other methods are economically justified.

## 7. Failure and success knowledge

Both successful and failed decisions become reusable cases.

A successful case proves only that a decision worked under recorded conditions. A failure case is used to identify boundary conditions, warning signals, failure mechanisms and prevention controls.

Case records SHALL link to original WHY, evidence available at the time, missing evidence, assumptions, production observations, economic consequence and lessons.

## 8. Economic closure

Where possible calculate:

- cost of architecture/research;
- cost of implementation;
- variance cost;
- rework cost;
- incident/loss cost;
- lost revenue/opportunity cost;
- migration cost;
- avoided loss;
- value created;
- research/architecture ROI.

This allows FATHER to determine how much analysis is justified for decisions where the price of error may be millions.

## 9. Learning actions

Outcome Review may generate controlled updates to:

- Architecture Pattern KB;
- Failure Case KB;
- Evidence/Source Reputation;
- Technology Intelligence status;
- estimation coefficients;
- Architecture Methods Catalog;
- competency requirements/training;
- fitness functions/tests;
- security/legal/economic controls;
- standards and templates;
- future decision review triggers.

No standard is improved merely because an LLM suggests it. The change must preserve provenance and rationale.

## 10. Core rule

No material decision without WHY.
No WHY without evidence.
No evidence without provenance.
No prediction without later validation.
No variance without causal analysis where economically justified.
No lesson without a controlled path back into organizational knowledge.
