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
- `VictorKVS/MindForge-v2.0x`;
- `VictorKVS/Librarian-AI`;
- `VictorKVS/PRODUCT_SPEC_UniversalAgent`;
- `VictorKVS/mindforge-ai-telegram-bot`;
- `VictorKVS/AURORA-Intelligence-Platform-`;
- `VictorKVS/Sokrat`;
- `VictorKVS/BotFerm`;
- `VictorKVS/KNOWLEDGE_MASTER`;
- `VictorKVS/gpt-agent`;
- OSINT-агенты и OSINT-проекты;
- ENIGMA — отдельный репозиторий пока не подтверждён, но концепция подтверждена в `KNOWLEDGE_MASTER`;
- `VictorKVS/AI-Product-Architect`;
- `VictorKVS/MindForge-Engineer-Profile`;
- `VictorKVS/mf-std-001-compliance-pack`;
- `VictorKVS/mindforge-polygon-framework`;
- связанные прототипы, выявляемые в ходе анализа.

## Ключевой принцип

> Старый проект оценивается не по количеству написанного кода, а по тому, какие проверяемые способности, решения, ошибки и знания он может передать FATHER.

## Типы извлекаемых активов

- продуктовые идеи;
- архитектурные решения;
- agent roles и agent workflows;
- системы коллективного принятия решений;
- OSINT-подходы;
- knowledge / RAG / graph-подходы;
- provider abstractions;
- API и capability-контракты;
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

Происхождение знания дополнительно помечается:

- `REMEMBERED` — восстановлено по воспоминаниям;
- `VERIFIED` — подтверждено GitHub-кодом или документацией;
- `ADOPTED` — официально принято в текущую архитектуру FATHER.

## Текущие документы

- [LEGACY-001 — Previous Generation Portfolio Analysis](LEGACY-001-Previous-Generation-Portfolio-Analysis.md)
- [LEGACY-002 — Capability & Reuse Map](LEGACY-002-Capability-and-Reuse-Map.md)
- [Development Log](../00_Project_Management/DEVELOPMENT_LOG.md) — причины решений и история развития.

## Уже подтверждено

В `Sokrat` найдены research sessions, expert reviews, discussion rounds, модель-судья, quality score и сохранение истории сессии. Этот актив принят как предок нового **SOCRATES Decision Engine**.

В `KNOWLEDGE_MASTER` подтверждены графовая база знаний, SPHINX, ENIGMA, evidence validation и expert feedback loop.

В `MindForge-v2.0x` подтверждены OSINT Hub, специализированные intelligence-агенты, telemetry и архитектурная лаборатория.

В `PRODUCT_SPEC_UniversalAgent` подтверждены Capability Registry, Policy Enforcement и Agent-ready Gateway.

В `BotFerm` подтверждены YAML-генерация проектов, Agent DNA, DevSecOps-контур и идея Smart Agent Factory.

## Статус

`ACTIVE / RESEARCH`

## Следующие шаги

1. продолжить inventory legacy-репозиториев;
2. дополнить Capability & Reuse Map конкретными файлами и кодовыми активами;
3. выполнить security review повторно используемых компонентов;
4. построить Asset Registry и Anti-pattern Registry;
5. создать Migration Map в целевую архитектуру FATHER;
6. привязать каждый перенос к записи в Development Log;
7. переносить подтверждённые паттерны в Knowledge Base только после проверки.

## Навигация

- ↑ [Documentation Map](../README.md)
- 🏠 [Project Home](../../README.md)
- → [LEGACY-001](LEGACY-001-Previous-Generation-Portfolio-Analysis.md)
- → [LEGACY-002](LEGACY-002-Capability-and-Reuse-Map.md)
- → [Development Log](../00_Project_Management/DEVELOPMENT_LOG.md)
- ↔ [03 — Architecture](../03_Architecture/README.md)
- ↔ [09 — Decisions](../09_Decisions/README.md)
- ↔ [90 — Innovation Registry](../../90_Innovation_Registry/README.md)
