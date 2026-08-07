# FATHER — Work Plan

**Status:** ACTIVE  
**Planning horizon:** MVP → validated factory loop  
**Principle:** каждый этап обязан оставлять измеримый артефакт, запись в Development Log и критерий проверки.

## Цель ближайшего цикла

Построить первую сквозную производственную цепочку FATHER:

`Idea / Request → Intake → Research → Expert Review → Decision → Blueprint → Child Agent → Tests/Security → Deployment → Outcome → Organizational Memory`.

Первая версия не пытается реализовать всю целевую архитектуру. Цель — доказать, что один проект можно провести через весь цикл и получить воспроизводимый результат с полной трассировкой решений, затрат и качества.

---

## Phase 0 — Baseline и инвентаризация

**Цель:** закрепить текущее состояние проекта и наследства.

Работы:

1. завершить inventory legacy-репозиториев;
2. для каждого значимого проекта создать capability card;
3. заполнить `KEEP / ADAPT / REWRITE / DEFER / REJECT`;
4. выявить повторяющиеся паттерны;
5. выделить код/документы, пригодные для переноса;
6. сформировать список anti-patterns;
7. связать выводы с Development Log.

**Результат:** `Legacy Asset Registry` и подтверждённая карта повторного использования.

**Gate:** мы знаем, что переносим, что переписываем и что не берём в MVP.

---

## Phase 1 — Требования и модель продукта

**Цель:** перевести концепцию FATHER в проверяемые требования первой версии.

Документы:

- Product Vision / Product Scope;
- Business Requirements;
- SRS;
- NFR;
- Use Cases;
- Acceptance Criteria;
- Risk Register;
- Security Requirements;
- Data Classification;
- Initial Cost/Time Estimate.

Ключевые вопросы:

- кто первый пользователь FATHER;
- какая одна задача проходит весь цикл;
- какой дочерний агент производится первым;
- какие данные обязательны;
- где требуется Human Gate;
- какие метрики подтверждают успех.

**Gate:** требования достаточно определены, чтобы построить архитектуру и тесты до написания основного кода.

---

## Phase 2 — Domain Model и Decision/Knowledge Model

**Цель:** описать сущности, которые должны жить дольше конкретной LLM или интерфейса.

Минимальные сущности:

- Project;
- Request / Idea;
- Source;
- Evidence;
- Knowledge Item;
- Expert Role;
- Methodology;
- Decision Session;
- Alternative;
- Expert Review;
- Decision;
- Risk;
- Estimate;
- Blueprint;
- Agent Build;
- Test Run;
- Security Finding;
- Outcome;
- Lesson Learned.

Для каждой сущности фиксируются ID, версия, источник, дата, статус, связи и audit fields.

**Gate:** можно восстановить путь от исходной задачи до финального решения и результата без чтения чатов.

---

## Phase 3 — Django Control Plane

**Цель:** создать минимальную панель управления FATHER.

Стек MVP:

- Python;
- Django;
- Django REST Framework;
- PostgreSQL;
- pgvector;
- Redis/Celery только при подтверждённой необходимости.

Минимальные функции:

- проекты;
- карточки запросов;
- источники и вложения;
- эксперты;
- decision sessions;
- решения;
- оценки;
- blueprints;
- build/test history;
- admin panel;
- REST API;
- audit log.

**Gate:** основные сущности создаются, читаются и связываются через UI/API.

---

## Phase 4 — Knowledge Foundation + SPHINX-lite

**Цель:** FATHER должен работать с доказательствами, а не только с текстом LLM.

MVP:

- ingest документов;
- hash/provenance;
- chunking;
- embeddings;
- PostgreSQL + pgvector retrieval;
- source metadata;
- evidence links;
- confidence/status;
- freshness/version fields;
- SPHINX-lite: ответ/вывод не считается подтверждённым без связанного evidence.

**Gate:** любой важный вывод можно связать с исходным источником или явно пометить как гипотезу/неподтверждённое утверждение.

---

## Phase 5 — AURORA-lite

**Цель:** автоматически собирать внешнюю информацию для проектного анализа.

Первая версия:

- поиск похожих решений;
- поиск GitHub-проектов;
- поиск документации и методик;
- сведения о технологиях;
- базовые рыночные/проектные ориентиры;
- сохранение источников и даты получения;
- дедупликация;
- передача данных в Knowledge Foundation.

Не включать в MVP сложный dark-web/geo/socio intelligence без конкретного сценария.

**Gate:** один запрос создаёт воспроизводимый research package с источниками.

---

## Phase 6 — Expert Blueprint Library

**Цель:** формализовать цифровых специалистов независимо от LLM-провайдера.

Для каждого эксперта:

- role;
- responsibility;
- domain knowledge;
- methodology;
- decision criteria;
- required evidence;
- tools;
- constraints;
- escalation rules;
- metrics;
- cost policy.

Первые три роли MVP:

1. Product / Business Analyst;
2. System Architect;
3. Security Architect.

Дополнительно — Estimator как следующий кандидат.

**Gate:** одна и та же роль может быть запущена на разных моделях без изменения её профессионального контракта.

---

## Phase 7 — SOCRATES-lite Decision Engine

**Цель:** реализовать управляемую выработку решения.

Цикл:

`Task → Evidence → Alternatives → Expert Reviews → Conflict Detection → Synthesis → Human Gate → Decision Record`.

Обязательные метрики сессии:

- experts_used;
- models_used;
- tokens;
- latency;
- monetary_cost;
- number_of_alternatives;
- agreement/disagreement;
- evidence_coverage;
- confidence;
- human_override;
- final decision.

