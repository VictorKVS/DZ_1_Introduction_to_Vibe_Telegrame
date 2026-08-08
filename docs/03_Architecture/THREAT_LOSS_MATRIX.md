# FATHER Threat & Loss Matrix v0.1

## Purpose

FATHER evaluates threats primarily through expected economic loss and lost opportunity, not only through abstract severity labels.

A threat is material when it can destroy value, prevent value creation, delay value creation, increase operating cost, create legal/security liability, or consume engineering capacity.

## Core principle

`Loss = Direct Loss + Recovery Cost + Downtime Loss + Lost Revenue + Lost Margin + Delay Cost + Legal/Regulatory Cost + Reputation/Churn Cost + Opportunity Cost`

Money that the organization could reasonably have earned but failed to earn because of a threat, delay, outage, poor decision, rejected release or blocked capability is treated as an economic loss and must be recorded separately from direct cash loss.

## Risk quantification

For each threat scenario FATHER stores:

- asset / business capability;
- threat event;
- vulnerability / cause;
- probability or frequency estimate;
- direct financial loss;
- recovery/remediation cost;
- downtime duration;
- revenue per unit of downtime;
- lost revenue;
- lost gross margin / contribution margin;
- cost of delay;
- customer churn / contract loss estimate;
- SLA/penalties/fines;
- legal/regulatory exposure;
- security incident handling cost;
- opportunity cost;
- secondary/cascade losses;
- confidence interval / uncertainty;
- expected annual loss / expected scenario loss;
- mitigation/control cost;
- residual loss after control;
- avoided loss;
- control ROI / payback.

## Economic risk formulas

### Expected Loss

`Expected Loss = Probability × Impact`

For recurring events:

`Annualized Loss Expectancy (ALE) = Annual Rate of Occurrence × Single Loss Expectancy`

### Lost revenue

`Lost Revenue = Baseline Revenue - Actual Revenue attributable to the event`

When direct attribution is uncertain, store a range and confidence instead of a fabricated point value.

### Downtime loss

`Downtime Loss = Downtime × Revenue/Contribution per time unit + Recovery Cost + SLA/Penalty Cost`

### Cost of Delay

`Cost of Delay = Expected Value not realized during delay + additional delay-induced costs`

### Control economics

`Avoided Loss = Inherent Expected Loss - Residual Expected Loss`

`Control Net Value = Avoided Loss - Control TCO`

`Control ROI = (Avoided Loss - Control TCO) / Control TCO`

## Threat matrix

| Threat | Probability | Direct loss | Lost revenue | Delay loss | Legal/Security loss | Total expected loss | Control cost | Residual loss | Net avoided loss |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Example outage | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

The matrix must support P50/P80 or low/base/high scenarios when uncertainty is material.

## Important distinction

FATHER separates:

1. **cash outflow** — money actually spent or paid;
2. **accounting loss** — recognized financial loss;
3. **lost revenue** — revenue not earned because the event prevented sales/operations;
4. **lost margin** — economically more meaningful than gross revenue in many decisions;
5. **opportunity cost** — value of the best forgone alternative;
6. **risk exposure** — expected loss before the event happens.

The business dashboard may aggregate them into a total economic impact, but source categories remain separate to avoid double counting.

## Integration into the production pipeline

At every gate FATHER asks an economic question:

- Requirements: what business value is at risk if the requirement is omitted or delayed?
- Architecture: what failure modes produce what economic losses?
- Security: what is the expected loss of each threat scenario before/after controls?
- Legal: what revenue, penalties, shutdown or market-access losses can non-compliance cause?
- Development: what is the cost of defect, rework and delay?
- Test: what loss is prevented by detecting this defect before release?
- Deployment: what is the outage/rollback exposure?
- Operations: what actual losses occurred and which assumptions were wrong?

## Link to organizational memory

Every realized threat is compared with its prior estimate:

`ThreatEstimate → Event → ActualLoss → Deviation → Cause → UpdatedModel`

This makes the threat matrix a learning dataset. Over time FATHER must improve estimates of event frequency, downtime, lost revenue, recovery cost and effectiveness of controls.

## Security and banking-style logic

The matrix borrows the useful financial-sector principle that risk must be translated into exposure and expected loss. Severity labels remain useful for triage, but final prioritization should include economic materiality, legal obligations, safety constraints and mandatory security controls.

A low-probability/high-loss scenario may outrank a frequent low-loss event. A mandatory legal/security control may be required even when pure financial ROI appears weak.

## Status

`ACCEPTED — ECONOMIC LOSS IS A PRIMARY RISK METRIC`
