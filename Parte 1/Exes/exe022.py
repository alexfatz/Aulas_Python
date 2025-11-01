# leia o nome de uma pessoa e mostre (o nome com todas as letras maiusc, todas minusc,
# letras ao todo sem considerar espaços e quantas letras tem o primeiro nome

nome = str(input('Qual seu nome completo? ')).strip()  # strip> cortar espaços antes e dps
print('Analisando seu nome...')
print(f'Seu nome em maiusculo: {nome.upper()}\n'
      f'Seu nome em minusculo: {nome.lower()}\n'
      f'Seu nome tem: {len(nome) - nome.count(" ")} letras.\n'  #contagem de caracterer - espaços
      f'Seu primeiro nome tem: {nome.find(" ")} letras.')  #contagem de caracteres até o primeiro espaço
# ou
separado = nome.split()
print(f'Seu primeiro nome tem: {len(separado[0])} letras.')