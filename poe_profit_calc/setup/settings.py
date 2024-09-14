import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./../.env.dev", env_prefix="POE_PROFIT_CALC_", case_sensitive=False
    )
    REQUEST_LIMIT_PER_MINUTE: int
    ENV: str


class LocalSettings(Settings):
    model_config = SettingsConfigDict(
        env_file="./../.env.local", env_prefix="POE_PROFIT_CALC_", case_sensitive=False
    )
    ENV: str = "local"


class DevSettings(Settings):
    model_config = SettingsConfigDict(
        env_file="./../.env.dev", env_prefix="POE_PROFIT_CALC_", case_sensitive=False
    )
    ENV: str = "dev"


class ProductionSettings(Settings):
    model_config = SettingsConfigDict(
        env_file="./../.env.prod", env_prefix="POE_PROFIT_CALC_", case_sensitive=False
    )
    ENV: str = "prod"


def get_settings():
    _env = os.getenv("POE_PROFIT_CALC_RUN_MODE", "local")
    if _env == "local":
        return LocalSettings()  # type: ignore
    elif _env == "dev":
        return DevSettings()  # type: ignore
    else:
        return ProductionSettings()  # type: ignore
