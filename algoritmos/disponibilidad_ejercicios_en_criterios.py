from .data_handling import ejercicios_df


def calcular_ejercicios_disponibles(criterio, nivel, ejercicios_agotados):
    """
    Verifica si hay ejercicios disponibles para un criterio y nivel específicos.

    inputs:

    criterio: El criterio para el cual se buscan ejercicios.
    nivel: El nivel de dificultad de los ejercicios.
    ejercicios_agotados: lista de ejercicios que ya están agotados.

    outputs: True si hay ejercicios disponibles, False en caso contrario.
    """

    # Filtrar el DataFrame de ejercicios basado en el criterio y nivel
    ejercicios_disponibles = ejercicios_df[
        (ejercicios_df["criterion_code"] == criterio)
        & (ejercicios_df["level"] == nivel)
        & (
            ~ejercicios_df["code"].isin(ejercicios_agotados)
        )  # excluyendo los ejercicios agotados
    ]
    # Si hay al menos un ejercicio disponible retornar True

    return not ejercicios_disponibles.empty
