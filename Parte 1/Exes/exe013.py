# algoritmo que leia salario de um funcionario com aumento de 15%
salario = float(input('Salário: R$'))
aumento = (salario * 0.15)

print(f'Analisando o salário de R${salario:.2f}, você receberá um aumento de R${aumento:.2f}!')
print(f'Seu novo salário agora passa a ser de R${salario + aumento:.2f}.')

