# fazer emprestimo de uma casa
# valor da casa / salario / anos de pagamento
# parcelas n podem exceder 30% do salario

print('Faça um empréstimo e compre sua casa agora mesmo!')
salario = float(input('Seu salário: R$'))
casa = float(input('Valor da casa: R$'))
anos = int(input('Em quantos anos planeja pagar? '))

if casa / (anos * 12) <= salario * 0.3:
    print(f'Empréstimo \033[32mconcedido\033[m!\n'
      f'A casa no valor de R$\033[34m{casa:.2f}\033[m será divida mensalmente em:\n'
      f'\033[34m{anos * 12}\033[m vezes de R$\033[33m{casa / (anos * 12):.2f}\033[m cada parcela.')
else:
    print(f'Empréstimo \033[31mnegado\033[m.\n'
      f'Cada parcela teria o custo de R$\033[33m{casa / (anos * 12):.2f}\033[m mensais,\n'
      f'analisando o salário atual, o mínimo recomendado é de R$\033[35m{salario * 0.3:.2f}\033[m')
