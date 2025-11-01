# preço a pagar pelo tempo e km percorrido com o carro alugado
km = float(input('Quilômetros percorridos: ')) # R$0.15 por km
dia = float(input('Dias alugados: ')) # R$60 por dia
print(f'Total a pagar: R${km * 0.15 + dia * 60:.2f}.')