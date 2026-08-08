# FATHER — Engineering Delivery Pipeline v0.1

**Status:** ACCEPTED / EVOLVING  
**Purpose:** зафиксировать нормативную цепочку производства программного продукта в FATHER.

## Главный принцип

Код не является исходной точкой проекта. Код является производным артефактом, который создаётся только после достаточной формализации требований, анализа, архитектуры, критериев приёмки и тестов.

Базовая производственная цепочка:

```text
Business / User Need
        ↓
Техническое задание / Requirements Baseline
        ↓
Business Analysis
        ↓
System Analysis
        ↓
Architecture
        ↓
Security Architecture / Threat & Risk Analysis
        ↓
Test Design / Acceptance Criteria
        ↓
Implementation Plan / Estimate
        ↓
Code Generation / Development
        ↓
Automated Tests
        ↓
Integration / Security / Performance Tests
        ↓
Acceptance Tests
        ↓
Release
        ↓
Operational Metrics / Outcome
        ↓
Lessons Learned / Organizational Memory
```

## 1. Техническое задание и требования

ТЗ/requirements baseline фиксирует не пожелания в свободной форме, а проверяемое соглашение о том, что должно быть создано.

Минимально фиксируются:

- бизнес-цель;
- границы системы и scope;
- функциональные требования;
- нефункциональные требования;
- ограничения;
- интеграции;
- данные и их классификация;
- требования ИБ;
- критерии приёмки;
- критерии качества;
- требования к эксплуатации;
- допущения и зависимости;
- правила управления изменениями.

Требование не считается готовым к разработке, если нельзя определить способ его проверки.

## 2. Аналитика

Аналитический этап отвечает на вопрос: **что именно требуется сделать и почему**.

Артефакты:

- Business Requirements;
- Use Cases / User Stories;
- Process Model;
- Data Requirements;
- Domain Model;
- Integration Requirements;
- Acceptance Criteria;
- Risks / Assumptions / Constraints;
- traceability к исходной бизнес-цели.

Аналитик не проектирует код. Он устраняет неоднозначность требований и формирует проверяемую постановку задачи для архитектуры.

## 3. Архитектура

Архитектура отвечает на вопрос: **каким техническим способом выполнить требования с заданными ограничениями по стоимости, срокам, качеству, безопасности и сопровождению**.

Артефакты:

- System Context;
- Component / Container Architecture;
- Data Architecture;
- API / Interface Contracts;
- Deployment Architecture;
- Security Architecture;
- ADR;
- Technology Decisions;
- NFR mapping;
- оценки сложности и стоимости;
- эксплуатационные ограничения.

Каждый значимый архитектурный элемент должен быть трассируем к требованию, риску либо измеримому NFR.

## 4. Security by Construction

ИБ является сквозным контуром, а не финальной проверкой.

Проверяются:

- активы и данные;
- модель угроз;
- границы доверия;
- идентификация и аутентификация;
- авторизация;
- журналирование;
- секреты;
- криптографическая защита при необходимости;
- защита API;
- supply-chain risks;
- secure defaults;
- требования к тестам безопасности;
- обязательные Human Gates.

Security requirements становятся входными данными для архитектуры, кода и тестов.

## 5. Тесты проектируются ДО основного кода

До начала реализации должны существовать как минимум:

- Acceptance Criteria;
- Test Scenarios;
- негативные сценарии;
- security test cases;
- API contract tests;
- критические integration scenarios;
- NFR tests там, где они измеримы.

Это создаёт целевое состояние продукта, относительно которого можно проверять сгенерированный или написанный код.

## 6. Код как производный артефакт

На вход генератору/разработчику передаются:

```text
Approved Requirements
+ Domain Model
+ Architecture
+ API Contracts
+ Data Contracts
+ Security Requirements
+ Test Specifications
+ Coding Standards
+ Reusable Capabilities
```

На выходе должны появиться:

- source code;
- migrations;
- configuration;
- API implementation;
- unit tests;
- integration tests;
- security controls;
- observability hooks;
- build/deployment artefacts;
- documentation generated from the same baseline where possible.

