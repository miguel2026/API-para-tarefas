from fastapi import FastAPI
from API.Presentation.routes import router as routes

app = FastAPI(
    title="Trabalho GB",
    description="API para o trabalho de GB",
    version="1.0.0",
)

app.include_router(routes)