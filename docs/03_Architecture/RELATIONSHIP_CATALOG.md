# FATHER — Relationship Catalog v0.1

**Status:** DRAFT / BASELINE  
**Purpose:** единый словарь связей Engineering Knowledge Graph.

## Принцип

Связь — это отдельный инженерный факт. Она имеет источник, дату, уверенность, направление, статус и при необходимости вес влияния.

Минимальная форма:

```yaml
id:
source_node:
relation_type:
target_node:
status:
confidence:
created_at:
evidence_ref:
metadata:
```

## Стратегия и цели

| Relation | Смысл |
|---|---|
| `PROJECT_PURSUes_GOAL` | проект направлен на достижение цели |
| `GOAL_MEASURED_BY` | цель измеряется метрикой |
| `PROBLEM_BLOCKS_GOAL` | проблема препятствует цели |
| `CONSTRAINT_LIMITS` | ограничение сужает пространство решений |
| `ASSUMPTION_AFFECTS` | предположение влияет на объект/решение |

## Требования и риски

| Relation | Смысл |
|---|---|
| `PROBLEM_CREATES_REQUIREMENT` | проблема породила требование |
| `REQUIREMENT_SUPPORTS_GOAL` | требование связано с целью |
| `REQUIREMENT_VERIFIED_BY` | требование проверяется критерием/тестом |
| `RISK_THREATENS` | риск угрожает цели, решению или компоненту |
| `CONTROL_MITIGATES_RISK` | контроль снижает риск |

## Знания и доказательства

| Relation | Смысл |
|---|---|
| `SOURCE_CONTAINS_EVIDENCE` | источник содержит доказательство |
| `EVIDENCE_SUPPORTS_CLAIM` | evidence поддерживает утверждение |
| `EVIDENCE_REFUTES_CLAIM` | evidence опровергает утверждение |
| `CLAIM_NORMALIZED_TO_KNOWLEDGE` | проверяемое утверждение стало KnowledgeItem |
| `KNOWLEDGE_CONTRADICTS` | знания противоречат друг другу |
| `KNOWLEDGE_DERIVED_FROM` | знание выведено из другого знания/evidence |
| `METHODOLOGY_APPLIES_TO` | методика применима к классу задач |

## Решения

| Relation | Смысл |
|---|---|
| `SESSION_ADDRESSES_PROBLEM` | DecisionSession решает проблему |
| `SESSION_CONSIDERS_ALTERNATIVE` | сессия рассматривает альтернативу |
| `EXPERT_REVIEWS_ALTERNATIVE` | эксперт оценил вариант |
| `REVIEW_USES_EVIDENCE` | экспертная оценка опирается на evidence |
| `DECISION_SELECTS` | решение выбирает альтернативу |
| `DECISION_REJECTS` | решение отклоняет альтернативу |
| `DECISION_RESOLVES_PROBLEM` | решение закрывает проблему полностью/частично |
| `DECISION_SUPPORTS_GOAL` | решение влияет на достижение цели |
| `HUMAN_GATE_APPROVES` | человек утвердил решение |
| `DECISION_SUPERSEDES` | новое решение заменяет старое |

## Архитектура и код

| Relation | Смысл |
|---|---|
| `CAPABILITY_SATISFIES_REQUIREMENT` | способность закрывает требование |
| `COMPONENT_REALIZES_CAPABILITY` | компонент реализует способность |
| `COMPONENT_DEPENDS_ON` | архитектурная зависимость |
| `INTERFACE_CONNECTS` | интерфейс связывает компоненты |
| `CODE_IMPLEMENTS_COMPONENT` | CodeArtifact реализует компонент |
| `CODE_IMPLEMENTS_REQUIREMENT` | код прямо связан с требованием |
| `CODE_DEPENDS_ON` | зависимость кода |
| `ARTIFACT_DESCRIBES` | документ/схема описывает объект |

## Тестирование и безопасность

