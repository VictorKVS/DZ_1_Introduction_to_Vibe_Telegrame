# Open Source Reuse & GitHub Harvesting Policy v0.1

Status: DRAFT / PROVISIONAL
Owner: Technology Intelligence + Architecture + Legal + Security

## Principle

FATHER should treat GitHub and other public software ecosystems as a strategic component market and knowledge source. Reuse is preferred over reinvention when a mature external component satisfies requirements economically and safely.

Publicly visible source code is not automatically free to copy, modify, redistribute or commercialize. Reuse requires explicit license and provenance review.

## Default decision order

NEED
→ existing standard?
→ mature open-source component?
→ commercial/open-core product?
→ managed/cloud service?
→ integration/adaptation?
→ internal implementation only if justified.

## GitHub Harvesting Pipeline

Requirement / Capability Gap
→ search repositories
→ shortlist
→ license gate
→ provenance / ownership check
→ project health analysis
→ security / supply-chain analysis
→ architecture fit
→ performance / benchmark review
→ TCO and maintenance cost
→ build/buy/integrate/adapt decision
→ sandbox PoC where needed
→ approved component registry
→ SBOM / version pinning / update policy
→ production outcome feedback.

## Repository evaluation card

For each candidate capture:
- repository and upstream organization;
- capability provided;
- license and obligations;
- commercial-use compatibility;
- attribution / notice requirements;
- copyleft implications where applicable;
- release cadence and latest stable version;
- contributors / bus factor;
- issue and PR activity;
- stars/forks only as weak signals, never proof of quality;
- dependency tree;
- known vulnerabilities/advisories;
- signed releases/provenance where available;
- tests/CI status;
- documentation quality;
- supported platforms;
- API stability;
- performance evidence;
- architecture fit;
- required adaptation effort;
- operational complexity;
- migration/exit path;
- TCO;
- confidence and review date.

## Decision classes

REUSE-AS-IS — approved dependency/component.
WRAP — isolate behind our contract to reduce lock-in.
FORK — only with an explicit maintenance owner and economic justification.
LEARN — use concepts/patterns, not source code.
WATCH — promising but not production-ready.
AVOID — unsuitable due to license, security, maintenance or architecture risk.
BUILD — internal implementation justified by requirements or strategic advantage.

## Mandatory gates

### License Gate
No code enters FATHER production merely because the repository is public. License, notices, redistribution, modification and commercial-use conditions must be understood and recorded. Repositories with no license are not presumed reusable.

### Security Gate
Review dependencies, known vulnerabilities, dangerous defaults, secret handling, update channel, build provenance and privilege requirements. High-risk components require stronger review and sandbox validation.

### Maintenance Gate
A technically excellent abandoned library may have a worse TCO than a less elegant actively maintained alternative. Record update frequency, maintainer concentration, ecosystem maturity and likely replacement cost.

### Architecture Gate
Prefer adapters and stable internal contracts around replaceable external components. Strategic FATHER logic should not become inseparable from one repository unless consciously accepted.

## Knowledge reuse vs code reuse

FATHER may learn from public architecture patterns, algorithms, benchmarks, postmortems and implementation techniques even when direct code reuse is not appropriate. Knowledge objects must preserve source, license/copyright context, provenance and paraphrased claims rather than blindly copying protected text.

## Component Intelligence Agent

A dedicated agent may continuously search GitHub and similar ecosystems for:
- better implementations of current components;
- new releases and deprecations;
- security advisories;
- abandoned dependencies;
- emerging standards;
- cheaper/faster alternatives;
- reference implementations;
- reusable testing and DevSecOps tooling.

It proposes changes; it does not silently replace production dependencies.

## Strategic rule

The objective is not "use everything on GitHub". The objective is "inspect everything useful, reuse what is legally and technically justified, learn from the rest, and avoid paying to reinvent solved problems."