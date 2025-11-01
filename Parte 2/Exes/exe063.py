#  leia um numero inteiro e mostra na tela os n primeiros elementos de uma sequencia de fibonacci
#  ex: 0 > 1 > 1 > 2 > 3 > 5 > 8
#  retomando estudos!

print('Sequência Fibonacci!')
num = int(input('Quantos termos você deseja ver? '))
t1 = 0
t2 = 1
contagem = 3
print(f'{t1} > {t2}', end='')
while contagem <= num:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    contagem += 1
print(' > Fim')
