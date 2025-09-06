from pydantic import BaseModel
from typing import List, Optional


class VehicleConsultRequest(BaseModel):
    plate: str
    mechanic_id: str


class QuoteItem(BaseModel):
    type: str
    code: Optional[str] = None
    description: str
    quantity: int
    unit_price: float


class AnalyticsResponse(BaseModel):
    total_consults: int
    total_quotes: int
    most_consulted_vehicle: Optional[str] = None
