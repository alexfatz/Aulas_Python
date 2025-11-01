# \033[m
# colocar depois para não preencher linha inteira voltando ao padrão do terminal

print('\033[31mTeste\033[m')
print('\033[1;33;45mTeste\033[m')
print('\033[4;32;mTeste\033[m')
print('\033[7;30mTeste\033[m')

# aprenderemos mais pra frente:
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print(f'{cores["amarelo"]}Amarelo, {cores["azul"]}Azul, {cores["pretoebranco"]}Preto e Branco\033[m')
