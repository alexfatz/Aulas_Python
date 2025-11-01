# leia o peso e altura de uma pessoa e calcule seu IMC e mostre seu status:
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepreso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida

while True:
    print('\033[mCalculadora de IMC:\033[m')
    altura = float(input('Sua altura (m): '))
    peso = float(input('Seu peso (Kg): '))
    imc = peso / (altura * altura)
    print(f'Seu IMC é: {imc:.1f}')

    if imc < 18.5:
        print('\033[33mAbaixo do peso\033[m.')
    elif imc < 25:
        print('\033[32mPeso ideal\033[m.')
    elif imc < 30:
        print('\033[34mSobrepeso\033[m.')
    elif imc <= 40:
        print('\033[35mObesidade\033[m.')
    else:
        print('\033[31mObesidade mórbida\033[m.')

