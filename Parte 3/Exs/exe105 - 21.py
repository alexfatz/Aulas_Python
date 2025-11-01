def escola(*notas, situacao=False):
    """
    Informe as notas da turma para dados.

    notas: Notas de cada aluno.

    situacao: Estado de desempenho da turma.

    retorna -> dict('quantidade_notas', 'maior', 'menor', 'situacao')
    """
    dicionario = dict()
    lista_notas = list(notas)
    dicionario['quantidade_notas'] = len(lista_notas)
    dicionario['maior'] = max(lista_notas)
    dicionario['menor'] = min(lista_notas)
    media = 0
    for nota in lista_notas:
        media += nota
    dicionario['media'] = f'{media / len(lista_notas):.1f}'
    if situacao:
        if media >= 7:
            situacao = 'Bom'
        elif media >= 5:
            situacao = 'Regular'
        else:
            situacao = 'Ruim'

    return dicionario, situacao

dados = escola(8, 5.5, 4, 7, 8, 3.6, 6.8, situacao=True)

print('Dados da turma')
print('Notas cadastradas:', dados[0]['quantidade_notas'])
print('Maior nota:', dados[0]['maior'])
print('Menor nota:', dados[0]['menor'])
print('Média da turma:', dados[0]['media'])
if dados[1]:
    print('Estado de desempenho:', dados[1])