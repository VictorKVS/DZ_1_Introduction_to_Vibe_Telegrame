# Stage 01 — Presale / Project Intake v0.1

## Назначение

Первый управляемый этап жизненного цикла FATHER. Его задача — не «продать любой ценой», а быстро и достаточно точно понять: что хочет заказчик, какую бизнес-проблему он решает, есть ли у нас право и возможность это делать, какие ограничения уже известны, какой диапазон сроков/стоимости реалистичен и стоит ли вообще запускать дальнейшее обследование.

Presale не заменяет Business Analysis, System Analysis или Architecture. Он создаёт минимально достаточный baseline для решения `GO / NO-GO / NEED-DISCOVERY`.

---

## 1. Почему этап существует

Без формального presale организация систематически получает:

- scope creep;
- обещания сроков до понимания объёма;
- нереалистичный Fixed Price;
- скрытые интеграции и инфраструктурные расходы;
- забытые ИБ/регуляторные ограничения;
- работу по проектам без достаточной маржи;
- конфликт ожиданий заказчика и команды;
- дорогие изменения уже после начала разработки.

Стоимость хорошего presale должна сравниваться со стоимостью предотвращённых переделок, отказов и убыточных обязательств.

---

## 2. Входы

Минимально возможные входы:

- описание идеи/проблемы заказчика;
- контактные лица и владельцы решения;
- предполагаемые пользователи;
- желаемый результат;
- известные сроки/дедлайны;
- бюджет или хотя бы допустимый диапазон, если заказчик готов его раскрыть;
- существующая инфраструктура и системы;
- известные интеграции;
- отрасль и юрисдикция;
- известные ограничения по данным/ИБ;
- имеющиеся документы, схемы, договоры, ТЗ предыдущих систем;
- критерий успеха глазами заказчика.

Неизвестные данные не удаляются из модели. Они фиксируются как `UNKNOWN / NOT_ESTIMATED / TO_DISCOVER`.

---

## 3. Обязательные артефакты

### PRE-001 — Opportunity / Project Intake Card

Обязательный короткий паспорт входящей возможности.

Содержит:

- customer/problem statement;
- sponsor / decision owner;
- target users;
- expected business outcome;
- urgency/deadline;
- known constraints;
- jurisdiction;
- known systems/integrations;
- confidentiality/data sensitivity indication;
- current stage;
- owner;
- next decision date.

### PRE-002 — Business Problem Statement

Кратко фиксирует:

`Current State → Pain / Loss → Desired State → Measurable Business Effect`.

Если нельзя сформулировать проблему отдельно от желаемой технологии, нужен дополнительный discovery.

### PRE-003 — Initial Scope Boundary

Фиксирует:

- in scope;
- out of scope;
- assumptions;
- dependencies;
- open questions;
- customer responsibilities.

### PRE-004 — Initial Risk & Constraint Register

Минимум категории:

- business;
- delivery;
- technical;
- security;
- legal/compliance;
- data;
- infrastructure;
- vendor/provider;
- staffing;
- economic.

### PRE-005 — Rough Order of Magnitude Estimate (ROM)

Не «точная смета», а диапазон.

Должны быть отдельно указаны:

- confidence level;
- assumptions;
- excluded costs;
- `NOT_ESTIMATED` cost categories;
- likely P50/P80 range where enough data exists;
- cost of discovery if required.

### PRE-006 — Initial Architecture Options Note

Не полноценная архитектура. Только 2–4 реалистичных класса решения, например:

- configure/buy;
- integrate/open source;
- build/custom;
- hybrid.

Для каждого: основные trade-offs, dependencies, rough cost/time, key risks.

### PRE-007 — Presale Decision Record

Результат:

- `GO`;
- `GO WITH CONDITIONS`;
- `NEED DISCOVERY`;
- `NO-GO`;
- `DEFER`.

Содержит причины, evidence, ограничения и следующий шаг.

---

## 4. Опциональные артефакты

Создаются только при необходимости:

- NDA / confidentiality record;
- RFI/RFP response;
- vendor questionnaire;
- high-level data-flow sketch;
- preliminary compliance memo;
- preliminary threat exposure note;
- PoC proposal;
- discovery plan;
- migration feasibility note;
- integration inventory;
- stakeholder map;
- competitor/analog review;
- Project Scout / GitHub Intelligence report;
- initial staffing hypothesis;
- initial infrastructure profile.

