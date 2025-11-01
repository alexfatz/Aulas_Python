def area(a, b):
    area = a * b
    print(f'A altura é {a}, a largura é {b} e a área é {area:.1f}m².')


a = int(input('Digite o número da altura em métros: '))
b = int(input('Digite o número da largura em métros: '))
area(a, b)
