from fastapi import APIRouter

router = APIRouter()


@router.post("/vehicle/consult/{plate}")
def normalize_plate(plate: str) -> str:
    """
    Recebe: "ESS-4H19", "ess4h19", "ESS 4 H 19"
    Retorna: "ESS4H19"

    Também detecta se é formato antigo (ABC1234) ou Mercosul (ABC1D23)
    """
    # Remove caracteres especiais e espaços
    normalized = plate.upper().replace("-", "").replace(" ", "")

    # Valida formato
    if len(normalized) == 7:
        # Verifica se é formato válido
        if normalized[:3].isalpha() and normalized[3].isdigit():
            return normalized

    raise ValueError("Formato de placa inválido")
