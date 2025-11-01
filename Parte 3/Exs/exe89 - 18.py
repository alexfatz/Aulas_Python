alunos = []
print('Cadastro de alunos')
while True:
    alunos.append([str(input('Nome do aluno: ')), [float(input('Nota 1: ')), float(input('Nota 2: '))]])
    continuar = str(input('Continuar? [S/N]'))
    while continuar not in 'SsNn':
        print('Inválido, tente novamente.')
        continuar = str(input('Continuar? [S/N]'))
    if continuar in 'Nn':
        print('Finalizando...')
        break

for i, item in enumerate(alunos):
    print(i, '-', item[0], '-', f'Média: {(item[1][0] + item[1][1]) / 2:.1f}')

while True:
    aluno = (input('Digite "Sair" para fechar o programa.\nInforme o número do aluno para notas individuais: '))
    print(f'Notas de {alunos[int(aluno)][0]}:\nNota 1: {alunos[int(aluno)][1][0]}\nNota 2: {alunos[int(aluno)][1][1]}\nMédia: {(alunos[int(aluno)][1][0] + alunos[int(aluno)][1][1]) / 2:.1f}')
    if aluno.lower().strip() in 'sair':
        print('Finalizando...')
        break