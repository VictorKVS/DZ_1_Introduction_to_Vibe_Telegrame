# Architecture Methods Catalog v0.1

Status: PROVISIONAL / TO BE REVIEWED AFTER OTUS ARCHITECTURE MODULE
Owner: Architecture Governance

## Purpose

Catalog methods that architects may use to understand a problem, compare alternatives, design a solution, validate quality attributes, assess risks and prepare a decision. The catalog is deliberately provisional: future OTUS lessons and project evidence may add, remove or change methods.

A method is not mandatory because it is fashionable. It is used when its expected decision value exceeds its cost and complexity.

## Method record

Every method SHALL eventually have:

- method_id;
- name;
- problem classes / applicability;
- objective;
- prerequisites / required inputs;
- required competencies;
- participants;
- typical duration / O-M-P / PERT range;
- tools;
- produced artifacts;
- decisions supported;
- limitations / failure modes;
- Quality/Security/Legal/Economic relevance;
- evidence quality;
- historical use count;
- average effort/cost;
- rework/downstream defects associated with use/non-use;
- outcome correlation;
- recommendation status: ADOPT / TRIAL / ASSESS / HOLD;
- review trigger.

## Provisional method families

### 1. Architecture communication and decomposition

- M-ARC-001 C4 Model — context/container/component/code level communication.
- M-ARC-002 UML selective use — sequence/state/component/deployment where it adds clarity.
- M-ARC-003 SysML selective use — systems with broader physical/organizational boundaries.
- M-ARC-004 Domain-Driven Design / bounded contexts — complex domain decomposition.
- M-ARC-005 Event Storming — collaborative exploration of domain events, commands, policies and boundaries.

### 2. Quality attributes and trade-offs

- M-ARC-010 Quality Attribute Scenarios — measurable stimulus/environment/response/measure specification.
- M-ARC-011 ATAM-style trade-off analysis — identify sensitivity points, trade-offs and architectural risks.
- M-ARC-012 CBAM-style economic prioritization — connect architectural strategies with costs and benefits where useful.
- M-ARC-013 Weighted Decision Matrix — compare alternatives against explicit weighted criteria.
- M-ARC-014 Architecture Fitness Functions — executable or measurable constraints that continuously validate architecture.

### 3. Decision and uncertainty

- M-ARC-020 ADR — capture context, alternatives, decision, rationale and consequences.
- M-ARC-021 PERT / three-point estimation — estimate uncertain engineering work.
- M-ARC-022 Scenario Analysis — compare alternative futures, loads, failures or business conditions.
- M-ARC-023 Sensitivity Analysis — determine which assumptions/parameters most change the decision.
- M-ARC-024 Value of Information — decide whether more research/prototyping is worth its cost.
- M-ARC-025 Proof of Concept / Spike — reduce high-impact technical uncertainty before commitment.

### 4. Security and trust

- M-ARC-030 Threat Modeling — identify assets, trust boundaries, threats and mitigations.
- M-ARC-031 STRIDE — structured threat prompts for software/system design.
- M-ARC-032 Abuse/Misuse Cases — describe malicious/undesired behavior and protections.
- M-ARC-033 Attack Surface Review — identify exposed interfaces and privilege transitions.
- M-ARC-034 Data Flow / Trust Boundary Analysis — connect data movement, identity and controls.

### 5. Capacity, reliability and operations

- M-ARC-040 Capacity Modeling — workload, throughput, latency, storage, concurrency and growth assumptions.
- M-ARC-041 Queueing / bottleneck analysis — identify saturation and waiting-time risks where applicable.
- M-ARC-042 Failure Mode Analysis — identify component/service failure consequences and responses.
- M-ARC-043 RTO/RPO and resilience scenario analysis — align recovery architecture with business impact.
- M-ARC-044 Load/Performance Prototyping — validate high-risk performance assumptions early.

### 6. Technology and reuse

- M-ARC-050 Build vs Buy vs Reuse analysis.
- M-ARC-051 Technology Radar / lifecycle assessment.
- M-ARC-052 Vendor lock-in and portability analysis.
- M-ARC-053 Migration/replacement cost analysis.
- M-ARC-054 Open-source/project maturity assessment.

### 7. Economics and risk

- M-ARC-060 TCO analysis.
- M-ARC-061 Expected Loss / residual risk economics.
- M-ARC-062 Cost of Delay / opportunity cost.
- M-ARC-063 Scenario-based ROI/NPV/payback where applicable.
- M-ARC-064 Engineering effort Bottom-Up estimate.

## Method selection rule

The architect records:

Problem / Decision → Candidate Methods → Selection Reason → Expected Cost/Time → Expected Information Gain → Actual Result.

For material decisions, FATHER should later compare whether a method reduced uncertainty, rework, incidents, architecture changes, delivery time or economic loss.

## Method minimalism

Do not run every method on every project. A Telegram bot may need a simple decision matrix, ADR and threat model; a critical enterprise platform may justify formal quality scenarios, trade-off workshops, capacity models, recovery analysis and multiple prototypes.

Method depth SHALL be proportional to expected consequence of error, uncertainty, project cost, reversibility and regulatory/security impact.

## Learning loop

Project class + method + competency profile + method effort/cost + decision confidence + downstream rework/incidents + business outcome → updated recommendation.

A method may move from ADOPT to HOLD if evidence shows poor value in a specific problem class. Conversely, a previously optional method may become required when repeated failures are correlated with its absence.

## OTUS review marker

After each relevant OTUS architecture lesson:

1. compare lesson methods/artifacts with this catalog;
2. add missing methods and terminology;
3. remove unsupported assumptions;
4. update role/competency requirements;
5. update Stage 04 and Architecture Views if needed;
6. record changes and reasons in the development log.

This catalog is therefore a living baseline, not a final doctrine.
