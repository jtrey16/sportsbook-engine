// docs/EVENT_MODEL.md

# Event Model

## Purpose

The Event Model defines how information moves between engines inside the Sportsbook Engine.

Instead of tightly coupling engines together through direct method calls, the platform communicates using immutable domain events.

Events represent facts.

They are never modified after creation.

Every engine consumes events, performs its own responsibility, and publishes new events.

This architecture provides:

- Loose coupling
- Replayability
- Auditability
- Deterministic behavior
- Easier testing
- Clear ownership

---

# Event Philosophy

Events describe facts that have already occurred.

Good event names

```

ODDS_UPDATED

PREDICTION_GENERATED

BET_SETTLED

```

Bad event names

```

UPDATE_ODDS

CALCULATE_PROBABILITY

GENERATE_TICKET

```

Commands tell something to happen.

Events describe what happened.

The Sportsbook Engine communicates primarily through events.

---

# Event Lifecycle

```

External Provider

↓

ODDS_UPDATED

↓

FEATURES_UPDATED

↓

PREDICTION_GENERATED

↓

EXPECTED_VALUE_UPDATED

↓

PORTFOLIO_UPDATED

↓

BET_RECOMMENDED

↓

BET_EXECUTED

↓

BET_SETTLED

↓

BANKROLL_UPDATED

↓

ANALYTICS_UPDATED

↓

MODEL_EVALUATED

```

Every engine reacts to events produced by previous engines.

---

# Event Structure

Every event shares a common structure.

```python
Event

event_id

event_type

timestamp

source

version

payload
```

Example

```python
{
    "event_id": "...",
    "event_type": "ODDS_UPDATED",
    "timestamp": "...",
    "source": "DraftKings",
    "version": 1,
    "payload": { ... }
}
```

---

# Event Categories

## Data Events

Produced by the Data Engine.

Examples

```
EVENT_CREATED

EVENT_UPDATED

TEAM_UPDATED

PLAYER_UPDATED

MARKET_CREATED

SELECTION_CREATED

ODDS_UPDATED

RESULT_POSTED
```

---

## Feature Events

Produced by the Feature Engine.

Examples

```
FEATURES_UPDATED

FEATURE_VECTOR_CREATED

FEATURE_VECTOR_UPDATED
```

---

## Prediction Events

Produced by the Prediction Engine.

Examples

```
PREDICTION_GENERATED

PREDICTION_UPDATED

MODEL_CHANGED

MODEL_CALIBRATED
```

---

## Value Events

Produced by the Value Engine.

Examples

```
EXPECTED_VALUE_UPDATED

EDGE_UPDATED

CANDIDATE_CREATED

CANDIDATE_REMOVED
```

---

## Portfolio Events

Produced by the Portfolio Engine.

Examples

```
PORTFOLIO_UPDATED

TICKET_CREATED

TICKET_UPDATED

TICKET_REMOVED

BET_RECOMMENDED
```

---

## Bankroll Events

Produced by the Bankroll Engine.

Examples

```
BANKROLL_UPDATED

STAKE_CALCULATED

RISK_LIMIT_UPDATED

EXPOSURE_UPDATED
```

---

## Execution Events

Produced by the Execution Engine.

Examples

```
BET_PLACED

BET_UPDATED

BET_CANCELLED

BET_SETTLED

TICKET_SETTLED
```

---

## Analytics Events

Produced by the Analytics Engine.

Examples

```
ROI_UPDATED

CLV_UPDATED

PERFORMANCE_UPDATED

ANALYTICS_UPDATED
```

---

## Research Events

Produced by the Research Engine.

Examples

```
MODEL_TRAINED

MODEL_VALIDATED

MODEL_PROMOTED

EXPERIMENT_COMPLETED

BACKTEST_COMPLETED
```

---

# Engine Communication

