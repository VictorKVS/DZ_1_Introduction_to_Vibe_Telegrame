# LEGACY-002 — Capability & Reuse Map

**Status:** ACTIVE  
**Purpose:** зафиксировать наследуемые идеи, компоненты и архитектурные решения предыдущих поколений MindForge/FATHER и определить, как они используются в новой архитектуре.

## 1. Принцип анализа

Каждый найденный актив получает один из статусов:

- **KEEP** — сохраняется как принцип или компонент почти без изменений;
- **ADAPT** — идея сохраняется, реализация перерабатывается под текущую архитектуру;
- **REWRITE** — ценность подтверждена, старый код не переносится;
- **DEFER** — полезно, но не требуется в текущем MVP;
- **REJECT** — не переносится; причина обязательно фиксируется.

Дополнительно фиксируется происхождение:

- **REMEMBERED** — восстановлено по воспоминаниям и обсуждениям;
- **VERIFIED** — подтверждено кодом или документацией в GitHub;
- **ADOPTED** — официально принято в текущую архитектуру FATHER.

## 2. Карта наследуемых возможностей

| ID | Источник | Возможность | Найденное наследство | Решение | Новый блок FATHER | Причина |
|---|---|---|---|---|---|---|
| LA-001 | `Sokrat` | Multi-model analysis | параллельный запуск GPT / DeepSeek / Qwen | ADAPT | SOCRATES | полезно для сложных решений, но не должно запускаться всегда из-за стоимости |
| LA-002 | `Sokrat` | Research sessions | сессии, раунды исследования, чекпоинты | KEEP | Decision Sessions | необходима воспроизводимость и история решения |
| LA-003 | `Sokrat` | Expert scoring | findings, suggestions, score по экспертам | ADAPT | Expert Council | основа измеримой экспертизы; расширить методологиями и метриками |
| LA-004 | `Sokrat` | Discussion rounds | несколько позиций и последующее обсуждение | ADAPT | SOCRATES | использовать только при конфликте или высокой неопределённости |
| LA-005 | `Sokrat` | Judge / synthesis | модель-судья формирует итог | REWRITE | Decision Synthesizer | нужен синтез с правилами, доказательствами и human gate, а не только LLM-judge |
| LA-006 | `Sokrat` | Decision history | сохранение первичного ответа, экспертиз и финала | KEEP | Decision Ledger | основа будущей оценки «решение → результат» |
| LA-007 | `KNOWLEDGE_MASTER` | Knowledge Graph | знания, связи, веса, версии, доказательства | ADAPT | Knowledge Factory | фундамент организационной памяти |
| LA-008 | `KNOWLEDGE_MASTER` | SPHINX | контроль доказательности и антигаллюцинационный контур | ADAPT | Evidence & Provenance Gate | переопределить как проверку происхождения, доказательности и допустимости вывода |
| LA-009 | `KNOWLEDGE_MASTER` | ENIGMA | логическая валидация и связи | ADAPT | Consistency & Relation Engine | проверка противоречий, зависимостей, причинных и логических связей |
| LA-010 | `KNOWLEDGE_MASTER` | Expert feedback loop | экспертная обратная связь в знания | KEEP | Organizational Learning | обязательный контур после эксплуатации |
| LA-011 | `MindForge-v2.0x` | OSINT Hub | сбор внешних данных по специализированным направлениям | ADAPT | AURORA Intelligence | единый разведывательный слой с профильными коллекторами |
| LA-012 | `MindForge-v2.0x` | ThreatIntel / RegIntel / GeoIntel / SocioIntel | специализированные intelligence-роли | KEEP | AURORA sub-agents | не один монолитный OSINT-агент, а набор специализированных контуров |
| LA-013 | `MindForge-v2.0x` | Telemetry | наблюдаемость, метрики, аудит | KEEP | Telemetry Plane | необходима для оценки качества, стоимости и результата |
| LA-014 | `PRODUCT_SPEC_UniversalAgent` | Capability Registry | бизнес-возможности вместо низкоуровневых API | KEEP | Capability Registry | единый язык между агентами и корпоративными системами |
| LA-015 | `PRODUCT_SPEC_UniversalAgent` | Policy Enforcement | whitelist, risk level, agent identity, audit | KEEP | Policy / Security Plane | ИБ должна действовать до выполнения операции, а не после |
| LA-016 | `PRODUCT_SPEC_UniversalAgent` | Agent-ready gateway | N агентов ↔ M провайдеров | ADAPT | Universal Tool Gateway | уменьшает стоимость повторных интеграций |
| LA-017 | `BotFerm` | YAML project bootstrap | генерация структуры проекта из формального описания | KEEP | Factory Runtime | основа серийного выпуска проектов и агентов |
| LA-018 | `BotFerm` | Agent DNA / validation | формальная спецификация агента и проверка структуры | ADAPT | Expert / Agent Blueprint | расширить ролью, методологиями, метриками, знаниями и инструментами |
| LA-019 | `BotFerm` | DevSecOps-by-default | Bandit, Semgrep, Trivy, CI/CD | KEEP | Secure Production Pipeline | безопасность с начала жизненного цикла |
| LA-020 | `gpt-agent` | Digital organizational roles | декомпозиция функций подразделений на роли | ADAPT | Digital Expert Model | эксперт определяется обязанностями и компетенциями, а не названием LLM |
| LA-021 | `KNOWLEDGE_MASTER/Agent School` | школа специализированных агентов | KnowledgeArchitect, KB Governor, NormGraph Builder, RAG Engineer | ADAPT | Expert Blueprint Library | использовать как шаблоны цифровых специалистов |
| LA-022 | старые проекты в целом | always-on complex architecture | раннее подключение большого числа БД, сервисов, моделей | REJECT for MVP | — | усложняет MVP до появления подтверждённых NFR и нагрузки |
| LA-023 | старые проекты в целом | rich architecture drafts | альтернативные схемы и эволюция архитектуры | KEEP | Architecture Lab | ценны как история решений и источник повторного использования |

