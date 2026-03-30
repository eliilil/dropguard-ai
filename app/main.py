from fastapi import FastAPI
from app.api import routes
from app.core.database import connect_to_mongo, close_mongo_connection

app = FastAPI(title="DropGuard AI Platform")

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.include_router(routes.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "DropGuard AI Engine is Online"}