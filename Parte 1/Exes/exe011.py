print('A DIMENSÃO, A ÁREA E A QUANTIDADE DE TINTA PARA PINTAR SUA PAREDE!')
comprimento = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = comprimento * altura
# nota = para cada 2m², 1L de tinta

print(f'Sua parede tem as dimensões de {comprimento}x{altura} e sua área é de {area}m².')
print(f'Para pintar sua parede, será necessário {area / 2}L de tinta.')

