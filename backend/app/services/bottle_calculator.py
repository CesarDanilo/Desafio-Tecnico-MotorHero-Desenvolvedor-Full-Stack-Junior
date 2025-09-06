import math

def process(api_response: dict):
    """
    Ajusta dados da API da Valvoline e calcula frascos.
    Exemplo esperado:
    {
        "product": "Valvoline 5W30",
        "capacity_liters": 4.5,
        "bottle_size": 1
    }
    """
    product = api_response.get("product")
    liters = api_response.get("capacity_liters", 0)
    bottle_size = api_response.get("bottle_size", 1)

    bottles_needed = math.ceil(liters / bottle_size)

    return {
        "product": product,
        "capacity_liters": liters,
        "bottle_size": bottle_size,
        "bottles_needed": bottles_needed
    }
