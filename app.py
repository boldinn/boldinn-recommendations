import json
import os
from flask import Flask, request, jsonify
from algoritmos.recomendaciones_inicial import (
    recomendar_ejercicios as recomendacion_inicial,
)
from algoritmos.recomendaciones import recomendar_ejercicios
from algoritmos.alimentar_modelo import actualizar_datos_entrenamiento
from algoritmos.data_handling import procesar_datos
from algoritmos.team_recommendation_algorithm import get_best_teams_for_challenge

app = Flask(__name__)

# la primera recomendación a cada grupo se hace con la siguiente función.
@app.route("/recomendacion_inicial", methods=["POST"])
def recomendacion_inicial_api():
    data = request.get_json()
    # Dict = json.loads(data)
    puntajes = data["puntajes"]
    try:
        ejercicios_recomendados = recomendacion_inicial(puntajes)
        return jsonify({"recommendations": ejercicios_recomendados})
    except ValueError as e:
        return jsonify({"error": "Error de valor: " + str(e)})
    except KeyError as e:
        return jsonify({"error": "Error de clave: " + str(e)})
    except TypeError as e:
        return jsonify({"error": "Error de tipo: " + str(e)})


# después de cada interacción con un grupo se usa la siguiente función.
@app.route("/actualizar_datos", methods=["POST"])
def actualizar_datos_api():
    data = request.get_json()
    # Dict = json.loads(data)
    utilidades = data["utilidades"]
    puntajes_ejercicios = data["puntajes_ejercicios"]
    puntajes = data["puntajes"]
    try:
        actualizar_datos_entrenamiento(utilidades, puntajes_ejercicios, puntajes)
        return jsonify({"success": True})
    except ValueError as e:
        return jsonify({"error": "Error de valor: " + str(e)})
    except KeyError as e:
        return jsonify({"error": "Error de clave: " + str(e)})
    except TypeError as e:
        return jsonify({"error": "Error de tipo: " + str(e)})


# para cada grupo, a partir de la segunda recomendación se usa la siguiente función.
@app.route("/recomendar_ejercicios", methods=["POST"])
def recomendar_ejercicios_api():
    data = request.get_json()
    # Dict = json.loads(data)
    puntajes = data["puntajes"]
    ejercicios = data["ejercicios_resueltos"]
    n_rec = data["n_rec"]
    try:
        ejercicios_recomendados = recomendar_ejercicios(puntajes, ejercicios, n_rec)
        return jsonify({"recommendations": ejercicios_recomendados})
    except ValueError as e:
        return jsonify({"error": "Error de valor: " + str(e)})
    except KeyError as e:
        return jsonify({"error": "Error de clave: " + str(e)})
    except TypeError as e:
        return jsonify({"error": "Error de tipo: " + str(e)})


@app.route("/recomendar_grupos", methods=["POST"])
def recomendar_grupos_api():
    data = request.get_json()
    # Dict = json.loads(data)
    desafio = data["desafio"]
    tamanio_grupo = data["tamanio_grupo"]
    include = data["include"]
    discard = data["discard"]
    history = data["history"]
    id_org = data["id_org"]
    position = data["position"]
    knowledge = data["knowledge"]
    area = data["area"]
    top_n = 8
    n_rec = data["n_rec"]  # número máximo de recomendaciones
    data_df, desafios_df = procesar_datos(id_org, position, knowledge, area)
    try:
        grupos_recomendados = get_best_teams_for_challenge(
                desafio,
                data_df,
                desafios_df,
                tamanio_grupo,
                top_n,
                include,
                discard,
                history,
                n_rec,
            )
        return jsonify({"recomendaciones": grupos_recomendados})
    except ValueError as e:
        return jsonify({"error": "Error de valor: " + str(e)})
    except KeyError as e:
        return jsonify({"error": "Error de clave: " + str(e)})
    except TypeError as e:
        return jsonify({"error": "Error de tipo: " + str(e)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use 5000 as a default if PORT is not set
    app.run(host="0.0.0.0", port=port)
