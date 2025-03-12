class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando o motor...')

# Essas 3 classes são filhas da classe Veiculo, e herdam todos os atributos da classe pai
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass


moto = Motocicleta('preta', 'ABC-1234', 2) # repare que o objeto moto herda os atributos da classe pai
moto.ligar_motor() # inclusive podemos atribuir métodos da classe pai para as classes herdeiras

carro = Carro('branco', 'XDE-0098', 4)
carro.ligar_motor()

caminhao = Caminhao('roxo', 'GFD-8712', 8)
caminhao.ligar_motor()