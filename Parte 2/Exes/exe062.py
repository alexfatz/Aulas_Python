#  melhore o exe061 perguntando se quer que mostre mais termos
#  termine o programa caso a resposta for 0

print('Progressão Aritmética!')
num = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
contador = 1
termo = num
mais = 10
total = 0

while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} > ', end='')
        contador += 1
        termo += razao
    print('Pausa...')
    mais = int(input('Mais quantos termos deseja ver? '))
print(f'Programa finalizado mostrando {total} termos.')
