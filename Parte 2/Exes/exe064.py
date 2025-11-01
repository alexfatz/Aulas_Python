#  leia varios numeros inteiros pelo teclado
#  ordem de parada: 999
#  mostre quantos numeros foram digitados e a soma entre eles
#  desconsidere o flag (999)
#  retomando estudos!

print('Somaqui!')
num = soma = contador = 0  # metodo para todos receberem o msm valor
while num != 999:
    num = int(input('Digite um número (999 para parar): '))
    if num != 999:
        contador += 1
        soma += num
print(f'Você digitou {contador} números e a soma entre eles é: {soma}')
