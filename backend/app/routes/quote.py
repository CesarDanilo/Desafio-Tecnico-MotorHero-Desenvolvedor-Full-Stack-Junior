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

    ### Exemplo de retorno:

    ```json
    [
      {
        "vehicle_plate": "ABC1234",
        "customer": {
          "name": "César",
          "phone": "11999999999"
        },
        "items": [
          {
            "type": "oil",
            "code": "OIL123",
            "description": "Óleo sintético 5W30",
            "quantity": 1,
            "unit_price": 120.5
          }
        ],
        "discount": {
          "type": "percentage",
          "value": 10
        }
      }
    ]
    """
    return quotes_db



@router.post("/")
async def post_quote(quote: QuoteRequest):
    """
    📌 Criar um novo orçamento (Quote)

    Este endpoint recebe os dados de um orçamento de veículo e salva em memória.
    Ele espera receber um JSON com as informações do veículo, cliente, itens e desconto.

    ### Estrutura do JSON esperado:

    ```json
    {
      "vehicle_plate": "ABC1234",
      "customer": {
        "name": "César",
        "phone": "11999999999"
      },
      "items": [
        {
          "type": "oil",
          "code": "OIL123",
          "description": "Óleo sintético 5W30",
          "quantity": 1,
          "unit_price": 120.5
        }
      ],
      "discount": {
        "type": "percentage",
        "value": 10
      }
    }
    ```

    ### Campos:

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

    ### Retorno:

    - **message** (str): Mensagem de confirmação.
    - **quote** (obj): Dados do orçamento criado.
    """
    quotes_db.append(quote)
    return {"message": "Quote created successfully", "quote": quote}

