def voto(ano_nascimento):
    """
    Informe o ano de nascimento e descubra se o voto é obrigatório.
    ano_nascimento: ano de nascimento
    """
    from datetime import datetime
    ano_atual = datetime.now().year
    if ano_atual - ano_nascimento < 18:
        return 'Não vota'
    elif ano_atual - ano_nascimento < 60:
        return 'Obrigatório'
    else:
        return 'Opcional'

ano_nascimento = int(input('Digite o ano: '))
help(voto)
print('Estado do voto:', voto(ano_nascimento))
