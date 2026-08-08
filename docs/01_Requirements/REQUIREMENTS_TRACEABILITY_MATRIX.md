# FATHER — Requirements Traceability Matrix v0.1

**Status:** BASELINE / EVOLVING  
**Purpose:** связать цели, требования, аналитику, архитектуру, ИБ, тесты, код и фактический результат в единую проверяемую цепочку.

## Принцип

Ни один существенный CodeArtifact не должен существовать без трассировки назад к требованию или одобренному Change Request. Ни одно существенное требование не считается закрытым без проверяемого TestCase/TestRun и связанного результата.

Базовая цепочка:

`Goal → Requirement → Analysis → Architecture Decision → Security Control → TestCase → CodeArtifact → TestRun → Metric → Outcome`

## Минимальные поля RTM

| Field | Meaning |
|---|---|
| requirement_id | стабильный ID требования |
| goal_ref | бизнес/инженерная цель |
| source_ref | источник требования |
| type | BR / FR / NFR / SEC / LEGAL / DATA / OPS |
| priority | MUST / SHOULD / COULD / WONT |
| analysis_ref | аналитический артефакт |
| decision_ref | ADR/Decision Record |
| architecture_ref | компонент/интерфейс |
| security_control_ref | мера/контроль ИБ |
| test_case_ref | проектный тест |
| code_artifact_ref | repository/path/symbol/commit |
| status | lifecycle status |
| verification_status | NOT_TESTED / PASS / FAIL / PARTIAL |
| outcome_ref | эксплуатационный результат |

## Первый шаблон RTM

| Requirement | Goal | Analysis | Architecture | Security | Test | Code | Verification | Outcome |
|---|---|---|---|---|---|---|---|---|
| FR-001 Project Intake | G-MVP-001 | BA-001 | ARC-Core-Project | AC-OWN-001 | TC-API-001 | `src/core/` | IN PROGRESS | — |
| FR-002 Goal Traceability | G-MVP-001 | SA-001 | ARC-Core-Goal | AC-OWN-001 | TC-TRACE-001 | `src/core/` | IN PROGRESS | — |
| FR-003 Problem Traceability | G-MVP-001 | SA-001 | ARC-Core-Problem | AC-OWN-001 | TC-TRACE-002 | `src/core/` | IN PROGRESS | — |
| FR-004 Provenance / Source | G-KNOW-001 | SA-002 | ARC-Core-Source | AC-DATA-001 | TC-SOURCE-001 | `src/core/` | IN PROGRESS | — |
| FR-005 Evidence | G-KNOW-001 | SA-002 | ARC-Core-Evidence | AC-DATA-001 | TC-EVID-001 | `src/core/` | IN PROGRESS | — |
| FR-009 Decision Session | G-DEC-001 | SA-003 | ARC-SOCRATES-Session | AC-OWN-001 | TC-DEC-001 | `src/decisions/` | IN PROGRESS | — |
| FR-010 Alternatives | G-DEC-001 | SA-003 | ARC-SOCRATES-Alternative | AC-OWN-001 | TC-DEC-002 | `src/decisions/` | IN PROGRESS | — |
| FR-011 Expert Review | G-DEC-001 | SA-003 | ARC-SOCRATES-Review | AC-LLM-001 | TC-DEC-003 | `src/decisions/` | IN PROGRESS | — |
| FR-012 Human Gate | G-GOV-001 | SA-004 | ARC-SOCRATES-Gate | AC-HUMAN-001 | TC-GATE-001 | `src/decisions/` | IN PROGRESS | — |

Таблица выше является seed-матрицей. Источником истины в будущем должна стать БД, а Markdown — генерируемым представлением.

## Правила качества трассировки

1. Для MUST-требования coverage обязан быть 100% до RELEASED.
2. NFR и Security Requirements имеют такие же права на трассировку, как функциональные требования.
3. Изменение CodeArtifact инициирует impact analysis по связанным требованиям, тестам и контролям.
4. Изменение Requirement инициирует impact analysis вниз по цепочке до кода и эксплуатации.
5. Связи many-to-many допустимы и ожидаемы.
6. Удаление требования требует статуса DEPRECATED/REJECTED и причины; история не стирается.
7. TestCase проектируется до или одновременно с реализацией, а не постфактум.

## Метрики

- requirement_coverage = requirements_with_architecture / active_requirements
- test_coverage_by_requirement = requirements_with_tests / active_requirements
- implementation_traceability = code_artifacts_with_requirement / governed_code_artifacts
- verification_pass_rate = passed_required_tests / required_tests
- orphan_artifacts = artifacts_without_valid_trace
- stale_trace_links = links_to_deprecated_or_missing_objects

## Gate

RTM считается пригодной для MVP, если для первой вертикали можно автоматически пройти в обе стороны:

`Requirement → Decision → Test → Code`

и

`Code → Test → Decision → Requirement → Goal`.
