num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite último número: '))
numeros = (num, num2, num3)
if numeros.count(9) > 0:
    print(f'O número 9 aparece: {numeros.count(9)} vezes')
else:
    print(f'O número 9 não aparece.')
if 3 in numeros:
    print(f'O número 3 aparece na posição: {numeros.index(3)}')
else:
    print(f'O número 3 não aparece.')
print('Números pares:', end=' ')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' ')