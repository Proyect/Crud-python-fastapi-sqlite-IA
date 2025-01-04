from pydantic import BaseModel

class HealthClaim(BaseModel):
    claim: str
    category: str
    trust_score: float
    status: str
