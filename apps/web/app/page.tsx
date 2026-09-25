async function getHealth() {
  const base = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";
  try {
    const res = await fetch(`${base}/health`, { cache: "no-store" });
    if (!res.ok) throw new Error("API unavailable");
    return await res.json();
  } catch {
    return null;
  }
}

export default async function Home() {
  const health = await getHealth();

  return (
    <main>
      <header>
        <div>
          <h1>TradeBot7x</h1>
          <div className="muted">Risk-controlled algorithmic trading platform</div>
        </div>
        <span className="badge">PAPER MODE</span>
      </header>

      <section className="grid">
        <div className="card">
          <h2>API</h2>
          <div className="value">{health ? "ONLINE" : "OFFLINE"}</div>
          <div className="muted">{health?.service ?? "Waiting for backend"}</div>
        </div>

        <div className="card">
          <h2>Trading Mode</h2>
          <div className="value">{health?.trading_mode?.toUpperCase() ?? "PAPER"}</div>
          <div className="muted">Live execution disabled</div>
        </div>

        <div className="card">
          <h2>Broker</h2>
          <div className="value">ALPACA</div>
          <div className="muted">Paper credentials required</div>
        </div>
      </section>

      <section className="grid">
        <div className="card panel">
          <h2>AI Market Scanner</h2>
          <p className="muted">Not started — planned for a later phase.</p>
        </div>
        <div className="card panel">
          <h2>Open Positions</h2>
          <p className="muted">No positions loaded.</p>
        </div>
      </section>
    </main>
  );
}
