# FATHER — Standards Profile v0.1

**Status:** BASELINE / EVOLVING  
**Purpose:** определить набор обязательных и подключаемых стандартов, требований заказчика и отраслевых правил для конкретного проекта.

## Идея

FATHER не должен зашивать один нормативный набор на все проекты. Для каждого проекта формируется `StandardsProfile`, который определяет, какие нормы и практики влияют на требования, архитектуру, ИБ, тесты, документы и критерии приёмки.

`Project → StandardsProfile → Requirements / Controls / Templates / Tests`

## Слои профиля

### 1. Engineering baseline

Общие правила системной и программной инженерии, управления требованиями, конфигурацией, изменениями и качеством.

### 2. Software engineering profile

Правила архитектуры, API, кодирования, тестирования, CI/CD, observability, reliability и сопровождения.

### 3. Security profile

Security by Construction, threat modeling, access control, secrets management, logging, vulnerability management, supply-chain security и security gates.

### 4. Regulatory / legal profile

Применимые законы, нормативные акты, договорные обязательства и ограничения обработки данных.

### 5. Industry profile

Отраслевые требования: медицина, промышленность, финансы, государственный сектор, строительство и другие домены.

### 6. Customer profile

Внутренние стандарты заказчика: архитектурные принципы, разрешённый стек, политики ИБ, SLA/SLO, шаблоны документов, требования к инфраструктуре.

## Структура StandardsProfile

```yaml
profile_id: STD-PROFILE-001
project_id: PROJECT-001
version: 0.1
status: DRAFT
standards:
  - standard_id: STD-001
    title: Example standard
    category: engineering
    applicability: REQUIRED
    source: official
    version: current
    clauses:
      - clause_id: C-001
        requirement_refs: []
        control_refs: []
        test_refs: []
exceptions: []
approved_by: null
```

## Applicability

- `REQUIRED` — обязательно для проекта;
- `CONTRACTUAL` — обязательно по договору;
- `REGULATORY` — обязательно по закону/регулятору;
- `RECOMMENDED` — инженерная практика;
- `OPTIONAL` — допустимо при наличии ценности;
- `NOT_APPLICABLE` — рассмотрено и обоснованно неприменимо.

## Правило трассировки

Стандарт не должен существовать в проекте как список литературы. Его применимое положение должно быть связано хотя бы с одним объектом:

`Standard Clause → Requirement / Control / Architecture Rule / TestCase / Document Template`

## Deviations / Exceptions

Любое отступление от обязательного профиля создаёт запись:

```yaml
exception_id:
standard_clause:
reason:
risk:
compensating_control:
approver:
expiry_date:
status:
```

Отступление без владельца, риска и срока пересмотра не допускается.

## Версионность

Профиль является versioned artifact. Обновление внешнего стандарта не переписывает историю завершённых решений. Создаётся новая версия профиля и Impact Analysis на активные проекты.

## MVP

Для первой вертикали достаточно трёх наборов:

1. `FATHER_BASELINE_ENGINEERING`;
2. `FATHER_BASELINE_SECURITY`;
3. `PROJECT_CUSTOM`.

Позже добавляются отраслевые и регуляторные профили без изменения ядра.

## Gate

До Architecture Baseline проект должен иметь утверждённый StandardsProfile или явно зафиксированный минимальный профиль для PoC.
