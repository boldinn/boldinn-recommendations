from algoritmos.recomendaciones import recomendar_ejercicios
import random
from algoritmos.data_handling import codigos_criterios

# Generar un caso

# 20 puntajes
P = {int(c): 100 * random.random() for c in codigos_criterios}

# ejercicios resueltos
ej = ["E1", "E3", "E5", "E7"]

# Prueba
print("Puntajes:", P)
print("Ejercicios resueltos:", ej)

R = recomendar_ejercicios(P, ej, 3)
print("\n\n")
template = f"""***RUTA EJERCICIOS RECOMENDADOS***:
{R}
"""
print(template)
