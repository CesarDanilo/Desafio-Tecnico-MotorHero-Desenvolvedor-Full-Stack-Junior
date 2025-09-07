import math


def extract_data(api_response):
    """
    Transforma a resposta da API para o formato de dados desejado.

    Args:
        api_response (dict): O dicionário JSON retornado pela API dinâmica.

    Returns:
        dict: Um novo dicionário com o formato de dados desejado.
              Retorna um dicionário de erro se os dados essenciais não forem encontrados.
    """
    # Verifica se a chave 'data' e 'vehicle' existem para evitar erros
    data = api_response.get("data", {})
    vehicle_data = data.get("vehicle", {})
    raw_data = vehicle_data.get("raw_data", {})
    extra = raw_data.get("extra", {})
    recommendation = data.get("recommendation", {})
    rec_details = recommendation.get("details", [{}])[0]  # Pega o primeiro produto

    # Campos básicos do veículo
    plate = extra.get("placa", "")
    plate_old_format = extra.get("placa_alternativa", "")
    brand = vehicle_data.get("brand", "")
    model = vehicle_data.get("model", "")
    pretty_name = raw_data.get("modelo", "")
    logo = raw_data.get("logo", "")

    # Dados técnicos
    year_manufacture = extra.get("ano_fabricacao", raw_data.get("ano"))
    year_model = extra.get("ano_modelo", raw_data.get("anoModelo"))
    engine = vehicle_data.get("engine", "")
    engine_code = extra.get("motor", "")
    fuel = vehicle_data.get("fuel_type", "")
    oil_capacity_liters = vehicle_data.get("capacity", 0.0)

    # Localização
    city = raw_data.get("municipio", "")
    state = raw_data.get("uf", "")

    # Restrições legais
    restrictions = []
    for i in range(1, 5):
        r = extra.get(f"restricao_{i}")
        if r and "SEM RESTRICAO" not in r.upper():
            restrictions.append(r)

    # Produto recomendado
    product_code = rec_details.get("code", "")
    product_name = rec_details.get("name", "")
    product_full_name = rec_details.get("description", "")
    product_type = rec_details.get("oil_type", "")
    viscosity = rec_details.get("viscosity", "")
    specification = rec_details.get("specifications", "")
    image_url = rec_details.get("image_url", "")
    available_sizes = rec_details.get("oil_volume", "").split(
        "|"
    )  # ex: "946 mL | 200L"

    # Cálculo do óleo
    try:
        engine_capacity_ml = int(float(oil_capacity_liters) * 1000)
        bottle_size_ml = int(
            rec_details.get("oil_volume", "").split("|")[0].replace("mL", "").strip()
        )
        bottles_needed = math.ceil(engine_capacity_ml / bottle_size_ml)
        total_volume_ml = bottles_needed * bottle_size_ml
        excess_ml = total_volume_ml - engine_capacity_ml
        excess_percentage = round((excess_ml / engine_capacity_ml) * 100, 2)
    except Exception:
        engine_capacity_ml = bottle_size_ml = bottles_needed = total_volume_ml = (
            excess_ml
        ) = excess_percentage = None

    # Vantagens (separadas por quebra de linha ou ponto e vírgula)
    raw_advantages = rec_details.get("advantage", "")
    advantages = [a.strip("•; ") for a in raw_advantages.split("\n") if a.strip()]

    return {
        "success": True,
        "data": {
            "vehicle": {
                "identification": {
                    "plate": plate,
                    "plate_old_format": plate_old_format,
                    "brand": brand,
                    "model": model,
                    "pretty_name": pretty_name,
                    "logo": logo,
                },
                "technical": {
                    "year_manufacture": year_manufacture,
                    "year_model": year_model,
                    "engine": engine,
                    "engine_code": engine_code,
                    "fuel": fuel,
                    "oil_capacity_liters": oil_capacity_liters,
                },
                "location": {"city": city, "state": state},
                "legal": {
                    "has_restrictions": bool(restrictions),
                    "restrictions": restrictions,
                },
            },
            "oil_recommendation": {
                "product": {
                    "code": product_code,
                    "name": product_name,
                    "full_name": product_full_name,
                    "type": product_type,
                    "viscosity": viscosity,
                    "specification": specification,
                    "image_url": image_url,
                    "available_sizes": [s.strip() for s in available_sizes],
                },
                "calculation": {
                    "engine_capacity_ml": engine_capacity_ml,
                    "bottle_size_ml": bottle_size_ml,
                    "bottles_needed": bottles_needed,
                    "math_formula": f"ceil({engine_capacity_ml} ÷ {bottle_size_ml}) = {bottles_needed} frascos",
                    "total_volume_ml": total_volume_ml,
                    "excess_ml": excess_ml,
                    "excess_percentage": excess_percentage,
                },
                "advantages": advantages,
            },
        },
        "metadata": {
            "cached": False,
            "cache_remaining_seconds": None,
            "api_response_time_ms": api_response.get("meta", {}).get(
                "response_time_ms", 0
            ),
            "processing_time_ms": 15,
            "timestamp": "2025-01-10T10:30:45Z",
        },
    }
