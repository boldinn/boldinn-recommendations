import pandas as pd
import numpy as np
from data_handling import ejercicios_df, codigos_criterios as criterios


def actualizar_datos_entrenamiento(utilidades, puntajes_ejercicios, puntajes):
    """
    Actualiza el archivo 'datos_entrenamiento.csv' agregando una nueva fila con los datos proporcionados.

    Inputs:
    - utilidades (lista) : utilidades de los ejercicios de la ruta.
    - puntajes_ejercicios (dict): puntajes obtenidos en los ejercicios de la ruta.
    - puntajes (dict): puntajes en los 20 criterios *antes de recomendar ruta*.

    No devuelve ningún valor.
    """

    # Calcular el promedio de las utilidades de los ejercicios
    promedio_utilidades = sum(utilidades) / len(utilidades)

    # Calcular la suma de los puntajes de los ejercicios de la ruta
    suma_puntajes = sum(puntajes_ejercicios.values())

    # Calcular Score (2.4 es el máximo incremento posible)
    score = 0.6 * promedio_utilidades + 0.4 * suma_puntajes / 2.4

    # Preparar la nueva fila con los puntajes finales
    nueva_fila = {
        f"Puntajes_Criterio_{i + 1}": p / 100 for i, p in enumerate(puntajes.values())
    }

    # Obtener los códigos de los ejercicios de la ruta
    codigos_ejercicios = list(puntajes_ejercicios.keys())

    # Para cada ejercicio, encontrar el criterio correspondiente y actualizar la nueva fila
    nueva_fila.update(
        {f"C{i + 1}": 0 for i in range(20)}
    )  # Inicializar codificación de criterios en 0

    for codigo in codigos_ejercicios:
        # Encontrar el criterio correspondiente al ejercicio
        criterio = ejercicios_df[ejercicios_df["code"] == codigo][
            "criterion_code"
        ].values
        i = int(np.where(criterios == criterio)[0][0]) + 1

        # Actualizar la nueva fila con la información del criterio
        nueva_fila[f"C{i}"] = 1  # '1' indica la presencia del criterio en ruta

    nueva_fila["score"] = score

    # Agregar la nueva fila a 'datos_entrenamiento.csv'
    # print(nueva_fila)

    fila_csv = ",".join(str(value) for value in nueva_fila.values()) + "\n"

    with open("datos_entrenamiento.csv", "a") as file:
        file.write(fila_csv)

    # La función no devuelve ningún valor, solo actualiza el archivo.
