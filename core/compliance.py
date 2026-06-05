from datetime import datetime
from typing import List, Dict

class ComplianceLogger:
    """NZ Privacy Act 2020 compliant logging"""
    
    def __init__(self):
        self.logs: List[Dict] = []
    
    def log(self, source: str, data_type: str, purpose: str = "OSINT Investigation"):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "source": source,
            "data_type": data_type,
            "purpose": purpose,
            "legal_basis": "Privacy Act 2020 - Public sources"
        }
        self.logs.append(entry)
        print(f"📋 [Compliance] {source} - {data_type}")
    
    def get_logs(self):
        return self.logs
