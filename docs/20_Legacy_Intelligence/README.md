# 20 — Legacy Intelligence

> Анализ предыдущих поколений проектов и извлечение повторно используемых архитектурных, продуктовых, агентных и инженерных активов для FATHER.

## Назначение

Этот блок превращает старые проекты, прототипы, эксперименты и неудачные реализации в проверяемые активы нового FATHER.

FATHER не должен бездумно переносить старый код. Для каждого legacy-проекта применяется единый цикл:

```text
Repository Discovery
        ↓
Purpose Reconstruction
        ↓
Architecture Reconstruction
        ↓
Code / Documentation Review
        ↓
Security Review
        ↓
Capability Extraction
        ↓
Technical Debt
        ↓
Lessons Learned
        ↓
KEEP / ADAPT / REWRITE / DEFER / REJECT
        ↓
FATHER Knowledge Base
```

## Первая исследуемая группа

Текущий Legacy Research Set включает:

- `VictorKVS/MindForge`;
- `VictorKVS/Librarian-AI`;
- `VictorKVS/PRODUCT_SPEC_UniversalAgent`;
- `VictorKVS/mindforge-ai-telegram-bot`;
- `VictorKVS/AURORA-Intelligence-Platform-`;
- OSINT-агенты и OSINT-проекты;
- SOCRATES — местоположение в GitHub ещё уточняется;
- ENIGMA — местоположение в GitHub ещё уточняется;
- `VictorKVS/AI-Product-Architect`;
- `VictorKVS/MindForge-Engineer-Profile`;
- `VictorKVS/mf-std-001-compliance-pack`;
- `VictorKVS/mindforge-polygon-framework`;
- связанные прототипы, которые будут выявлены в ходе анализа.

## Ключевой принцип

> Старый проект оценивается не по количеству написанного кода, а по тому, какие проверяемые способности, решения, ошибки и знания он может передать FATHER.

## Типы извлекаемых активов

- продуктовые идеи;
- архитектурные решения;
- agent roles и agent workflows;
- OSINT-подходы;
- knowledge / RAG / graph-подходы;
- provider abstractions;
- API-контракты;
- security controls;
- тестовые паттерны;
- installer / scaffold generators;
- документационные стандарты;
- reusable code;
- anti-patterns;
- lessons learned;
- оценки трудоёмкости и сложности, если они доступны.

## Решения по наследованию

Для каждого найденного элемента используется один из статусов:

- `KEEP` — можно сохранить почти без изменений;
- `ADAPT` — идея или компонент полезны, но должны быть приведены к стандарту FATHER;
- `REWRITE` — функциональность нужна, но текущая реализация не подходит;
- `DEFER` — ценная идея, но преждевременна для текущего PoC;
- `REJECT` — переносить в FATHER нецелесообразно;
- `ARCHIVE_AS_LESSON` — технически не используется, но сохраняется как опыт.

## Текущие документы

- [LEGACY-001 — Previous Generation Portfolio Analysis](LEGACY-001-Previous-Generation-Portfolio-Analysis.md)

## Статус

`ACTIVE / RESEARCH`

Начат первый пробный анализ на основе MindForge и связанных legacy-проектов. AURORA обнаружена как отдельный репозиторий, но на момент первичной проверки репозиторий пуст. SOCRATES и ENIGMA пока не обнаружены как отдельные репозитории по имени и должны быть найдены по содержимому/истории других проектов.

## Следующие шаги

1. построить полный inventory legacy-репозиториев;
2. восстановить назначение каждого проекта;
3. построить Capability Map;
4. выявить дублирующиеся способности;
5. провести security review;
6. сформировать Asset Registry;
7. создать Migration Map в целевую архитектуру FATHER;
8. перенести подтверждённые паттерны в Knowledge Base.

## Навигация

- ↑ [Documentation Map](../README.md)
- 🏠 [Project Home](../../README.md)
- → [LEGACY-001](LEGACY-001-Previous-Generation-Portfolio-Analysis.md)
- ↔ [03 — Architecture](../03_Architecture/README.md)
- ↔ [90 — Innovation Registry](../../90_Innovation_Registry/README.md)
