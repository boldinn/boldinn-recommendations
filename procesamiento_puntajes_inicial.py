import random

def obtener_4_criterios(criterios_ordenados):

  """ Obtiene 4 criterios apropiados (según indicaciones de La Cocreadora)
  entre la lista de criterios ordenados de menor a mayor puntaje.
  Input: lista de parejas (criterio, puntaje) ordenada de menor a mayor
  puntaje.
  Output: sublista apropiada de cuatro items del input.
  """
  
  # Criterios con puntaje imperfecto
  imperfectos= [(c, p) for c, p in criterios_ordenados if p < 100]
  n=len(imperfectos)
  if n>=4:    # Encontrar el mejor y los tres peores criterios entre los <100
    criterios_ordenados=imperfectos
    best_criterion = criterios_ordenados[-1]
    criteria = criterios_ordenados[:3]
    criteria.append(best_criterion)
  else:    # Tomar los imperfectos (menos que 4) y completar 4 con los perfectos de manera aleatoria
    criteria=imperfectos
    perfectos= random.sample(criterios_ordenados[n:],4-n)
    criteria += perfectos

  return criteria