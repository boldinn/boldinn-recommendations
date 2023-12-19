import random
import json
from algoritmos.recomendaciones import recomendar_ejercicios
from algoritmos.data_handling import ejercicios_df
from algoritmos.alimentar_modelo import actualizar_datos_entrenamiento
import pandas as pd


class Grupo:
    def __init__(self, group_id, puntajes):  # se puede iniciar con puntajes del test
        self.group_id = group_id
        self.puntajes = puntajes
        self.ejercicios_realizados = []
        self.WIN = False

    def recomendar_ruta_y_actualizar(self):
        # a) Recomendar una ruta de ejercicios
        try:
            recomendaciones = recomendar_ejercicios(
                self.puntajes, self.ejercicios_realizados, n_rec=1
            )[0]
        except IndexError:
            self.WIN = True
            print(f"GROUP {self.group_id} WON")
            return

        # b) Simular la utilidad de los ejercicios
        utilidades = [
            1 if random.random() < 0.7 else -1 for ej in recomendaciones.values()
        ]

        # c) Simular si los ejercicios fueron aprobados y buscar su valor
        valores_ejercicios = {}
        for criterio, ejercicio in recomendaciones.items():
            aprobado = random.random() < 0.7
            valor_ejercicio = ejercicios_df.loc[
                ejercicios_df["code"] == ejercicio, "value"
            ].item()
            valores_ejercicios[ejercicio] = (
                valor_ejercicio if aprobado else -valor_ejercicio
            )

        # d) Actualizar los datos de entrenamiento
        actualizar_datos_entrenamiento(utilidades, valores_ejercicios, self.puntajes)

        # e) Actualizar los ejercicios realizados y los puntajes
        for ejercicio, valor in valores_ejercicios.items():
            criterio = ejercicios_df.loc[
                ejercicios_df["code"] == ejercicio, "criterion_code"
            ].item()
            self.puntajes[str(criterio)] += 20 * valor
            if valor > 0:  # Si el ejercicio fue aprobado
                self.ejercicios_realizados.append(ejercicio)


# Creamos instancias con grupos reales
grupos_df = pd.read_csv("grupos.csv")

# Convertir los puntajes de la columna "criterion_answers" a listas de diccionarios de Python
grupos_df["criterion_answers"] = grupos_df["criterion_answers"].apply(
    lambda x: json.loads(x.replace("=>", ":"))
)

# Crear una lista para almacenar las instancias de Grupo
grupos = []

# Inicializar las instancias de Grupo
for index, row in grupos_df.iterrows():
    puntajes_inst = row["criterion_answers"]
    grupo = Grupo(group_id=row["group_id"], puntajes=puntajes_inst)
    grupos.append(grupo)

# Verificar una de las instancias creadas
# print(grupos[0].__dict__)


import matplotlib.pyplot as plt


# Realizar n iteraciones, aplicando el método recomendar_ruta_y_actualizar por cada grupo
promedios_por_iteracion = []

n = 60  # número de iteraciones

for iteracion in range(n):
    promedios_iteracion = []
    for grupo in grupos:
        if grupo.WIN == False:
            grupo.recomendar_ruta_y_actualizar()
        Puntajes = grupo.puntajes.values()
        promedio_puntajes = sum(Puntajes) / len(Puntajes)
        promedios_iteracion.append(promedio_puntajes)
    promedios_por_iteracion.append(promedios_iteracion)

# Crear una gráfica con matplotlib que muestre el promedio de puntajes a través de las n iteraciones para cada grupo
plt.figure(figsize=(8, 6))
for i, grupo in enumerate(grupos):
    plt.plot(
        range(1, n + 1),
        [promedios[i] for promedios in promedios_por_iteracion],
        label=f"Grupo {grupo.group_id}",
    )

plt.xlabel("Iteración")
plt.ylabel("Promedio de Puntajes")
plt.title("Promedio de Puntajes por Grupo a lo Largo de las Iteraciones")
plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1), borderaxespad=0.0)
# plt.tight_layout()
plt.show()
