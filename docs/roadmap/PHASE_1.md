# Phase 1 — Foundation

## Goal

Create a safe, runnable foundation for TradeBot7x with paper-only broker connectivity.

## Included

- FastAPI backend
- Next.js frontend
- PostgreSQL service
- Docker Compose
- Alpaca paper account integration
- Health endpoint
- Account endpoint
- Environment-based configuration
- Hard block on live execution
- Basic system dashboard

## Not included yet

- Strategy engine
- Scanner
- Backtesting
- Automated order execution
- Options trading
- AI decisioning
- Live trading

## Acceptance criteria

1. `docker compose up --build` starts database, API, and web UI.
2. `GET /health` returns status and trading mode.
3. With Alpaca paper credentials configured, `GET /account` returns paper account data.
4. Live execution remains disabled regardless of broker credentials.
5. Secrets are excluded from Git.
