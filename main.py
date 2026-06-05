#!/usr/bin/env python3
"""
Solomon Main Entry Point
"""
import asyncio
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solomon.core.orchestrator import SolomonOrchestrator

async def main():
    print("="*60)
    print("🚀 SOLOMON — Autonomous Intelligence Platform")
    print("="*60)
    
    orchestrator = SolomonOrchestrator()
    
    result = await orchestrator.run_full_sentinel("Havelock North")
    
    print("\n✅ Solomon Sweep Complete")
    print(f"Location: {result.get('location')}")
    print(f"Bluetooth Devices Found: {result.get('bluetooth', {}).get('devices_found', 0)}")

if __name__ == "__main__":
    asyncio.run(main())