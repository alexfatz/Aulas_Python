#leia km, e diga se foi multado ou n
#nota = r$7,00 por km multado (CORRIGIDO)
velocidade = float(input('Qual a velocidade? '))
if velocidade > 80:
    print(f'Você excedeu o limite permitido, e pagará uma multa no valor de R${(velocidade - 80) * 7:.2f}')
print('Tenha um bom dia! Dirija com segurança!') #linha colada na parede (executada sempre)