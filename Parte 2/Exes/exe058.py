#  melhore o exe028
#  advinhe um número entre 0 a 10
#  fale quantas tentativas a pessoa precisou para acertar
#  retomando as aulas

from random import randint
computador = randint(0, 10)
acerto = False
tentativa = 0

print('Adivinhe o número que estou pensando entre 0 e 10!')
while not acerto:
    tentativa += 1
    jogador = int(input('Adivinhe: '))
    if jogador == computador:
        acerto = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez!')
        elif jogador > computador:
            print('Menos... tente mais uma vez!')
print(f'Você acertou com {tentativa} tentativas, parabéns!')
