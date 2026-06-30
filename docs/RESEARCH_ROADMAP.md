// docs/RESEARCH_ROADMAP.md

# Research Roadmap

## Purpose

The Research Roadmap defines the long-term research direction of the Sportsbook Engine.

Unlike the architecture documents, which describe how the system is built, this document describes what the platform is trying to learn.

The goal is to continuously improve probability estimation, expected value detection, portfolio optimization, and bankroll growth through disciplined experimentation.

Every experiment should answer a measurable question.

Every successful experiment should eventually become production code.

---

# Research Philosophy

Sports betting is treated as a quantitative research problem.

The objective is not to predict winners.

The objective is to estimate probabilities more accurately than the betting market in specific situations.

Research follows the scientific method.

Observation

↓

Hypothesis

↓

Experiment

↓

Backtest

↓

Evaluation

↓

Promotion

↓

Production

Every experiment must be reproducible.

---

# Long-Term Vision

The Sportsbook Engine should become a self-improving research platform.

```
Historical Data

↓

Research

↓

Experiments

↓

Backtesting

↓

Evaluation

↓

Model Promotion

↓

Production

↓

Analytics

↓

New Research
```

The system should continuously learn while maintaining deterministic production behavior.

---

# Research Areas

## Probability Estimation

Primary Goal

Estimate the true probability of every betting selection.

Research Topics

- Regression models
- Gradient boosting
- Neural networks
- Bayesian methods
- Ensemble models
- Probability calibration

Success Metrics

- Calibration Error
- Brier Score
- Log Loss
- Closing Line Value
- Long-term ROI

---

## Feature Engineering

Primary Goal

Identify predictive signals from historical sports data.

Potential Features

Player

- Rolling averages
- Usage rate
- Minutes trend
- Shooting efficiency
- Injury status
- Fatigue
- Recent form

Team

- Offensive rating
- Defensive rating
- Pace
- Rest days
- Travel distance
- Home/Away
- Lineup changes

Game

- Weather
- Officials
- Altitude
- Schedule congestion
- Historical matchup

Market

- Opening odds
- Closing odds
- Line movement
- Public betting percentages
- Sharp money indicators

---

## Market Efficiency

Primary Goal

Determine which betting markets are least efficient.

Research Questions

- Which sports produce the largest edge?
- Which sportsbooks consistently misprice markets?
- Which player props outperform moneylines?
- How quickly does the market react to injuries?
- Are opening lines more exploitable than closing lines?

Potential Markets

- Moneyline
- Spread
- Totals
- Player Props
- Team Props
- Same Game Parlays
- Live Betting

---

## Portfolio Optimization

Primary Goal

Construct portfolios that maximize long-term bankroll growth.

Research Topics

- Correlation
- Diversification
- Portfolio variance
- Expected growth
- Exposure balancing
- Daily risk budgeting

Questions

- Are singles superior to parlays?
- When do parlays improve expected return?
- How much correlation is acceptable?
- How many tickets should be recommended daily?

---

## Bankroll Management

Primary Goal

Maximize long-term compounding while minimizing drawdowns.

Research Topics

- Kelly Criterion
- Fractional Kelly
- Flat Betting
- Dynamic Position Sizing
- Drawdown Controls
- Volatility Targeting

Questions

- What fraction of bankroll should be risked?
- Should exposure vary by confidence?
- Should stake size adapt to model calibration?

---

## Closing Line Value

Primary Goal

Measure prediction quality independently of outcomes.

Research Questions

- Does beating the closing line predict long-term profitability?
- How often does the model beat market movement?
- Which markets produce the highest CLV?

Metrics

- Average CLV
- CLV by sport
- CLV by sportsbook
- CLV by market type

---

## Calibration

Primary Goal

Ensure predicted probabilities match observed outcomes.

Example

Model predicts

70%

Expected Result

Approximately 70 wins out of 100 opportunities.

Research Topics

- Reliability diagrams
- Probability calibration
- Confidence adjustment

---

## Explainability

Primary Goal

Understand why the model produced a recommendation.

Potential Techniques

- SHAP values
- Feature importance
- Decision trees
- Natural language summaries

Every recommendation should be explainable.

---

# Initial Experiments

## Experiment 001

Question

Can a simple baseline model outperform implied sportsbook probability?

Method

- Historical player props
- Logistic Regression
- No advanced features

Success

Positive expected value after backtesting.

---

## Experiment 002

Question

Do rolling averages improve prediction quality?

Method

Add

- Last 5 games
- Last 10 games
- Last 20 games

Measure

Calibration improvement.

---

## Experiment 003

Question

Does injury information improve player props?

Method

Compare

Without injuries

vs

With injuries

Measure

Brier Score improvement.

---

## Experiment 004

Question

Can line movement improve probability estimates?

Method

Include

Opening Odds

↓

Current Odds

↓

Closing Odds

Evaluate

Calibration

ROI

CLV

---

## Experiment 005

Question

Do diversified portfolios outperform independent recommendations?

Method

Compare

Independent bets

vs

Portfolio optimization

Measure

ROI

Variance

Maximum drawdown

---

# Promotion Criteria

Research is not promoted because it "looks good."

Promotion requires objective evidence.

Potential Requirements

✓ Improved calibration

✓ Positive CLV

✓ Positive ROI

✓ Reduced drawdown

✓ Statistically significant improvement

✓ Reproducible results

---

# Long-Term AI Roadmap

Phase 1

Baseline statistical models

↓

Phase 2

Gradient Boosting

↓

Phase 3

Ensemble Models

↓

Phase 4

Deep Learning

↓

Phase 5

Adaptive Online Learning

↓

Phase 6

Portfolio-Aware AI

---

# Success Metrics

The project should optimize for

Prediction Quality

- Brier Score
- Log Loss
- Calibration

Investment Performance

- ROI
- Expected Value
- Closing Line Value
- Profit Factor
- Sharpe-like Ratio
- Maximum Drawdown

Portfolio Quality

- Correlation
- Diversification
- Risk-adjusted Return

Operational Metrics

- Backtest Speed
- Model Latency
- Data Quality
- Reproducibility

---

# Guiding Principle

The Sportsbook Engine should improve through disciplined research rather than intuition.

Every new feature, model, or strategy begins as a hypothesis.

Only ideas that demonstrate measurable improvement through backtesting and statistical evaluation should become part of the production system.

The long-term objective is not to build the most complex model.

The objective is to build the most reliable decision-making system for allocating capital within sports betting markets.

# One addition I would make

This is something I don't think we emphasized enough in HLQE until later.

I'd add one more research section called "Edge Discovery."

Instead of assuming your edge is "AI predicts better," the platform should actively search for where an edge exists.

For example:

Does the model perform better on NBA assists than points?
Are NHL moneylines more efficient than NHL shots-on-goal props?
Which sportsbooks lag the market after injury announcements?
Which time of day produces the best opportunities?
Does the model perform better before or after significant line movement?

The assumption should be that edge is localized, not universal. Your goal is to discover those pockets where your probability estimates consistently outperform the market and then allocate more capital there. That research mindset is what separates a quantitative platform from a generic betting model.