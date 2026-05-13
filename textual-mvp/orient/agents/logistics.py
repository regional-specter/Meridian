import asyncio
import json
import os
from typing import Dict, Any
from datetime import datetime
from base_loop import BaseAgent

class LogisticsAgent(BaseAgent):
    def __init__(self):
        super().__init__("LogisticsAgent")
        # Capacity constants (M bpd)
        self.fujairah_capacity = 1.7 
        self.strait_capacity_share = 3.15 # Remaining to reach 4.85
        self.ais_key = os.getenv("AISSTREAM_API_KEY")

    async def observe(self) -> Dict[str, Any]:
        """Fetch AIS tanker data and port status."""
        # Simulated AIS signals for Hormuz and Fujairah
        # In a real run, this would connect to wss://stream.aisstream.io/v0/stream
        return {
            "tankers_in_strait": 12,
            "tankers_at_fujairah": 4,
            "avg_wait_time_hours": 18.5,
            "weather_condition": "clear"
        }

    async def orient(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate throughput efficiency and logistics bottlenecks."""
        tanker_count = raw_data["tankers_in_strait"] + raw_data["tankers_at_fujairah"]
        wait_time = raw_data["avg_wait_time_hours"]
        
        # Math: Logistics Constraint Index (0.0 to 1.0)
        # Higher wait times and high tanker counts increase the index
        congestion_factor = (tanker_count / 30.0) * 0.5 + (wait_time / 48.0) * 0.5
        logistics_index = min(1.0, congestion_factor)
        
        # Calculate current 'Effective Capacity'
        # If Hormuz is 'risky' (from Geopolitical Agent, shared via bus), this would drop
        effective_throughput = self.fujairah_capacity + (self.strait_capacity_share * (1.0 - logistics_index * 0.2))

        trend = "congested" if logistics_index > 0.6 else "fluid"
        
        self.state["metrics"]["confidence"] = 0.80
        self.state["metrics"]["trend"] = trend

        return {
            "logistics_constraint_index": round(logistics_index, 2),
            "effective_export_capacity_mbpd": round(effective_throughput, 2),
            "fujairah_utilization": "92%" if logistics_index > 0.5 else "75%",
            "strait_status": "open" if wait_time < 24 else "bottlenecked",
            "vessels_active": tanker_count
        }

async def main():
    agent = LogisticsAgent()
    result = await agent.run()
    agent.save_to_bus()
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    asyncio.run(main())
