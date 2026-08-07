# FATHER — Information Architecture v0.1

**Status:** ACCEPTED / EVOLVING  
**Purpose:** определить, какие классы информации существуют в FATHER, кто их создаёт, как они версионируются, связываются, проверяются, архивируются и превращаются в организационную память.

## 1. Главный принцип

FATHER хранит не набор разрозненных документов, а связанную инженерную модель:

`Goal → Problem → Requirement → Evidence → Alternative → Decision → Capability → Architecture → Code → Test → Metric → Outcome → Lesson → Standard`.

Документы, отчёты, README, SRS, ADR и другие артефакты являются представлениями этой модели и не должны становиться независимыми источниками противоречащей истины.

## 2. Информационные домены

### 2.1 Strategy
- Organization
- Stakeholder
- Goal
- KPI
- Constraint
- Assumption

### 2.2 Delivery
- Project
- WorkItem
- Milestone
- Estimate
- Resource
- CostRecord
- TimeRecord

### 2.3 Requirements
- Problem
- Requirement
- NFR
- AcceptanceCriterion
- UseCase
- Risk

### 2.4 Decision Intelligence
- DecisionSession
- Alternative
- ExpertReview
- Decision
- DecisionRationale
- HumanGate

### 2.5 Knowledge & Evidence
- Source
- Evidence
- KnowledgeItem
- Claim
- Contradiction
- Methodology
- Pattern
- AntiPattern

### 2.6 Engineering
- Capability
- Component
- Interface
- Repository
- CodeArtifact
- ConfigurationArtifact
- DeploymentArtifact

### 2.7 Quality & Security
- TestCase
- TestRun
- SecurityFinding
- Control
- Vulnerability
- Incident
- QualityMetric

### 2.8 Outcome & Learning
- Metric
- Outcome
- Deviation
- LessonLearned
- Standard
- Template
- ReuseRecord

### 2.9 Agent Factory
- ExpertRole
- ExpertBlueprint
- AgentBlueprint
- AgentBuild
- ToolCapability
- Policy
- PromptAsset
- EvaluationRun

## 3. Общие поля сущностей

Каждая долговечная сущность должна иметь минимум:

```yaml
id:
type:
title:
status:
version:
created_at:
updated_at:
created_by:
source_of_truth:
classification:
project_id:
metadata:
```

При необходимости добавляются:

```yaml
valid_from:
valid_to:
confidence:
owner:
approved_by:
review_at:
retention_class:
```

## 4. Классы статуса знания

- `RAW` — получено, но не обработано;
- `CANDIDATE` — извлечено и требует проверки;
- `SUPPORTED` — имеет evidence;
- `VERIFIED` — прошло установленную проверку;
- `DISPUTED` — имеются значимые противоречия;
- `REJECTED` — признано неверным/неприменимым;
- `STALE` — потеряло актуальность;
- `DEPRECATED` — сохранено для истории, но не используется.

## 5. Provenance

Любой критичный KnowledgeItem, Claim, Requirement или Decision должен иметь путь происхождения до исходного материала или явно помечаться как гипотеза.

Минимальная цепочка:

`Source → Evidence → Claim/Knowledge → Decision/Requirement`.

SPHINX отвечает за проверку существования и качества этой цепочки.

## 6. Версионирование

Версионируются обязательно:

- Requirement;
- Decision;
- Methodology;
- Standard;
- ExpertBlueprint;
- AgentBlueprint;
- Capability contract;
- Policy;
- KnowledgeItem, если изменился смысл;
- CodeArtifact через commit SHA/tag.

Старые версии не перезаписываются без следа.

## 7. Права изменения

Три уровня авторства:

- `AGENT_PROPOSED` — агент может создать предложение;
- `AUTOMATION_CONFIRMED` — правило/тест может подтвердить автоматически;
- `HUMAN_APPROVED` — требуется ответственное лицо.

Для существенных архитектурных, финансовых, правовых и ИБ-решений Human Gate включается политикой риска.

## 8. Архивирование и удаление

Не все данные одинаковы.

- временные технические данные могут удаляться по retention policy;
- решения, ADR, результаты тестов, план/факт и lessons learned должны архивироваться;
- чувствительные данные должны иметь отдельную классификацию, срок хранения и право удаления;
- удаление источника не должно оставлять ложное впечатление, будто evidence всё ещё существует.

## 9. Представления

Из одной модели могут генерироваться:

- README;
- PRD/SRS;
- ADR;
- Risk Register;
- Architecture views;
- API specification;
- Test Plan/Report;
- Security Review;
- Project Dashboard;
- Lessons Learned;
- GitHub Pages.

## 10. Минимальная реализация MVP

Хранилище:

- PostgreSQL;
- JSONB для расширяемых свойств;
- pgvector для semantic retrieval;
- таблицы `nodes` и `edges` для универсальных связей;
- отдельные типизированные таблицы для транзакционных ключевых сущностей;
- Git SHA / file path для ссылок на код.

Neo4j или другая graph DB не обязательны до появления запросов, которые PostgreSQL решает плохо.

## 11. Инварианты

1. Решение без связи с проблемой/целью считается неполным.
2. Критичный вывод без evidence помечается как неподтверждённый.
3. Код без связи с Requirement/Capability допускается только как эксперимент.
4. TestRun без ссылки на объект проверки не считается инженерным доказательством.
5. Outcome должен быть сопоставим с ожидаемым эффектом решения.
6. Lesson Learned возникает только из наблюдаемого результата, отклонения или подтверждённого опыта.

## 12. Следующий шаг

На основе этой архитектуры создать:

- `CORE_ENTITY_CATALOG.md`;
- `RELATIONSHIP_CATALOG.md`;
- machine-readable `GRAPH_SCHEMA_V0_1.json`;
- затем `DOMAIN_MODEL.md` и Django Models.

## Навигация

- ↑ [Architecture](README.md)
- ↔ [FATHER Meta Model](FATHER_META_MODEL.md)
- ↔ [Engineering Knowledge Graph](ENGINEERING_KNOWLEDGE_GRAPH.md)
- ↔ [FATHER Dictionary](FATHER_DICTIONARY.md)
