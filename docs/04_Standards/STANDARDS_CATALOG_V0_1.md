# FATHER Standards Catalog v0.1

## Назначение

Реестр внутренних стандартов FATHER. Значение `PLANNED` означает, что стандарт обязателен к появлению, но ещё не детализирован.

| ID | Стандарт | Статус | Основной результат |
|---|---|---|---|
| STD-001 | Project Lifecycle | ACTIVE | единый жизненный цикл проекта и gates |
| STD-002 | Business Requirements | PLANNED | BRD/Product Scope/Business Value |
| STD-003 | Business & System Analysis | PLANNED | модели процессов, данных, ограничений, сценариев |
| STD-004 | Architecture | ACTIVE-PARTIAL | архитектура, ADR, trade-offs, NFR trace |
| STD-005 | Infrastructure Lifecycle | ACTIVE | инфраструктурные требования, design, protection, tests, ops |
| STD-006 | Security Engineering | ACTIVE-PARTIAL | security requirements, threat model, controls, security gates |
| STD-007 | Legal & Regulatory Compliance | ACTIVE-PARTIAL | jurisdiction profile, obligations, legal gates |
| STD-008 | Engineering Economics | ACTIVE-PARTIAL | estimates, TCO, ROI/NPV/payback where applicable, plan/fact |
| STD-009 | Threat & Loss Economics | ACTIVE | угрозы → сценарии ущерба → expected/residual loss |
| STD-010 | Cost Model | ACTIVE | полный каталог затрат и `NOT_ESTIMATED` placeholders |
| STD-011 | Test Engineering | PLANNED | test design, acceptance, V&V, regression |
| STD-012 | Software Development | PLANNED | secure coding rules, reviews, quality baseline |
| STD-013 | DevSecOps & Secure SDLC | ACTIVE-PARTIAL | GitHub governance, CI security pipeline, supply-chain security, controlled release |
| STD-014 | Operations & Observability | PLANNED | monitoring, SLO/SLA, incidents, capacity |
| STD-015 | Change & Impact Management | ACTIVE-PARTIAL | impact graph, change record, regression scope |
| STD-016 | Knowledge & Evidence | ACTIVE-PARTIAL | provenance, confidence, freshness, validation |
| STD-017 | Decision Engineering | ACTIVE-PARTIAL | alternatives, expert review, human gate, decision record |
| STD-018 | Organizational Memory | ACTIVE-PARTIAL | outcome, lessons learned, reuse statistics |
| STD-019 | Documentation & Navigation | ACTIVE | README hierarchy, traceability, documentation lifecycle |
| STD-020 | Agent/Product Blueprint | PLANNED | reproducible product/agent assembly contract |
| STD-021 | Technology Intelligence & Reuse | PLANNED | аналоги, technology radar, buy/adapt/build, migration economics |

## Обязательные поля будущего машинного представления

```yaml
standard_id:
title:
version:
status:
owner:
scope:
inputs:
required_artifacts:
required_gates:
controls:
metrics:
pass_criteria:
exceptions:
linked_templates:
linked_patterns:
linked_requirements:
evidence:
effective_from:
review_date:
```

## Правило

Стандарт не становится `VALIDATED`, пока не использован хотя бы в одном реальном проектном цикле и не получены метрики результата.
