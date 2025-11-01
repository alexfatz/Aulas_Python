dicionario = {}
lista = []
media_idade = 0

while True:
    dicionario['nome'] = input('Nome: ')
    dicionario['idade'] = int(input('Idade: '))
    dicionario['sexo'] = input('Sexo: [M/F]')
    lista.append(dicionario.copy())
    dicionario.clear()
    continuar = input('Continuar? [S/N]')
    if continuar in 'Nn':
        print('Finalizando...')
        break
print(f'{len(lista)} foram cadastradas.')

for item in lista:
    media_idade += item['idade']
media_idade = media_idade / len(lista)
print(f'A idade média é de {media_idade:.1f} anos.')
print(f'Mulheres registradas: ')
for item in lista:
    if item['sexo'] in 'Ff':
        print(item['nome'], end=', ')
print()
print(f'Pessoas com idade acima da média: ')
for item in lista:
    if item['idade'] > media_idade:
        print(f'{item['nome']}, {item['idade']} anos', end=', ')