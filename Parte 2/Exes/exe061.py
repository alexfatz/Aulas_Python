#  refaça o exe051
#  retomando os estudos!

print('Progressão Aritmética!')
num = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
contador = 1
termo = num

while contador <= 10:
    print(f'{termo} > ', end='')
    contador += 1
    termo += razao
print('Fim')