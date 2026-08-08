# FATHER — NFR v0.1

**Status:** DRAFT / BASELINE CANDIDATE  
**Scope:** первая сквозная вертикаль

## 1. Security

### NFR-SEC-001 Least Privilege
Доступ к проектам, evidence, decisions, blueprints и builds должен быть ограничен ролями и областью проекта.

### NFR-SEC-002 Human Gate
Решения с высоким финансовым, правовым, ИБ или репутационным воздействием не должны исполняться автоматически без Human Gate.

### NFR-SEC-003 Secrets
API keys, токены и пароли запрещено хранить в исходном коде, Markdown, JSON-примерах и Git history. Секреты должны поступать через secrets manager/environment и маскироваться в логах.

### NFR-SEC-004 Auditability
Критические изменения должны быть трассируемы до actor, timestamp, entity/version и action.

### NFR-SEC-005 Evidence Integrity
Для файловых/документных источников хранится cryptographic hash; изменение оригинала должно обнаруживаться.

### NFR-SEC-006 Upload Safety
При реализации upload обязательны allowlist типов, ограничения размера, безопасное имя/путь, изолированное хранение и возможность malware scan.

### NFR-SEC-007 Prompt/Tool Safety
Внешний контент считается недоверенным. Инструкции из документов/веб-источников не должны автоматически изменять system policy, tool permissions или Human Gate.

### NFR-SEC-008 Supply Chain
CI должен включать secrets scan, SAST и dependency vulnerability scan. Container scan обязателен при контейнеризации.

## 2. Privacy & Data Governance

### NFR-DATA-001 Classification
Source, Artifact и Project должны поддерживать classification минимум `PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED`.

### NFR-DATA-002 Minimization
Система хранит только данные, необходимые для заявленной цели проекта и доказуемой трассировки.

### NFR-DATA-003 Retention
Для классов данных должна поддерживаться политика retention/archive/delete; критические decision/audit records не удаляются без отдельного разрешения.

### NFR-DATA-004 Provenance
Knowledge/Evidence без provenance должен иметь пониженный статус доверия и не использоваться как единственное основание критичного решения.

## 3. Reliability & Integrity

### NFR-REL-001 Transactional Integrity
Создание Decision + связанных refs не должно оставлять полузаписанные критические состояния; использовать транзакции БД.

### NFR-REL-002 Idempotency
Повторный ingest одного source/hash не должен бесконтрольно создавать дубли.

### NFR-REL-003 Versioning
Requirements, Decision, Blueprint, AgentBuild и Knowledge Items должны поддерживать версии или immutable history.

### NFR-REL-004 Recovery
База данных и критические артефакты должны иметь проверяемый backup/restore процесс до production use.

## 4. Performance

Цифры ниже — стартовые SLO для MVP и подлежат измерению.

### NFR-PERF-001 API
P95 для обычных CRUD/read запросов при локальном/тестовом профиле: ≤ 500 ms без учёта внешних LLM/API.

### NFR-PERF-002 Trace Query
Получение полной trace цепочки одного проекта: P95 ≤ 2 s при тестовом объёме до 100 000 graph edges.

### NFR-PERF-003 Async External Work
LLM, web research, embeddings и тяжёлый ingest не должны удерживать синхронный HTTP request сверх установленного timeout; для длинных операций предусматривается job/session status.

## 5. Cost & Reasoning Economy

### NFR-COST-001 Session Cost
Каждая LLM/agent session должна сохранять provider/model, tokens или доступный usage, latency и estimated monetary cost.

### NFR-COST-002 Budget
Decision Session должна поддерживать cost/time budget и останавливаться/эскалировать при его превышении.

### NFR-COST-003 Adaptive Depth
Дополнительный эксперт/модель вызывается только при заданном условии: риск, конфликт, низкая confidence или требование пользователя/политики.

## 6. Explainability & Traceability

### NFR-EXP-001 Structured Rationale
Для Decision хранится структурированное rationale: key factors, trade-offs, uncertainties, rejected alternatives и evidence refs.

### NFR-EXP-002 No Hidden-CoT Dependency
Система не должна зависеть от сохранения скрытой chain-of-thought модели для аудита. Аудит строится на Decision Record, evidence, inputs/outputs, metrics и human actions.

### NFR-EXP-003 Goal Impact
Для существенного Decision должен быть указан ожидаемый эффект на одну или несколько Goal/Metric.

## 7. Observability

### NFR-OBS-001 Correlation ID
Request, Decision Session, build/test jobs и внешние вызовы должны поддерживать correlation/trace ID.

### NFR-OBS-002 Metrics
Минимально: request count, error rate, latency, job duration, LLM calls/tokens/cost, decision sessions, human overrides, failed gates.

### NFR-OBS-003 Logging
Логи структурированные; secrets и restricted content по умолчанию не логируются.

## 8. Maintainability

### NFR-MNT-001 Modular Monolith
MVP реализуется модульным монолитом с явными доменными границами; микросервисы вводятся по измеримой необходимости.

### NFR-MNT-002 Provider Independence
Expert Blueprint и Decision contracts не должны зависеть от API одной LLM.

### NFR-MNT-003 Schema First
Публичные структуры graph/decision/API версионируются и валидируются схемами/контрактными тестами.

### NFR-MNT-004 Documentation Trace
Существенное изменение модели/контракта обновляет соответствующий документ и Development Log.

## 9. Testability

### NFR-TST-001 Automated Validation
`GRAPH_SCHEMA_V0_1.json` и `DECISION_RECORD_SCHEMA.json` должны иметь автоматические positive/negative validation tests.

### NFR-TST-002 Gate Tests
До RELEASED обязательны unit + integration + API + authorization + security baseline tests.

### NFR-TST-003 Reproducible Fixture
Репозиторий должен содержать один воспроизводимый fixture `Sokrat → SOCRATES` для проверки graph/decision trace.

## 10. Portability

### NFR-PORT-001 Local First
Core MVP должен запускаться локально без обязательной зависимости от одного cloud provider.

### NFR-PORT-002 PostgreSQL Baseline
Основное долговременное хранилище MVP — PostgreSQL; pgvector добавляется для retrieval. Отдельная graph DB — только после доказанной необходимости.

## 11. NFR Acceptance Gate

Перед началом production-like эксплуатации должны быть измерены и записаны минимум:

- API P95;
- trace query P95;
- schema validation coverage;
- test pass rate;
- number of critical/high security findings;
- LLM cost per Decision Session;
- percentage of Decisions with evidence;
- percentage of high-impact Decisions with Human Gate;
- restore test result.

## Навигация

- ↑ [Requirements](README.md)
- ← [SRS v0.1](SRS_V0_1.md)
- ↔ [Architecture](../03_Architecture/README.md)
- ↔ [Security Review](../06_Security/)
