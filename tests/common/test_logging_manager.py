# tests/common/test_logging_manager.py

import logging

from sportsbook.common.logging_manager import LoggingManager


def test_get_logger_returns_logger():

    logger = LoggingManager.get_logger(
        "TestEngine",
    )

    assert isinstance(
        logger,
        logging.Logger,
    )


def test_get_logger_name():

    logger = LoggingManager.get_logger(
        "PredictionEngine",
    )

    assert logger.name == "PredictionEngine"


def test_logging_is_configured():

    LoggingManager.configure()

    LoggingManager.configure()

    LoggingManager.configure()

    assert LoggingManager.is_configured()
