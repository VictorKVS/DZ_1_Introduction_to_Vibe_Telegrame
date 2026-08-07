# FATHER Innovation Registry

> Реестр продуктовых идей, исследований и интеллектуальных активов FATHER.
>
> Базовый принцип: **Every Project Must Leave an Asset** — каждый исследованный замысел, даже не дошедший до разработки, должен оставить повторно используемый актив: исследование, архитектуру, паттерн, тест, датасет, оценочную модель, компонент, антипаттерн или продуктовую концепцию.

## Назначение

Innovation Registry хранит не просто список идей, а их путь от гипотезы до коммерческого продукта. Идеи не удаляются: они могут быть отложены, отклонены, переработаны или возвращены в работу после появления новых технологий, рынка или финансирования.

## Idea Readiness Level (IRL)

| Уровень | Состояние |
|---|---|
| IRL-0 | Идея зафиксирована |
| IRL-1 | Проблема и целевая аудитория сформулированы |
| IRL-2 | Проведено исследование рынка, аналогов и ограничений |
| IRL-3 | Сформированы варианты решения и целевая архитектура |
| IRL-4 | Подготовлен и проверен PoC |
| IRL-5 | Рабочий прототип |
| IRL-6 | MVP |
| IRL-7 | Первый платящий клиент / подтвержденная бизнес-ценность |
| IRL-8 | Коммерческий продукт |
| IRL-9 | Масштабируемый повторяемый продукт / шаблон репликации |

## Статусы

`BACKLOG` · `RESEARCH` · `ARCHITECTURE` · `POC` · `PROTOTYPE` · `MVP` · `COMMERCIAL` · `FUTURE` · `FROZEN` · `REJECTED`

## Реестр

| ID | Идея | Направление | IRL | Статус | Приоритет | Следующий шаг |
|---|---|---|---:|---|---|---|
| FTR-0001 | FATHER Product & Agent Factory | Platform | 2 | RESEARCH | Critical | Создать Django Control Plane и формализовать Domain Model |
| FTR-0002 | Knowledge Factory | Knowledge | 2 | RESEARCH | Critical | Source → Evidence → Knowledge Item → Versioning → Retrieval |
| FTR-0003 | Agent Factory | Agents | 2 | RESEARCH | Critical | Agent Blueprint, permissions, tools, tests, lifecycle |
| FTR-0004 | AI Product Discovery | Product / Presale | 2 | RESEARCH | High | Экспертный прогон идеи + рынок + варианты + оценка |
| FTR-0005 | GitHub Reengineering Engine | Engineering Intelligence | 1 | RESEARCH | High | Анализ похожих проектов, reuse assessment, migration plan |
| FTR-0006 | Estimation & Delivery Intelligence | Estimation | 2 | RESEARCH | Critical | WBS + PERT + Analogous + Bottom-Up + Plan/Fact + TCO |
| FTR-0007 | OSINT Project Intelligence | Research | 1 | RESEARCH | High | Сбор доказательств по рынку, технологиям и референсным проектам |
| FTR-0008 | Professional Mentor Agent | Personal / Professional | 0 | FUTURE | Medium | Исследовать модель долгосрочного профессионального наставничества |
| FTR-0009 | Olympiad Mentor | Education | 0 | FUTURE | High | Персональная подготовка детей к олимпиадам по математике и другим предметам |
| FTR-0010 | Personal Cognitive Mentor | Personal / Aging | 0 | FUTURE | High | Исследовать безопасную поддержку памяти, мотивации и повседневной активности пожилых |
| FTR-0011 | Personal Life Knowledge Core | Personal Knowledge | 0 | FUTURE | Medium | Модель персональной базы знаний и сменных специализированных агентов |
| FTR-0012 | Agent Marketplace / Product Showcase | Commercial | 0 | BACKLOG | Medium | Витрина исследованных идей, PoC, шаблонов и готовых агентов |

## Миссии

### MISSION-001 — Agent for Everyone

**Агент для каждого.** Не универсальный чат, а набор персонализированных цифровых соратников, наставников и профессиональных помощников, усиливающих человека, а не заменяющих его.

### MISSION-002 — Product Factory

FATHER должен уметь превращать идею в исследованную продуктовую гипотезу, набор вариантов, согласованную архитектуру, план, оценку и при подтверждении — в работающий продукт.

### MISSION-003 — Lifelong Mentorship

В долгосрочной перспективе персональные агенты могут сопровождать человека на разных этапах жизни: обучение, профессиональное развитие, планирование, поддержка памяти и повседневной самостоятельности.

### MISSION-004 — Every Project Must Leave an Asset

Время, токены, исследования, ошибки и решения не должны исчезать после завершения проекта. Они должны пополнять проверенную инженерную память FATHER.

## Правила реестра

1. Идея получает постоянный идентификатор `FTR-XXXX`.
2. Исходная формулировка идеи сохраняется неизменно; последующие версии оформляются отдельно.
3. Любое исследование должно фиксировать источники, дату, применимость и уровень доверия.
4. `REJECTED` не означает удаление: причина отказа становится знанием и может быть пересмотрена позже.
5. Переход между IRL должен подтверждаться артефактом или проверяемым результатом.
6. Для High/Critical Security сценариев обязательна отдельная Security Review независимо от IRL.
7. Медицинские и детские сценарии не должны позиционироваться как замена врачу, родителю, преподавателю или ответственному специалисту.
8. Идеи, связанные с людьми, проектируются по принципам human-in-the-loop, privacy-by-design и минимизации данных.
9. Повторное использование чужих решений означает анализ идей, паттернов и допустимых компонентов с учетом лицензий; целью является собственное решение, а не копирование продукта.

## Шаблон новой карточки

```yaml
idea:
  id: FTR-XXXX
  title: ""
  status: BACKLOG
  irl: 0
  priority: Medium
  domain: ""
  created_at: ""

problem:
  statement: ""
  target_users: []
  business_value: ""

research:
  market: null
  competitors: []
  github_references: []
  standards: []
  evidence: []

solution:
  options: []
  recommended_option: null
  architecture_status: null

estimation:
  effort: null
  duration: null
  cost: null
  tco: null
  confidence: null

risk:
  business: []
  legal: []
  security: []
  technical: []

assets_created: []
next_step: ""
```
