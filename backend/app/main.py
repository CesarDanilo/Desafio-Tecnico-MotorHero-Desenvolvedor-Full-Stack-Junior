from fastapi import FastAPI
from app.routes import vehicle, analytics, quote

app = FastAPI(title="MotorHero API")

# Registrar rotas
app.include_router(vehicle.router, prefix="/api/vehicle", tags=["vehicle"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])
app.include_router(quote.router, prefix="/api/quote", tags=["quote"])
