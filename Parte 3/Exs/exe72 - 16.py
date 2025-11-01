numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

while True:
    escolha = int(input('Diga um número de 0 até 10: '))
    while escolha < 0 or escolha > 10:
        print('Inválido, tente novamente.')
        escolha = int(input('Diga um número de 0 até 10: '))
    if  0 <= escolha <= 10:
        print(f'Você escolheu: {numeros[escolha]}')