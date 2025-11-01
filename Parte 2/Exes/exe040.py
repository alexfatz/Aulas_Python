# calcule a media de um aluno e informe se foi reprovado, se esta de recuperação ou se foi aprovado

print('Análise do seu boletim escolar!')
bim1 = float(input('Média 1° Bimestre: '))
bim2 = float(input('Média 2° Bimestre: '))
bim3 = float(input('Média 3³ Bimestre: '))
bim4 = float(input('Média 4° Bimestre: '))
medtotal = (bim1 + bim2 + bim3 + bim4) / 4

if medtotal < 6:
    print(f'Média: \033[34m{medtotal}\033[m')
    print('\033[1;31mReprovado.\033[m')
elif 7.1 > medtotal > 5.9:
    print(f'Média: \033[34m{medtotal}\033[m')
    print('\033[1;33mRecuperação.\033[m')
else:
    print(f'Média: \033[34m{medtotal}\033[m')
    print('\033[1;32mAprovado.\033[m')
