# ler um número e escolher a base de conversão
# 1 = binario
# 2 = octal
# 3 = hexadecimal


print('\033[35mCONVERSOR DE NÚMEROS\033[m')

num = int((input('Diga um número inteiro: ')))
escolha = int(input('Escolha dentre as opções:\n'
                 '1 = Binário\n'
                 '2 = Octal\n'
                 '3 = Hexadecimal\n'    
                 'Escolha: '))

if escolha == 1:
    print(f'{num} em Binário é: {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} em Octal é: {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} em Hexadecimal é: {hex(num)[2:]}')
# [2:] = começar da terceira posição e ir até o final. (fatiamento)
else:
    print('Inválido.')