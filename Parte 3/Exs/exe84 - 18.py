pessoas = []
pesados = []
leves = []
for pessoa in range(0, 5):
    pessoas.append([input("Digite o nome: "), float(input('Digite o peso: '))])
    if pessoas[pessoa][1] < 80:
        leves.append(pessoas[pessoa])
    else:
        pesados.append(pessoas[pessoa])
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'{len(pesados)} pessoas pesadas foram registradas:')
for pessoa in pesados:
    if pessoa:
        print(f'{pessoa[0]}, peso: {pessoa[1]}\n')
print(f'{len(leves)} pessoas leves foram registradas:')
for pessoa in leves:
    if pessoa:
        print(f'{pessoa[0]}, peso: {pessoa[1]}\n')