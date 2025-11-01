# pergunte a data de nascimento e informe quando a pessoa terá que se alistar ou se já se alistou
# diga quanto tempo falta e quanto tempo ja se passou

from datetime import date
atual = date.today().year
print('Alistamento Militar Obrigatório')
ano = int(input('Ano de nascimento: '))
idade = atual - ano

if idade < 18:
    print(f'Esse ano, você fará \033[33m{idade}\033[m anos.\n'
          f'Falta \033[33m{18 - idade}\033[m anos para seu alistamento.')
elif idade == 18:
    print(f'Esse ano, você fará \033[32m{idade}\033[m anos.\n'
          f'\033[32mEsse ano é seu alistamento!\033[m')
else:
    print(f'Esse ano, você fará \033[35m{idade}\033[m anos.\n'
          f'Esse ano completa \033[30m{idade - 18}\033[m anos desde seu alistamento.')
