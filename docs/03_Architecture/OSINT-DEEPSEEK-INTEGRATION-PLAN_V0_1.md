# OSINT DeepSeek Completion & FATHER Integration Plan v0.1

Status: DRAFT / ACTIVE DESIGN
Owner: FATHER Knowledge Intelligence
Source donor: `VictorKVS/OSINT_deepseek`

## Goal

Complete the existing OSINT_deepseek project as a reusable OSINT Collection & Analysis service and integrate it into FATHER through a stable connector/API boundary.

The donor project already contains a local agent runtime, Ollama integration, agent tracking, resource monitoring, crash handling, safe model modes and an LLM gateway. These assets should be preserved where useful rather than rewritten blindly.

## Architectural rule

OSINT_deepseek SHALL NOT become an inseparable internal module of FATHER. It should operate as a replaceable service/plugin with stable contracts.

`Sources → OSINT_deepseek → normalized observations/claims → FATHER Knowledge Ingestion → Analyst → Socrates → KnowledgeObject`

## Target capabilities

### 1. Source registry
Store source metadata: stable source ID, type, URL/identifier, domain, trust profile, bias/affiliation, collection method, priority, polling policy, last success, legal/ToS notes and owner.

Initial source types:
- Telegram public channels/groups accessible under lawful account/API use;
- GitHub repositories/releases/issues;
- RSS/Atom;
- websites/news/vendor advisories;
- standards/regulator pages;
- papers/preprints/publication feeds.

### 2. Collectors
Collectors produce raw immutable observations with provenance. Collection and reasoning are separated.

Each observation stores at minimum:
`observation_id, source_id, source_item_id, fetched_at, published_at, raw_uri/hash, text/content reference, language, collector_version`.

### 3. Telegram watcher
Add a dedicated Telegram collector/watch service with:
- allow-listed channels only;
- incremental message cursor/checkpoint;
- duplicate/repost detection;
- edited/deleted message handling where observable;
- attachment/link metadata;
- rate limiting/retry/backoff;
- explicit credentials outside Git;
- channel health and last-seen metrics.

The watcher must collect only sources/accounts the operator is authorized to access and must not attempt access-control bypass.

### 4. Normalization & deduplication
Convert heterogeneous inputs into a common Observation schema. Cluster exact/near duplicates, reposts and syndicated copies while retaining source lineage.

### 5. Event / Claim extraction
DeepSeek or another configured model may extract candidate entities, events, claims, dates, technologies, risks, organizations and relationships. Model output is PROVISIONAL and never treated as evidence by itself.

### 6. Source and claim scoring
Maintain separate values for:
- source reliability/history;
- claim confidence;
- corroboration count;
- recency/freshness;
- relevance to active projects/Knowledge Domains;
- novelty;
- potential impact.

Do not hide all factors in a single opaque score.

### 7. Analyst handoff
Candidate claims enter the FATHER Analyst stage with supporting and contradicting sources, provenance and unresolved questions.

### 8. Socrates challenge
Socrates tests assumptions, missing context, vendor bias, alternative explanations, stale evidence, contradictions and falsification criteria before knowledge can move to VERIFIED status.

### 9. FATHER connector
Expose stable service operations such as:
`health`, `source.search`, `source.upsert`, `collect.run`, `observation.search`, `observation.fetch`, `claim.search`, `claim.export`, `watch.start/stop/status`, `metrics`.

Integration output should support the FATHER KnowledgeObject schema and direct linking to Project, Requirement, ADR, Risk, Technology Horizon, Competitor, Failure Case and Survival Rule.

## What to reuse from current OSINT_deepseek

Current repository elements to evaluate and reuse:
- `core/agent_tracker.py` — execution/agent telemetry;
- `core/logger.py` — system/resource telemetry;
- `run.py` — launcher and safe-mode concepts;
- `scripts/deepseek_safe.py` — local safe reasoning mode;
- `scripts/smart_agent.py` — orchestration patterns;
- `scripts/rtx3060_agent.py` — local hardware-aware profile;
- `services/llm-gateway/` — model abstraction boundary;
- crash/stress tooling — resilience tests and hardware protection.

These are donor assets, not automatically production-ready modules.

## Missing major modules

To reach FATHER-ready state, add:
- configuration/settings layer;
- source registry and persistent storage;
- Telegram collector;
- web/RSS/GitHub collectors;
- normalized schemas;
- deduplication;
- provenance store;
- claim/event extraction;
- scoring and corroboration;
- REST/service API;
- authentication/authorization for write operations;
- tests;
- CI/CD;
- secrets management;
- structured logs/metrics;
- export adapter to FATHER Knowledge Ingestion.

## Suggested first implementation stack

Keep the first version small:
- Python 3.12+;
- FastAPI for service API;
- Pydantic models;
- PostgreSQL for registry/observations/claims;
- pgvector only when semantic dedup/search is justified;
- object/file storage for large raw artifacts;
- Ollama/DeepSeek behind the existing or revised LLM gateway;
- Telethon or another maintained Telegram client library for authorized Telegram collection;
- pytest;
- Ruff/Black or equivalent formatting/linting;
- Bandit/Semgrep/SCA/secrets scanning in CI.

## Delivery sequence

M0 — repository audit and cleanup.
M1 — schemas + config + storage + source registry.
M2 — Telegram watcher MVP with checkpoints and raw provenance.
M3 — normalization/deduplication + claim extraction.
M4 — Analyst/Socrates export contract.
M5 — FATHER connector + KnowledgeObject linking.
M6 — dashboards/metrics, source quality history and continuous learning.

## Test-before-code rule

Before implementing each collector/service, define tests for:
- source authentication/configuration;
- incremental collection and checkpoints;
- duplicates/reposts;
- rate limits/network failures;
- malformed content;
- provenance integrity;
- restart recovery;
- secret leakage prevention;
- model output schema validation;
- FATHER export contract.

## Integration outcome

FATHER should be able to ask:
`Find new evidence about technology X since last review, show corroboration/contradictions, create PROVISIONAL KnowledgeObjects and link them to ADR/Risk/Horizon Y.`

OSINT_deepseek performs collection and first-pass extraction; FATHER governs truth status, decisions and knowledge lifecycle.
