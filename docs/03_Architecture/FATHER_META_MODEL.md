# FATHER — Meta Model v0.1

**Status:** DRAFT / FOUNDATION  
**Purpose:** единый машинно-читаемый смысловой каркас FATHER: типы сущностей, связи, жизненные циклы, веса, трассировка от цели до результата и правила переноса в Django Models / API / Knowledge Graph.

> FATHER должен хранить не только документы и ответы LLM, а причинно-связанную историю инженерной деятельности: что хотели достичь, что мешало, какие данные были доступны, какие решения приняли, какой код это реализовал, как проверили и что получилось фактически.

---

## 1. Базовый принцип

Любой значимый объект системы должен быть представлен как сущность с уникальным ID, версией, статусом, источником происхождения и связями.

Минимальная трассировка:

```text
GOAL
  ↓
PROBLEM
  ↓
EVIDENCE / KNOWLEDGE
  ↓
ALTERNATIVE
  ↓
DECISION
  ↓
REQUIREMENT
  ↓
ARCHITECTURE COMPONENT
  ↓
CODE ARTIFACT
  ↓
TEST
  ↓
METRIC
  ↓
OUTCOME
  ↓
LESSON LEARNED
  ↓
STANDARD / TEMPLATE / RULE UPDATE
```

Это является основной единицей организационного обучения.

---

## 2. Основные типы узлов

### Strategy / Business

- `Organization`
- `Customer`
- `Stakeholder`
- `Goal`
- `BusinessMetric`
- `Constraint`
- `Opportunity`
- `Problem`
- `Hypothesis`

### Project / Product

- `Project`
- `Product`
- `Request`
- `UseCase`
- `Requirement`
- `NFR`
- `AcceptanceCriterion`
- `Risk`
- `Estimate`
- `ChangeRequest`

### Knowledge / Evidence

- `Source`
- `Document`
- `Evidence`
- `KnowledgeItem`
- `Claim`
- `Contradiction`
- `Rule`
- `Methodology`
- `Pattern`
- `AntiPattern`
- `LessonLearned`
- `Standard`

### Decision

- `DecisionSession`
- `Alternative`
- `ExpertReview`
- `Decision`
- `Assumption`
- `TradeOff`
- `HumanApproval`

### Experts / Agents

- `ExpertRole`
- `ExpertBlueprint`
- `AgentBlueprint`
- `AgentInstance`
- `Capability`
- `Tool`
- `Policy`

### Engineering

- `ArchitectureComponent`
- `Interface`
- `APIContract`
- `DataModel`
- `Repository`
- `CodeArtifact`
- `Build`
- `Deployment`
- `Configuration`

### Quality / Security

- `TestCase`
- `TestRun`
- `SecurityControl`
- `SecurityFinding`
- `Vulnerability`
- `Incident`
- `QualityFinding`

### Operations / Outcome

- `Metric`
- `Measurement`
- `Outcome`
- `Deviation`
- `CostRecord`
- `TimeRecord`
- `Feedback`

---

## 3. Типы связей

Связь является отдельным объектом и тоже имеет ID, тип, вес, источник и дату.

### Goal / Problem

- `PROJECT_SUPPORTS_GOAL`
- `METRIC_MEASURES_GOAL`
- `PROBLEM_BLOCKS_GOAL`
- `RISK_THREATENS_GOAL`
- `OUTCOME_IMPACTS_GOAL`

### Knowledge / Evidence

- `SOURCE_SUPPORTS_CLAIM`
- `SOURCE_CONTRADICTS_CLAIM`
- `EVIDENCE_SUPPORTS_DECISION`
- `EVIDENCE_REFUTES_ALTERNATIVE`
- `KNOWLEDGE_DERIVED_FROM_SOURCE`
- `KNOWLEDGE_SUPERSEDES_KNOWLEDGE`
- `KNOWLEDGE_RELATED_TO_KNOWLEDGE`

### Decision

- `DECISION_ADDRESSES_PROBLEM`
- `DECISION_SELECTS_ALTERNATIVE`
- `DECISION_REJECTS_ALTERNATIVE`
- `EXPERT_REVIEW_EVALUATES_ALTERNATIVE`
- `METHODOLOGY_USED_IN_REVIEW`
- `ASSUMPTION_SUPPORTS_DECISION`
- `HUMAN_APPROVES_DECISION`

### Requirements / Architecture / Code

- `REQUIREMENT_DERIVED_FROM_DECISION`
- `REQUIREMENT_SATISFIED_BY_COMPONENT`
- `COMPONENT_IMPLEMENTED_BY_CODE`
- `CODE_DEPENDS_ON_CODE`
- `CODE_EXPOSES_INTERFACE`
- `API_IMPLEMENTED_BY_COMPONENT`
- `CONFIG_CONFIGURES_COMPONENT`

