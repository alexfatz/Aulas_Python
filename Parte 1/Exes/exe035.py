# leia 3 retas e diga se é possivel formar um retangulo
reta1 = float(input('Valor da 1° reta: '))
reta2 = float(input('Valor da 2° reta: '))
reta3 = float(input('Valor da 3° reta: '))

if (reta1 - reta2) < reta3 < (reta1 + reta2):
    print('Regra 1= Verdadeiro')
else:
    print('Regra 1= Falso\n'
          'Sendo assim, não é possivel formar um retângulo com os valores.')
if (reta1 - reta3) < reta2 < (reta1 + reta3):
    print('Regra 2= Verdadeiro')
else:
    print('Regra 2= Falsa\n'
          'Sendo assim, não é possivel formar um retângulo com os valores.')
if (reta2 - reta3) < reta1 < (reta2 + reta3):
    print('Regra 3= Verdadeiro')
else:
    print('Regra 3= Falsa\n'
          'Sendo assim, não é possivel formar um retângulo com os valores.')

# ou (Vídeo)

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os valores formam um triângulo!')
else:
    print('Os valores não formam um triângulo.')
