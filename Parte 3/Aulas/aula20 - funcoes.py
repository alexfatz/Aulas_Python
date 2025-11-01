def soma (a, b):
    print(a + b)

# multiplos parametros 
def contador (*num):
    print(num)
    print(len(num))
    for numero in num:
        print(numero, end=' -> ')


soma(1, 5)
soma(b=10, a=2)

contador(1, 2, 3, 4, 5, 6)
