
# Sistema de Recomendación de Ejercicios de LaCocreadoraML

## Descripción General

LaCocreadoraML utiliza algoritmos de aprendizaje automático para mejorar la experiencia de los usuarios al recomendar rutas de ejercicios personalizadas y optimizar el modelo subyacente a través de la retroalimentación del usuario. El sistema se compone de dos funciones principales, descritas en detalle a continuación.

## 1. Recomendación de Rutas de Ejercicios

### Descripción

Esta función selecciona una serie de ejercicios basados en la dificultad preferida del usuario y los criterios seleccionados, proporcionando una experiencia de entrenamiento personalizada.

### Implementación

El módulo `recomendaciones.py` contiene la lógica principal de esta función. Utiliza los datos de los ejercicios disponibles y los puntajes de los criterios para seleccionar ejercicios que no solo cumplan con los requisitos de dificultad sino que también se alineen con los objetivos del usuario.

#### Métodos Principales

- `recomendar_ejercicios`: Este método toma los puntajes de los criterios como entrada y utiliza esta información para seleccionar ejercicios con el nivel adecuado de dificultad. Los ejercicios se seleccionan de manera aleatoria dentro de los que cumplen con los criterios, y luego se ordenan basándose en su nivel de dificultad.

- `calcular_nivel`: Determina el nivel de dificultad de un ejercicio específico, que se utiliza para asegurar que las recomendaciones se ajusten a las preferencias del usuario.

- `nivel`: Calcula el nivel de dificultad basado en el puntaje proporcionado.

### Bibliotecas y Dependencias

- `pandas`: Utilizado para la manipulación de datos y operaciones con dataframes.
- `json`: Para el manejo de datos en formato JSON, facilitando el intercambio de datos.
- `random`: Para la selección aleatoria de ejercicios.
- `math`: Utilizado para realizar cálculos matemáticos básicos necesarios en la lógica del algoritmo.

## 2. Alimentación de Datos del Modelo

### Descripción

Esta función es crucial para el aprendizaje y la mejora continua del sistema. Acepta datos en forma de utilidades y puntajes, actualiza el modelo y ajusta las recomendaciones futuras.

### Implementación

El módulo `alimentar_modelo.py` maneja la lógica para esta función. Actualiza un archivo 'datos_entrenamiento.csv' con nuevas entradas basadas en la retroalimentación y el rendimiento del usuario.

#### Métodos Principales

- `actualizar_datos_entrenamiento`: Este método recopila nuevos datos en forma de JSON, realiza varios cálculos y agrega una nueva fila al conjunto de datos de entrenamiento.

### Bibliotecas y Dependencias

- `json`: Para manejar datos en formato JSON.
- `pandas`: Utilizado para la manipulación de datos y operaciones con dataframes.
- `numpy`: Para operaciones matemáticas y manejo de arrays multidimensionales.

## Instalación

Consulte el archivo `requirements.txt` para obtener una lista de las bibliotecas necesarias para ejecutar estos scripts en un entorno virtual.
