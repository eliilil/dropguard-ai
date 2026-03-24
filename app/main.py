from fastapi import FastAPI
from app.core.database import connect_to_mongo, close_mongo_connection
from app.api import routes

app = FastAPI(title="DropGuard AI Platform")

# Lifecycle Events
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

# Include Routes
app.include_router(routes.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "DropGuard AI Engine is Online"}