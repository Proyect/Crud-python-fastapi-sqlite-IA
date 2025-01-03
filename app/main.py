from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Verify Influencers API"}

@app.get("/status")
def check_status():
    return {"status": "API is running smoothly!"}
