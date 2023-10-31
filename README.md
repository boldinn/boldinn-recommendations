
# LaCocreadoraML

Bienvenido al repositorio del algoritmo avanzado de recomendación de ejercicios de LaCocreadora, ahora potenciado con capacidades de aprendizaje automático para proporcionar recomendaciones más precisas y personalizadas.

## Descripción

Este sistema se basa en dos componentes principales:

1. **Recomendación de Rutas de Ejercicios**: Utilizando un algoritmo inteligente, el sistema recomienda una serie de ejercicios basados en la complejidad y los criterios específicos del usuario, asegurando una experiencia personalizada y desafiante.

2. **Alimentación de Datos de Modelo**: Para mejorar continuamente la precisión de nuestras recomendaciones, el sistema incorpora regularmente datos de rendimiento y feedback del usuario en el modelo de aprendizaje automático.

Ambos componentes utilizan datos detallados y actualizados de los ejercicios disponibles, asegurando que las recomendaciones estén alineadas con los recursos y objetivos actuales.

## Archivos Principales

- `recomendaciones.py`: Contiene la lógica principal para generar recomendaciones de ejercicios.
- `alimentar_modelo.py`: Responsable de actualizar y alimentar el modelo de aprendizaje automático con nuevos datos.

## Módulos Auxiliares

- `procesamiento_puntajes.py`: Procesa los puntajes asociados con cada ejercicio, contribuyendo a la lógica de recomendación.
- `disponibilidad_ejercicios_en_criterios.py`: Verifica la disponibilidad de ejercicios, asegurando que las recomendaciones sean factibles y relevantes.

## Datos

- `ejercicios.csv`: Contiene datos actualizados sobre los ejercicios disponibles y sus relaciones con los criterios específicos.

## Instalación

Para instalar y ejecutar este proyecto, primero clone el repositorio y luego instale las dependencias necesarias utilizando:

```
pip install -r requirements.txt
```