### Tests / Security

- `TEST_VERIFIES_REQUIREMENT`
- `TEST_VERIFIES_CODE`
- `SECURITY_CONTROL_MITIGATES_RISK`
- `FINDING_AFFECTS_COMPONENT`
- `VULNERABILITY_AFFECTS_CODE`
- `FIX_RESOLVES_FINDING`

### Outcomes / Learning

- `MEASUREMENT_MEASURES_METRIC`
- `OUTCOME_CONFIRMS_DECISION`
- `OUTCOME_WEAKENS_DECISION`
- `OUTCOME_REFUTES_ASSUMPTION`
- `DEVIATION_CAUSED_BY_PROBLEM`
- `LESSON_DERIVED_FROM_OUTCOME`
- `LESSON_UPDATES_STANDARD`
- `LESSON_UPDATES_BLUEPRINT`
- `LESSON_CHANGES_WEIGHT`

---

## 4. Универсальные поля узла

```yaml
id: UUID
node_type: enum
name: string
summary: string
status: enum
version: string
project_id: UUID|null
organization_id: UUID|null
source_type: human|document|system|llm|measurement|import
source_ref: string|null
created_at: datetime
updated_at: datetime
valid_from: datetime|null
valid_to: datetime|null
created_by: actor_id
approved_by: actor_id|null
confidentiality: public|internal|confidential|restricted
integrity_status: draft|reviewed|verified|disputed|deprecated
metadata: json
```

---

## 5. Универсальные поля связи

```yaml
id: UUID
from_node_id: UUID
to_node_id: UUID
relation_type: enum
status: active|disputed|deprecated
confidence: 0.0..1.0
evidence_strength: 0.0..1.0
relevance: 0.0..1.0
freshness: 0.0..1.0
goal_impact: -1.0..1.0
risk_impact: -1.0..1.0
reuse_success: 0.0..1.0
source_ref: string|null
created_at: datetime
validated_at: datetime|null
metadata: json
```

Важно: не использовать один универсальный `weight` как истину. Вес вычисляется функцией под конкретную задачу.

Пример:

```text
Decision Recommendation Weight
= evidence_strength
× relevance
× freshness
× source_trust
× context_similarity
× historical_success
```

Коэффициенты и формула должны быть версионируемыми.

---

## 6. Статусы знаний

Для `Claim / KnowledgeItem / Evidence`:

- `CANDIDATE`
- `PRELIMINARY`
- `VERIFIED`
- `DISPUTED`
- `REFUTED`
- `OUTDATED`
- `DEPRECATED`

Отдельно фиксируется происхождение:

- `OBSERVED` — измерено/зафиксировано;
- `SOURCE_DERIVED` — извлечено из источника;
- `INFERRED` — выведено алгоритмом/LLM;
- `HUMAN_JUDGMENT` — экспертное мнение;
- `SYNTHESIZED` — сформировано из нескольких источников.

---

## 7. Жизненный цикл решения

```text
PROBLEM IDENTIFIED
      ↓
EVIDENCE GATHERED
      ↓
ALTERNATIVES GENERATED
      ↓
EXPERT REVIEWS
      ↓
CONFLICT / CONSENSUS
      ↓
DECISION PROPOSED
      ↓
HUMAN GATE (если требуется)
      ↓
DECISION ACCEPTED
      ↓
IMPLEMENTED
      ↓
MEASURED
      ↓
VALIDATED / REVISED / REJECTED
```

Решение не становится "хорошим" в момент принятия. Его качество определяется после появления фактического Outcome.

---

## 8. Жизненный цикл проблемы

```text
DETECTED
  ↓
CLASSIFIED
  ↓
ROOT CAUSE HYPOTHESIS
  ↓
EVIDENCE
  ↓
RESOLUTION DECISION
  ↓
IMPLEMENTATION
  ↓
VERIFICATION
  ↓
RESOLVED / PARTIAL / REOPENED
```

Связь `DEVIATION_CAUSED_BY_PROBLEM` должна позволять накопить статистику причин срыва сроков, стоимости, качества и безопасности.

---

## 9. Трассировка до машинного кода

На MVP код не копируется в Knowledge Graph целиком. Создаётся `CodeArtifact`:

```yaml
id: UUID
repository: VictorKVS/example
branch: main
commit_sha: abc123
path: src/core/service.py
symbol: PaymentService.calculate
language: python
artifact_type: module|class|function|config|schema|migration
content_hash: sha256:...
```

Связи:

```text
Requirement
  └─SATISFIED_BY→ ArchitectureComponent
                       └─IMPLEMENTED_BY→ CodeArtifact
                                           ├─VERIFIED_BY→ TestCase
                                           └─AFFECTED_BY→ SecurityFinding
```