---

## 5. Роли

Минимальное ядро:

- Sales / Account Manager — коммерческий контакт и контекст клиента;
- Product / Business Analyst — проблема, ценность, scope;
- Solution / Software Architect — классы решений, технические ограничения;
- Project Manager / Estimator — сроки, зависимости, ресурсная модель;
- Security Expert — initial security exposure;
- Legal/Compliance Expert — jurisdiction/legal constraints;
- Economic/Finance role — ROM, margin, TCO categories, Cost of Delay.

Дополнительно по необходимости:

- infrastructure/cloud architect;
- data architect;
- domain expert;
- procurement/licensing expert;
- AI/ML architect;
- external specialist.

В FATHER большинство ролей может быть сначала представлено агентами, но высокий риск, юридически значимые обязательства, Fixed Price и финальное коммерческое предложение требуют Human Gate.

---

## 6. Требуемые компетенции

Компетенции измеряются отдельно от роли.

Примеры:

- problem framing;
- requirements elicitation;
- estimation under uncertainty;
- architecture option analysis;
- security triage;
- regulatory triage;
- economic modelling;
- negotiation;
- technical writing;
- OSINT / solution research;
- risk identification.

Для каждой компетенции в будущем хранится уровень, evidence, успешность применения и need-for-training.

---

## 7. Методики

Разрешённый набор выбирается по типу проекта:

- structured interview;
- stakeholder mapping;
- 5 Whys;
- problem framing;
- Value Proposition / Jobs-to-be-Done where applicable;
- Analogous estimation;
- Parametric estimation;
- PERT;
- Bottom-Up только для уже достаточно детализированных частей;
- risk matrix + expected loss where possible;
- Cost of Delay;
- buy/build/adapt analysis;
- Technology Radar / reuse review;
- preliminary data classification;
- high-level threat exposure review.

Методика должна сохраняться как часть Project Record, чтобы позднее сравнивать её точность.

---

## 8. Cross-Cutting Gates

### Quality Gate

Проверяет:

- проблема сформулирована;
- понятен ожидаемый outcome;
- scope boundary зафиксирован;
- неизвестные явно помечены;
- estimate содержит assumptions;
- нет ложной точности;
- decision owner известен.

### Security Gate

Проверяет минимум:

- будут ли обрабатываться чувствительные данные;
- есть ли внешние пользователи/интеграции;
- есть ли privileged operations;
- предполагаемые trust boundaries;
- требуется ли полноценный threat model на следующем этапе;
- нет ли очевидного неприемлемого security risk.

### Legal / Compliance Gate

Проверяет минимум:

- юрисдикцию;
- тип данных;
- наличие потенциально регулируемой отрасли;
- трансграничные потоки;
- лицензирование/интеллектуальную собственность;
- необходимость юридического review до коммерческого обязательства.

### Economic Gate

Проверяет:

- ROM range;
- cost placeholders;
- margin hypothesis;
- Cost of Delay;
- high-cost dependencies;
- hidden infrastructure/licensing/support costs;
- affordability / economic plausibility.

### Technology Strategy Gate

Проверяет:

- существует ли зрелое готовое решение;
- можно ли адаптировать open source;
- оправдана ли собственная разработка;
- vendor lock-in;
- migration/exit cost;
- technology maturity.

---

## 9. Метрики результата (Outcome Metrics)

Первые метрики появляются не сразу — часть измеряется после запуска проекта.

- Presale Decision Accuracy: доля GO-проектов, которые не пришлось отменять по причинам, которые можно было обнаружить на presale;
- Scope Stability after Discovery;
- Estimate Error after detailed planning;
- Margin Preservation;
- Customer Expectation Alignment;
- Discovery Conversion Rate;
- Avoided Loss from NO-GO decisions;
- percentage of hidden cost categories discovered before contract;
- percentage of critical security/legal constraints discovered before contract.

---

## 10. Метрики процесса

- lead time от первого контакта до Presale Decision;
- analyst hours;
- architect hours;
- security/legal/economic review hours;
- LLM/API cost;
- number of clarification cycles;
- number of unresolved critical questions;
- document production time;
- percentage of reused templates/capabilities;
- automation ratio;
- presale cost as percentage of expected contract value.

