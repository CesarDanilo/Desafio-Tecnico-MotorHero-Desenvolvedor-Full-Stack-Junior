import re

def normalize_plate(plate: str) -> str:
    """Remove espaços e transforma em maiúsculo"""
    return plate.strip().upper()

def is_valid_plate(plate: str) -> bool:
    """
    Valida formato de placa brasileira (AAA1234 ou ABC1D23 - Mercosul)
    """
    pattern = r"^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$"
    return bool(re.match(pattern, plate))
