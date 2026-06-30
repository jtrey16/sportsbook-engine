Sportsbook Engine is a quantitative betting platform that
identifies positive expected value wagers,
constructs risk-aware betting portfolios,
manages bankroll growth,
and continuously improves prediction quality.


System Philosophy:
Raw Data

↓

Information

↓

Probability

↓

Expected Value

↓

Portfolio Construction

↓

Bankroll Allocation

↓

Performance Feedback

↓

Model Improvement


The Engines:
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

Analytics Engine


The Domain:
League

Game

Player

Team

Sportsbook

Market

Odds

Bet

Ticket

Portfolio

Bankroll

Prediction

Result


The Data Layer:
Download

Normalize

Store

Serve

Example:
ESPN

Odds API

Weather

↓

Normalized Game

↓

Database


Feature Layer:
Example
LeBron

↓

Average Last 5

↓

Minutes Trend

↓

Opponent Pace

↓

Usage Rate

↓

Rest Days

↓

Travel Distance

↓

Home Court


Prediction Layer

This is AI.

Nothing else.

Input

Features

Output

Probability

Not

BET

NO BET

Never.

Value Layer

Probably my favorite engine.

Prediction

↓

Sportsbook Odds

↓

Expected Value

↓

Edge

↓

Confidence

This becomes

Candidate Bet
Portfolio Engine

This is where your HLQE experience becomes valuable.

Don't optimize one bet.

Optimize today's portfolio.

Questions:

How many tickets?
Singles?
Parlays?
Correlation?
Exposure?
Maximum daily risk?

This is literally portfolio optimization.

Bankroll Engine

Should never know sports.

Only

Current bankroll

↓

Risk tolerance

↓

Kelly

↓

Recommended stake

That's it.

Analytics Engine

This becomes your Bloomberg Terminal.

Track everything.

ROI

Closing Line Value

Drawdown

Profit Factor

Average Odds

Expected Value

Calibration

Sharpe Ratio

Units Won

Edge By Sport

Edge By Market

Eventually hundreds of metrics.

Event Flow

I'd even document this.

Odds Updated

↓

Features Updated

↓

Predictions Updated

↓

Expected Value Updated

↓

Portfolio Generated

↓

Tickets Recommended

↓

User Bets

↓

Games Finish

↓

Bankroll Updated

↓

Analytics Updated

↓

Model Retrained

That becomes your lifecycle.

AI

Notice where AI lives.

One box.

Prediction Engine

Everything else is deterministic.

Exactly like HLQE.

The database

Eventually

Games

Markets

Odds

Players

Teams

Predictions

Tickets

Results

Bankroll History

Performance

Those become tables.

Biggest Difference from HLQE

One thing I'd change from your trading engine is adopting a hexagonal (ports and adapters) architecture much earlier.

Instead of modules calling APIs directly, define interfaces such as:

OddsProvider
PlayerStatsProvider
WeatherProvider
NewsProvider
SportsbookProvider

Then implement adapters like:

OddsAPIProvider
ESPNProvider
DraftKingsProvider
FanDuelProvider

Now, if you change data sources later, your prediction and optimization engines don't care—they just consume the interfaces. That keeps the core of your system independent of external services.

My recommendation for the next week

I would not write any production code yet. Instead, produce a design document that makes the implementation almost mechanical afterward.

Here's the order I'd follow:

Architecture Overview – System goals, guiding principles, and high-level pipeline.
Domain Model – Define every core object (Game, Market, Odds, Bet, Ticket, Portfolio, etc.) and their relationships.
Engine Responsibilities – Clearly document what each engine owns and, just as importantly, what it does not own.
Data Flow – Trace information from ingestion all the way through recommendation, settlement, and model feedback.
Directory-to-Responsibility Mapping – Explain what belongs in each folder so future code has a clear home.
Research Roadmap – List the first prediction strategies, feature ideas, and experiments you want to test.
Implementation Milestones – Break the build into small, testable phases with success criteria.

If we do that well, the codebase will grow around a stable architecture instead of the architecture having to catch up to the code. Given how your HLQE project evolved, I think this will save you a tremendous amount of refactoring later.