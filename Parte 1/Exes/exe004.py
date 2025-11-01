x = input('Digite algo: ')

# tipo primitivo str
print(f'O tipo primitivo é: \033[35m{type(x)}\033[m')

# apenas nums
print(f'\033[33m{x}\033[m, é um número? \033[31m{x.isnumeric()}\033[m')

# apenas letras
print(f'\033[33m{x}\033[m, é alfabético? \033[31m{x.isalpha()}\033[m')

# letra + num
print(f'\033[33m{x}\033[m, é alfanumérico? \033[31m{x.isalnum()}\033[m')

# maiusc
print(f'\033[33m{x}\033[m, está em maisculo? \033[31m{x.isupper()}\033[m')

# minusc
print(f'\033[33m{x}\033[m, está em minusculo? \033[31m{x.islower()}\033[m')

# maiusc + minusc
print(f'\033[33m{x}\033[m, está capitalizada? \033[31m{x.istitle()}\033[m')
