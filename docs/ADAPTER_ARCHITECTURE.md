// docs/ADAPTER_ARCHITECTURE.md

External APIs

↓

Provider Models

↓

Provider Adapters

↓

Canonical Models

↓

Business Logic

Business logic never imports provider models.

Ever.

Only canonical models.

This philosophy scales beautifully

Today

Odds API

Tomorrow

DraftKings

FanDuel

BetMGM

Pinnacle

ESPN

Weather

Twitter

News

Rotowire

Nothing changes.

Every provider writes

Provider Schema

↓

Canonical Game

That's why it's orthogonal.

I think we should adopt a philosophy very similar to HLQE

One of the strongest ideas that emerged from HLQE was:

Everything inside the engine speaks one language.

Not

DraftKingsGame

OddsApiGame

ESPNGame

Only

Game

Not

DraftKingsOdds

FanDuelOdds

Only

Odds

The adapters absorb all the messiness of external APIs. Once data crosses into the engine, every subsystem—from feature engineering to prediction, optimization, and analytics—works exclusively with canonical domain objects. That's what keeps the core architecture clean, testable, and extensible as you add more data sources over time.