# FATHER — Engineering Knowledge Graph

**Status:** ACCEPTED / DESIGN

## Цель

Создать собственную инженерную базу знаний FATHER не только как RAG-хранилище документов, а как граф причинно-следственных связей между целями, проблемами, решениями, кодом, метриками и фактическими результатами.

Ключевой вопрос графа:

> Как конкретное знание, решение, компонент или изменение кода повлияло на достижение цели проекта?

## Основная идея

Обычная база знаний отвечает: `что мы знаем?`.

Engineering Knowledge Graph должен дополнительно отвечать:

- зачем это знание использовалось;
- какую проблему оно объясняло;
- какое решение было принято;
- какой код/конфигурация реализовали решение;
- какие тесты подтвердили реализацию;
- какие метрики изменились;
- достигнута ли цель;
- какой фактический эффект получен;
- стоит ли повторять решение в похожих проектах.

## Базовая цепочка

```text
GOAL
  ↓
PROBLEM / CONSTRAINT
  ↓
EVIDENCE / KNOWLEDGE
  ↓
ALTERNATIVES
  ↓
DECISION
  ↓
REQUIREMENT
  ↓
ARCHITECTURE / CAPABILITY
  ↓
CODE / CONFIG / PROMPT / DATA
  ↓
TEST / SECURITY CHECK
  ↓
METRIC
  ↓
OUTCOME
  ↓
LESSON LEARNED
  ↓
STANDARD / PATTERN / ANTI-PATTERN
```

## Типы узлов MVP

- `Goal`
- `Problem`
- `Constraint`
- `Hypothesis`
- `Source`
- `Evidence`
- `KnowledgeItem`
- `Requirement`
- `Alternative`
- `Decision`
- `Risk`
- `Capability`
- `ArchitectureComponent`
- `Repository`
- `CodeArtifact`
- `ConfigArtifact`
- `PromptArtifact`
- `DataArtifact`
- `TestCase`
- `SecurityControl`
- `Finding`
- `Metric`
- `Estimate`
- `Outcome`
- `LessonLearned`
- `Pattern`
- `AntiPattern`
- `Standard`
- `ExpertRole`
- `Methodology`

## Типы связей

Примеры машинно-читаемых отношений:

- `GOAL_DEPENDS_ON`
- `PROBLEM_BLOCKS_GOAL`
- `EVIDENCE_SUPPORTS`
- `EVIDENCE_CONTRADICTS`
- `DECISION_RESOLVES`
- `DECISION_SELECTED_ALTERNATIVE`
- `REQUIREMENT_DERIVED_FROM`
- `CAPABILITY_SATISFIES`
- `COMPONENT_IMPLEMENTS`
- `CODE_IMPLEMENTS_COMPONENT`
- `COMMIT_CHANGES_ARTIFACT`
- `TEST_VERIFIES`
- `SECURITY_CONTROL_MITIGATES`
- `RISK_THREATENS_GOAL`
- `METRIC_MEASURES_GOAL`
- `OUTCOME_CONFIRMS`
- `OUTCOME_REFUTES`
- `LESSON_DERIVED_FROM_OUTCOME`
- `PATTERN_GENERALIZED_FROM`
- `STANDARD_ADOPTED_FROM`
- `EXPERT_APPLIED_METHOD`

## Вес узла и связи

Один общий `weight` недостаточен. Для каждого знания/решения желательно хранить несколько независимых характеристик:

```yaml
confidence: 0.00-1.00
source_trust: 0.00-1.00
evidence_strength: 0.00-1.00
freshness: 0.00-1.00
relevance: 0.00-1.00
impact: 0.00-1.00
reuse_success: 0.00-1.00
risk: 0.00-1.00
```

Итоговый вычисляемый вес может зависеть от сценария. Например, для нормативного ответа выше вес `source_trust/freshness`, а для выбора архитектурного паттерна — `reuse_success/impact`.

## Влияние на цели

Для цели хранится baseline и target:

```yaml
goal_id: GOAL-001
metric: response_latency_p95
baseline: 4.2s
target: 2.0s
actual: 1.8s
status: achieved
```

Любое существенное решение связывается с ожидаемым эффектом:

```yaml
decision_id: DEC-042
expected_effect:
  metric: response_latency_p95
  delta_expected: -35%
confidence: 0.70
```

После эксплуатации добавляется фактический эффект:

```yaml
actual_effect:
  delta_actual: -48%
observation_window: 30d
```

