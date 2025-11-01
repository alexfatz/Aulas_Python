lista = []

for x in range(0,5):
    x = int(input('Digite um número: '))
    lista.append(x)

print(f'Foram registrados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Lista decrescente: {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')