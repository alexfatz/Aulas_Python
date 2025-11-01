n = 0
par = impar = 0  # sim, da pra fazer isso kk

print('Quantos pares e impares com WHILE!')

while n != 0:  # *enquanto* n for diferente de 0:
    n = int(input('Digite um valor: '))
    if n != 0:  # desconsiderando o 0
        if n % 2 == 0:  # considerando o 0
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares.')
