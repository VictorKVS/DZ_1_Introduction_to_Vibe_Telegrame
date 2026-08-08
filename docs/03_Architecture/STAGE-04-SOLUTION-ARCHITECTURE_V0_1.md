# Stage 04 — Solution Architecture v0.1

Status: DRAFT
Conforms to: FATHER Stage Operating Model v0.1

## WHY
Select and justify a solution architecture that satisfies business/system requirements at acceptable quality, security, legal, economic and technology-strategy risk, while remaining buildable and operable by available or obtainable capabilities.

## INPUT
System Analysis Package: SRS, context/boundaries, functional/NFR requirements, domain/data models, integrations, capacity assumptions, security/privacy/legal requirements, acceptance/testability, traceability, cost-driving requirements, capability gaps, assumptions, evidence and estimate confidence.

## WHAT — mandatory architecture package
- ARC-001 Architecture Drivers & Quality Attributes
- ARC-002 Architecture Context / System Landscape
- ARC-003 Candidate Solution Options (minimum alternatives where meaningful)
- ARC-004 Trade-off / Decision Matrix
- ARC-005 Target Solution Architecture
- ARC-006 Component / Service Model
- ARC-007 Data Architecture
- ARC-008 Integration / API / Event Architecture
- ARC-009 Infrastructure & Deployment Architecture
- ARC-010 Capacity / Performance Model
- ARC-011 Availability / Resilience / Backup / DR Architecture
- ARC-012 Observability / Logging / Audit Architecture
- ARC-013 Security Architecture & Trust Boundaries
- ARC-014 Legal / Jurisdiction Architecture Constraints
- ARC-015 Technology Portfolio & Build/Buy/Reuse Analysis
- ARC-016 ADR Set
- ARC-017 Architecture Risk Register with monetary loss scenarios where estimable
- ARC-018 Migration / Transition Architecture when applicable
- ARC-019 Architecture Test / Fitness Function Plan
- ARC-020 Architecture Cost / TCO / Migration Cost Model
- ARC-021 Architecture WBS / Resource / Capability Plan
- ARC-022 Architecture Handover & Decision Record

## HOW — architecture methods
Methods are chosen, justified and later measured. Candidates: quality-attribute scenarios, trade-off analysis/ATAM-inspired review where appropriate, C4, DDD/context mapping, event storming outputs, ADR, threat modeling, data-flow/trust-boundary modeling, capacity modeling, failure-mode analysis, dependency mapping, prototypes/PoC/spikes, benchmarking, technology radar, build-buy-reuse analysis, TCO/ROI/NPV/payback where appropriate, migration analysis and architecture fitness functions.

No method is mandatory merely by fashion. Method value is evaluated against decision quality, effort, downstream rework and outcomes.

## OPTIONS FIRST
Material architecture decisions SHALL compare alternatives when alternatives exist. For each option record:
- requirements/NFR fit;
- implementation effort and schedule;
- required competencies/capacity;
- infrastructure/resources;
- CAPEX/OPEX/TCO;
- migration/switching cost;
- vendor lock-in;
- security/privacy/legal impact;
- operational complexity;
- scalability/resilience;
- technology maturity/lifecycle risk;
- reuse/strategic asset value;
- expected risk loss;
- confidence and evidence.

Decision = selected option + rejected alternatives + reasons + evidence + owner + review trigger.

## WITH WHAT
Architecture repository, SRS/traceability, standards/pattern/anti-pattern libraries, Technology Radar, prior project outcomes, GitHub/project scout evidence, vendor/open-source documentation, benchmarks, data schemas, APIs, infrastructure catalog, cloud/on-prem capabilities, cost catalogs, threat/loss data, legal profiles, modeling/prototyping tools and test environments.

## BY WHOM
Solution Architect owns the architecture package. Supporting roles: System Analyst, Product, Enterprise/Domain/Data/Security Architect as applicable, DevOps/Platform, Developers/Tech Leads, QA/Test Architect, Security, Legal/Compliance, Economist/FinOps, SRE/Operations, Technology Scout/OSINT, Domain Expert.

Record required and actual competency, availability, historical performance, review/supervision and conflicts of interest/vendor dependence where material.

