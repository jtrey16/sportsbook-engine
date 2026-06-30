// docs/DATA_FLOW.md

# Data Flow

## Purpose

The Data Flow document describes how information moves through the Sportsbook Engine from external data sources to final recommendations, settlement, analytics, and continuous model improvement.

Unlike the Domain Model, which defines **what exists**, and the Engine Responsibilities document, which defines **who owns what**, this document defines **how information moves** throughout the platform.

The data flow is intentionally unidirectional.

Information always moves forward through the system.

---

# Guiding Principles

## Canonical First

Every external provider is normalized into canonical domain objects before entering the platform.

No downstream engine is aware of provider-specific schemas.

```
DraftKings

↓

DraftKings Adapter

↓

Canonical Odds
```

The rest of the engine only understands canonical objects.

---

## Orthogonal Data Adaptation

Every provider is responsible for adapting itself into the canonical domain model.

```
DraftKings API

FanDuel API

Odds API

ESPN

League APIs

Weather API

News API

            │

            ▼

Provider Adapters

            │

            ▼

Canonical Domain Objects
```

Business logic never imports provider-specific models.

---

## One-Way Information Flow

The platform operates as a pipeline.

```
External Data

↓

Canonical Data

↓

Features

↓

Predictions

↓

Expected Value

↓

Portfolio

↓

Bankroll

↓

Execution

↓

Settlement

↓

Analytics

↓

Research
```

Information flows forward.

Engines never reach backward to modify upstream state.

---

# Complete System Flow

```
External Providers

        │

        ▼

Data Engine

        │

        ▼

Canonical Domain Objects

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

Settlement

        │

        ▼

Analytics Engine

        │

        ▼

Research Engine

        │

        ▼

Model Improvements
```

---

# Stage 1 — Data Ingestion

## Inputs

Examples

- Sportsbooks
- Odds providers
- League APIs
- Statistics providers
- Injury reports
- Weather
- News
- Historical databases

Example

```
DraftKings API

↓

DraftKings Adapter

↓

Canonical Odds
```

Responsibilities

- Download
- Validate
- Normalize
- Convert
- Store

Output

Canonical domain objects.

---

# Stage 2 — Canonical Domain

The Data Engine produces canonical business objects.

Examples

```
League

Season

Event

Team

Player

Market

Selection

Odds
```

Everything downstream consumes these objects.

Nothing downstream knows where they originated.

---

# Stage 3 — Feature Engineering

The Feature Engine transforms domain objects into predictive features.

Examples

```
Player Game Logs

↓

Rolling Average

↓

Opponent Rank

↓

Rest Days

↓

Travel

↓

Minutes Trend

↓

Usage Rate

↓

Weather

↓

Line Movement
```

Output

Feature vectors.

---

# Stage 4 — Prediction

The Prediction Engine estimates probabilities.

Input

Feature vectors.

Output

```
Selection

↓

Probability

↓

Confidence

↓

Model Version
```

The Prediction Engine does not know:

- sportsbook
- ticket
- bankroll
- optimization

It predicts probabilities only.

---

# Stage 5 — Expected Value

The Value Engine combines:

```
Prediction

+

Odds

↓

Expected Value

↓

Edge

↓

Candidate Opportunity
```

Only positive expected value opportunities continue.

---

# Stage 6 — Portfolio Construction

The Portfolio Engine evaluates candidate opportunities.

Objectives

- Reduce correlation
- Diversify exposure
- Maximize expected return
- Control variance
- Build tickets

Output

Recommended tickets.

---

# Stage 7 — Bankroll Allocation

The Bankroll Engine determines:

```
Current Bankroll

↓

Risk Budget

↓

Stake Size

↓

Daily Exposure

↓

Recommended Allocation
```

The Bankroll Engine never changes recommendations.

It determines capital allocation only.

---

# Stage 8 — Execution

Execution records the recommendation as a wager.

Execution manages:

- ticket lifecycle
- bet lifecycle
- status
- timestamps

Output

Executed bets.

---

# Stage 9 — Settlement

When events complete:

```
Event Result

↓

Bet Settlement

↓

Ticket Settlement

↓

Portfolio Update

↓

Bankroll Update
```

Possible outcomes

- Won
- Lost
- Push
- Void
- Cancelled

---

# Stage 10 — Analytics

Analytics measures system performance.

Metrics include

- ROI
- Win Rate
- Closing Line Value
- Drawdown
- Profit Factor
- Calibration
- Exposure
- Edge Realization

Analytics never changes live recommendations.

Its purpose is measurement.

---

# Stage 11 — Research

Research consumes historical analytics.

Examples

```
Historical Bets

↓

Model Evaluation

↓

Feature Importance

↓

Calibration

↓

Retraining

↓

Model Promotion
```

The Research Engine develops future models.

It never participates in live recommendations.

---

# Feedback Loop

The Sportsbook Engine continuously improves over time.

```
Historical Results

↓

Analytics

↓

Research

↓

Improved Models

↓

Prediction Engine

↓

Future Recommendations
```

The feedback loop improves prediction quality while preserving deterministic execution.

---

# Information Ownership

| Information | Owner |
|-------------|-------|
| Games | Data Engine |
| Teams | Data Engine |
| Players | Data Engine |
| Markets | Data Engine |
| Odds | Data Engine |
| Features | Feature Engine |
| Predictions | Prediction Engine |
| Expected Value | Value Engine |
| Candidate Opportunities | Value Engine |
| Tickets | Portfolio Engine |
| Stake Size | Bankroll Engine |
| Executed Bets | Execution Engine |
| Settlements | Execution Engine |
| Performance Metrics | Analytics Engine |
| Experiments | Research Engine |

---

# Architectural Guarantees

The data pipeline guarantees:

- Every engine communicates using canonical domain objects.
- Information moves in one direction.
- Engines own exactly one responsibility.
- Upstream state is never mutated by downstream engines.
- Every recommendation is reproducible given the same inputs and model version.
- External provider changes are isolated within the Data Engine.

These guarantees make the platform deterministic, modular, testable, and extensible.