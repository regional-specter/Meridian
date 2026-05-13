import asyncio
import json
import feedparser
from typing import Dict, Any, List
from datetime import datetime
from base_loop import BaseAgent

class GeopoliticsAgent(BaseAgent):
    def __init__(self):
        super().__init__("GeopoliticalAgent")
        self.news_feeds = [
            "https://www.reutersagency.com/feed/?best-topics=political-news&post_type=best",
            "http://feeds.bloomberg.com/politics/news.rss"
        ]
        self.risk_keywords = {
            "critical": ["blockade", "war", "missile", "seized", "closure"],
            "high": ["sanctions", "threat", "military", "conflict", "tensions"],
            "medium": ["diplomatic", "negotiations", "protest", "summit"]
        }

    async def observe(self) -> Dict[str, Any]:
        """Fetch latest news signals."""
        signals = []
        # In a real environment, we'd use GDELT API or a more robust scraper
        # For this MVP, we parse major RSS feeds for Hormuz-related signals
        for url in self.news_feeds:
            feed = feedparser.parse(url)
            for entry in feed.entries[:10]:
                signals.append({
                    "title": entry.title,
                    "summary": getattr(entry, "summary", ""),
                    "published": getattr(entry, "published", "")
                })
        
        return {"news_signals": signals}

    async def orient(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate Hormuz Risk Index and determine trend."""
        signals = raw_data.get("news_signals", [])
        risk_score = 0.0
        matches = []

        # Simple math-based scoring logic
        for signal in signals:
            text = (signal["title"] + " " + signal["summary"]).lower()
            
            # Focus specifically on regional relevance
            if "hormuz" in text or "iran" in text or "strait" in text or "gulf" in text:
                match_found = False
                if any(k in text for k in self.risk_keywords["critical"]):
                    risk_score += 0.25
                    match_found = True
                elif any(k in text for k in self.risk_keywords["high"]):
                    risk_score += 0.15
                    match_found = True
                elif any(k in text for k in self.risk_keywords["medium"]):
                    risk_score += 0.05
                    match_found = True
                
                if match_found:
                    matches.append(signal["title"])

        # Normalize score between 0.0 and 1.0
        hormuz_risk_index = min(1.0, risk_score)
        
        # Determine trend
        trend = "stable"
        if hormuz_risk_index > 0.7:
            trend = "volatile"
        elif hormuz_risk_index > 0.4:
            trend = "escalating"
        elif hormuz_risk_index < 0.2:
            trend = "improving"

        self.state["metrics"]["confidence"] = 0.85 # High confidence in news signals
        self.state["metrics"]["trend"] = trend

        return {
            "hormuz_risk_index": round(hormuz_risk_index, 2),
            "trend": trend,
            "relevant_headlines": matches[:5],
            "status": "active" if hormuz_risk_index < 0.8 else "crisis_mode"
        }

async def main():
    agent = GeopoliticsAgent()
    result = await agent.run()
    agent.save_to_bus()
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
