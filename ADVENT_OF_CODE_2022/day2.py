"""
Piedra, papel o tijera.

1º Columna: lo que el oponente elige.
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
2º Columna lo que yo elegiría.
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""
import pandas as pd

puntuacion_herramientas = {
    # Piedra
    'X': 1,
    # Papel
    'Y': 2,
    # Tijera
    'Z': 3
}

puntuacion_partidas = {
    # Piedra contra papel: Yo gano - 6 (por ganar) + 2 (papel) -.
    'A Y': 6 + puntuacion_herramientas['Y'],
    # Papel contra piedra: Yo pierdo - 0 (por perder) + 1 (piedra) -.
    'B X': 0 + puntuacion_herramientas['X'],
    # Tijera contra tijera: Empate - 3 (por empate) + 3 (tijera) -
    'C Z': 3 + puntuacion_herramientas['Z'],

    # Aparte de las 3 posibilidades anteriores, nuestra estrategia, entiendo que debemos crear todas las combinaciones posibles.
    'A Z': 0 + puntuacion_herramientas['Z'],
    'B Y': 3 + puntuacion_herramientas['Y'],
    'C X': 6 + puntuacion_herramientas['X'],
    'C Y': 0 + puntuacion_herramientas['Y'],
    'B Z': 6 + puntuacion_herramientas['Z'],
    'A X': 3 + puntuacion_herramientas['X']
}

with open('day2.txt', 'r') as day2:

    lista_de_partidas = [line.replace('\n', "") for line in day2]

puntuaciones_por_partida = [puntuacion_partidas[partida] for partida in lista_de_partidas]

print(f'Resultado 1º parte: {sum(puntuaciones_por_partida)}')

""" Podría hacer lo mismo con pandas. Faltaría hacer la suma.
df_partidas = pd.DataFrame({
    'PARTIDAS': lista_de_partidas,
})

df_partidas['PUNTUACION'] = df_partidas['PARTIDAS'].map(puntuacion_partidas)
print(df_partidas.head())
"""

################################### SEGUNDA PARTE ###################################

# El dict puntuacion_herramientas todavía nos sirve.

puntuacion_partida = {
    # Perder
    'X': 0,
    # Empatar
    'Y': 3,
    # Ganar
    'Z': 6
}
combinaciones_ganar = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}
combinaciones_perder = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}
combinaciones_empatar = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

df_partidas = pd.DataFrame({
    'OPONENTE_Y_COMO_FINALIZAR': lista_de_partidas,
})

# Sacamos la última letra, el código de cómo finalizar.
df_partidas['COMO_FINALIZAR'] = df_partidas['OPONENTE_Y_COMO_FINALIZAR'].str.slice(start=-1)

# En función de cómo finalizar y la jugada del oponente, devolvemos la jugada oportuna.

def escoger_jugada(oponente_y_como_finalizar):
    jugada_oponente = oponente_y_como_finalizar[0]
    como_finalizar = oponente_y_como_finalizar[-1]
    if como_finalizar == 'X':
        return combinaciones_perder[jugada_oponente]
    elif como_finalizar == 'Y':
        return combinaciones_empatar[jugada_oponente]
    elif como_finalizar == 'Z':
        return combinaciones_ganar[jugada_oponente]

df_partidas['MI_JUGADA'] = df_partidas['OPONENTE_Y_COMO_FINALIZAR'].apply(lambda oponente_y_como_finalizar: escoger_jugada(oponente_y_como_finalizar)) # apply recorre la serie y me pasa como parámetro (oponente_y_como_finalizar) cada valor de la misma.

# Puntuación según debo perder, ganar o empatar.

df_partidas['PUNTUACION_PARTIDA'] = df_partidas['COMO_FINALIZAR'].map(puntuacion_partida)

df_partidas['PUNTUACION_HERRAMIENTAS'] = df_partidas['MI_JUGADA'].map(puntuacion_herramientas)

df_partidas['PUNTUACION_TOTAL'] = df_partidas['PUNTUACION_PARTIDA'] + df_partidas['PUNTUACION_HERRAMIENTAS']

print(df_partidas.head())

print(f'Resultado 2º parte: {df_partidas["PUNTUACION_TOTAL"].sum()}')






