"""
closures -> funções internas que guardam informações de outras funções de escopo externo
"""


def criar_multiplicador(x: int) -> int:
    def multiplicar(y: int) -> int:
        return x * y

    return multiplicar

duplicar: int = criar_multiplicador(2)
print(duplicar(5)) # guarda o parametro anterior e inicia o processo de multiplicar


"""
nonlocal -> modificar variavel em função de escopo externo dentro de uma função interna
"""
def agregador() -> int:
    num: int = 0

    def agregar() -> int:
        nonlocal num
        num += 1

        return num
        
    return agregar


numero_agregado: int = agregador()

print(numero_agregado())
print(numero_agregado())
print(numero_agregado())