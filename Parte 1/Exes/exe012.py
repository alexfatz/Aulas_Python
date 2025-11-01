# algoritimo que leia o preço de um item com desconto de 5%
preço = float(input('Digite o preço do item: R$'))
desconto = preço * 0.05

print(f'Analisando o valor de R${preço:.2f}, você recebeu R${desconto:.2f} de desconto!')
print(f'O preço atualizado com o desconto já aplicado é: R${preço - desconto:.2f}.')