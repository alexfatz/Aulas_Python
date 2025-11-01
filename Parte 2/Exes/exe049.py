#  refazer o desafio009 (tabuada) com laços

print('\033[34mTabuada reformulada! #  Remake desafio009\033[m')
num = int(input('Tabuada do número: '))
for tabuada in range (1, 11):
    print(f'{tabuada:2} X \033[33m{num:2}\033[m = \033[32m{tabuada * num:2}\033[m')
