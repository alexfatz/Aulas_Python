print(81**(1/2))  # (1/2) descrobrir raiz quadrada
print(27**(1/3))  # (1/3) descobrir raiz cubica

num1 = int(input('Primeiro número? '))
num2 = int(input('Segundo número? '))
# {:.1f} casas decimais depois da virgula (f > float)
print(
    f'A soma é {num1 + num2}, a subtração é {num1 - num2} e a divisão é {num1 / num2:.1f}.')
print(
    f'Já a divisão inteira é {num1 // num2} e o resto da divisão é {num1 % num2}.')
print(f' A soma é \033[32m{num1 + num2}\033[m \n',  # \n > quebrar a linha
      f'A subtração é \033[32m{num1 - num2}\033[m \n',
      f'A divisão é \033[32m{num1 / num2:.1f}\033[m\n',
      f'A divisão inteira é \033[32m{num1 // num2}\033[m \n',
      f'O resto da divisão é \033[32m{num1 % num2}\033[m.')
