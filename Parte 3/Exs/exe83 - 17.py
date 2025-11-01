conta = input('Escreva a conta: ')
contagem = 0
for caracter in conta:
    if caracter in '(':
        contagem += 1
    if caracter in ')':
        contagem -= 1

if contagem == 0:
    print('Conta correta.')
else:
    print('Conta errada.')