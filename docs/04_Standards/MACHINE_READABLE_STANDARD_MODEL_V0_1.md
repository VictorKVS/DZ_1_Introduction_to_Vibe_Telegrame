# Machine-Readable Standard Model v0.1

> Формальная модель исполняемых инженерных стандартов FATHER.

[← Standards Library](README.md)

## Цель

Перевести стандарты из Markdown-документов в машинно-читаемые объекты, которые FATHER сможет применять к проекту, проверять автоматически, связывать с evidence и использовать в Gate-процессах.

## Базовые сущности

### StandardDefinition
Описывает внутренний или внешний стандарт.

Минимальные поля:
- `standard_id`;
- `title`;
- `version`;
- `status`;
- `scope`;
- `owner_role`;
- `applicability_rules`;
- `required_artifacts`;
- `controls`;
- `gates`;
- `metrics`;
- `evidence_requirements`;
- `references`;
- `change_history`.

### ControlDefinition
Одна проверяемая обязанность стандарта.

Поля:
- `control_id`;
- `title`;
- `stage`;
- `mandatory`;
- `requirement`;
- `verification_method`;
- `pass_criteria`;
- `fail_severity`;
- `evidence_type`;
- `automation_level`;
- `human_gate_required`.

### GateDefinition
Набор контролей, который должен быть выполнен перед переходом между стадиями.

Поля:
- `gate_id`;
- `gate_type`: `QUALITY | SECURITY | LEGAL | ECONOMIC | COMPOSITE`;
- `stage`;
- `required_controls`;
- `pass_policy`;
- `exception_policy`;
- `approver_role`.

### MetricDefinition
Метрика, по которой измеряется соблюдение стандарта и его полезность.

Примеры:
- defect escape rate;
- requirement coverage;
- security findings by severity;
- expected loss;
- cost variance;
- lead time;
- rework ratio;
- evidence coverage.

### StandardProfile
Набор стандартов, применимых к конкретному проекту.

Формируется из:
- базового профиля FATHER;
- отраслевого профиля;
- Security Profile;
- Jurisdiction Profile;
- Customer Profile;
- Contract Profile.

### ComplianceRecord
Факт применения стандарта к конкретному объекту проекта.

Хранит:
- standard/control/gate;
- project;
- artifact;
- status;
- evidence;
- findings;
- reviewer;
- timestamp;
- exception/waiver;
- remediation;
- recheck date.

## Жизненный цикл

```text
StandardDefinition
      ↓
StandardProfile
      ↓
Project / Artifact / Stage
      ↓
Applicable Controls
      ↓
GateRun
      ↓
PASS / FAIL / WAIVER / NOT_APPLICABLE
      ↓
ComplianceRecord
      ↓
Metrics / Findings / Outcome
      ↓
Standard Review
```

## Статусы

Для стандарта:
`DRAFT → REVIEW → ACTIVE → REVISED → DEPRECATED`.

Для контроля:
`NOT_EVALUATED | PASS | FAIL | WAIVED | NOT_APPLICABLE`.

Для Gate:
`PENDING | RUNNING | PASSED | FAILED | BLOCKED | APPROVED_WITH_EXCEPTION`.

## Правило исключения

`FAIL` не превращается в `PASS` автоматически. Исключение оформляется как отдельный `Waiver/Exception Record` с:
- причиной;
- владельцем риска;
- сроком действия;
- компенсирующими мерами;
- экономическим и security impact;
- обязательной датой пересмотра.

## Связь с графом знаний

Минимальные отношения:

```text
StandardDefinition --requires--> ControlDefinition
ControlDefinition --verified_by--> TestCase / Review
ControlDefinition --applies_to--> Requirement / Architecture / CodeArtifact / InfrastructureComponent
GateDefinition --contains--> ControlDefinition
ComplianceRecord --evidenced_by--> Evidence
Finding --violates--> ControlDefinition
Remediation --resolves--> Finding
Outcome --validates_effectiveness_of--> ControlDefinition
```

## Django mapping

Планируемые модели:
- `StandardDefinition`;
- `ControlDefinition`;
- `GateDefinition`;
- `MetricDefinition`;
- `StandardProfile`;
- `ProfileStandard`;
- `ComplianceRecord`;
- `GateRun`;
- `GateCheckResult`;
- `Finding`;
- `Waiver`;
- `RemediationAction`.

## MVP

Первая машинно-читаемая реализация должна поддержать один стандарт целиком: `STD-006 Security Engineering`.

Минимальный сценарий:

`Project → Security Standard Profile → controls for current stage → GateRun → findings/evidence → PASS/FAIL → stored ComplianceRecord`.

## Gate готовности

Модель считается практически применимой, если FATHER может без ручного чтения Markdown определить:
1. какие проверки обязательны на текущей стадии;
2. какие evidence нужны;
3. кто должен подтвердить Human Gate;
4. можно ли переходить к следующей стадии;
5. что именно нарушено при FAIL.
