from pydantic import BaseModel
from typing import List, Optional, Literal


class VehicleConsultRequest(BaseModel):
    plate: str
    mechanic_id: str


class QuoteItem(BaseModel):
    type: Literal["oil", "service", "part"]  # restringe tipos válidos
    code: Optional[str] = None
    description: str
    quantity: int
    unit_price: float


class Discount(BaseModel):
    type: Literal["percentage", "fixed"]
    value: float


class AnalyticsResponse(BaseModel):
    total_consults: int
    total_quotes: int
    most_consulted_vehicle: Optional[str] = None


class Customer(BaseModel):
    name: str
    phone: str


class QuoteRequest(BaseModel):
    vehicle_plate: str
    customer: Customer
    items: List[QuoteItem]
    discount: Optional[Discount] = None
