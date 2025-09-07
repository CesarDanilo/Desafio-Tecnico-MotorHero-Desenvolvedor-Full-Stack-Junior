# from fastapi import APIRouter, HTTPException
# from sqlmodel import Session, select
# from decimal import Decimal, ROUND_HALF_UP
# from datetime import date, timedelta
# from app.models import (
#     QuoteRequest,
#     QuoteItemRequest,
#     Quote,
#     QuoteItem,
#     Customer,
#     VehicleConsultHistory,
# )
# from app.database import engine
# from typing import List, Optional

# router = APIRouter()


# @router.post("/create")
# def create_quote(quote: QuoteRequest):
#     with Session(engine) as session:
#         # Salvar cliente
#         customer = Customer(name=quote.customer.name, phone=quote.customer.phone)
#         session.add(customer)
#         session.commit()
#         session.refresh(customer)

#         # Salvar orçamento
#         discount_type = quote.discount.type if quote.discount else None
#         discount_value = quote.discount.value if quote.discount else None

#         quote_db = Quote(
#             vehicle_plate=quote.vehicle_plate,
#             customer_id=customer.id,
#             discount_type=discount_type,
#             discount_value=discount_value,
#         )
#         session.add(quote_db)
#         session.commit()
#         session.refresh(quote_db)

#         # Gerar número do orçamento
#         quote_number = f"ORC-2025-{quote_db.id:05d}"

#         # Salvar itens e calcular subtotal
#         subtotal = Decimal("0.00")
#         items_detail = []

#         for idx, item in enumerate(quote.items, start=1):
#             item_subtotal = Decimal(item.unit_price) * item.quantity
#             subtotal += item_subtotal

#             item_db = QuoteItem(
#                 type=item.type,
#                 code=item.code,
#                 description=item.description,
#                 quantity=item.quantity,
#                 unit_price=item.unit_price,
#                 quote_id=quote_db.id,
#             )
#             session.add(item_db)

#             items_detail.append(
#                 {
#                     "item": idx,
#                     "description": item.description,
#                     "quantity": item.quantity,
#                     "unit": "UN" if item.type == "oil" else "SV",
#                     "unit_price": float(
#                         Decimal(item.unit_price).quantize(
#                             Decimal("0.01"), rounding=ROUND_HALF_UP
#                         )
#                     ),
#                     "subtotal": float(
#                         item_subtotal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
#                     ),
#                 }
#             )

#         session.commit()

#         # Totais
#         discount_percentage = (
#             quote.discount.value
#             if quote.discount and quote.discount.type == "percentage"
#             else 0
#         )
#         discount_amount = (subtotal * Decimal(discount_percentage) / 100).quantize(
#             Decimal("0.01"), rounding=ROUND_HALF_UP
#         )
#         final_total = (subtotal - discount_amount).quantize(
#             Decimal("0.01"), rounding=ROUND_HALF_UP
#         )

#         # Buscar descrição do veículo
#         vehicle_desc = None
#         history = session.exec(
#             select(VehicleConsultHistory).where(
#                 VehicleConsultHistory.plate == quote.vehicle_plate
#             )
#         ).first()
#         if history:
#             vehicle_desc = history.get_vehicle_data().get("description")

#         # Datas
#         today = date.today()
#         valid_until = today + timedelta(days=7)

#         # WhatsApp link
#         whatsapp_link = (
#             f"https://wa.me/55{quote.customer.phone}?text=Orcamento%20{quote_number}"
#         )

#         return {
#             "quote": {
#                 "number": quote_number,
#                 "date": today.isoformat(),
#                 "valid_until": valid_until.isoformat(),
#                 "status": "active",
#             },
#             "vehicle": {"plate": quote.vehicle_plate, "description": vehicle_desc},
#             "customer": {"name": quote.customer.name, "phone": quote.customer.phone},
#             "items_detail": items_detail,
#             "totals": {
#                 "subtotal": float(subtotal),
#                 "discount_percentage": discount_percentage,
#                 "discount_amount": float(discount_amount),
#                 "final_total": float(final_total),
#             },
#             "share": {"whatsapp_link": whatsapp_link},
#         }
