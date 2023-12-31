import json
import random
import requests
from algoritmos.data_handling import codigos_criterios

utilidades = [0.2, 0.3, 0.5, 0.4]
puntajes_ejercicios = {"E10": 0.2, "E20": 0.4, "E30": 0.4, "E40": 0.6}

# 20 puntajes
P = {int(c): 100 * random.random() for c in codigos_criterios}

content = {
    "utilidades": utilidades,
    "puntajes_ejercicios": puntajes_ejercicios,
    "puntajes": P,
}
json = json.dumps(content)

# Realiza una solicitud POST a la ruta /recomendar_ejercicios
url = "http://localhost:5000/actualizar_datos"
response = requests.post(url, json=json, timeout=60)

# Mostrar respuesta

# Verifica si la solicitud fue exitosa e imprime la respuesta
if response.status_code == 200:
    data = response.json()
    print("Respuesta de /actualizar_datos:")
    print(data)
else:
    print("Error en la solicitud a /actualizar_datos:", response.status_code)
