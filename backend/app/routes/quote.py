from fastapi import APIRouter, Query
from sqlmodel import Session, select
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from typing import List, Optional
from app.database import engine
from app.models import QuoteRequest, Customer, Quote, QuoteItem, DiscountType

router = APIRouter()


@router.get("/", response_model=List[dict])
def get_quotes(
    vehicle_plate: Optional[str] = Query(
        None, description="Filtrar por placa do veículo"
    ),
    mechanic_id: Optional[str] = Query(None, description="Filtrar por ID do mecânico"),
):
    """
    📌 Listar todos os orçamentos (Quotes)

    Permite filtrar por placa do veículo e por ID do mecânico.
    """
    results = []
    with Session(engine) as session:
        query = select(Quote).join(Customer)

        if vehicle_plate:
            query = query.where(Quote.vehicle_plate == vehicle_plate)

        quotes = session.exec(query).all()

        for quote in quotes:
            # Se filtrar por mecânico, precisamos buscar na tabela VehicleConsultHistory
            if mechanic_id:
                consults = session.exec(
                    "SELECT * FROM VehicleConsultHistory WHERE plate=:plate AND mechanic_id=:mechanic",
                    {"plate": quote.vehicle_plate, "mechanic": mechanic_id},
                ).all()
                if not consults:
                    continue

            results.append(
                {
                    "quote_id": quote.id,
                    "vehicle_plate": quote.vehicle_plate,
                    "customer": {
                        "name": quote.customer.name,
                        "phone": quote.customer.phone,
                    },
                    "discount_type": quote.discount_type,
                    "discount_value": quote.discount_value,
                    "items": [
                        {
                            "type": item.type,
                            "code": item.code,
                            "description": item.description,
                            "quantity": item.quantity,
                            "unit_price": item.unit_price,
                        }
                        for item in quote.items
                    ],
                }
            )

    return results


@router.post("/create", response_model=dict)
async def post_quote(quote: QuoteRequest):
    with Session(engine) as session:
        # ===== Salvar cliente =====
        customer = Customer(name=quote.customer.name, phone=quote.customer.phone)
        session.add(customer)
        session.commit()
        session.refresh(customer)

        # ===== Salvar orçamento =====
        discount_type = quote.discount.type if quote.discount else None
        discount_value = quote.discount.value if quote.discount else None
        quote_db = Quote(
            vehicle_plate=quote.vehicle_plate,
            customer_id=customer.id,
            discount_type=discount_type,
            discount_value=discount_value,
        )
        session.add(quote_db)
        session.commit()
        session.refresh(quote_db)

        # ===== Gerar número do orçamento baseado no ID =====
        quote_number = f"ORC-2025-{quote_db.id:05d}"

        # ===== Salvar itens e calcular subtotal =====
        subtotal = Decimal("0.00")
        items_detail = []

        for idx, item in enumerate(quote.items, start=1):
            item_subtotal = Decimal(item.unit_price) * item.quantity
            subtotal += item_subtotal

            item_db = QuoteItem(
                type=item.type,
                code=item.code,
                description=item.description,
                quantity=item.quantity,
                unit_price=item.unit_price,
                quote_id=quote_db.id,
            )
            session.add(item_db)

            items_detail.append(
                {
                    "item": idx,
                    "description": item.description,
                    "quantity": item.quantity,
                    "unit": "UN" if item.type == "oil" else "SV",
                    "unit_price": float(
                        Decimal(item.unit_price).quantize(
                            Decimal("0.01"), rounding=ROUND_HALF_UP
                        )
                    ),
                    "subtotal": float(
                        item_subtotal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                    ),
                }
            )

        session.commit()

        # ===== Totais =====
        discount_percentage = (
            quote.discount.value
            if quote.discount and quote.discount.type == DiscountType.percentage
            else 0
        )
        discount_amount = (subtotal * Decimal(discount_percentage) / 100).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        final_total = (subtotal - discount_amount).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

        # ===== Datas =====
        today = date.today()
        valid_until = today + timedelta(days=7)

        # ===== Link para WhatsApp =====
        whatsapp_number = quote.customer.phone
        whatsapp_link = (
            f"https://wa.me/55{whatsapp_number}?text=Orcamento%20{quote_number}"
        )

        # ===== Retorno detalhado =====
        return {
            "quote": {
                "number": quote_number,
                "date": today.isoformat(),
                "valid_until": valid_until.isoformat(),
                "status": "active",
            },
            "vehicle": {
                "plate": quote.vehicle_plate,
                "description": quote.vehicle_description or "Descrição não cadastrada",
            },
            "customer": {"name": quote.customer.name, "phone": quote.customer.phone},
            "items_detail": items_detail,
            "totals": {
                "subtotal": float(subtotal),
                "discount_percentage": discount_percentage,
                "discount_amount": float(discount_amount),
                "final_total": float(final_total),
            },
            "share": {"whatsapp_link": whatsapp_link},
        }
