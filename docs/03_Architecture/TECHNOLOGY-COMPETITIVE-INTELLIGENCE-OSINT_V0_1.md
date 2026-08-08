# Technology & Competitive Intelligence / OSINT Operating Model v0.1

Status: DRAFT / PROVISIONAL
Owner: Technology Intelligence + Architecture Governance

## Purpose

Maintain a lawful, evidence-based external intelligence function that continuously supplies Product, Architecture, Security, Legal and Economics with current information about technologies, solutions, failures, competitors, prices, skills and market change.

## Intelligence domains

- architecture patterns and implementation cases;
- failure/postmortem/incident cases;
- open-source and commercial technologies;
- competitors/products/features/pricing;
- standards and regulation;
- vulnerabilities/security advisories;
- research/books/papers/conferences;
- GitHub/open-source activity;
- vendor roadmaps/EOL/deprecations;
- cloud/API/LLM/licensing prices;
- labor market, vacancies and competency demand;
- acquisitions/partnerships/ecosystem change;
- relevant patents/public technical disclosures where lawful and useful.

## Collection principles

Collection is limited to lawful, authorized/open sources and must respect access controls, privacy, contractual restrictions, intellectual property and applicable law. Do not bypass authentication, technical restrictions or collect unnecessary personal data.

Every observation records provenance, timestamp, collection method, source reliability, confidence, jurisdiction where relevant, freshness policy and links to supported/contradicted claims.

## Collection cycle

Intelligence Requirement → Source Plan → Collection → Normalization → Deduplication → Verification/Triangulation → Confidence → Analysis → Evidence/Knowledge Graph → Alert/Brief/Decision Pack → Outcome Feedback.

## Core knowledge bases

1. Evidence Source KB.
2. Architecture Patterns & Decisions KB.
3. Failure / Incident / Postmortem KB.
4. Technology Intelligence KB.
5. Competitor & Product KB.
6. Market & Price Time-Series KB.
7. Skills & Competency Market KB.
8. Security/Vulnerability KB.
9. Regulation/Standards KB.
10. Internal Production Evidence KB.

## Risk-based research depth

Research depth SHALL scale with expected decision loss and irreversibility.

Decision Research Profile records:

- decision value/exposure;
- probability and magnitude of error;
- reversibility/switching cost;
- uncertainty;
- time available;
- minimum evidence level;
- required independent sources;
- need for PoC/benchmark/expert review;
- research budget;
- Value of Information.

Low-impact reversible decisions use lightweight research. High-impact decisions with potential losses in millions require deeper triangulation, failure-case search, independent evidence, scenario/sensitivity analysis and often PoC/benchmark validation.

## Competitor record

Track only relevant, lawfully obtained business/technical signals:

- product/segment/value proposition;
- public feature/capability history;
- public pricing history;
- releases/deprecations;
- public technology/open-source signals;
- public vacancies/skill demand as strategic indicators;
- partnerships/acquisitions;
- public incidents/postmortems;
- market positioning and observable changes;
- evidence/confidence and alternative explanations.

Do not convert weak signals into factual claims.

## Intelligence deliverables

- Architecture Evidence Pack;
- Technology Radar update;
- Competitor Brief;
- Failure Case Alert;
- Price/Cost Change Alert;
- Technology EOL/Deprecation Alert;
- Security Advisory Impact Brief;
- Skill/Capacity Market Brief;
- Build/Buy/Reuse dossier;
- Migration Timing recommendation;
- periodic Technology/Market Landscape.

## Metrics

Track:

- freshness SLA compliance;
- source/evidence coverage;
- time from external event to detection;
- false-positive/false-negative rate where measurable;
- forecast calibration;
- stale evidence causing rework;
- source reputation by domain;
- intelligence reuse across projects;
- research cost;
- avoided loss;
- decisions changed by new evidence;
- migration/deprecation detected before forced action;
- price forecast error;
- competitor/market forecast error;
- value of information realized.

## Integration with Architecture Gate

For material decisions, Architecture Gate requests an Intelligence Evidence Pack. The pack must include current alternatives, supporting and contradicting evidence, relevant failure cases, technology lifecycle, market/price signals, competency availability, migration/switching cost and confidence.

After implementation, Architecture Outcome Review feeds actual results back to Intelligence KB so external claims can be compared against internal evidence.
