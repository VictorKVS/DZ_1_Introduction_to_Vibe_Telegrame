# LEGACY-001 — Previous Generation Portfolio Analysis

```yaml
document:
  id: LEGACY-001
  title: Previous Generation Portfolio Analysis
  status: ACTIVE
  version: 0.1
  owner_role: father_legacy_intelligence
  parent: docs/20_Legacy_Intelligence/README.md
  related:
    - docs/03_Architecture/README.md
    - 90_Innovation_Registry/README.md
```

## 1. Цель исследования

Провести первый официальный разбор предыдущего поколения проектов и использовать его как испытательный полигон для будущего FATHER Repository Intelligence.

Исследование должно ответить не на вопрос «какой старый проект лучше», а на вопросы:

- какие способности уже проектировались ранее;
- какие архитектурные идеи повторялись;
- что было реально реализовано, а что осталось только в документации;
- какие решения стоит сохранить;
- какие компоненты нужно переписать;
- какие идеи нужно отложить;
- какие ошибки должны стать anti-patterns;
- какие знания можно превратить в шаблоны будущей Product / Software / Agent Factory.

## 2. Исследуемый портфель

### Confirmed repositories

| ID | Repository | Preliminary role | Discovery status |
|---|---|---|---|
| LEG-R01 | `VictorKVS/MindForge` | knowledge + agent platform / early FATHER core | FOUND |
| LEG-R02 | `VictorKVS/Librarian-AI` | knowledge / information processing | FOUND |
| LEG-R03 | `VictorKVS/PRODUCT_SPEC_UniversalAgent` | universal agent product specification | FOUND |
| LEG-R04 | `VictorKVS/mindforge-ai-telegram-bot` | Telegram delivery channel / agent interface | FOUND |
| LEG-R05 | `VictorKVS/AURORA-Intelligence-Platform-` | intelligence / research hypothesis | FOUND, EMPTY AT INITIAL CHECK |
| LEG-R06 | `VictorKVS/AI-Product-Architect` | product / architecture role hypothesis | FOUND |
| LEG-R07 | `VictorKVS/MindForge-Engineer-Profile` | professional profile / specialization | FOUND |
| LEG-R08 | `VictorKVS/mf-std-001-compliance-pack` | standards / compliance | FOUND |
| LEG-R09 | `VictorKVS/mindforge-polygon-framework` | framework / experimentation | FOUND |
| LEG-R10 | OSINT-related repositories and agents | intelligence collection | PARTIALLY FOUND |

### To be located

| Name | Status | Required action |
|---|---|---|
| SOCRATES | NOT FOUND AS SEPARATE REPOSITORY BY NAME | search code, docs, branches and historical repositories |
| ENIGMA | NOT FOUND AS SEPARATE REPOSITORY BY NAME | search code, docs, branches and historical repositories |

Отсутствие отдельного репозитория не означает отсутствие проекта: название могло использоваться внутри MindForge, в документах, ветках, локальных файлах или другом репозитории.

## 3. Что уже подтверждено по MindForge

MindForge декларировал себя как платформу, превращающую сырые данные в структурированные знания и AI-агентов с использованием parsing, embeddings, vector search, knowledge graphs и LLM.

В реальном дереве проекта обнаружены:

- специализированные agent-модули `osint`, `info_security`, `law`, `assets_audit`;
- FastAPI API;
- API v1 endpoints;
- unit и integration tests;
- `pyproject.toml` и инженерные инструменты Python;
- installer/scaffold generator;
- архитектурные draft-файлы разных версий;
- планы LLM provider abstraction;
- планы embeddings providers;
- планы RAG, vector stores и graph evaluation;
- планы Celery/Redis и инфраструктуры;
- changelog и элементы инженерного процесса.

### Preliminary extraction

| Capability | Preliminary decision | Reason |
|---|---|---|
| Specialized agent roles | KEEP / ADAPT | соответствует фабрике специализированных агентов |
| Provider-independent LLM layer | KEEP | базовый принцип нового FATHER |
| API modularity | ADAPT | полезно, но необходимо согласовать с Django Control Plane |
| OSINT Agent | REWRITE | роль нужна, реализация была PoC |
| Knowledge/RAG/vector abstraction | ADAPT | концепция полезна; текущему PoC нужна более простая реализация |
| Graph evaluation | DEFER | сохранить как будущую capability |
| Markdown → scaffold installer | KEEP / EVOLVE | прямой предок Project Generator |
| Unit/integration tests | KEEP / EXPAND | необходимый quality gate |
| Early Kubernetes/Qdrant/Celery everywhere | DEFER | использовать только при доказанной необходимости |
| Repository organization | REWRITE | привести к стандарту FATHER 01–99 и README navigation |

## 4. Ключевая гипотеза

Предыдущие проекты могут оказаться не независимыми программами, а разными попытками реализовать отдельные органы одной будущей системы.

Рабочая гипотеза Capability Map:

