dicionario = {}
dicionario['nome'] = input('Nome do aluno: ')
dicionario['nota'] = float(input('Média do aluno: '))
if dicionario['nota'] < 6:
    dicionario['estado'] = 'Reprovado'
else:
    dicionario['estado'] = 'Aprovado'
print(f'Informações do aluno: {dicionario['nome']}\nMédia: {dicionario['nota']:.1f}\nEstado: {dicionario["estado"]}')