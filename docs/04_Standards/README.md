# 04 — FATHER Standards Library

> Нормативный слой FATHER: внутренние инженерные стандарты, обязательные правила производства, шаблоны принятия решений, паттерны и анти-паттерны.

[← К карте документации](../README.md) · [↑ Главный README](../../README.md)

## Назначение

Этот раздел определяет **как именно FATHER обязан работать**, независимо от конкретной LLM, языка программирования, облака или отрасли.

Стандарты используются как исполняемые правила для требований, аналитики, архитектуры, ИБ, юридического соответствия, экономики, инфраструктуры, тестирования, эксплуатации и организационной памяти.

## Базовый принцип

```text
Goal / Business Need
        ↓
Applicable Standards Profile
        ↓
Required Artifacts + Gates
        ↓
Engineering Work
        ↓
Evidence / Tests / Metrics
        ↓
Outcome
        ↓
Standard Review / Improvement
```

Стандарт не считается полезным только потому, что он существует. Он должен иметь область применения, обязательные проверки и измеримый эффект.

## Текущие документы

- [Engineering Constitution v0.1](ENGINEERING_CONSTITUTION_V0_1.md) — неизменяемые базовые принципы инженерного производства FATHER.
- [Standards Catalog v0.1](STANDARDS_CATALOG_V0_1.md) — реестр внутренних стандартов `STD-*`.
- [STD-013 DevSecOps & Secure SDLC v0.1](STD-013-DEVSECOPS-SECURE-SDLC_V0_1.md) — сквозная безопасность разработки: GitHub → CI → supply chain → release → operations.
- [GitHub Security Baseline v0.1](GITHUB_SECURITY_BASELINE_V0_1.md) — чек-лист безопасной организации репозиториев FATHER и дочерних продуктов.
- [Machine-Readable Standard Model v0.1](MACHINE_READABLE_STANDARD_MODEL_V0_1.md) — формальная модель `StandardDefinition / ControlDefinition / GateDefinition / ComplianceRecord`.
- [Pattern Library v0.1](PATTERN_LIBRARY_V0_1.md) — переиспользуемые инженерные решения `PAT-*`.
- [Anti-Pattern Library v0.1](ANTIPATTERN_LIBRARY_V0_1.md) — решения и практики, которые приводят к систематическим потерям `APT-*`.
- [Decision Pattern Library v0.1](DECISION_PATTERN_LIBRARY_V0_1.md) — стандартизированные способы принятия решений `DP-*`.

## Машинно-читаемые артефакты

- [`STANDARD_DEFINITION_SCHEMA_V0_1.json`](STANDARD_DEFINITION_SCHEMA_V0_1.json) — JSON Schema для исполняемого стандарта.
- [`GATE_RECORD_SCHEMA_V0_1.json`](GATE_RECORD_SCHEMA_V0_1.json) — JSON Schema результата выполнения Gate.
- [`STD-006-SECURITY-ENGINEERING_V0_1.json`](STD-006-SECURITY-ENGINEERING_V0_1.json) — первый исполняемый профиль стандарта: Security Engineering.

## Идентификаторы

- `STD-*` — стандарт;
- `PAT-*` — паттерн;
- `APT-*` — анти-паттерн;
- `DP-*` — паттерн принятия решения;
- `CTL-*` — контроль;
- `GATE-*` — обязательный gate;
- `MET-*` — метрика;
- `TPL-*` — шаблон.

## Правило развития

Любой стандарт обязан иметь:

1. цель;
2. область применения;
3. обязательные входы и выходы;
4. обязательные артефакты;
5. Quality/Security/Legal/Economic Gates;
6. критерии PASS/FAIL;
7. метрики эффективности;
8. владельца;
9. версию;
10. историю изменений;
11. ссылку на evidence и результаты эксплуатации.

## Сквозной DevSecOps baseline

Для программных продуктов безопасность начинается при создании репозитория и продолжается после релиза. Целевой pipeline включает quality checks, unit tests, SAST, secret scanning, SCA, dependency/license controls, SBOM, container/IaC scanning, integration/API/DAST security tests и Release Security Gate.

Конкретные инструменты выбираются через Technology Strategy Gate; стандарт фиксирует обязательную capability, а не vendor lock.

## Исполняемый цикл

```text
StandardDefinition
      ↓
StandardProfile for Project
      ↓
Applicable Controls by Stage
      ↓
GateRun
      ↓
Evidence + Findings + Economic Impact
      ↓
PASS / FAIL / WAIVER
      ↓
ComplianceRecord
      ↓
Outcome / Metrics
      ↓
Update Standard
```

Первый эталонный стандарт — `STD-006 Security Engineering`. `STD-013 DevSecOps & Secure SDLC` расширяет его до полного производственного контура GitHub/CI/CD/supply chain/release/operations.

## Следующий шаг

1. Валидировать `STD-006-SECURITY-ENGINEERING_V0_1.json` против `STANDARD_DEFINITION_SCHEMA_V0_1.json` в CI.
2. Пройти текущий репозиторий по `GITHUB_SECURITY_BASELINE_V0_1.md`.
3. Добавить/усилить CI jobs: SAST, secret scanning, SCA, container/IaC scanning where applicable.
4. Добавить модели Django: `StandardDefinition`, `ControlDefinition`, `StandardProfile`, `GateRun`, `GateCheckResult`, `Finding`, `Waiver`, `ComplianceRecord`.
5. Реализовать первый автоматический `Security Gate`.
6. Затем тем же форматом перевести `STD-007 Legal/Compliance`, `STD-008 Economics`, `STD-005 Infrastructure`, `STD-011 Testing`.

## Статус

`BASELINE v0.1 / SECURITY + DEVSECOPS EXECUTABLE LAYER IN DEVELOPMENT`
