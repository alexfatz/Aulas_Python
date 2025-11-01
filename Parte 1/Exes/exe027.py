# leia o nome de uma pessoa e diga o primeiro e ultimo nome
# tirar espaços antes e depois

nome = str(input('Digite seu nome completo: ')).strip()
nomes = nome.split()  # separar a string em partes
print(f'Seu primeiro nome é {nomes[0]} e seu ultimo nome é {nomes[-1]}.')
# -1 = ultimo
# -2 = penultimo
# ...
