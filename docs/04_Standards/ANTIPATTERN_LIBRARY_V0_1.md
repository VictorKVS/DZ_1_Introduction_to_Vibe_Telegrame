# FATHER Anti-Pattern Library v0.1

## Назначение

Реестр решений и практик, которые систематически приводят к лишней стоимости, рискам, переделкам или ухудшению результата.

## Карточка anti-pattern

```yaml
antipattern_id:
name:
symptoms:
root_causes:
loss_mechanism:
security_impact:
legal_impact:
economic_impact:
detection:
prevention:
recovery:
observed_cases:
status:
```

## Начальный каталог

- `APT-001` Prompt-to-Production — переход от идеи прямо к коду без requirements/analysis/architecture/test baseline.
- `APT-002` Security-at-the-End — проверка ИБ только перед релизом.
- `APT-003` Compliance-at-the-End — подключение юриста после реализации.
- `APT-004` Zero-Means-Free — считать неизвестную стоимость равной отсутствующей стоимости.
- `APT-005` Architecture-by-Fashion — ввод технологии без требования и измеримой причины.
- `APT-006` Premature Microservices — раннее дробление без подтверждённой организационной/технической необходимости.
- `APT-007` Invisible Infrastructure — инфраструктура появляется без формального lifecycle и стоимости.
- `APT-008` Color-Only Risk Matrix — риск имеет цвет, но не связан со сценарием ущерба и деньгами.
- `APT-009` Decision Without Outcome — решение принято, но его ожидаемый и фактический эффект не отслеживаются.
- `APT-010` Document Graveyard — документы существуют без provenance, traceability, владельца и повторного использования.

## Экономический принцип

Для каждого подтверждённого anti-pattern FATHER должен стремиться сохранять фактическую цену ошибки: переделка, задержка, недополученная маржа, инциденты, штрафы и opportunity cost.
