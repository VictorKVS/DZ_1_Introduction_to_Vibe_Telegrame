# FATHER Architecture Views Catalog v0.1

Status: DRAFT
Owner: Architecture Governance

## Purpose

Defines the mandatory and optional architecture views used to explain, verify, estimate and govern a solution. A view is not decorative documentation. Every view must answer a stakeholder question, support a decision, reduce a known risk, enable verification, or improve handover.

## General rules

Each view SHALL record:
- View ID and type;
- stakeholder/audience;
- question answered;
- source requirements/NFRs/ADRs;
- method/notation;
- owner/reviewer;
- required evidence;
- update trigger;
- quality criteria;
- related tests/fitness functions;
- security/legal/economic implications where relevant.

Views may be merged for small systems, but required information may not disappear.

## AV-001 System Context View

Question: what is the system, who/what interacts with it, and where is its boundary?

Shows users, external organizations, external systems, major data flows, trust assumptions and boundary.

Primary audience: Product, BA, System Analyst, Architect, Security, Legal.

Quality criteria: boundary explicit; all material external actors represented; no hidden critical integration; flows traceable to requirements.

## AV-002 Container / Application View

Question: what major deployable/runtime building blocks compose the solution?

Shows applications/services, databases, queues, external dependencies and principal protocols.

Primary audience: Architects, Developers, DevOps, QA, Security.

Quality criteria: responsibilities non-overlapping enough to reason about; ownership and deployment unit clear; dependencies justified.

## AV-003 Component View

Question: how is a container/service internally decomposed for implementation and change impact?

Shows modules/components, responsibilities, dependencies and contracts.

Required for complex/high-risk containers; optional for simple components.

Quality criteria: aligns with code/package boundaries or explicit target design; cyclic dependencies identified; critical components linked to tests and requirements.

## AV-004 Domain & Data View

Question: what information exists, who owns it, how is it related and what is its lifecycle?

Shows domain entities, aggregates where useful, schemas, data ownership, classification, retention, lineage, versioning and key constraints.

Quality criteria: authoritative source identified; lifecycle and retention known; sensitive data marked; duplication/master-data decisions explicit.

## AV-005 Integration View

Question: how do systems exchange data and what happens when dependencies fail?

Shows interfaces, APIs/events/files, protocols, sync/async choice, schemas, ownership, SLAs, retries, idempotency, versioning and failure handling.

Quality criteria: every material integration has contract, owner, error behavior, security controls and test strategy.

## AV-006 Sequence / Interaction View

Question: how does a critical scenario execute across components over time?

Used for critical business flows, complex distributed interactions, authentication/authorization flows and failure/recovery paths.

Quality criteria: happy path and material failure path shown; ordering/transaction boundaries clear; timeouts/retries visible where relevant.

## AV-007 Deployment View

Question: where does each runtime component execute?

Shows environments, hosts/nodes/containers/cloud services, regions/zones, scaling groups, external dependencies and deployment topology.

Quality criteria: maps every deployable component to environment; capacity assumptions traceable; production/non-production separation explicit.

## AV-008 Network & Trust Boundary View

Question: how is network connectivity segmented and where do trust levels change?

Shows zones, subnets/VPC/VNet segments, ingress/egress, firewalls/gateways, trust boundaries, exposed services and protected management paths.

Quality criteria: all externally reachable paths explicit; default-deny/allowed-flow assumptions documented; admin paths distinguished; flows tied to security controls.

## AV-009 IAM / Authorization View

Question: who can do what, through which identity, and under which policy?

Shows users/services, identity providers, roles, permissions, service identities, MFA, privileged access, authorization points and audit trails.

Quality criteria: least privilege review possible; privilege escalation paths considered; human/service identities separated; critical actions auditable.

## AV-010 Security Architecture View

Question: how does the design address identified threat scenarios and security requirements?

Shows assets, trust boundaries, attack surfaces, key controls, crypto points, secrets, detection, protective mechanisms and residual-risk ownership.

Quality criteria: controls trace to threats/requirements; no control exists only as narrative without implementation/test target; residual risks explicit.

## AV-011 Availability / Resilience / DR View

Question: how does the system survive component/site/provider failures?

Shows failure domains, redundancy, failover, backups, restore paths, dependencies, RTO/RPO, degradation modes and disaster recovery.

Quality criteria: RTO/RPO trace to business need; backup is paired with restore testing; single points of failure visible; degraded mode defined where needed.

## AV-012 Capacity & Performance View

