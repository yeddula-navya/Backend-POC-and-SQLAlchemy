from fastapi import FastAPI
from app.routers.user_router import router as user_router
from app.database.postgres import engine
from app.db.base import Base

app = FastAPI(
    title="Backend POC",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
app.include_router(user_router)

@app.get("/health")
def health_check():
    return {
        "status": 200,
        "message": "Backend is running",
        "data": None
    }