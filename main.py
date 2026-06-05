import asyncio
from solomon.core.orchestrator import SolomonOrchestrator

async def main():
    print("🚀 Solomon Platform Starting...")
    orchestrator = SolomonOrchestrator()
    
    # Example run
    result = await orchestrator.run_full_sentinel("Havelock North")
    print("\n📊 Final Report:")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
