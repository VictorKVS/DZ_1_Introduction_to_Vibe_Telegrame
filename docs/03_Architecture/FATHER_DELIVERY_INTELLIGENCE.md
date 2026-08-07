# FATHER Delivery Intelligence

**Status:** Draft 0.1  
**Purpose:** архитектура проектной разведки, оценки, подбора ресурсов и накопления статистики для FATHER.

---

## 1. Назначение

FATHER должен уметь отвечать не только на вопрос **«как построить систему?»**, но и на вопросы:

- сколько это займёт времени;
- сколько это будет стоить;
- какие ресурсы потребуются;
- насколько надёжна оценка;
- какие внешние факторы могут сорвать проект;
- какой состав команды оптимален;
- что из аналогичных проектов уже известно;
- насколько фактический результат отклоняется от плана.

Поэтому оценка не должна быть одним ответом LLM. Она выделяется в отдельный вычислительный контур **FATHER Delivery Intelligence**.

---

## 2. Общая архитектура

```text
                         FATHER CORE
                              │
                    PROJECT INTELLIGENCE
                              │
       ┌──────────────────────┼──────────────────────┐
       ▼                      ▼                      ▼
 Project OSINT         Technology OSINT       Talent Intelligence
       │                      │                      │
       └──────────────────────┼──────────────────────┘
                              ▼
                       EVIDENCE LAYER
                              │
                              ▼
                      ESTIMATION ENGINE
                              │
          ┌───────────────────┼────────────────────┐
          ▼                   ▼                    ▼
        TIME                 COST                 TEAM
          │                   │                    │
          └───────────────────┼────────────────────┘
                              ▼
                         RISK ENGINE
                              │
                              ▼
                     DELIVERY PLANNER
                              │
                              ▼
                    DELIVERY CONTROLLER
                              │
                              ▼
                        PLAN vs FACT
                              │
                              ▼
                    VERIFIED EXPERIENCE
                              │
                              ▼
                      KNOWLEDGE BASE
```

---

## 3. Project Intelligence / OSINT

### 3.1. Project OSINT

Назначение: поиск внешних референсов для оценки класса проекта.

Ищет только законно доступные источники:

- open-source репозитории;
- публичные архитектурные разборы;
- case studies;
- postmortem;
- публичные отчёты;
- benchmark-исследования;
- технические статьи;
- данные о стоимости сервисов и инфраструктуры;
- официальную документацию продуктов;
- вакансии и публичные рыночные диапазоны ставок — как вспомогательный сигнал, а не как единственный источник цены.

Результат:

```yaml
reference_class:
  project_type: enterprise_rag
  comparable_projects: 12
  public_case_studies: 7
  repositories: 25
  common_components:
    - ingestion
    - retrieval
    - evaluation
    - access_control
  common_failure_modes:
    - poor_data_quality
    - integration_delay
    - missing_golden_dataset
  confidence: medium
```

### 3.2. Technology OSINT

Проверяет актуальные свойства технологического варианта:

- лицензирование;
- системные требования;
- стоимость;
- производительность;
- эксплуатационную зрелость;
- известные ограничения;
- security advisories;
- поддержку и частоту релизов;
- vendor lock-in;
- альтернативы.

OSINT не принимает архитектурное решение. Он поставляет **evidence** архитектору и Estimation Engine.

### 3.3. Talent Intelligence

Назначение: понять, какие компетенции и какой уровень исполнителей нужен проекту.

Допустимые данные:

- подтверждённый профессиональный опыт;
- публичное портфолио;
- GitHub и открытые contribution;
- технические публикации;
- результаты тестовых заданий;
- внутренние показатели прошлых проектов;
- соблюдение сроков;
- процент возвратов QA;
- повторные security defects;
- специализация по типам задач.

Не используются скрытые личные сведения, чувствительные категории и данные, не относящиеся к профессиональной пригодности.

---

## 4. Estimation Engine

Оценка выполняется несколькими методами и сопоставляется между собой.

### 4.1. Analogous Estimation

Использует похожие завершённые проекты.

```text
Новый проект
    ↓
Поиск аналогов
    ↓
Коррекция на масштаб / стек / риски / команду
    ↓
Range Estimate
```

### 4.2. Parametric Estimation

Использует параметрическую модель проекта, например:

```text
количество интеграций
количество ролей
количество экранов
объём документов
количество типов источников
число AI-компонентов
уровень security criticality
требуемый SLA
```

Параметрические коэффициенты должны постепенно калиброваться по собственным фактическим данным.

### 4.3. Bottom-Up

WBS декомпозируется до задач, которым можно назначить:

- роль;
- базовые часы;
- зависимости;
- параллельность;
- артефакт результата;
- критерии приёмки.

### 4.4. PERT для R&D

Для стохастических задач сохраняются три значения:

```text
O — optimistic
M — most likely
P — pessimistic
```

Расчёт:

```text
E = (O + 4M + P) / 6
σ = (P - O) / 6
```

Оценка должна показываться диапазоном, а не искусственно точной датой.

### 4.5. Historical Correction

После накопления статистики FATHER корректирует первоначальные оценки:

```yaml
historical_adjustment:
  task_class: external_api_integration
  samples: 34
  median_overrun: 0.18
  p80_overrun: 0.31
  confidence: 0.79
```

---

## 5. Risk Engine

Каждый риск должен быть связан с вероятностью, влиянием и стоимостью реагирования.

```text
Risk Exposure = Probability × Impact
```

Категории:

- Business;
- Scope;
- Data;
- AI / Model;
- Integration;
- Infrastructure;
- Security;
- Legal;
- Supplier;
- Team;
- Schedule;
- Operations.

Стратегии:

- Avoid;
- Mitigate;
- Transfer;
- Accept.

