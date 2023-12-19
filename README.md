
# Documentación del Repositorio: Algoritmo de Rutas

## Descripción General
Este repositorio contiene un sistema de recomendación de ejercicios implementado en Python. Utiliza un conjunto de algoritmos para ofrecer recomendaciones personalizadas basadas en los puntajes y respuestas de los usuarios. El sistema está diseñado para ser ejecutado en un entorno de servidor, utilizando Flask para la gestión de las API.

## Estructura del Repositorio
- **algoritmos/**: Carpeta conteniendo los algoritmos de recomendación y actualización de datos.
- **app.py**: Aplicación Flask principal, define las rutas de la API para recomendaciones y actualizaciones de datos.
- **grupos.csv**: Archivo CSV con datos de los grupos de usuarios.
- **Makefile**: Archivo para automatizar comandos.
- **prueba_*.py**: Varios scripts de prueba para distintas funcionalidades del sistema.
- **requirements.txt**: Dependencias necesarias para ejecutar el proyecto.
- **simulacion_*.py**: Scripts para simular escenarios deterministas o aleatorios.

## Instalación
1. Instalar las dependencias: 
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecutar `app.py` para iniciar el servidor Flask.

## Uso
- **Recomendación Inicial**: 
  - Ruta API: `/recomendacion_inicial`
  - Método: POST
  - Descripción: Ofrece la primera recomendación de ejercicios a un grupo basándose en sus puntajes iniciales.

- **Actualización de Datos**:
  - Ruta API: `/actualizar_datos`
  - Método: POST
  - Descripción: Actualiza los datos de entrenamiento después de cada interacción con un grupo.

- **Recomendación de Ejercicios**:
  - Ruta API: `/recomendar_ejercicios`
  - Método: POST
  - Descripción: Provee recomendaciones de ejercicios a partir de la segunda recomendación para un grupo, basándose en los puntajes y ejercicios resueltos.

## Ejemplos de Prueba
- **prueba_inicial.py**: Ejemplo de cómo utilizar el algoritmo para hacer recomendaciones iniciales a partir de los datos en `grupos.csv`.

## Dependencias
- Pandas, NumPy, Scikit-Learn, Requests, Flask.

## Notas Adicionales
- Asegúrese de configurar adecuadamente el entorno y las rutas de los archivos según su sistema de archivos local.
- Revise y ajuste el archivo `grupos.csv` según los datos de los grupos a los que desea aplicar el algoritmo.

## Descripción detallada del algoritmo

https://docs.google.com/document/d/1u4v_0eCuR7DA5Lrzi63kip1RFjf3E6jzB0K1Cqr-kVA


# Documentación del Segundo Repositorio: Algoritmo de Recomendación de Grupos

## Descripción General
Este repositorio implementa un algoritmo de recomendación para formar equipos óptimos para desafíos específicos. Se utiliza Python y Flask para crear una API que facilita la recomendación de grupos basada en diferentes criterios como conocimiento, área, y preferencias.

## Estructura del Repositorio
- **algoritmos/**: Contiene el algoritmo principal y funciones de manejo de datos.
- **app.py**: Aplicación Flask principal, define la ruta de la API para la recomendación de grupos.
- **Makefile**: Utilizado para automatización de tareas.
- **prueba.py**: Script de prueba para el algoritmo de recomendación de grupos.
- **prueba_API.py**: Script de prueba para la API de recomendación de grupos.
- **requirements.txt**: Lista de dependencias necesarias para el proyecto.

## Instalación
1. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecutar `app.py` para iniciar el servidor Flask.

## Uso
- **Recomendación de Grupos**:
  - Ruta API: `/recomendar_grupos`
  - Método: POST
  - Descripción: Recomienda grupos óptimos para un desafío específico basándose en criterios como tamaño del grupo, conocimientos, áreas, etc.

## Ejemplos de Prueba
- **prueba.py**: Ejemplo de cómo utilizar el algoritmo para obtener recomendaciones de equipos para diferentes desafíos.

## Dependencias
- Pandas, Requests, Flask.

## Notas Adicionales
- Es importante configurar correctamente las rutas y los datos de entrada según los requisitos y el contexto en el que se utilizará el algoritmo.
- El script `prueba.py` proporciona una forma clara de entender cómo se pueden aplicar los algoritmos a situaciones prácticas.

## Descripción conceptual del algoritmo
https://docs.google.com/document/d/1kGPl3hO4V415y2Wi-5WCvhwu-vBUm5ZE1jmmwPYzBhE/edit?usp=sharing
