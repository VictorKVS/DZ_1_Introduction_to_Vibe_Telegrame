# FATHER Intelligence → Analyst → Socrates → Knowledge Pipeline v0.1

Status: DRAFT / PROVISIONAL
Owner: Knowledge & Intelligence Governance

## Purpose

Define the first production-grade knowledge acquisition loop for FATHER. The pipeline turns raw external and internal information into governed, role-specific knowledge objects without allowing collection output or an LLM summary to become truth by default.

Core sequence:

Intelligence / Reconnaissance
→ Analyst
→ Socrates / Critical Challenge
→ Knowledge Formation
→ Domain Knowledge Bases
→ Agent Working Memory / Retrieval
→ Decision / Project Use
→ Outcome Feedback
→ Knowledge Revision.

## 1. Intelligence / Reconnaissance Agent

Role: continuously discover and collect potentially useful information from approved sources.

Typical sources:
- Telegram channels and public communities;
- GitHub/GitLab repositories, issues, releases and discussions;
- official documentation and standards;
- scientific papers and books where legally accessible;
- vendor documentation/advisories;
- postmortems and incident reports;
- regulatory/legal sources;
- industry reports;
- job/vacancy signals for technology and competency demand;
- competitor/product updates;
- internal project outcomes and near misses.

The Intelligence Agent MUST preserve source provenance and raw observation separately from analysis.

Output object: Observation.

Minimum fields:
- observation_id;
- source_id;
- source_type;
- source_uri/reference;
- publication/observation time;
- retrieval time;
- raw/raw-derived hash;
- author/publisher if known;
- topic candidates;
- entities;
- language;
- collector confidence;
- access/legal notes;
- duplicate/repost relationship;
- project/domain relevance candidates.

The collector does not decide truth.

## 2. Analyst Agent

Role: convert observations into structured analytical candidates.

Functions:
- deduplicate and cluster related observations;
- separate facts, claims, opinions, forecasts and marketing assertions;
- identify entities and relationships;
- establish context and conditions of applicability;
- compare with existing FATHER Knowledge Objects;
- identify contradictions;
- identify missing evidence;
- estimate materiality and relevance;
- classify likely target knowledge domains/roles;
- identify whether a finding may affect an active project, Survival Rule, Technology Horizon, architecture pattern or risk register.

Output objects may include:
- Claim;
- Event;
- Technology Signal;
- Risk Signal;
- Competitor Signal;
- Failure Case;
- Success Case;
- Method Candidate;
- Algorithm Candidate;
- Legal/Regulatory Candidate;
- Cost/Market Signal;
- Knowledge Update Candidate.

The Analyst records WHY a source set supports a claim and does not hide contradictory evidence.

## 3. Socrates Agent

Role: adversarial but constructive challenge before knowledge publication.

Socrates asks at least:
- What exactly is being claimed?
- What evidence directly supports it?
- Is the evidence primary, secondary or hearsay?
- What is the source's incentive/bias?
- Under what conditions is the claim true?
- Under what conditions can it fail?
- Is this correlation being mistaken for causation?
- Are important alternatives missing?
- Is the benchmark representative?
- Are units, samples, dates, versions and environments comparable?
- What independent evidence exists?
- What evidence contradicts it?
- What would falsify this claim?
- What is unknown?
- What is the cost of being wrong?
- Does the claim require a domain expert or experiment?

Socrates may return:
PASS / PASS_WITH_LIMITS / NEED_MORE_EVIDENCE / CONTRADICTED / DOMAIN_EXPERT_REQUIRED / EXPERIMENT_REQUIRED / REJECT_AS_LOW_VALUE.

Socrates is not an authority source. It is a challenge mechanism.

## 4. Knowledge Formation

Only after analysis and challenge is a Knowledge Candidate transformed into a governed KnowledgeObject.

Lifecycle:
DISCOVERED
→ COLLECTED
→ ANALYZED
→ CHALLENGED
→ PROVISIONAL
→ VERIFIED
→ ACTIVE
→ REVIEW_DUE / STALE / CONTRADICTED
→ SUPERSEDED / RETIRED.

High-risk knowledge may require human/domain-expert verification before ACTIVE status.

## 5. Knowledge Domains

Knowledge is stored once at the canonical level but may be projected into domain/role views.

