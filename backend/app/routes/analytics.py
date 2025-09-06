from fastapi import APIRouter
from app.models import AnalyticsResponse

router = APIRouter()

@router.get("/dashboard", response_model=AnalyticsResponse)
def get_dashboard():
    """
    Endpoint que retorna métricas básicas para o dashboard.
    (Aqui por enquanto é mockado, depois você conecta no banco)
    """
    return {
        "total_consults": 10,
        "total_quotes": 5,
        "most_consulted_vehicle": "Fiat Uno 1.0"
    }
