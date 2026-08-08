# FATHER — Impact Analysis Model v0.1

**Status:** BASELINE / EVOLVING  
**Purpose:** определять, что необходимо пересмотреть, изменить и повторно проверить при изменении требования, решения, архитектуры, кода, стандарта или данных.

## Задача

FATHER должен отвечать не только на вопрос «что связано?», но и на вопрос «что может сломаться или потребовать пересмотра, если объект X изменится?».

## Основной принцип

Любое управляемое изменение создаёт `ChangeEvent`.

`ChangeEvent → ChangedObject → Graph Traversal → Impact Set → Required Actions → Verification → Updated Baseline`

## Типы изменений

- REQUIREMENT_CHANGE
- STANDARD_CHANGE
- ARCHITECTURE_CHANGE
- SECURITY_CONTROL_CHANGE
- API_CHANGE
- DATA_MODEL_CHANGE
- CODE_CHANGE
- DEPENDENCY_CHANGE
- CONFIGURATION_CHANGE
- TEST_CHANGE
- MODEL_PROVIDER_CHANGE
- KNOWLEDGE_SOURCE_CHANGE

## Уровни влияния

- `DIRECT` — непосредственная зависимость;
- `TRANSITIVE` — влияние через другие объекты;
- `POTENTIAL` — возможное влияние, требуется экспертная проверка;
- `NONE` — проверено, влияния нет.

## Критичность

Для каждого объекта рассчитывается не один универсальный вес, а профиль влияния:

```yaml
impact:
  goal: 0.0
  business: 0.0
  architecture: 0.0
  security: 0.0
  compliance: 0.0
  data: 0.0
  testing: 0.0
  operations: 0.0
  cost: 0.0
  schedule: 0.0
```

Итоговая приоритизация зависит от StandardsProfile, класса проекта и текущего этапа жизненного цикла.

## Пример: изменение кода

`CodeArtifact changed`

Система ищет:

1. какие Components реализуются этим кодом;
2. какие Requirements реализуют эти Components;
3. какие Decisions определили их устройство;
4. какие Security Controls зависят от компонента;
5. какие TestCases проверяют поведение;
6. какие API/Data contracts затрагиваются;
7. какие документы должны быть пересобраны;
8. какие Metrics/Outcomes могут измениться.

Результат:

```yaml
change_id: CHG-001
affected:
  requirements: [FR-004, NFR-SEC-003]
  decisions: [ADR-014]
  components: [EvidenceStore]
  tests: [TC-EVID-001, TC-AUTH-004]
  docs: [SRS, SecurityArchitecture]
required_actions:
  - rerun_tests
  - security_review
  - update_rtm
  - regenerate_docs
```

## Пример: изменение стандарта

`Standard Clause changed`

Путь:

`StandardClause → Requirement/Control → Architecture → Code/Test → Active Projects`

FATHER формирует список проектов, которым требуется review, и не переписывает автоматически ранее утверждённые решения без Human Gate.

## Blast Radius

Вводится метрика `change_blast_radius`:

```text
число затронутых управляемых объектов
× критичность связей
× зрелость/статус проекта
```

Она используется для выбора процесса изменения:

- LOW — обычный change;
- MEDIUM — architecture/test review;
- HIGH — Change Request + security/architecture gates;
- CRITICAL — formal approval + rollback plan + full regression scope.

## Обязательный результат Impact Analysis

Каждый анализ создаёт:

- change summary;
- impacted objects;
- evidence of dependency;
- uncertainty list;
- required reviews;
- required tests;
- documentation updates;
- estimate delta;
- risk delta;
- release/rollback implications;
- approver when required.

## Machine workflow

```text
Change
  ↓
Identify node
  ↓
Traverse governed relations
  ↓
Classify direct/transitive impact
  ↓
Apply StandardsProfile
  ↓
Calculate required gates
  ↓
Generate Impact Package
  ↓
Human review for significant change
  ↓
Execute + retest
  ↓
Update graph / RTM / baseline
```

## MVP

Первая реализация поддерживает три направления:

1. `Requirement → Decision → Test → Code`;
2. `Code → Test → Requirement → Goal`;
3. `Standard/Control → Requirement → Test`.

Глубокий AST-call graph и runtime dependency graph остаются `DEFER` до появления реальной необходимости.

## Gate

Модель считается реализованной для MVP, когда изменение одного тестового CodeArtifact автоматически выдаёт минимальный набор связанных требований, тестов и решений для повторной проверки.
