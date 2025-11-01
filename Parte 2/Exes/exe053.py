#  leia uma frase e diga se ela e um palindromo, desconsiderando os espaços
#  exemplo: apos a sopa é igual de tras pra frente e de frente pra tras

print('Descubra se a frase é um palindromo!')
frase = input('Digite a frase aqui (desconsidere acentuações): ')

if frase.replace(" ", "").strip().lower() == frase[::-1].replace(" ", "").strip().lower():
    print(f'A frase inversa é: "{frase[::-1]}"\n'
          f'sendo assim a frase é um palindromo.')
else:
    print(f'A frase inversa é: "{frase[::-1]}"\n'
          f'sendo assim a frase não é um palindromo.')

#########################################################################################
###               REFAZENDO COM A ESTRUTURA DE REPETIÇÃO "FOR"                        ###
###  para separar as palavras tb posso utilizar o frase.split()                       ###
###  então para alterar a separação ou tira-la posso usar tb 'separação'.join(frase)  ###
#########################################################################################

palavras = frase.lower().split()
junto = ''.join(palavras)
inverso = ''

for letras in range(len(junto) - 1, -1, -1):  # com len separo os caracteres da str, -1 pois vai de 0 até o ultimo caracter da frase
    inverso += junto[letras]
if junto == inverso:
    print(f'A frase é um palindromo.')
else:
    print(f'A frase não é um palindromo.')
print(f'inverso fica: {inverso}')