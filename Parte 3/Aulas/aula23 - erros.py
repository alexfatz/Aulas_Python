try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a/b
except Exception as erro: # Se der errado
    print(f'Erro encontrado!\nTipo: {erro.__class__}\nNota: {erro}')
else: # Se deu certo
    print(f'O resultado é: {r}')
finally: # Independente se deu certo ou errado
    print('Volte sempre!')