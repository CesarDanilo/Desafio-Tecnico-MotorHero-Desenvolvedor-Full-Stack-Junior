from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.services import valvoline, cache, bottle_calculator, extract_essential_data
from app.database import engine
from app.utils import plate_utils
from app.models import VehicleConsultRequest, ConsultResponse, Consultation
from datetime import datetime

router = APIRouter()


@router.get("/consultations", response_model=list[Consultation])
def get_consultations():
    try:
        with Session(engine) as session:
            statement = select(Consultation)
            results = session.exec(statement).all()

            if not results:
                raise HTTPException(
                    status_code=404, detail="Nenhuma consulta encontrada"
                )

            return results
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao buscar consultas: {str(e)}"
        )


@router.post("/consult", response_model=ConsultResponse)
def consult_vehicle(data: VehicleConsultRequest):

    plate = plate_utils.normalize_plate(data.plate)
    if not plate_utils.is_valid_plate(plate):
        raise HTTPException(status_code=400, detail="Placa inválida")

    # 🔹 Verifica cache
    cached = cache.get(plate)
    if cached:
        return ConsultResponse(
            source="cache",
            plate=plate,
            data=cached.get("vehicle_detail"),
            enriched_data=cached.get("enriched_data"),
        )

    try:
        # 🔹 Busca dados na API
        api_response = valvoline.fetch_vehicle_data(plate)
        enriched_data = bottle_calculator.calculate_bottles(api_response)
        vehicle_detail = extract_essential_data.extract_data(api_response)

        # 🔹 Salva no cache
        cache.set(
            plate, {"vehicle_detail": vehicle_detail, "enriched_data": enriched_data}
        )

        # 🔹 Extrair dados corretos do JSON
        vehicle_info = vehicle_detail["data"]["vehicle"]
        identification = vehicle_info.get("identification", {})
        technical = vehicle_info.get("technical", {})
        location = vehicle_info.get("location", {})
        legal = vehicle_info.get("legal", {})
        oil_product = vehicle_info.get("oil_recommendation", {}).get("product", {})

        with Session(engine) as session:
            consultation = Consultation(
                plate=data.plate,
                plate_normalized=plate,
                brand=identification.get("brand"),
                model=identification.get("model"),
                year_manufacture=int(technical.get("year_manufacture") or 0),
                year_model=int(technical.get("year_model") or 0),
                engine=technical.get("engine"),
                fuel_type=technical.get("fuel"),
                oil_capacity=float(technical.get("oil_capacity_liters") or 0),
                oil_code=enriched_data.get("oil_code") or oil_product.get("code") or "",
                oil_name=oil_product.get("name"),
                bottles_calculated=int(enriched_data.get("bottles_needed") or 0),
                bottle_size_ml=int(enriched_data.get("bottle_size_ml") or 0),
                excess_ml=int(enriched_data.get("excess_ml") or 0),
                city=location.get("city"),
                state=location.get("state"),
                has_restrictions=legal.get("has_restrictions"),
                restrictions=", ".join(legal.get("restrictions") or []),
                mechanic_id=data.mechanic_id,
                cached=False,
                created_at=datetime.utcnow(),
            )

            session.add(consultation)
            session.commit()
            session.refresh(consultation)

        return ConsultResponse(
            source="valvoline_api",
            plate=plate,
            data=vehicle_detail,
            enriched_data=enriched_data,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na consulta: {str(e)}")
