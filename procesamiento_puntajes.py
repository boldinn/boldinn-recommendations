import random
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import itertools

data = pd.read_csv("datos_entrenamiento.csv")
# print(len(data))
# entrenamiento modelo de regresión

X = data.drop("score", axis=1)  # Características
y = data["score"]  # Etiquetas
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)

print("Error cuadrático medio regresión:", mse)


def cuadrupla(vector_binario):
    cuadrupla = np.where(vector_binario == 1)[0] + 1
    return cuadrupla


def obtener_4_criterios(criterios_puntajes, lista):
    """Obtiene 4 criterios apropiados (modelo de regresión y maximización)
    del diccionario de con items criterio:puntaje.
    Inputs:
    -diccionario de items criterio:puntaje
    -lista de criterios con ejercicios disponibles
    Output: lista apropiada de cuatro criterios.
    """
    # print('lista:',lista)
    # print('dict:',criterios_puntajes)
    n = 20
    k = 4
    # Criterio de máximo puntaje entre los que tienen ej. disponibles
    c_p_filtrado = {c: criterios_puntajes[c] for c in criterios_puntajes if c in lista}
    # print('filtrado:',c_p_filtrado)
    c_max = max(c_p_filtrado, key=lambda k: c_p_filtrado[k])
    # print('c_max',c_max)
    # Genera todas las combinaciones de 4 unos
    # en una secuencia de criterios disponibles, *con c_max fijo*
    lista.remove(c_max)
    combinaciones = list(itertools.combinations(lista, k - 1))
    combinaciones_con_c_max = [(c_max,) + c for c in combinaciones]
    n_comb = len(combinaciones_con_c_max)

    # Crea una matriz para almacenar los vectores
    matriz_posibles = np.zeros((n_comb, n), dtype=int)

    # Rellena la matriz con los vectores posibles
    for i, comb in enumerate(combinaciones_con_c_max):
        matriz_posibles[i, comb] = 1
    # print(n_comb)
    posible = {}
    for i in range(1, n + 1):
        posible[f"Puntajes_Criterio_{i}"] = np.full(
            n_comb, criterios_puntajes[i - 1] / 100
        )

    for i in range(1, n + 1):
        posible[f"C{i}"] = matriz_posibles[:, i - 1]

    posible_df = pd.DataFrame(posible)
    predicted_scores = model.predict(posible_df)
    i_max = np.argmax(predicted_scores)
    vector_binario = posible_df.iloc[i_max].to_numpy(dtype=int)[20:]
    criteria = cuadrupla(vector_binario)

    return criteria
