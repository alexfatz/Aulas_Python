# algoritimo que leia um numero real e mostre sua parte inteira
from math import trunc  # trunc > cortar a parte inteira do num

num = float(input('Digite um número real: '))
print(f'A parte inteira do número real {num} é {trunc(num)}.')
# ou
print(f'A parte inteira do número real {num} é {int(num)}.')
