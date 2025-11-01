def metade(x, formatar=False):
    """Retorna a metade do valor"""
    if formatar:
        return f'{x/2:.2f}'
    x/2

def dobro(x, formatar=False):
    """Retorna o dobro do valor"""
    if formatar:
        return f'{x*2:.2f}'
    return x*2

def aumentar(x, formatar=False):
    """Retorna o total do valor + 15%"""
    if formatar:
        return f'{x + (x*0.15):.2f}'
    return x + (x*0.15)

def diminuir(x, formatar=False):
    """Retorna o total do valor - 10%"""
    if formatar:
        return f'{x - (x*0.1):.2f}'
    return x - (x*0.1)

def resumo(valor, aumento=0.15, desconto=0.10):
    """Informe o valor para resumo das outras funções"""
    resumo = (
        f'---------- Resumo do valor ----------\n'
        f'O dobro do valor é: R${dobro(valor, formatar=True)}\n'
        f'A metade do valor é: R${metade(valor, formatar=True)}\n'
        f'O aumento de 15% no valor é: R${valor + (valor*aumento):.2f}\n'
        f'O desconto de 10% no valor é: R${valor - (valor*desconto):.2f}\n'
    )
    return resumo