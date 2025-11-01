# se forma ou não um triangulo (desafio035), e diz qual tipo de triangulo é:
# equilátero: todos os lados iguais
# isósceles: dois lados iguais
# escaleno: todos os lados diferentes

print('\033[mDescubra se as retas formam um triângulo e o tipo do triângulo!\033[m')
valor1 = float(input('Comprimento reta 1: '))
valor2 = float(input('Comprimento reta 2: '))
valor3 = float(input('Comprimento reta 3: '))

if valor1 < valor2 + valor3 and valor2 < valor1 + valor3 and valor3 < valor1 + valor2:
    print('Triângulo formado!')
    if valor1 != valor2 != valor3 != valor1:  # atenção!
        tipo = str('Escaleno')
    elif valor1 == valor2 == valor3:
        tipo = str('Equilátero')
    else:
        tipo = str('Isósceles')
    print(f'Tipo: {tipo}.')
else:
    print('Não formou-se um triângulo.')
