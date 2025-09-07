from typing import Optional, Dict, Any
from datetime import datetime, date
from sqlmodel import SQLModel, Field, Column, JSON
from pydantic import BaseModel


class Consultation(SQLModel, table=True):
    __tablename__ = "consultations"

    id: Optional[int] = Field(default=None, primary_key=True)
    plate: str = Field(max_length=10, nullable=False)
    plate_normalized: str = Field(max_length=10, nullable=False, index=True)
    brand: Optional[str] = Field(default=None, max_length=50)
    model: Optional[str] = Field(default=None, max_length=100)
    year_manufacture: Optional[int] = None
    year_model: Optional[int] = None
    engine: Optional[str] = Field(default=None, max_length=20)
    fuel_type: Optional[str] = Field(default=None, max_length=20)
    oil_capacity: Optional[float] = None 
    oil_code: Optional[str] = Field(default=None, max_length=20)
    oil_name: Optional[str] = Field(default=None, max_length=100)
    bottles_calculated: Optional[int] = None
    bottle_size_ml: Optional[int] = None
    excess_ml: Optional[int] = None
    city: Optional[str] = Field(default=None, max_length=100)
    state: Optional[str] = Field(default=None, max_length=2)
    has_restrictions: Optional[bool] = None
    restrictions: Optional[str] = None
    mechanic_id: Optional[str] = Field(default=None, max_length=50, index=True)
    cached: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)


class Quote(SQLModel, table=True):
    __tablename__ = "quotes"

    id: Optional[int] = Field(default=None, primary_key=True)
    quote_number: str = Field(max_length=20, nullable=False, unique=True, index=True)
    plate: Optional[str] = Field(default=None, max_length=10)
    vehicle_description: Optional[str] = Field(default=None, max_length=200)
    customer_name: Optional[str] = Field(default=None, max_length=100)
    customer_phone: Optional[str] = Field(default=None, max_length=20)
    items: Optional[dict] = Field(default=None, sa_column=Column(JSON))
    subtotal: Optional[float] = None
    discount_percentage: Optional[float] = None
    discount_amount: Optional[float] = None
    total: Optional[float] = None
    mechanic_id: Optional[str] = Field(default=None, max_length=50)
    status: str = Field(default="active", max_length=20, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    valid_until: Optional[date] = None


class VehicleConsultRequest(BaseModel):
    plate: str
    mechanic_id: str


class ConsultResponse(BaseModel):
    source: str
    plate: str
    data: Dict[str, Any]
    enriched_data: Dict[str, Any]
