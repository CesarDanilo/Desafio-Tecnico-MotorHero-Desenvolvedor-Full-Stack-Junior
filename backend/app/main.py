from fastapi import FastAPI
from .routes.vehicle import router

app = FastAPI()
app.include_router(router, prefix="/api")
