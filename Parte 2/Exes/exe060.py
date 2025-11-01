#  leia um numero qualquer e mostre seu fatorial
#  ex: 5! = 5x4x3x2x1 = 120
#  retomando estudos!

# USANDO MODULOS
from math import factorial

print('Calculando Fatoriais usando módulos!')
num = int(input('Digite um número: '))
print('Calculando...')
print(f'{num}! = {factorial(num)}')

# SEM MODULOS
print('*-' * 15)
print('Calculando Fatoriais sem usar módulos!')
num2 = int(input('Digite um número: '))
contador = num2
f = 1
print('Calculando...')
print(f'{num2}! = ', end='')
while contador > 0:
    print(f'{contador}', 'x ' if contador > 1 else '= ', end= '')
    f *= contador
    contador -= 1
print(f)

# USANDO FOR
print('*-' * 15)
print('Calculando Fatoriais usando FOR!')
num3 = int(input('Digite um número: '))
f2 = 1
print('Calculando...')
print(f'{num3}! = ', end='')

for contador1 in range (num3, 0, -1):
    print(f'{contador1}', 'x ' if contador1 > 1 else '= ', end='')
    f2 *= contador1
print(f2)