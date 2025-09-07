from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_connection  # função para pegar a sessão do banco
from app.models import QuoteRequest  # vamos criar um modelo para resposta

router = APIRouter()

@router.get("/")
async def get_quote():
    return {"success": True, "message": "Rota de Quote funcionando!"}


@router.post("/")
async def post_quote(quote: QuoteRequest):
    # Cálculo total
    subtotal = sum(item.quantity * item.unit_price for item in quote.items)

    discount_value = 0
    if quote.discount:
        if quote.discount.type == "percentage":
            discount_value = subtotal * (quote.discount.value / 100)
        else:
            discount_value = quote.discount.value

    total = subtotal - discount_value

    return {
        "success": True,
        "data": {
            "vehicle_plate": quote.vehicle_plate,
            "customer": quote.customer,
            "items": quote.items,
            "subtotal": round(subtotal, 2),
            "discount": {
                "type": quote.discount.type if quote.discount else None,
                "value": quote.discount.value if quote.discount else 0,
            },
            "total": round(total, 2),
        },
    }