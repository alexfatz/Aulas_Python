# listas = []
lista = ["Pizza", "Hamburguer", "Suco", "Pudim"]
lista[3] = "Sorvete"  # mutável # Pudim > Sorvete
lista.append("Cenoura")  # adiciona no lista da lista
lista.insert(2, "Batata")  # inserir no indice, um novo item
lista.pop()  # remover o ultimo item da lista
lista.pop(2)  # remover o indice da lista
del lista[0]  # remover o indice da lista
if "Pizza" in lista:
    lista.remove("Pizza")  # remover o item, fornecendo o item
lista.sort(reverse=True) # Organiza a lista e retorna None
print(lista)

# Atenção!
a = [1, 2, 3, 4 ,5]
b = a # Não é uma cópia e sim uma ligação, caso substitua um item em b, a lista a será afetada!
b = a[:] # Para fazer apenas uma cópia dos itens e não uma ligação