```text
MindForge
  → Knowledge / RAG / Agent Core

AURORA
  → Intelligence / Research

SOCRATES
  → Critical Review / Questions / Hypothesis Testing ?

ENIGMA
  → Relationship / Pattern / Analytical Intelligence ?

AI Product Architect
  → Product & Architecture Design

Universal Agent
  → Generic Agent Blueprint

Telegram Bot
  → Delivery Interface

Compliance Pack
  → Governance / Security / Legal Controls
```

Знаки `?` означают неподтверждённую гипотезу. Функции SOCRATES и ENIGMA нельзя фиксировать как факт до анализа исходных материалов.

## 5. Метод анализа каждого проекта

Каждый проект проходит одинаковую карточку:

```yaml
legacy_project:
  identity:
    repository:
    period:
    status:

  intent:
    problem:
    target_user:
    intended_result:

  architecture:
    components: []
    integrations: []
    data_flows: []

  implementation:
    implemented: []
    planned_only: []
    stubs: []

  quality:
    tests:
    documentation:
    maintainability:

  security:
    findings: []
    controls: []

  assets:
    reusable_code: []
    reusable_patterns: []
    knowledge: []
    test_assets: []

  lessons:
    worked: []
    failed: []
    unknown: []

  father_decision:
    keep: []
    adapt: []
    rewrite: []
    defer: []
    reject: []
```

## 6. Capability Map

После анализа отдельных репозиториев строится единая матрица способностей.

Пример целевой формы:

| Capability | MindForge | AURORA | SOCRATES | ENIGMA | Other | FATHER target |
|---|---:|---:|---:|---:|---:|---|
| OSINT / Research | TBD | TBD | TBD | TBD | TBD | Project Intelligence |
| Knowledge ingestion | TBD | TBD | TBD | TBD | TBD | Knowledge Factory |
| Evidence / provenance | TBD | TBD | TBD | TBD | TBD | Evidence Layer |
| Critical review | TBD | TBD | TBD | TBD | TBD | Expert Review Board |
| Agent blueprint | TBD | TBD | TBD | TBD | TBD | Agent Factory |
| LLM routing | TBD | TBD | TBD | TBD | TBD | Provider Adapter Layer |
| Product analysis | TBD | TBD | TBD | TBD | TBD | Product Discovery |
| Estimation | TBD | TBD | TBD | TBD | TBD | Estimation Engine |
| Security | TBD | TBD | TBD | TBD | TBD | Security Plane |
| Testing | TBD | TBD | TBD | TBD | TBD | Evaluation / QA Gates |

`TBD` заменяется только после фактического анализа.

## 7. Репозиторный интеллект как будущая функция FATHER

LEGACY-001 является не просто разовым аудитом. Его процесс должен стать шаблоном будущего `Repository Intelligence Agent`.

```text
Repository URL / Portfolio
        ↓
Inventory
        ↓
Code Map
        ↓
Architecture Reconstruction
        ↓
Dependency Map
        ↓
Security Review
        ↓
Documentation Review
        ↓
Capability Extraction
        ↓
Reuse Decision
        ↓
Migration / Reengineering Plan
        ↓
Estimate
        ↓
Knowledge Assets
```

## 8. Правило интеллектуальной собственности и повторного использования

FATHER должен уметь исследовать внешние open-source проекты, но не превращать анализ в скрытое копирование.

Для внешних проектов обязательны:

- проверка лицензии;
- фиксация происхождения идей и компонентов;
- разделение идеи/паттерна и конкретного кода;
- использование кода только в рамках лицензии;
- предпочтение собственной целевой архитектуры;
- security review до любого reuse.

Для собственных legacy-проектов сохраняется provenance: откуда пришёл компонент, когда и почему он был перенесён.

## 9. Первый ожидаемый результат

LEGACY-001 должен закончиться пятью артефактами:

1. `Legacy Project Inventory`;
2. `Capability Map`;
3. `Reusable Asset Registry`;
4. `Lessons Learned / Anti-pattern Registry`;
5. `Legacy → FATHER Migration Map`.

После этого отдельные полезные решения переходят в Architecture, Innovation Registry, Knowledge Base или backlog реализации.

## 10. Статус v0.1

- MindForge обнаружен и первично разобран;
- подтверждены ранние agent/API/testing/scaffold-подходы;
- AURORA обнаружена как отдельный репозиторий, но при первичной проверке не содержит файлов;
- SOCRATES и ENIGMA по имени отдельных репозиториев не найдены;
- остальные проекты портфеля ожидают последовательного анализа;
- выводы о SOCRATES/ENIGMA пока не считаются фактами.

## Навигация

- ↑ [20 — Legacy Intelligence](README.md)
- ↑ [Documentation Map](../README.md)
- 🏠 [Project Home](../../README.md)
- ↔ [03 — Architecture](../03_Architecture/README.md)
- ↔ [90 — Innovation Registry](../../90_Innovation_Registry/README.md)
