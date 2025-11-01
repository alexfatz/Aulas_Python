def fatorial(numero, show=False):
    """
    Informe um número e saiba seu fatorial.
    numero: Número a ser fatorado.
    show: Saiba os detalhes da operação.
    """
    fat = numero
    for x in range(numero, 0, -1):
        if x != fat:
            fat *= x
        if show:
            print(x, end=' -> ')
    return f'Resultado final: {fat}'

print(fatorial(10, show=True))

