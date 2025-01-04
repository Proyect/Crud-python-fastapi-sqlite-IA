from fastapi import FastAPI
from app.routers import influencers, claims

app = FastAPI(title="Verify Influencers API")

#rutas de comentarios
app.include_router(claims.router, prefix="/api", tags=["Claims"])

# Incluir rutas desde influencers
app.include_router(influencers.router, prefix="/api", tags=["Influencers"])

#app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Verify Influencers API"}

@app.get("/status")
def check_status():
    return {"status": "API is running smoothly!"}
