# aumento no salario
# superior a 1250, calcule 10%
# igual ou inferior, calcule 15%

salario = float(input('Salário: R$'))

if salario > 1250:
    aumento = (salario * 0.10 + salario)
else:
    aumento = (salario * 0.15 + salario)

print(f'Você ganhava R${salario:.2f}, e agora passa a ganhar R${aumento:.2f}')
