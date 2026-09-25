from alpaca.trading.client import TradingClient

from app.core.config import get_settings


def get_trading_client() -> TradingClient:
    settings = get_settings()

    if settings.live_trading_enabled:
        raise RuntimeError(
            "Live trading is intentionally disabled in Phase 1. "
            "Do not enable until live execution safeguards are implemented."
        )

    if not settings.alpaca_api_key or not settings.alpaca_secret_key:
        raise RuntimeError("Alpaca paper credentials are not configured.")

    return TradingClient(
        settings.alpaca_api_key,
        settings.alpaca_secret_key,
        paper=True,
    )
