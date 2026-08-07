# Documentation Map

> Этот раздел является навигационным уровнем документации FATHER.

Каждый функциональный блок проекта обязан иметь собственный `README.md`, который кратко объясняет назначение блока, его границы, ключевые артефакты, текущий статус и ссылки на дочерние документы.

## Правило навигации

Иерархия документации строится сверху вниз:

```text
README.md проекта
    ↓
docs/README.md
    ↓
README.md функционального блока
    ↓
детальные документы / ADR / спецификации / схемы
```

Это правило является частью стандарта FATHER: агент должен создавать и сопровождать навигацию одновременно с созданием новых блоков и документов.

## Разделы

- [00 — Project Management](00_Project_Management/README.md) — стандарты ведения проекта, документации и будущего инженерного портала.
  - [FATHER Documentation Standard](00_Project_Management/DOCUMENTATION_STANDARD.md)
  - [GitHub Pages / Engineering Portal Plan](00_Project_Management/GITHUB_PAGES_PLAN.md)
- [03 — Architecture](03_Architecture/README.md) — архитектура FATHER, производственные контуры, Delivery Intelligence, будущие архитектурные схемы.
- [09 — Decisions](09_Decisions/README.md) — архитектурные решения ADR и история ключевых технических решений.
- [20 — Legacy Intelligence](20_Legacy_Intelligence/README.md) — анализ предыдущих поколений проектов, извлечение capabilities, reusable assets, lessons learned и план миграции в FATHER.
  - [LEGACY-001 — Previous Generation Portfolio Analysis](20_Legacy_Intelligence/LEGACY-001-Previous-Generation-Portfolio-Analysis.md)
- [90 — Innovation Registry](../90_Innovation_Registry/README.md) — реестр идей, будущих продуктов и интеллектуальных активов.

## Стандарт README блока

Каждый `README.md` блока должен содержать минимум:

1. назначение блока;
2. его место в общей архитектуре;
3. входы и выходы;
4. основные сущности или процессы;
5. список текущих документов;
6. статус реализации;
7. следующие шаги;
8. ссылки вверх и вниз по дереву документации.

Полное правило: [FATHER Documentation Standard](00_Project_Management/DOCUMENTATION_STANDARD.md).

## Принцип сопровождения агентом

При создании нового каталога или крупного функционального блока FATHER должен автоматически:

- создать локальный `README.md`;
- добавить ссылку на него в родительский `README.md`;
- при необходимости добавить ссылку в главный `README.md`;
- обновить статус блока;
- не оставлять «осиротевшие» документы без навигации;
- проверять битые ссылки и пригодность документов к публикации.

## Будущий портал

Markdown в Git остаётся исходной инженерной документацией. На его основе планируется GitHub Pages / Engineering Portal, а затем тот же граф документов будет использоваться Django Control Plane и базой знаний FATHER.

Подробнее: [GitHub Pages / Engineering Portal Plan](00_Project_Management/GITHUB_PAGES_PLAN.md).

## Навигация

- 🏠 [Главный README проекта](../README.md)
- → [00 — Project Management](00_Project_Management/README.md)
- → [03 — Architecture](03_Architecture/README.md)
- → [09 — Decisions](09_Decisions/README.md)
- → [20 — Legacy Intelligence](20_Legacy_Intelligence/README.md)
- → [90 — Innovation Registry](../90_Innovation_Registry/README.md)
