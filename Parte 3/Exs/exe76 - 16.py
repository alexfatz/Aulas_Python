itens = ('Computador', 2500, 'Celular', 1200, 'Carro', 35000, 'Caneta', 8)
# print(
#     'LOJINHA\n',
#     f'Item: {itens[0]}, preço: {itens[1]}\n',
#     f'Item: {itens[2]}, preço: {itens[3]}\n',
#     f'Item: {itens[4]}, preço: {itens[5]}\n',
#     f'Item: {itens[6]}, preço: {itens[7]}'
# )

# Explicação do vídeo:

for index in range(0, len(itens)):
    if index % 2 == 0:
        print(itens[index], end=': ')
    else:
        print(f'R${itens[index]:.2f}')
