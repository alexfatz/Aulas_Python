dicionario = {}
lista = []
dicionario['nome_jogador'] = input('Nome do jogador: ')
dicionario['partidas'] = int(input('Quantas partidas jogou? '))
for x in range(0, dicionario['partidas']):
    lista.append([f'Jogo {x + 1}', int(input(f'Gols feitos no jogo {x + 1}: '))])
dicionario['gols'] = lista
print(f'Aproveitamento de {dicionario["nome_jogador"]}')
print(f'O jogador jogou {dicionario["partidas"]} partidas.')
for item in dicionario['gols']:
    print(f'{item[0]}: {item[1]} gols')