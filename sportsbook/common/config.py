# sportsbook/common/config.py

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    #
    # Application
    #

    project_name: str = Field(default="Sportsbook Engine")
    version: str = Field(default="0.1.0")

    environment: str = Field(default="development")
    debug: bool = Field(default=True)

    #
    # Data
    #

    raw_data_directory: Path = Field(default=Path("data/raw"))
    processed_data_directory: Path = Field(default=Path("data/processed"))
    cache_directory: Path = Field(default=Path("data/cache"))

    #
    # Logging
    #

    log_level: str = Field(default="INFO")
    log_directory: Path = Field(default=Path("logs"))

    #
    # Database
    #

    database_path: Path = Field(default=Path("data/sportsbook.db"))

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


_settings = Settings()


def get_settings() -> Settings:
    return _settings
