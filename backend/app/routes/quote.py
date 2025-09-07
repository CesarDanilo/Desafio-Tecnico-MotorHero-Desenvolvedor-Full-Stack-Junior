from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_connection  # função para pegar a sessão do banco
from app.models import QuoteRequest  # vamos criar um modelo para resposta
from app.models import QuoteRequest, QuoteItem, Customer,VehicleConsultRequest  # modelos SQLAlchemy
# from schemas import QuoteRequest, QuoteItem, Customer, Discount  # seus Pydantic models
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
