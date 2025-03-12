'''
NOSSO PRIMEIRO PROGRAMA POO

João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.
Uma bicicleta pode: buzinar, parar e correr.
Adicione esses comportamentos.
'''

class Bicicleta:
   
    # depois criamos o método construtor
    def __init__(self, cor, modelo, ano, valor): 
        # características da classe
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # criando os métodos da classe, os métodos na POO são muito parecidos com as funções
    def buzinar(self):
        print('Plim plim')

    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada.')

    def correr(self):
        print('Vruuuuum')

# Criando o nosso objeto de classe Bicicleta    
bicicleta1 = Bicicleta('Vermelha', 'Caloi', 2024, 1600)
bicicleta2 = Bicicleta('Preta', 'Alphameq', 2025, 2300)

# Chamando os métodos
bicicleta1.correr()  
bicicleta1.buzinar() 
bicicleta1.parar()  

# Chamando as características do nosso objeto:
print(bicicleta1.cor, bicicleta1.modelo, bicicleta1.ano, bicicleta1.valor)
print(bicicleta2.cor, bicicleta2.modelo, bicicleta2.ano, bicicleta2.valor)

# Acessando os atributos de classe dos objetos

print(bicicleta2.cor) # preta
