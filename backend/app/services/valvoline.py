import requests

URL = "https://valvoline-oil-backend.pecapecas.com.br/api/v1/oil/plate-search"

def fetch_vehicle_data(plate: str):
    payload = {"plate": plate, "component_type": "MOTOR"}
    headers = {"Content-Type": "application/json"}
    response = requests.post(URL, json=payload, headers=headers, timeout=5)
    response.raise_for_status()
    return response.json() #aqui ela vai me retornar todos os dados da api que estamos consultando 
