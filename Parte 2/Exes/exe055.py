#  leia o peso de 5 pessoas e diga qual o maior e o menor peso

print('Gráfico de pesos')
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Peso da {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'Analisando os dados: ')
print(f'O maior peso foi de: {maior}')
print(f'e o menor peso foi de: {menor}')