Позднее при необходимости вводится Code Graph на основе AST/парсеров:

- `CALLS`
- `IMPORTS`
- `READS`
- `WRITES`
- `IMPLEMENTS`
- `INHERITS`

Отдельная графовая БД для этого не является обязательной до появления измеримой нагрузки.

---

## 10. Goal Impact Model

Для каждого решения и результата хранится предполагаемое и фактическое влияние на цель.

```yaml
expected_impact:
  goal_id: GOAL-001
  metric_id: METRIC-001
  direction: increase|decrease|maintain
  expected_delta: 0.15
  confidence: 0.65

actual_impact:
  measured_delta: 0.09
  observation_window: 90d
  confidence: 0.80
```

Таким образом можно оценивать не только "работает ли код", а "помогло ли решение достичь цели".

---

## 11. Plan / Fact / Causality

Минимальная цепочка:

```text
Decision
   ↓ expected
ExpectedEffect
   ↓ implementation
Build / Change
   ↓ measurement
Outcome
   ↓ comparison
Deviation
   ↓ analysis
Cause / Contributing Factors
   ↓
LessonLearned
```

Нельзя автоматически считать причинность доказанной только потому, что Outcome произошёл после Decision.

Статус влияния:

- `CORRELATED`
- `PLAUSIBLE_CAUSE`
- `SUPPORTED_CAUSE`
- `EXPERIMENTALLY_CONFIRMED`
- `REFUTED`

---

## 12. Security by Design для Knowledge Graph

Обязательно:

- RBAC/ABAC на типы узлов и проектов;
- tenant/project isolation;
- audit trail изменений;
- provenance каждого критичного факта;
- запрет скрытой перезаписи истории;
- versioning вместо destructive overwrite;
- классификация данных;
- retention/deletion rules;
- контроль импорта внешних источников;
- защита от prompt/data poisoning;
- ручной gate для критичных выводов о людях, безопасности и существенных бизнес-решениях.

---

## 13. MVP storage model

Первая реализация:

```text
PostgreSQL
├── graph_nodes
├── graph_edges
├── projects
├── sources
├── documents
├── decisions
├── metrics
├── measurements
├── code_artifacts
└── audit_events

pgvector
└── embeddings для семантического поиска
```

`JSONB` используется для расширяемых метаданных, но ключевые поля должны быть нормализованы.

Neo4j / RDF store / специализированный graph engine — `DEFER`, пока реальные запросы не покажут ограничение PostgreSQL.

---

## 14. Минимальные Graph Queries MVP

Система должна уметь отвечать:

1. Какая цель породила это требование?
2. Какое решение привело к этому компоненту?
3. Какие источники подтверждают это решение?
4. Какой код реализует требование?
5. Какие тесты подтверждают реализацию?
6. Какие проблемы связаны с этим компонентом?
7. Какие решения раньше применялись к похожим проблемам?
8. Чем они закончились?
9. Какие решения чаще всего дают положительный Goal Impact?
10. Какие типы проблем чаще вызывают перерасход времени/денег?
11. Какие изменения кода чаще приводили к security findings или regression?
12. Какие lessons learned уже должны изменить стандарт или blueprint?

---

## 15. Definition of Done для Meta Model v0.1

- [x] определены базовые типы узлов;
- [x] определены базовые типы связей;
- [x] введены раздельные веса;
- [x] определён Decision lifecycle;
- [x] определён Problem lifecycle;
- [x] зафиксирована трассировка до CodeArtifact;
- [x] введена связь Goal ↔ Outcome;
- [x] зафиксировано различие correlation / causality;
- [x] определена storage strategy MVP;
- [ ] создать JSON Schema / Pydantic schema для Node и Edge;
- [ ] создать Django Models draft;
- [ ] создать ER/Graph diagram;
- [ ] создать controlled vocabulary для relation_type;
- [ ] протестировать модель на одном реальном legacy-кейсе Sokrat → SOCRATES.

---

## 16. Следующий шаг

На основе этого документа создать:

1. `FATHER_DICTIONARY.md` — официальные определения терминов;
2. `GRAPH_SCHEMA_V0_1.json` — машинно-читаемая схема;
3. `DOMAIN_MODEL.md` — прикладная модель Django Control Plane;
4. первый тестовый граф: `Sokrat legacy → capability → decision → new SOCRATES design`.

## Навигация

- ↑ [03 — Architecture](README.md)
- ↔ [Engineering Knowledge Graph](ENGINEERING_KNOWLEDGE_GRAPH.md)
- ↔ [Work Plan](../00_Project_Management/WORK_PLAN.md)
- ↔ [Development Log](../00_Project_Management/DEVELOPMENT_LOG.md)
- ↔ [Legacy Intelligence](../20_Legacy_Intelligence/README.md)
