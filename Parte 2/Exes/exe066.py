cont = soma = 0
while True:
    num = int(input('[999 para parar]\nDigite um número:'))
    if num == 999:
        break  # interrompa
    else:
        cont += 1
        soma += num
print(f'{cont} números foram digitados, e a soma entre eles é {soma}')
print('Finalizando...')
