I actually think we should break Phase 1 down much further.

Right now it's still at the "project management" level. We want it to become an implementation roadmap where every task is only a few hours (or at most a day) of work.

One thing I learned from HLQE is that **architecture work should happen before infrastructure work**, because your infrastructure ends up depending on the architecture.

---

# Phase 1 — Foundation

## Goal

Establish the core architecture and development infrastructure required for all future work.

---

# Milestone 1.1 — Project Bootstrap

## Goal

Create a healthy development environment.

### Tasks

* Initialize Git repository
* Configure Python virtual environment
* Install core dependencies
* Configure VS Code workspace
* Configure `.gitignore`
* Configure `requirements.txt`
* Verify project builds

### Deliverables

```text
sportsbook-engine/

.gitignore

requirements.txt

.venv/
```

### Success Criteria

* Project opens successfully.
* Python interpreter configured.
* Dependencies install without errors.
* Git repository connected to GitHub.

---

# Milestone 1.2 — Repository Structure

## Goal

Create the permanent directory structure.

### Tasks

Create production folders

```text
sportsbook/

    data/

    features/

    models/

    optimizer/

    bankroll/

    backtest/

    analytics/

    api/

    common/

    research/
```

Create project folders

```text
docs/

tests/

scripts/

notebooks/

data/

    raw/

    processed/

    cache/
```

### Success Criteria

* Folder ownership matches architecture.
* No placeholder "misc" or "utils" folders.

---

# Milestone 1.3 — Configuration System

## Goal

Centralize application configuration.

### Tasks

Create

```text
sportsbook/common/config.py
```

Support

* Environment variables
* API keys
* Debug mode
* Database paths
* Logging configuration

Use

```
.env
```

internally.

### Deliverables

Configuration object

```python
Settings()
```

### Success Criteria

* No hardcoded configuration.
* Entire application loads configuration from one place.

---

# Milestone 1.4 — Logging System

## Goal

Build standardized logging.

### Tasks

Create

```text
sportsbook/common/logging.py
```

Support

* Console logging
* File logging
* Log levels
* Structured formatting

Example

```
[Data Engine]

Downloading odds...
```

### Success Criteria

Every engine logs consistently.

---

# Milestone 1.5 — Exception Framework

## Goal

Create a common exception hierarchy.

Example

```python
SportsbookError

    DataError

    PredictionError

    PortfolioError

    ConfigurationError
```

No generic

```python
Exception
```

inside business logic.

---

# Milestone 1.6 — Domain Models

This is where real implementation starts.

Create

```text
sportsbook/domain/
```

Implement

```text
Sport

League

Season

Event

Venue

Team

Player

Sportsbook

Market

Selection

Odds

Bet

Ticket

Portfolio

Bankroll

Settlement
```

Initially

Only data models.

No business logic.

---

# Milestone 1.7 — Event System

## Goal

Implement canonical event infrastructure.

Create

```text
sportsbook/events/
```

Implement

```python
Event
```

Base class

```python
EventType
```

Enum

```python
EventBus
```

Simple publish

subscribe

mechanism.

No engine-specific logic yet.

---

# Milestone 1.8 — Common Types

Create

```text
sportsbook/common/types.py
```

Shared

* IDs
* Enums
* Status objects
* Market types
* Selection types

Avoid duplicate enums across engines.

---

# Milestone 1.9 — Testing Infrastructure

Install

```text
pytest
```

Configure

```
tests/
```

Create

```python
test_domain.py

test_events.py

test_config.py
```

CI-ready.

---

# Milestone 1.10 — Development Tooling

Configure

* Ruff
* Black
* MyPy
* Pre-commit hooks

Add

```bash
make test

make lint

make format
```

(or equivalent scripts)

---

# Phase 1 Deliverables

At completion we should have

```
Repository

↓

Architecture

↓

Directory Structure

↓

Configuration

↓

Logging

↓

Exceptions

↓

Domain Models

↓

Event System

↓

Testing

↓

Developer Tooling
```

No betting logic yet.

No AI.

No optimization.

Just a solid platform.

---

# Success Criteria

✅ Repository builds

✅ Tests execute

✅ Logging operational

✅ Configuration centralized

✅ Domain models implemented

✅ Event system functional

✅ Development tooling configured

✅ Documentation aligned with implementation

---

# One architectural change I'd make

After everything we've documented, I'd introduce one new top-level package before writing any code:

```text
sportsbook/

    domain/

    events/

    engines/

    common/
```

Instead of immediately creating implementation files under `data`, `models`, `optimizer`, and so on, I'd separate **the architectural concepts** from **their implementations**:

* **`domain/`** → Canonical business objects (`Event`, `Market`, `Odds`, `Ticket`, etc.).
* **`events/`** → Event definitions, event bus, event types, replay support.
* **`engines/`** → The major engines (`data`, `features`, `prediction`, `value`, `portfolio`, `bankroll`, `analytics`, `research`), each owning its own implementation.
* **`common/`** → Shared infrastructure (configuration, logging, exceptions, utilities).

That mirrors the architecture documents you've written. The codebase starts by reflecting the concepts of the system rather than the technologies used to implement it, which makes it much easier to keep the implementation aligned with the architecture as the project grows.


sportsbook/

    common/
        config.py
        logging.py
        exceptions.py
        constants.py
        ids.py
        time.py

    domain/
        sport.py
        league.py
        season.py
        event.py
        venue.py
        team.py
        player.py
        sportsbook.py
        market.py
        selection.py
        odds.py
        ticket.py
        bet.py
        bankroll.py
        portfolio.py
        settlement.py

    events/
        event.py
        event_bus.py
        event_types.py
        replay.py

    engines/

        data/
            providers/
            adapters/
            normalization/
            repositories/
            storage/

        features/
            generators/
            transforms/
            validation/

        prediction/
            inference/
            calibration/
            ensemble/

        value/
            implied_probability.py
            expected_value.py
            edge.py

        portfolio/
            correlation.py
            optimizer.py
            ticket_builder.py

        bankroll/
            kelly.py
            sizing.py
            exposure.py

        execution/
            ticket_manager.py
            settlement.py

        analytics/
            roi.py
            clv.py
            reporting.py

        research/
            experiments/
            promotion/
            evaluation/

        backtest/
            replay_engine.py
            simulator.py

    api/

    ui/