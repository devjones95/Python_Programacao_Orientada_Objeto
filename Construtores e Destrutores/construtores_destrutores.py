# o def __init__ é o nosso método construtor, método inicializador
class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # método de "destruição da classe, repare que ao executar o script, todos os métodos são executados e logo depois, removidos."
    def __del__(self):
        print('Removendo a instância da classe...')


def criar_cachorro():
    c = Cachorro('Zeus', 'Branco', False)
    print(c.nome)

criar_cachorro()


