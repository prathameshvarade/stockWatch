from app.database import engine
from fastapi import FastAPI
from app.config import settings

app = FastAPI()


@app.get("/")
def root():
    print(engine)
    return {
        "database": settings.DATABASE_URL
    }
