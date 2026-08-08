# OSINT + Analyst + Socrates Knowledge Ingestion Pipeline v0.1

Status: DRAFT / PROVISIONAL
Owner: Knowledge Intelligence

## Purpose

Create a governed pipeline that discovers external/internal knowledge, evaluates it, challenges weak claims, normalizes it into reusable KnowledgeObjects, and writes approved knowledge directly into FATHER-managed stores.

## Roles

### OSINT Specialist / Scout Agent
Responsible for source discovery and collection from lawful, authorized/open sources.

Typical targets:
- scientific papers, books and standards;
- official documentation;
- GitHub/GitLab projects and release history;
- public postmortems, incidents and failure cases;
- vendor and independent benchmarks;
- market/pricing/job-skill signals;
- competitor products, public architecture disclosures and roadmaps;
- regulations and official guidance;
- internal repositories, approved reports and production evidence.

The Scout does not decide truth. It collects candidates with provenance.

### Analyst Agent
Transforms collected material into structured claims and context.

Responsibilities:
- deduplicate;
- classify source type;
- extract supported claims;
- identify applicability conditions;
- detect contradictions;
- compare candidate methods/technologies;
- estimate confidence and freshness;
- link claims to existing requirements, decisions, patterns, failures and technologies;
- identify evidence gaps.

### Socrates / Critical Review Agent
Acts as adversarial reviewer before knowledge becomes trusted organizational memory.

Questions include:
- What exactly is claimed?
- What evidence supports it?
- Is the source independent?
- Under what conditions is the claim valid?
- What would falsify it?
- Are there contradictory sources?
- Is this correlation, benchmark artifact or causal evidence?
- Is the sample/workload relevant to us?
- Is the source stale or superseded?
- What assumptions are hidden?
- What happens if the claim is wrong?
- What confidence is justified?

Socrates may downgrade, reject, request more evidence or escalate to a domain expert/research cycle.

## Pipeline

Intelligence Requirement
→ Source Plan
→ OSINT Collection
→ Provenance Capture
→ Parsing / Normalization
→ Analyst Claim Extraction
→ Similarity / Duplicate Check
→ Contradiction Search
→ Socratic Challenge
→ Confidence / Applicability / Freshness
→ Human or Domain Review when required
→ KnowledgeObject Creation
→ Direct Write to appropriate store
→ Index / Graph Link / Version
→ Usage tracking
→ Outcome feedback
→ Re-review / retirement.

## Knowledge states

DISCOVERED — raw candidate found.
PARSED — normalized metadata available.
ANALYZED — claims/context extracted.
CHALLENGED — Socratic review completed.
PROVISIONAL — usable with explicit uncertainty.
VERIFIED — sufficient evidence for defined scope.
CONTRADICTED — important conflict exists.
STALE — freshness SLA exceeded.
SUPERSEDED — replaced by newer knowledge.
RETIRED — intentionally removed from active use.

## Direct write model

Agents should be able to work with stores through connectors, not by asking humans to copy/paste.

Typical actions:
SEARCH → FETCH → CREATE_DRAFT → LINK → COMPARE → UPDATE → REQUEST_REVIEW → PUBLISH → SUPERSEDE → ARCHIVE.

Writes are policy-controlled:
- raw discoveries may be written automatically to staging;
- trusted KB updates require rule-based review depending on impact;
- Survival Rules, legal/security controls and high-impact decision guidance require explicit accountable approval;
- immutable provenance and version history are preserved.

## Storage routing

Git/GitHub:
- standards, ADRs, policies, diagrams-as-code, test definitions, knowledge packs.

PostgreSQL:
- structured KnowledgeObjects, claims, metadata, confidence, relationships, usage and review state.

pgvector/vector index:
- semantic retrieval of knowledge objects and source chunks.

Object storage:
- papers, reports, datasets, benchmark artifacts, archived source snapshots where legally permitted.

Knowledge graph:
- SOURCE SUPPORTS/CONTRADICTS CLAIM;
- CLAIM APPLIES_TO CONTEXT;
- CLAIM JUSTIFIES DECISION;
- DECISION PRODUCES OUTCOME;
- OUTCOME CONFIRMS/WEAKENS CLAIM;
- FAILURE UPDATES RULE/PATTERN/METHOD.

## Source and claim scoring

Do not use one opaque truth score. Preserve dimensions such as:
- authority;
- independence;
- methodological transparency;
- reproducibility;
- relevance;
- recency;
- sample/workload fit;
- contradiction status;
- conflict of interest;
- internal confirmation;
- consequence if wrong.

## Escalation

If confidence is low and expected loss is low, retain as PROVISIONAL.
If confidence is low and expected loss is material, request more evidence, benchmark, PoC or domain expert.
If sources strongly conflict, preserve both and mark the unresolved decision boundary.
If a new source contradicts an ACTIVE Survival Rule or major standard, do not silently update; create a review proposal.

## Continuous operation

The pipeline is permanent, not a one-time migration. It should periodically or event-driven:
- discover new versions/releases;
- detect EOL/deprecations;
- detect changed prices/licensing;
- re-check cited URLs/sources;
- identify stale knowledge;
- ingest new internal outcomes;
- recalibrate source reputation;
- propose KB updates.

## Metrics

Track:
- candidate sources discovered;
- percentage accepted/rejected;
- duplicate rate;
- contradiction discovery rate;
- stale knowledge rate;
- time from external change to KB update;
- analyst/Socrates human review hours;
- knowledge reuse count;
- decisions influenced;
- later corrections/retractions;
- source reputation by domain;
- avoided loss/value attributed to knowledge;
- ingestion cost per useful KnowledgeObject.

## Core rule

OSINT finds.
Analyst structures.
Socrates doubts.
Domain experts resolve high-impact uncertainty.
FATHER stores, links, versions and learns from outcomes.
