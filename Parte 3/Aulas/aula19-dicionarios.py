pessoa = {'nome': 'Alex', 'idade': 50, 'comida': 'Café'}
for key, value in pessoa.items():
    print(f'{key} recebe {value}')
print('-' * 30)
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
del pessoa['idade']
print(pessoa)
pessoa['comida'] = 'Pizza'
print(pessoa['comida'])
pessoa['jogo'] = 'God of War'
print(pessoa['jogo'])