| Relation | Смысл |
|---|---|
| `TEST_VERIFIES_REQUIREMENT` | тест проверяет требование |
| `TEST_VERIFIES_CAPABILITY` | тест проверяет capability |
| `TEST_RUN_EXECUTES_TEST` | запуск относится к TestCase |
| `TEST_RUN_PRODUCES_MEASUREMENT` | тест создаёт измерение |
| `FINDING_AFFECTS` | security finding относится к объекту |
| `CONTROL_IMPLEMENTED_BY` | контроль реализован кодом/конфигурацией/процессом |
| `EVIDENCE_PROVES_CONTROL` | evidence подтверждает работу контроля |

## Результаты и обучение

| Relation | Смысл |
|---|---|
| `DECISION_EXPECTS_OUTCOME` | решение имеет ожидаемый результат |
| `OUTCOME_MEASURED_BY` | результат подтверждается измерениями |
| `OUTCOME_CONFIRMS_DECISION` | факт поддерживает качество решения |
| `OUTCOME_WEAKENS_DECISION` | факт показывает слабость решения |
| `DEVIATION_EXPLAINS_OUTCOME` | отклонение помогает объяснить результат |
| `LESSON_DERIVED_FROM_OUTCOME` | урок получен из фактического результата |
| `LESSON_UPDATES_STANDARD` | урок изменил стандарт |
| `LESSON_UPDATES_METHODOLOGY` | урок скорректировал методику |
| `REUSE_RECORD_APPLIES_ASSET` | актив переиспользован в проекте |
| `REUSE_RESULT_STRENGTHENS_PATTERN` | успешное повторение усиливает доверие к паттерну |

## Агентная фабрика

| Relation | Смысл |
|---|---|
| `EXPERT_BLUEPRINT_REALIZES_ROLE` | blueprint реализует профессиональную роль |
| `EXPERT_USES_METHODOLOGY` | эксперт использует методику |
| `EXPERT_USES_KNOWLEDGE` | эксперт использует набор знаний |
| `AGENT_BLUEPRINT_REQUIRES_CAPABILITY` | агенту нужна способность |
| `AGENT_BLUEPRINT_USES_EXPERT` | агент использует экспертную роль |
| `AGENT_BUILD_INSTANTIATES_BLUEPRINT` | build создан из blueprint |
| `AGENT_USES_TOOL` | агент имеет доступ к инструменту |
| `POLICY_GOVERNS` | политика ограничивает агент/инструмент/решение |
| `EVALUATION_EVALUATES_BUILD` | eval относится к конкретной сборке |

## Связи влияния

Для причинно-ориентированных связей разрешены дополнительные поля:

```yaml
influence_direction: positive | negative | mixed | unknown
influence_strength: 0.0..1.0
confidence: 0.0..1.0
causality_status: observed | correlated | hypothesized | experimentally_supported
context_scope:
valid_from:
valid_to:
```

**Важно:** `influence_strength` не означает доказанную причинность. Причинный статус хранится отдельно.

## Запрещённые сокращения

Не использовать универсальные связи `RELATED_TO`, `HAS`, `USES`, если существует более точный тип. Они допустимы только как временный `UNCLASSIFIED_RELATION` до нормализации.

## MVP Relationship Set

Для первой реализации обязательны:

`PROJECT_PURSUes_GOAL`, `PROBLEM_BLOCKS_GOAL`, `PROBLEM_CREATES_REQUIREMENT`, `SOURCE_CONTAINS_EVIDENCE`, `EVIDENCE_SUPPORTS_CLAIM`, `SESSION_ADDRESSES_PROBLEM`, `SESSION_CONSIDERS_ALTERNATIVE`, `EXPERT_REVIEWS_ALTERNATIVE`, `DECISION_SELECTS`, `DECISION_RESOLVES_PROBLEM`, `CAPABILITY_SATISFIES_REQUIREMENT`, `CODE_IMPLEMENTS_COMPONENT`, `TEST_VERIFIES_REQUIREMENT`, `DECISION_EXPECTS_OUTCOME`, `OUTCOME_MEASURED_BY`, `LESSON_DERIVED_FROM_OUTCOME`.

## Навигация

- ↑ [Architecture](README.md)
- ↔ [Core Entity Catalog](CORE_ENTITY_CATALOG.md)
- ↔ [Information Architecture](FATHER_INFORMATION_ARCHITECTURE.md)
- ↔ [Engineering Knowledge Graph](ENGINEERING_KNOWLEDGE_GRAPH.md)
