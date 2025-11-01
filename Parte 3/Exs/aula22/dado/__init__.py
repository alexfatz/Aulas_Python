from aula22.moedas import resumo

def dado(valor):
    while not valor.strip().isnumeric():
        print('Inválido! Somente valores númericos são aceitos.')
        dado(input('Digite novamente: R$'))
    return resumo(float(valor))