# leia dois numeros e informe qual é maior, menor ou se forem iguais

print('Compare números!')
num = float(input('Diga qualquer número: '))
num1 = float(input('Diga qualquer outro número: '))

if num > num1:
    print(f'Analisando os números {num} e {num1}...\n'
          f'{num} é o maior\n'
          f'{num1} é o menor')
elif num < num1:
    print(f'Analisando os números {num} e {num1}...\n'
          f'{num1} é o maior\n'
          f'{num} é o menor')
else:
    print(f'Analisando os números {num} e {num1}...\n'
          f'São iguais.')
