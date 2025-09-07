from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from datetime import datetime, date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from typing import List
from app.models import QuoteRequest, QuoteItemRequest, Quote, Consultation
from app.database import engine
import random

router = APIRouter()


@router.post("/create")
def create_quote(quote_request: QuoteRequest):
    """
    Cria um orçamento com base nos itens e veículo informado.
    """
    try:
        # 🔹 Gerar número do orçamento
        quote_number = (
            f"Q{datetime.utcnow().strftime('%Y%m%d%H%M%S')}{random.randint(100, 999)}"
        )

        # 🔹 Buscar dados do veículo no banco (Consultation)
        plate = quote_request.plate
        vehicle_description = None
        if plate:
            with Session(engine) as session:
                statement = select(Consultation).where(
                    Consultation.plate_normalized == plate
                )
                vehicle_data = session.exec(statement).first()
                if vehicle_data:
                    vehicle_description = f"{vehicle_data.brand or ''} {vehicle_data.model or ''} {vehicle_data.year_model or ''}".strip()

        # 🔹 Calcular subtotal
        subtotal = Decimal(0)
        items_data = []
        for item in quote_request.items:
            item_total = Decimal(item.unit_price) * Decimal(item.quantity)
            subtotal += item_total
            items_data.append(
                {
                    "type": item.type,
                    "description": item.description,
                    "code": item.code,
                    "quantity": item.quantity,
                    "unit_price": item.unit_price,
                    "total": float(item_total),
                }
            )

        # 🔹 Aplicar desconto
        discount_percentage = Decimal(quote_request.discount_percentage or 0)
        discount_amount = (subtotal * discount_percentage / Decimal(100)).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        total = (subtotal - discount_amount).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

        # 🔹 Salvar orçamento no banco
        with Session(engine) as session:
            quote = Quote(
                quote_number=quote_number,
                plate=plate,
                vehicle_description=vehicle_description,
                customer_name=quote_request.customer_name,
                customer_phone=quote_request.customer_phone,
                items=items_data,
                subtotal=float(subtotal),
                discount_percentage=float(discount_percentage),
                discount_amount=float(discount_amount),
                total=float(total),
                mechanic_id=quote_request.mechanic_id,
                status="active",
                created_at=datetime.utcnow(),
                valid_until=date.today()
                + timedelta(days=7),  # orçamento válido por 7 dias
            )
            session.add(quote)
            session.commit()
            session.refresh(quote)

        return {"success": True, "quote": quote}

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao criar orçamento: {str(e)}"
        )