Initial domains:
- Product / Business Model KB;
- Business Analysis KB;
- System Analysis KB;
- Architecture KB;
- Developer Algorithm & Implementation KB;
- QA / Test Design KB;
- Security KB;
- Legal / Compliance KB;
- Economics / Finance / FinOps KB;
- Infrastructure / Cloud / Platform KB;
- DevOps / DevSecOps KB;
- Operations / SRE KB;
- Project / Delivery Management KB;
- OSINT / Source Intelligence KB;
- Competitive Intelligence KB;
- Technology Horizon KB;
- Failure / Success Case KB;
- Survival Rules KB.

A KnowledgeObject may belong to multiple domains without duplication through typed relationships/tags.

## 6. Agent Knowledge Views

Agents do not receive the entire knowledge base by default. Each agent receives a governed view based on:
- role;
- task;
- project;
- jurisdiction;
- technology stack;
- FATHER Depth;
- Decision Level;
- sensitivity/permissions;
- freshness requirements.

Example:
Senior Developer Agent working on a graph-routing task may retrieve Developer KB + Architecture constraints + relevant tests + performance evidence + security constraints, rather than all legal and product knowledge.

## 7. KnowledgeObject minimum schema

- knowledge_id;
- title;
- type;
- canonical statement/claim;
- domain_tags;
- role_tags;
- applicability;
- exclusions/known limitations;
- supporting evidence links;
- contradicting evidence links;
- provenance chain;
- confidence;
- freshness;
- valid_from / valid_until if applicable;
- jurisdiction/version/environment;
- owner;
- reviewer;
- status;
- source quality notes;
- related methods/algorithms/decisions/risks/tests;
- supersedes / superseded_by;
- usage count;
- decisions influenced;
- observed outcomes;
- estimated avoided loss/value contribution;
- next review trigger/date.

## 8. Direct Storage / Connector Behavior

The pipeline should work through direct connectors rather than manual copy/paste.

Required abstract operations:
SEARCH
→ FETCH
→ COLLECT
→ STORE_RAW
→ CREATE_OBSERVATION
→ CREATE_CLAIM
→ LINK
→ COMPARE
→ CHALLENGE
→ CREATE_KNOWLEDGE_DRAFT
→ REVIEW
→ PUBLISH
→ UPDATE
→ SUPERSEDE
→ ARCHIVE.

Initial physical stack may use:
- GitHub/Git for versioned human-readable standards, ADRs, knowledge packs and diagrams;
- PostgreSQL for canonical structured objects and relations;
- pgvector for semantic retrieval;
- object storage for source artifacts and large evidence files.

The storage backend may later change without changing the logical contract.

## 9. Priority / Economic Depth

Not every observation deserves expert analysis.

Each candidate receives triage by:
- relevance to active work;
- novelty;
- strategic value;
- potential loss if ignored;
- potential gain;
- uncertainty;
- source quality;
- cost of verification;
- expected reuse.

Low-value information may remain searchable as raw observation without becoming canonical knowledge.

## 10. Triggered routes

Examples:

New Telegram post about a vulnerability
→ collector
→ analyst identifies affected technology
→ cross-check official advisory/CVE
→ Socrates checks evidence
→ Security KB draft
→ if active project affected: alert project Security Agent / create risk/change candidate.

New GitHub library benchmark
→ analyst extracts test conditions
→ Socrates challenges vendor bias/sample/environment
→ Developer KB provisional entry
→ benchmark internally if material
→ VERIFIED result linked to Implementation Pattern.

New competitor capability
→ Competitive Intelligence KB
→ Technology Horizon comparison
→ BUILD/BUY/INTEGRATE/LEARN/WATCH recommendation candidate.

## 11. Feedback from decisions and projects

Knowledge quality is not judged only at ingestion time.

Every use may create feedback:
KnowledgeObject
→ Decision
→ Implementation
→ Test
→ Runtime / Business Outcome
→ Outcome Review
→ update confidence/applicability/weights.

If a knowledge object repeatedly leads to poor outcomes, it is automatically flagged for review even if its sources remain prestigious.

## 12. Maturity path

M0 — manual source collection and Markdown drafts.
M1 — Source Registry + Observation/Claim/Knowledge schemas.
M2 — Telegram/GitHub/Web collectors + deduplication + Analyst agent.
M3 — Socrates challenge workflow + role-specific KB routing.
M4 — direct storage connectors + automated impact routing to projects/agents.
M5 — outcome-calibrated confidence, source quality and method weights.

## 13. Core principle

Reconnaissance discovers.
Analysis structures.
Socrates challenges.
Knowledge Governance decides what may become reusable organizational knowledge.
Agents consume only the subset they need.
Outcomes continuously correct the system.
