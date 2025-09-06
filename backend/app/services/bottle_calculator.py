import math


def calculate_bottles(api_response):
    """
    LÓGICA DE CÁLCULO DE FRASCOS - Versão segura
    """

    # 1. Extrair dados de forma segura usando .get()
    data = api_response.get("data", {})
    capacity_liters = data.get("vehicle", {}).get("capacity")
    details_list = data.get("recommendation", {}).get("details", [])

    # 2. VALIDAR se os dados necessários existem
    if not capacity_liters:
        raise ValueError("Capacidade do veículo não encontrada na resposta da API.")

    # ESTA É A CORREÇÃO PRINCIPAL!
    if not details_list:
        raise ValueError(
            "Nenhuma recomendação de óleo (details) foi encontrada para este veículo."
        )

    # 3. Prosseguir com a lógica, agora com segurança
    oil_volume_str = details_list[0].get("oil_volume")
    if not oil_volume_str:
        raise ValueError("Informação 'oil_volume' não encontrada dentro de 'details'.")

    capacity_ml = capacity_liters * 1000

    bottle_size_str = oil_volume_str.split("|")[0].strip()

    # Adicionar uma verificação para o caso de não haver dígitos
    digits_in_bottle_size = "".join(filter(str.isdigit, bottle_size_str))
    if not digits_in_bottle_size:
        raise ValueError(
            f"Não foi possível extrair um tamanho de frasco numérico de '{bottle_size_str}'."
        )

    bottle_size_ml = int(digits_in_bottle_size)
    if bottle_size_ml == 0:
        raise ValueError("Tamanho do frasco calculado como zero, impossível dividir.")

    bottles_needed = math.ceil(capacity_ml / bottle_size_ml)

    total_volume_ml = bottles_needed * bottle_size_ml
    excess_ml = total_volume_ml - capacity_ml
    excess_percentage = (excess_ml / capacity_ml) * 100

    return {
        "engine_capacity_ml": capacity_ml,
        "bottle_size_ml": bottle_size_ml,
        "bottles_needed": bottles_needed,
        "math_formula": f"ceil({capacity_ml} ÷ {bottle_size_ml}) = {bottles_needed} frascos",
        "total_volume_ml": total_volume_ml,
        "excess_ml": excess_ml,
        "excess_percentage": round(excess_percentage, 2),
    }
