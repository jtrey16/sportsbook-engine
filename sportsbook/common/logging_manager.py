# sportsbook/common/logging_manager.py
# sportsbook/common/logging_manager.py

from __future__ import annotations

import logging

from sportsbook.common.config import get_settings


class LoggingManager:
    """
    Centralized logging configuration for the Sportsbook Engine.

    Responsibilities
    ----------------
    - Configure the application's root logger.
    - Create consistent console and file log handlers.
    - Provide configured loggers for every subsystem.

    This class is safe to configure multiple times. Only the first call
    performs initialization.
    """

    _configured = False

    @classmethod
    def configure(cls) -> None:
        """
        Configure the application's logging system.

        Safe to call multiple times.
        """

        if cls._configured:
            return

        settings = get_settings()

        settings.log_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        formatter = logging.Formatter(
            fmt=("%(asctime)s | " "%(levelname)-8s | " "%(name)-20s | " "%(message)s"),
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            formatter,
        )

        file_handler = logging.FileHandler(
            settings.log_directory / "sportsbook.log",
            encoding="utf-8",
        )
        file_handler.setFormatter(
            formatter,
        )

        root_logger = logging.getLogger()

        root_logger.setLevel(
            getattr(
                logging,
                settings.log_level.upper(),
            )
        )

        #
        # Remove any existing handlers so repeated configuration
        # never produces duplicate log messages.
        #
        root_logger.handlers.clear()

        root_logger.addHandler(
            console_handler,
        )

        root_logger.addHandler(
            file_handler,
        )

        cls._configured = True

    @classmethod
    def get_logger(
        cls,
        name: str,
    ) -> logging.Logger:
        """
        Return a configured logger.

        Logging is automatically configured on first use.
        """

        cls.configure()

        return logging.getLogger(
            name,
        )

    @classmethod
    def is_configured(cls) -> bool:
        """
        Return whether the logging system has been configured.
        """

        return cls._configured
