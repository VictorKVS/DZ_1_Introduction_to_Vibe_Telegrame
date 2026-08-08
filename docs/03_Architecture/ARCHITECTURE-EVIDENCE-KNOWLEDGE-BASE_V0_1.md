# Architecture Evidence & Technology Intelligence Knowledge Base v0.1

Status: DRAFT / PROVISIONAL — subject to OTUS review
Owner: Architecture Governance + Technology Intelligence

## 1. Principle

A material architecture decision SHALL NOT be justified only by opinion, habit, popularity or an LLM answer. It SHALL be traceable to explicit requirements and supported by verifiable evidence.

Decision chain:

Business Goal → Requirement/NFR → Architecture Driver → Candidate Options → Method of Evaluation → Evidence Sources → Decision/ADR → Implementation → Production Evidence → Outcome → Knowledge Update.

## 2. What is selected at architecture stage

Depending on project class, architecture may select or constrain:

- system topology: monolith, modular monolith, services/microservices, event-driven, serverless, hybrid;
- communication: REST, gRPC, messaging, events, streaming, batch;
- algorithms and algorithm families where they materially affect NFRs, cost, security or feasibility;
- data stores, indexing/search/vector/graph technologies and caching;
- consistency, transaction and synchronization approaches;
- integration bridges/adapters/gateways and external interfaces;
- queues/brokers/event buses;
- deployment/runtime/container/orchestration patterns;
- cloud/on-prem/hybrid infrastructure;
- IAM, trust boundaries and security mechanisms;
- resilience, backup/DR, observability and operational approaches;
- build/buy/reuse decisions and major third-party components.

Detailed implementation algorithms may remain for Technical Design/Engineering. The architect owns algorithmic decisions when they change architecture drivers, capacity, security, cost, data model, interfaces, scalability or technology lock-in.

## 3. Evidence Source Registry

Every reusable source receives a SourceRecord.

Required fields:

- source_id;
- title;
- source_type;
- author/organization;
- publisher/vendor;
- publication/version date;
- URL/DOI/ISBN/repository reference where applicable;
- access date;
- technology/domain tags;
- claims supported;
- evidence level;
- independence/conflict-of-interest notes;
- applicability conditions;
- freshness policy;
- last verified date;
- next review date;
- status: ACTIVE / REVIEW_DUE / STALE / SUPERSEDED / RETIRED;
- supersedes/superseded_by;
- linked decisions, standards, methods and technologies.

Source types include: STANDARD, REGULATION, BOOK, PEER_REVIEWED_PAPER, TECHNICAL_PAPER, OFFICIAL_DOCUMENTATION, VENDOR_BENCHMARK, INDEPENDENT_BENCHMARK, INCIDENT_REPORT, CASE_STUDY, GITHUB_PROJECT, MARKET_REPORT, PRICE_LIST, JOB_MARKET_DATA, INTERNAL_EXPERIMENT, INTERNAL_BENCHMARK, PRODUCTION_METRIC, LESSON_LEARNED, EXPERT_REVIEW.

## 4. Evidence hierarchy and scoring

Evidence is contextual; no source type is universally superior. Record at minimum:

- authority;
- independence;
- reproducibility;
- relevance to our workload;
- recency;
- sample/data quality;
- methodological transparency;
- conflict-of-interest risk;
- confidence.

Vendor claims SHALL be marked as vendor evidence. LLM output is not primary evidence; it may discover, summarize or challenge evidence, but the underlying source must be retained.

## 5. Architecture Decision Evidence Pack

Every material ADR SHALL link an Evidence Pack containing:

- decision question;
- requirements/NFRs and constraints;
- candidate options;
- evaluation method;
- sources for each material claim;
- contradictory evidence;
- assumptions;
- benchmark/PoC results where needed;
- security/legal/economic evidence;
- capability and capacity evidence;
- technology maturity and market evidence;
- cost/TCO and migration evidence;
- confidence and uncertainty;
- decision expiry/review triggers.

If evidence is insufficient, status is EVIDENCE_GAP rather than silently assuming certainty.

## 6. Internal evidence

FATHER SHALL treat its own measured results as first-class evidence:

Estimate → Actual effort/cost → Performance → Defects → Incidents → Availability → Security findings → Operational cost → Business outcome.

