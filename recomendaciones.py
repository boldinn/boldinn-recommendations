from procesamiento_puntajes import obtener_4_criterios
from math import floor
import random
from disponibilidad_ejercicios_en_criterios import ejercicios_disponibles
from data_handling import ejercicios_df, codigos_criterios


# Función para obtener los ejercicios recomendados
def recomendar_ejercicios(puntajes,ejercicios):

  """Función de recomendación de rutas de ejercicios,
  a partir de los puntajes de un grupo en los diferentes criterios y
  los ejercicios ya resueltos por los grupos.

  Inputs:
  - dicionario de parejas de la forma 'criterio':'puntaje'.
  - lista de ejercicios resueltos por los grupos.

  Output: diccionario 4 parejas de la forma 'criterio':'ejercicio_recomendado'.
  """

  # criterios con ejercicios disponibles 
  criterios_ej_disp=[i  for i,(c,p) in enumerate (puntajes.items()) if ejercicios_disponibles(int(c), nivel(p),ejercicios)]
  
  # orden rango 0 al 19
  puntajes={i : v for i, v in enumerate(puntajes.values())} 
  
  # Escoger 4 criterios apropiados entre los ordenados
  criterios = obtener_4_criterios(puntajes,criterios_ej_disp)

  ejercicios_recomendados = {}

  for criterio in criterios:
      porcentaje=puntajes[criterio]

      # Calcular nivel de complejidad
      nivel_elegido=nivel(porcentaje)
      
      # Seleccionar un ejercicio aleatorio con el nivel de complejidad elegido
      # para el criterio actual
      code=int(codigos_criterios[criterio])
      ejercicios_filtrados = ejercicios_df[(ejercicios_df['level'] == nivel_elegido) & (ejercicios_df['criterion_code']==code)]
      ejercicio_elegido = random.choice(ejercicios_filtrados['code'].tolist())
      ejercicios_recomendados[code]=ejercicio_elegido  

  #Finalmente, necesitamos obtener los niveles de los ejercicios recomendados
  ejercicios_con_niveles = [(code,calcular_nivel(ejercicio)) for code, ejercicio in ejercicios_recomendados.items()]

  # Ahora, ordenamos los ejercicios por su nivel, de menor a mayor
  ejercicios_ordenados = sorted(ejercicios_con_niveles, key=lambda x: x[1])
  
  # Construimos el resultado final con los ejercicios ordenados
  ejercicios_recomendados_ordenados = {code: ejercicios_recomendados[code] for code,level in ejercicios_ordenados}

  return ejercicios_recomendados_ordenados


def calcular_nivel(ejercicio):
  level=ejercicios_df.loc[ejercicios_df['code'] == ejercicio]['level'].iloc[0]
  return level

def nivel(puntaje):
  level= 3 if puntaje == 100 else floor(puntaje / 25) # escogencia por cuartiles
  return level
  