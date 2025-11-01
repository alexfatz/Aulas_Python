# leia a frase e diga quantas vezes aparece a letra 'a', que posição ela aparece
# pela primeira vez e ultima vez

frase = input('Digite uma frase: ')
print(f'A letra "a" aparece na frase {frase.count("a")} vezes.\n'
      f'A primeira se encontra no caracter {frase.find("a")}\n'
      f'A ultima se encontra no caracter {frase.rfind("a")}.')