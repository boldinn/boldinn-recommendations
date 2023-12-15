import pandas as pd
import requests

# URL de la API de los datos de organizaciones
# url = "https://boldinn-api.herokuapp.com/api/v1/recommendations/org_data"
url = "http://localhost:3000/api/v1/recommendations/org_data"


def procesar_datos(org_id, position, knowledge, area):
    # obtener datos vía url, haciendo la solicitud HTTP GET
    response = requests.get(f"{url}/{org_id}")

    # crear dataframe
    data_df = pd.DataFrame(response.json())

    # cargar datos de desafíos
    desafios_df = pd.read_csv("desafíos.csv", encoding="ISO-8859-1", delimiter=";")

    # preparar datos de desafíos (pasar V o F a True o False)
    for col in ["H1", "H2", "H3", "H4", "H5"]:
        desafios_df[col] = desafios_df[col].apply(
            lambda x: True if x.strip().upper() == "VERDADERO" else False
        )

    # obtener lista de criterios involucrados

    desafios_df["I"] = desafios_df["Indicadores"].str.split(",")

    # filtrado de acuerdo a posición, conocimiento y área
    if position:
        fd1 = data_df[data_df["position"].isin(position)]
    else:
        fd1 = data_df

    if knowledge:
        fd2 = fd1[fd1["knowledge"].isin(knowledge)]
    else:
        fd2 = fd1

    if area:
        filtered_data = fd2[fd2["area"].isin(area)]
    else:
        filtered_data = fd2

    return filtered_data, desafios_df


# print(desafios_df['I'])

# Cargar información de ejercicios
ejercicios_df = pd.read_csv("ejercicios.csv")

# Códigos de los criterios (no están del 1 al 20)
codigos_criterios = ejercicios_df["criterion_code"].unique()
