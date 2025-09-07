from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel

class VehicleConsultRequest(BaseModel):
    plate: str
    mechanic_id: str

# Enum para tipos
class ItemType(str, Enum):
    oil = "oil"
    service = "service"
    part = "part"

class DiscountType(str, Enum):
    percentage = "percentage"
    fixed = "fixed"

# Cliente
class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    phone: str
    quotes: List["Quote"] = Relationship(back_populates="customer")

# Orçamento
class Quote(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vehicle_plate: str
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.id")
    discount_type: Optional[DiscountType] = None
    discount_value: Optional[float] = None
    customer: Optional[Customer] = Relationship(back_populates="quotes")
    items: List["QuoteItem"] = Relationship(back_populates="quote")

# Itens do orçamento
class QuoteItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: ItemType
    code: Optional[str] = None
    description: str
    quantity: int
    unit_price: float
    quote_id: Optional[int] = Field(default=None, foreign_key="quote.id")
    quote: Optional[Quote] = Relationship(back_populates="items")


class CustomerRequest(BaseModel):
    name: str
    phone: str

class QuoteItemRequest(BaseModel):
    type: ItemType
    code: Optional[str] = None
    description: str
    quantity: int
    unit_price: float

class DiscountRequest(BaseModel):
    type: DiscountType
    value: float

class QuoteRequest(BaseModel):
    vehicle_plate: str
    customer: CustomerRequest
    items: List[QuoteItemRequest]
    discount: Optional[DiscountRequest] = None