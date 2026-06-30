// docs/ARCHITECTURE_OVERVIEW.md

1. Architecture Overview – System goals, guiding principles, and high-level pipeline.
2. Domain Model – Define every core object (Game, Market, Odds, Bet, Ticket, Portfolio, etc.) and their relationships.
3. Engine Responsibilities – Clearly document what each engine owns and, just as importantly, what it does not own.
4. Data Flow – Trace information from ingestion all the way through recommendation, settlement, and model feedback.
5. Directory-to-Responsibility Mapping – Explain what belongs in each folder so future code has a clear home.
6. Research Roadmap – List the first prediction strategies, feature ideas, and experiments you want to test.
7. Implementation Milestones – Break the build into small, testable phases with success criteria.

# Sportsbook Engine Architecture Overview

## Vision

Sportsbook Engine is a quantitative sports betting research platform inspired by algorithmic trading systems.

Instead of attempting to predict individual winners, the platform estimates outcome probabilities, identifies positive expected value (+EV) opportunities, constructs risk-aware betting portfolios, and manages bankroll growth through disciplined, data-driven decision making.

The objective is not to maximize the payout of individual tickets, but to maximize long-term expected bankroll growth while controlling risk and drawdowns.

---

# Guiding Principles

## Probability First

The engine never predicts "win" or "lose."

Every market is evaluated as a probability distribution.

Example:

Market

LeBron James Over 24.5 Points

↓

Estimated Probability

61.8%

Everything downstream operates from probabilities rather than binary predictions.

---

## Expected Value Over Win Rate

High win percentage alone is not a goal.

Every recommendation must demonstrate positive expected value relative to the sportsbook's implied probability.

The objective is to consistently identify situations where the estimated probability exceeds the market's implied probability.

---

## Portfolio Thinking

Individual bets are not optimized independently.

Recommendations are generated as portfolios of wagers that balance:

- Expected value
- Correlation
- Variance
- Daily exposure
- Bankroll risk

The optimizer seeks long-term growth rather than maximizing short-term payout.

---

## Risk Management

Risk management is treated as a first-class system.

The engine determines:

- Position sizing
- Maximum daily exposure
- Maximum portfolio exposure
- Drawdown limits
- Stake allocation

No recommendation bypasses the bankroll management system.

---

## Modular Architecture

Every major subsystem owns exactly one responsibility.

Modules communicate through well-defined interfaces.

Prediction models can be replaced without changing portfolio construction.

Data providers can be replaced without affecting feature engineering.

Optimization algorithms can evolve independently from prediction models.

---

## Deterministic Pipeline

Given identical historical inputs and model versions, the engine should produce identical recommendations.

This property enables:

- Reliable backtesting
- Reproducible experiments
- Model comparison
- Strategy validation

---

# High-Level Pipeline

Raw Sports Data

↓

Data Collection

↓

Canonical Sports Database

↓

Feature Engineering

↓

Probability Models

↓

Expected Value Engine

↓

Portfolio Optimizer

↓

Bankroll Manager

↓

Ticket Recommendations

↓

Settlement

↓

Analytics

↓

Model Improvement

---

# System Goals

The platform should:

- Collect and normalize sports, player, and betting market data.
- Estimate probabilities for available betting markets.
- Measure expected value relative to sportsbook odds.
- Construct optimal betting portfolios.
- Allocate stake sizes according to bankroll management rules.
- Backtest strategies over historical data.
- Measure long-term performance.
- Continuously improve prediction quality.

---

# Non-Goals

The platform is not intended to:

- Guarantee profitable betting.
- Chase high-payout lottery parlays.
- Recommend wagers without quantitative justification.
- Optimize for win percentage alone.
- Replace disciplined bankroll management with intuition.

---

# Core Architectural Layers

## Data Layer

Responsible for collecting, normalizing, validating, and storing all external data.

Owns:

- Games
- Teams
- Players
- Odds
- Results
- Historical statistics

Does not perform predictions.

---

## Feature Layer

Transforms raw data into predictive features.

Examples:

- Rolling averages
- Rest days
- Injury indicators
- Pace metrics
- Weather
- Travel
- Line movement

Does not make betting decisions.

---

## Prediction Layer

Consumes engineered features and produces calibrated probability estimates.

Responsible only for probability estimation.

---

## Value Layer

Combines:

- Model probabilities
- Sportsbook odds

to produce:

- Expected value
- Edge
- Confidence

Only positive expected value opportunities progress to optimization.

---

## Portfolio Layer

Constructs betting tickets from candidate wagers.

Responsible for:

- Correlation reduction
- Ticket construction
- Exposure balancing
- Risk-adjusted optimization

---

## Bankroll Layer

Determines position sizing and capital allocation.

Responsible for:

- Stake sizing
- Daily risk limits
- Drawdown controls
- Growth optimization

---

## Analytics Layer

Measures system performance.

Tracks:

- ROI
- Closing Line Value
- Calibration
- Drawdown
- Profit Factor
- Win Rate
- Sharpe-like metrics
- Model performance over time

---

# Artificial Intelligence

Artificial intelligence is one component of the platform rather than the platform itself.

AI is primarily responsible for:

- Probability estimation
- Pattern discovery
- Feature importance
- Model calibration

Portfolio construction, bankroll management, and analytics remain deterministic systems that operate on model outputs.

---

# Engineering Philosophy

The Sportsbook Engine is designed as a quantitative research platform.

Its architecture emphasizes:

- Reproducibility
- Modularity
- Explainability
- Testability
- Separation of concerns
- Continuous experimentation

The objective is to create a system that can evolve through research while maintaining stable engineering foundations.

## Canonical State

Every piece of information in the system has a single authoritative owner.

Derived values are computed rather than duplicated.

Examples:

- Odds are owned by the Market Data layer.
- Predictions are owned by the Prediction Engine.
- Expected Value is owned by the Value Engine.
- Stake sizing is owned by the Bankroll Engine.

No subsystem mutates another subsystem's canonical state.

## Orthogonal Data Adaptation

External data providers are considered implementation details rather than business logic.

The Sportsbook Engine operates on canonical domain objects that are independent of any individual API.

Every external provider is responsible for adapting its own schema into the engine's canonical model.

Example:

DraftKings API
        │
FanDuel API
        │
Odds API
        │
        ▼
Canonical Market
Canonical Odds
Canonical Game

The remainder of the system never depends on provider-specific schemas.