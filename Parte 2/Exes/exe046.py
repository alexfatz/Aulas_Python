#  contagem regressiva para solta de fogos de artificio contando 1 segundo entre eles

from time import sleep

print('É VIRADA DE ANO NOVO MINHA GENTE! CONTANDO...')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('TEY TEY TEY TEY TEY, TEY TEY!')