#  leia nome idade e sexo de 4 pessoas e mostre:
#  media de idade do grupo
#  nome do homem mais velho
#  quantas mulheres com menos de 21 anos

idades = 0
mediaidades = 0
idadevelho = 0
nomevelho = ''
fmenores = 0

print('Registro')
for pessoas in range(1, 5):
    print(f'{pessoas}° pessoa ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    mediaidades += idade
    if sexo == 'm' and pessoas == 1:
        idadevelho = idade
        nomevelho = nome
    if sexo == 'm' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo == 'f' and idade < 21:
        fmenores += 1
print(f'Analisando os dados cadastrados...')
print(f'A média entre as idades foi de {mediaidades / pessoas:.0f} anos.')
print(f'{nomevelho.title()} foi o homem mais velho registrado com {idadevelho} anos.')
print(f'{fmenores} mulheres foram registradas com menos de 21 anos.')
