# calcule o valor a ser pago considerando as condições:
# à vista (dinheiro/cheque): 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais: 20% de juros

print('Calcule prestações!')
valor = float(input('Digite o valor: R$'))
print('Deseja pagar como?')
met_pag = int(input('1 = À vista no dinheiro ou cheque. \033[34m(10% de desconto)\033[m\n'
                    '2 = À vista no cartão. \033[34m(5% de desconto)\033[m\n'
                    '3 = 2x no cartão.\n'
                    '4 = 3x ou mais. \033[34m(20% de juros)\033[m\n'
                    'Digite aqui: '))

if met_pag == 1:
    pagamento = valor - (valor * 0.1)
elif met_pag == 2:
    pagamento = valor - (valor * 0.005)
elif met_pag == 3:
    pagamento = valor
elif met_pag == 4:
    q_parcelas = int(input('Em quantas vezes? '))
    pagamento = valor + (valor * 0.2)
    print(f'Seu pagamento foi dividido em {q_parcelas} vezes de R$\033[32m{pagamento / q_parcelas:.2f}\033[m')
else:
    pagamento = 0
    print('\033[31mInválido\033[m, tente novamente.')
print(f'Valor: R$\033[32m{pagamento:.2f}\033[m')
