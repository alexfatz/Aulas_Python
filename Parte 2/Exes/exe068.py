from random import randint
computador = randint(0, 9)
vitoria = True
cont = soma = 0

while vitoria:
    jogada = int(input('Digite um número: '))
    print('Computador: "Também estou fazendo minha jogada..."')
    escolha = input('Par ou Impar? ').lower()
    if (jogada + computador) % 2 == 0 and escolha in 'par':
        cont += 1
        soma += 1
        print('Você venceu!')
        print(f'Você jogou {jogada} e escolheu {escolha.title()}')
        print(f'O Computador jogou {computador}')
    elif (jogada + computador) % 2 != 0 and escolha in 'impar':
        cont += 1
        soma += 1
        print('Você venceu!')
        print(f'Você jogou {jogada} e escolheu {escolha.title()}')
        print(f'O Computador jogou {computador}')
    else:
        cont += 1
        print(f'Perdeu! Foram {cont} jogadas e {soma} vitorias!')
        print(f'Você jogou {jogada} e escolheu {escolha.title()}')
        print(f'O Computador jogou {computador}')
        vitoria = False
