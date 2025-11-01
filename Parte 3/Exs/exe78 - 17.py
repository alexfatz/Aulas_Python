lista = []
for x in range(0,5):
    x = input('Digite um número: ')
    while not x.isdigit():
        print('Inválido! Tente novamente.')
        x = input('Digite um número: ')
    x = int(x)
    lista.append(x)
print(f'Os números coletados foram: {lista}')
print(f'O maior é {max(lista)} na {lista.index(max(lista))}° posição')
print(f'O menor é {min(lista)} na {lista.index(min(lista))}° posição')

# Casos de números repetidos (mostrado no curso)
print('*'*50)
print(f'O maior é {max(lista)} nas posições: ', end='')
for index, numero in enumerate(lista):
    if numero == max(lista):
        print(f'{index}°', end=' ')
print() # Quebrar linha por conta do end
print(f'O menor é {min(lista)} nas posições: ', end='')
for index, numero in enumerate(lista):
    if numero == min(lista):
        print(f'{index}°', end=' ')