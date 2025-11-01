#  leia 2 valores e mostre um menu
#  somar, multiplicar, maior, novos números, parar programa
#  retomando os estudos!

print('Menuzinho para seus números! :D')
n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
escolha = 0

while escolha != 6:
    print('-*' * 15)
    escolha = int(input(
        'Escolha uma das opções:\n1 - Somar\n2 - Multiplicar\n3 - Dividir\n4 - Maior\n5 - Trocar números\n6 - Sair\nDigite aqui: '))
    if escolha == 1:
        print('-*' * 15)
        print(f'A soma de {n1} + {n2} é {n1 + n2}')
    elif escolha == 2:
        print('-*' * 15)
        print(f'A multiplação de {n1} x {n2} é {n1 * n2}')
    elif escolha == 3:
        print('-*' * 15)
        print(f'A divisão de {n1} / {n2} é {n1 / n2}')
    elif escolha == 4:
        if n1 > n2:
            maior = n1
            print('-*' * 15)
            print(f'O maior dentre {n1} e {n2} é {maior}')
        elif n1 == n2:
            print('-*' * 15)
            print(f'Os números {n1} e {n2} são iguais.')
        else:
            print('-*' * 15)
            print(f'O maior dentre {n1} e {n2} é {n2}')
    elif escolha == 5:
        print('-*' * 15)
        print('Informe os novos números: ')
        n1 = int(input('Escolha um número: '))
        n2 = int(input('Escolha outro número: '))
    elif escolha == 6:
        print('-*' * 15)
        print('Finalizando...')
    else:
        print('-*' * 15)
        print('Inválido! Tente novamente...')
print('-*' * 15)
print('Finalizado, volte sempre!')
