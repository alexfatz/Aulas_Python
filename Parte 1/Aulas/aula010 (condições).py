condição = int(input('Qual sua idade? '))

if condição <= 18:
    print('\033[35mNovo!\033[m')
else:
    print('\033[31mVelho!\033[m')
# ou
print('\033[35mNovo!\033[m'if condição <= 18 else '\033[31mVelho!\033[m')
# exemplo
nota = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
m = (nota+nota2) / 2
print(f'Sua média foi \033[33m{m}\033[m')
print('\033[32mParabéns!\033[m' if m >= 6 else '\033[31mHá de melhorar!\033[m')
