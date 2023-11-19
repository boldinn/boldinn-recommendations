from alimentar_modelo import actualizar_datos_entrenamiento
import pandas as pd
import random
from data_handling import ejercicios_df, codigos_criterios

utilidades = [0.2, 0.3, 0.5, 0.4]
puntajes_ejercicios = {'E10': 0.2, 'E20': 0.4, 'E30': 0.4, 'E40':0.6}

# 20 puntajes (previos)
P={int(c): 100*random.random() for c in codigos_criterios}

actualizar_datos_entrenamiento(utilidades, puntajes_ejercicios, P)