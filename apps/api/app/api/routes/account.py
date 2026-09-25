from fastapi import APIRouter, HTTPException

from app.brokers.alpaca_client import get_trading_client

router = APIRouter(prefix="/account", tags=["account"])


@router.get("")
def account() -> dict:
    try:
        acct = get_trading_client().get_account()
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    return {
        "id": str(acct.id),
        "status": str(acct.status),
        "currency": acct.currency,
        "equity": str(acct.equity),
        "cash": str(acct.cash),
        "buying_power": str(acct.buying_power),
        "portfolio_value": str(acct.portfolio_value),
        "paper": True,
    }
