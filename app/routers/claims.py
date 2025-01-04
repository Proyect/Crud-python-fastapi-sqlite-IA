from fastapi import APIRouter
from typing import List
from app.services.verify_claims import process_claims

router = APIRouter()

@router.post("/claims/verify", summary="Verify health claims")
def verify_claims(claims: List[str]):
    results = process_claims(claims)
    return {"verified_claims": results}
