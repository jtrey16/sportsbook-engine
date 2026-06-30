// docs/DIRECTORY_TO_RESPONSIBILITY_MAPPING.md

# Directory-to-Responsibility Mapping

## Purpose

This document defines the responsibility of every directory within the Sportsbook Engine.

Every file should have one obvious home.

If new functionality does not clearly belong in an existing directory, the architecture should be reconsidered before creating a new location.

The objective is to maintain:

- Clear ownership
- High cohesion
- Low coupling
- Discoverable code
- Predictable project organization

---

# Guiding Principles

## Single Responsibility

Every directory owns one area of responsibility.

Directories should not overlap.

---

## Business Before Technology

Directories represent business capabilities rather than implementation details.

Good

```

bankroll/
portfolio/
analytics/

```

Poor

```

helpers/
utils2/
misc/

```

---

## Canonical Flow

The repository follows the system pipeline.

```

Data

↓

Features

↓

Models

↓

Optimization

↓

Bankroll

↓

Execution

↓

Analytics

↓

Research

```

The folder structure mirrors the architecture.

---

# Repository Layout

```

sportsbook-engine/

├── sportsbook/
├── data/
├── docs/
├── notebooks/
├── scripts/
├── tests/

```

---

# sportsbook/

Contains all production source code.

Nothing outside this directory should contain business logic.

```

sportsbook/

```

---

# sportsbook/data/

## Purpose

Responsible for external data acquisition and normalization.

Owns

- API clients
- Provider adapters
- Authentication
- Rate limiting
- Validation
- Canonical conversion
- Data synchronization

Examples

```

draftkings/

fanduel/

espn/

odds_api/

providers/

adapters/

normalization/

validation/

```

Does NOT contain

- Features
- AI models
- Optimization
- Analytics

---

# sportsbook/features/

## Purpose

Transforms canonical domain objects into predictive features.

Owns

- Rolling statistics
- Feature generation
- Derived metrics
- Feature validation
- Feature versioning

Examples

```

rolling_average.py

injury_features.py

pace_features.py

travel_features.py

weather_features.py

```

Does NOT contain

- Model inference
- Odds
- Portfolio logic

---

# sportsbook/models/

## Purpose

Contains production prediction models.

Owns

- Model inference
- Calibration
- Ensemble logic
- Model loading
- Probability estimation

Examples

```

nba_model.py

mlb_model.py

ensemble.py

calibration.py

```

Does NOT contain

- Feature generation
- Optimization
- Backtesting

---

# sportsbook/optimizer/

## Purpose

Builds betting portfolios.

Owns

- Ticket construction
- Bet ranking
- Correlation analysis
- Diversification
- Portfolio optimization

Examples

```

ticket_builder.py

correlation.py

portfolio_optimizer.py

```

Does NOT contain

- Predictions
- Stake sizing

---

# sportsbook/bankroll/

## Purpose

Determines capital allocation.

Owns

- Stake sizing
- Kelly calculations
- Daily limits
- Drawdown protection
- Exposure management

Examples

```

kelly.py

position_sizing.py

risk_budget.py

```

Does NOT contain

- Ticket generation
- Predictions

---

# sportsbook/backtest/

## Purpose

Provides deterministic replay and historical evaluation.

Owns

- Historical simulation
- Replay
- Strategy evaluation
- Performance calculation

Examples

```

backtest_runner.py

replay.py

historical_engine.py

```

Does NOT contain

- Model training
- Live execution

---

# sportsbook/analytics/

## Purpose

Measures system performance.

Owns

- ROI
- CLV
- Drawdown
- Performance metrics
- Reporting
- Dashboards

Examples

```

roi.py

clv.py

performance.py

reports.py

```

Does NOT contain

- Predictions
- Portfolio generation

---

# sportsbook/research/

## Purpose

Experimental work.

Nothing here is production.

Owns

- Experiments
- Feature ideas
- Model comparisons
- Hyperparameter tuning
- Validation
- Promotion candidates

Examples

```

experiments/

models/

datasets/

analysis/

```

Production code should never depend on Research.

Research may depend on production.

---

# sportsbook/api/

## Purpose

Application interfaces.

Owns

- REST API
- FastAPI
- Endpoints
- Serialization
- Request validation

Examples

```

routes/

schemas/

responses/

```

Does NOT contain

Business logic.

The API should call production engines.

---

# sportsbook/ui/

## Purpose

Presentation layer.

Owns

- Dashboards
- Web UI
- Desktop UI
- CLI

Contains no business logic.

---

# sportsbook/common/

## Purpose

Shared infrastructure.

Contains reusable code used by multiple engines.

Examples

```

config.py

logging.py

exceptions.py

constants.py

time.py

types.py

```

Should NOT become a dumping ground.

If functionality belongs to a specific engine, it belongs there instead.

---

# docs/

Architecture documentation.

Examples

```

ARCHITECTURE_OVERVIEW.md

DOMAIN_MODEL.md

DATA_FLOW.md

EVENT_MODEL.md

```

Documentation is treated as part of the architecture.

---

# data/

Persistent datasets.

```

raw/

processed/

cache/

```

## raw/

Downloaded external data.

Never modified.

## processed/

Normalized datasets.

Produced from raw data.

## cache/

Temporary artifacts.

Safe to regenerate.

---

# notebooks/

Research notebooks.

Exploration only.

Notebook code should eventually migrate into production modules.

---

# scripts/

Utility scripts.

Examples

```

download_data.py

train_model.py

build_dataset.py

```

Scripts orchestrate existing modules.

They should contain minimal business logic.

---

# tests/

Automated tests.

Structure should mirror production.

Example

```

tests/

data/

features/

models/

optimizer/

bankroll/

```

---

# Dependency Rules

```

docs

↑

scripts

↑

api

↑

ui

↑

analytics

↑

backtest

↑

bankroll

↑

optimizer

↑

models

↑

features

↑

data

```

Dependencies flow upward.

Lower layers never depend on higher layers.

Examples

Feature Engine

✓ May depend on Data

✗ May NOT depend on Optimizer

Prediction Engine

✓ May depend on Features

✗ May NOT depend on Analytics

Optimizer

✓ May depend on Predictions

✗ May NOT depend on UI

---

# File Placement Rules

Before creating a new file, ask:

1. Which engine owns this responsibility?
2. Does this file introduce business logic or infrastructure?
3. Is there already a module responsible for this behavior?
4. Can another engine own this more naturally?

If ownership is unclear, revisit the architecture before writing code.

---

# Long-Term Philosophy

The directory structure mirrors the architecture.

Every folder corresponds to a business capability.

Every engine owns one responsibility.

Every file has one obvious home.

By enforcing ownership at the directory level, the Sportsbook Engine remains modular, scalable, and understandable as the codebase grows.


One thing I'd add that will pay off later

Given your experience with HLQE, I'd eventually split sportsbook/data into two subdomains:

sportsbook/

    data/

        providers/
        adapters/
        normalization/
        storage/
        repositories/

Why?

Because there are five distinct responsibilities hiding inside "data":

Providers → talk to external APIs.
Adapters → convert provider models to canonical models.
Normalization → clean and validate incoming data.
Storage → persist canonical data.
Repositories → expose clean query interfaces to the rest of the application.

That separation is something HLQE evolved into over time. Starting with it here will keep the Data Engine much cleaner as you add sportsbooks, statistics providers, weather feeds, injury reports, and other data sources.