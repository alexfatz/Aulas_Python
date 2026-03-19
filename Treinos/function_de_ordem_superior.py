"""
funções de ordem superior se trata de funções que recebem outra função como parâmetro ou retornam uma outra função
"""

def aplicar_soma(function, *args) -> int | float:
    return function(*args)

def soma(*args) -> int | float:
    return sum(args)

print(aplicar_soma(soma, 1, 2, 3, 4))