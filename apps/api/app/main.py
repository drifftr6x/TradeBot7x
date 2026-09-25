from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.account import router as account_router
from app.api.routes.health import router as health_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title="TradeBot7x API",
    version="0.1.0",
    description="Risk-controlled algorithmic trading platform API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(account_router)


@app.get("/")
def root() -> dict:
    return {
        "name": "TradeBot7x API",
        "version": "0.1.0",
        "mode": settings.trading_mode,
    }
