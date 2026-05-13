import asyncio
import json
from typing import Dict, Any
from datetime import datetime
from base_loop import BaseAgent

class DemandAgent(BaseAgent):
    def __init__(self):
        super().__init__("DemandAgent")
        # Baseline data for Asia-Pacific demand (M bpd)
        self.baseline_demand = 35.5 
        # China EV adoption rate baseline (monthly % of new sales)
        self.china_ev_adoption = 45.0 

    async def observe(self) -> Dict[str, Any]:
        """Fetch demand signals (Simulated for research MVP)."""
        # In a production environment, this would pull from IEA API or custom scrapers
        # For now, we simulate a slight increase in EV adoption and its impact
        current_month = datetime.now().month
        seasonal_refinery_factor = 1.0 + (0.05 if current_month in [6, 7, 8, 12] else -0.02)
        
        return {
            "china_ev_sales_pct": self.china_ev_adoption + (current_month * 0.5), # Rising EV adoption
            "refinery_intake_global": self.baseline_demand * seasonal_refinery_factor,
            "iea_forecast_delta": -0.2 # IEA predicting slight surplus
        }

    async def orient(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate peak demand risk and fleet displacement."""
        ev_pct = raw_data["china_ev_sales_pct"]
        refinery_intake = raw_data["refinery_intake_global"]
        
        # Math: Calculate 'Barrels Displaced' (Heuristic)
        # Assuming every 1% increase in China EV sales displaces 50k bpd of future demand
        displacement_bpd = (ev_pct - 30.0) * 50000 
        
        # Strategic Clock: How close are we to the 2030 peak?
        years_to_2030 = 2030 - datetime.now().year
        peak_risk_index = min(1.0, (ev_pct / 100.0) + (1.0 / max(1, years_to_2030)))

        trend = "plateauing" if peak_risk_index > 0.6 else "growing"
        
        self.state["metrics"]["confidence"] = 0.75
        self.state["metrics"]["trend"] = trend

        return {
            "peak_demand_risk": round(peak_risk_index, 2),
            "china_ev_adoption_rate": f"{round(ev_pct, 1)}%",
            "est_displacement_bpd": int(displacement_bpd),
            "refinery_utilization_forecast": "high" if refinery_intake > self.baseline_demand else "moderate",
            "strategic_window": "closing" if ev_pct > 50 else "open"
        }

async def main():
    agent = DemandAgent()
    result = await agent.run()
    agent.save_to_bus()
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
