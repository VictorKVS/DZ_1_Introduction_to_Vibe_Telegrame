# Architecture Governance & Metrics v0.1

## Назначение

Этот документ задаёт порядок архитектурного разбора каждого этапа FATHER: зачем он существует, какие документы и артефакты обязательны, какие метрики измеряются, как оцениваются качество, производительность и компетенции, и как система должна улучшаться со временем.

## Базовый принцип

Каждый этап производственного цикла обязан отвечать на восемь вопросов:

1. Какую проблему решает этап?
2. Почему он необходим именно в этом месте жизненного цикла?
3. Какие входы ему нужны?
4. Какие документы/артефакты он обязан породить?
5. Какие проверки и gates обязательны?
6. Какими метриками измеряется качество результата и эффективность процесса?
7. Какие компетенции нужны человеку/агенту для выполнения этапа?
8. Как результаты этапа улучшают следующий проект и соответствующий стандарт?

## Карточка архитектурного этапа

Для каждого этапа создаётся Stage Definition:

```yaml
stage_id:
title:
purpose:
business_reason:
entry_criteria:
inputs:
required_artifacts:
optional_artifacts:
standards:
roles:
competencies:
methods:
tools:
quality_gates:
security_gates:
legal_gates:
economic_gates:
technology_strategy_gate:
metrics:
exit_criteria:
traceability:
expected_cost:
expected_duration:
risks:
learning_outputs:
owner:
version:
status:
```

## Три уровня метрик

### 1. Outcome Metrics — качество результата

Показывают, получили ли мы нужный продукт/решение.

Примеры:
- fulfilment требований;
- acceptance pass rate;
- escaped defects;
- security findings after release;
- legal/compliance exceptions;
- business outcome vs expected value;
- фактический ROI/TCO/Cost of Delay;
- reliability/SLO achievement.

### 2. Process Metrics — производительность процесса

Показывают, насколько эффективно мы производим результат.

Примеры:
- lead time;
- cycle time этапа;
- wait time между этапами;
- rework rate;
- number of review cycles;
- automation ratio;
- cost per artifact;
- cost per accepted requirement;
- deployment frequency;
- change failure rate;
- MTTR;
- estimation error plan/fact.

### 3. Capability & Competency Metrics — способность организации

Показывают, почему качество/скорость растут или падают.

Примеры:
- уровень зрелости capability;
- качество решений по роли;
- accuracy экспертных прогнозов;
- доля работ без ручной переделки;
- reuse rate;
- число validated patterns;
- число повторно используемых шаблонов;
- skill coverage по ролям;
- gap между требуемыми и фактическими компетенциями;
- learning velocity;
- стоимость обучения до достижения требуемого уровня.

## Нельзя смешивать качество и скорость

Ускорение этапа не считается улучшением, если ухудшились outcome-метрики. Повышение качества не считается эффективным, если его стоимость и сроки непропорциональны бизнес-ценности.

Каждое улучшение оценивается минимум по четырём координатам:

```text
Quality
Speed
Cost
Risk
```

Дополнительно отслеживаются:

```text
Knowledge Value
Competency Growth
Reuse
Automation
```

## Quality Baseline

Для каждого класса артефактов создаётся измеримый baseline.

Пример для SRS:
- traceability coverage >= target;
- unresolved ambiguity count <= target;
- testable requirements ratio >= target;
- security/legal/economic requirements coverage >= target;
- number of change requests caused by requirement defects;
- defects escaped from requirements stage.

Пример для Architecture:
- ADR coverage;
- NFR traceability;
- threat-model coverage;
- identified dependency risks;
- estimated TCO;
- migration/exit strategy for critical dependencies;
- architecture-driven defect/rework rate.

Пример для Code:
- tests pass;
- coverage target where meaningful;
- complexity thresholds;
- SAST/SCA/secrets findings;
- code review findings;
- escaped defects;
- change failure rate;
- maintainability/rework data.

## Производительность как поток

FATHER должен измерять не только длительность отдельных задач, но и полный value stream:

```text
Request
  ↓
Analysis
  ↓
Architecture
  ↓
Tests-as-Specification
  ↓
Implementation
  ↓
Verification
  ↓
Release
  ↓
Outcome
```

Для каждого перехода фиксируются work time и wait time. Узкие места выявляются по факту, а не по впечатлению.

## Компетенции

Каждая роль получает Competency Profile:

```yaml
role:
required_competencies:
level_required:
evidence_required:
methods_known:
tools_known:
validated_projects:
decision_accuracy:
quality_score:
rework_caused:
learning_plan:
```

Компетенция не считается подтверждённой только по курсу или сертификату. Evidence может включать:
- успешно выполненные задачи;
- review quality;
- решения и их outcome;
- тесты;
- отсутствие/частоту переделок;
- подтверждённое применение методик.

## Цикл улучшения

После каждого проекта/релиза:

```text
Plan
 ↓
Fact
 ↓
Deviation
 ↓
Root Cause
 ↓
Was it Process / Standard / Tool / Competency / Architecture?
 ↓
Corrective Action
 ↓
Update Standard / Pattern / Training / Tooling
 ↓
Next Baseline
```

## Архитектурный аудит документов

Каждый документ проверяется не по принципу «он есть», а по пяти признакам:

1. Necessity — зачем он нужен и какое решение/контроль поддерживает.
2. Sufficiency — достаточно ли содержимого для следующего этапа.
3. Traceability — связан ли он с целями, требованиями, решениями, тестами и outcome.
4. Measurability — можно ли оценить его качество.
5. Reuse Value — может ли он стать шаблоном/знанием для следующих проектов.

Документ без доказуемой функции должен быть либо упрощён, объединён, либо исключён.

## Первая очередь архитектурного разбора

1. Project Intake / Presale
2. Business Requirements
3. Business Analysis
4. System Analysis
5. Architecture
6. Security Engineering
7. Legal/Compliance
8. Economics & Estimation
9. Infrastructure
10. Test Engineering
11. Software Development
12. DevSecOps / CI/CD
13. Release & Deployment
14. Operations & Observability
15. Incident / Problem Management
16. Change & Impact Management
17. Outcome / Benefits Realization
18. Organizational Memory
19. Competency Development
20. Standard Improvement

Для каждого пункта должен появиться отдельный Stage Card с набором документов, RACI/ролями, компетенциями, gates, метриками, target/baseline и правилами улучшения.

## Принцип зрелости

Стандарт или процесс проходит уровни:

```text
DEFINED
  ↓
MEASURED
  ↓
BASELINED
  ↓
CONTROLLED
  ↓
OPTIMIZED
  ↓
PREDICTIVE
```

`PREDICTIVE` означает, что накопленных данных достаточно, чтобы система заранее оценивала качество, срок, стоимость и вероятность переделок с измеримой ошибкой прогноза.

## Ключевой вывод

Цель FATHER — не максимальная документация и не максимальная скорость. Цель — непрерывный рост способности организации стабильно производить нужный результат с меньшими сроками, затратами, риском и количеством переделок при одновременном росте инженерных компетенций и повторного использования знаний.
