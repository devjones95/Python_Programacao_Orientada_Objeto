class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        

class Mamifero(Animal):
    def __init__(self, nro_patas, cor_pelo):
        self.nro_patas = nro_patas
        self.cor_pelo = cor_pelo
        super().__init__(nro_patas) # chamamos a classe Pai
        

class Ave(Mamifero):
    def __init__(self, nro_patas, cor_bico):
        self.nro_patas = nro_patas
        self.cor_bico = cor_bico


class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    pass


gato = Gato(4, 'preto')

ornitorrinco = Ornitorrinco(2, 'vermelho')