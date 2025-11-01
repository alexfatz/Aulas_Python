lista = []
for x in range(0,5):
    y = int(input('Digite um número: '))
    if x == 0 or y > lista[-1]:
        lista.append(y)
    else:
        index = 0
        while index < len(lista):
            if y <= lista[index]:
                lista.insert(index, y)
                break
            index += 1
print(lista)