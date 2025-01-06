from fastapi import FastAPI
from app.routers import influencers, claims
from app.routers import claims_openai

app = FastAPI(title="Verify Influencers API")

#rutas de comentarios
app.include_router(claims.router, prefix="/api", tags=["Claims"])

# Incluir rutas desde influencers
app.include_router(influencers.router, prefix="/api", tags=["Influencers"])

#open ai
app.include_router(claims_openai.router, prefix="/api", tags=["AI Claims Analysis"])

#app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Verify Influencers API"}

@app.get("/status")
def check_status():
    return {"status": "API is running smoothly!"}
