
import pandas as pd
from recomendaciones import recomendar_ejercicios
import random
from data_handling import ejercicios_df, codigos_criterios

# Generar un caso

# 20 puntajes
P={int(c): 100*random.random() for c in codigos_criterios}

# ejercicios resueltos
ej=['E1','E3','E5','E7']

# Prueba
print('Puntajes:',P)
print('Ejercicios resueltos:', ej)

R=recomendar_ejercicios(P,ej)
print('\n\n')
template=f"""***RUTA EJERCICIOS RECOMENDADOS***:
{R}
"""
print(template)

