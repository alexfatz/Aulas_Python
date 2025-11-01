from aula22.moedas import *

valor = float(input('Digite uma quantidade: R$'))
print(
    f'A metade do valor é: R${metade(valor, formatar=True)}\n'
    f'O dobro do valor é: R${dobro(valor, formatar=True)}\n'
    f'O aumento de 15% do valor é: R${aumentar(valor, formatar=True)}\n'
    f'O desconto de 10% do valor é: R${diminuir(valor, formatar=True)}\n'
)