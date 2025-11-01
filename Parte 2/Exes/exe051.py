#  leia o primeiro termo e a razao de uma PA #  mostre os 10 primeiros termos dessa progressao

print('Progressão Aritmética!')
primeiro = int(input('Partiremos de qual número? '))
razao = int(input('Pulando de quantos em quantos? '))
décimo = primeiro + (10 - 1) * razao  # formula

for pa in range (primeiro, décimo + razao, razao):
    print(pa)
#  corrigido!