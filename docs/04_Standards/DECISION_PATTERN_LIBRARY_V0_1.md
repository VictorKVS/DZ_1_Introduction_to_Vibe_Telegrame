# FATHER Decision Pattern Library v0.1

## Назначение

Реестр повторяемых способов принятия инженерных и управленческих решений в условиях ограничений, риска и неполной информации.

## Карточка decision pattern

```yaml
decision_pattern_id:
name:
trigger:
required_inputs:
methods:
required_experts:
required_gates:
output:
confidence_rule:
escalation_rule:
economic_rule:
validation:
```

## Начальный каталог

- `DP-001` Incomplete Information — определить недостающие данные, Value of Information, временной лимит, PERT/risk range и Human Gate.
- `DP-002` Architecture Alternatives — минимум две реалистичные альтернативы, trade-off analysis, NFR, Security/Legal/Economic gates, ADR.
- `DP-003` Buy / Build / Reuse — сравнение существующего решения, разработки и повторного использования по TCO, сроку, риску, lock-in и knowledge value.
- `DP-004` Security Control Selection — loss scenario → control cost → residual risk → avoided expected loss → решение владельца риска.
- `DP-005` Infrastructure Choice — workload → capacity → alternatives → security/compliance → TCO → resilience → selected infrastructure profile.
- `DP-006` Regulatory Change — изменение нормы → applicability → impact analysis → required changes → deadline/cost/risk → legal Human Gate.
- `DP-007` Change Request — scope change → impact on requirements/architecture/tests/infrastructure/cost/time → approve/reject/defer.
- `DP-008` Release Decision — quality + security + legal + economics + acceptance evidence → release / conditional release / block.
- `DP-009` Incident Response Investment — frequency/severity evidence → expected loss → response/control options → cost-benefit → prioritized action.
- `DP-010` Stop / Continue Project — sunk cost ignored; remaining cost, expected value, risk, opportunity cost and strategic value drive the decision.

## Принцип

Decision pattern не выдаёт ответ автоматически. Он стандартизирует **как должен быть получен и проверен ответ**.
