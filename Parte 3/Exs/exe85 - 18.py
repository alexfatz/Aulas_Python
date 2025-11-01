lista = [[], []]

for num in range(0, 10):
    num = int(input('Digite 10 números inteiros: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Lista de pares: {lista[0]}\nLista de impares: {lista[1]}')