# 07 — API

> Контракты API и интеграционных интерфейсов FATHER.

## Назначение

Раздел фиксирует API как инженерный контракт между Control Plane, интерфейсами, дочерними агентами и будущими внешними системами.

## Текущие документы

- [REST API Contract v0.1](REST_API_CONTRACT_V0_1.md) — минимальный REST-контракт первой вертикали `Project → Goal → Source/Evidence → DecisionSession → Alternatives → ExpertReviews → Decision`.

## Принципы

- API проектируется от доменной модели, а не от UI.
- Версионирование начинается с `/api/v1/`.
- Критические write-actions должны быть auditable.
- External IDs устойчивы и не зависят от внутреннего PK.
- Ошибки имеют единый envelope.
- Authentication/authorization и security requirements проектируются одновременно с API.

## Следующие шаги

- OpenAPI baseline;
- serializers/viewsets mapping;
- integration test полного trace;
- capability/tool API для дочерних агентов после появления Factory Runtime.

## Навигация

- ↑ [Карта документации](../README.md)
- 🏠 [Главный README](../../README.md)
- ↔ [Architecture](../03_Architecture/README.md)
- → [REST API Contract v0.1](REST_API_CONTRACT_V0_1.md)
