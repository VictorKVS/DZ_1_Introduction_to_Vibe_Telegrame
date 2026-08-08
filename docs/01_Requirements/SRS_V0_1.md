# FATHER — SRS v0.1

**Status:** DRAFT / BASELINE CANDIDATE  
**Scope:** первая сквозная вертикаль FATHER

## 1. Цель

Построить минимальную сквозную систему, которая принимает инженерную задачу, собирает и связывает доказательства, получает структурированные экспертные оценки, формирует решение через SOCRATES-lite, создаёт Decision Record и Blueprint, производит одного дочернего агента, проводит тесты/ИБ-проверки и сохраняет фактический результат в Organizational Memory.

## 2. Граница первой версии

Входит:

`Request → Project → Source/Evidence → Expert Reviews → Decision Session → Decision → Blueprint → Agent Build → Test/Security → Outcome → Lesson`

Не входит в обязательный MVP:

- Kubernetes;
- полноценный Neo4j;
- десятки LLM одновременно;
- автономное принятие существенных решений без Human Gate;
- сложный dark-web/geo intelligence;
- отдельный микросервис на каждую функцию.

## 3. Пользователи

- FATHER Operator — создаёт проект, загружает материалы, запускает процессы;
- Analyst — уточняет проблему, evidence и критерии;
- Architect — оценивает архитектурные варианты;
- Security Architect — оценивает ИБ-риски;
- Approver — утверждает существенные решения;
- Child Agent User — использует произведённого агента.

## 4. Функциональные требования

### FR-001 Project Intake
Система должна создавать Project и Request/Idea с уникальными ID, целью, описанием, статусом, автором и временными метками.

**Acceptance:** созданный Request можно однозначно связать с Project и Goal.

### FR-002 Goal & Problem Traceability
Система должна позволять фиксировать цели, проблемы, ограничения и предположения и связывать их типизированными отношениями.

**Acceptance:** путь `Goal → Problem` восстанавливается программно.

### FR-003 Source Registration
Каждый источник должен получать provenance: тип, URI/путь, время получения, автора/поставщика при наличии, hash и классификацию.

**Acceptance:** critical evidence без source_ref не получает статус VERIFIED.

### FR-004 Evidence Management
Система должна создавать Evidence, связывать его с Source и Claim/Problem/Decision и хранить confidence/status/freshness.

### FR-005 Expert Blueprint
Система должна хранить профессиональный контракт Expert Role независимо от конкретной LLM: responsibility, methodology, criteria, evidence requirements, tools, constraints, escalation rules и metrics.

### FR-006 Expert Review
Эксперт должен возвращать структурированный review минимум с recommendation, confidence, evidence refs, assumptions, risks, alternatives и objections.

### FR-007 Decision Session
SOCRATES-lite должен создавать Decision Session, принимать минимум одну Alternative и экспертные reviews, фиксировать agreement/disagreement и формировать Decision Record.

### FR-008 Human Gate
Для решений, отмеченных как существенные, Decision не может получить ACCEPTED/IMPLEMENTED без результата Human Gate.

### FR-009 Decision Record
Каждое решение должно соответствовать `DECISION_RECORD_SCHEMA.json` и содержать проблему, альтернативы, выбранный вариант, rationale, evidence, expected effects и validation plan.

### FR-010 Blueprint
Система должна преобразовать утверждённые требования и решения в versioned Agent/Product Blueprint.

### FR-011 Child Agent Build
По Blueprint должна создаваться версия Agent Build с трассировкой к требованиям, решениям и исходному blueprint.

### FR-012 Test Gate
Agent Build не получает RELEASED, пока не пройдены обязательные acceptance/security тесты.

### FR-013 Outcome Capture
После использования/проверки система должна сохранять фактические Outcome и Measurement, связанные с Decision/Build/Goal.

### FR-014 Plan-Fact
Для сроков, стоимости и ключевых метрик должны храниться planned и actual значения, deviation и причина отклонения.

### FR-015 Lesson Learned
После закрытия цикла система должна создавать Lesson Learned или явно фиксировать `NO_NEW_LESSON`.

### FR-016 Knowledge Graph
Все основные артефакты первой вертикали должны быть представлены как узлы/связи инженерного графа либо иметь адаптер в этот граф.

### FR-017 Repository Traceability
CodeArtifact должен ссылаться минимум на repository, path и commit SHA/version.

### FR-018 Audit Log
Изменения критичных сущностей должны оставлять audit record: кто, что, когда, старое/новое значение или версию.

### FR-019 REST API
Основные сущности первой вертикали должны быть доступны через versioned REST API `/api/v1/`.

### FR-020 Admin UI
Оператор должен иметь административный UI для просмотра Project, Evidence, Decision Session, Decision, Blueprint, Build, TestRun и Outcome.

## 5. Бизнес-правила

- BR-001: LLM output сам по себе не является verified knowledge.
- BR-002: существенный Decision требует evidence либо явного статуса `INSUFFICIENT_EVIDENCE`.
- BR-003: внутренние скрытые reasoning traces модели не хранятся как источник истины; хранится структурированное инженерное обоснование.
- BR-004: accepted requirement должен иметь acceptance criterion.
- BR-005: released build должен быть связан с versioned blueprint и тестовым результатом.
- BR-006: deletion критических артефактов предпочтительно заменяется archive/deprecate с сохранением истории.

## 6. Минимальный сценарий приёмки MVP

1. Создать Project и Goal.
2. Зарегистрировать Problem.
3. Добавить минимум два Source и Evidence.
4. Создать минимум две Alternative.
5. Запустить три Expert Role: Product/BA, System Architect, Security Architect.
6. Создать Decision Session и Decision Record.
7. Подтвердить Human Gate.
8. Создать Blueprint.
9. Создать дочерний Web+Telegram Agent Build.
10. Выполнить обязательные тесты/ИБ gate.
11. Зафиксировать Outcome, plan/fact и Lesson Learned.
12. Восстановить всю цепочку через API без чтения чата.

## 7. Traceability Gate

MVP считается функционально доказанным, если API может вернуть непрерывную цепочку:

`Goal → Problem → Evidence → Alternative → ExpertReview → Decision → Blueprint → AgentBuild → TestRun → Outcome → LessonLearned`.

## Навигация

- ↑ [Requirements](README.md)
- → [NFR v0.1](NFR_V0_1.md)
- ↔ [Domain Model](../03_Architecture/DOMAIN_MODEL.md)
- ↔ [REST API Contract](../07_API/REST_API_CONTRACT_V0_1.md)
