import aula22.moedas

valor = float(input('Digite uma quantidade: R$'))
print(
    f'A metade do valor é: R${aula22.moedas.metade(valor)}\n'
    f'O dobro do valor é: R${aula22.moedas.dobro(valor)}\n'
    f'O aumento de 15% do valor é: R${aula22.moedas.aumentar(valor)}\n'
    f'O desconto de 10% do valor é: R${aula22.moedas.diminuir(valor)}\n'
)