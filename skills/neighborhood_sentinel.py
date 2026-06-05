from solomon.agents.counter_surv_agent import CounterSurvAgent
from solomon.core.config import SolomonConfig
from solomon.core.compliance import ComplianceLogger

async def run_neighborhood_sentinel(location: str = "Havelock North"):
    """Main Neighborhood Sentinel Skill"""
    config = SolomonConfig()
    compliance = ComplianceLogger()
    agent = CounterSurvAgent(config, compliance)
    
    result = await agent.run_full_sweep(location)
    return result
