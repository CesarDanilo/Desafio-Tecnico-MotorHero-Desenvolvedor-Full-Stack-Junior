from fastapi import APIRouter, HTTPException
from app.models import VehicleConsultRequest
from app.services import valvoline, cache, bottle_calculator
from app.utils import plate_utils

router = APIRouter()

@router.post("/consult")
def consult_vehicle(data: VehicleConsultRequest):
    """
    Consulta informações de óleo do veículo a partir da placa.
    Fluxo:
      1. Normaliza e valida placa
      2. Consulta cache
      3. Se não tiver → consulta API da Valvoline
      4. Calcula frascos
      5. Retorna resultado
    """

    # 1 - Normalizar e validar placa
    plate = plate_utils.normalize_plate(data.plate)
    if not plate_utils.is_valid_plate(plate):
        raise HTTPException(status_code=400, detail="Placa inválida")

    # 2 - Tentar buscar no cache
    cached_data = cache.get(plate)
    if cached_data:
        return {
            "source": "cache",
            "plate": plate,
            "data": cached_data
        }

    try:
        # 3 - Consultar API da Valvoline
        api_response = valvoline.fetch_vehicle_data(plate)

        # 4 - Calcular frascos
        enriched_data = bottle_calculator.calculate_bottles(api_response)

        # 5 - Salvar no cache
        cache.set(plate, enriched_data)

        return {
            "source": "valvoline_api",
            "plate": plate,
            "data": enriched_data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na consulta: {str(e)}")
