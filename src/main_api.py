from fastapi import FastAPI
from src.api.endpoints.message_endpoint import router

app = FastAPI(
    title="Sushi Parking Assistant API",
    description="API for finding sushi restaurants and parking spots in Munich",
    version="1.0.0"
)

app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)