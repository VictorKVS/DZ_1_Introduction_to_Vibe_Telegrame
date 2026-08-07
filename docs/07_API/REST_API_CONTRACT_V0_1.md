# FATHER REST API Contract v0.1

**Status:** DRAFT  
**Scope:** первый вертикальный сценарий Control Plane.

## 1. Цель

API должен позволять пройти минимальную трассу:

`Project → Goal → Source/Evidence → DecisionSession → Alternatives → ExpertReviews → Decision`.

API проектируется вокруг доменных сущностей, а не экранов UI.

## 2. Базовые правила

- Base path: `/api/v1/`
- JSON only для MVP API.
- UUID/public_id для внешних ссылок.
- Все timestamps — ISO 8601 UTC.
- Ошибки — единая структура.
- Пагинация обязательна для коллекций.
- Фильтрация по `project`, `status`, `created_at`.
- Идемпотентность для операций сборки/запуска будет добавлена отдельным контрактом.

## 3. Error envelope

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable message",
    "details": {},
    "request_id": "uuid"
  }
}
```

## 4. Projects

### POST `/api/v1/projects/`
Создать проект.

### GET `/api/v1/projects/`
Список проектов.

### GET `/api/v1/projects/{project_id}/`
Карточка проекта.

### PATCH `/api/v1/projects/{project_id}/`
Изменить разрешённые поля проекта.

## 5. Goals

### POST `/api/v1/projects/{project_id}/goals/`
Создать измеримую цель.

Минимальный payload:

```json
{
  "name": "Сократить время проектирования дочернего агента",
  "success_criteria": ["Получить рабочий blueprint"],
  "baseline_value": {"hours": 40},
  "target_value": {"hours": 8},
  "priority": 1
}
```

### GET `/api/v1/projects/{project_id}/goals/`

## 6. Sources

### POST `/api/v1/projects/{project_id}/sources/`
Регистрирует источник и provenance.

Поля:
- source_type;
- title;
- uri/path;
- effective_date;
- content_hash;
- origin/author;
- trust_score;
- classification.

### GET `/api/v1/projects/{project_id}/sources/`

## 7. Evidence

### POST `/api/v1/projects/{project_id}/evidence/`

```json
{
  "source_id": "SRC-...",
  "locator": {"page": 4, "lines": "12-18"},
  "excerpt_or_summary": "...",
  "extraction_quality": 0.95,
  "relevance_score": 0.88,
  "confidence": 0.9
}
```

### GET `/api/v1/projects/{project_id}/evidence/`

## 8. Expert Roles

### GET `/api/v1/expert-roles/`
Каталог ролей.

### POST `/api/v1/expert-roles/`
Создание/регистрация роли администратором.

## 9. Methodologies

### GET `/api/v1/methodologies/`

### POST `/api/v1/methodologies/`

## 10. Decision Sessions

### POST `/api/v1/projects/{project_id}/decision-sessions/`

```json
{
  "task": "Выбрать архитектуру MVP",
  "mode": "STANDARD",
  "time_budget": 900,
  "cost_budget": 2.0,
  "human_gate_required": true
}
```

### GET `/api/v1/decision-sessions/{session_id}/`

### POST `/api/v1/decision-sessions/{session_id}/start/`
Запуск SOCRATES-lite появится после реализации orchestrator.

## 11. Alternatives

### POST `/api/v1/decision-sessions/{session_id}/alternatives/`

### GET `/api/v1/decision-sessions/{session_id}/alternatives/`

## 12. Expert Reviews

### POST `/api/v1/decision-sessions/{session_id}/expert-reviews/`
Первоначально может использоваться для ручной/тестовой загрузки экспертного заключения.

```json
{
  "expert_role_id": "EXP-ARCHITECT",
  "methodology_id": "METH-ATAM",
  "recommendation": "...",
  "findings": [],
  "risks": [],
  "assumptions": [],
  "missing_information": [],
  "score": 8.2,
  "confidence": 0.74
}
```

## 13. Decisions

### POST `/api/v1/decision-sessions/{session_id}/decision/`
Создание Decision Record по `DECISION_RECORD_SCHEMA.json`.

### GET `/api/v1/decisions/{decision_id}/`

### POST `/api/v1/decisions/{decision_id}/approve/`
Human Gate.

### POST `/api/v1/decisions/{decision_id}/reject/`
Human Gate.

## 14. Traceability endpoint

### GET `/api/v1/projects/{project_id}/trace/`

Возвращает компактную трассу проекта:

```text
Goal
→ Problems
→ Evidence
→ Decision Sessions
→ Decisions
→ Capabilities / Components
→ Tests
→ Metrics
→ Outcomes
```

В MVP endpoint может строиться через ORM. Позднее — через graph layer.

## 15. Audit

Критические write-actions должны формировать AuditEvent:

- создание/изменение Decision;
- human approval/rejection;
- изменение Evidence/Source provenance;
- изменение security-sensitive configuration.

## 16. Authorization MVP

Минимальные роли:

- `admin`
- `project_owner`
- `analyst`
- `reviewer`
- `viewer`

До внедрения полноценной RBAC используется Django permissions + project ownership.

## 17. Не входит в v0.1

- public external API;
- streaming LLM responses;
- websocket;
- agent tool gateway;
- billing;
- marketplace;
- multi-tenant enterprise federation;
- bulk ingest больших объёмов;
- webhook orchestration.

## 18. Acceptance Gate

API v0.1 считается достаточным, если автоматический integration test может:

1. создать Project;
2. создать Goal;
3. зарегистрировать Source и Evidence;
4. создать DecisionSession;
5. добавить 2+ Alternative;
6. добавить 3 ExpertReview;
7. создать Decision;
8. получить trace и увидеть всю цепочку.

## Навигация

- ↑ [API section](README.md)
- ↔ [Domain Model](../03_Architecture/DOMAIN_MODEL.md)
- ↔ [Decision Record Schema](../03_Architecture/DECISION_RECORD_SCHEMA.json)
- ↔ [Django Model Mapping](../03_Architecture/DJANGO_MODEL_MAPPING.md)
