import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import itertools

def cuadrupla(vector_binario):
  cuadrupla=np.where(vector_binario==1)[0]
  return cuadrupla


def obtener_4_criterios(criterios_puntajes,lista,n_rec):

  """ Obtiene 4 criterios apropiados (modelo de regresión y maximización)
  del diccionario con items criterio:puntaje.
  Inputs: 
  - diccionario de items 'criterio' (0-19):'puntaje'.
  - lista de criterios con ejercicios disponibles.
  - número de recomendaciones que se quieren (1,2 o 3).

  Output: lista de listas apropiada de cuatro criterios, de tamaño n_rec.
  """
  data = pd.read_csv('datos_entrenamiento.csv')
  print(len(data))
  # entrenamiento modelo de regresión

  X = data.drop('score', axis=1) # Características
  y = data['score'] # Etiquetas
  model = LinearRegression()
  model.fit(X, y)
  y_pred = model.predict(X)
  mse = mean_squared_error(y, y_pred)

  print("Error cuadrático medio regresión:", mse)

  #print('lista:',lista)
  #print('dict:',criterios_puntajes)
  n=20
  k=4
  # Criterio de máximo puntaje entre los que tienen ej. disponibles
  c_p_filtrado={c:criterios_puntajes[c] for c in criterios_puntajes if c in lista }
  #print('filtrado:',c_p_filtrado)
  c_max = max(c_p_filtrado, key=lambda k: c_p_filtrado[k])
  #print('c_max',c_max)
  # Genera todas las combinaciones de 4 unos 
  # en una secuencia de criterios disponibles, *con c_max fijo*
  lista.remove(c_max)
  combinaciones = list(itertools.combinations(lista, k-1))
  combinaciones_con_c_max = [(c_max,) + c for c in combinaciones]
  n_comb=len(combinaciones_con_c_max)

  # Crea una matriz para almacenar los vectores
  matriz_posibles = np.zeros((n_comb, n), dtype=int)

  # Rellena la matriz con los vectores posibles
  for i, comb in enumerate(combinaciones_con_c_max):
    matriz_posibles[i, comb] = 1
  #print(n_comb)
  posible={}
  for i in range(n):
    posible[f'Puntajes_Criterio_{i+1}'] = np.full(n_comb,criterios_puntajes[i]/100)

  for i in range(n):
    posible[f'C{i+1}'] = matriz_posibles[:,i]
  posible_df = pd.DataFrame(posible)
  #print(posible_df.shape)
  predicted_scores = model.predict(posible_df)
  #i_max=np.argmax(predicted_scores)
  top_n_rec=np.argsort(predicted_scores)[:len(predicted_scores)-n_rec-1:-1]
  print('top_n_rec',top_n_rec)
  #vector_binario=posible_df.iloc[i_max].to_numpy(dtype=int)[20:]
  vectores_binarios=[posible_df.iloc[i].to_numpy(dtype=int)[20:] for i in top_n_rec]
  #criteria=[cuadrupla(vector_binario)]
  criteriaxn=[cuadrupla(vector_binario) for vector_binario in vectores_binarios]
  return criteriaxn
