# 09 — Architecture Decisions

> Реестр ADR — история существенных архитектурных решений FATHER.

[← К карте документации](../README.md) · [↑ Главный README](../../README.md)

## Назначение

ADR фиксируют не только выбранное решение, но и контекст, альтернативы, причины выбора, последствия, риски и условия пересмотра. Это позволяет FATHER накапливать архитектурную память и в будущем сравнивать решения с фактическими результатами проектов.

## Жизненный цикл решения

```text
Problem / Requirement
        ↓
Alternatives
        ↓
Analysis
        ↓
Decision
        ↓
Approval
        ↓
Implementation
        ↓
Plan vs Fact
        ↓
Lesson Learned
```

## Статусы ADR

- `PROPOSED`
- `ACCEPTED`
- `SUPERSEDED`
- `REJECTED`
- `DEPRECATED`

## Текущие ADR

- [ADR-002 — Project Intelligence & Estimation Engine](ADR-002-Project-Intelligence-Estimation-Engine.md) — выделить в FATHER самостоятельный контур OSINT, оценки сроков/денег, рисков, staffing и plan/fact.

## Правило FATHER

Существенное архитектурное решение не должно исчезать после изменения проекта. При смене решения создаётся новое ADR или фиксируется `SUPERSEDED`, чтобы сохранялась история: **что выбрали, почему, что получили фактически и чему научились**.
