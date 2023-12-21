from itertools import combinations
from .data_handling import ejercicios_df as E


# Función para calcular el número máximo de medallas de una abilidad dada en todos los usuarios
def max_medals(ability, data_df):
    return max(x.count(ability) for x in data_df["ability_medals"])


# Función para encontrar los top_n usuarios para cada criterio requerido
def get_top_users_for_crit(users_df, criteria_required, top_n):
    top_users = {c: [] for c in criteria_required}

    for c in criteria_required:
        skill = ability_from(c)
        # calcular el score de criterios-medallas y ordenar los usuarios
        users_df[c] = (
            0.6 * users_df["criteria"].apply(lambda x, crit=c: x.get(crit, 0)) / 100
        )
        users_df[c] += (
            0.2
            * users_df["ability_medals"].apply(
                lambda x, skill=ability_from(c): x.count(skill)
            )
            / max_medals(skill, users_df)
        )
        top_users_for_crit = users_df.sort_values(by=c, ascending=False).head(top_n)
        top_users[c] = top_users_for_crit["user_id"].tolist()

    # Recolectar usuarios a lo largo de los criterios
    blend_top_users = sum(top_users.values(), [])
    users_df_top = users_df[users_df["user_id"].isin(blend_top_users)].copy()

    # Calcular el promedio de todos los criterios requeridos para cada usuario
    users_df_top.loc[:, "average_score"] = users_df_top[criteria_required].mean(axis=1)

    # Ordenar por promedio de mayor a menor y seleccionar los top_n usuarios
    top_list = users_df_top.sort_values(by="average_score", ascending=False)

    return top_list["user_id"].to_list()


def ability_from(criterion):
    # Filtrando los datos por el código de criterio dado
    filtered_data = E[E["criterion_code"] == int(criterion)]
    ability = filtered_data["ability_code"].unique()[0]
    return ability


# Función para recomendar los mejores equipos para un desafío dado
def get_best_teams_for_challenge(
    challenge_number,
    users_df,
    challenges_df,
    team_size,
    top_n,
    include,
    discard,
    history,
    n_rec,
):
    # Eliminar usuarios en 'discard' del DataFrame users_df
    if discard:
        users_df = users_df.drop(users_df[users_df["user_id"].isin(discard)].index)

    # Ajustar el tamaño del equipo si hay usuarios para incluir
    team_size = team_size - len(include) if include else team_size

    # Identificar las habilidades requeridas para el desafío
    challenge_row = challenges_df[challenges_df["#"] == challenge_number]
    criteria_required = [n for n in challenge_row["I"].values[0] if n]

    # Obtener los mejores usuarios para cada criterio requerido
    top_users_for_crit = get_top_users_for_crit(users_df, criteria_required, top_n)

    # Generar combinaciones relevantes de equipos
    best = top_users_for_crit[:team_size]  # best candidates
    worst = top_users_for_crit[team_size:]  # worst candidates
    S = combinations(best, team_size - 1)
    all_possible_teams = [best] + [
        list(s) + [person] for s in S for person in worst
    ]  # simplification of the code below

    # Agregar los usuarios de 'include' a cada equipo
    if include:
        all_possible_teams = [include + team for team in all_possible_teams]

    # Eliminar combinaciones que ya están en el historial 'history'
    if history:
        #   history with sets (to take account of permutations)
        H = [set(h) for h in history]
        all_possible_teams = [team for team in all_possible_teams if set(team) not in H]

    # Calcular el puntaje promedio de habilidades para cada equipo
    team_scores = []
    for team in all_possible_teams:
        team_df = users_df[users_df["user_id"].isin(team)]

        # Calcular el promedio de cada habilidad-medalla a través de todos los miembros del equipo
        crit_averages = [team_df[c].mean() for c in criteria_required]

        # Luego, tomar el promedio de esos promedios de habilidades-medallas para obtener el puntaje final del equipo
        final_team_score = sum(crit_averages) / len(crit_averages)
        team_scores.append((team, final_team_score))

    # Ordenar los equipos por el puntaje promedio de criterios-medallas y seleccionar los cuatro mejores
    team_scores.sort(key=lambda x: x[1], reverse=True)
    best_teams = team_scores[:n_rec]
    best = [list(t[0]) for t in best_teams]

    return best
