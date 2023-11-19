

import json,random
import requests
from data_handling import  codigos_criterios

# Generar un caso

# 20 puntajes
P={int(c): 100*random.random() for c in codigos_criterios}

# ejercicios resueltos
ej=['E1','E3','E5','E7']

# Prueba
print('Puntajes:',P)
print('Ejercicios resueltos:', ej)

content={'puntajes':P, 'ejercicios_resueltos':ej}
json=json.dumps(content)
#print(json)
# Realiza una solicitud POST a la ruta /recomendar_ejercicios
url = "http://localhost:5000/recomendar_ejercicios"
response = requests.post(url, json=json)

# Mostrar respuesta

# Verifica si la solicitud fue exitosa e imprime la respuesta
if response.status_code == 200:
    data = response.json()
    print("Respuesta de /recomendar_ejercicios:")
    print(data)
else:
    print("Error en la solicitud a /recomendar_ejercicios:", response.status_code)

