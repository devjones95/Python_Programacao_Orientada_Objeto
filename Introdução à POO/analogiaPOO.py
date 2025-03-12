'''SE LIGA NA ANALOGIA QUE EU CRIEI PRA PODERMOS PRATICAR E ENTENDER MELHOR 
SOBRE A PROGRAMAÇÃO ORIENTADA À OBJETOS
USANDO COMO EXEMPLO UM EPISÓDIO DOS POWER RANGERS'''


# Vamos criar a classe Power Ranger e seus atributos
class PowerRanger:
    def __init__(self, nome, cor, zord, arma):
        self.nome = nome
        self.cor = cor
        self.zord = zord
        self.arma = arma

    # Agora os métodos, ou nesse caso, as "ações" dos Rangers
    def morfar(self):
        print(f'{self.nome} diz: Power Ranger {self.cor}, é hora de morfar!')
        print('Morfagem completa.')

    def invocarArma(self):
        print(f'{self.nome} invocou sua {self.arma}.')

    def chamarZord(self):
        print(f'{self.nome} chamou seu Zord {self.zord}.')
        print(f'Zord {self.zord}, atacar!!!')

    def megaZord(self):
        print('MegaZord, ativar!')
        print('Fusão completa.')

    def ataqueSupremo(self):
        print('MEGAZORD, ATAQUE SUPREMO!!!')
        print('O monstro foi derrotado, mais uma vez a cidade foi salva graças aos Power Rangers')

# Agora, vamos criar os objetos da classe Power Rangers, os objetos serão nossos Rangers
rangerRed = PowerRanger('Jason', 'vermelho', 'Tiranossauro', 'Espada')
rangerBlue = PowerRanger('Bob', 'azul', 'Tricerátopis', 'Adaga')
rangerBlack = PowerRanger('Zack', 'preto', 'Mastodonte', 'Machado')
rangerPink = PowerRanger('Kimberly', 'rosa', 'Pterodátil', 'Arco')
rangerYellow = PowerRanger('Trini', 'amarelo', 'Tigre', 'Bastão')

print()
print('A cidade está sendo atacada, precisamos dos Power Rangers!!!')
print()
print('É HORA DE MORFAR!!!')
print()

# A cidade está sendo atacada, precisamos chamar os objetos Power Rangers para defender:

rangerRed.morfar()
print()

rangerBlue.morfar()
print()

rangerBlack.morfar()
print()

rangerYellow.morfar()
print()

rangerPink.morfar()
print()

# De repente os Rangers começam a sentir dificuldades de enfrentar os inimigos, eles precisam de suas armas.
print('OS RANGERS ESTÃO COM DIFICULDADES, VAMOS INVOCAR SUAS ARMAS.')
print()


print(f'{rangerRed.nome} diz: Preciso da minha {rangerRed.arma}.')
rangerRed.invocarArma()
print()


print(f'{rangerBlue.nome} diz: Preciso da minha {rangerBlue.arma}.')
rangerBlue.invocarArma()
print()


print(f'{rangerBlack.nome} diz: Preciso do meu {rangerBlack.arma}.')
rangerBlack.invocarArma()
print()


print(f'{rangerYellow.nome} diz: Preciso do meu {rangerYellow.arma}.')
rangerYellow.invocarArma()
print()


print(f'{rangerPink.nome} diz: Preciso do meu {rangerPink.arma}.')
rangerPink.invocarArma()
print()


# O MONSTRO GIGANTE.
print('O MONSTRO GIGANTE APARECEU, PARA ENFRENTÁ-LO, OS RANGERS PRECISAM DE SEUS ZORDS...')

rangerRed.chamarZord()
print()

rangerBlue.chamarZord()
print()

rangerBlack.chamarZord()
print()

rangerYellow.chamarZord()
print()

rangerPink.chamarZord()
print()

# O ATO FINAL
print('Após uma árdua batalha contra o monstro gigante, os Zords parecem não conseguir derrotá-lo...')
print('É HORA DE FUNDIR OS ZORDS E MONTAR O MEGAZORD!!!')
print()

rangerRed.megaZord()
print()

# O ATAQUE SUPREMO

rangerRed.ataqueSupremo()







