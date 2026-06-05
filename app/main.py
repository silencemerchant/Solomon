from fastapi import FastAPI
from solomon.core.orchestrator import SolomonOrchestrator

app = FastAPI(title="Solomon Intelligence Platform")

orchestrator = SolomonOrchestrator()

@app.get("/")
async def root():
    return {"message": "Solomon is alive. Ready for operations."}

@app.post("/sentinel")
async def run_sentinel(location: str = "Havelock North"):
    """Run Neighborhood + Counter-Surveillance Sweep"""
    result = await orchestrator.run_full_sentinel(location)
    return result

@app.get("/health")
async def health():
    return {"status": "healthy", "version": "0.1"}q
