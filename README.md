# FATHER — Agent Engineering Factory

> **FATHER проектирует проекты, которые создают агентов.**

FATHER — учебно-инженерный прототип метасистемы для анализа идей, проектирования, оценки, создания, тестирования и сопровождения AI-агентов. Текущая версия строится как единое ядро с Web- и Telegram-интерфейсами.

## Навигация по проекту

FATHER ведётся как иерархическая инженерная система: **каждый функциональный блок имеет собственный `README.md`, а родительские README содержат ссылки на дочерние блоки**.

- [Документация — карта разделов](docs/README.md)
  - [00 — Project Management](docs/00_Project_Management/README.md)
    - [FATHER Documentation Standard](docs/00_Project_Management/DOCUMENTATION_STANDARD.md)
    - [GitHub Pages / Engineering Portal Plan](docs/00_Project_Management/GITHUB_PAGES_PLAN.md)
  - [03 — Architecture](docs/03_Architecture/README.md)
  - [09 — Architecture Decisions / ADR](docs/09_Decisions/README.md)
- [90 — Innovation Registry](90_Innovation_Registry/README.md)
  - [Главный реестр идей](90_Innovation_Registry/Registry.md)
  - [FTR-0009 — Olympiad Mentor](90_Innovation_Registry/FTR-0009-Olympiad-Mentor.md)
  - [FTR-0010 — Personal Cognitive Mentor](90_Innovation_Registry/FTR-0010-Personal-Cognitive-Mentor.md)

### Правило сопровождения README

При создании нового крупного блока FATHER должен одновременно:

1. создать локальный `README.md`;
2. описать назначение, границы, входы/выходы, статус и следующие шаги;
3. добавить ссылку в README родительского раздела;
4. при необходимости добавить ссылку в этот главный README;
5. не оставлять документы без навигации;
6. проверять целостность ссылок и пригодность документов к публикации.

Это считается частью поведения будущего агента FATHER, а не ручной косметикой репозитория.

## Documentation Portal

Markdown в Git является первым источником истины для инженерной документации. На его основе планируется создать GitHub Pages / Engineering Portal. Позже тот же граф документов должен использоваться Django Control Plane и Knowledge Base.

```text
Git Markdown
   ├── GitHub Repository
   ├── GitHub Pages
   ├── Django Documentation UI
   └── FATHER Knowledge Base
```

Стандарт: [FATHER Documentation Standard](docs/00_Project_Management/DOCUMENTATION_STANDARD.md)  
План портала: [GitHub Pages / Engineering Portal Plan](docs/00_Project_Management/GITHUB_PAGES_PLAN.md)

## Главная идея

FATHER не является одним универсальным чат-ботом. Это производственный контур, который:

1. принимает идею или бизнес-задачу;
2. уточняет требования и ограничения;
3. формирует варианты решения;
4. оценивает сроки, стоимость, риски и ресурсы;
5. проектирует архитектуру и модель безопасности;
6. генерирует проектную документацию;
7. декомпозирует решение на задачи;
8. организует разработку и тестирование;
9. выпускает дочернего агента;
10. сохраняет план/факт, ошибки, решения и результаты в базу знаний.

## Ключевые принципы

- **Security by Construction + Security by Default** — безопасность проектируется одновременно с системой.
- **Evidence over opinion** — существенные решения должны иметь источник, измерение или явное допущение.
- **Minimum Sufficient Architecture** — архитектура должна быть достаточной требованиям, а не максимально сложной.
- **Human Decision Gates** — критические бизнес-, архитектурные и security-решения утверждаются человеком.
- **Plan → Fact → Learning** — каждый проект пополняет инженерную память.
- **Every Project Must Leave an Asset** — каждый проект, исследование или даже отклонённая идея должны оставить повторно используемый интеллектуальный актив.
- **Documentation First, Navigation Always** — каждый значимый блок документируется и включается в навигационный граф.
- **Provider Independence** — LLM и внешние сервисы подключаются через адаптеры; ключи и секреты не хардкодятся.

## Режимы глубины

- `FAST` — небольшие учебные и типовые задачи.
- `STANDARD` — обычные коммерческие проекты.
- `PRO` — расширенный due diligence, сценарный анализ и архитектурная проработка.
- `AUTO` — FATHER сам выбирает необходимую глубину.

Security Screening выполняется всегда. При выявлении критических признаков уровень ИБ автоматически повышается независимо от режима проекта.

## FATHER Delivery Intelligence

В архитектуру включается отдельный контур оценки и проектной разведки:

```text
Project / Technology OSINT
          ↓
Reference Projects & Market Evidence
          ↓
Estimation Engine
          ↓
Time / Cost / Team / TCO / Confidence
          ↓
Staffing & Delivery Planning
          ↓
Plan vs Fact
          ↓
Verified Experience
          ↓
Knowledge Base
```

Контур объединяет Analogous, Parametric, Bottom-Up, PERT, Risk Register, WBS, TCO и накопленную статистику собственных проектов.

Подробнее: [FATHER Delivery Intelligence](docs/03_Architecture/FATHER_DELIVERY_INTELLIGENCE.md)

## Innovation Registry

FATHER сохраняет не только код и документацию, но и продуктовые идеи, исследования и гипотезы. Для этого ведётся отдельный [Innovation Registry](90_Innovation_Registry/README.md) с уровнями зрелости `IRL-0…IRL-9`.

Исследование не списывается как потеря только потому, что заказчик отказался от реализации. Оно должно быть сохранено, переоценено и при возможности превращено в следующий продукт, паттерн, компонент или обучающий материал для FATHER.

## Текущий PoC

Цель первого PoC — провести один небольшой дочерний агент через полный цикл:

```text
IDEA
  ↓
ANALYSIS
  ↓
REQUIREMENTS
  ↓
ARCHITECTURE
  ↓
SECURITY
  ↓
ESTIMATE
  ↓
TEST SPECIFICATION
  ↓
IMPLEMENTATION
  ↓
VERIFICATION
  ↓
CHILD AGENT
  ↓
LESSONS LEARNED
```

Проект развивается как учебный прототип, но архитектурные решения документируются с расчётом на дальнейшее масштабирование и репликацию FATHER под разные предметные области.
