from fastapi import FastAPI

from app.database import Base, engine
from app.models.user import User

app = FastAPI(
    title="StockWatch API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Welcome to StockWatch API 🚀"
    }