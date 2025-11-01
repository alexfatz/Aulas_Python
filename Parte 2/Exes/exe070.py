# ler nome e preço de varios produtos
# mostrar total gasto / quantos produtos + 1000$ / falar o produto mais barato no final

total = 0
produtos_caros = 0
barato = []
continuar = ''

while continuar in 'Ss':
    print('Registrar produtos:')
    nome = input('Nome do produto: ')
    preco = int(input('Preço: R$'))
    while preco < 1:
        print('Preço inválido, tente novamente usando números inteiros.')
        preco = int(input('Preço: R$'))
    total += preco
    if preco > 1000:
        produtos_caros += 1
    barato.append(nome)
    barato.append(preco)
    if preco < barato[1]:
        barato.clear()
        barato.append(nome)
        barato.append(preco)
    continuar = input('Continuar? [S/N]')
    while continuar not in 'SsNn':
        print('Inválido, tente novamente.')
        continuar = input('Continuar? [S/N]')
print(f'Resultado:\nTotal: R${total},00\nProdutos com preços maiores que R$1000,00: {produtos_caros}\nProduto mais barato: {barato[0]}, preço: R${barato[1]},00')