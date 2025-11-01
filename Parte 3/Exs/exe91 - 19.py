from random import randint
from operator import itemgetter

jogadores = {
    'jogador 1': randint(1,6),
    'jogador 2': randint(1,6),
    'jogador 3': randint(1,6),
    'jogador 4': randint(1,6)
}

# Explicação da aula:
jogadores_ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # itemgetter(0) = key, (1) = value
print(f'Ranking dos jogadores: {jogadores_ranking}')
