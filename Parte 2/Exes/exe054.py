#  leia o ano de nascimento de sete pessoas e dps diga quantas atingiram a maioridade e quantas ainda sao menores

from datetime import date

print('Maioridade e menoridade')
atual = date.today().year
maioridade = 0
menoridade = 0

for m in range(1, 8):
    anasc = int(input(f'Ano de nascimentoda {m}ª pessoa: '))
    if atual - anasc < 18:
        menoridade += 1
    else:
        maioridade += 1
print(f'Analisando os dados cadastrados:\n'
      f'{maioridade} pessoas são maiores de idade,\n'
      f'e {menoridade} são menores de idade.')
