# Knowledge Storage & Direct Connector Model v0.1

Status: DRAFT / PROVISIONAL
Owner: Knowledge Platform / Enterprise Architecture

## Purpose

FATHER must work with knowledge stores and external systems directly, in the same spirit as direct repository operations: search, read, create, update, link, version, validate and audit without forcing a human to manually copy information between systems.

The architecture therefore separates three concerns:
1. Source systems and authoritative stores.
2. FATHER Knowledge Model and graph of relationships.
3. Connector/Tool layer that performs controlled direct reads/writes.

## Core principle

Do not build one giant database containing everything.
Use a federated knowledge architecture with typed stores and a unified semantic/traceability layer.

The model should support:
- authoritative source remains authoritative;
- knowledge objects retain provenance;
- searchable normalized representations may be cached/indexed;
- graph relationships may span many systems;
- writes go back to the correct source through controlled connectors;
- every write is auditable and versioned where possible.

## 1. Storage classes

### A. Operational relational store
Suitable for strongly structured transactional entities:
Projects, requirements, decisions, risks, tests, work packages, approvals, costs, permissions, lifecycle state.

Initial candidate: PostgreSQL.

### B. Knowledge graph
Stores typed relationships among goals, requirements, decisions, evidence, technologies, people/agents, cases, tests, code, incidents and outcomes.

The graph may initially be implemented using relational edges, then moved/extended to a graph engine when scale/queries justify it.

### C. Semantic/vector index
Used for retrieval over papers, books, standards, postmortems, documentation, decisions, code/document fragments and historical cases.

Important: embeddings/search index are derived retrieval structures, not the source of truth.

### D. Object/document store
For original PDFs, images, reports, datasets, exports, diagrams, benchmark artifacts, logs and other binary/large objects.

### E. Git repositories
For versionable engineering text and machine-readable artifacts:
- standards;
- ADRs/templates;
- architecture-as-code;
- diagram source;
- policies;
- schemas;
- test definitions;
- infrastructure-as-code;
- knowledge packs that benefit from peer review/version history.

### F. Time-series / observability store
For runtime metrics, traces, logs, cost observations and benchmark measurements.

## 2. Canonical Knowledge Object

FATHER uses a common envelope around knowledge regardless of physical storage:

KnowledgeObject
- id
- type
- title/name
- domain/role
- content_ref
- source_system
- source_id/url
- version
- created_at / updated_at
- valid_from / valid_to where applicable
- jurisdiction/context
- provenance
- confidence
- freshness/review_date
- access_classification
- owner
- supported_claims
- contradicted_claims
- relationships
- usage_count
- linked_decisions
- outcomes
- supersedes / superseded_by
- checksum/content hash where useful.

## 3. Direct Connector Layer

Every supported external system exposes a controlled set of operations similar to repository tools:

DISCOVER
SEARCH
FETCH/READ
CREATE
UPDATE
LINK
COMMENT/REVIEW
VERSION/COMPARE
DELETE/ARCHIVE where allowed
EXPORT
SUBSCRIBE/WATCH where supported.

FATHER should call connectors through typed contracts, not screen scraping.

Examples of future connectors:
- GitHub / GitLab;
- Google Drive / Docs;
- Jira / Confluence;
- SharePoint;
- cloud storage;
- PostgreSQL/SQL data sources;
- S3-compatible object stores;
- observability platforms;
- CI/CD systems;
- vulnerability/security platforms;
- ERP/CRM/PLM/BIM systems;
- scientific/publication databases where licensing permits;
- standards/regulatory sources;
- internal document management systems.

## 4. Read path

User/Agent Question
→ determine required knowledge domains
→ query Knowledge Graph
→ select source systems
→ connector SEARCH/FETCH
→ normalize metadata
→ verify freshness/provenance
→ retrieve relevant content
→ produce evidence-backed result
→ store usage and trace links.

Cached/indexed content may accelerate retrieval, but important claims should remain traceable to the authoritative source.

## 5. Write path

Generated/approved artifact
→ determine authoritative target store
→ policy/permission check
→ human approval if required by decision level
→ connector CREATE/UPDATE
→ receive source ID/version
→ record KnowledgeObject/graph links
→ index for retrieval
→ audit event.

The system must never report that an artifact was saved when the connector write failed.

## 6. Repository-like Knowledge Operations

Desired UX examples:

"Find all architecture decisions that used Kafka and later exceeded cost estimates"
→ Graph + SQL + outcomes search.

"Open the source that justified ADR-084"
→ Direct source fetch.

"Update our PostgreSQL technology card with this new benchmark"
→ propose structured change → approval → direct KB update → version retained.

"Create a new Security Survival Rule from these three incident cases"
→ draft → evidence links → review → direct write to governed registry.

"Compare the current standard to the previous version"
→ version/semantic diff.

## 7. Knowledge ingestion pipeline

Source discovered
→ lawful/authorized collection check
→ fetch original
→ malware/content safety checks where applicable
→ metadata extraction
→ classification
→ deduplication
→ chunk/index generation
→ claims/entities/relations extraction
→ provenance preservation
→ confidence assignment
→ optional expert review
→ publish into Knowledge Graph/index.

Do not treat LLM-extracted claims as automatically true. They remain derived assertions linked to source evidence.

## 8. Knowledge lifecycle

NEW
→ REVIEWED
→ ACTIVE
→ REVIEW_DUE
→ STALE
→ SUPERSEDED
→ ARCHIVED.

A stale source may still be historically valuable; stale does not mean deleted.

Freshness policy depends on domain:
- algorithms/classic theory: slow-changing;
- cloud/API prices: fast-changing;
- vulnerabilities: very fast-changing;
- law/regulation: jurisdiction-dependent;
- vendor roadmap/EOL: frequently reviewed.

## 9. Access and security

Connector layer must support:
- least privilege;
- scoped credentials;
- secret management;
- tenant/project isolation;
- read/write separation;
- audit logs;
- classification labels;
- retention rules;
- legal/privacy constraints;
- source-specific permissions.

A knowledge retrieval agent must not gain write permissions simply because it can read a source.

## 10. Initial implementation strategy

Do not deploy every database class on day one.

MVP:
- GitHub for standards/docs/versioned knowledge packs;
- PostgreSQL for structured entities and edge tables;
- pgvector or equivalent for semantic retrieval;
- filesystem/S3-compatible object storage for originals;
- stable IDs and provenance in all objects.

Later add a dedicated graph database, search cluster, time-series platform or specialized stores only when measured workload justifies them.

## 11. Knowledge Store Registry

FATHER maintains a registry of all connected stores:
Store ID
→ system type
→ owner
→ purpose
→ authoritative object types
→ connector capabilities
→ read/write permissions
→ data classification
→ regions/jurisdictions
→ backup/retention
→ cost
→ SLA
→ health
→ last sync
→ dependency/exit plan.

## 12. Core rule

Knowledge is not "inside the LLM".
Knowledge lives in governed sources and stores.
FATHER discovers, connects, reasons over, links and updates that knowledge through controlled tools while preserving provenance and history.
