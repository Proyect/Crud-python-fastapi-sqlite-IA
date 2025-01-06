from fastapi import APIRouter, HTTPException
from app.services.openai_client import analyze_claim
from typing import List

router = APIRouter()

@router.post("/claims/analyze", summary="Analyze health claims using OpenAI")
def analyze_health_claims(claims: List[str]):
    """
    Endpoint para analizar afirmaciones de salud con OpenAI.
    """
    results = []
    for claim in claims:
        analysis = analyze_claim(claim)
        results.append({"claim": claim, "analysis": analysis})
    return {"results": results}
