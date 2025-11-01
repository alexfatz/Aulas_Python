# jogo jokenpô

from random import randint
from time import sleep

while True:
    print('Vamos jogar Jokenpô!')
    computer = randint(1, 3)
    jogada = int(input('Faça sua jogada!\n'
                       '1 = Pedra\n'
                       '2 = Papél\n'
                       '3 = Tesoura\n'
                       'Escolha: '))

    if computer == 1 and jogada == 2:
        computer = str('Pedra')
        jogada = str('Papél')
        print('Jo')
        sleep(1)
        print('ken')
        sleep(1)
        print('Pôôô!')
        print(f'Joguei: \033[33m{computer}\033[m\n'
              f'Você jogou: \033[34m{jogada}\033[m\n'
              f'\033[1;32mVocê venceu!\033[m')

    elif computer == 1 and jogada == 3:
        computer = str('Pedra')
        jogada = str('Tesoura')
        print('Jo')
        sleep(1)
        print('ken')
        sleep(1)
        print('Pôôô!')
        print(f'Joguei: \033[33m{computer}\033[m\n'
              f'Você jogou: \033[34m{jogada}\033[m\n'
              f'\033[1;31mVocê perdeu.\033[m')

    elif computer == 2 and jogada == 3:
        computer = str('Papél')
        jogada = str('Tesoura')
        print('Jo')
        sleep(1)
        print('ken')
        sleep(1)
        print('Pôôô!')
        print(f'Joguei: \033[33m{computer}\033[m\n'
              f'Você jogou: \033[34m{jogada}\033[m\n'
              f'\033[1;32mVocê venceu!\033[m')

    elif computer == 2 and jogada == 1:
        computer = str('Papél')
        jogada = str('Pedra')
        print('Jo')
        sleep(1)
        print('ken')
        sleep(1)
        print('Pôôô!')
        print(f'Joguei: \033[33m{computer}\033[m\n'
              f'Você jogou: \033[34m{jogada}\033[m\n'
              f'\033[1;31mVocê perdeu.\033[m')

    elif computer == 3 and jogada == 1:
        computer = str('Tesoura')
        jogada = str('Pedra')
        print('Jo')
        sleep(1)
        print('ken')
        sleep(1)
        print('Pôôô!')
        print(f'Joguei: \033[33m{computer}\033[m\n'
              f'Você jogou: \033[34m{jogada}\033[m\n'
              f'\033[1;32mVocê venceu!\033[m')

    elif computer == 3 and jogada == 2:
        computer = str('Tesoura')
        jogada = str('Papél')
        print('Jo')
        sleep(1)
        print('ken')
        sleep(1)
        print('Pôôô!')
        print(f'Joguei: \033[33m{computer}\033[m\n'
              f'Você jogou: \033[34m{jogada}\033[m\n'
              f'\033[1;31mVocê perdeu.\033[m')

    elif computer == jogada:
        if computer == 1 and jogada == 1:
            computer = str('Pedra')
            jogada = str('Pedra')
            print('Jo')
            sleep(1)
            print('ken')
            sleep(1)
            print('Pôôô!')
            print(f'Joguei: \033[33m{computer}\033[m\n'
              f'Você jogou: \033[34m{jogada}\033[m\n'
              f'\033[1;36mEmpate.\033[m')
        elif computer == 2 and jogada == 2:
            computer = str('Papél')
            jogada = str('Papél')
            print('Jo')
            sleep(1)
            print('ken')
            sleep(1)
            print('Pôôô!')
            print(f'Joguei: \033[33m{computer}\033[m\n'
                  f'Você jogou: \033[34m{jogada}\033[m\n'
                  f'\033[1;36mEmpate.\033[m')
        elif computer == 3 and jogada == 3:
            computer = str('Tesoura')
            jogada = str ('Tesoura')
            print('Jo')
            sleep(1)
            print('ken')
            sleep(1)
            print('Pôôô!')
            print(f'Joguei: \033[33m{computer}\033[m\n'
                  f'Você jogou: \033[34m{jogada}\033[m\n'
                  f'\033[1;36mEmpate.\033[m')
    else:
        print('\033[31mOpção inválida!\033[m tente novamente.')
