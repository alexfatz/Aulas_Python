#preço da passagem
#0.50 centavos/km caso for menor que 200 kilometros rodados
#0.45/km caso a viagem seja maior

dist = float(input('Diga a distância em km: '))
if dist>=200:
    print(f'A passagem de uma viagem de {dist}km é de R${dist * 0.45:.2f}')
else:
    print(f'A passagem de uma viagem de {dist}km é de R${dist * 0.50:.2f}')

#2° método (Vídeo)
distancia = float(input('Distância: '))
print(f'Você está prestes a fazer uma viagem de {distancia}KM')
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'Sua passagem custará R${preço:.2f}')