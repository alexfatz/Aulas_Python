# 87 no 86

# Tentando eficientizar o código:
lista = [[], [], []]
pares = []
soma = 0
for x in range(0,3):
    for y in range(0,3):
        lista[x].append(int(input(f'Item {y}:1: ')))

for x in range(0,3):
    for y in range(0,3):
        print(lista[x][y], end=' | ')

        if lista[x][y] % 2 == 0:
            pares.append(lista[x][y])
            soma += lista[x][y]
    print()
# 1 2 3
# 4 5 6
# 7 8 9
# Exercicio 87:

print(f'A soma dos números pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {lista[0][2] + lista[1][2] + lista[2][2]}')
print(f'O maior valor da segunda linha é: {max(lista[1])}')