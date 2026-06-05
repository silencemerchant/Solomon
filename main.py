#!/usr/bin/env python3
"""
Solomon Main Entry Point
"""
import asyncio
from solomon.core.orchestrator import SolomonOrchestrator

async def main():
    print("="*60)
    print("🚀 SOLOMON — Autonomous Intelligence Platform")
    print("="*60)
    
    orchestrator = SolomonOrchestrator()
    
    # Example usage
    result = await orchestrator.run_full_sentinel("Havelock North")
    
    print("\n✅ Solomon Sweep Complete")
    print(f"Location: {result.get('location')}")
    print(f"Bluetooth Devices: {result.get('bluetooth', {}).get('devices_found', 0)}")
    print(f"Threat Level: {result.get('threat_level', 'NORMAL')}")

if __name__ == "__main__":
    asyncio.run(main()) 