## 3. Целевая сборка наследства

```text
AURORA
  external intelligence
       ↓
Knowledge Factory
  facts / sources / history
       ↓
ENIGMA
  relations / consistency / contradictions
       ↓
SOCRATES
  alternatives / expert council / decision
       ↓
SPHINX
  evidence / provenance / policy gate
       ↓
FATHER Factory Runtime
  design / docs / code / tests / deployment
       ↓
Universal Tool Gateway
  safe capabilities and integrations
       ↓
Product / Agent
       ↓
Telemetry + Outcome
       ↓
Organizational Memory
```

## 4. MVP-граница

В текущую вертикаль включаем только минимально достаточный набор:

1. Web + Telegram вход.
2. Django + PostgreSQL как основной каркас.
3. Единая карточка проекта / исследования.
4. AURORA-lite: ограниченный поиск и сбор источников.
5. Три экспертные роли.
6. SOCRATES-lite: независимые оценки, конфликт, синтез, решение.
7. Decision Ledger: причины, альтернативы, доказательства, confidence, стоимость.
8. Knowledge Base + pgvector.
9. Blueprint проекта / агента.
10. Генерация одного дочернего агента.
11. Тестирование и ИБ-контроль до публикации.
12. Plan/Fact и Outcome после эксплуатации.

Neo4j, Kubernetes, множество vector DB, постоянно работающий много-модельный совет и другие тяжёлые компоненты подключаются только при подтверждённой необходимости.

## 5. Критерий переноса старого компонента

Старый актив не переносится только потому, что он уже написан. Для принятия требуется ответить:

- какую проблему он решает;
- используется ли эта проблема в текущем сценарии;
- есть ли более простое решение;
- каков риск ИБ;
- сколько стоит эксплуатация;
- как измеряется польза;
- существует ли тест, подтверждающий результат;
- можно ли заменить компонент без разрушения архитектуры.

## 6. Связь с журналом разработки

Каждое изменение статуса `KEEP / ADAPT / REWRITE / DEFER / REJECT`, включение актива в MVP или отказ от него фиксируется в:

`docs/00_Project_Management/DEVELOPMENT_LOG.md`

с обязательным указанием **что изменили, почему, на основании чего и как проверим результат**.
