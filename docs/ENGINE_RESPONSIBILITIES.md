// docs/ENGINE_RESPONSIBILITIES.md

# Engine Responsibilities

## Purpose

The Sportsbook Engine is composed of independent engines.

Each engine owns a single area of responsibility and exposes a well-defined interface to the rest of the system.

An engine may consume information from other engines, but it must never assume ownership of another engine's canonical state.

The goal is to maintain:

- Single responsibility
- Clear ownership
- Low coupling
- High cohesion
- Replaceable implementations
- Deterministic behavior

---

# Ownership Principles

## Single Ownership

Every piece of information has exactly one canonical owner.

Examples

| Data | Owner |
|-------|-------|
| Games | Data Engine |
| Markets | Data Engine |
| Odds | Data Engine |
| Features | Feature Engine |
| Predictions | Prediction Engine |
| Expected Value | Value Engine |
| Recommended Tickets | Portfolio Engine |
| Stake Size | Bankroll Engine |
| Performance Metrics | Analytics Engine |

No engine duplicates or mutates another engine's canonical state.

---

## Derived State

Whenever possible, information should be derived rather than duplicated.

Examples

Expected Value is derived from:

- Odds
- Predictions

Portfolio Exposure is derived from:

- Active Tickets
- Bankroll

Recommendation Scores are derived from:

- Expected Value
- Correlation
- Risk

---

## Orthogonal Data Adaptation

External providers are implementation details.

Every provider adapts into the canonical domain model before entering the system.

```
DraftKings API
FanDuel API
Odds API
ESPN
Weather API

        │

        ▼

Provider Adapter

        │

        ▼

Canonical Domain Objects
```

Business logic never imports provider-specific models.

---

# Engine Overview

```
Data Engine

↓

Feature Engine

↓

Prediction Engine

↓

Value Engine

↓

Portfolio Engine

↓

Bankroll Engine

↓

Execution Engine

↓

Analytics Engine
```

Each engine owns exactly one stage of the pipeline.

---

# Data Engine

## Purpose

Collect, validate, normalize, and store external data.

The Data Engine is responsible for converting external provider schemas into canonical domain objects.

---

## Owns

✓ API clients

✓ Provider adapters

✓ Authentication

✓ Rate limiting

✓ Retry logic

✓ Validation

✓ Normalization

✓ Canonical conversion

✓ Historical storage

✓ Data synchronization

✓ Data quality monitoring

---

## Does NOT Own

✗ Feature engineering

✗ Predictions

✗ Expected value

✗ Portfolio optimization

✗ Stake sizing

✗ Recommendation logic

---

## Produces

- Events
- Teams
- Players
- Markets
- Selections
- Odds
- Results

---

# Feature Engine

## Purpose

Transform canonical data into predictive features.

Features are reusable inputs for prediction models.

---

## Owns

✓ Feature generation

✓ Rolling statistics

✓ Derived metrics

✓ Historical windows

✓ Feature versioning

✓ Feature validation

---

## Does NOT Own

✗ Data ingestion

✗ Predictions

✗ Expected value

✗ Portfolio construction

✗ Stake sizing

---

## Produces

Examples

- Rolling averages
- Usage rates
- Injury indicators
- Rest days
- Home/Away
- Pace
- Travel
- Weather features
- Line movement metrics

---

# Prediction Engine

## Purpose

Estimate probabilities for betting selections.

The Prediction Engine predicts probabilities—not betting decisions.

---

## Owns

✓ Model inference

✓ Probability estimation

✓ Confidence estimation

✓ Calibration

✓ Model versioning

✓ Ensemble logic

---

## Does NOT Own

✗ Odds

✗ Expected value

✗ Portfolio optimization

✗ Stake sizing

✗ Bet recommendations

---

## Produces

- Probability estimates
- Confidence scores
- Model metadata

---

# Value Engine

## Purpose

Determine whether a betting opportunity has positive expected value.

This engine combines model predictions with sportsbook odds.

---

## Owns

✓ Implied probability

✓ Expected value calculations

