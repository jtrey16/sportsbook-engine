# tests/test_config.py

from sportsbook.common.config import get_settings


def test_configuration():

    settings = get_settings()

    assert settings.project_name == "Sportsbook Engine"
