def leiaint(num):
    """
    Leia um caracter e descubra se é do tipo numérico.
    num: Número a ser analisado
    return: True ou False
    """
    verificar = num.isnumeric()
    if verificar:
        return True
    else:
        return False

numero = leiaint(input('Digite somente inteiros: '))
while numero is False:
    print('Inválido, tente novamente.')
    numero = leiaint(input('Digite somente inteiros: '))
print('Númerico!')