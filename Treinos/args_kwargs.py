# ARGS E KWARGS

"""
args -> Argumentos não nomeados
kwargs -> Argumentos nomeados

args -> retorna tupla
kwargs -> retorna dicionário
"""


def somar(a: int | float, b: int | float, c: int | float) -> int | float:
    """
    Soma três números
    """
    return a + b + c


lista: list[dict[str, int | float]]= [
    {
        'a': 1,
        'b': 2,
        'c': 3
    },
    {
        'a': 4.5,
        'b': 5.6,
        'c': 6.8
    }
]

# for item in lista:
#     resultado: int | float = somar(**item)
#     resultado: int | float = somar(*item.values())
#     print(resultado)


"""
ordem de parâmetros em uma única função -> obrigatórios, *args, **kwargs
"""


def registro(nome: str, *args, **kwargs) -> None:
    return nome, args, kwargs


print(registro("luiz", 1, 2, 3, 4, idade="30", cargo="ADM"))