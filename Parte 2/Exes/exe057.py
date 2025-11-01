#  leia o sexo de pessoas [M/F] e caso esteja errado, peça que digite novamente
#  retomando as aulas

print('Registro de Sexos')
# [0] pegando somente a primeira letra, ex: [F]eminino
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(
        input('Dados inválidos! Informe seu sexo [M/F]: ')).strip().upper()[0]
if sexo in 'M':
    print(f'Sexo masculino registrado com sucesso!')
else:
    print(f'Sexo feminino registrado com sucesso!')
