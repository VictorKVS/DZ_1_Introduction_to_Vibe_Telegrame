# 03 — Architecture

> Архитектурный блок FATHER: как устроена фабрика продуктов, программ, знаний и AI-агентов.

[← К карте документации](../README.md) · [↑ Главный README](../../README.md)

## Назначение

Раздел фиксирует целевую и эволюционную архитектуру FATHER, границы подсистем, потоки данных, архитектурные варианты, trade-off и связь архитектуры со сроками, стоимостью, рисками и безопасностью.

## Место в FATHER

```text
Idea / Requirements
        ↓
Architecture
        ↓
Estimation / Security / Tests
        ↓
Implementation
        ↓
Verified Product / Agent
        ↓
Lessons Learned
```

Архитектура не считается обоснованной, если невозможно объяснить, какое требование или риск требует конкретного компонента и какие стоимость и эксплуатационную сложность он создаёт.

## Ключевые принципы

- Minimum Sufficient Architecture.
- Security by Construction + Security by Default.
- Evidence over opinion.
- Provider Independence.
- Human Decision Gates.
- Architecture Baseline + Change Management.
- План/факт и обучение на фактическом результате.
- Goal → Problem → Decision → Implementation → Outcome traceability.
- Knowledge Graph хранит причинно-связанную историю инженерной деятельности, а не только документы.
- Controlled Vocabulary: один термин имеет одно официальное значение в системе.

## Текущие документы

- [FATHER Delivery Intelligence](FATHER_DELIVERY_INTELLIGENCE.md) — Project/Technology OSINT, Estimation Engine, Talent Intelligence, Staffing, Risk, TCO и Delivery Control.
- [Engineering Knowledge Graph](ENGINEERING_KNOWLEDGE_GRAPH.md) — граф целей, проблем, доказательств, решений, кода, тестов, метрик, результатов и lessons learned.
- [FATHER Meta Model v0.1](FATHER_META_MODEL.md) — типы узлов/связей, веса, жизненные циклы, трассировка до CodeArtifact и Goal Impact Model.
- [FATHER Dictionary v0.1](FATHER_DICTIONARY.md) — официальный контролируемый словарь терминов FATHER.
- [FATHER Information Architecture v0.1](FATHER_INFORMATION_ARCHITECTURE.md) — информационные домены, provenance, versioning, права изменения, retention и представления.
- [Core Entity Catalog v0.1](CORE_ENTITY_CATALOG.md) — базовые сущности, их назначение и MVP Core Set.
- [Relationship Catalog v0.1](RELATIONSHIP_CATALOG.md) — словарь инженерных связей, включая влияние и causal status.
- [ADR-002: Project Intelligence & Estimation Engine](../09_Decisions/ADR-002-Project-Intelligence-Estimation-Engine.md) — решение о выделении оценочного и разведывательного контура.

## Планируемые архитектурные блоки

- Machine-readable Graph Schema.
- Domain Model / Django Models.
- Product Discovery & Expert Review Board.
- Solution Research / GitHub Intelligence / Reengineering.
- Knowledge Factory.
- Agent Factory.
- Django Control Plane / REST API.
- Security Architecture.
- Evaluation & Quality Gates.
- Replica / Domain Profile architecture.

## Статус

`EARLY ARCHITECTURE / EVOLVING`

Архитектура развивается вместе с учебным PoC. Новые компоненты добавляются только после появления обоснованной функции или требования.

## Следующий шаг

Создать машинно-читаемую `GRAPH_SCHEMA_V0_1.json` для узлов/связей и первый тестовый граф на реальном legacy-кейсе `Sokrat → SOCRATES`, затем перевести проверенную схему в `DOMAIN_MODEL.md` и Django Models.
