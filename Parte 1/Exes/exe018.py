# leia um angulo (radians > graus) e retorna o seno, cosseno e tangente
from math import sin,cos,tan,radians

ang = float(input('Informe o valor do ângulo: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print(f'Analisando o ângulo {ang}: \n'
      f'Seno: {seno:.2f} \n'
      f'Cosseno: {coss:.2f} \n'
      f'Tangente: {tang:.2f}.')