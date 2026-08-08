# FATHER Pattern Library v0.1

## Назначение

Реестр проверяемых переиспользуемых инженерных решений. Паттерн — не догма: он применяется только при выполнении условий применимости.

## Карточка паттерна

```yaml
pattern_id:
name:
problem:
context:
when_to_use:
when_not_to_use:
solution:
trade_offs:
security_effect:
legal_effect:
economic_effect:
infrastructure_effect:
required_tests:
observed_outcomes:
reuse_count:
success_rate:
status:
```

## Начальный каталог

- `PAT-001` Modular Monolith First — модульный монолит как базовый выбор до доказанной необходимости микросервисов.
- `PAT-002` Evidence-Backed RAG — важный вывод имеет provenance/evidence и статус доверия.
- `PAT-003` Human Gate for High Impact — существенное решение требует ответственного подтверждения.
- `PAT-004` Tests-as-Specification — acceptance и критические tests определяются до основной реализации.
- `PAT-005` Cost Placeholder — обязательная, но неизвестная статья затрат хранится как `0 + NOT_ESTIMATED`.
- `PAT-006` Threat-to-Money — риск переводится в loss scenario и residual expected loss.
- `PAT-007` Standards Profile — набор стандартов подключается по отрасли, юрисдикции и заказчику.
- `PAT-008` Infrastructure as Product — инфраструктура проектируется и проверяется как часть продукта.
- `PAT-009` Decision Record — сохраняются альтернативы, evidence, rationale, expected effect и validation plan.
- `PAT-010` Outcome Feedback Loop — фактический результат изменяет знания, стандарты и оценки.

## Зрелость

`IDEA → OBSERVED → REUSED → VALIDATED → STANDARD-CANDIDATE`
