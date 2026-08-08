# 03 — Architecture

> Архитектурный блок FATHER: как устроена фабрика продуктов, программ, знаний и AI-агентов.

[← К карте документации](../README.md) · [↑ Главный README](../../README.md)

## Назначение

Раздел фиксирует целевую и эволюционную архитектуру FATHER, границы подсистем, потоки данных, архитектурные варианты, trade-off и связь архитектуры со сроками, стоимостью, рисками, безопасностью и соблюдением норм.

## Место в FATHER

```text
Idea / Requirements
        ↓
Analysis
        ↓
Architecture
        ↓
Quality / Security / Legal / Economics / Test Design
        ↓
Implementation
        ↓
Verification / Validation
        ↓
Verified Product / Agent
        ↓
Operational Outcome
        ↓
Lessons Learned / Organizational Memory
```

Архитектура не считается обоснованной, если невозможно объяснить, какое требование или риск требует конкретного компонента, какими тестами он проверяется, каким нормам должен соответствовать и какие стоимость и эксплуатационную сложность он создаёт.

## Ключевые принципы

- Minimum Sufficient Architecture.
- Security by Construction + Security by Default.
- Legal/Compliance by Construction.
- Economics by Construction.
- Cross-Cutting Gates: Quality + Security + Legal/Compliance + Economics на всех стадиях.
- Evidence over opinion.
- Provider Independence.
- Human Decision Gates.
- Architecture Baseline + Change Management.
- Tests-as-Specification до основного кодирования.
- Код является производным артефактом требований, анализа, архитектуры и тестового baseline.
- План/факт и обучение на фактическом результате.
- Goal → Requirement → Decision → Code → Test → Outcome traceability.
- Knowledge Graph хранит причинно-связанную историю инженерной деятельности, а не только документы.
- Controlled Vocabulary: один термин имеет одно официальное значение в системе.

## Текущие документы

- [Engineering Delivery Pipeline v0.1](ENGINEERING_DELIVERY_PIPELINE.md) — нормативная цепочка ТЗ → аналитика → архитектура → ИБ → тесты → код → V&V → outcome.
- [Cross-Cutting Gates Standard v0.1](CROSS_CUTTING_GATES_STANDARD.md) — обязательные Quality, Security, Legal/Compliance и Economic Gate на всех стадиях производства.
- [Economic Gate v0.1](ECONOMIC_GATE.md) — стоимость, сроки, TCO, ROI/NPV/payback при применимости, Cost of Delay, Value of Information и plan/fact.
- [Legal & Regulatory Compliance Gate](LEGAL_COMPLIANCE_GATE.md) — юрисдикции, региональные нормы, regulatory impact и Human Gate юриста.
- [Impact Analysis Model](IMPACT_ANALYSIS_MODEL.md) — радиус изменений от требований/стандартов/кода до тестов, рисков и стоимости.
- [FATHER Delivery Intelligence](FATHER_DELIVERY_INTELLIGENCE.md) — Project/Technology OSINT, Estimation Engine, Talent Intelligence, Staffing, Risk, TCO и Delivery Control.
- [Engineering Knowledge Graph](ENGINEERING_KNOWLEDGE_GRAPH.md) — граф целей, проблем, доказательств, решений, кода, тестов, метрик, результатов и lessons learned.
- [FATHER Meta Model v0.1](FATHER_META_MODEL.md) — типы узлов/связей, веса, жизненные циклы, трассировка до CodeArtifact и Goal Impact Model.
- [FATHER Dictionary v0.1](FATHER_DICTIONARY.md) — официальный контролируемый словарь терминов FATHER.
- [FATHER Information Architecture v0.1](FATHER_INFORMATION_ARCHITECTURE.md) — информационные домены, provenance, versioning, права изменения, retention и представления.
- [Core Entity Catalog v0.1](CORE_ENTITY_CATALOG.md) — базовые сущности, их назначение и MVP Core Set.
- [Relationship Catalog v0.1](RELATIONSHIP_CATALOG.md) — словарь инженерных связей, включая влияние и causal status.
- [Domain Model v0.1](DOMAIN_MODEL.md) — предметная модель для первой реализации Control Plane.
- [Decision Record Schema v0.1](DECISION_RECORD_SCHEMA.json) — машинно-читаемый контракт инженерного решения.
- [Django Model Mapping v0.1](DJANGO_MODEL_MAPPING.md) — отображение доменной модели на apps/models модульного Django-монолита.
- [ADR-002: Project Intelligence & Estimation Engine](../09_Decisions/ADR-002-Project-Intelligence-Estimation-Engine.md) — решение о выделении оценочного и разведывательного контура.

## Машинно-читаемые артефакты

- `GRAPH_SCHEMA_V0_1.json` — схема узлов и связей Engineering Knowledge Graph.
- `DECISION_RECORD_SCHEMA.json` — структура Decision Record.
- `../20_Legacy_Intelligence/SOKRAT_TO_SOCRATES_GRAPH_V0_1.json` — первый реальный тестовый граф наследования.

## Сквозной стандарт ворот

На каждом этапе действуют четыре обязательных класса проверки:

```text
              QUALITY
                 │
SECURITY ─── Engineering Stage ─── LEGAL / COMPLIANCE
                 │
              ECONOMICS
```

Результат каждого gate сохраняется как проверяемый артефакт со статусом, findings, evidence, владельцем и при необходимости Human Gate. `FAIL` не должен превращаться в молчаливое продолжение разработки.

## Планируемые архитектурные блоки

- Machine-readable Gate Record schema.
- Standards/Jurisdiction Profile model in Django.
- TraceLink / ChangeEvent / ImpactRecord implementation.
- Product Discovery & Expert Review Board.
- Solution Research / GitHub Intelligence / Reengineering.
- Knowledge Factory.
- Agent Factory.
- Django Control Plane / REST API.
- Security Architecture.
- Evaluation & Quality Gates.
- Replica / Domain Profile architecture.

## Статус

`EARLY ARCHITECTURE / DOMAIN BASELINE FORMED`

Архитектура развивается вместе с учебным PoC. Новые компоненты добавляются только после появления обоснованной функции или требования.

## Следующий шаг

Перевести Cross-Cutting Gates в машинно-читаемую модель: `GateDefinition`, `GateCheck`, `GateRun`, `Finding`, `StandardProfile`, `JurisdictionProfile`, `EconomicRecord`; связать их с Requirements Traceability Matrix и реализовать первый автоматический gate в Django/CI.
