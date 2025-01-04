from app.models.schemas import HealthClaim
from typing import List

def process_claims(claims: List[str]) -> List[HealthClaim]:
    # Simulación de procesamiento con IA
    processed_claims = []
    for claim in claims:
        processed_claims.append(
            HealthClaim(
                claim=claim,
                category="Nutrition",
                trust_score=0.85,  # Simulación de puntaje
                status="Verified",
            )
        )
    return processed_claims
