import pandas as pd

# Cargar información de ejercicios
ejercicios_df = pd.read_csv('ejercicios.csv')

# Códigos de los criterios (no están del 1 al 20)
codigos_criterios=ejercicios_df['criterion_code'].unique()


  