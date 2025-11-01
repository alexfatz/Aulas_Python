prox = ''
while prox in 'Ss':
    num = int(input('Digite um número: '))
    while num < 0:
        print('Um número negativo! Tente novamente...')
        num = int(input('Digite um número: '))
    for cont in range(1, 11):
        print(f'{num} x {cont:2} = {num * cont}')
    prox = input('Deseja continuar? [S/N]')
    while prox not in 'SsNn':
        prox = input('Deseja continuar? [S/N]')
print('Finalizando...')
