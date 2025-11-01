# leia um numero de 0 a 9999 e mostre na tela sua casa milhar, centena, dezena e unidade

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Casa de milhar: {m}\n'
      f'Casa de centena: {c}\n'
      f'Casa de dezena: {d}\n'
      f'Casa de unidade: {u}.')