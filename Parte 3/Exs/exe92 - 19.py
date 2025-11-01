from datetime import date

dicionario = {}

dicionario['nome'] = input("Digite o nome: ")
dicionario['ano_nascimento'] = int(input("Ano de nascimento: "))
dicionario['carteira_trabalho'] = int(input("Identificação: "))
if dicionario['carteira_trabalho'] > 0:
    dicionario['ano_contratacao'] = int(input("Ano de contratação: "))
    dicionario['salario'] = float(input("Salário: "))

agora = date.today()
idade = agora.year - dicionario['ano_nascimento']
if dicionario['carteira_trabalho'] > 0:
    tempo_empregado = agora.year - dicionario['ano_contratacao']
    tempo_aposentadoria = 0
    if tempo_empregado < 20:
        tempo_aposentadoria = tempo_empregado + (20 - tempo_empregado)
    else:
        tempo_aposentadoria = tempo_empregado

print(f'Dados de {dicionario["nome"]}')
print(f'Idade: {idade}')
print(f'Carteira de trabalho: {dicionario['carteira_trabalho'] if dicionario['carteira_trabalho'] > 0 else "Não possui"}')
if dicionario['carteira_trabalho'] > 0:
    print(f'Contratado(a) no ano: {dicionario["ano_contratacao"]}')
    print(f'Salário: {dicionario["salario"]}')
    print(f'Aposentadoria: Idade: {idade if tempo_empregado >= 20 else idade + tempo_aposentadoria} anos, Ano: {agora.year if tempo_empregado >= 20 else agora.year + tempo_aposentadoria}')