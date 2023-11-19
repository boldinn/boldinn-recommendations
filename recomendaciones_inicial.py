from procesamiento_puntajes_inicial import obtener_4_criterios
from math import floor
import json
import pandas as pd
import random


# Cargar información de ejercicios
ejercicios_df = pd.read_csv('ejercicios.csv')

# Función para obtener los ejercicios recomendados
def recomendar_ejercicios(puntajes):

  """Función de recomendación de rutas de ejercicios,
  a partir de los puntajes de un grupo en los diferentes criterios.

  Input: diccionario de parejas de la forma 'criterio':'puntaje'.
  Output: diccionario de 4 parejas de la forma 'criterio':'ejercicio_recomendado'. 
  """
  puntajes={int(k): v for k, v in puntajes.items()}
  # Obtener los criterios ordenados por puntaje (de menor a mayor)
  sorted_criteria = sorted(puntajes.items(), key=lambda x: x[1])
  
  # Escoger 4 criterios apropiados entre los ordenados
  criteria = obtener_4_criterios(sorted_criteria)

  ejercicios_recomendados = {}

  for criterion, porcentaje in criteria:

      # Calcular nivel de complejidad
      if porcentaje==100:
        nivel_elegido=3 # máximo nivel
      else:
        nivel_elegido = floor(porcentaje/25) # escogencia por cuartiles

      # Seleccionar un ejercicio aleatorio con el nivel de complejidad elegido
      # para el criterio actual
      ejercicios_filtrados = ejercicios_df[(ejercicios_df['level'] == nivel_elegido) & (ejercicios_df['criterion_code']==criterion)]
      ejercicio_elegido = random.choice(ejercicios_filtrados['code'].tolist())
      ejercicios_recomendados[criterion]=ejercicio_elegido
  
  return ejercicios_recomendados


