import os
from dataclasses import dataclass
from pathlib import Path

@dataclass
class SolomonConfig:
    """Central configuration for Solomon Platform"""
    VERSION: str = "0.1"
    USER_AGENT: str = "Solomon-OSINT/0.1 (+https://lowkeyconsultants.nz)"
    
    # Paths
    BASE_DIR: Path = Path(__file__).parent.parent.parent
    OUTPUT_DIR: Path = BASE_DIR / "reports"
    DATA_DIR: Path = BASE_DIR / "data"
    
    # API Keys
    NZBN_API_KEY: str = os.getenv("NZBN_API_KEY", "")
    
    def __post_init__(self):
        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.DATA_DIR.mkdir(parents=True, exist_ok=True)
