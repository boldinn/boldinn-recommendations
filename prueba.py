
from team_recommendation_algorithm import get_best_teams_for_challenge
#from tra import get_best_teams_for_challenge as gbt
from data_handling import procesar_datos

org_id=12
position=None
knowledge=None
area= ['Grupo 2','Grupo 6']
n_rec=6 # número máximo de recomendaciones
data_df,desafios_df=procesar_datos(org_id,position, knowledge, area)
#print(data_df)
team_size=8
top_n=8
include=[150,100]
discard=[207,206]
history=[[150,100,176,155],[150,100,176,148]]

for desafio in range(1,43): #43
    best_teams_for_challenge = get_best_teams_for_challenge(desafio, data_df, desafios_df, team_size, top_n, include,discard,history,n_rec)
    #btfc = gbt(desafio, data_df, desafios_df, team_size, top_n, include=None,discard=None,history=None)     
    #matches=[set(best_teams_for_challenge[i]).symmetric_difference(set(btfc[i])) for i in range(4) ]
    print(f"""--------------------------
    ***GRUPOS RECOMENDADOS DESAFIO {desafio}***:
    {best_teams_for_challenge}
    """)