## CAPABILITY & CAPACITY
Architecture must be feasible for the delivery/operations organization. Compare required vs available skills, people-hours, infrastructure, environments, data and tooling. A theoretically elegant architecture that cannot be built/operated within constraints is not PASS.

Gap alternatives: train, hire, contract, managed service, reuse, AI assistance, simplify architecture, change technology, phase delivery, reduce scope, increase budget or formally accept risk.

## WORK / TIME / COST
Core WPs: drivers/NFR review; option research; PoC/benchmark where needed; target architecture; data/integration; infrastructure/capacity; security/legal; operations/resilience; economics/TCO; ADR/risk; fitness/test plan; review/handover.

Each WP: O/M/P → PERT; role/capacity; rate; labor; cloud/LLM/tool/license/external cost; tax/overhead placeholder; risk reserve; confidence; baseline; actual.

## ECONOMIC ARCHITECTURE
Architecture choices SHALL expose economic consequences. Track implementation cost, recurring OPEX, cloud/compute/storage/network, LLM/API, licenses, support, people, security/compliance, downtime exposure, expected loss, migration cost, switching cost, Cost of Delay and decommission cost. Unknown = 0 + NOT_ESTIMATED.

Compare not only cheapest implementation but lifecycle value and risk. Record cost sensitivity to scale/load and key assumptions.

## SECURITY BY DESIGN
Threat modeling and trust boundaries are architecture work, not a post-build audit. Architecture shall define identity/access boundaries, data protection, secrets/key approach, network/segmentation assumptions, auditability, dependency/supply-chain considerations, resilience and required security controls. Security findings feed the monetary Threat & Loss Matrix where possible.

## TECHNOLOGY EVOLUTION / REPLACEABILITY
For material technologies record lifecycle state, maturity, community/vendor health, license, lock-in, portability, data/export strategy, replacement candidates, migration effort, compatibility boundaries and review triggers. Design replaceable commodity components where economically reasonable; protect strategic assets and organizational memory from vendor coupling.

## GATES
Quality Gate: requirements/NFR coverage, consistency, evidence, simplicity, operability, testability.
Security Gate: threat model, controls, residual risk, trust boundaries.
Legal Gate: jurisdiction/data/provider/licensing/contract constraints.
Economic Gate: TCO, cost drivers, risk loss, migration/switching cost, affordability and business value.
Technology Strategy Gate: build/buy/reuse, maturity, lifecycle, lock-in, replacement strategy and strategic asset decision.

## DONE
Architecture is complete when drivers are explicit; material options were compared; decisions have ADR/evidence; target architecture covers required functional/NFR concerns; infrastructure/capacity/operations/security/legal/economics are addressed; risks and residual unknowns have owners; capability/capacity gaps have plans; architecture fitness/test criteria exist; WBS/PERT/cost baseline exists; required gates resolved; engineering/QA/operations representatives accept the handover.

## OUTPUT — ENGINEERING ARCHITECTURE PACKAGE
Target architecture + ADRs + interfaces/contracts + data/infrastructure/security/operations architecture + technology choices + capacity model + fitness/test criteria + risks + TCO/cost assumptions + build/buy/reuse decisions + migration/replacement strategy + required competencies/capacity + estimates + evidence + traceability + open questions.

## METRICS & LEARNING
Outcome: architecture-related production incidents, realized NFRs, TCO vs forecast, business outcome support.
Process: lead/touch/wait time, option-analysis effort, review cycles, PERT vs actual, cost plan/fact.
Quality: architecture rework, ADR reversals, late NFR discoveries, integration failures, fitness-function failures, technical debt attributable to architecture.
Technology: migration frequency/cost, lock-in exposure, obsolete dependencies, reuse rate, technology forecast accuracy.
Capability: competency gaps, review findings by domain, team ability to build/operate selected architecture.
Economics: lifecycle cost variance, avoided loss, Cost of Delay, cost of change, migration/switching cost.

Learning loop: architecture pattern/technology/method + project context + team capability + forecast cost/risk + actual delivery/operations/outcome → update standards, patterns, Technology Radar, estimation coefficients and competency plans.
