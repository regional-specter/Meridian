import asyncio
import json
import yfinance as yf
from typing import Dict, Any
from datetime import datetime, timedelta
from base_loop import BaseAgent

class MarketAgent(BaseAgent):
    def __init__(self):
        super().__init__("MarketAgent")
        self.benchmark = "BZ=F"  # Brent Crude Futures

    async def observe(self) -> Dict[str, Any]:
        """Fetch market data via yfinance."""
        ticker = yf.Ticker(self.benchmark)
        # Fetch last 5 days of data for trend analysis
        hist = ticker.history(period="5d")
        
        if hist.empty:
            return {"error": "No market data available"}

        latest_price = hist['Close'].iloc[-1]
        prev_price = hist['Close'].iloc[-2]
        
        return {
            "latest_price": float(latest_price),
            "prev_price": float(prev_price),
            "history": hist['Close'].tolist()
        }

    async def orient(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate price trend and market regime."""
        if "error" in raw_data:
            return raw_data

        latest = raw_data["latest_price"]
        prev = raw_data["prev_price"]
        price_change = ((latest - prev) / prev) * 100
        
        # Simple math for trend detection
        history = raw_data["history"]
        avg_price = sum(history) / len(history)
        
        trend = "bullish" if latest > avg_price else "bearish"
        volatility = "high" if abs(price_change) > 2.0 else "low"

        # Intelligence Fusion: Price Path Model
        sentiment = "neutral"
        if trend == "bullish" and volatility == "low":
            sentiment = "stable_growth"
        elif trend == "bearish" and volatility == "high":
            sentiment = "panic_selling"
        
        self.state["metrics"]["confidence"] = 0.90
        self.state["metrics"]["trend"] = trend

        return {
            "brent_price": round(latest, 2),
            "price_change_pct": round(price_change, 2),
            "market_regime": sentiment,
            "volatility": volatility,
            "benchmark": "Brent Crude (ICE)"
        }

async def main():
    agent = MarketAgent()
    result = await agent.run()
    agent.save_to_bus()
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
