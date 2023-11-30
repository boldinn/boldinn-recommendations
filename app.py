# pylint: disable=undefined-variable

import json
import os
from flask import Flask, request, jsonify
from recomendaciones_inicial import recomendar_ejercicios as recomendacion_inicial
from recomendaciones import recomendar_ejercicios
from alimentar_modelo import actualizar_datos_entrenamiento

app = Flask(__name__)


# la primera recomendación a cada grupo se hace con la siguiente función.
@app.route("/recomendacion_inicial", methods=["POST"])
def recomendacion_inicial_api():
    data = request.get_json()
    # Dict =json.loads(data)
    puntajes = data["puntajes"]
    try:
        ejercicios_recomendados = recomendacion_inicial(puntajes)
        return jsonify({"recommendations": ejercicios_recomendados})
    except Exception as e:
        return jsonify({"error": str(e)})


# después de cada interacción con un grupo se usa la siguiente función.
@app.route("/actualizar_datos", methods=["POST"])
def actualizar_datos_api():
    data = request.get_json()
    # Dict = json.loads(data)
    utilidades = data["utilidades"]
    puntajes_ejercicios = data["puntajes_ejercicios"]
    puntajes = data["puntajes"]
    print(data)

    try:
        actualizar_datos_entrenamiento(utilidades, puntajes_ejercicios, puntajes)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)})


# para cada grupo, a partir de la segunda recomendación se usa la siguiente función.
@app.route("/recomendar_ejercicios", methods=["POST"])
def recomendar_ejercicios_api():
    data = request.get_json()
    # Dict =json.loads(data)
    puntajes = data["puntajes"]
    ejercicios = data["ejercicios_resueltos"]
    n_rec = data["n_rec"]
    try:
        ejercicios_recomendados = recomendar_ejercicios(puntajes, ejercicios, n_rec)
        return jsonify({"recommendations": ejercicios_recomendados})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use 5000 as a default if PORT is not set
    app.run(host="0.0.0.0", port=port)
