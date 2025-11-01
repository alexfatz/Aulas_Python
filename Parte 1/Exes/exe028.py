#  Resolução do vídeo
from random import randint
from time import sleep #esperar (em segundos)

computador = randint(0,5)
print('Irei pensar num número de 0 a 5, tente adivinhar!')
user = int(input('O número que pensei é: '))
print('Pensando...')
sleep(2) #esperando (em segundos)
if user == computador:
    print('Parabéns! Você acertou!')
else:
    print('Errou! Babão!\n'
          f'O número que pensei foi {computador}, não {user}')

#pense em um número de 0 a 5 e faça o usuário advinhar (TENTATIVA)
num = int(input('Adivinhe o número de 0 a 5: '))
print('Acertou!' if num == 4 else 'Errou! blaaaa')