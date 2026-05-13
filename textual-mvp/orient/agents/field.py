import asyncio
import json
import random
from typing import Dict, Any
from datetime import datetime
from base_loop import BaseAgent

class FieldAgent(BaseAgent):
    def __init__(self):
        super().__init__("FieldAgent")
        # ADNOC Total Capacity: 4.85M bpd
        self.total_capacity = 4.85
        self.current_production = 3.4 # Current estimated level

    async def observe(self) -> Dict[str, Any]:
        """Fetch field telemetry (Simulated SCADA/ENERGYai)."""
        # In a real environment, this connects to ADNOC Panorama / SCADA
        return {
            "reservoir_pressure_avg": 2450.0, # PSI
            "water_cut_pct": 12.5,
            "equipment_health_index": 0.94,
            "maintenance_active": False,
            "spare_capacity_available": self.total_capacity - self.current_production
        }

    async def orient(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate production ceiling and ramp-up readiness."""
        health = raw_data["equipment_health_index"]
        pressure = raw_data["reservoir_pressure_avg"]
        
        # Math: Production Ceiling
        # If health is low or pressure is dropping, the ceiling decreases
        health_penalty = (1.0 - health) * 2.0
        pressure_factor = min(1.0, pressure / 2500.0)
        
        production_ceiling = self.total_capacity * pressure_factor * (1.0 - health_penalty)
        
        # Ramp-up speed (M bpd per 24h)
        # Higher health = faster ramp-up
        ramp_speed = 0.5 * health 
        
        trend = "expanding" if production_ceiling > self.total_capacity * 0.95 else "stagnant"
        
        self.state["metrics"]["confidence"] = 0.95
        self.state["metrics"]["trend"] = trend

        return {
            "production_ceiling_mbpd": round(production_ceiling, 2),
            "ramp_up_readiness_24h": round(ramp_speed, 2),
            "reservoir_health": "stable" if pressure > 2300 else "declining",
            "spare_capacity_mbpd": round(production_ceiling - self.current_production, 2),
            "equipment_risk": "low" if health > 0.9 else "monitor"
        }

async def main():
    agent = FieldAgent()
    result = await agent.run()
    agent.save_to_bus()
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
