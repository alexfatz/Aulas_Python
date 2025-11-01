#leia um num e diga se é par ou impar
num = int(input('Diga um número: '))
numresto = num % 2
if numresto == 0:
    print(f'O número {num} é PAR!')
else:
    print(f'O número {num} é IMPAR!')

