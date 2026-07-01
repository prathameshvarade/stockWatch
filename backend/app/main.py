from fastapi import FastAPI

app = FastAPI(
    title="Stock Price Tracker API",
    version="1.0.0",
    description="Backend API for the Stock Price Tracker project."
)


@app.get("/")
def root():
    return {
        "message": "Stock Price Tracker API is running!"
    }