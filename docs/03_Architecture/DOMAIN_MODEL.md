# FATHER Domain Model v0.1

**Status:** DRAFT / BASELINE CANDIDATE  
**Purpose:** перевести Meta Model и Engineering Knowledge Graph в доменную модель, пригодную для Django/PostgreSQL реализации.

## 1. Принцип

Доменная модель строится вокруг непрерывной трассы:

`Goal → Problem → Evidence → Decision → Capability → Component → CodeArtifact → TestRun → Metric → Outcome → LessonLearned`.

Каждая сущность должна иметь устойчивый ID, статус, версию, timestamps, provenance и audit fields.

## 2. Домены MVP

### Project & Governance
- `Organization`
- `Project`
- `Goal`
- `Task`
- `Risk`

### Knowledge & Evidence
- `Source`
- `Evidence`
- `KnowledgeItem`
- `KnowledgeRelation`

### Decision Intelligence
- `DecisionSession`
- `Alternative`
- `ExpertRole`
- `Methodology`
- `ExpertReview`
- `Decision`

### Engineering
- `Requirement`
- `Capability`
- `Component`
- `Repository`
- `CodeArtifact`
- `Blueprint`
- `AgentBuild`

### Verification & Outcome
- `TestRun`
- `SecurityFinding`
- `Metric`
- `Outcome`
- `LessonLearned`

## 3. Базовые поля

Для большинства сущностей:

```text
id: UUID
public_id: stable human-readable ID
name/title
description
status
version
created_at
updated_at
created_by
updated_by
source/provenance
metadata: JSONB
```

## 4. Ключевые связи

```text
Project HAS_GOAL Goal
Goal BLOCKED_BY Problem
Problem SUPPORTED_BY Evidence
Problem ADDRESSED_BY Decision
Decision SELECTS Alternative
Decision PRODUCED_BY DecisionSession
DecisionSession HAS_REVIEW ExpertReview
ExpertReview PERFORMED_BY ExpertRole
ExpertReview USES Methodology
Decision REQUIRES Capability
Capability IMPLEMENTED_BY Component
Component REALIZED_AS CodeArtifact
CodeArtifact VERIFIED_BY TestRun
TestRun PRODUCES Metric
Metric MEASURES Outcome
Outcome AFFECTS Goal
Outcome PRODUCES LessonLearned
LessonLearned IMPROVES Capability/Methodology/Standard
```

## 5. Project

Минимальные поля:

```text
id
code
name
description
status
project_type
owner
start_date
planned_end_date
actual_end_date
planned_cost
actual_cost
currency
priority
metadata
```

Проект является контейнером трассировки, но знания и методы могут переиспользоваться между проектами.

## 6. Goal

```text
id
project_id
name
description
priority
success_criteria
baseline_value
target_value
actual_value
status
```

Цель должна иметь измеримый критерий успеха, иначе влияние решений на неё нельзя проверить.

## 7. Problem

```text
id
project_id
title
description
severity
probability
status
root_cause_status
```

Проблема может препятствовать нескольким целям и иметь несколько решений.

## 8. Source / Evidence / KnowledgeItem

`Source` хранит происхождение. `Evidence` хранит конкретный подтверждающий фрагмент/наблюдение. `KnowledgeItem` хранит нормализованное знание.

Evidence не должно терять ссылку на источник.

Поля качества:

```text
source_trust
extraction_quality
freshness
relevance
confirmation_count
contradiction_count
confidence
```

## 9. DecisionSession

```text
id
project_id
task
status
mode
started_at
completed_at
time_budget
cost_budget
actual_tokens
actual_cost
latency_ms
human_gate_required
human_gate_result
```

Сессия хранит процесс выработки инженерного решения без хранения скрытых chain-of-thought моделей.

## 10. Alternative

```text
id
session_id
title
description
estimated_cost
estimated_time
risk_score
benefit_score
status
rejection_reason
```

## 11. ExpertRole / Methodology / ExpertReview

`ExpertRole` не привязан к конкретной LLM.

Эксперт = `Role + Knowledge + Methodologies + Rules + Tools + Metrics + Constraints`.

`ExpertReview` хранит:

```text
recommendation
score
confidence
findings
risks
assumptions
required_evidence
missing_information
model_used
tokens
cost
latency
```

## 12. Decision

`Decision` — утверждённый выбор, а не ответ модели.

Обязательные поля определяются отдельной `DECISION_RECORD_SCHEMA.json`.

## 13. Requirement / Capability / Component

Разделяем уровни:

```text
Requirement = что система обязана обеспечить
Capability = какую способность необходимо иметь
Component = какой технический элемент реализует способность
```

Это позволяет менять реализацию без потери причин появления компонента.

## 14. Repository / CodeArtifact

Для MVP код не копируется в Knowledge Graph целиком.

`CodeArtifact` хранит:

```text
repository
path
symbol
artifact_type
commit_sha
language
version
hash
```

Позже возможен AST/code graph.

## 15. TestRun / SecurityFinding

Любое критическое требование или capability должно иметь механизм проверки.

`TestRun` связывается с конкретной версией кода/blueprint/build.

`SecurityFinding` содержит severity, category, status, evidence, affected artifact и remediation.

## 16. Metric / Outcome

Metric — измерение. Outcome — фактический результат.

Не допускается подмена Outcome прогнозом.

```text
Decision
  ↓ expected_effect
Outcome
  ↓ comparison
DecisionEvaluation
```

В MVP `DecisionEvaluation` может храниться в metadata/связи; при росте выделяется отдельной сущностью.

## 17. LessonLearned

Урок должен содержать:

```text
observation
cause
scope
confidence
recommended_change
validated_reuse_count
failed_reuse_count
```

После подтверждённого повторного применения урок может стать Pattern/Standard.

## 18. Audit / Security by Design

Критические сущности не удаляются физически без специальной политики. Используются status/archived/retention.

Необходимы:
- RBAC;
- audit trail;
- immutable event references для критических решений;
- provenance;
- data classification;
- tenant/organization isolation в enterprise-версии;
- secret separation.

## 19. MVP Django apps — предварительное отображение

```text
core        Organization, common fields, audit
projects    Project, Goal, Task, Risk
knowledge   Source, Evidence, KnowledgeItem, KnowledgeRelation
decisions   DecisionSession, Alternative, ExpertReview, Decision
experts     ExpertRole, Methodology
engineering Requirement, Capability, Component, Repository, CodeArtifact, Blueprint, AgentBuild
quality     TestRun, SecurityFinding, Metric, Outcome, LessonLearned
```

Это логическое разделение модульного монолита, не микросервисы.

## 20. Gate

Domain Model v0.1 считается достаточным для начала Django-моделей, если:

- можно восстановить путь `Goal → Outcome`;
- Decision имеет альтернативы и evidence;
- код связан с требованием/capability;
- тест связан с кодом/build;
- outcome отделён от expected effect;
- provenance не теряется;
- схема допускает накопление plan/fact.

## Навигация

- ↑ [Architecture](README.md)
- ↔ [FATHER Meta Model](FATHER_META_MODEL.md)
- ↔ [Information Architecture](FATHER_INFORMATION_ARCHITECTURE.md)
- ↔ [Core Entity Catalog](CORE_ENTITY_CATALOG.md)
- ↔ [Relationship Catalog](RELATIONSHIP_CATALOG.md)
- → [Decision Record Schema](DECISION_RECORD_SCHEMA.json)
- → [Django Model Mapping](DJANGO_MODEL_MAPPING.md)
