# simular um funcionamento de um caixa eletronico
# perguntar qual o valor a ser sacado e informar a quantidade de cedulas
# cedulas: 1, 10, 20 e 50

cedula = 50
totalcedulas = 0

print('Caixa eletrônico:')
dinheiro = int(input('Quanto deseja sacar? R$'))
total = dinheiro
while True:
    if total >= cedula:
        total -= cedula
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'Cédulas de {cedula}: {totalcedulas}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        elif total == 0:
            break
        totalcedulas = 0