Риск может быть переведён в:

- дополнительные часы;
- резерв бюджета;
- изменение critical path;
- дополнительный security control;
- контрактное ограничение;
- Change Request.

---

## 6. Модель исполнителя

FATHER не оценивает человека как личность. Он оценивает **подтверждённую пригодность к конкретному типу работы**.

```yaml
performer_profile:
  role: senior_backend
  verified_skills:
    python: 0.92
    django: 0.88
    postgres: 0.86
  delivery_statistics:
    estimate_accuracy: 0.88
    on_time_rate: 0.91
    qa_first_pass: 0.84
    rework_ratio: 0.11
  security_quality:
    critical_defects_recent: 0
  task_velocity:
    standard_api: 1.15
    unfamiliar_ai_rnd: 0.70
  evidence_confidence: 0.81
```

Все коэффициенты должны иметь происхождение и не использоваться как скрытый автоматический HR-скоринг для значимых решений без участия человека.

---

## 7. Staffing Engine

После формирования WBS система строит несколько вариантов команды.

```text
Architecture
    ↓
WBS
    ↓
Skill Matrix
    ↓
Critical Tasks
    ↓
Required Seniority
    ↓
Available / Market Resources
    ↓
Team Scenarios
```

Пример вариантов:

```text
LEAN
1 Senior + part-time QA/Security
низкая стоимость / ниже параллельность

BALANCED
1 Senior + 2 Middle + QA + part-time Security/DevOps
баланс срока и стоимости

FAST DELIVERY
несколько Senior + параллельные потоки
короче календарный срок / выше стоимость и coordination overhead
```

Заказчику или PM передаётся выбор сценариев и trade-off, а не автоматическое решение.

---

## 8. Effort, Duration и Cost — разные величины

```text
Effort ≠ Calendar Duration ≠ Price
```

`Effort` — человеко-часы/дни.  
`Duration` — календарный срок с учётом зависимостей и параллельности.  
`Cost` — стоимость труда, инфраструктуры, лицензий, рисков и управления.

Нельзя делить суммарные часы на 8 и считать это сроком без dependency graph.

---

## 9. Budget Model

Смета включает минимум:

```text
Base WBS Effort
+ Technical Leadership Overhead
+ Architecture Oversight
+ AI/DS Lead Overhead
+ PM / Coordination
+ QA
+ Security
+ Confirmed Risk Buffer
+ Infrastructure CapEx
+ Expected OpEx
= Project Cost Baseline
```

В качестве первоначальной учебной модели допускаются коэффициенты из материалов курса OTUS, но они должны быть явно помечены как **external baseline / uncalibrated** до появления собственной статистики.

---

## 10. TCO

Для каждого архитектурного сценария оценивается не только запуск, но и владение:

```text
TCO = CapEx + OpEx за выбранный горизонт
```

Учитываются:

- разработка;
- данные и разметка;
- лицензии;
- оборудование;
- токены / inference;
- GPU;
- storage;
- monitoring;
- support;
- DevOps / MLOps;
- обновление базы знаний;
- security operations.

---

## 11. Delivery Controller

После начала разработки оценка превращается в прогнозируемую систему plan/fact.

Для задачи хранится:

```yaml
task_execution:
  task_id: TASK-207
  estimate_hours: 8
  pert_p80_hours: 13
  spent_hours: 14
  progress: 0.60
  tests: pending
  blockers:
    - external_api_mismatch
```

При пересечении порога FATHER:

1. создаёт Issue из Risk;
2. выполняет impact analysis;
3. пересчитывает critical path;
4. пересчитывает budget forecast;
5. предлагает mitigation;
6. при изменении scope создаёт Change Request.

---

## 12. Learning Loop

После завершения проекта:

```text
ПЛАН
 ↓
ФАКТ
 ↓
ОТКЛОНЕНИЕ
 ↓
ПРИЧИНА
 ↓
КАЧЕСТВО
 ↓
РИСКИ, КОТОРЫЕ РЕАЛИЗОВАЛИСЬ
 ↓
LESSONS LEARNED
 ↓
VERIFIED EXPERIENCE
 ↓
ESTIMATION KNOWLEDGE BASE
```

Следующие оценки должны постепенно использовать реальные распределения:

```text
p50
p80
p95
```

вместо только экспертных коэффициентов.

---

## 13. Security Requirements

Project Intelligence и Talent Intelligence являются потенциально чувствительными контурами.

Обязательные требования:

- законность источников;
- provenance каждого внешнего факта;
- разделение факта и вывода LLM;
- минимизация персональных данных;
- запрет скрытого профилирования по чувствительным признакам;
- RBAC/ABAC;
- журналирование поисковых запросов и решений;
- human approval для значимых кадровых решений;
- защита от prompt injection из внешних web-источников;
- очистка и классификация загружаемых данных;
- запрет автоматического доверия OSINT-источнику.

---

## 14. Минимальный PoC

Первый PoC Estimation Engine не требует собственного большого датасета.

Достаточно:

1. принять одну спецификацию проекта;
2. построить WBS;
3. разметить Engineering и R&D задачи;
4. оценить Engineering методом Bottom-Up;
5. оценить R&D методом PERT;
6. добавить Risk Register;
7. рассчитать три варианта команды;
8. получить диапазон срока и цены;
9. сохранить baseline;
10. после выполнения сравнить plan/fact.

Это создаёт первую собственную точку данных для обучения последующих оценок.

---

## 15. Принцип FATHER

> **Оценка без источников и диапазона — предположение.**
>
> **Оценка с WBS, PERT, рисками и аналогами — инженерная гипотеза.**
>
> **Оценка, откалиброванная сотнями plan/fact проектов, — корпоративный интеллектуальный актив.**
