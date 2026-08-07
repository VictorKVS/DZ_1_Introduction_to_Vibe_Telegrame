# FATHER Documentation Standard

**Document ID:** STD-DOC-001  
**Status:** Active  
**Applies to:** repository, GitHub Pages, future Django documentation portal and Documentation Agent.

## 1. Purpose

FATHER treats documentation as a first-class engineering artifact. Documentation must be navigable by a human and machine-readable enough for future agents to maintain, validate and publish it automatically.

Core rule:

> **Documentation First, Navigation Always.**

No major block may exist without a local `README.md`, and no important document may remain disconnected from the navigation graph.

## 2. Documentation hierarchy

```text
ROOT README.md
    ↓
section README.md
    ↓
subsection README.md
    ↓
detailed documents / ADR / specifications / diagrams / evidence
```

The root README is the public map of the whole project. Every lower README is the landing page for its block.

## 3. Mandatory README content

Each block README must contain:

1. purpose;
2. scope and boundaries;
3. place in the overall FATHER architecture;
4. inputs and outputs where applicable;
5. key entities/processes;
6. current documents;
7. current implementation status;
8. next steps;
9. navigation to parent and related blocks.

## 4. Navigation rules

Every detailed document should provide enough context to return to its parent block. Related documents should be explicitly linked instead of relying on folder browsing.

Recommended navigation section:

```text
↑ Parent
← Related
→ Related
🏠 Project Home
```

The exact visual form may evolve, but parent and related relations must remain explicit.

## 5. Document metadata

Important documents should gradually adopt a compact metadata header:

```yaml
document:
  id: ARCH-003
  title: Delivery Intelligence
  status: draft
  version: 0.3
  owner_role: architect
  parent: docs/03_Architecture/README.md
  related:
    - ADR-002
    - EST-001
    - SEC-004
```

Metadata is intended for later ingestion into Django, search, knowledge graphs and automatic documentation generation.

## 6. Status vocabulary

Recommended statuses:

- `DRAFT`
- `REVIEW`
- `APPROVED`
- `ACTIVE`
- `SUPERSEDED`
- `ARCHIVED`
- `FUTURE`

A document may remain historically accessible after being superseded; replacement must be linked.

## 7. Source of truth

Markdown in the Git repository is the initial source of truth for engineering documentation.

```text
Markdown
   ├── GitHub repository
   ├── GitHub Pages portal
   ├── future Django portal
   └── FATHER Knowledge Base ingestion
```

Generated representations must not silently diverge from the repository version.

## 8. Agent behavior

The future Documentation Agent must:

- create a README when a new major block is created;
- insert links into the parent README;
- update the project navigation when a first-class subsystem appears;
- detect orphaned documents;
- detect broken relative links;
- check duplicated or conflicting navigation;
- maintain status and version metadata;
- flag stale documentation when implementation changes;
- generate a publication-ready navigation tree.

The agent may propose structural changes, but important renames or moves should pass normal project change control.

## 9. Documentation and implementation traceability

Documentation should eventually participate in project traceability:

```text
Business Requirement
        ↓
System Requirement
        ↓
Architecture / ADR
        ↓
Implementation
        ↓
Test
        ↓
Evidence
        ↓
Operational Result
```

The documentation portal is therefore not only a knowledge site but also a view of the project evidence chain.

## 10. Security requirements

Documentation may itself contain sensitive architecture, secrets references, internal URLs and customer information. Therefore:

- secrets must never be stored in Markdown;
- confidential documents must not be published to public GitHub Pages;
- publication must use an explicit public/private classification;
- generated site content must inherit document classification;
- customer-specific or restricted knowledge must remain inside its security boundary.

## 11. Definition of Done for a documentation block

A block is documentation-complete when:

- its README exists;
- purpose and scope are described;
- parent navigation points to it;
- key child documents are listed;
- related blocks are linked;
- status is visible;
- no critical document is orphaned;
- public/private publication status is known.

## 12. Principle

> **A person or an agent should be able to enter FATHER at the root README and reach any important architectural decision, requirement, idea, risk or implementation artifact through explicit navigation rather than repository archaeology.**

## Navigation

- ↑ [00 — Project Management](README.md)
- ↑ [Documentation Map](../README.md)
- 🏠 [Project Home](../../README.md)
- → [GitHub Pages Plan](GITHUB_PAGES_PLAN.md)
