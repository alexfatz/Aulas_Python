# algoritomo que calcule 2 notas e mostre sua média
num1 = float(input('Nota 1°Bimestre: '))
num2 = float(input('Nota 2°Bimestre: '))
num3 = float(input('Nota 3°Bimestre: '))
num4 = float(input('Nota 4°Bimestre: '))
print(f'A média entre os bimestres é: {(num1 + num2 + num3 + num4) / 4:.1f}.')

#algoritimo que calcule media ponderada de provas com pesos diferentes
peso1 = float(input('Quanto vale a 1° prova? '))
nota1 = float(input('Quanto você tirou nela? '))
peso2 = float(input('Quanto vale a 2° prova? '))
nota2 = float(input('Quanto você tirou nela? '))
peso3 = float(input('Quanto vale a 3° prova? '))
nota3 = float(input('Quanto você tirou nela? '))
peso4 = float(input('Quanto vale a 4° prova? '))
nota4 = float(input('Quanto você tirou nela? '))
calculo1 = (peso1 * nota1) + (peso2 * nota2) + (peso3 * nota3) + (peso4 * nota4)
resultado = calculo1 / (peso1 + peso2 + peso3 + peso4)

print(f'Analisando suas notas em todas as provas considerando seu valor, sua média foi de {resultado:.1f} ')