Внутренние скрытые рассуждения моделей не являются журналом проекта. Хранится структурированное обоснование решения, факторы, альтернативы, evidence и причины отклонения вариантов.

**Gate:** SOCRATES формирует решение, которое человек может проверить и позднее сопоставить с фактическим результатом.

---

## Phase 8 — Estimation & Economics Engine

**Цель:** научить FATHER считать время, стоимость и неопределённость.

Методы первой версии:

- Analogous;
- Parametric;
- Bottom-Up;
- PERT;
- contingency/risk buffer.

Хранить:

- method;
- assumptions;
- confidence range;
- P50/P80 при наличии данных;
- planned hours/cost;
- actual hours/cost;
- deviation;
- cause of deviation.

Экономические критерии по задаче:

- TCO;
- ROI;
- NPV;
- payback;
- Cost of Delay;
- Reasoning Cost.

**Gate:** первая оценка проекта после завершения может быть сравнена с фактом и дать ошибку оценки.

---

## Phase 9 — Blueprint / Product Generator

**Цель:** восстановить лучшие идеи BotFerm и UniversalAgent как управляемый генератор проекта.

Вход:

- approved requirements;
- architecture;
- security requirements;
- expert decisions;
- selected stack;
- capability list.

Выход:

- repository structure;
- README/navigation;
- configs;
- API skeleton;
- data models;
- tests;
- security checks;
- CI skeleton;
- deployment configuration;
- agent manifest.

**Gate:** FATHER создаёт воспроизводимый каркас дочернего проекта по blueprint, а не через свободную генерацию файлов.

---

## Phase 10 — Первый дочерний агент

**Цель:** доказать фабричный цикл на одном реальном продукте.

Рекомендуемый первый продукт: простой Web + Telegram специализированный агент на проверенной базе знаний.

Необходимые свойства:

- один домен;
- один набор ролей;
- ограниченный набор tools;
- Web + Telegram;
- API;
- RAG;
- audit;
- security baseline;
- acceptance tests.

**Gate:** созданный агент запускается, проходит тесты и трассируется обратно до blueprint и решений FATHER.

---

## Phase 11 — Test & Security Gates

**Цель:** встроить качество и ИБ в производство, а не проверять после него.

Минимальный pipeline:

- unit tests;
- integration tests;
- API tests;
- RAG/evaluation tests;
- prompt injection tests;
- authorization tests;
- secrets scan;
- SAST;
- dependency scan;
- container scan при использовании контейнеров;
- basic DAST;
- acceptance test.

**Gate:** build не получает статус RELEASED при провале обязательного quality/security gate.

---

## Phase 12 — Outcome / Plan-Fact Loop

**Цель:** замкнуть обучение организации.

После эксплуатации сохраняются:

- фактические сроки;
- фактическая стоимость;
- дефекты;
- переделки;
- security findings/incidents;
- usage;
- latency;
- reliability;
- пользовательская оценка;
- бизнес-метрики, если доступны;
- причины отклонений.

Далее:

`Decision → Expected Effect → Actual Outcome → Evaluation → Lesson Learned → Standard/Template/Metric Update`.

**Gate:** завершённый проект изменяет Organizational Memory или явно фиксирует, что новых знаний не получено.

---

## Phase 13 — GitHub Pages / Engineering Portal

После стабилизации документов:

- включить GitHub Pages;
- выбрать MkDocs Material / Docusaurus отдельным ADR;
- строить навигацию из существующих Markdown;
- публиковать Architecture, Decisions, Legacy, Roadmap, Standards;
- не публиковать secrets, внутренние данные заказчиков и чувствительные сведения.

**Gate:** документация читается как единый инженерный портал и остаётся синхронизированной с репозиторием.

---

## Что сознательно отложено

До появления измеримой необходимости не вводим автоматически:

- Kubernetes;
- Neo4j как обязательную БД;
- отдельные Qdrant/Milvus при достаточности pgvector;
- десятки LLM одновременно;
- полную автономность существенных решений;
- сложный multi-agent swarm;
- отдельный микросервис на каждую функцию;
- тяжёлую enterprise-инфраструктуру.

Эти элементы имеют статус `DEFER`, а не `REJECT`.

---

## Ритм разработки

Каждый крупный шаг проходит одинаково:

1. проблема/цель;
2. варианты;
3. решение;
4. запись в `DEVELOPMENT_LOG.md`;
5. документ/ADR при необходимости;
6. реализация;
7. тест;
8. security review;
9. plan/fact;
10. lessons learned;
11. обновление Knowledge/Standards.

## Ближайшие 5 практических действий

1. Завершить Legacy Asset Registry по найденным репозиториям.
2. Написать SRS/NFR первой вертикали FATHER.
3. Зафиксировать Domain Model и Decision Record schema.
4. Поднять Django + PostgreSQL control plane и базовые сущности.
5. Реализовать Knowledge Foundation и первую SOCRATES-lite сессию на трёх экспертных ролях.

После этих пяти действий проект перейдёт от архитектурной концепции к проверяемому работающему ядру.

## Навигация

- ↑ [00 — Project Management](README.md)
- ↔ [Development Log](DEVELOPMENT_LOG.md)
- ↔ [Documentation Standard](DOCUMENTATION_STANDARD.md)
- ↔ [Legacy Intelligence](../20_Legacy_Intelligence/README.md)
- ↔ [Architecture](../03_Architecture/README.md)
- ↔ [Decisions](../09_Decisions/README.md)
