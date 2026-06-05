from solomon.core.config import SolomonConfig
from solomon.core.compliance import ComplianceLogger
from solomon.agents.counter_surv_agent import CounterSurvAgent

class SolomonOrchestrator:
    """Main brain of Solomon - coordinates all agents"""
    
    def __init__(self):
        self.config = SolomonConfig()
        self.compliance = ComplianceLogger()
        self.counter_surv = CounterSurvAgent(self.config, self.compliance)
    
    async def run_full_sentinel(self, target_location: str = "Havelock North"):
        """Run Neighborhood + Counter-Surveillance sweep"""
        print(f"🛡️ Solomon Sentinel Activated for {target_location}")
        
        report = await self.counter_surv.run_full_sweep(target_location)
        
        self.compliance.log("SolomonOrchestrator", "Full Sentinel Run", f"Neighborhood sweep: {target_location}")
        
        return report
