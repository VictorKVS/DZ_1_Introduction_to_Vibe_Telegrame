# Developer Algorithm & Implementation Knowledge Base v0.1

Status: DRAFT / PROVISIONAL
Owner: Engineering / Developer Intelligence

## Purpose

Provide Senior Engineer / Development Agent with a reusable, evidence-backed knowledge base for selecting implementation approaches, algorithms, data structures, libraries and optimization strategies according to the actual objective function of the task.

The KB answers not only WHAT to implement, but WHEN, WHY and UNDER WHICH CONDITIONS a specific approach is preferable.

## Core principle

No material implementation choice without:
Problem Class → Objective Function → Constraints → Candidate Methods → Evidence → Weighted Evaluation → Benchmark/Validation → Decision → Actual Outcome → Knowledge Update.

## Knowledge object: ImplementationPattern

Each reusable implementation pattern records:
- pattern_id;
- problem class;
- applicable task types;
- candidate algorithm/data structure/approach;
- preconditions;
- contraindications / anti-use cases;
- asymptotic time complexity;
- memory complexity;
- expected CPU/GPU/network/storage profile;
- energy profile where material;
- latency/throughput characteristics;
- scalability characteristics;
- determinism/reproducibility;
- numerical precision/error characteristics where applicable;
- concurrency/parallelization properties;
- security/privacy implications;
- maintainability/readability;
- implementation complexity;
- testability;
- licensing/dependency constraints;
- required developer competency;
- supporting sources;
- contradicting sources;
- reference implementations;
- external benchmarks;
- internal benchmarks;
- historical outcomes;
- confidence;
- freshness/review date.

## Objective weights

Weights SHALL be task-specific. Default weights are only priors, never universal truth.

Possible criteria:
- correctness;
- latency;
- throughput;
- CPU cost;
- GPU cost;
- memory;
- storage;
- network traffic;
- energy consumption;
- monetary cost per useful operation;
- accuracy/precision;
- completeness/search coverage;
- robustness;
- uncertainty handling;
- explainability;
- maintainability;
- developer effort;
- operational complexity;
- security;
- reliability;
- portability;
- time-to-market.

Each task creates an OptimizationProfile with weights, hard constraints and rationale.

## Example profiles

### HIGH_THROUGHPUT_ENERGY_EFFICIENT
For compute-intensive repeated work where speed and energy dominate.
Possible emphasis: throughput, joules/useful-operation, hardware utilization, cost/unit.

### EXHAUSTIVE_RESEARCH
For scenario exploration, forecasting or design-space search where quality/coverage dominates speed.
Possible emphasis: completeness, sensitivity analysis, uncertainty propagation, reproducibility, explainability and result quality.

### LOW_LATENCY_REALTIME
For interactive/real-time paths.
Possible emphasis: P95/P99 latency, bounded execution, memory, failure behavior.

### ECONOMIC_BALANCED
For ordinary product engineering.
Possible emphasis: total lifecycle cost, maintainability, sufficient performance, security, implementation effort and operational simplicity.

### SAFETY_SECURITY_CRITICAL
Correctness, failure containment, auditability and security dominate optimization convenience.

## Scientific and technical evidence

Preferred evidence may include:
- peer-reviewed papers;
- textbooks/monographs;
- standards;
- official language/runtime/library documentation;
- established algorithm references;
- independent benchmarks;
- mature open-source reference implementations;
- production postmortems;
- internal controlled benchmarks and production results.

LLM-generated explanation is not primary evidence. It may locate, compare and summarize evidence, but underlying sources are retained.

## Weighted selection

For material choices, store a decision matrix:
Candidate × Criterion → normalized score + weight + confidence + evidence.

A high weighted score is advisory, not an automatic truth. Hard constraints can eliminate a candidate regardless of score.

The system must preserve WHY the weights were chosen.

## Benchmark protocol

When theory or public evidence is insufficient, create a reproducible benchmark:
- workload/dataset;
- dataset size/distribution;
- hardware/runtime versions;
- warmup;
- repetitions;
- metrics;
- statistical summary;
- energy/cost measurement where applicable;
- source code/commit;
- environment config;
- limitations;
- result confidence.

## Developer flow

Developer receives Requirements + Architecture + Technical Design + Test Package + OptimizationProfile.

Then:
1. classify problem;
2. retrieve relevant patterns/candidates;
3. compare theory and evidence;
4. eliminate invalid candidates;
5. benchmark uncertain finalists when economically justified;
6. record Implementation Decision and WHY;
7. implement;
8. execute predesigned tests;
9. run performance/security/cost verification;
10. compare expected vs actual;
11. update KB.

## Anti-overengineering rule

Do not turn trivial CRUD/business glue into an algorithm research project. Research depth scales with impact, frequency, cost of execution, risk, uncertainty and expected lifetime.

## Learning weights

FATHER may propose updated priors from history.
Example:
Problem Class + workload characteristics + objective profile → historical performance of approaches.

The KB can learn that a method which is theoretically attractive performs poorly in our runtime, team or workload conditions.

Learned weights/recommendations must preserve dataset/context and confidence; never universalize beyond observed conditions without explicit reasoning.

## Outcome metrics

Track:
- algorithm/approach selection accuracy;
- predicted vs actual latency/throughput;
- predicted vs actual memory/energy/cost;
- defects caused by algorithm choice;
- rework caused by poor implementation decision;
- maintainability/complexity outcomes;
- benchmark prediction accuracy;
- source reliability by topic;
- pattern reuse;
- engineering hours saved;
- avoided infrastructure/energy cost;
- optimization ROI.

## Traceability

Requirement/NFR → OptimizationProfile → ImplementationPattern candidates → Sources → Implementation Decision → Tests → Code/Commit → Benchmark → Runtime Metric → Outcome → Lesson.

This turns the developer from a code generator into an evidence-informed implementation engineer whose choices improve with accumulated organizational experience.
