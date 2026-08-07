# FATHER — Core Entity Catalog v0.1

**Status:** DRAFT / BASELINE  
**Purpose:** единый каталог базовых сущностей FATHER перед проектированием Django Models и API.

## Классы сущностей

| Entity | Назначение | Ключевые поля | Версионирование |
|---|---|---|---|
| Organization | организация/контур, которому принадлежит память и проекты | name, type, owner | да |
| Person | человек, участник, ответственный, эксперт | identity_ref, role, org | по изменениям |
| Project | единица производственного цикла | goal, scope, status, dates | да |
| Goal | измеримая цель | statement, metric, target, deadline | да |
| Problem | препятствие/неудовлетворённое состояние | description, severity, status | да |
| Constraint | ограничение | type, value, source | да |
| Assumption | предположение, влияющее на решение | statement, confidence, expiry | да |
| Requirement | проверяемое требование | text, type, priority, source | да |
| AcceptanceCriterion | условие приёмки | condition, measurement | да |
| Risk | неопределённость с влиянием | probability, impact, owner | да |
| Source | исходный источник | uri/path, author, date, hash | неизменяемый snapshot |
| Evidence | фрагмент/наблюдение, подтверждающее или опровергающее утверждение | source, locator, strength | да |
| Claim | проверяемое утверждение | statement, status, confidence | да |
| KnowledgeItem | нормализованное знание | content, status, valid_from/to | да |
| Contradiction | конфликт знаний/источников | items, severity, resolution | да |
| Methodology | формализованный метод работы/оценки | steps, applicability, limitations | да |
| Pattern | повторно применимый успешный подход | context, solution, evidence | да |
| AntiPattern | повторяющийся вредный подход | context, consequence | да |
| ExpertRole | профессиональная функция | responsibility, authority | да |
| ExpertBlueprint | цифровая спецификация специалиста | role, methods, tools, metrics | да |
| DecisionSession | процесс выработки решения | task, experts, evidence, cost | да |
| Alternative | рассматриваемый вариант | description, benefits, costs, risks | да |
| ExpertReview | структурированная позиция эксперта | recommendation, score, evidence | неизменяемый результат |
| Decision | утверждённый выбор | chosen_alternative, rationale, approver | да |
| HumanGate | событие ручного согласования | reason, actor, result | audit record |
| Estimate | оценка времени/стоимости/ресурсов | method, p50/p80, assumptions | да |
| Capability | полезная способность системы | contract, maturity, owner | да |
| Component | архитектурный компонент | responsibility, interfaces | да |
| Interface | контракт взаимодействия | protocol/schema/version | да |
| Repository | репозиторий исходного кода | url, default_branch | по состоянию |
| CodeArtifact | ссылка на код/символ/модуль | repo, path, symbol, commit_sha | commit-based |
| ConfigurationArtifact | конфигурация | path, schema, version | да |
| TestCase | определение проверки | target, steps, expected | да |
| TestRun | фактическое выполнение проверки | test_case, result, evidence | immutable |
| SecurityFinding | ИБ-находка | severity, target, status | audit history |
| Control | мера/контроль | requirement, implementation, evidence | да |
| Metric | определение измерения | name, unit, formula | да |
| Measurement | конкретное измеренное значение | metric, value, time, context | immutable |
| Outcome | фактический результат решения/проекта | expected, actual, delta | да |
| Deviation | отклонение план/факт | planned, actual, reason | immutable after approval |
| LessonLearned | вывод из результата | observation, applicability, evidence | да |
| Standard | принятое правило повторного использования | rule, scope, exceptions | да |
| Template | повторно используемый артефакт | type, source, version | да |
| ReuseRecord | факт повторного применения | asset, project, result | immutable |
| AgentBlueprint | спецификация создаваемого агента | capabilities, knowledge, policies | да |
| AgentBuild | конкретная сборка агента | blueprint_version, build_id, status | immutable |
| ToolCapability | доступный агенту инструмент | contract, permissions, risk | да |
| Policy | ограничение/правило исполнения | condition, action, priority | да |
| EvaluationRun | оценка поведения агента/модели | suite, scores, cost | immutable |
| Artifact | универсальная ссылка на документ/отчёт/схему | type, location, hash | да |

## Обязательные системные поля

Для большинства сущностей:

```yaml
id: UUID
status: enum
version: string/int
created_at: datetime
updated_at: datetime
created_by: actor_ref
project_id: UUID|null
classification: enum
metadata: jsonb
```

## Что не объединяем в одну сущность

- `Source` и `Evidence`: источник может содержать много доказательств.
- `Claim` и `KnowledgeItem`: утверждение ещё может быть спорным, знание прошло нормализацию/оценку.
- `DecisionSession` и `Decision`: процесс и итог — разные объекты.
- `Metric` и `Measurement`: определение измерения и факт измерения — разные объекты.
- `Capability` и `Component`: способность описывает «что умеем», компонент — «чем реализуем».
- `ExpertRole` и `LLM model`: роль должна переживать смену модели.

## MVP Core Set

Для первого Django-контура достаточно начать с:

`Project, Goal, Problem, Requirement, Source, Evidence, KnowledgeItem, ExpertRole, DecisionSession, Alternative, ExpertReview, Decision, Risk, Estimate, Capability, Artifact, TestRun, Metric, Measurement, Outcome, LessonLearned`.

Остальные сущности добавляются по мере появления реального сценария.

## Навигация

- ↑ [Architecture](README.md)
- ↔ [Information Architecture](FATHER_INFORMATION_ARCHITECTURE.md)
- ↔ [Relationship Catalog](RELATIONSHIP_CATALOG.md)
- ↔ [Meta Model](FATHER_META_MODEL.md)
