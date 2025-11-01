def dados_jogador(nome, gols=0):
    """
    Insira os dados do jogador para gerar uma ficha.
    nome: Nome do jogador
    gols: Número de gols marcados na temporada
    """
    if len(nome) < 1:
        nome = 'Desconhecido'

    return f'Ficha do jogador\nNome: {nome}\nGols: {gols}'

nome = input('Nome do jogador: ')
gols = int(input('Número de gols na temporada: '))
print(dados_jogador(nome, gols))
