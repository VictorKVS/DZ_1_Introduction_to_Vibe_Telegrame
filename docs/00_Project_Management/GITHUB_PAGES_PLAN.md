# GitHub Pages / Engineering Portal Plan

**Document ID:** PM-DOC-002  
**Status:** Planned  
**Purpose:** publish the FATHER documentation as a navigable engineering portal while preserving Markdown in Git as the source of truth.

## 1. Goal

Create a public documentation site for FATHER that looks and behaves like a technical product portal rather than a directory of files.

The site must provide:

- project overview;
- architecture navigation;
- requirements and decisions;
- security and quality documentation;
- innovation registry;
- roadmap;
- diagrams;
- links back to source files and repository history.

## 2. Publication model

```text
Git Markdown
     ↓
Documentation Build
     ↓
Link / Structure Validation
     ↓
Public Content Filter
     ↓
Static Site
     ↓
GitHub Pages
```

The website is a rendered view. The repository remains the authoritative engineering source.

## 3. Information architecture

Proposed top navigation:

```text
Home
├── About FATHER
├── Documentation
│   ├── Project Management
│   ├── Requirements
│   ├── System Analysis
│   ├── Architecture
│   ├── Development
│   ├── Testing
│   ├── Security
│   ├── API
│   └── ADR
├── Knowledge
├── Agent Factory
├── Innovation Registry
├── Roadmap
└── GitHub
```

Sections are added only when the corresponding repository blocks exist and have navigable README files.

## 4. First implementation

The first version should stay deliberately simple:

1. use existing Markdown documents;
2. generate site navigation from approved documentation blocks;
3. render Mermaid diagrams where supported;
4. provide search if the selected static-site tooling supports it;
5. deploy through GitHub Actions / GitHub Pages;
6. reject publication if critical links are broken.

A heavy custom frontend is not required for the first release.

## 5. Candidate tooling

A later technical decision may select one of:

- MkDocs + Material theme;
- Docusaurus;
- GitHub-native Jekyll.

Selection criteria:

- Markdown compatibility;
- nested navigation;
- Mermaid support;
- search;
- versioning options;
- low maintenance cost;
- GitHub Actions integration;
- ability to keep the repository as the source of truth.

This document intentionally does not fix the tool before comparison and ADR approval.

## 6. Public/private boundary

GitHub Pages for a public repository must contain only content explicitly suitable for publication.

Required future publication metadata:

```yaml
publication:
  visibility: public
  include_in_portal: true
```

Possible values should later include at least `public`, `internal`, `restricted`.

The site generator must never infer that all Markdown is public merely because it exists in the repository.

## 7. Future Django integration

The Django Control Plane should later ingest the same document metadata and links:

```text
Git Markdown
   │
   ├── GitHub Pages
   │
   ├── Django Documentation UI
   │
   └── Knowledge / Search Index
```

This allows one information model to serve developers, customers and FATHER agents without maintaining duplicate documentation sets.

## 8. Documentation Agent integration

The Documentation Agent will eventually be responsible for:

- maintaining navigation manifests;
- validating links;
- identifying missing README files;
- proposing publication metadata;
- detecting stale pages;
- generating changelog/navigation updates;
- preparing a Pages build;
- blocking publication of restricted documents.

## 9. First milestone

`DOC-PORTAL-M1` is complete when:

- every active first-level block has README navigation;
- root README links all first-level blocks;
- publication tooling is chosen by ADR;
- the basic GitHub Pages site builds automatically;
- Architecture, Decisions and Innovation Registry are accessible through site navigation;
- no confidential project material is exposed.

## Navigation

- ↑ [00 — Project Management](README.md)
- ← [Documentation Standard](DOCUMENTATION_STANDARD.md)
- ↑ [Documentation Map](../README.md)
- 🏠 [Project Home](../../README.md)
