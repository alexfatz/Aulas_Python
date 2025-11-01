lista = []
continuar = ''
while continuar in 'Ss':
    x = input('Digite um número: ')
    while not x.isnumeric():
        print('Inválido! Tente novamente.')
    x = int(x)
    if x in lista:
        print('Numéro já registrado.')
    else:
        lista.append(x)
        print('Número registrado.')
    continuar = input('Deseja continuar? [S/N]')
    while continuar not in 'SsNn':
        print('Inválido! Tente novamente.')
        continuar = input('Deseja continuar? [S/N]')
lista.sort()
print(f'Números registrados: {lista}')