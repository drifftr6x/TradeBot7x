from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "TradeBot7x API"
    trading_mode: Literal["research", "paper", "live"] = "paper"
    allow_live_trading: bool = False

    alpaca_api_key: str = ""
    alpaca_secret_key: str = ""

    database_url: str = "postgresql+psycopg://tradebot:tradebot@db:5432/tradebot7x"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def live_trading_enabled(self) -> bool:
        return self.trading_mode == "live" and self.allow_live_trading


@lru_cache
def get_settings() -> Settings:
    return Settings()
