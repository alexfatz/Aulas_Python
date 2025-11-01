dicionario = {}
lista = []
gols = []

while True:
    dicionario['nome'] = input('Nome do jogador: ')
    dicionario['jogos'] = int(input('Número de jogos: '))
    for x in range(0, dicionario['jogos']):
        gols.append(int(input(f'Gols na partida {x + 1}: ')))
    dicionario['gols'] = gols.copy()
    lista.append(dicionario.copy())
    gols.clear()

    continuar = input('Continuar? [S/N]')
    if continuar in 'Nn':
        print('Finalizando...')
        break

for i, jogador in enumerate(lista):
    contagem_gols = 0
    for gol in jogador['gols']:
        contagem_gols += gol
    print(f'{i + 1} - {jogador['nome']} - {jogador['jogos']} jogos - {contagem_gols} gols')

while True:
    dados = int(input('Informe o número do jogador para detalhes: '))
    print(f'Detalhes de {lista[dados - 1]['nome']}')
    for x in range(0, lista[dados - 1]['jogos']):
        print(f'{x + 1}° partida: {lista[dados - 1]['gols'][x]} gols')
    continuar = input('Continuar? [S/N]')
    if continuar in 'Nn':
        print('Finalizando...')
        break