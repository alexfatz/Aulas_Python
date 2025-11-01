#  leia varios numeros inteiros na tela
#  mostre a media entre todos
#  mostre qual o maior e o menor valor digitado
#  sempre pergunte se o usuario quer continuar
#  retomando estudos!

print('Análise entre números!')
escolha = 'S'
num = soma = contador = maior = menor = 0

while escolha in 'Ss':
    num = int(input('Digite um número: '))
    escolha = input('Deseja continuar? (S/N) ').upper().strip()[0]
    soma += num
    contador += 1
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(
    f'O maior número foi {maior} e o menor foi {menor}, a média entre os números foi de {soma / contador}')
