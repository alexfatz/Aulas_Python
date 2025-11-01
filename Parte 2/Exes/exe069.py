# ler idade e sexo de varias pessoas
# mostrar na tela: quantos de maior / quantos homens / quantas mulheres com menos de 20 anos

maiores = 0
homens = 0
mulheres_adultas = 0
sexo = ''
idade = 0
continuar = ''

while continuar in 'Ss':
    print('Registro de pessoas')
    sexo = input('Sexo: [M/F]')
    while sexo not in 'MmFf':
        print('Sexo inválido, tente novamente.')
        sexo = input('Sexo: [M/F]')
    idade = int(input('Idade: '))
    while idade < 1:
        print('Idade inválida, tente novamente.')
        idade = int(input('Idade: '))
    if sexo in 'Mm':
        homens += 1
    if idade >= 18:
        maiores += 1
    if sexo in 'Ff' and idade > 20:
        mulheres_adultas += 1
    continuar = input('Continuar? [S/N]')
    while continuar not in 'SsNn':
        print('Inválido, tente novamente.')
        continuar = input('Continuar? [S/N]')
print(f'Resultados:\nMaiores: {maiores}\nHomens: {homens}\nMulheres com mais de 20 anos: {mulheres_adultas}')