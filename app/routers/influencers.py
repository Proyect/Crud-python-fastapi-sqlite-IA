from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Define el router
router = APIRouter()

# Modelo de ejemplo para un influencer
class Influencer(BaseModel):
    name: str
    platform: str
    followers: int

# Datos simulados
influencers_db = [
    {"name": "John Doe", "platform": "Twitter", "followers": 100000},
    {"name": "Jane Smith", "platform": "Instagram", "followers": 250000},
]

@router.get("/influencers", summary="Get all influencers")
def get_influencers():
    return {"influencers": influencers_db}

@router.get("/influencers/{name}", summary="Get influencer by name")
def get_influencer(name: str):
    influencer = next((i for i in influencers_db if i["name"].lower() == name.lower()), None)
    if not influencer:
        raise HTTPException(status_code=404, detail="Influencer not found")
    return influencer

@router.post("/influencers", summary="Add a new influencer")
def add_influencer(influencer: Influencer):
    influencers_db.append(influencer.dict())
    return {"message": "Influencer added successfully", "influencer": influencer}