Question: what load must the system sustain and what resources are required?

Shows workload model, throughput, concurrency, latency targets, storage growth, compute/memory/GPU/network estimates, headroom and scaling thresholds.

Quality criteria: assumptions explicit; peak/normal growth scenarios included; capacity linked to infrastructure cost and performance tests.

## AV-013 Observability & Operations View

Question: how will operators know whether the system works and how will incidents be diagnosed?

Shows logs, metrics, traces, events, dashboards, SLI/SLO, alerts, ownership, runbooks and audit streams.

Quality criteria: critical user journeys observable end-to-end; alert has owner/action; telemetry retention/cost defined; security monitoring integrated.

## AV-014 CI/CD & Supply Chain View

Question: how does source become a trusted release?

Shows repositories, branches/PRs, build pipeline, tests, SAST/SCA/secrets/SBOM/container/IaC scans, artifact registry, signing/provenance, environments and release approvals.

Quality criteria: no undocumented production path; required gates machine-enforced where possible; artifact traceable to source commit and test evidence.

## AV-015 Infrastructure View

Question: what infrastructure capabilities are required, how are they provisioned and protected?

Shows compute, storage, network, DB/platform services, IaC boundaries, configuration baselines, backup/DR, monitoring and cost drivers.

Quality criteria: every infrastructure component exists because of workload/requirement; owner/provider/capacity/cost/security posture known or NOT_ESTIMATED.

## AV-016 Cost / Economic View

Question: where does the architecture create cost and economic value?

Shows CAPEX/OPEX, cloud/API/LLM/storage/network/license/labor/security/legal/support costs, major cost drivers, scaling curves, TCO and cost-of-change/migration candidates.

Quality criteria: unknown cost is explicit NOT_ESTIMATED; alternatives comparable; major NFRs tied to economic impact where possible.

## AV-017 Technology Lifecycle & Portability View

Question: what happens when a technology/provider changes or must be replaced?

Shows critical technologies, lifecycle state, vendor lock-in, standards/contracts used, export/migration path, replacement candidates, migration dependencies and review triggers.

Quality criteria: strategic dependencies explicit; no critical provider without exit assumption for systems requiring portability; migration cost candidate recorded.

## AV-018 Compliance / Jurisdiction View

Question: which technical elements are affected by legal, regulatory or contractual obligations?

Shows data location, regulated flows, retention, processors/providers, jurisdiction boundaries, mandatory controls, prohibited operations and human approval points.

Quality criteria: obligation source cited in project evidence; requirement/control traceability exists; legal assumptions not silently converted to facts.

## AV-019 Testability / Fitness Function View

Question: how will architecture qualities be continuously verified?

Maps architectural characteristics to automated/manual checks: latency, dependency rules, security controls, resilience, schema compatibility, cost thresholds, DR restore tests, observability and other fitness functions.

Quality criteria: every critical architecture driver has a verification mechanism or explicit reason why not.

## AV-020 Change Impact View

Question: what could be affected if a requirement, technology, component, law or interface changes?

Shows dependency/trace graph across requirement → ADR → component → data/API → infrastructure → security control → test → cost → operational process.

Quality criteria: enables regression scope and cost/time estimate; critical hidden dependencies are findings.

## View selection profile

Not every project needs every diagram at full detail. The architect creates a View Applicability Matrix with values REQUIRED, OPTIONAL, NOT_APPLICABLE and justification.

Mandatory baseline for most non-trivial software systems:
- AV-001 Context;
- AV-002 Container/Application;
- AV-004 Data;
- AV-005 Integration;
- AV-007 Deployment;
- AV-008 Network/Trust Boundaries;
- AV-009 IAM;
- AV-010 Security;
- AV-012 Capacity/Performance;
- AV-013 Observability;
- AV-014 CI/CD Supply Chain;
- AV-016 Economic;
- AV-019 Fitness Functions.

## View quality metrics

Track:
- downstream questions caused by missing/ambiguous view information;
- architecture handover rejection rate;
- view rework hours;
- defects/incidents linked to missing architecture information;
- percentage of critical requirements/NFRs represented and verified;
- outdated-view age after material change;
- automation ratio for generated/validated views;
- reuse of view templates/patterns;
- time/cost to produce each view;
- realized value: avoided rework, defects, incidents or migration cost.

## Learning loop

Project class + selected views + method/notation + architect competency + production effort + downstream rework/defects + operational outcome → update view applicability rules, templates, method recommendations, estimation coefficients and competency model.
