from fastapi import FastAPI
from app.routes import vehicle
from app.routes import quote
from app.database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MotorHero API")

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],         
    allow_headers=["*"],         
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(vehicle.router, prefix="/api/vehicle", tags=["vehicle"])
app.include_router(quote.router, prefix="/api/quote", tags=["quote"])
