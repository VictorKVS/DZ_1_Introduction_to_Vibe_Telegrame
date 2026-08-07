# FATHER — Django Model Mapping v0.1

**Status:** DRAFT  
**Purpose:** отобразить доменную модель FATHER на Django-приложения и модели модульного монолита.

## 1. Принцип

Django является Control Plane MVP. Архитектурные границы отражаются через отдельные apps, но не превращаются преждевременно в микросервисы.

## 2. Предлагаемые apps

```text
father/
├── core/
├── projects/
├── knowledge/
├── experts/
├── decisions/
├── engineering/
├── quality/
└── api/
```

## 3. core

### BaseTrackedModel
Абстрактная модель:

```text
id UUID primary key
public_id CharField unique
title/name
status
version
metadata JSONField
created_at
updated_at
created_by
updated_by
```

### Organization
- name
- code
- status
- metadata

Позже: tenant isolation, retention policy, classification policy.

## 4. projects

### Project
- organization FK
- code
- name
- description
- project_type
- owner FK user
- start_date
- planned_end_date
- actual_end_date
- planned_cost
- actual_cost
- currency
- priority

### Goal
- project FK
- name
- success_criteria JSON
- baseline_value JSON
- target_value JSON
- actual_value JSON
- priority

### Task
- project FK
- parent self FK nullable
- title
- status
- planned_hours
- actual_hours

### Risk
- project FK
- title
- probability
- impact
- mitigation
- owner
- status

## 5. knowledge

### Source
- project FK nullable
- source_type
- title
- uri/path
- received_at
- effective_date
- content_hash
- author/origin
- trust_score
- classification

### Evidence
- source FK
- project FK
- locator JSON (page/lines/url/fragment)
- excerpt_or_summary
- extraction_quality
- freshness_score
- relevance_score
- confidence

### KnowledgeItem
- project FK nullable
- title
- statement
- knowledge_type
- status
- confidence
- valid_from
- valid_to
- embedding VectorField nullable

### KnowledgeRelation
- from_item FK
- to_item FK
- relation_type
- weight
- causal_status
- metadata

## 6. experts

### ExpertRole
- code
- name
- responsibility
- decision_criteria JSON
- required_evidence JSON
- constraints JSON
- escalation_rules JSON
- metrics JSON
- cost_policy JSON

### Methodology
- code
- name
- purpose
- algorithm JSON
- applicability JSON
- limitations JSON
- metrics JSON

ExpertRole ↔ Methodology через M2M/through model для веса и условий применения.

## 7. decisions

### DecisionSession
- project FK
- task
- status
- mode
- time_budget
- cost_budget
- actual_tokens
- actual_cost
- latency_ms
- human_gate_required
- human_gate_result

### Alternative
- session FK
- title
- description
- estimated_cost
- estimated_time_hours
- risk_score
- benefit_score
- status
- rejection_reason

### ExpertReview
- session FK
- expert_role FK
- methodology FK nullable
- model_provider
- model_name
- recommendation
- findings JSON
- risks JSON
- assumptions JSON
- missing_information JSON
- score
- confidence
- tokens
- monetary_cost
- latency_ms

### Decision
- session OneToOne/ForeignKey
- selected_alternative FK
- title
- status
- rationale JSON
- confidence
- expected_effects JSON
- validation_plan JSON
- human_approver nullable

Decision ↔ Evidence — M2M.
Decision ↔ Risk — M2M.

## 8. engineering

### Requirement
- project FK
- code
- requirement_type
- statement
- priority
- acceptance_criteria JSON
- status

### Capability
- code
- name
- description
- maturity_level
- reuse_status
- metrics JSON

### Component
- project FK nullable
- capability M2M
- name
- component_type
- version
- status

### Repository
- project FK nullable
- provider
- full_name
- default_branch
- url

### CodeArtifact
- repository FK
- component FK nullable
- path
- symbol
- artifact_type
- language
- commit_sha
- content_hash
- version

### Blueprint
- project FK
- version
- manifest JSON
- status

### AgentBuild
- blueprint FK
- build_number
- status
- repository_ref
- artifact_ref
- started_at
- finished_at

## 9. quality

### TestRun
- project FK
- build FK nullable
- code_artifact FK nullable
- test_type
- status
- started_at
- finished_at
- metrics JSON
- evidence JSON

### SecurityFinding
- project FK
- build FK nullable
- code_artifact FK nullable
- category
- severity
- finding
- evidence JSON
- remediation
- status

### Metric
- project FK
- name
- metric_type
- value JSON
- unit
- measured_at
- source_ref

### Outcome
- project FK
- goal FK nullable
- name
- actual_value JSON
- measured_at
- confidence
- causal_status
- notes

### LessonLearned
- project FK nullable
- observation
- cause
- scope
- confidence
- recommended_change
- validated_reuse_count
- failed_reuse_count
- status

## 10. Generic Graph Layer

Для Engineering Knowledge Graph поверх предметных моделей нужен универсальный слой связей. MVP-вариант:

### GraphNodeRef
- id
- object_type
- object_id
- public_id

### GraphEdge
- from_node FK
- to_node FK
- relation_type
- weight
- evidence_strength
- goal_impact
- causal_status
- metadata JSON

Это позволяет строить граф без перехода на Neo4j и не ломает нормализованные предметные таблицы.

## 11. Индексы MVP

Обязательные индексы:
- public_id;
- project/status;
- source content_hash;
- repository/path/commit_sha;
- relation_type;
- GraphEdge(from_node, relation_type);
- GraphEdge(to_node, relation_type);
- KnowledgeItem embedding vector index после выбора pgvector конфигурации.

## 12. Security requirements to models

Сразу предусмотреть:
- `created_by` / `updated_by`;
- object ownership;
- organization scope;
- classification on Source/Artifact;
- immutable audit event для критических решений;
- soft-delete/archive вместо бесконтрольного удаления;
- запрет хранения API keys/secrets в JSON metadata;
- hash источников и файлов.

## 13. Не делать сейчас

- GenericForeignKey для всей предметной модели;
- микросервисы;
- отдельную graph DB;
- Celery без фоновой нагрузки;
- event sourcing для всех объектов;
- сложную RBAC-иерархию до появления второго реального пользователя.

## 14. Первый кодовый инкремент

Создать Django-проект и apps:

```text
core
projects
knowledge
decisions
experts
```

В первом миграционном срезе реализовать только:

```text
Organization
Project
Goal
Source
Evidence
KnowledgeItem
ExpertRole
Methodology
DecisionSession
Alternative
ExpertReview
Decision
```

Остальные модели добавлять по вертикальному сценарию, не заранее.

## 15. Gate

Первый database baseline принят, если через Django Admin/API можно создать:

`Project → Goal → Source/Evidence → DecisionSession → Alternatives → ExpertReviews → Decision`

и восстановить эту цепочку одним запросом/представлением.

## Навигация

- ↑ [Architecture](README.md)
- ← [Domain Model](DOMAIN_MODEL.md)
- ↔ [Decision Record Schema](DECISION_RECORD_SCHEMA.json)
- ↔ [Engineering Knowledge Graph](ENGINEERING_KNOWLEDGE_GRAPH.md)
