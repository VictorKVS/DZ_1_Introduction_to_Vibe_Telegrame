# STD-013 — DevSecOps & Secure SDLC v0.1

## Статус

`ACTIVE-PARTIAL`

## Цель

Встроить информационную безопасность в полный жизненный цикл разработки: от создания репозитория и требований до эксплуатации, мониторинга, реагирования и вывода из эксплуатации.

## Базовый принцип

Безопасность не является отдельным этапом после разработки. Каждый инженерный этап обязан иметь собственные security controls, evidence и критерии PASS/FAIL.

```text
Repository Bootstrap
        ↓
Requirements + Security Requirements
        ↓
Threat Modeling / Abuse Cases
        ↓
Architecture Security Review
        ↓
Secure Coding
        ↓
SAST / Secrets / SCA / License
        ↓
Build / SBOM / Artifact Integrity
        ↓
Container / IaC / Config Scan
        ↓
DAST / API / Integration Security Tests
        ↓
Release Security Gate
        ↓
Deployment Hardening
        ↓
Monitoring / SIEM / Detection
        ↓
Vulnerability & Incident Management
        ↓
Lessons Learned / Standard Update
```

## 1. GitHub Repository Bootstrap

Новый production-oriented репозиторий должен проектироваться сразу как управляемый инженерный актив.

Обязательный baseline:

- `README.md`;
- `SECURITY.md`;
- `.gitignore`;
- `.editorconfig`;
- dependency manifest + lock file where applicable;
- `CODEOWNERS` when team workflow becomes applicable;
- issue/PR templates;
- branch and review policy;
- CI workflows;
- automated tests;
- security scanning workflows;
- secrets are never stored in source code;
- environment configuration uses secret/config management;
- release/versioning policy;
- changelog or release notes policy;
- documentation navigation according to STD-019.

## 2. Source Control Governance

Для защищённых веток production-проектов целевой режим:

- изменения через Pull Request;
- минимум один review для значимых изменений;
- отдельный security review для security-sensitive changes;
- обязательный успешный CI перед merge;
- запрет прямого push в protected branch where supported;
- запрет merge при критических security findings;
- traceability `Requirement/Issue → PR → Commit → Test → Release`;
- подписанные commits/tags рассматриваются как целевая возможность для high-assurance профилей;
- права репозитория строятся по least privilege.

## 3. Security Controls по стадиям

### 3.1 Idea / Discovery

- определить типы данных;
- определить возможный ущерб;
- определить regulatory/security class;
- зарезервировать security budget и security effort;
- выявить high-risk use cases.

### 3.2 Requirements

Обязательны security requirements:

- authentication;
- authorization;
- audit;
- confidentiality;
- integrity;
- availability;
- backup/recovery;
- secrets management;
- data retention/deletion;
- incident handling;
- supply-chain requirements.

### 3.3 Analysis

- data flow analysis;
- trust boundaries;
- abuse/misuse cases;
- sensitive asset inventory;
- dependency on third parties;
- preliminary threat/loss matrix.

### 3.4 Architecture

- threat modeling;
- attack surface review;
- segmentation/trust zones;
- IAM model;
- encryption requirements;
- logging/monitoring design;
- backup/DR design;
- secure integration design;
- residual risk decision.

### 3.5 Development

Минимальный automated baseline:

- unit tests;
- lint/static quality checks;
- SAST;
- secret scanning;
- SCA/dependency vulnerability scanning;
- dependency/license policy checks;
- security-focused code review for sensitive changes.

### 3.6 Build & Supply Chain

- reproducible/controlled build where feasible;
- artifact integrity;
- SBOM generation target;
- dependency provenance where feasible;
- immutable release artifacts target;
- build secrets must not leak into artifacts/logs.

### 3.7 Infrastructure / IaC

- IaC scanning;
- container/image scanning;
- hardening baseline;
- network policy review;
- IAM/RBAC review;
- secrets handling;
- exposed services review;
- backup and recovery validation;
- infrastructure cost and risk linkage.

### 3.8 Testing

- negative tests;
- authorization tests;
- authentication tests;
- API security tests;
- DAST when applicable;
- dependency/runtime tests;
- regression security tests;
- performance/DoS-related tests where risk justifies them;
- acceptance against security requirements.

### 3.9 Release

Release must have a Security Gate containing:

- unresolved findings by severity;
- accepted residual risks;
- approved waivers;
- evidence from security tests;
- SBOM/artifact identity where applicable;
- rollback readiness;
- monitoring readiness;
- responsible owner.

Critical unresolved finding blocks release unless formally accepted by an authorized Human Gate under the applicable profile.

### 3.10 Operations

- security logs;
- centralized monitoring/SIEM where profile requires;
- alerting;
- vulnerability management;
- patch management;
- incident response;
- access review;
- configuration drift control;
- backup/recovery tests;
- periodic threat model review.

### 3.11 Decommission

- revoke credentials and access;
- remove secrets;
- archive required evidence;
- apply retention/deletion policy;
- dispose of infrastructure/data securely;
- document residual dependencies;
- update organizational memory.

## 4. CI Security Pipeline — target sequence

```text
Commit / Pull Request
  ↓
Format/Lint
  ↓
Unit Tests
  ↓
SAST
  ↓
Secrets Scan
  ↓
SCA / Dependency Scan
  ↓
License Policy
  ↓
Build
  ↓
SBOM
  ↓
Container / IaC Scan
  ↓
Integration Tests
  ↓
Security Tests / DAST (where applicable)
  ↓
Quality + Security + Legal + Economic Gate
  ↓
Controlled Release
```

## 5. Planned Tool Classes

Конкретные продукты выбираются Technology Strategy Gate. В стандарте фиксируются классы возможностей, а не vendor lock:

- SAST;
- secrets scanning;
- SCA;
- SBOM;
- container scanning;
- IaC scanning;
- DAST;
- API security testing;
- dependency/license governance;
- SIEM/observability;
- artifact signing/provenance.

Для текущего Python/Django PoC допустимы инструменты уровня Bandit/Semgrep, secret scanners, dependency scanners, Trivy/ZAP и аналогичные решения после отдельной оценки.

## 6. Mandatory Security Metrics

Минимальный будущий набор:

- critical/high findings by stage;
- mean time to remediate;
- vulnerabilities escaped to production;
- secrets findings;
- dependency risk;
- security test coverage;
- percentage of releases passing without waiver;
- residual expected loss;
- cost of security controls;
- avoided expected loss;
- security-caused rework;
- incident cost;
- security debt.

## 7. Связь с экономикой

Каждый significant finding может связываться с Threat & Loss Matrix:

`Finding → Threat Scenario → Expected Loss → Control Cost → Residual Loss`.

Security prioritization должна учитывать не только CVSS/severity, но и бизнес-контекст и ожидаемые потери.

## 8. Definition of Done для security-sensitive изменения

Изменение не считается завершённым, пока:

1. требование трассируется до реализации;
2. security impact оценён;
3. необходимые тесты выполнены;
4. автоматические security checks пройдены;
5. findings обработаны;
6. документация и threat model обновлены, если затронуты;
7. residual risk зафиксирован;
8. результат вошёл в Development Log / Organizational Memory when material.

## 9. Следующий шаг реализации

1. создать GitHub Security Baseline checklist;
2. привести текущий репозиторий к baseline;
3. добавить CI jobs для SAST/secrets/SCA/container/IaC where applicable;
4. внедрить machine-readable Security Gate Record;
5. связать findings с Django `GateRun`, `Finding`, `Risk`, `EconomicRecord`.