Это позволяет считать не только качество решения, но и ошибку прогноза его эффекта.

## Связь с машинным кодом

Граф должен уметь доходить до конкретной реализации:

```text
Problem
 ↓
Decision
 ↓
Requirement
 ↓
Architecture Component
 ↓
Repository
 ↓
File / Function / Class / API / Migration
 ↓
Commit / PR
 ↓
Test
 ↓
Build / Release
 ↓
Runtime Metric
```

Для кода в MVP достаточно хранить ссылки и идентификаторы, а не копировать весь исходный код в Knowledge Graph:

```yaml
artifact_type: python_function
repository: VictorKVS/project
path: src/service/router.py
symbol: route_request
commit_sha: abc123
version: v0.4.1
```

Позже можно добавить AST/code graph и связи `CALLS`, `IMPORTS`, `DEPENDS_ON`, `MODIFIES`, `READS`, но только при подтверждённой пользе.

## Связь проблем между собой

Проблема является отдельной сущностью, а не строкой в отчёте.

Примеры связей:

```text
P-001 High latency
  ├─ CAUSED_BY → P-014 Excessive LLM calls
  ├─ CAUSED_BY → P-019 Large context
  ├─ AGGRAVATES → P-020 Cloud cost
  └─ BLOCKS → GOAL-003 Response < 2 sec
```

Решения также связываются:

```text
DEC-021 Semantic cache
  ├─ RESOLVES → P-014
  ├─ CONTRIBUTES_TO → GOAL-003
  ├─ CREATES_RISK → RISK-009 stale answer
  └─ REQUIRES_CONTROL → CTRL-012 cache invalidation
```

Так FATHER сможет видеть, что исправление одной проблемы может создать другую.

## Знание не равно факту

Статусы Knowledge Item:

- `CANDIDATE`
- `HYPOTHESIS`
- `SUPPORTED`
- `VERIFIED`
- `DISPUTED`
- `REFUTED`
- `STALE`
- `DEPRECATED`

Обязательные поля:

```yaml
id:
statement:
status:
source_ids: []
evidence_ids: []
valid_from:
valid_to:
confidence:
created_by:
reviewed_by:
version:
```

## Почему граф не надо начинать с Neo4j

На MVP графовая семантика должна существовать в модели данных, но физически может храниться в PostgreSQL:

- таблица `nodes`;
- таблица `edges`;
- JSONB metadata;
- pgvector для semantic retrieval;
- обычные FK для ключевых бизнес-связей.

Если реальные запросы покажут, что многошаговый traversal и graph analytics становятся узким местом, перенос/репликация части графа в Neo4j будет отдельным ADR.

## Метрики качества графа

- `evidence_coverage`
- `orphan_node_rate`
- `broken_trace_rate`
- `decision_to_outcome_coverage`
- `goal_to_metric_coverage`
- `code_traceability_coverage`
- `stale_knowledge_rate`
- `contradiction_rate`
- `reuse_success_rate`
- `prediction_error`

## Практическая ценность

Через накопление проектов система сможет отвечать на вопросы:

- какие проблемы чаще всего приводят к срыву цели;
- какие решения реально устраняли такие проблемы;
- какой код реализовывал решение;
- какие изменения дали наибольший эффект;
- какие решения выглядели правильными, но не дали результата;
- какие архитектурные паттерны работают для конкретного класса проектов;
- какие проблемы обычно возникают вместе;
- какое изменение минимально необходимо для изменения требуемой метрики;
- какое решение стоит переиспользовать в следующем проекте.

## Граница с внутренними рассуждениями LLM

Engineering Knowledge Graph не хранит скрытую chain-of-thought модели. Он хранит проверяемую инженерную трассу:

`evidence → alternative → decision → implementation → test → outcome`.

Это воспроизводимый и пригодный для аудита объект.

## MVP Gate

Первая версия считается реализованной, если для одного дочернего агента можно выполнить запрос:

> `Goal → Problem → Decision → Code Artifact → Test → Metric → Outcome`

и получить непрерывную трассу без ручного поиска по чатам и папкам.

## Навигация

- ↑ [Architecture](README.md)
- ↔ [Work Plan](../00_Project_Management/WORK_PLAN.md)
- ↔ [Development Log](../00_Project_Management/DEVELOPMENT_LOG.md)
- ↔ [Legacy Intelligence](../20_Legacy_Intelligence/README.md)
