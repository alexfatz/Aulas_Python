#  leia 6 numeros inteiros e some-os desconsiderando os impares

print('Some números inteiros desconsiderando os impares!')
soma = 0
for n in range (1, 7):
    num = int(input('Digite aqui: '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos números pares é: \033[34m{soma}\033[m')