// docs/DOMAIN_MODEL.md

# Domain Model

## Purpose

The Domain Model defines the canonical business objects used throughout the Sportsbook Engine.

These objects represent the language of the system and are intentionally independent of:

- External APIs
- Sportsbooks
- Data providers
- AI models
- Optimization algorithms
- User interfaces

Every subsystem communicates using these canonical domain objects.

External providers are responsible for adapting their own schemas into these models.

---

# Design Principles

## Canonical Objects

Every business concept has exactly one canonical representation.

Examples:

- Event
- Market
- Odds
- Selection
- Bet
- Ticket
- Portfolio
- Bankroll

No provider-specific objects should exist outside the Data Engine.

---

## Single Ownership

Every domain object has exactly one owner.

Examples:

- Event owns participating teams.
- Market owns available selections.
- Odds belong to a Selection.
- Ticket owns Bets.
- Portfolio owns Tickets.
- Bankroll owns capital.

No object duplicates another object's canonical state.

---

## Business First

The Domain Model describes what exists.

It does **not** describe:

- AI
- Expected value
- Feature engineering
- Optimization
- Backtesting
- Analytics

Those belong to engine documentation.

---

# Domain Hierarchy

```
Sport
    └── League
            └── Season
                    └── Event
                            ├── Teams
                            ├── Players
                            ├── Markets
                            └── Results
```

```
Portfolio
    ├── Bankroll
    ├── Tickets
    │       └── Bets
    │               └── Selection
    └── Performance
```

---

# Core Domain Objects

## Sport

Represents a category of competition.

Examples:

- NBA
- NFL
- MLB
- NHL
- UFC
- Tennis

Fields

```
sport_id

name
```

---

## League

Represents an organized competition.

Examples

- NBA
- NFL
- MLB
- Premier League

Fields

```
league_id

sport

name
```

---

## Season

Represents a league season.

Fields

```
season_id

league

year

start_date

end_date
```

---

## Event

Represents a single sporting contest.

Examples

- Lakers vs Celtics
- Chiefs vs Bills
- Jones vs Aspinall

Fields

```
event_id

league

season

start_time

status

venue

participants
```

---

## Venue

Represents the location where an event occurs.

Fields

```
venue_id

name

city

country

altitude

surface
```

---

## Team

Represents a competitive team.

Fields

```
team_id

league

name

roster

coach
```

---

## Player

Represents an individual participant.

Fields

```
player_id

team

position

status

attributes
```

---

## Sportsbook

Represents a betting provider.

Examples

- DraftKings
- FanDuel
- BetMGM
- Pinnacle

Fields

```
sportsbook_id

name
```

Sportsbooks provide odds.

They do not own markets.

---

## Market

Represents a betting market.

Examples

```
Moneyline

Spread

Total

Player Points

Player Assists
```

Markets describe what is being wagered.

Markets do not contain odds.

Fields

```
market_id

event

market_type

status
```

---

## Selection

Represents one selectable outcome within a market.

Examples

```
Chiefs Moneyline

Bills Moneyline

Over 24.5

Under 24.5
```

Selections are what users actually wager on.

Fields

```
selection_id

market

description
```

---

## Odds

Represents sportsbook pricing for a Selection.

Odds belong to:

Selection + Sportsbook

Fields

```
odds_id

selection

sportsbook

price

opening_price

closing_price

timestamp
```

Odds are market data.

They contain no predictions.

---

## Prediction

Represents the model's estimated probability for a Selection.

Fields

```
prediction_id

selection

probability

confidence

model_version

created_at
```

Predictions are independent of sportsbook odds.

---

## Bet

Represents a single wager.

Fields

```
bet_id

selection

sportsbook

odds

stake

status
```

A Bet always references exactly one Selection.

---

## Ticket

Represents one betting ticket.

A ticket contains one or more Bets.

Fields

```
ticket_id

bets

stake

potential_payout

status

created_at
```

---

## Portfolio

Represents the user's betting exposure.

Fields

```
portfolio_id

tickets

bankroll

daily_risk

open_exposure
```

The Portfolio owns all active tickets.

---

## Bankroll

Represents available betting capital.

Fields

```
starting_balance

current_balance

peak_balance

available_balance

reserved_balance

daily_risk

drawdown

roi
```

The Bankroll owns capital allocation.

---

## Settlement

Represents the final outcome of a completed Bet.

Possible outcomes

```
Won

Lost

Push

Void

Cancelled
```

Fields

```
settlement_id

bet

result

payout

settled_at
```

Settlement updates the Portfolio and Bankroll.

---

# Object Relationships

```
Sport

└── League

      └── Season

            └── Event

                  ├── Team

                  ├── Player

                  ├── Market

                  │      └── Selection

                  │              └── Odds

                  └── Result
```

```
Portfolio

├── Bankroll

├── Ticket

│      └── Bet

│              └── Selection

└── Performance
```

---

# Canonical Data Model

Every external provider must be adapted into these domain objects.

```
DraftKings API
                │
FanDuel API
                │
Odds API
                │
League APIs
                │
                ▼
Canonical Domain Objects
                │
                ▼
Business Logic
```

Business logic never consumes provider-specific schemas.

Every subsystem communicates exclusively through the canonical domain model.

---

# Future Domain Objects

The following objects are expected to be added as the platform evolves:

- Injury Report
- Line Movement
- Weather
- Official / Referee
- Lineup
- News Event
- Feature Vector
- Model Version
- Experiment
- Closing Line Value
- Performance Snapshot

These are intentionally excluded from the initial domain until they become first-class business concepts.

If this were my project, I'd eventually split the world into:

Core Domain: Event, Market, Selection, Odds, Bet, Ticket, Portfolio, Bankroll, Settlement
Research Domain: Prediction, FeatureVector, ModelVersion, Experiment, Calibration
Execution Domain: CandidateBet, Recommendation, StakeAllocation

That separation mirrors the architecture of quantitative trading systems: the market exists independently of your models, your models produce research outputs, and those outputs drive execution decisions. It keeps the business model stable even as your AI and optimization techniques evolve. I think you'll appreciate that distinction as the platform grows.