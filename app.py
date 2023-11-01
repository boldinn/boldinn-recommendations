import json
import os
from flask import Flask, request, jsonify
from recomendaciones import recomendar_ejercicios
from alimentar_modelo import actualizar_datos_entrenamiento

app = Flask(__name__)

@app.route('/recomendar_ejercicios', methods=['POST'])
def recomendar_ejercicios_api():
    data = request.get_json()
    puntajes=data['puntajes']
    ejercicios=data['ejercicios_resueltos']
    try:
        ejercicios_recomendados = recomendar_ejercicios(puntajes,ejercicios)
        return jsonify({'recommendations': ejercicios_recomendados})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/actualizar_datos', methods=['POST'])
def actualizar_datos_api():
    data = request.get_json()
    utilidades= data['utilidades']
    puntajes_ejercicios= data['puntajes_ejercicios']
    puntajes = data['puntajes']
    print(data)
    try:
        actualizar_datos_entrenamiento(utilidades, puntajes_ejercicios, puntajes)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use 5000 as a default if PORT is not set
    app.run(host='0.0.0.0', port=port)
