# Versão otimizada no exercício 87
lista = [[], [], []]
pares = []
soma = 0
for x in range(0,3):
    lista[0].append(int(input(f'Item {x}:1: ')))
for x in range(0,3):
    lista[1].append(int(input(f'Item {x}:2: ')))
for x in range(0,3):
    lista[2].append(int(input(f'Item {x}:3: ')))

for item in lista[0]:
    print(item, end=' | ')
print()
for item in lista[1]:
    print(item, end=' | ')
print()
for item in lista[2]:
    print(item, end=' | ')
print()
# 1 2 3
# 4 5 6
# 7 8 9
# Exercicio 87:
for item in lista[0]:
    if item % 2 == 0:
        pares.append(item)
for item in lista[1]:
    if item % 2 == 0:
        pares.append(item)
for item in lista[2]:
    if item % 2 == 0:
        pares.append(item)
for par in pares:
    soma += par
print(f'A soma dos números pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {lista[0][2] + lista[1][2] + lista[2][2]}')
print(f'O maior valor da segunda linha é: {max(lista[1])}')