Таким образом LLM не получает инструкцию «напиши приложение». Она получает инженерный пакет производства.

## 7. Финальный Verification & Validation

После реализации выполняются два разных класса проверки.

### Verification

> Мы правильно реализовали спецификацию?

Проверяются:

- unit tests;
- contracts;
- integrations;
- SAST/SCA;
- authorization;
- secrets;
- migrations;
- API schemas;
- performance/NFR tests;
- security tests.

### Validation

> Мы создали то, что действительно решает задачу заказчика?

Проверяются:

- Acceptance Criteria;
- бизнес-сценарии;
- пользовательский результат;
- экономический эффект;
- эксплуатационная пригодность.

## 8. Двухуровневая система тестов

FATHER различает:

1. **Tests-as-Specification** — тесты и критерии, созданные до реализации из требований и архитектуры.
2. **Implementation Tests** — unit/integration/security/regression tests, создаваемые вместе с кодом.

Второй набор не может тихо изменить первый. Если код не проходит исходный acceptance test, необходимо либо исправить код, либо провести формальный Change Request требований.

## 9. Traceability

Для критических элементов должна существовать цепочка:

```text
Goal
 ↓
Requirement
 ↓
Analysis Artifact
 ↓
Architecture Decision
 ↓
Security Control
 ↓
Test Case
 ↓
Code Artifact
 ↓
Test Run
 ↓
Metric
 ↓
Outcome
```

Это позволяет через годы определить:

- зачем существует конкретный участок кода;
- какое требование он реализует;
- какими тестами он проверяется;
- какой риск закрывает;
- что произойдёт при его изменении;
- какой бизнес-эффект он обеспечивает.

## 10. Изменение кода в будущем

Перед изменением CodeArtifact FATHER должен иметь возможность выполнить impact analysis:

```text
CodeArtifact
  ├── implements → Requirement
  ├── belongs_to → Component
  ├── verified_by → Tests
  ├── mitigates → Risk / Control
  ├── contributes_to → Metric
  └── contributes_to → Goal
```

После изменения автоматически определяется минимальный набор:

- документов для пересмотра;
- зависимых компонентов;
- regression tests;
- security tests;
- acceptance tests;
- метрик для повторного измерения.

## 11. Стандарты как профили

FATHER не должен жёстко зашивать единственный стандарт на все отрасли. Используется базовый pipeline и подключаемые **Standards Profiles**.

Пример:

```text
FATHER Core Engineering Standard
        +
Software Engineering Profile
        +
Security Profile
        +
Industry / Customer Profile
        +
Contract / Regulatory Profile
```

В профиль могут входить ГОСТ, ISO/IEC/IEEE, OWASP, NIST, внутренние стандарты заказчика и иные применимые требования. Конкретный состав профиля фиксируется для проекта и версионируется.

## 12. Definition of Ready for Coding

Кодирование начинается только если:

- требования имеют baseline;
- критические неоднозначности разрешены либо явно отмечены;
- NFR определены;
- архитектура принята;
- API/data contracts определены для затрагиваемых интерфейсов;
- security requirements определены;
- acceptance criteria существуют;
- критические тестовые сценарии подготовлены;
- оценка/риски зафиксированы;
- изменения находятся под Change Management.

## 13. Definition of Done

Функция/компонент не считается завершённым только потому, что код написан.

Необходимо:

- соответствие baseline requirements;
- прохождение обязательных тестов;
- security gate;
- traceability;
- документация/контракты актуальны;
- план/факт сохранён;
- результат измерим;
- Development Log обновлён;
- Lessons Learned фиксируются после появления фактического результата.

## Архитектурный вывод

FATHER должен генерировать код **из инженерного пакета**, а не из одиночного промпта.

Это превращает цепочку

`Prompt → Code`

в управляемое производство:

`Need → Requirements → Analysis → Architecture → Tests → Code → Verification → Outcome → Learning`.