InternalEvidence records environment, dataset/workload, versions, test method, hardware/cloud configuration, date, raw result location, reproducibility instructions and confidence.

Internal evidence must not be generalized beyond its tested conditions without an explicit inference.

## 7. Technology Intelligence Record

Each material technology/component receives a TechnologyRecord:

- category and use cases;
- current version/release cadence;
- lifecycle: RESEARCH / ASSESS / TRIAL / ADOPT / STANDARD / LEGACY / RETIRE;
- architecture fit;
- supported platforms;
- license and legal constraints;
- security history/advisories;
- maintenance/community health;
- ecosystem/integrations;
- required competencies;
- labor-market availability;
- training/onboarding cost;
- infrastructure/resource requirements;
- current acquisition/subscription/API/cloud cost;
- expected operating cost;
- switching/migration cost;
- vendor lock-in/portability;
- replacement candidates;
- market adoption signals;
- market demand/job signals;
- price trend;
- expected availability/support horizon;
- forecast scenarios and confidence;
- evidence links;
- last verified/next review.

Forecasts SHALL be expressed as scenarios/probabilities with evidence and uncertainty, never as facts.

## 8. Price and market history

Prices are time-series evidence, not a static field.

PriceObservation:

Technology/Service + Provider + Region + SKU/Tier + Currency + Unit + Price + Tax inclusion + Contract assumptions + ObservedAt + Source + ValidUntil.

MarketObservation may track release activity, contributor activity, security advisories, job postings/skill demand, cloud/vendor availability, ecosystem integrations, community adoption and deprecation signals.

This enables trend and migration calculations rather than relying on today's price/popularity.

## 9. Freshness and review engine

Every source/technology has a review policy based on volatility and criticality.

Examples:

- regulation/security advisory/high-volatility cloud/API pricing: frequent review;
- active framework/library: release/event-driven plus scheduled review;
- standards/books/fundamental algorithms: slower periodic review;
- internal benchmark: review when workload, version, architecture or infrastructure changes.

Events that trigger review include new major release, deprecation/EOL, critical vulnerability, license change, major price change, vendor acquisition/closure, market support decline, architecture/NFR change, incident, failed fitness function, or materially better alternative.

## 10. Knowledge graph relationships

Recommended graph edges:

SOURCE SUPPORTS/CONTRADICTS CLAIM
CLAIM JUSTIFIES DECISION
DECISION SATISFIES REQUIREMENT
DECISION USES TECHNOLOGY
TECHNOLOGY REQUIRES COMPETENCY
TECHNOLOGY CONSUMES INFRASTRUCTURE
TECHNOLOGY HAS_PRICE OBSERVATION
TECHNOLOGY HAS_MARKET_SIGNAL OBSERVATION
DECISION VERIFIED_BY TEST/PRODUCTION_METRIC
OUTCOME CONFIRMS/WEAKENS DECISION
LESSON UPDATES SOURCE/METHOD/STANDARD/TECHNOLOGY_STATUS.

## 11. Quality metrics for the knowledge base

Track:

- evidence coverage of material ADR claims;
- percentage of sources within freshness SLA;
- stale/superseded source rate;
- contradictory-evidence coverage;
- decisions with internal validation;
- forecast calibration over time;
- technology price forecast error;
- market/adoption forecast error;
- source reuse across projects;
- decisions later reversed due to poor/outdated evidence;
- hours saved by reusable evidence;
- cost of maintaining evidence vs avoided rework/loss.

## 12. Governance

Roles: Knowledge Curator, Technology Scout/OSINT Agent, Architect, Security, Legal, Economist/FinOps, Domain Expert and Human Decision Owner.

Agents may collect and normalize evidence, detect staleness and propose updates. Material decisions, source trust changes and high-impact forecasts require accountable review according to project risk.

## 13. Architecture gate addition

Architecture Gate SHALL fail or become CONDITIONAL when a material decision lacks:

1. traceability to architecture drivers;
2. considered alternatives;
3. evaluation method;
4. evidence references;
5. cost/TCO and switching impact where material;
6. security/legal impact where applicable;
7. capability/capacity feasibility;
8. uncertainty/confidence;
9. validation plan/fitness function;
10. review trigger.

This converts architecture from opinion-driven design into evidence-informed engineering while preserving human judgment under uncertainty.
