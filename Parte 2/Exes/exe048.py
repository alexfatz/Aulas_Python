#  soma de todos os numeros impares entre 1 e 500, multiplos de 3

soma = 0
count = 0
for num in range (1, 501, 2):
    if num % 3 == 0:
        soma += num
        count += 1
print(f'Analisando todos os {count} números impares e multiplos de 3, temos a soma de {soma}')