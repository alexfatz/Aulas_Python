from random import choice


def sortear(numeros):
    sorteados = list()
    for x in range(0,5):
        sorteados.append(choice(numeros))
    print('Números sorteados:', sorteados)

    def pares(sorteados):
        contador = 0
        for num in sorteados:
            if num % 2 == 0:
                contador += num
        print('Soma dos números pares sorteados:', contador)
    pares(sorteados)


num = list()

for x in range(0,10):
    num.append(int(input('Digite um número inteiro: ')))
sortear(num)