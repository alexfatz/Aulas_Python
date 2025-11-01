#  leia um numero inteiro e diga se ele é ou n um numero primo (divisivel por 1 ou ele mesmo)

print('É PRIMO OU NÃO É!?')  # corrigido
num = int(input('Diga o número: '))
cont = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mO número \033[34m{num}\033[m foi divisivel \033[33m{cont}\033[m vezes,', end=' ')
if cont == 2:
    print('sendo dele um número \033[32mPrimo\033[m.')
else:
    print('\033[31mnão\033[m sendo um número Primo.')

