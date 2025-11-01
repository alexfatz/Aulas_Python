def contador(inicio, fim, passo):
    if passo < 0:
        passo = +passo
    if passo == 0:
        passo = 1
    if fim < inicio:
        passo = -passo
    for x in range(inicio, fim, passo):
        print(x, end=' -> ')
    print('Fim')

contador(0, 10, 1)
contador(10, 0, -1)
print('Sua vez de fazer a sequência!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passos: '))
contador(inicio, fim, passo)
