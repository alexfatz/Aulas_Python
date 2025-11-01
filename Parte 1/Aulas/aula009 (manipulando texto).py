frase = 'café é bom, se você gosta de café então você é uma boa pessoa.'

print(len(frase))  # len > comprimento > analise
print(frase[:31])  # fatiamento
print(frase.count('café'))  # contagem de caracteres
print(frase.count('café', 0, 31))  # contagem + fatiamento
print(frase.find('é'))  # contagem de caracteres até o caracter especifico
print('café' in frase)  # tem?
print(frase.replace('café', 'bom bom'))  # substituir
print(frase.upper())  # maiusc
print(frase.lower())  # minusc
print(frase.capitalize())  # somente a primeira letra maiusc
print(frase.title())  # maiusc todo começo de palavra
frase1 = '   café   '
print(frase1.strip())  # remover espaços inicio e fim do campo
print(frase1.rstrip())  # remove somente os ultimos espaços (r > right > direita)
# remove somente os primeiros espaços (l > left > esquerda)
print(frase1.lstrip())

frase2 = 'frase do split'

print(f'\033[33m{frase2.split()}\033[m')  # divisão dentro da string (ex > 01234  01  01234)
# cada palavra vira uma nova lista
print(f'\033[33m{"-".join(frase2)}\033[m') # separação das palavras
