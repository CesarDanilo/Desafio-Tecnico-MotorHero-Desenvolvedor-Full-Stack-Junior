from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from app.models import VehicleConsultRequest, ConsultResponse, VehicleConsultHistory
from app.services import valvoline, cache, bottle_calculator, extract_essential_data
from app.database import engine
from app.utils import plate_utils

router = APIRouter()


@router.post("/consult", response_model=ConsultResponse)
def consult_vehicle(data: VehicleConsultRequest):
    """
    Consulta informações de óleo do veículo a partir da placa.
    Fluxo:
      1. Normaliza e valida placa
      2. Consulta cache
      3. Se não tiver → consulta API da Valvoline
      4. Calcula frascos
      5. Salva histórico e retorna resultado
    """
    # 1 - Normalizar e validar placa
    plate = plate_utils.normalize_plate(data.plate)
    if not plate_utils.is_valid_plate(plate):
        raise HTTPException(status_code=400, detail="Placa inválida")

    # 2 - Buscar no cache
    cached = cache.get(plate)
    if cached:
        return ConsultResponse(
            source="cache",
            plate=plate,
            data=cached.get("vehicle_detail"),
            enriched_data=cached.get("enriched_data"),
        )

    try:
        # 3 - Consultar API da Valvoline
        api_response = valvoline.fetch_vehicle_data(plate)

        # 4 - Calcular frascos + extrair dados essenciais
        enriched_data = bottle_calculator.calculate_bottles(api_response)
        vehicle_detail = extract_essential_data.extract_data(api_response)

        # 5 - Salvar no cache
        cache.set(
            plate, {"vehicle_detail": vehicle_detail, "enriched_data": enriched_data}
        )

        # 6 - Salvar histórico no banco de dados
        with Session(engine) as session:
            history = VehicleConsultHistory(plate=plate)
            history.set_vehicle_data(vehicle_detail)
            history.set_enriched_data(enriched_data)
            session.add(history)
            session.commit()

        # 7 - Retorno
        return ConsultResponse(
            source="valvoline_api",
            plate=plate,
            data=vehicle_detail,
            enriched_data=enriched_data,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na consulta: {str(e)}")
