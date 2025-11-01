lista = []
pares = []
impares = []

for x in range(0, 10):
    x = int(input('Digite um número: '))
    lista.append(x)
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
print(f'Lista completa: {lista}')
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')