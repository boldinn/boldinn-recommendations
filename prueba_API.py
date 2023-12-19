import json
import requests

content = {
    "desafio": 1,
    "tamaño_grupo": 8,
    "id_org": 12,
    "include": [150, 100],
    "discard": [206, 207],
    "history": [[150, 100, 176, 155], [150, 100, 176, 148]],
    "position": None,
    "knowledge": None,
    "area": ["Grupo 2", "Grupo 1", "Grupo 6"],
    "n_rec": 6,  # número de recomendaciones deseadas
}
JSON = json.dumps(content)

url = "http://localhost:5000/recomendar_grupos"
response = requests.post(url, json=JSON, timeout=60)
data = response.json()
print(
    f"""--------------------------
***RESPUESTA recomendar_grupos***:
{data}"""
)
