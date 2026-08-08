# FATHER — Economic Gate v0.1

**Status:** ACCEPTED / EARLY BASELINE  
**Purpose:** встроить проверку экономической целесообразности во все стадии инженерного производства FATHER.

[← Architecture](README.md)

## Принцип

Экономическая проверка не является отдельной финальной сметой. Она сопровождает проект от идеи до эксплуатации и отвечает на вопрос: **создаёт ли предлагаемое решение достаточную ценность относительно стоимости, сроков, риска и альтернатив?**

Базовый конвейер:

`Idea → Requirements → Analysis → Architecture → Test Design → Estimate → Code → Release → Operations → Outcome`

На каждом этапе выполняется Economic Gate соответствующей глубины.

## Экономические проверки по этапам

| Этап | Economic Gate |
|---|---|
| Idea / Presale | размер проблемы, потенциальная ценность, бюджетный диапазон, Cost of Delay, build/buy/no-go |
| Requirements | стоимость требований, MoSCoW/приоритет, value vs effort, обязательные/опциональные функции |
| Analysis | альтернативы, ограничения, стоимость неопределённости, Value of Information |
| Architecture | TCO, CAPEX/OPEX, лицензии, инфраструктура, стоимость сопровождения, цена сложности |
| Security / Legal | стоимость обязательных контролей, стоимость нарушения/штрафов/инцидентов, остаточный риск |
| Test Design | стоимость тестирования против стоимости дефекта и переделки |
| Implementation Plan | Bottom-Up/PERT, P50/P80, contingency, staffing profile, календарный план |
| Development | фактические часы, LLM/API/cloud cost, rework, deviation from estimate |
| Release | release cost, rollback cost, support readiness, operational budget |
| Operations | unit economics, cloud/runtime cost, support cost, reliability cost |
| Outcome | ROI, NPV/payback при применимости, бизнес-эффект, plan/fact, opportunity cost |

## Обязательные поля Economic Record

```yaml
project_id:
stage:
decision_ref:
alternatives:
assumptions:
planned_hours:
planned_cost:
confidence_range:
p50:
p80:
capex:
opex:
tco:
expected_value:
cost_of_delay:
value_of_information:
risk_cost:
reasoning_cost:
actual_hours:
actual_cost:
deviation:
outcome_ref:
approver:
status:
```

Поля применяются по необходимости; отсутствие данных должно фиксироваться явно, а не заменяться выдуманной точностью.

## Методы первой версии

- Analogous Estimation;
- Parametric Estimation;
- Bottom-Up;
- PERT / three-point estimate;
- contingency / risk reserve;
- TCO;
- ROI;
- payback;
- NPV — когда есть приемлемые денежные потоки и горизонт;
- Cost of Delay;
- Value of Information;
- sensitivity / scenario analysis;
- plan/fact deviation analysis.

## Экономика AI

Для AI/agent workloads отдельно фиксируются:

- model/provider;
- input/output tokens;
- cost per session;
- retrieval/embedding cost;
- external API cost;
- latency;
- retries;
- human review time;
- cost of expert council;
- cost per successful outcome.

Цель — сравнивать не «какая модель умнее», а **какая конфигурация даёт приемлемое качество решения при заданной цене, задержке и риске**.

## Human Gate

Economic Gate не принимает самостоятельно существенные инвестиционные решения. Он формирует расчёт, диапазон неопределённости, альтернативы и рекомендацию.

Обязательный Human Gate применяется при:

- превышении согласованного бюджета/резерва;
- существенном изменении scope;
- высоком финансовом риске;
- необратимых CAPEX-решениях;
- слабой доказательной базе;
- конфликте экономии с Security/Legal/Quality Gate.

## Конфликт ворот

Минимальная система принятия решения FATHER использует четыре параллельных оценки:

`QUALITY + SECURITY + LEGAL/COMPLIANCE + ECONOMICS`

Экономическая выгода не отменяет обязательные требования закона и согласованный уровень безопасности. Аналогично безопасность не должна автоматически приводить к максимально дорогой архитектуре: выбирается **достаточный и доказуемый контроль**, соответствующий риску и требованиям.

## Обучение на факте

После завершения проекта обязательно сохраняются:

`Estimate → Actual → Deviation → Cause → Outcome → Lesson → Updated Estimation Rule`

В дальнейшем FATHER должен рассчитывать статистику точности методов, технологий, типов работ и профилей исполнителей по классам проектов.

## Gate

Этап не считается экономически подтверждённым, если невозможно показать:

1. какие альтернативы рассматривались;
2. сколько они ориентировочно стоят;
3. какова неопределённость оценки;
4. какой эффект ожидается;
5. как будет измерен фактический результат.