✓ Edge calculations

✓ Candidate evaluation

✓ Value ranking

---

## Does NOT Own

✗ Predictions

✗ Portfolio optimization

✗ Stake sizing

✗ Execution

---

## Produces

- Expected value
- Edge
- Candidate opportunities

---

# Portfolio Engine

## Purpose

Construct betting portfolios from candidate opportunities.

The objective is to maximize long-term expected growth while managing correlation and exposure.

---

## Owns

✓ Ticket construction

✓ Bet selection

✓ Correlation analysis

✓ Diversification

✓ Ticket ranking

✓ Exposure balancing

---

## Does NOT Own

✗ Predictions

✗ Stake sizing

✗ Bankroll management

✗ Execution

---

## Produces

- Recommended tickets
- Portfolio allocation
- Exposure analysis

---

# Bankroll Engine

## Purpose

Determine capital allocation.

The Bankroll Engine decides how much to wager—not what to wager.

---

## Owns

✓ Stake sizing

✓ Risk budgeting

✓ Kelly calculations

✓ Maximum exposure

✓ Daily limits

✓ Drawdown protection

✓ Capital allocation

---

## Does NOT Own

✗ Predictions

✗ Expected value

✗ Ticket construction

✗ Analytics

---

## Produces

- Stake recommendations
- Exposure limits
- Capital allocation

---

# Execution Engine

## Purpose

Manage the lifecycle of wagers.

Execution is responsible for recording, tracking, and settling bets.

---

## Owns

✓ Ticket creation

✓ Bet lifecycle

✓ Bet status

✓ Settlement

✓ Portfolio updates

✓ Bankroll updates

---

## Does NOT Own

✗ Predictions

✗ Optimization

✗ Analytics

---

## Produces

- Executed bets
- Settlements
- Updated bankroll
- Portfolio state

---

# Analytics Engine

## Purpose

Measure performance and generate research insights.

Analytics never influences live recommendations directly.

Its role is measurement.

---

## Owns

✓ ROI

✓ Closing Line Value

✓ Drawdown

✓ Profit factor

✓ Calibration metrics

✓ Win rate

✓ Historical reporting

✓ Model evaluation

✓ Experiment comparison

---

## Does NOT Own

✗ Predictions

✗ Optimization

✗ Stake sizing

✗ Execution

---

## Produces

- Performance reports
- Historical metrics
- Research datasets
- Experiment results

---

# Research Engine

## Purpose

Develop and validate new strategies before production deployment.

The Research Engine is intentionally isolated from production systems.

---

## Owns

✓ Feature experiments

✓ Model training

✓ Hyperparameter tuning

✓ Strategy comparison

✓ Backtesting

✓ Walk-forward validation

---

## Does NOT Own

✗ Live recommendations

✗ Production bankroll

✗ Execution

---

## Produces

- Candidate models
- Research reports
- Experimental features
- Validated strategies

---

# Engine Dependency Rules

```
Data Engine
        │
        ▼
Feature Engine
        │
        ▼
Prediction Engine
        │
        ▼
Value Engine
        │
        ▼
Portfolio Engine
        │
        ▼
Bankroll Engine
        │
        ▼
Execution Engine
        │
        ▼
Analytics Engine
```

Information flows downward.

Lower engines may consume outputs from higher engines.

Higher engines never depend on lower engines.

---

# Dependency Principles

An engine may depend only on:

- Canonical domain models
- Public interfaces exposed by upstream engines

An engine must never:

- Mutate another engine's state
- Import provider-specific models
- Bypass engine boundaries
- Duplicate canonical ownership

---

# Architectural Goal

The Sportsbook Engine is designed so that every engine can be replaced independently.

Examples:

- Replace the prediction model without modifying portfolio optimization.
- Replace the bankroll algorithm without affecting execution.
- Add a new sportsbook without changing business logic.
- Swap data providers without changing downstream engines.

By maintaining strict ownership boundaries and canonical interfaces, the platform remains modular, testable, and extensible as research and production capabilities evolve.