```
Data Engine

↓

ODDS_UPDATED

↓

Feature Engine

↓

FEATURES_UPDATED

↓

Prediction Engine

↓

PREDICTION_GENERATED

↓

Value Engine

↓

EXPECTED_VALUE_UPDATED

↓

Portfolio Engine

↓

BET_RECOMMENDED

↓

Bankroll Engine

↓

STAKE_CALCULATED

↓

Execution Engine

↓

BET_PLACED

↓

Settlement

↓

BET_SETTLED

↓

Analytics

↓

PERFORMANCE_UPDATED

↓

Research

↓

MODEL_PROMOTED
```

No engine directly modifies another engine.

Only events move information.

---

# Event Immutability

Events are immutable.

Once published, an event can never change.

Incorrect

```
ODDS_UPDATED

↓

modify event

↓

reuse event
```

Correct

```
ODDS_UPDATED

↓

new odds arrive

↓

ODDS_UPDATED
```

Each event represents one historical fact.

---

# Event Replay

One major advantage of the event model is replay.

Historical events can rebuild system state.

```
Historical Events

↓

Replay Engine

↓

Reconstructed State
```

Replay enables

- Backtesting
- Debugging
- Auditing
- Model evaluation
- Historical simulations

---

# Event Ordering

Events must always be processed in chronological order.

Example

```
ODDS_UPDATED

↓

FEATURES_UPDATED

↓

PREDICTION_GENERATED

↓

EXPECTED_VALUE_UPDATED
```

A Prediction must never be generated before the Features that produced it.

---

# Event Ownership

Each event has exactly one producer.

Examples

| Event | Producer |
|--------|----------|
| ODDS_UPDATED | Data Engine |
| FEATURES_UPDATED | Feature Engine |
| PREDICTION_GENERATED | Prediction Engine |
| EXPECTED_VALUE_UPDATED | Value Engine |
| BET_RECOMMENDED | Portfolio Engine |
| STAKE_CALCULATED | Bankroll Engine |
| BET_PLACED | Execution Engine |
| BET_SETTLED | Execution Engine |
| BANKROLL_UPDATED | Execution Engine |
| ANALYTICS_UPDATED | Analytics Engine |
| MODEL_PROMOTED | Research Engine |

Consumers may react to events.

Consumers never rewrite them.

---

# Event Payloads

Events contain only the information necessary for downstream engines.

Example

```
ODDS_UPDATED

payload

selection_id

sportsbook

price

timestamp
```

Example

```
PREDICTION_GENERATED

payload

selection_id

probability

confidence

model_version
```

Payloads should reference canonical domain objects whenever possible.

---

# Event Versioning

Events are versioned.

```
ODDS_UPDATED

Version 1
```

If the schema changes

```
ODDS_UPDATED

Version 2
```

Older events remain replayable.

---

# Architectural Rules

Events must

✓ Describe facts

✓ Be immutable

✓ Have exactly one producer

✓ Be replayable

✓ Reference canonical domain objects

✓ Be versioned

✓ Be timestamped

Events must never

✗ Contain provider-specific models

✗ Be modified after publication

✗ Contain business logic

✗ Skip ownership boundaries

✗ Depend on downstream engines

---

# Long-Term Vision

The Sportsbook Engine is designed as an event-driven quantitative research platform.

Every recommendation, settlement, bankroll update, model evaluation, and research experiment can be reconstructed entirely from the event history.

This enables deterministic replay, reproducible backtesting, complete auditability, and continuous model improvement while maintaining strict ownership boundaries between engines.


One change I would make compared to HLQE

There's one thing I would improve over what we learned from HLQE.

I would introduce two distinct categories of events:

1. Market Events (immutable facts)
ODDS_UPDATED
PLAYER_STATUS_UPDATED
EVENT_STARTED
RESULT_POSTED
WEATHER_UPDATED

These come from the outside world.

2. System Events (decisions made by the engine)
PREDICTION_GENERATED
EXPECTED_VALUE_UPDATED
TICKET_CREATED
STAKE_CALCULATED
MODEL_PROMOTED

These are produced internally.

That distinction becomes incredibly useful when replaying or debugging because you can answer questions like:

Did the outside world change? (Market Event)
Or did our system make a different decision with the same inputs? (System Event)

I think that separation will make this architecture even cleaner than HLQE's and will be invaluable as you begin backtesting, comparing model versions, and diagnosing why recommendations changed over time.