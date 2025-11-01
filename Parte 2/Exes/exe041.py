# programa que leia a data de nascimento e informe se:
# até 9 anos = mirim
# até 14 anos = infantil
# até 19 anos = junior
# até 25 anos = sênior
# acima = master

from datetime import date

print('Classificação sob faixa etária')
atual = date.today().year  # ano atual
ano = int(input('Seu ano de nascimento: '))

print(f'Esse ano você faz {atual - ano} anos.')

if atual - ano <= 9:
    print('Classificação: \033[36mMirim\033[m')

elif atual - ano <= 14:
    print('Classificação: \033[33mInfantil\033[m')

elif atual - ano <= 19:
    print('Classificação: \033[35mJunior\033[m')

elif atual - ano <= 25:
    print('Classificação: \033[35mSênior\033[m')

else:
    print('Classificação: \033[31mMaster\033[m')
