from fastapi import FastAPI

from app.database import Base, engine
from app.models.user import User
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router   

app = FastAPI(
    title="StockWatch API",
    version="1.0.0",
    description="Backend API for StockWatch"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(users_router)   


@app.get("/")
def root():
    return {
        "message": "Welcome to StockWatch API 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }