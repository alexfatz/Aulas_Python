palavras = ('Mataleao', 'Chaves', 'Madrugar', 'Stardew', 'Fazendinha')

for index in range(0, len(palavras)):
    print(f'\nVogais de {palavras[index]}: ', end='')
    for letra in palavras[index].lower():
        if letra in 'aeiou':
            print(f'{letra}', end='')