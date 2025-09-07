import re


def normalize_plate(plate: str) -> str:

    return plate.strip().upper()


def is_valid_plate(plate: str) -> bool:

    pattern = r"^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$"
    return bool(re.match(pattern, plate))
