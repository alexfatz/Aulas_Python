# return e docstring
def minha_funcao(a:int, b:int):
    """
    Args:
        a (int): Primeiro valor
        b (int): Segundo valor
    Returns:
        A soma de {a} e {b}
    """
    return a + b

help(minha_funcao)

print(minha_funcao(5, 5))
variavel = minha_funcao(10, 10)
print(variavel)

# parametro opcionais
def somar(a=0, b=0, c=0):
    s = a+b+c
    print(s)
somar(3,2)