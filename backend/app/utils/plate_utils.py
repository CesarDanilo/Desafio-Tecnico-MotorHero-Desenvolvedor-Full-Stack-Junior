import re


def normalize_plate(plate: str) -> str:
    """
    Normaliza a placa removendo espaços e convertendo para maiúsculas.
    """
    return re.sub(r"[^A-Z0-9]", "", plate.strip().upper())


def is_valid_plate(plate: str) -> bool:
    normalized = normalize_plate(plate)

    if len(normalized) != 7:
        return False

    old_format = r"^[A-Z]{3}[0-9]{4}$"

    mercosul_format = r"^[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}$"

    return bool(re.match(old_format, normalized)) or bool(
        re.match(mercosul_format, normalized)
    )
