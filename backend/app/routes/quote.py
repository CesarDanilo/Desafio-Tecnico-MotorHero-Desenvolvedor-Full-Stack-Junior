from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from typing import List, Optional
from app.database import engine  # Certifique de ter o engine configurado em database.py
from app.models import (
    Quote,
    QuoteItem,
    Customer,
    QuoteRequest,
    QuoteItemRequest,
    CustomerRequest,
    DiscountRequest,
    ItemType,
    DiscountType,
)

router = APIRouter()


# ===== GET QUOTES =====
@router.get("/", response_model=List[QuoteRequest])
async def get_quote():
    """
    📌 Listar todos os orçamentos (Quotes)

    Este endpoint retorna a lista completa de orçamentos cadastrados no sistema.

    ### Retorno:

    - Uma lista de objetos **QuoteRequest**, cada um contendo:
        - **vehicle_plate** (str): Placa do veículo.
        - **customer** (obj):
            - **name** (str): Nome do cliente.
            - **phone** (str): Telefone do cliente.
        - **items** (lista de objetos): Lista de itens do orçamento.
            - **type** (str): Tipo do item (`oil`, `service`, `part`).
            - **code** (str, opcional): Código do item.
            - **description** (str): Descrição do item.
            - **quantity** (int): Quantidade do item.
            - **unit_price** (float): Preço unitário do item.
        - **discount** (obj, opcional):
            - **type** (str): Tipo de desconto (`percentage` ou `fixed`).
            - **value** (float): Valor do desconto.
    """
    with Session(engine) as session:
        quotes = session.exec(select(Quote)).all()
        result = []

        for q in quotes:
            session.refresh(q)
            items = [
                {
                    "type": i.type,
                    "code": i.code,
                    "description": i.description,
                    "quantity": i.quantity,
                    "unit_price": i.unit_price,
                }
                for i in q.items
            ]
            discount = None
            if q.discount_type and q.discount_value is not None:
                discount = {"type": q.discount_type, "value": q.discount_value}

            result.append(
                {
                    "vehicle_plate": q.vehicle_plate,
                    "customer": {"name": q.customer.name, "phone": q.customer.phone},
                    "items": items,
                    "discount": discount,
                }
            )
        return result


# ===== POST QUOTE =====
@router.post("/", response_model=dict)
async def post_quote(quote: QuoteRequest):
    """
    📌 Criar um novo orçamento (Quote)

    Este endpoint recebe os dados de um orçamento de veículo e salva no banco de dados.

    ### Estrutura do JSON esperado:
    (exemplo idêntico ao seu)
    """
    with Session(engine) as session:
        # Salvar cliente
        customer = Customer(name=quote.customer.name, phone=quote.customer.phone)
        session.add(customer)
        session.commit()
        session.refresh(customer)

        # Salvar orçamento
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

        # Salvar itens
        for item in quote.items:
            item_db = QuoteItem(
                type=item.type,
                code=item.code,
                description=item.description,
                quantity=item.quantity,
                unit_price=item.unit_price,
                quote_id=quote_db.id,
            )
            session.add(item_db)
        session.commit()

        return {"message": "Quote created successfully", "quote_id": quote_db.id}
