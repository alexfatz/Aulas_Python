# leia o valor dos catetos e descubra a hipotenusa de um triangulo retangulo
from math import hypot
# hypot > calcular a hipotenusa atraves dos catetos de um triangulo retangulo

co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
print(f'O valor da hipotenusa é: {hypot(co, ca):.2f}.')
# ou
hip = (co ** 2 + ca ** 2) ** 0.5
print(f'O valor da hipotenusa é: {hip:.2f}.')