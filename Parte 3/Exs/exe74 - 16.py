from random import randint

numeros = (randint(0,100), randint(0,100), randint(0,100))

print(f'Números sorteados:')
print(numeros)
print(f'Menor: {sorted(numeros)[0]}\nMaior: {sorted(numeros)[-1]}')