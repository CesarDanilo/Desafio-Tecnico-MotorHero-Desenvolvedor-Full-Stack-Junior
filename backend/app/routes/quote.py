from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_connection
from app.models import QuoteRequest
from app.models import QuoteRequest, QuoteItem, Customer, VehicleConsultRequest
from typing import List

router = APIRouter()

quotes_db: List[QuoteRequest] = []
vehicle_consults_db: List[VehicleConsultRequest] = []


@router.get("/")
async def get_quote():
    return quotes_db


@router.post("/")
async def post_quote(quote: QuoteRequest):
    quotes_db.append(quote)
    return {"message": "Quote created successfully", "quote": quote}
