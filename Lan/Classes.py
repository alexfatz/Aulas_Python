class Fruta:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def caracteristicas(self):
        return f'{self.nome} é do tipo {self.tipo}'

class Citrica(Fruta):
    def __init__(self, nome, tipo, cor):
        super().__init__(nome, tipo)
        self.cor = cor

    def resumo(self):
        return f'{super().caracteristicas()}, da cor {self.cor}'

fruta = Citrica('Laranja', 'Docinho diferente', 'Laranja')
print(fruta.resumo())

