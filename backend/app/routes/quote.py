from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_quote():
    return {"message": "Rota de Quote funcionando!"}
