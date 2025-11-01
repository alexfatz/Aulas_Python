# leia 3 numeros e fale o menor e o maior
num = float(input('Diga um número: '))
num1 = float(input('Diga outro número: '))
num2 = float(input('Diga um terceiro número: '))

if num > num1 > num2:
    print(f'O maior dentre os três é: {num}\n'
          f'e o menor é: {num2}')
if num > num2 > num1:
    print(f'O maior dentre os três é: {num}\n'
          f'e o menor é: {num1}')
if num1 > num > num2:
    print(f'O maior dentre os três é: {num1}\n'
          f'e o menor é: {num2}')
if num1 > num2 > num:
    print(f'O maior dentre os três é: {num1}\n'
          f'e o menor é: {num}')
if num2 > num > num1:
    print(f'O maior dentre os três é: {num2}\n'
          f'e o menor é: {num1}')
if num2 > num1 > num:
    print(f'O maior dentre os três é: {num2}\n'
          f'e o menor é: {num}')
    
# ou

maior = num
if num1 > num and num1 > num2:
    maior = num1
if num2 > num and num2 > num1:
    maior = num2
print(f'O número maior foi: {maior}')

menor = num
if num1 < num and num1 < num2:
    menor = num1
if num2 < num and num2 < num1:
    menor = num2
print(f'O menor número foi: {menor}')


