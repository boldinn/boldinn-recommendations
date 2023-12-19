from .procesamiento_puntajes import obtener_4_criterios
from math import floor
import random
from .disponibilidad_ejercicios_en_criterios import calcular_ejercicios_disponibles
from .data_handling import ejercicios_df, codigos_criterios


# Función para obtener los ejercicios recomendados
def recomendar_ejercicios(puntajes, ejercicios, n_rec):
    """Función de recomendación de rutas de ejercicios,
    a partir de los puntajes de un grupo en los diferentes criterios y
    los ejercicios ya resueltos por los grupos.

    Inputs:
    - dicionario de parejas de la forma 'criterio':'puntaje'.
    - lista de ejercicios resueltos por los grupos.
    - número de recomendaciones que se quieren (1,2 o 3).

    Output: diccionario 4 parejas de la forma 'criterio':'ejercicio_recomendado'.
    """

    # criterios con ejercicios disponibles
    criterios_ej_disp = [
        i
        for i, (c, p) in enumerate(puntajes.items())
        if calcular_ejercicios_disponibles(int(c), nivel(p), ejercicios)
    ]

    # orden rango 0 al 19
    puntajes = {i: v for i, v in enumerate(puntajes.values())}

    # escoger 4 criterios apropiados entre los ordenados
    # criterios = obtener_4_criterios(puntajes,criterios_ej_disp)
    criteriosxn = obtener_4_criterios(puntajes, criterios_ej_disp, n_rec)

    # escoger ejercicios para cada tupla de criterios
    ejercicios_recomendadosxn = [
        escoger_ejercicios(puntajes, criterios) for criterios in criteriosxn
    ]

    # ordenar ejercicios por puntajes en criterios (orden ascendente)
    ejercicios_recomendados_ordenadosxn = [
        organizar_ejercicios(ejercicios_recomendados)
        for ejercicios_recomendados in ejercicios_recomendadosxn
    ]

    return ejercicios_recomendados_ordenadosxn


def calcular_nivel(ejercicio):
    level = ejercicios_df.loc[ejercicios_df["code"] == ejercicio]["level"].iloc[0]
    return level


def nivel(puntaje):
    level = 3 if puntaje == 100 else floor(puntaje / 25)  # escogencia por cuartiles
    return level


def escoger_ejercicios(puntajes, criterios):
    ejercicios_recomendados = {}
    for criterio in criterios:
        # Calcular nivel de complejidad
        porcentaje = puntajes[criterio]
        nivel_elegido = nivel(porcentaje)

        # Seleccionar un ejercicio aleatorio con el nivel de complejidad elegido
        # para el criterio actual
        code = int(codigos_criterios[criterio])
        ejercicios_filtrados = ejercicios_df[
            (ejercicios_df["level"] == nivel_elegido)
            & (ejercicios_df["criterion_code"] == code)
        ]
        ejercicio_elegido = random.choice(ejercicios_filtrados["code"].tolist())
        ejercicios_recomendados[code] = ejercicio_elegido
    return ejercicios_recomendados


def organizar_ejercicios(ejercicios_recomendados):
    # Finalmente, necesitamos obtener los niveles de los criterios recomendados
    criterios_con_niveles = [
        (code, calcular_nivel(ejercicio))
        for code, ejercicio in ejercicios_recomendados.items()
    ]

    # Ahora, ordenamos los criterios por su nivel, de menor a mayor
    ejercicios_ordenados = sorted(criterios_con_niveles, key=lambda x: x[1])

    # Construimos el resultado final con los ejercicios ordenados
    ejercicios_recomendados_ordenados = {
        code: ejercicios_recomendados[code] for code, level in ejercicios_ordenados
    }

    return ejercicios_recomendados_ordenados
