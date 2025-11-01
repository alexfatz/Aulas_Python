from random import randint
from time import sleep

jogos = []

quant_jogos = int(input('Quantos jogos você quer que eu gere? '))
for x in range(0,quant_jogos):
    jogos.append([randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100)])

for i, jogo in enumerate(jogos):
    sleep(2)
    print(f'Jogo {i + 1}: ')
    for num in jogo:
        print(num, end=' ')
    print()