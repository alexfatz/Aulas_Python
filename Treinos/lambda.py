from collections.abc import Callable

"""
syntax -> lambda argumentos: expressão

curiosidade: para tipar em lambda, usamos from collections.abc import Callable e então aplicamos: Callable[[int], int]
"""

soma: Callable[[int, int], int] = lambda x, y: x + y
print(soma(1, 2))

## exemplo real
materias: dict[str, float] = {
    "portugues": 8.5,
    "matematica": 9.5,
    "ingles": 8.0,
    "historia": 7.5,
    "geografia": 9.0,
    "fisica": 8.5
}

materias_organizadas: dict[str, float] = sorted(materias.items(), key=lambda materia: materia[1], reverse=True)
"""
materia[1] -> pega o valor em vez da key
reverse -> começar do maior em vez do menor
"""
print(materias_organizadas)
