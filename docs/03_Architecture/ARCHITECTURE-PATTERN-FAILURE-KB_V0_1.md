# Architecture Pattern & Failure Knowledge Base v0.1

Status: DRAFT / PROVISIONAL — subject to OTUS review
Owner: Architecture Governance + Knowledge Management + Technology Intelligence

## Purpose

Create a reusable, evidence-backed knowledge base of successful architecture patterns, anti-patterns, failures, boundary conditions and lessons so new architecture decisions can be compared against both positive and negative historical examples.

## Core principle

Success shows that a solution can work under recorded conditions. Failure often reveals the boundaries where it stops working. Both are first-class evidence.

## 1. Pattern Record

Required fields:

- pattern_id;
- name;
- category;
- problem class;
- context/applicability conditions;
- architecture drivers addressed;
- known benefits;
- known trade-offs;
- known failure modes;
- required competencies;
- required infrastructure/capacity;
- expected cost/TCO characteristics;
- security/legal implications;
- implementation complexity;
- migration/switching considerations;
- supporting evidence;
- contradicting evidence;
- successful internal cases;
- failed/problematic internal cases;
- external cases;
- confidence;
- lifecycle/status;
- review triggers.

## 2. Failure Case Record

Required fields:

- failure_case_id;
- title;
- source and provenance;
- organization/project anonymization where required;
- original problem and context;
- original architecture decision;
- original WHY / ADR;
- evidence available at decision time;
- missing/ignored evidence;
- assumptions;
- early warning signals;
- failure mechanism;
- triggering event;
- direct financial loss;
- downtime loss;
- lost revenue / lost margin;
- rework and recovery cost;
- legal/security/reputation consequence;
- time-to-detect;
- time-to-recover;
- root cause(s);
- contributing factors;
- competency/capacity gaps;
- prevention/detection controls;
- architectural alternative that could have reduced impact;
- lessons;
- standards/patterns updated;
- confidence and evidence quality.

Unknown monetary values use 0 + NOT_ESTIMATED rather than FREE/NO_LOSS.

## 3. Anti-Pattern Record

Anti-patterns are recurring approaches that appear attractive but historically create predictable costs, risks or defects under specific conditions.

Fields include symptom, why it looks attractive, boundary conditions, failure mechanism, leading indicators, typical economic consequence, examples, detection rules, safer alternatives and evidence.

## 4. Case similarity model

Before approving a material ADR, FATHER SHOULD search for similar prior cases using dimensions such as:

- project/domain class;
- scale/load;
- data volume/velocity;
- integration count/type;
- consistency requirements;
- availability/RTO/RPO;
- security/regulatory level;
- team size and competency;
- infrastructure model;
- technology stack;
- budget/timeline constraints;
- organizational maturity;
- migration constraints.

Similarity output must explain which factors match and which differ. Similarity is evidence aid, not proof.

## 5. Architecture Review use

An Architecture Evidence Pack for a material decision SHOULD include:

- relevant successful patterns;
- relevant anti-patterns;
- similar failure cases;
- differences in context;
- external evidence;
- internal evidence;
- expected loss if known failure mode recurs;
- mitigations or reasons the failure mode is not applicable.

## 6. Learning from outcomes

Architecture Outcome Review can create or update Pattern/Failure records.

Decision → Prediction → Actual → Variance → Cause → Success/Failure Classification → Pattern/Anti-pattern/Failure update.

A pattern's confidence increases only when outcomes support it under clearly described conditions. Contradictory outcomes reduce confidence or narrow applicability.

## 7. Failure economics

Failure cases SHOULD capture monetary impact using the shared economic risk model:

Direct Loss + Recovery Cost + Downtime Loss + Lost Margin + Cost of Delay + Legal/Security Cost + Opportunity Cost + Migration/Rework Cost.

The knowledge base can then rank failure modes by expected loss, not by narrative severity alone.

## 8. Source types

Useful sources include public postmortems, incident reports, engineering blogs, conference talks, books, research papers, standards, GitHub issues/retrospectives, vendor/customer case studies, independent analyses, internal incidents, internal project retrospectives and production metrics.

Vendor or promotional material must be marked and triangulated where material.

## 9. Metrics

Track:

- number of reusable pattern records;
- number of failure cases;
- evidence freshness;
- case reuse in ADRs;
- ADRs changed after failure-case review;
- repeated failures that already existed in KB;
- failure recurrence rate;
- avoided loss attributable to reused lessons;
- time saved by reusable pattern evidence;
- pattern prediction accuracy;
- anti-pattern detection precision/recall where measurable;
- economic value of the knowledge base.

## 10. Governance

Agents may discover, summarize, classify and link cases. High-impact failure conclusions and economic loss estimates require accountable human review when uncertainty or reputational/legal risk is material.

Cases involving persons or organizations must respect lawful processing, minimization, confidentiality and correction requirements.

## 11. Core rule

Do not ask only: "Where has this worked?"
Also ask: "Where has this failed, why, under what conditions, how early could we have known, and how expensive was the mistake?"
