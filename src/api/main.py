from fastapi import FastAPI
from src.api.routers.query import router as query_router

app = FastAPI()

app.include_router(query_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}