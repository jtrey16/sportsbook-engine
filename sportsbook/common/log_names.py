# sportsbook/common/log_names.py

from enum import StrEnum


class LogName(StrEnum):
    DATA = "engine.data"
    FEATURES = "engine.features"
    PREDICTION = "engine.prediction"
    VALUE = "engine.value"
    PORTFOLIO = "engine.portfolio"
    BANKROLL = "engine.bankroll"
    EXECUTION = "engine.execution"
    ANALYTICS = "engine.analytics"
    RESEARCH = "engine.research"
    BACKTEST = "engine.backtest"
