import json
import os
import asyncio
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.state = {
            "agent": self.name,
            "timestamp": datetime.now().isoformat(),
            "status": "initialized",
            "data": {},
            "metrics": {
                "confidence": 0.0,
                "trend": "stable"
            }
        }

    @abstractmethod
    async def observe(self) -> Dict[str, Any]:
        """Fetch raw signals from data sources."""
        pass

    @abstractmethod
    async def orient(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process raw data into intelligence/trends."""
        pass

    async def run(self) -> Dict[str, Any]:
        """Execute the agent loop and return the state."""
        try:
            raw_data = await self.observe()
            processed_data = await self.orient(raw_data)
            self.state["data"] = processed_data
            self.state["status"] = "success"
            self.state["timestamp"] = datetime.now().isoformat()
        except Exception as e:
            self.state["status"] = "error"
            self.state["error"] = str(e)
        
        return self.state

    def save_to_bus(self, file_path: str = "world_state.json"):
        """Update the global world state bus."""
        bus_data = {}
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                try:
                    bus_data = json.load(f)
                except json.JSONDecodeError:
                    bus_data = {}
        
        bus_data[self.name] = self.state
        bus_data["last_update"] = datetime.now().isoformat()
        
        with open(file_path, "w") as f:
            json.dump(bus_data, f, indent=4)

if __name__ == "__main__":
    import asyncio
    from geopolitics import GeopoliticsAgent
    from market import MarketAgent
    from demand import DemandAgent
    from logistics import LogisticsAgent
    from esg import ESGAgent
    from field import FieldAgent
    from competitor import CompetitorAgent

    async def run_all():
        agents = [
            GeopoliticsAgent(),
            MarketAgent(),
            DemandAgent(),
            LogisticsAgent(),
            ESGAgent(),
            FieldAgent(),
            CompetitorAgent()
        ]
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Launching Sovereign Intelligence Fusion...")
        
        tasks = [agent.run() for agent in agents]
        results = await asyncio.gather(*tasks)
        
        # Save each to bus
        for agent in agents:
            agent.save_to_bus()

        # Synthesis: Intelligence Fusion Output
        fusion = {
            "metadata": {
                "system": "Meridian OODA Orient Layer",
                "cycle_timestamp": datetime.now().isoformat(),
                "agent_count": len(agents)
            },
            "world_state_vector": {r["agent"]: r["data"] for r in results},
            "intelligence_fusion": {
                "summary": "Synthesizing multi-agent signals...",
                "global_confidence": sum(r["metrics"]["confidence"] for r in results) / len(results),
                "regime_alert": "Nominal"
            }
        }

        # Simple Fusion Logic
        risk = fusion["world_state_vector"]["GeopoliticalAgent"]["hormuz_risk_index"]
        brent = fusion["world_state_vector"]["MarketAgent"]["brent_price"]
        ceiling = fusion["world_state_vector"]["FieldAgent"]["production_ceiling_mbpd"]

        if risk > 0.6:
            fusion["intelligence_fusion"]["summary"] = f"HIGH RISK: Hormuz tensions ({risk}) detected. Market pricing Brent at ${brent}. Strategic recommendation: Maximize Fujairah bypass throughput."
            fusion["intelligence_fusion"]["regime_alert"] = "CRISIS_POSTURE"
        else:
            fusion["intelligence_fusion"]["summary"] = f"STABLE: System operating at {ceiling}M bpd ceiling. Market sentiment is {fusion['world_state_vector']['MarketAgent']['market_regime']}."

        print(json.dumps(fusion, indent=4))

    asyncio.run(run_all())
