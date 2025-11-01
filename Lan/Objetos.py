class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.ligado = False
        self.gasolina = 100


    def ligar(self):
        if self.ligado:
            print(f'O {self.nome} já está ligado.')
        else:
            self.ligado = True
            print(f'O {self.nome} foi ligado.')


    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f'O {self.nome} foi desligado.')
        else:
            print(f'O {self.nome} já está desligado desligado.')


    def andar(self):
        if self.gasolina < 10:
            print(f'O {self.nome} está sem combustível e precisa abastecer.\n Painel de combustível: {self.gasolina} litros restantes.')
        elif not self.ligado:
            print(f'Para andar, o {self.nome} precisa estar ligado.')
        else:
            self.gasolina -= 10
            print(f'O {self.nome} andou e gastou 10 litros de gasolina.')
            print(f'Painel de combustível: {self.gasolina} litros restantes.')


    def abastecer(self):
        if self.ligado:
            print(f'Para abastecer o {self.nome} precisa estar desligado.')
        elif self.gasolina >= 100:
            print(f'O tanque de combustível está cheio.')
        else:
            self.gasolina += 10
            print(f'O {self.nome} abasteceu +10 litros de gasolina.')
            print(f'Painel de combustível: {self.gasolina} litros.')


print('-------------- Jogo do carro --------------')
carro = Carro(input('Qual o nome do seu carro? '))
print(f'Você entrou na garagem, {carro.nome} estava te esperando ;)')
print('-------------------------------------------')
while True:
    print('\nAções disponíveis: Ligar, Desligar, Andar, Abastecer e Sair')
    acao = input('Digite sua ação: ').strip().lower()
    if acao in 'ligar':
        carro.ligar()
    elif acao in 'desligar':
        carro.desligar()
    elif acao in 'andar':
        carro.andar()
    elif acao in 'abastecer':
        carro.abastecer()
    elif acao in 'sair':
        print(f'Guardando {carro.nome} na garagem. Obrigado por jogar.')
        break
    else:
        print('Ação inválida, tente novamente.')
        continue

