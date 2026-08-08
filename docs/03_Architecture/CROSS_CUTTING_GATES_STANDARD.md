# FATHER — Cross-Cutting Gates Standard v0.1

**Status:** ACCEPTED / BASELINE  
**Purpose:** закрепить обязательные сквозные проверки качества, ИБ, права/комплаенса и экономики на всех стадиях производства.

[← Architecture](README.md)

## Основной принцип

Ни один этап FATHER не считается завершённым только потому, что создан его основной артефакт. Для перехода на следующий этап должны быть выполнены применимые сквозные проверки.

Минимальный набор ворот:

- **Quality Gate** — полнота, корректность, трассируемость, тестируемость;
- **Security Gate** — угрозы, доступ, конфигурация, уязвимости, остаточный риск;
- **Legal / Compliance Gate** — применимые юрисдикции, нормативы, договорные и отраслевые обязательства;
- **Economic Gate** — стоимость, сроки, TCO, неопределённость, эффект, альтернативы.

## Матрица по жизненному циклу

| Stage | Quality | Security | Legal / Compliance | Economics |
|---|---|---|---|---|
| Idea / Presale | проблема и критерий успеха | sensitivity / misuse screening | jurisdiction / lawful feasibility | value, budget range, no-go alternatives |
| Requirements | completeness / acceptance criteria | security requirements | mandatory obligations | cost/value prioritization |
| Analysis | assumptions / evidence | data flows / abuse cases | applicable norms / roles | alternatives / Value of Information |
| Architecture | ADR / NFR coverage | threat model / trust boundaries | localization / contractual constraints | TCO / complexity cost |
| API & Data Design | contract consistency | authn/authz/logging/data protection | retention / data subject / sector rules | integration and storage cost |
| Test Design | coverage / traceability | security test plan | compliance evidence plan | test cost vs defect cost |
| Implementation | code quality | SAST/SCA/secrets/config | license/obligation checks where relevant | plan/fact hours and runtime cost |
| Build / Deploy | reproducibility | container/IaC/config scans | deployment jurisdiction constraints | infrastructure/release cost |
| Acceptance | acceptance criteria | security acceptance | compliance acceptance | budget/value acceptance |
| Operations | SLO/SLA / defects | monitoring/incidents/access review | regulatory change watch | unit economics / support cost |
| Change | regression impact | security impact | regulatory impact | cost/schedule/value impact |
| Outcome | product quality | incidents / residual risk | violations / audit results | ROI / plan-fact / benefit realization |

## Gate Result

Каждая проверка возвращает стандартизированный результат:

```yaml
gate_id:
project_id:
stage:
gate_type: QUALITY | SECURITY | LEGAL | ECONOMIC
profile_version:
checks:
findings:
critical_findings:
residual_risk:
evidence_refs:
required_actions:
owner:
reviewer:
status: PASS | PASS_WITH_ACTIONS | FAIL | NOT_APPLICABLE
valid_until:
```

## Правила перехода

- `FAIL` блокирует переход стадии, если только формальный Human Gate не допускает исключение там, где исключение юридически и технически возможно.
- Критические Legal/Compliance ограничения не могут быть отменены экономической выгодой.
- Критический Security finding не закрывается только принятием финансового риска без отдельного формального решения и допустимости такого решения.
- `PASS_WITH_ACTIONS` обязан создавать отслеживаемые задачи с владельцем и сроком.
- `NOT_APPLICABLE` требует причины, чтобы проверки нельзя было молча пропускать.

## Standards Profiles

Состав проверок определяется активными профилями проекта:

`Base Engineering + Software + Security + Jurisdiction + Industry + Customer`.

Профиль должен быть версионируемым. Изменение профиля создаёт `ChangeEvent` и запускает Impact Analysis для связанных Requirements, Controls, Tests, CodeArtifacts и Deployments.

## Evidence-first

Результат ворот не должен быть только текстовой оценкой LLM. Где возможно, он связан с проверяемым evidence:

- пунктом стандарта;
- требованием;
- ADR;
- Threat Model;
- результатом теста;
- scanner output;
- договорным условием;
- расчётом стоимости;
- Human approval.

## Automation policy

FATHER автоматизирует проверки, которые можно выполнить воспроизводимо. Высокорисковые, спорные или юридически значимые выводы эскалируются специалисту.

`Machine Check → Evidence → Expert Review when needed → Human Gate → Gate Record`.

## Definition of Done для стадии

Стадия завершена только когда:

1. создан основной артефакт;
2. выполнены обязательные Gate Checks;
3. findings либо устранены, либо формально приняты;
4. трассировка обновлена;
5. тесты/доказательства сохранены;
6. стоимость и plan/fact обновлены;
7. существенные изменения внесены в Development Log.

## Производственная цель

Эта модель делает FATHER не генератором артефактов, а контролируемой производственной системой, в которой качество, безопасность, законность и экономика являются свойствами процесса с самого начала, а не внешней проверкой после написания продукта.