---

## 11. Метрики качества артефактов

Каждый артефакт оценивается минимум по:

- completeness;
- correctness;
- consistency;
- traceability;
- evidence coverage;
- ambiguity count;
- review findings;
- rework after next stage;
- usefulness to next stage.

Особенно важна последняя метрика: документ, который следующая стадия не использует, должен быть пересмотрен или удалён.

---

## 12. Метрики компетенций

По ролям/агентам/методикам:

- estimation accuracy;
- risk detection rate;
- missed constraint rate;
- false positive rate;
- recommendation acceptance rate;
- downstream rework attributed to presale;
- average confidence calibration;
- cost per useful recommendation;
- time to complete review;
- successful reuse rate.

Компетенция не равна «прочитан курс». Она подтверждается результатами работы.

---

## 13. Экономика этапа

Presale получает собственный `CostProfile`.

Статьи:

- human labor;
- agent/LLM cost;
- external expert cost;
- travel/meetings if applicable;
- tools/subscriptions;
- research/OSINT;
- PoC cost;
- legal review;
- security review;
- infrastructure estimation effort.

Одновременно считаются:

- expected contract value;
- expected margin;
- probability of win;
- expected presale value;
- avoided loss from rejection of bad project;
- cost of delay caused by excessive presale.

---

## 14. Риски самого Presale

- false confidence;
- anchoring on customer-proposed technology;
- optimism bias;
- sales pressure overriding engineering evidence;
- insufficient legal/security involvement;
- copying estimates from non-comparable projects;
- ignoring future operational cost;
- underestimated integration complexity;
- unvalidated assumptions;
- excessive presale bureaucracy.

---

## 15. Exit Criteria

Этап можно закрыть, если:

- есть Project Intake Card;
- сформулирован business problem;
- определён preliminary scope;
- зафиксированы assumptions/open questions;
- выполнены обязательные gates;
- существует ROM или явно зафиксирована невозможность оценки без discovery;
- определены архитектурные классы решения;
- принято решение GO/NO-GO/NEED-DISCOVERY;
- назначен владелец следующего этапа;
- все артефакты связаны с Project/Goal/Decision Record.

---

## 16. Maturity Model для Stage 01

### L1 — DEFINED

Есть шаблоны и обязательные документы.

### L2 — MEASURED

Считаем часы, стоимость, estimate error, rework.

### L3 — BASELINED

Есть статистические диапазоны по классам проектов.

### L4 — CONTROLLED

FATHER обнаруживает отклонения от baseline и требует review.

### L5 — OPTIMIZED

Шаблоны, роли и методики меняются на основании outcome.

### L6 — PREDICTIVE

Система прогнозирует вероятность перерасхода, scope change, security/legal blocker, экономическую нецелесообразность и необходимый объём discovery до заключения обязательств.

---

## 17. Что должно улучшаться со временем

Качество должно расти не за счёт увеличения количества документов, а за счёт:

- уменьшения пропущенных рисков;
- уменьшения downstream rework;
- повышения точности оценок;
- ускорения сбора контекста;
- роста reuse;
- повышения качества вопросов заказчику;
- улучшения калибровки confidence;
- лучшего раннего выявления NO-GO;
- уменьшения стоимости presale на сопоставимый проект.

Главная долгосрочная цель:

> Более быстрый presale должен одновременно становиться точнее, дешевле и полезнее для следующего этапа.

---

## 18. Связи с FATHER Knowledge Graph

Минимальная трасса:

```text
Customer Need
   ↓
Business Problem
   ↓
Goal
   ↓
Initial Scope / Constraints
   ↓
Risks / Evidence
   ↓
Architecture Options
   ↓
ROM / Economic Scenario
   ↓
Presale Decision
   ↓
Discovery / Requirements
```

После завершения проекта обратная трасса добавляет:

```text
Actual Cost / Time / Outcome
   ↓
Presale Accuracy
   ↓
Lessons Learned
   ↓
Updated Estimation Rules / Competency Scores / Standards
```

---

## Статус

`DEFINED / NOT YET VALIDATED ON REAL PROJECT CYCLE`
