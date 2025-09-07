from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, Dict, Any
from enum import Enum
from pydantic import BaseModel
import json


# -----------------------
# Enums
# -----------------------
class ItemType(str, Enum):
    oil = "oil"
    service = "service"
    part = "part"


class DiscountType(str, Enum):
    percentage = "percentage"
    fixed = "fixed"


# -----------------------
# Pydantic Models
# -----------------------
class VehicleConsultRequest(BaseModel):
    plate: str
    mechanic_id: str


class ConsultResponse(BaseModel):
    source: str
    plate: str
    data: Dict[str, Any]
    enriched_data: Dict[str, Any]


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
    vehicle_description: Optional[str] = None
    customer: CustomerRequest
    items: List[QuoteItemRequest]
    discount: Optional[DiscountRequest] = None


# -----------------------
# SQLModel Models
# -----------------------
class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    phone: str
    quotes: List["Quote"] = Relationship(back_populates="customer")


class Quote(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vehicle_plate: str
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.id")
    discount_type: Optional[DiscountType] = None
    discount_value: Optional[float] = None
    customer: Optional[Customer] = Relationship(back_populates="quotes")
    items: List["QuoteItem"] = Relationship(back_populates="quote")


class QuoteItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: ItemType
    code: Optional[str] = None
    description: str
    quantity: int
    unit_price: float
    quote_id: Optional[int] = Field(default=None, foreign_key="quote.id")
    quote: Optional[Quote] = Relationship(back_populates="items")


class VehicleConsultHistory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    plate: str
    vehicle_data_json: str
    enriched_data_json: str

    def set_vehicle_data(self, data: Dict[str, Any]):
        self.vehicle_data_json = json.dumps(data)

    def get_vehicle_data(self) -> Dict[str, Any]:
        return json.loads(self.vehicle_data_json)

    def set_enriched_data(self, data: Dict[str, Any]):
        self.enriched_data_json = json.dumps(data)

    def get_enriched_data(self) -> Dict[str, Any]:
        return json.loads(self.enriched_data_json)
