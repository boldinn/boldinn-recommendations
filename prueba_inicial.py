# Prueba del algoritmo para la información de los grupos en grupos.csv

import pandas as pd
from recomendaciones_inicial import recomendar_ejercicios
import json

grupos_df = pd.read_csv('grupos.csv')

# Procesar el formato de "criterion_answers" en grupos_df
def parse_criterion_answers(criterion_answers_str):
    criterion_answers = criterion_answers_str.replace("=>", ":")
    return criterion_answers

grupos_df['criterion_answers'] = grupos_df['criterion_answers'].apply(parse_criterion_answers)

# Función diccionario de puntajes de un grupo dado
def obtener_puntajes(group_id):
    criterion_answers = grupos_df.loc[grupos_df['group_id'] == group_id, 'criterion_answers'].values[0]
    return criterion_answers

print(obtener_puntajes(6))

# Recomendaciones para los grupos en la base de datos grupos.csv

grupos=grupos_df['group_id'].tolist()
for g in grupos:
  grupo_id = g
  ejercicios_recomendados = recomendar_ejercicios(json.loads(obtener_puntajes(grupo_id)))
  print(f"""***RUTA DE EJERCICIOS RECOMENDADOS GRUPO {g}***:
  {ejercicios_recomendados}
*********************************************

        """)